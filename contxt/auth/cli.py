from getpass import getpass
from json import dump, load
from pathlib import Path
from typing import Dict, Optional

from auth0.v3.authentication import GetToken

from contxt.auth import BaseAuth, DependentTokenProvider, TokenProvider
from contxt.services.auth import AuthService
from contxt.utils import make_logger

logger = make_logger(__name__, "debug")


class Auth0TokenProvider(TokenProvider):
    """
    Same as `TokenProvider`, but the access token provided is authenticated via
    username and password and granted for offline access, meaning expired tokens
    are refreshed with a refresh token. To do so, our own Auth API
    (i.e. `AuthService`) is replaced by Auth0's API.
    """

    def __init__(self, client_id: str, client_secret: str, audience: str):
        super().__init__(client_id, client_secret, audience)
        # Replace our auth api with auth0, and also store a refresh token
        self.auth_service = GetToken("ndustrial.auth0.com")
        self._refresh_token: Optional[str] = None

    def _get_new_access_token(self) -> str:
        token = self.login()
        self.refresh_token = token["refresh_token"]
        return token["access_token"]

    def _refresh_access_token(self) -> str:
        token = self.auth_service.refresh_token(
            self.client_id, self.client_secret, self.refresh_token
        )
        self.refresh_token = token["refresh_token"]
        return token["access_token"]

    @property
    def refresh_token(self) -> str:
        """Gets the refresh token"""
        if self._refresh_token is None:
            # Token not yet set, fetch it now
            self.access_token
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, value: str) -> None:
        """Sets the refresh token"""
        self._refresh_token = value

    def login(
        self, username: Optional[str] = None, password: Optional[str] = None
    ) -> Dict:
        """Returns an access_token from Auth0, from client `client_id` and
        `client_secret` for audience `audience`, with username `username` and
        password `password`"""
        return self.auth_service.login(
            client_id=self.client_id,
            client_secret=self.client_secret,
            username=username or input("Contxt Username: "),
            password=password or getpass("Contxt Password: "),
            scope="offline_access",
            audience=self.audience,
            grant_type="password",
            realm="",
        )


class CliAuth(BaseAuth):
    """
    Same as `BaseAuth`, but specifically for the client CLI. It uses
    `Auth0TokenProvider` to authenticate requests to get an access token for
    target clients defined by `audience`.

    If `enable_cache` is True, the access token from Auth0 will be cached in a
    JSON file in a hidden directory, meaning that the user will only have to
    authenticate with their credientials once.

    Auth Flow:
    1. User provides Contxt username/password credentials
    2. Retrieve access token directly from Auth0 for our `AuthService`, authenticating with
       above credientials
    3. When authenticating to a service, retrieve access token from our `AuthService`
       for the target service, authenticating with the above Auth0 access token
    """

    def __init__(self):
        super().__init__(
            client_id="bleED0RUwb7CJ9j7D48tqSiSZRZn29AV",
            client_secret="0s8VNQ26QrteS3H5KXIIPvkDcNL5PfT-_pWwAVNI4MpDaDg86O2XUH8lT19KLNiZ",
        )
        self.auth_service = AuthService()
        self.token_provider = Auth0TokenProvider(
            self.client_id, self.client_secret, self.auth_service.config.audience
        )

        # Initialize cache details
        self._cache_file = Path.home() / ".contxt_new" / "tokens_v2"
        self._cache = {}
        self._init_cache()

    def get_token_provider(self, audience: str) -> DependentTokenProvider:
        """Get `TokenProvider` for audience `audience`"""
        return DependentTokenProvider(self.token_provider, audience)

    def logged_in(self) -> bool:
        return self.token_provider.audience in self._cache

    def login(self) -> None:
        """Prompt the user to login"""
        pass
        # # Ensure we are in a logged out state
        # self.logout()
        # # Trigger a login prompt and update the cache
        # # NOTE: This works by fetching the access token
        # self._init_cache()

    def logout(self) -> None:
        """Logs the user out by clearing the cache"""
        # Clear the cached and current access_token
        self.token_provider._access_token = None
        self.clear_cache()

    def query_user(self, question: str) -> bool:
        """Query the user with `question`, and return if user confirmed"""
        choices = ("y", "n")
        # Get only the first character in the response
        answer = input(f"{question} ({'/'.join(choices)}) ").lower()[0:1]
        while answer not in choices:
            answer = input(f"Please enter {' or '.join(choices)}. ").lower()[0:1]
        return answer == "y"

    def _init_cache(self):
        # Load the cache
        self._cache = self.read_cache()

        # Only cache the auth0 access_token, so we do not have to repeatedly
        # query the user for their credentials
        if self.token_provider.audience in self._cache:
            # Token exists in cache, set it
            token_info = self._cache[self.token_provider.audience]
            self.token_provider.access_token = token_info["access_token"]
            self.token_provider.refresh_token = token_info["refresh_token"]
        else:
            # Token not in cache, update it
            # NOTE: this triggers a login prompt
            self._cache[self.token_provider.audience] = {
                "access_token": self.token_provider.access_token,
                "refresh_token": self.token_provider.refresh_token
            }
            self.update_cache()

    def read_cache(self) -> Dict:
        logger.debug(f"Reading tokens from {self._cache_file}")
        if self._cache_file.is_file():
            with self._cache_file.open("r") as f:
                return load(f)
        return {}

    def update_cache(self) -> None:
        logger.debug(f"Updating tokens from {self._cache_file}")
        self._cache_file.parent.mkdir(parents=True, exist_ok=True)
        with self._cache_file.open("w") as f:
            dump(self._cache, f, indent=4)

    def clear_cache(self) -> None:
        logger.debug(f"Clearing tokens from {self._cache_file}")
        self._cache_file.unlink()
        self._cache = {}
