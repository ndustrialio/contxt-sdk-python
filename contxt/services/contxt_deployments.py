from ..auth import Auth
from ..models.contxt import (
    Cluster,
)
from .api import ApiEnvironment, ConfiguredApi


class ContxtDeploymentService(ConfiguredApi):
    """Contxt API client"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://contxt.api.ndustrial.io/deploy/v1",
            client_id="8qY2xJob1JAxhmVhIDLCNnGriTM9bct8",
        ),
    )

    def __init__(self, auth: Auth, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, auth=auth, **kwargs)

    '''
    Clusters
    '''
    def get_cluster(self, organization_id: str, cluster_slug: str) -> Cluster:
        resp = self.get(f"{organization_id}/clusters/{cluster_slug}")
        return Cluster.from_api(resp)

    def register_cluster(self, organization_id: str, secret_bearer_token: str, cluster: Cluster) -> Cluster:
        obj = cluster.post()
        obj['secrets'] = {'BEARER_TOKEN': secret_bearer_token}
        resp = self.post(f"{organization_id}/clusters", json=obj)
        return Cluster.from_api(resp)
