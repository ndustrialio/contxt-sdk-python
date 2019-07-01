from typing import List, Union

from contxt.services.api import ApiEnvironment, ConfiguredApi
from contxt.utils import make_logger

logger = make_logger(__name__)


class AuthService(ConfiguredApi):
    """
    Service to interact with our Auth API.
    """

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://contxtauth.com/v1",
            client_id="75wT048QcpE7ujwBJPPjr263eTHl4gEX",
        ),
    )

    def __init__(self, env: str = "production"):
        super().__init__(env)

    def get_token(self, access_token: str, audiences: Union[str, List[str]]) -> str:
        audiences = [audiences] if isinstance(audiences, str) else audiences
        response = self.post(
            "token",
            json={"audiences": audiences},
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

    def get_jwks(self) -> str:
        return self.get(".well-known/jwks.json")
