from typing import Any, Callable, Dict, List, Optional, Set, Tuple

from contxt.auth.cli import CLIAuth
from contxt.models.contxt import (ConfigValue, Organization, OrganizationUser,
                                  Role, User)
from contxt.services.api import ApiServiceConfig, ConfiguredApiService
from contxt.utils import make_logger

logger = make_logger(__name__)


class ContxtService(ConfiguredApiService):
    _configs = (
        ApiServiceConfig(
            name="production",
            base_url="https://contxt.api.ndustrial.io",
            audience="8qY2xJob1JAxhmVhIDLCNnGriTM9bct8"),
        ApiServiceConfig(
            name="staging",
            base_url="https://contxt-staging.api.ndustrial.io",
            audience="8qY2xJob1JAxhmVhIDLCNnGriTM9bct8"),
    )

    def __init__(self, auth: CLIAuth, env: str = "production"):
        super().__init__(auth, env)

    def get_organizations(self) -> List[Organization]:
        logger.debug("Fetching organizations")
        resp = self.get("organizations")
        return [Organization.from_api(rec) for rec in resp]

    def create_organization(self, organization: Organization) -> Organization:
        data = organization.post()
        logger.debug(f"Creating organization with {data}")
        resp = self.post("organizations", data=data)
        return Organization.from_api(resp)

    def add_user_to_organization(self, user_id: str, organization_id: str) -> OrganizationUser:
        logger.debug(f"Adding user {user_id} to organization {organization_id}")
        resp = self.post(f"organizations/{organization_id}/users/{user_id}")
        return OrganizationUser.from_api(resp)

    # TODO: update references: get_organization_users
    def get_users_for_organization(self, organization_id: str) -> List[User]:
        logger.debug(f"Fetching users for organizations {organization_id}")
        resp = self.get(f"organizations/{organization_id}/users")
        return [User.from_api(rec) for rec in resp]

    def get_config_values_for_worker(self, worker_id: str, environment: str = None) -> List[ConfigValue]:
        logger.debug(f"Fetching configuration_values for worker {worker_id}")
        resp = self.get(
            f"workers/{worker_id}/configurations/values",
            params={"environment": environment})
        return [ConfigValue.from_api(rec) for rec in resp]

    def create_config_value(self, configuration_id: str) -> ConfigValue:
        data = configuration_value.post()
        logger.debug(f"Creating configuration_value with {data}")
        resp = self.post(
            f"configurations/{configuration_id}/values", data=data)
        return ConfigValue.from_api(resp)

    def update_config_value(self, configuration_id: str, value_id: str):
        data = configuration_value.put()
        logger.debug(f"Updating configuration_value {value_id} with {data}")
        self.put(
            f"configurations/{configuration_id}/values/{value_id}", data=data)

    def delete_config_value(self, configuration_id, value_id):
        logger.debug(f"Deleting configuration_value {value_id}")
        self.delete(f"configurations/{configuration_id}/values{value_id}")
