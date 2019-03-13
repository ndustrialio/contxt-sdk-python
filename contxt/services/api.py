from typing import Dict, List, Optional, Set, Tuple

import pandas as pd
import requests
from jwt import decode
from requests import PreparedRequest, Response
from requests.auth import AuthBase
from requests.exceptions import HTTPError
from tabulate import tabulate

from contxt.utils import make_logger

logger = make_logger(__name__)

API_VERSION = 'v1'


class RequestAuth(AuthBase):

    def __init__(self, access_token: str) -> None:
        self.access_token = access_token

    def __call__(self, request: PreparedRequest):
        request.headers['Authorization'] = f'Bearer {self.access_token}'
        return request


class ApiClient:

    def __init__(self, access_token: str) -> None:
        self.access_token = access_token


class ApiService:
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

    def _log_response(self, response, *args, **kwargs):
        url = f"{response.url}/{response.request.body or ''}"
        t = response.elapsed.total_seconds()
        logger.debug(f"Called {response.request.method} {url} ({t} s)")

    def _process_response(self, response: Response):
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

    def _get_json(self, response: Response):
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
    __marker = object()
    creatable_fields = []
    updatable_fields = []

    def __init__(self, keys_to_ignore=None):
        # TODO: may want to following a naming pattern for ignored keys, like
        # prefixed with _ instead of explicitly declaring the ignored keys
        self._keys_to_ignore = {'_keys_to_ignore'} | set(keys_to_ignore or [])

    def get_dict(self, include=None, exclude=None):
        if include is not None and exclude is not None:
            raise KeyError("Cannot provide both include and exclude")
        if include is not None:
            keys = include
        elif exclude is not None:
            keys = set(self.__dict__.keys()) - set(exclude)
        else:
            keys = set(self.__dict__.keys()) - self._keys_to_ignore

        return {k: v for k, v in self.__dict__.items() if k in keys}

    def get_keys(self):
        return self.get_dict().keys()

    def get_values(self):
        return self.get_dict().values()

    def get_df(self):
        d = self.get_dict()
        return pd.DataFrame(data=d.values(), columns=d.keys())

    def post(self):
        """Get data for a post request"""
        return self.get_dict(include=self.creatable_fields)

    def put(self):
        """Get data for a put request"""
        return self.get_dict(include=self.updatable_fields)

    def __str__(self):
        d = self.get_dict()
        return tabulate([d.values()], headers=d.keys())


if __name__ == "__main__":
    print('Done')
