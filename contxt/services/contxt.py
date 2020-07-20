from datetime import datetime
from typing import Any, Dict, List, Optional

from ..auth import Auth
from ..models.contxt import Config, ConfigValue, Organization, OrganizationUser, User
from .api import ApiEnvironment, ConfiguredApi


class ContxtService(ConfiguredApi):
    """Contxt API client"""

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

    def __init__(self, auth: Auth, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, auth=auth, **kwargs)

    def get_organizations(self) -> List[Organization]:
        resp = self.get("organizations")
        return [Organization.from_api(rec) for rec in resp]

    def get_organization_with_name(self, name: str) -> Optional[Organization]:
        for organization in self.get_organizations():
            if organization.name.lower() == name.lower():
                return organization
        return None

    def create_organization(self, organization: Organization) -> Organization:
        data = organization.post()
        resp = self.post("organizations", data={"name": data["name"], "slug": data["name"]})
        return Organization.from_api(resp)

    def add_user_to_organization(self, user_id: str, organization_id: str) -> OrganizationUser:
        resp = self.post(f"organizations/{organization_id}/users/{user_id}")
        return OrganizationUser.from_api(resp)

    def get_users_for_organization(self, organization_id: str) -> List[User]:
        resp = self.get(f"organizations/{organization_id}/users")
        return [User.from_api(rec) for rec in resp]

    def get_config(self, configuration_id: str) -> Config:
        resp = self.get(f"configurations/{configuration_id}")
        return Config.from_api(resp)

    def get_config_for_client(self, client_id: str, environment_id: str) -> Config:
        params = {"environment_id": environment_id}
        resp = self.get(f"clients/{client_id}/configurations", params=params)
        return Config.from_api(resp)

    def delete_config_value(self, configuration_id: str, value_id: str) -> None:
        # TODO: is this value_id or key?
        self.delete(f"configurations/{configuration_id}/values{value_id}")

    def get_config_values(self, config_id: str, environment_id: str) -> List[ConfigValue]:
        params = {"environment": environment_id}
        resp = self.get(f"configurations/{config_id}/values", params=params)
        return [ConfigValue.from_api(rec) for rec in resp]

    def get_config_values_for_worker(self, worker_id: str, environment_id: str) -> List[ConfigValue]:
        params = {"environment": environment_id}
        resp = self.get(f"workers/{worker_id}/configurations/values", params=params)
        return [ConfigValue.from_api(rec) for rec in resp]

    def start_worker_run(self, client_id: str) -> Dict:
        data = {"start_time": datetime.now()}
        return self.post(f"clients/{client_id}/runs", data=data)

    def end_worker_run(self, client_id: str, run_id: str) -> None:
        data = {"end_time": datetime.now()}
        self.put(f"clients/{client_id}/runs/{run_id}", data=data)

    def create_worker_run_metric(self, run_id: str, key: str, value: Any) -> Dict:
        data = {"key": key, "value": value}
        return self.post(f"runs/{run_id}/metrics", data=data)
