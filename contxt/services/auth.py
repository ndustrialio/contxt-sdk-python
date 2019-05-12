from contxt.services.api import ApiServiceConfig, ConfiguredApiService
from contxt.utils import make_logger

logger = make_logger(__name__)


class AuthService(ConfiguredApiService):
    """
    Service to interact with our Auth API.
    """

    _configs = (
        ApiServiceConfig(
            name="production",
            base_url="https://contxtauth.com",
            audience="75wT048QcpE7ujwBJPPjr263eTHl4gEX",
        ),
    )

    def __init__(self, env: str = "production"):
        super().__init__(None, env)

    def get_token(self, access_token: str, audience: str) -> str:
        response = self.post(
            "token",
            json={"audiences": [audience]},
            headers={"Authorization": f"Bearer {access_token}"},
        )
        return response["access_token"]

    def get_oauth_token(self, client_id: str, client_secret: str, audience: str) -> str:
        response = self.post(
            "oauth/token",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "audience": audience,
                "grant_type": "client_credentials",
            },
        )
        return response["access_token"]
