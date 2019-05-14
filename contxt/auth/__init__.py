from datetime import datetime
from typing import Dict, Optional

from jose.jwt import get_unverified_claims
from pytz import UTC

from contxt.services.auth import AuthService
from contxt.utils import make_logger

logger = make_logger(__name__)


class TokenProvider:
    """
    Provides an unexpired `access_token` from the source client (defined by
    `client_id` and `client_secret`) for the target client (defined by `audience`).

    Overload this class to customize how the `access_token` is fetched and refreshed.
    """

    def __init__(self, client_id: str, client_secret: str, audience: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.audience = audience
        self.auth_service = AuthService()
        self._access_token: Optional[str] = None
        self._access_token_decoded: Optional[Dict] = None

    def _token_expiring(self, within: int = 60) -> bool:
        """Returns if `access_token` is within `within` seconds of expiring.
        Returns `False` if `exp` is not in the token's claims."""
        expiration = self.decoded_access_token.get("exp")
        if not expiration:
            logger.debug("'exp' not in token's claims")
            return False
        return expiration <= datetime.now(UTC).timestamp() + within

    @property
    def access_token(self) -> str:
        """Gets a valid access token for audience `audience`"""
        if self._access_token is None or self._token_expiring():
            # Token either not yet set or expiring soon, fetch one
            logger.debug(f"Fetching new access_token for {self.audience}")
            self.access_token = self.auth_service.get_oauth_token(
                self.client_id, self.client_secret, self.audience
            )
        return self._access_token

    @access_token.setter
    def access_token(self, value: str) -> None:
        """Sets both the access token and the decoded access token"""
        self._access_token = value
        self._access_token_decoded = get_unverified_claims(self._access_token)

    @property
    def decoded_access_token(self) -> Dict:
        """Gets the decoded access token"""
        if self._access_token_decoded is None:
            # Token not yet set, fetch it now
            self.access_token
        return self._access_token_decoded

    def reset(self):
        self._access_token: Optional[str] = None
        self._access_token_decoded: Optional[Dict] = None


class DependentTokenProvider(TokenProvider):
    """
    Same as `TokenProvider`, except the `access_token` is retreived by
    authenticating with a separate access token, rather than a client_id and
    client_secret pair. Thus, it is dependent on a `TokenProvider`.

    Note this is not the typical auth flow.
    """

    def __init__(self, token_provider: TokenProvider, audience: str):
        self.token_provider = token_provider
        self.audience = audience
        self.auth_service = AuthService()
        self._access_token: Optional[str] = None
        self._access_token_decoded: Optional[Dict] = None

    @TokenProvider.access_token.getter
    def access_token(self) -> str:
        """Gets a valid access token for audience `audience`"""
        if self._access_token is None or self._token_expiring():
            # Token either not yet set or expiring soon, fetch one
            logger.debug(f"Fetching new access_token for {self.audience}")
            self.access_token = self.auth_service.get_token(
                self.token_provider.access_token, self.audience
            )
        return self._access_token


class BaseAuth:
    """
    A client (service, worker, etc.) defined by `client_id` and `client_secret`.
    When the client needs to authenicate to another client, use `get_token_provider(...)`.

    Overload this class to return a custom `TokenProvider`.
    """

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_token_provider(self, audience: str) -> TokenProvider:
        """Get `TokenProvider` for audience `audience`"""
        return TokenProvider(self.client_id, self.client_secret, audience)
