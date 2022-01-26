from ..utils import make_logger
from . import Auth, Token, TokenProvider
from ..utils.config import ContxtEnvironmentConfig

logger = make_logger(__name__)


class PlainTokenProvider(TokenProvider):
    """Plain-ole `TokenProvider` for a client, where `token` is the token that is used for every request.
    """
    def __init__(self, token: str) -> None:
        super().__init__('')
        self.token = token

    @TokenProvider.access_token.getter  # type: ignore
    def access_token(self) -> Token:
        """Retrieves the token to use for the API Request"""
        return self.token


class PlainTokenAuth(Auth):
    """Concrete `Auth` for a machine client"""

    def __init__(self, env_config: ContxtEnvironmentConfig, token: str) -> None:
        super().__init__(env_config)
        self.env_config = env_config
        self.token = token
    
    def get_token_provider(self, audience: str = '') -> PlainTokenProvider:
        """Get `PlainTokenProvider` for audience `audience`"""
        return PlainTokenProvider(token=self.token)
