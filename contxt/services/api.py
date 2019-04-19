from __future__ import annotations

from abc import ABC, abstractmethod
from ast import literal_eval
from datetime import date, datetime
from importlib import import_module
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union

import requests
from dateutil import parser
from jwt import decode
from pytz import UTC, ZERO
from requests import PreparedRequest, Response, Session
from requests.auth import AuthBase
from requests.exceptions import HTTPError

from contxt.utils import make_logger
from contxt.utils.serializer import Serializer

logger = make_logger(__name__)

API_VERSION = "v1"


def warn_of_unexpected_api_keys(cls, kwargs):
    # Warn of unexpected kwargs
    for k, v in kwargs.items():
        logger.warning(f"{cls.__name__}: Unexpected key from api {k}")
    # Warn of a present global (for asset service)
    if getattr(cls, "is_global", False):
        logger.warning(
            f"{cls.__name__}: received global (id {getattr(cls, 'id', None)}, label {getattr(cls, 'label', None)})"
        )


class Parsers:
    """
    Parsers needed to parse an API's response as the appropriate Python object
    """

    @staticmethod
    def parse_as_datetime(timestamp: str) -> datetime:
        return datetime.strptime(timestamp,
                                 "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=UTC)

    @staticmethod
    def parse_as_date(datestamp: str) -> date:
        return date.fromisoformat(datestamp)

    @staticmethod
    def parse_as_unknown(val: Any):
        # First, try a general parser (supports strings, numbers, tuples,
        # lists, dicts, booleans (True/False strings only), and None)
        try:
            return literal_eval(val)
        except (SyntaxError, ValueError) as e:
            pass
        # Next, fall back to a naive datetime parser
        try:
            return Parsers.parse_as_datetime(val)
        except (TypeError, ValueError) as e:
            pass
        # Next, fall back to a more powerful date/datetime parser
        # TODO: this works fine, but for a tz-aware datetime, it sets
        # tzinfo = tzutc(), not pytz.UTC, so equality checks will fail
        try:
            return parser.parse(val)
        except (TypeError, ValueError) as e:
            pass
        # Next, convert yes/no/true/false strings to bool
        try:
            if val.lower() in ("yes", "no"):
                return val.lower() == "yes"
            if val.lower() in ("true", "false"):
                return val.lower() == "true"
        except (AttributeError, TypeError, ValueError) as e:
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
        # Require timezone to be UTC
        if datetime_.utcoffset() != ZERO:
            raise AssertionError(
                f"Datetime must be UTC, not {datetime_.tzinfo}"
            )
        # NOTE: almost exactly the same as isoformat(), but ensures
        # microseconds are always represented
        return datetime_.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    @staticmethod
    def format_date(date_: date):
        return date_.isoformat()

    # Delay binding the functions to simple names to avoid overshadowing the datetime modules
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
    __marker = object()

    def __init__(self,
                 base_url: str,
                 access_token: str,
                 api_version: Optional[str] = __marker,
                 use_session: Optional[bool] = True):
        api_version = API_VERSION if api_version is self.__marker else api_version
        self.client = ApiClient(access_token)
        self.base_url = self._init_base_url(base_url, api_version)
        self.session = self._init_session() if use_session else None

    def _init_session(self):
        session = Session()
        session.auth = RequestAuth(self.client.access_token)
        session.hooks = {"response": self._log_response}
        return session

    def _init_base_url(self, base_url: str, api_version: str) -> str:
        return f"{base_url}/{api_version}" if api_version else base_url

    def _url(self, uri: str) -> str:
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
        t = response.elapsed.total_seconds()
        logger.debug(
            f"Called {response.request.method} {response.url} with body {response.request.body} ({t} s)"
        )

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

    def get(self,
            uri,
            params: Optional[Dict[str, str]] = None,
            records_only: Optional[bool] = True,
            **kwargs):
        if self.session:
            response = self.session.get(
                self._url(uri), params=params, **kwargs)
        else:
            # Merge default options with method options
            kwargs = {**self._request_kwargs(), **(kwargs or {})}
            response = requests.get(self._url(uri), params=params, **kwargs)

        response_json = self._process_response(response)

        # Return just records, if requested and available
        records = response_json.get("records") if isinstance(
            response_json, dict) else None
        if records_only and records is not None:
            return records

        # Return entire response
        return response_json

    def post(self,
             uri: str,
             data: Optional[Dict] = None,
             json: Optional[Dict] = None,
             **kwargs):
        if self.session:
            response = self.session.post(
                self._url(uri), data=data, json=json, **kwargs)
        else:
            # Merge default options with method options
            kwargs = {**self._request_kwargs(), **(kwargs or {})}
            response = requests.post(
                self._url(uri), data=data, json=json, **kwargs)
        return self._process_response(response)

    def put(self,
            uri: str,
            data: Optional[Dict] = None,
            json: Optional[Dict] = None,
            **kwargs):
        if self.session:
            response = self.session.put(
                self._url(uri), data=data, json=json, **kwargs)
        else:
            # Merge default options with method options
            kwargs = {**self._request_kwargs(), **(kwargs or {})}
            response = requests.put(
                self._url(uri), data=data, json=json, **kwargs)
        return self._process_response(response)

    def delete(self, uri: str, **kwargs):
        if self.session:
            response = self.session.delete(self._url(uri), **kwargs)
        else:
            # Merge default options with method options
            kwargs = {**self._request_kwargs(), **(kwargs or {})}
            response = requests.delete(self._url(uri), **kwargs)
        return self._process_response(response)


class ApiServiceConfig:
    """
    A configuration to specify the API's name, url, and audience
    """

    def __init__(self, name: str, base_url: str, audience: str):
        self.name = name
        self.base_url = base_url
        self.audience = audience


# TODO: we should automatically refresh the access token here
class ConfiguredApiService(ApiService, ABC):
    """
    An ApiService that has a list of configurations, selected by name
    """

    def __init__(self, auth, env: str, **kwargs):
        self.auth = auth
        self.config = self._init_config(env)
        super().__init__(
            base_url=self.config.base_url,
            access_token=auth.get_token_for_audience(self.config.audience),
            **kwargs)

    @property
    @abstractmethod
    def _configs(self):
        pass

    @classmethod
    def _init_configs_by_env(cls):
        if hasattr(cls, "_configs_by_env"):
            return
        cls._configs_by_env = {c.name: c for c in cls._configs}

    def _init_config(self, env: str):
        self._init_configs_by_env()
        if env not in self._configs_by_env:
            raise KeyError(
                f"Invalid environment '{env}'. Expected one of {', '.join(self._configs_by_env.keys())}."
            )
        return self._configs_by_env[env]


class ApiObject(ABC):
    """
    An abstract base class for a response from an API. This class serves to
    take a raw response from an API and create a parsed Python object.
    """
    _api_fields = NotImplemented

    def __init__(self):
        cls = self.__class__
        # Set creatable, updateable fields for class (if not yet set)
        # HACK: move this somewhere more appropriate
        if not hasattr(cls, "_creatable_fields"):
            cls._creatable_fields = {
                f.attr_key: f
                for f in cls._api_fields if f.creatable
            }
        if not hasattr(cls, "_updatable_fields"):
            cls._updatable_fields = {
                f.attr_key: f
                for f in cls._api_fields if f.updatable
            }

    def __str__(self):
        return Serializer.to_table(self)

    # @property
    # @classmethod
    # @abstractmethod
    # def _api_fields(cls):
    #     pass

    @classmethod
    def clean_api_value(cls, api_field: ApiField, api_value: Any):
        if api_value is None:
            # No value
            return api_value
        elif isinstance(api_value, (list, tuple,)):
            # Value is a list, clean each item
            return [cls.clean_api_value(api_field, v) for v in api_value]
        elif callable(getattr(api_field.data_type, "from_api", None)):
            # Type is an ApiObject, apply from_api instead of init
            return api_field.data_type.from_api(api_value)
        else:
            # Apply type
            return api_field.data_type(api_value)

    @classmethod
    def from_api(cls, api_dict: Dict):
        # Create clean dictionary to pass to init
        clean_dict = {
            f.attr_key: cls.clean_api_value(
                api_field=f,
                api_value=api_dict.pop(f.api_key, None)
                if f.optional else api_dict.pop(f.api_key))
            for f in cls._api_fields
        }

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
        """Get data for a POST request"""
        # Transform api fields to dict
        d = Serializer.to_dict(
            self, key_filter=lambda k: k in set(self._creatable_fields.keys()))
        # Swap attr_keys for api_keys
        return {self._creatable_fields[k].api_key: v for k, v in d.items()}

    def put(self):
        """Get data for a PUT request"""
        # Transform api fields to dict
        d = Serializer.to_dict(
            self, key_filter=lambda k: k in set(self._updatable_fields.keys()))
        # Swap attr_keys for api_keys
        return {self._updatable_fields[k].api_key: v for k, v in d.items()}


# TODO: Need a way to track changed attributes
# TODO: This custom schema-validation can be replaced by a more robust
# (although slower) implementation: see https://github.com/marshmallow-code/marshmallow
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
            data_type: Optional[Union[Callable, str]] = str,
            creatable: Optional[bool] = False,
            updatable: Optional[bool] = False,
            optional: Optional[bool] = False
    ):
        self.api_key = api_key
        self.attr_key = attr_key or api_key
        self._data_type = data_type
        self.creatable = creatable
        self.updatable = updatable
        self.optional = optional

    @property
    def data_type(self):
        if isinstance(self._data_type, str):
            # Load callable from str
            # NOTE: this is to delay the type assignment to instance creation,
            # as the type might not yet be defined at class creation
            modname, qualname_separator, qualname = self._data_type.partition(":")
            obj = import_module(modname)
            if qualname_separator:
                for attr in qualname.split("."):
                    obj = getattr(obj, attr)
            self._data_type = obj
        return self._data_type
