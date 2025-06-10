from typing import List

from requests.exceptions import HTTPError

from ..auth import Auth
from ..models.contxt import Cluster, EdgeNode, EdgeNodeGrant, ServiceInstanceGrant, ServiceInstanceScope
from .api import ApiEnvironment, ConfiguredApi


class ContxtDeploymentService(ConfiguredApi):
    """Contxt API client"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://contxt.api.ndustrial.io/deploy/v1",
            client_id="8qY2xJob1JAxhmVhIDLCNnGriTM9bct8",
        ),
        ApiEnvironment(
            name="staging",
            base_url="https://contxt.api.staging.ndustrial.io/deploy/v1",
            client_id="qGzdTXcmB57zlTp86rYsivG9qEss1lbF",
        ),
    )

    def __init__(self, auth: Auth, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, auth=auth, **kwargs)

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

    def get_edge_nodes(self, organization_id: str, project_slug: int) -> List[EdgeNode]:
        resp = self.get(f"{organization_id}/projects/{project_slug}/edgenodes")
        return [EdgeNode.from_api(rec) for rec in resp]

    def get_edge_node_grants(self, organization_id: str, edge_node_id: int) -> List[EdgeNodeGrant]:
        resp = self.get(f"{organization_id}/edgenodes/{edge_node_id}/grants")
        return [EdgeNodeGrant.from_api(rec) for rec in resp]

    def get_service_instance_grants(
        self, organization_id: str, service_instance_id: int
    ) -> List[ServiceInstanceGrant]:
        resp = self.get(f"{organization_id}/service_instances/{service_instance_id}/grants")
        return [ServiceInstanceGrant.from_api(rec) for rec in resp]

    def get_service_instance_scopes(
        self, organization_id: str, service_instance_id: int
    ) -> List[ServiceInstanceScope]:
        resp = self.get(f"{organization_id}/service_instances/{service_instance_id}/scopes")
        return [ServiceInstanceScope.from_api(rec) for rec in resp]
