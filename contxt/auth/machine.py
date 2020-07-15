from ..services.auth import AuthService
from ..utils import make_logger
from . import Auth, Token, TokenProvider

logger = make_logger(__name__)


class MachineTokenProvider(TokenProvider):
    """Concrete `TokenProvider` for a machine client, where `client_id` and
    `client_secret` serve as the identity provider.
    """

    def __init__(self, client_id: str, client_secret: str, audience: str) -> None:
        super().__init__(audience)
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_service = AuthService()

    @TokenProvider.access_token.getter  # type: ignore
    def access_token(self) -> Token:
        """Gets a valid access token for audience `audience`"""
        if self._access_token is None or self._token_expiring():
            # Token either not yet set or expiring soon, fetch one
            logger.debug(f"Fetching new access_token for {self.audience}")
            self.access_token = self.auth_service.get_oauth_token(
                self.client_id, self.client_secret, self.audience
            )["access_token"]
        return self._access_token  # type: ignore


class MachineAuth(Auth):
    """Concrete `Auth` for a machine client"""

    def get_token_provider(self, audience: str) -> MachineTokenProvider:
        """Get `MachineTokenProvider` for audience `audience`"""
        return MachineTokenProvider(self.client_id, self.client_secret, audience)
