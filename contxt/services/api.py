from abc import ABC
from typing import Dict, FrozenSet, Optional, Tuple, Union, List

from auth0.v3.authentication import GetToken
from requests import PreparedRequest, Response, Session
from requests.adapters import HTTPAdapter
from requests.auth import AuthBase
from requests.exceptions import HTTPError
from urllib3.util.retry import Retry

from ..auth import TokenProvider
from ..services.auth import StoredTokenCache
from ..utils import make_logger
from ..utils.config import ContxtEnvironmentConfig

logger = make_logger(__name__)

# NOTE: support breaking change in urllib3: https://github.com/urllib3/urllib3/issues/2092
RETRY_METHODS_PARM = (
    "allowed_methods" if hasattr(Retry.DEFAULT, "allowed_methods") else "method_whitelist"
)


class BearerTokenAuth(AuthBase):
    """Bearer token to authorize requests"""

    def __init__(self, token_provider: TokenProvider) -> None:
        self.token_provider = token_provider

    def __call__(self, request: PreparedRequest) -> PreparedRequest:
        request.headers["Authorization"] = f"Bearer {self.token_provider.access_token}"
        return request


class ApiRetry(Retry):
    def __init__(
        self,
        total: int = 3,
        backoff_factor: float = 0.1,
        method_whitelist: FrozenSet = frozenset(
            # NOTE: be careful as some of these methods are not idempotent
            ["DELETE", "GET", "OPTIONS", "POST", "PUT", "TRACE", "HEAD"]
        ),
        status_forcelist: Tuple[int, ...] = (500, 502, 504),
        raise_on_status: bool = False,
        **kwargs,
    ) -> None:
        kwargs[RETRY_METHODS_PARM] = method_whitelist
        super().__init__(
            total=total,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
            raise_on_status=raise_on_status,
            **kwargs,
        )


class Api:
    """An API with url `baseUrl`.

    If `token_provider` is specified, all requests will be authenticated with
    the access token it provides.
    """

    def __init__(
        self,
        base_url: str,
        token_provider: Optional[TokenProvider] = None,
        retry: Optional[ApiRetry] = ApiRetry(),
    ) -> None:
        self.base_url = base_url if base_url.endswith("/") else f"{base_url}/"

        # Initialize session
        self.session = Session()
        self.token_provider = token_provider
        self.session.auth = BearerTokenAuth(token_provider) if token_provider else None
        self.session.headers.update({"Cache-Control": "no-cache"})
        self.session.hooks = {"response": self._log_response}  # type: ignore

        # Attach retry adapter
        if retry:
            adapter = HTTPAdapter(max_retries=retry)
            self.session.mount("http://", adapter)
            self.session.mount("https://", adapter)

    def _url(self, uri: str) -> str:
        return f"{self.base_url}{uri}"

    def _log_response(self, response: Response, *args, **kwargs) -> None:
        t = response.elapsed.total_seconds()
        logger.debug(
            f"Called {response.request.method} {response.url} with body"  # type: ignore
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
            logger.debug(f"HTTP Error: {response.reason} - {msg}")
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

    def post(self, uri: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> Dict:
        """Sends a POST request"""
        response = self.session.post(url=self._url(uri), data=data, json=json, **kwargs)
        return self._process_response(response)

    def put(self, uri: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> Dict:
        """Sends a PUT request"""
        response = self.session.put(url=self._url(uri), data=data, json=json, **kwargs)
        return self._process_response(response)

    def delete(self, uri: str, **kwargs) -> Dict:
        """Sends a DELETE request"""
        response = self.session.delete(url=self._url(uri), **kwargs)
        return self._process_response(response)


class EnvironmentException(Exception):
    pass


class ConfiguredLegacyApi(Api, ABC):
    """An `Api` configured for multiple environments, such as staging and production.
    Available environments are expressed by `_envs` and the desired environment is
    specified by its name `env`.

    Overload this class to implement `_envs`.
    """

    def __init__(self, env_config: ContxtEnvironmentConfig, override_token_provider: TokenProvider = None, **kwargs) -> None:
        if override_token_provider:
            token_provider = override_token_provider
        elif env_config.clientId is None:
            from ..auth.cli import CliAuth
            cli_auth = CliAuth(service_config=env_config)
            token_provider = cli_auth.get_token_provider(audience=env_config.apiEnvironment.clientId)
        else:
            from ..auth.machine import PlainMachineTokenProvider
            token_provider = PlainMachineTokenProvider(env_config)
        super().__init__(base_url=env_config.apiEnvironment.baseUrl, token_provider=token_provider, **kwargs)


class ConfiguredGraphApi(Api, ABC):
    """An `Api` configured for multiple environments, such as staging and production.
    Available environments are expressed by `_envs` and the desired environment is
    specified by its name `env`.

    Overload this class to implement `_envs`.
    """

    def __init__(self, contxt_env: ContxtEnvironmentConfig, **kwargs) -> None:
        if contxt_env.clientId is None:
            from ..auth.cli import CliAuth

            cli_auth = CliAuth(service_config=contxt_env)
            token_provider = cli_auth.get_token_provider(audience=contxt_env.apiEnvironment.clientId)
        else:
            from ..auth.machine import PlainMachineTokenProvider

            token_provider = PlainMachineTokenProvider(contxt_env)

        super().__init__(base_url=contxt_env.apiEnvironment.baseUrl, token_provider=token_provider, **kwargs)


class AuthService(Api):
    """Auth API client"""

    def __init__(self, contxt_env: ContxtEnvironmentConfig) -> None:
        super().__init__(f'https://{contxt_env.apiEnvironment.authProvider}')
        self.service_env = contxt_env
        self.token_cache = StoredTokenCache()

    def get_jwks(self) -> Dict:
        return self.get(".well-known/jwks.json")

    def get_token(self, access_token: str, audiences: Union[str, List[str]]) -> Dict:
        audiences = [audiences] if isinstance(audiences, str) else audiences
        return self.post(
            "token", json={"audiences": audiences}, headers={"Authorization": f"Bearer {access_token}"}
        )

    def get_cluster_config(self, access_token: str, host: str) -> Dict:
        return self.post(
            "clusterconfig", headers={"Authorization": f"Bearer {access_token}"}, json={"host": host}
        )

    def get_oauth_token(self, client_id: str, client_secret: str, audience: str) -> str:
        cached_token = self.token_cache.get_token(client_id=self.service_env.clientId,
                                                  audience=self.service_env.apiEnvironment.clientId)
        if cached_token is None:
            logger.info('Token not found for client...fetching new one')
            req = GetToken(self.service_env.apiEnvironment.authProvider)
            token = req.client_credentials(client_id=self.service_env.clientId,
                                           client_secret=self.service_env.clientSecret,
                                           audience=self.service_env.apiEnvironment.clientId)
            self.token_cache.set_token(client_id=self.service_env.clientId,
                                       audience=self.service_env.apiEnvironment.clientId,
                                       token=token['access_token'])

            return token['access_token']
        else:
            logger.info('Using cached token')
            return cached_token
