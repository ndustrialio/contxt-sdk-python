import time
import webbrowser
from json import dump, load
from pathlib import Path
from typing import Any, Dict, Optional

from auth0.v3.authentication import GetToken
from requests.exceptions import HTTPError

from contxt.services.api import Api

from ..services.auth import AuthService
from ..utils import make_logger
from . import Auth, Token, TokenProvider

logger = make_logger(__name__)

CLI_CLIENT_ID = "bleED0RUwb7CJ9j7D48tqSiSZRZn29AV"


class DeviceAuthPendingException(Exception):
    pass


class DeviceAuthTimeout(Exception):
    pass


class DeviceAuthDenied(Exception):
    pass


class Auth0DeviceProvider(Api):
    def __init__(self, auth0_tenant):
        self.base_url = auth0_tenant
        self.auth_service = AuthService()
        super().__init__(base_url=f"https://{self.base_url}")

    def get_device_code_url(self):
        data = {
            "client_id": CLI_CLIENT_ID,
            "scope": "offline_access",
            "audience": self.auth_service.client_id,
        }

        return self.post("oauth/device/code", data)

    def get_access_token(self, code_info):

        data = {
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            "device_code": code_info["device_code"],
            "client_id": CLI_CLIENT_ID,
        }

        while True:
            # sleep between polling for the access token for the amount of time
            # recommended in the response
            time.sleep(code_info["interval"])

            try:
                resp = self.post("oauth/token", data)
                return resp
            except HTTPError as e:
                resp = e.response.json()
                if resp["error"] == "authorization_pending":
                    # no authorization yet...we'll wait and try again
                    continue
                elif resp["error"] == "expired_token":
                    raise DeviceAuthTimeout(
                        "The Contxt login timed out. Please run `auth login` command " "to try again."
                    )
                elif resp["error"] == "access_denied":
                    raise DeviceAuthDenied(
                        "You either cancelled the activation or you are currently not "
                        "allowed to use the Contxt CLI. Please contact support if you "
                        "believe this is an error"
                    )
                else:
                    raise e


class UserIdentityProvider(TokenProvider):
    """Concrete `TokenProvider` for a user's identity. The access token is provided
    directly from Auth0 via username and password and granted for offline access, so
    expired tokens are refreshed with a refresh token.

    If `cache_file` is specified, both the `access_token` and `refresh_token`
    are cached there as a JSON blob.
    """

    def __init__(
        self, client_id: str, client_secret: str, audience: str, cache_file: Optional[Path] = None
    ) -> None:
        super().__init__(audience)
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_service = GetToken("ndustrial.auth0.com")
        self._refresh_token: Optional[Token] = None
        self.device_provider = Auth0DeviceProvider("ndustrial.auth0.com")

        # Initialize cache
        self._cache_file = cache_file
        self._init_from_cache()

    def _init_from_cache(self) -> None:
        if self._cache_file:
            # Load the cache
            cache = self.read_cache()

            if cache:
                # Token exists in cache, set it
                logger.debug("Setting token from cache")
                self.access_token = cache["access_token"]
                self.refresh_token = cache["refresh_token"]
            else:
                # Token not in cache
                logger.debug("Token not found in cache")

    @TokenProvider.access_token.getter  # type: ignore
    def access_token(self) -> Token:
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
        return self._access_token  # type: ignore

    @property
    def refresh_token(self) -> Token:
        """Gets the refresh token"""
        if self._refresh_token is None:
            # Token not yet set, fetch it now
            self.access_token
        return self._refresh_token  # type: ignore

    @refresh_token.setter
    def refresh_token(self, value: Token) -> None:
        """Sets the refresh token"""
        self._refresh_token = value

    def login(self) -> Dict[str, Any]:
        """Returns an access_token from Auth0 after running the
        "Device Authorization Flow" successfully"""

        # Retrieve a device code to use for the user to login with
        code = self.device_provider.get_device_code_url()

        # Open their default web browser so they can login with their Contxt Account
        print(
            f"You're being redirected to your browser to complete your login. If your browser "
            f"does not automatically open, please navigate to {code['verification_uri_complete']} "
            f"to complete your login."
        )
        print(f"Please ensure the code on the webpage matches the following: {code['user_code']}")
        webbrowser.open(code["verification_uri_complete"])

        # Continuously poll Auth0 to see if they've completed their login yet
        print("Waiting for CLI to be authorized...")
        resp = self.device_provider.get_access_token(code)

        print("Success!")
        return resp

    def reset(self) -> None:
        super().reset()
        self._refresh_token = None

    def read_cache(self) -> Dict[str, Any]:
        if self._cache_file:
            logger.debug(f"Reading cache {self._cache_file}")
            if self._cache_file.is_file():
                with self._cache_file.open("r") as f:
                    return load(f)
        return {}

    def update_cache(self) -> None:
        if self._cache_file:
            logger.debug(f"Updating cache {self._cache_file}")
            cache = {"access_token": self.access_token, "refresh_token": self.refresh_token}
            self._cache_file.parent.mkdir(parents=True, exist_ok=True)
            with self._cache_file.open("w") as f:
                dump(cache, f, indent=4)

    def clear_cache(self) -> None:
        if self._cache_file:
            logger.debug(f"Clearing cache {self._cache_file}")
            if self._cache_file.is_file():
                self._cache_file.unlink()


class UserTokenProvider(TokenProvider):
    """Concrete `TokenProvider` for a user, where `identity_provider` serves as the
    identity provider.
    """

    def __init__(self, identity_provider: UserIdentityProvider, audience: str) -> None:
        super().__init__(audience)
        self.identity_provider = identity_provider
        self.auth_service = AuthService()

    @TokenProvider.access_token.getter  # type: ignore
    def access_token(self) -> Token:
        """Gets a valid access token for audience `audience`"""
        if self._access_token is None or self._token_expiring():
            # Token either not yet set or expiring soon, fetch one
            logger.debug(f"Fetching new access_token for {self.audience}")
            self.access_token = self.auth_service.get_token(
                self.identity_provider.access_token, self.audience
            )["access_token"]
        return self._access_token  # type: ignore


class CliAuth(Auth):
    """Concrete `Auth` for a CLI user, where `identity_provider` authenticates requests
    for an access token for target clients defined by `audience`.

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

    def __init__(self) -> None:
        super().__init__(client_id=CLI_CLIENT_ID, client_secret="")
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
