from datetime import datetime
from typing import Any, Dict, List, Optional

from contxt.auth import Auth
from contxt.models.contxt import Config, Organization, OrganizationUser, User
from contxt.services.api import ApiEnvironment, ConfiguredApi
from contxt.utils import make_logger

logger = make_logger(__name__)


class ContxtService(ConfiguredApi):
    """Wrapper around our Contxt API"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://contxt.api.ndustrial.io/v1",
            client_id="8qY2xJob1JAxhmVhIDLCNnGriTM9bct8",
        ),
        # FIXME: staging shares the same client_id, which breaks assumptions
        # ApiEnvironment(
        #     name="staging",
        #     base_url="https://contxt-staging.api.ndustrial.io/v1",
        #     client_id="8qY2xJob1JAxhmVhIDLCNnGriTM9bct8",
        # ),
    )

    def __init__(self, auth: Auth, env: str = "production") -> None:
        super().__init__(env=env, auth=auth)

    def get_organizations(self) -> List[Organization]:
        """Get organizations"""
        resp = self.get("organizations")
        return Organization.from_api(resp, many=True)

    def get_organization_with_name(self, name: str) -> Optional[Organization]:
        """Get organization `name`"""
        for organization in self.get_organizations():
            if organization.name.lower() == name.lower():
                return organization
        logger.warning(f"Failed to find organization with name {name}")
        return None

    def create_organization(self, organization: Organization) -> Organization:
        """Create organization `organization`"""
        resp = self.post("organizations", data=organization.post())
        return Organization.from_api(resp)

    def create_organization_user(
        self, user_id: str, organization_id: str
    ) -> OrganizationUser:
        """Add user `user_id` to organization `organization_id`"""
        resp = self.post(f"organizations/{organization_id}/users/{user_id}")
        return OrganizationUser.from_api(resp)

    add_user_to_organization = create_organization_user

    def delete_organization_user(self, user_id: str, organization_id: str) -> None:
        """Remove user `user_id` from organization `organization_id`"""
        self.delete(f"organizations/{organization_id}/users/{user_id}")

    remove_user_from_organization = delete_organization_user

    def get_users_for_organization(self, organization_id: str) -> List[User]:
        """Get users for organization `organization_id`"""
        resp = self.get(f"organizations/{organization_id}/users")
        return User.from_api(resp, many=True)

    def get_config(self, configuration_id: str) -> Config:
        """Get configuration `configuration_id`"""
        resp = self.get(f"configurations/{configuration_id}")
        return Config.from_api(resp)

    def get_config_for_client(self, client_id: str, environment_id: str) -> Config:
        """Get configuration for client `client_id` and environment `environment_id`"""
        resp = self.get(
            f"clients/{client_id}/configurations",
            params={"environment_id": environment_id},
        )
        return Config.from_api(resp)

    def create_worker_run(
        self, client_id: str, start_time: Optional[datetime] = None
    ) -> Dict:
        """Create worker run for client `client_id`"""
        # TODO: create model for response
        return self.post(
            f"clients/{client_id}/runs",
            data={"start_time": start_time or datetime.now()},
        )

    def update_worker_run(
        self, client_id: str, run_id: str, end_time: Optional[datetime] = None
    ) -> None:
        """"Update `end_time` for worker run `run_id` and client `client_id`"""
        self.put(
            f"clients/{client_id}/runs/{run_id}",
            data={"end_time": end_time or datetime.now()},
        )

    def create_metric_for_worker_run(self, run_id: str, key: str, value: Any) -> Dict:
        """Create `key`: `value` metric for worker run `run_id`"""
        # TODO: create model for response
        return self.post(f"runs/{run_id}/metrics", data={"key": key, "value": value})
