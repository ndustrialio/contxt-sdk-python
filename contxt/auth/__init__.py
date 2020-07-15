"""Auth for API clients"""

from abc import ABC, abstractmethod
from datetime import datetime, timezone
from typing import Any, Dict, Optional

from jwt import decode

Token = str
DecodedToken = Dict[str, Any]


# TODO: Replace with https://github.com/requests/requests-oauthlib
class TokenProvider(ABC):
    """An abstact base class to provide an unexpired `access_token` from the source
    client to the target client, defined by `audience`.

    Overload this class to implement `access_token`.
    """

    def __init__(self, audience: str) -> None:
        self.audience = audience
        self._access_token: Optional[Token] = None
        self._access_token_decoded: Optional[DecodedToken] = None

    def _token_expiring(self, within: int = 60) -> bool:
        """Returns if `access_token` is within `within` seconds of expiring.
        Returns `False` if `exp` is not in the token's claims."""
        expiration = self.decoded_access_token.get("exp")
        if not expiration:
            return False
        return expiration <= datetime.now(timezone.utc).timestamp() + within

    @property
    @abstractmethod
    def access_token(self) -> str:
        """Gets a valid access token for audience `audience`"""

    @access_token.setter
    def access_token(self, value: Token) -> None:
        """Sets both the access token and the decoded access token"""
        self._access_token = value
        self._access_token_decoded = decode(self._access_token, verify=False)

    @property
    def decoded_access_token(self) -> DecodedToken:
        """Gets the decoded access token"""
        if self._access_token_decoded is None:
            # Token not yet set, fetch it now
            self.access_token
        return self._access_token_decoded  # type: ignore

    def reset(self) -> None:
        self._access_token = None
        self._access_token_decoded = None


class Auth(ABC):
    """An abstract base class for a client defined by `client_id` and `client_secret`.
    To authenticate to another client, use `get_token_provider()`.

    Overload this class to implement `get_token_provider()`.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret

    @abstractmethod
    def get_token_provider(self, audience: str) -> TokenProvider:
        """Get `TokenProvider` for audience `audience`"""
