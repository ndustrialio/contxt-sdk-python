from ..auth import Auth
from ..models.health import Health
from .api import ApiEnvironment, ConfiguredApi


class HealthService(ConfiguredApi):
    """Health API client"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://health.api.ndustrial.io/v1",
            client_id="6uaQIV1KnnWhXiTm09iGDvy2aQaz2xVI",
        ),
    )

    def __init__(self, auth: Auth, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, auth=auth, **kwargs)

    def create_health_status(self, org_id: str, asset_id: str, health: Health) -> Health:
        resp = self.post(f"{org_id}/assets/{asset_id}", data=health.post())
        return Health.from_api(resp)
