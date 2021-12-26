from typing import List

from requests.exceptions import HTTPError

from ..auth import Auth
from ..models.contxt import Cluster
from ..utils.config import ContxtEnvironmentConfig
from .api import ApiEnvironment, ConfiguredLegacyApi


class ContxtDeploymentService(ConfiguredLegacyApi):
    """Contxt API client"""

    def __init__(self, auth: Auth, env_config: ContxtEnvironmentConfig, **kwargs) -> None:
        super().__init__(env_config=env_config, auth=auth, **kwargs)

    def get_clusters(self, organization_id: str) -> List[Cluster]:
        return [Cluster.from_api(rec) for rec in self.get(f"{organization_id}/clusters")]

    def get_cluster(self, organization_id: str, cluster_slug: str) -> Cluster:
        resp = self.get(f"{organization_id}/clusters/{cluster_slug}")
        return Cluster.from_api(resp)

    def register_cluster(self, organization_id: str, cluster: Cluster) -> None:
        obj = cluster.post()
        try:
            resp = self.post(f"{organization_id}/clusters", json=obj)
            return Cluster.from_api(resp)
        except HTTPError:
            pass
            return
