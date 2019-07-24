from contxt.auth import Auth, TokenProvider
from contxt.services.auth import AuthService
from contxt.utils import make_logger

logger = make_logger(__name__)


class MachineTokenProvider(TokenProvider):
    """
    Same as `TokenProvider`, but specifically for a non-human client. In this case,
    `client_id` and `client_secret` serve as the identity provider for the source
    client.
    """

    def __init__(self, client_id: str, client_secret: str, audience: str):
        super().__init__(audience)
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_service = AuthService()

    @TokenProvider.access_token.getter
    def access_token(self) -> str:
        """Gets a valid access token for audience `audience`"""
        if self._access_token is None or self._token_expiring():
            # Token either not yet set or expiring soon, fetch one
            logger.debug(f"Fetching new access_token for {self.audience}")
            self.access_token = self.auth_service.get_oauth_token(
                self.client_id, self.client_secret, self.audience
            )["access_token"]
        return self._access_token


class MachineAuth(Auth):
    """
    Same as `Auth`, but specifically for a non-human client, such as a service,
    API, or worker.
    """

    def get_token_provider(self, audience: str) -> MachineTokenProvider:
        """Get `MachineTokenProvider` for audience `audience`"""
        return MachineTokenProvider(self.client_id, self.client_secret, audience)
