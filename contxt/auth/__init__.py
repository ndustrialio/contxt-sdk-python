from datetime import datetime
from typing import Dict, Optional

from jwt import decode
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
        """Returns if `access_token` is within `within` seconds of expiring"""
        return self.decoded_access_token["exp"] <= (
            datetime.now(UTC).timestamp() + within
        )

    @property
    def access_token(self) -> str:
        """Gets a valid access_token for audience `audience`"""
        if self._access_token is None or self._token_expiring():
            # Token either not set or expiring soon, fetch one
            self.access_token = self.auth_service.get_oauth_token(
                self.client_id, self.client_secret, self.audience
            )
        return self._access_token

    @access_token.setter
    def access_token(self, value: str) -> None:
        """Sets both the `access_token` and the `decoded_access_token`"""
        self._access_token = value
        self._access_token_decoded = decode(self._access_token, verify=False)

    @property
    def decoded_access_token(self) -> Dict:
        """Gets the `decoded_access_token`"""
        if self._access_token_decoded is None:
            # Token not yet set, fetch it now
            self.access_token
        return self._access_token_decoded


class BaseAuth:
    """
    A client (service, worker, etc.) defined by `client_id` and `client_secret`.
    When the client needs to authenicate to another client, use `get_token_provider`.

    Overload this class to return a custom `TokenProvider`.
    """

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret

    def get_token_provider(self, audience: str) -> TokenProvider:
        """Get `TokenProvider` for audience `audience`"""
        return TokenProvider(self.client_id, self.client_secret, audience)
