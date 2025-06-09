from typing import Dict, List

from ..auth import Auth
from ..models.contxt import Role, ServiceInstanceScope
from .api import ApiEnvironment, ConfiguredApi


class ContxtAccessService(ConfiguredApi):
    """Contxt API client"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://contxt.api.ndustrial.io/access/v1",
            client_id="8qY2xJob1JAxhmVhIDLCNnGriTM9bct8",
        ),
        ApiEnvironment(
            name="staging",
            base_url="https://contxt.api.staging.ndustrial.io/access/v1",
            client_id="qGzdTXcmB57zlTp86rYsivG9qEss1lbF",
        ),
    )

    def __init__(self, auth: Auth, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, auth=auth, **kwargs)

    def get_roles(self, organization_id: str) -> List[Role]:
        return [Role.from_api(rec) for rec in self.get(f"{organization_id}/roles")]

    def add_role_application(
        self, organization_id: str, target_role_id: str, application_id: int
    ) -> Dict:
        return self.post(f"{organization_id}/roles/{target_role_id}/applications/{application_id}")

    def get_role_scopes(self, organization_id: str, role_id: str) -> List[Role]:
        return [
            ServiceInstanceScope.from_api(rec)
            for rec in self.get(f"{organization_id}/roles/{role_id}/scopes")
        ]

    def add_role_service_instance_scope(
        self, organization_id: str, target_role_id: str, service_instance_scope_id: int
    ) -> Dict:
        return self.post(f"{organization_id}/roles/{target_role_id}/scopes/{service_instance_scope_id}")
