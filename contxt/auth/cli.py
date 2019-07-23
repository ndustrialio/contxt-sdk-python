from getpass import getpass
from json import dump, load
from pathlib import Path
from typing import Dict, Optional

from auth0.v3.authentication import GetToken

from contxt.auth import Auth, TokenProvider
from contxt.services.auth import AuthService
from contxt.utils import make_logger

logger = make_logger(__name__)


class UserIdentityProvider(TokenProvider):
    """
    Same as `TokenProvider`, but the access token provided is authenticated via
    username and password and granted for offline access, meaning expired tokens
    are refreshed with a refresh token. To do so, our own Auth API
    (i.e. `AuthService`) is replaced by Auth0's API.

    If `cache_file` is specified, both the `access_token` and `refresh_token`
    are cached there as a JSON blob.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        audience: str,
        cache_file: Optional[Path] = None,
    ):
        super().__init__(audience)
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_service = GetToken("ndustrial.auth0.com")
        self._refresh_token: Optional[str] = None

        # Initialize cache
        self._cache_file = cache_file
        self._init_from_cache()

    def _init_from_cache(self) -> None:
        if self._cache_file:
            # Load the cache
            cache = self.read_cache()

            if cache:
                # Token exists in cache, set it
                logger.debug(f"Setting token from cache")
                self.access_token = cache["access_token"]
                self.refresh_token = cache["refresh_token"]
            else:
                # Token not in cache
                logger.debug(f"Token not found in cache")

    @TokenProvider.access_token.getter
    def access_token(self) -> str:
        """Gets a valid access token for audience `audience`"""
        if self._access_token is None:
            # Token not yet set, fetch one
            logger.debug(f"Fetching new access_token for {self.audience}")
            token_info = self.login()
            self.access_token = token_info["access_token"]
            self.refresh_token = token_info["refresh_token"]
            # Update cache
            self.update_cache()
        elif self._token_expiring():
            # Token expiring soon, refresh it
            logger.debug(f"Refreshing access_token for {self.audience}")
            token_info = self.auth_service.refresh_token(
                self.client_id, self.client_secret, self.refresh_token
            )
            self.access_token = token_info["access_token"]
            # Update cache
            self.update_cache()
        return self._access_token

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

    def reset(self):
        super().reset()
        self._refresh_token: Optional[str] = None

    def read_cache(self) -> Dict:
        if self._cache_file:
            logger.debug(f"Reading cache {self._cache_file}")
            if self._cache_file.is_file():
                with self._cache_file.open("r") as f:
                    return load(f)
        return {}

    def update_cache(self) -> None:
        if self._cache_file:
            logger.debug(f"Updating cache {self._cache_file}")
            cache = {
                "access_token": self.access_token,
                "refresh_token": self.refresh_token,
            }
            self._cache_file.parent.mkdir(parents=True, exist_ok=True)
            with self._cache_file.open("w") as f:
                dump(cache, f, indent=4)

    def clear_cache(self) -> None:
        if self._cache_file:
            logger.debug(f"Clearing cache {self._cache_file}")
            if self._cache_file.is_file():
                self._cache_file.unlink()


class UserTokenProvider(TokenProvider):
    """
    Same as `TokenProvider`, but specifically for a human client. In this case,
    `identity_provider.access_token` serves as the identity provider for the client.
    """

    def __init__(self, identity_provider: UserIdentityProvider, audience: str):
        super().__init__(audience)
        self.identity_provider = identity_provider
        self.auth_service = AuthService()

    @TokenProvider.access_token.getter
    def access_token(self) -> str:
        """Gets a valid access token for audience `audience`"""
        if self._access_token is None or self._token_expiring():
            # Token either not yet set or expiring soon, fetch one
            logger.debug(f"Fetching new access_token for {self.audience}")
            self.access_token = self.auth_service.get_token(
                self.identity_provider.access_token, self.audience
            )["access_token"]
        return self._access_token


class CliAuth(Auth):
    """
    Same as `Auth`, but specifically for the client CLI. It uses
    `UserIdentityProvider` to authenticate requests to get an access token for
    target clients defined by `audience`.

    The access token from Auth0 is cached in a JSON file in a hidden directory,
    meaning that the user will only have to authenticate with their credientials
    once.

    Auth Flow:
    1. User provides Contxt username/password credentials
    2. Retrieve access token directly from Auth0 for our `AuthService`, authenticating
       with above credientials
    3. When authenticating to a service, retrieve access token from our `AuthService`
       for the target service, authenticating with the above Auth0 access token
    """

    def __init__(self):
        super().__init__(client_id="bleED0RUwb7CJ9j7D48tqSiSZRZn29AV", client_secret="")
        self.auth_service = AuthService()
        self.identity_provider = UserIdentityProvider(
            client_id=self.client_id,
            client_secret=self.client_secret,
            audience=self.auth_service.client_id,
            cache_file=Path.home() / ".contxt" / "cli_token",
        )

    def get_token_provider(self, audience: str) -> UserTokenProvider:
        """Get `TokenProvider` for audience `audience`"""
        return UserTokenProvider(self.identity_provider, audience)

    @property
    def user_id(self) -> str:
        return self.identity_provider.decoded_access_token["sub"]

    def logged_in(self) -> bool:
        return bool(self.identity_provider._access_token)

    def login(self) -> None:
        """Force a prompt for the user to login. Note this will happen automatically."""
        if self.logged_in() and not self.query_user("Already logged in. Continue?"):
            return None
        # NOTE: this works by unsetting the current access token, and then
        # calling the getter, which triggers a login prompt
        self.identity_provider.reset()
        self.identity_provider.access_token

    def logout(self) -> None:
        """Logs the user out by clearing the cache"""
        # Reset both the instance and the cache
        self.identity_provider.reset()
        self.identity_provider.clear_cache()

    def query_user(self, question: str) -> bool:
        """Query the user with `question`, and return if user confirmed"""
        choices = ("y", "n")
        # Get only the first character in the response
        answer = input(f"{question} ({'/'.join(choices)}) ").lower()[0:1]
        while answer not in choices:
            answer = input(f"Please enter {' or '.join(choices)}. ").lower()[0:1]
        return answer == "y"
