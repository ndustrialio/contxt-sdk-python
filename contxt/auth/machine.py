from ..services.api import AuthService
from ..utils import make_logger
from ..utils.config import ContxtEnvironmentConfig
from . import Auth, Token, TokenProvider
from contxt.services.auth import StoredTokenCache

import requests
from auth0.v3.authentication import GetToken

logger = make_logger(__name__)


class PlainMachineTokenProvider(TokenProvider):
    """Plain-ole `TokenProvider` for a machine client, where `client_id` and
        `client_secret` serve as the identity provider WITHOUT using Contxt Auth Service
    """
    def __init__(self, contxt_env: ContxtEnvironmentConfig) -> None:
        super().__init__(contxt_env.apiEnvironment.clientId)
        self.contxt_env = contxt_env
        self.token_cache = StoredTokenCache()

    @TokenProvider.access_token.getter  # type: ignore
    def access_token(self) -> Token:
        """Gets a valid access token for audience `audience`"""
        cached_token = self.token_cache.get_token(client_id=self.contxt_env.clientId,
                                                  audience=self.contxt_env.apiEnvironment.clientId)

        if cached_token:
            return cached_token

        if self.contxt_env.apiEnvironment.authRequired:
            print(f'Getting token for {self.contxt_env.clientId}: {self.contxt_env.clientSecret} '
                  f'against {self.contxt_env.apiEnvironment.clientId} at auth provider: '
                  f'{self.contxt_env.apiEnvironment.authProvider}')
            req = GetToken(self.contxt_env.apiEnvironment.authProvider)
            token = req.client_credentials(client_id=self.contxt_env.clientId,
                                           client_secret=self.contxt_env.clientSecret,
                                           audience=self.contxt_env.apiEnvironment.clientId)
            self.token_cache.set_token(client_id=self.contxt_env.clientId,
                                       audience=self.contxt_env.apiEnvironment.clientId,
                                       token=token['access_token'])
            return token['access_token']


class MachineTokenProvider(TokenProvider):
    """Concrete `TokenProvider` for a machine client, where `client_id` and
    `client_secret` serve as the identity provider.
    """

    def __init__(self, env_config: ContxtEnvironmentConfig, audience: str) -> None:
        super().__init__(audience)
        self.env_config = env_config
        self.auth_service = AuthService(env_config)

    @TokenProvider.access_token.getter  # type: ignore
    def access_token(self) -> Token:
        """Gets a valid access token for audience `audience`"""
        if self._access_token is None or self._token_expiring():
            # Token either not yet set or expiring soon, fetch one
            logger.debug(f"Fetching new access_token for {self.audience}")
            self.access_token = self.auth_service.get_oauth_token(
                self.env_config.clientId, self.env_config.clientSecret, self.audience
            )
        return self._access_token  # type: ignore


class MachineAuth(Auth):
    """Concrete `Auth` for a machine client"""

    def get_token_provider(self, audience: str) -> MachineTokenProvider:
        """Get `MachineTokenProvider` for audience `audience`"""
        return MachineTokenProvider(self.env_config, audience)
