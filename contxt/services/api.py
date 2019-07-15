from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Optional, Tuple

from requests import PreparedRequest, Response, Session
from requests.auth import AuthBase
from requests.exceptions import HTTPError

from contxt.auth import Auth, TokenProvider
from contxt.utils import make_logger

logger = make_logger(__name__)


class BearerTokenAuth(AuthBase):
    """
    Bearer token to authorize requests.
    """

    def __init__(self, token_provider: TokenProvider) -> None:
        self.token_provider = token_provider

    def __call__(self, request: PreparedRequest) -> PreparedRequest:
        request.headers["Authorization"] = f"Bearer {self.token_provider.access_token}"
        return request


class Api:
    """
    An API with url `base_url`.

    If `token_provider` is specified, all requests will be authenticated with
    the access token it provides.
    """

    def __init__(
        self, base_url: str, token_provider: Optional[TokenProvider] = None
    ) -> None:
        self.base_url = base_url if base_url.endswith("/") else f"{base_url}/"
        # Initialize session
        self.session = Session()
        self.session.auth = BearerTokenAuth(token_provider) if token_provider else None
        self.session.hooks = {"response": self._log_response}

    def _url(self, uri: str) -> str:
        return f"{self.base_url}{uri}"

    def _log_response(self, response: Response, *args, **kwargs) -> None:
        t = response.elapsed.total_seconds()
        logger.debug(
            f"Called {response.request.method} {response.url} with body"
            f" {response.request.body} ({t} s)"
        )

    def _process_response(self, response: Response) -> Dict:
        try:
            # Raise any error
            response.raise_for_status()
        except HTTPError:
            # Catch the error, to log the response's message, and reraise
            # Try to decode the response as json, else fall back to raw text
            response_json = self._get_json(response)
            msg = response_json.get("message") or response_json or response.text
            logger.error(f"HTTP Error: {response.reason} - {msg}")
            raise

        # Return json, if any
        return self._get_json(response)

    def _get_json(self, response: Response) -> Dict:
        try:
            return response.json()
        except ValueError:
            return {}

    def get(self, uri: str, params: Optional[Dict] = None, **kwargs) -> Dict:
        """Sends a GET request"""
        response = self.session.get(url=self._url(uri), params=params, **kwargs)
        return self._process_response(response)

    def post(
        self,
        uri: str,
        data: Optional[Dict] = None,
        json: Optional[Dict] = None,
        **kwargs,
    ) -> Dict:
        """Sends a POST request"""
        response = self.session.post(url=self._url(uri), data=data, json=json, **kwargs)
        return self._process_response(response)

    def put(
        self,
        uri: str,
        data: Optional[Dict] = None,
        json: Optional[Dict] = None,
        **kwargs,
    ) -> Dict:
        """Sends a PUT request"""
        response = self.session.put(url=self._url(uri), data=data, json=json, **kwargs)
        return self._process_response(response)

    def delete(self, uri: str, **kwargs) -> Dict:
        """Sends a DELETE request"""
        response = self.session.delete(url=self._url(uri), **kwargs)
        return self._process_response(response)


@dataclass
class ApiEnvironment:
    """
    An environment for an API.

    Note `client_id` is only needed if authentication is required.
    """

    name: str
    base_url: str
    client_id: str


class ConfiguredApi(Api, ABC):
    """
    An `Api` configured for multiple environments, such as staging and production.
    Available environments are expressed by `_envs` and the desired environment is
    specified by its name `env`.

    Overload this class to implement `_envs`.
    """

    def __init__(self, env: str, auth: Optional[Auth] = None) -> None:
        # TODO: figure out a cleaner approach to environment selection
        api_env = self._get_env(env)
        self.env = env
        self.client_id = api_env.client_id
        token_provider = auth.get_token_provider(self.client_id) if auth else None
        super().__init__(base_url=api_env.base_url, token_provider=token_provider)

    @classmethod
    def _get_env(cls, name: str) -> ApiEnvironment:
        """Get environment with name `name`."""
        envs = {e.name: e for e in cls._envs}
        if name not in envs:
            raise KeyError(
                f"Invalid environment '{name}'. Choose from {list(envs.keys())}."
            )
        return envs[name]

    @property
    @classmethod
    @abstractmethod
    def _envs(cls) -> Tuple[ApiEnvironment, ...]:
        """Lists available environments."""
        pass
