from typing import Any, Dict, List, Union

from contxt.services.api import ApiEnvironment, ConfiguredApi
from contxt.utils import make_logger

logger = make_logger(__name__)


class AuthService(ConfiguredApi):
    """Wrapper around our Auth API"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://contxtauth.com/v1",
            client_id="75wT048QcpE7ujwBJPPjr263eTHl4gEX",
        ),
    )

    def __init__(self, env: str = "production"):
        super().__init__(env=env)

    def get_jwks(self) -> Dict:
        return self.get(".well-known/jwks.json")

    def get_token(
        self, access_token: str, audiences: Union[str, List[str]]
    ) -> Dict[str, Any]:
        audiences = [audiences] if isinstance(audiences, str) else audiences
        return self.post(
            "token",
            json={"audiences": audiences},
            headers={"Authorization": f"Bearer {access_token}"},
        )

    def get_oauth_token(
        self, client_id: str, client_secret: str, audience: str
    ) -> Dict[str, Any]:
        return self.post(
            "oauth/token",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "audience": audience,
                "grant_type": "client_credentials",
            },
        )
