from typing import List

from requests.exceptions import HTTPError

from ..auth import Auth
from ..models.contxt import (
    Cluster,
    EdgeNode,
    ServiceInstance,
    ServiceInstanceGrant,
    ServiceInstanceGrantScope,
    ServiceInstanceScope,
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

    """
    Edge Nodes
    """

    def get_edge_nodes(self, organization_id: str) -> List[EdgeNode]:
        resp = self.get(f"{organization_id}/edgenodes")
        return [EdgeNode.from_api(row) for row in resp]

    """
    Service Instances
    """

    def get_service_instance(self, organization_id: str, service_instance_id: int) -> ServiceInstance:
        resp = self.get(f"{organization_id}/service_instances/{service_instance_id}")
        return ServiceInstance.from_api(resp)

    def get_service_instances(self, organization_id: str) -> List[ServiceInstance]:
        resp = self.get(f"{organization_id}/service_instances")
        return [ServiceInstance.from_api(row) for row in resp]

    """
    Scopes
    """

    def get_service_instance_scopes(
        self, organization_id: str, service_instance_id: int
    ) -> List[ServiceInstanceScope]:
        resp = self.get(f"{organization_id}/service_instances/{service_instance_id}/scopes")
        return [ServiceInstanceScope.from_api(rec) for rec in resp]

    def add_service_instance_scope(
        self, service_grant: ServiceInstanceGrant, service_scope: ServiceInstanceScope
    ) -> ServiceInstanceGrantScope:
        resp = self.post(f"grants/{service_grant.id}/scopes/{service_scope.id}")
        return ServiceInstanceGrantScope.from_api(resp)

    def remove_service_instance_scope(
        self, service_grant: ServiceInstanceGrant, service_scope: ServiceInstanceScope
    ):
        resp = self.delete(f"grants/{service_grant.id}/scopes/{service_scope.id}")
        return resp

    """
    Dependencies
    """

    def get_service_instance_dependencies(
        self, organization_id: str, service_instance_id: int
    ) -> List[ServiceInstanceGrant]:
        resp = self.get(f"{organization_id}/service_instances/{service_instance_id}/grants")
        return [ServiceInstanceGrant.from_api(rec) for rec in resp]

    def create_service_dependency(
        self, organization_id: str, service_grant: ServiceInstanceGrant
    ) -> ServiceInstanceGrant:
        resp = self.post(
            f"{organization_id}/service_instances/{service_grant.from_service_instance_id}/grants",
            json=service_grant.post(),
        )
        return ServiceInstanceGrant.from_api(resp)
