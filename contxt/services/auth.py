from typing import Dict, List, Union

from .api import ApiEnvironment, ConfiguredApi


class AuthService(ConfiguredApi):
    """Auth API client"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://contxtauth.com/v1",
            client_id="75wT048QcpE7ujwBJPPjr263eTHl4gEX",
        ),
        ApiEnvironment(
            name="staging",
            base_url="https://contxt-auth-service.staging.ndustrial.io/v1",
            client_id="7TceUsM1eC4nKmdoC717383DWyfc9QoY",
        ),
    )

    def __init__(self, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, **kwargs)

    def get_jwks(self) -> Dict:
        return self.get(".well-known/jwks.json")

    def get_token(self, access_token: str, audiences: Union[str, List[str]]) -> Dict:
        audiences = [audiences] if isinstance(audiences, str) else audiences
        return self.post(
            "token", json={"audiences": audiences}, headers={"Authorization": f"Bearer {access_token}"}
        )

    def get_oauth_token(self, client_id: str, client_secret: str, audience: str) -> Dict:
        return self.post(
            "oauth/token",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "audience": audience,
                "grant_type": "client_credentials",
            },
        )
