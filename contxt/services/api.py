from ast import literal_eval
from datetime import date, datetime
from typing import Callable, Dict, List, Optional, Set, Tuple

import requests
from jwt import decode
from pytz import UTC
from requests import PreparedRequest, Response
from requests.auth import AuthBase
from requests.exceptions import HTTPError

from contxt.utils import make_logger
from contxt.utils.serializer import Serializer

logger = make_logger(__name__)

API_VERSION = "v1"


def warn_of_unexpected_api_keys(cls, kwargs):
    # Warn of unexpected kwargs
    cls_name = cls.__class__.__name__
    for k, v in kwargs.items():
        logger.warning(f"{cls_name}: Unexpected key from api {k} = {v}")
    # Warn of a present global
    # if hasattr(cls_, "is_global") and cls_.is_global:
    #     logger.warning(
    #         f"{cls_name}: received global (id {cls_.id}, label {cls_.label})"
    #     )


class Parsers:
    """
    Parsers needed to parse an API's response as the appropriate Python object
    """

    @staticmethod
    def parse_as_datetime(timestamp) -> datetime:
        return datetime.strptime(timestamp,
                                 '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=UTC)

    @staticmethod
    def parse_as_date(date):
        return datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=UTC)

    @staticmethod
    def parse_as_unknown(val):
        # First, try a general parser (supports strings, numbers, tuples,
        # lists, dicts, booleans, and None)
        try:
            return literal_eval(val)
        except (SyntaxError, ValueError) as e:
            pass
        # Next, fall back to a date parser
        try:
            return Parsers.parse_as_datetime(val)
        except (TypeError, ValueError) as e:
            pass
        # Failed, return original value
        return val

    boolean = bool
    datetime = parse_as_datetime
    date = parse_as_date
    number = float
    string = str
    unknown = parse_as_unknown


class Formatters:
    """
    Formatters needed to format a parsed response back to json
    """

    @staticmethod
    def format_datetime(datetime_: datetime) -> str:
        return datetime_.isoformat().replace("+00:00", "Z")

    # TODO: change these as dates rather than datetimes
    @staticmethod
    def format_date(date_: date):
        return date_.isoformat().replace("+00:00", "Z")

    datetime = format_datetime
    date = format_date


class RequestAuth(AuthBase):
    """
    Authorization passed to requests (sets bearer access token in request header)
    """

    def __init__(self, access_token: str) -> None:
        self.access_token = access_token

    def __call__(self, request: PreparedRequest):
        request.headers['Authorization'] = f'Bearer {self.access_token}'
        return request


class ApiClient:

    def __init__(self, access_token: str) -> None:
        self.access_token = access_token


class ApiService:
    """
    A service associated with an API
    """

    configs_by_env = {
        'staging': dict(base_url=None, audience=None),
        'production': dict(base_url=None, audience=None)
    }

    def __init__(self,
                 base_url: str,
                 access_token: str,
                 api_version: str = API_VERSION) -> None:
        self.client = ApiClient(access_token)
        self.base_url = self._init_base_url(base_url, api_version)
        # TODO: we can speed up calls by using Request.Session object

    def _init_base_url(self, base_url: str, api_version: str) -> str:
        return f"{base_url}/{api_version}" if api_version else base_url

    def _get_url(self, uri: str) -> str:
        return f"{self.base_url}/{uri}"

    def _request_kwargs(self):
        return {
            "auth": RequestAuth(self.client.access_token),
            # "timeout": 1,
            "hooks": {
                "response": self._log_response
            }
        }

    def _log_response(self, response: Response, *args, **kwargs):
        url = f"{response.url}/{response.request.body or ''}"
        t = response.elapsed.total_seconds()
        logger.debug(f"Called {response.request.method} {url} ({t} s)")

    def _process_response(self, response: Response) -> Dict:
        # Handle any errors
        try:
            # Raise any error
            response.raise_for_status()
        except HTTPError as e:
            # Catch the error, to log the response's message, and reraise
            # Try to decode the response as json, else fall back to raw text
            response_json = self._get_json(response)
            msg = response_json.get('message') or response_json or response.text
            logger.error(f"HTTP Error: {response.reason} - {msg}")
            raise

        # Return json, if any
        return self._get_json(response)

    def _get_json(self, response: Response) -> Dict:
        try:
            return response.json()
        except ValueError as e:
            return {}

    def get_logged_in_user_id(self) -> str:
        # TODO do actual token verification
        decoded_token = decode(self.client.access_token, verify=False)
        return decoded_token['sub']

    def get(self, uri, params: Optional[Dict[str, str]] = None, records_only=True):
        response = requests.get(
            url=self._get_url(uri), params=params, **self._request_kwargs())
        response_json = self._process_response(response)

        # Return just records, if requested and available
        records = response_json.get("records") if isinstance(response_json, dict) else None
        if records_only and records is not None:
            return records

        # Return entire response
        return response_json

    def post(self, uri: str, data: Optional[dict] = None, json: Optional[dict] = None):
        response = requests.post(
            url=self._get_url(uri),
            data=data,
            json=json,
            **self._request_kwargs())
        return self._process_response(response)

    def put(self, uri: str, data=None):
        response = requests.put(
            url=self._get_url(uri), data=data, **self._request_kwargs())
        return self._process_response(response)

    def delete(self, uri: str):
        response = requests.delete(
            url=self._get_url(uri), **self._request_kwargs())
        return self._process_response(response)


class ApiObject:
    """
    An abstract base class for a response from an API. This class serves to
    take a raw response from an API and create a parsed Python object.
    """

    __marker = object()
    # creatable_fields = None
    # updatable_fields = None

    # def __init__(self):
    #     raise NotImplementedError

    def __str__(self):
        return Serializer.to_table(self)

    # @property
    # def api_fields(self):
    #     raise NotImplementedError

    @classmethod
    def clean_api_value(cls, api_field, api_value):
        if api_value is None:
            # No value
            return api_value
        elif callable(getattr(api_field.type, "from_api", None)):
            # Type is an ApiObject, apply from_api_dict instead of init
            return api_field.type.from_api(api_value)
        elif isinstance(api_value, (list, tuple,)):
            # Value is a list, clean each item
            return [cls.clean_api_value(api_field, v) for v in api_value]
        else:
            # Apply type
            return api_field.type(api_value)

    @classmethod
    def from_api(cls, api_dict: dict):
        # Create clean dictionary to pass to init
        clean_dict = {
            f.attr_key: cls.clean_api_value(
                api_field=f,
                api_value=api_dict.pop(f.api_key, None)
                if f.optional else api_dict.pop(f.api_key))
            for f in cls.api_fields
        }

        # Set creatable, updateable fields
        if not hasattr(cls, "_creatable_fields"):
            cls._creatable_fields = tuple(
                f for f in cls.api_fields if f.creatable)
        if not hasattr(cls, "_updatable_fields"):
            cls._updatable_fields = tuple(
                f for f in cls.api_fields if f.updatable)

        # Warn of any unused keys
        warn_of_unexpected_api_keys(cls, api_dict)

        # Return new instance
        return cls(**clean_dict)

    def get_dict(self):
        # TODO: deprecate, call Serializer directly
        return Serializer.to_dict(self)

    def get_df(self):
        # TODO: deprecate, call Serializer directly
        return Serializer.to_df(self)

    def post(self):
        """Get data for a post request"""
        return Serializer.to_dict(
            self,
            key_filter=lambda k: k in set(
                f.api_key for f in self._creatable_fields))

    def put(self):
        """Get data for a put request"""
        return Serializer.to_dict(
            self,
            key_filter=lambda k: k in set(
                f.api_key for f in self._updatable_fields))


# TODO: Need a way to track changed attributes
class ApiField:
    """
    A field retrieved from an API service.

    Contains the expected key, the desired class attribute key, the object type,
    and if it is a creatable or updatable field.
    """

    def __init__(
            self,
            api_key: str,
            attr_key: Optional[str] = None,
            type: Optional[Callable] = str,
            creatable: Optional[bool] = False,
            updatable: Optional[bool] = False,
            optional: Optional[bool] = False
    ):
        self.api_key = api_key
        self.attr_key = attr_key or api_key
        self.type = type
        self.creatable = creatable
        self.updatable = updatable
        self.optional = optional
