from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Optional

from jose.jwt import get_unverified_claims
from pytz import UTC

from contxt.utils import make_logger

logger = make_logger(__name__)


# NOTE: we should migrate to the official Oauth Sessions
# https://github.com/requests/requests-oauthlib
class TokenProvider(ABC):
    """
    An abstact base class to provide an unexpired `access_token` from the source
    client to the target client (defined by `audience`).

    Overload this class to implement `access_token`.
    """

    def __init__(self, audience: str) -> None:
        self.audience = audience
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
    @abstractmethod
    def access_token(self) -> str:
        """Gets a valid access token for audience `audience`"""

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

    def reset(self) -> None:
        self._access_token: Optional[str] = None
        self._access_token_decoded: Optional[Dict] = None


class Auth(ABC):
    """
    An abstract base class for a client (user, service, worker, etc.) defined
    by `client_id` and `client_secret`. When the client needs to authenticate
    to another client, use `get_token_provider(...)`.

    Overload this class to implement `get_token_provider(...)`.
    """

    def __init__(self, client_id: str, client_secret: str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret

    @abstractmethod
    def get_token_provider(self, audience: str) -> TokenProvider:
        """Get `TokenProvider` for audience `audience`"""
