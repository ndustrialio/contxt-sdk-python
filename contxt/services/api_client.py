import logging
from typing import Dict, List, Optional, Set, Tuple

import pandas as pd
import requests
from jwt import decode
from requests import PreparedRequest, Response
from requests.auth import AuthBase
from requests.exceptions import HTTPError
from tabulate import tabulate

from contxt.utils import make_logger

# from contxt.utils.auth import CLIAuth

logger = make_logger(__name__)
logger.setLevel(logging.DEBUG)

API_VERSION = 'v1'


class UnauthorizedException(Exception):
    pass


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

    def __init__(self,
                 base_url: str,
                 access_token: str,
                 api_version: str = API_VERSION) -> None:
        self.client = ApiClient(access_token)
        self.base_url = self._init_base_url(base_url, api_version)

    def _init_base_url(self, base_url: str, api_version: str) -> str:
        return f"{base_url}/{api_version}" if api_version else base_url

    def _request_kwargs(self):
        return {
            "auth": RequestAuth(self.client.access_token),
            # "timeout": 1,
            "hooks": {
                "response": self._log_response_url
            }
        }

    def _log_response_url(self, response, *args, **kwargs):
        url = f"{response.url}/{response.request.body}" if response.request.body else response.url
        logger.debug(f"Called {response.request.method} {url}")

    def _is_paged(self, response_json) -> bool:
        return "_metadata" in response_json

    def get_url(self, uri: str) -> str:
        return f"{self.base_url}/{uri}"

    def get_logged_in_user_id(self) -> str:
        # TODO do actual token verification
        decoded_token = decode(self.client.access_token, verify=False)
        return decoded_token['sub']

    def get(self, uri, params: Optional[Dict[str, str]] = None):
        response = requests.get(
            url=self.get_url(uri), params=params, **self._request_kwargs())
        response_json = self.process_response(response)

        # Check for paged response
        if self._is_paged(response_json):
            response_json = response_json["records"]

        return response_json

    def post(self, uri: str, data: Optional[dict] = None, json: Optional[dict] = None):
        response = requests.post(
            url=self.get_url(uri),
            data=data,
            json=json,
            **self._request_kwargs())
        return self.process_response(response)

    def put(self, uri: str, data=None):
        response = requests.put(
            url=self.get_url(uri), data=data, **self._request_kwargs())
        return self.process_response(response)

    def delete(self, uri: str):
        response = requests.delete(
            url=self.get_url(uri), **self._request_kwargs())
        return self.process_response(response)

    def process_response(self, response: Response):
        try:
            # Raise any error
            response.raise_for_status()
        except HTTPError as e:
            # Catch the error, to log the response's message, and reraise
            # Try to decode the response as json, else fall back to raw text
            response_json = self.get_json(response) or {}
            msg = response_json.get('message', None) or response_json or response.text
            logger.error(f"HTTP Error: {response.reason} - {msg}")
            raise

        return self.get_json(response)

    def get_json(self, response: Response):
        try:
            return response.json()
        except ValueError as e:
            logger.warning("No valid json object found")
            return None


class ApiObject:
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
