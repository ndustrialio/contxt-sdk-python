from datetime import datetime
from typing import Any, Callable, Dict, List, Optional, Set, Tuple

from contxt.auth.cli import CLIAuth
from contxt.models.contxt import (Config, ConfigValue, Organization,
                                  OrganizationUser, User)
from contxt.services.api import ApiServiceConfig, ConfiguredApiService
from contxt.utils import make_logger

logger = make_logger(__name__)


class ContxtService(ConfiguredApiService):
    """
    Service to interact with our Contxt API.
    """
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

    def get_organization_with_name(self, name: str):
        logger.debug(f"Fetching organization {name}")
        for organization in self.get_organizations():
            if organization.name.lower() == name.lower():
                return organization
        logger.warning(f"Failed to find organization with name {name}")

    def create_organization(self, organization: Organization) -> Organization:
        data = organization.post()
        logger.debug(f"Creating organization with {data}")
        resp = self.post("organizations", data=data)
        return Organization.from_api(resp)

    def add_user_to_organization(self, user_id: str, organization_id: str) -> OrganizationUser:
        logger.debug(f"Adding user {user_id} to organization {organization_id}")
        resp = self.post(f"organizations/{organization_id}/users/{user_id}")
        return OrganizationUser.from_api(resp)

    def get_users_for_organization(self, organization_id: str) -> List[User]:
        logger.debug(f"Fetching users for organizations {organization_id}")
        resp = self.get(f"organizations/{organization_id}/users")
        return [User.from_api(rec) for rec in resp]

    def get_config(self, configuration_id: str) -> Config:
        logger.debug(f"Fetching configuration {configuration_id}")
        resp = self.get(f"configurations/{configuration_id}")
        return Config.from_api(resp)

    def get_config_for_client(self, client_id: str, environment_id: str):
        params = {"environment_id": environment_id}
        logger.debug(
            f"Fetching configuration for client {client_id} with {params}")
        resp = self.get(f"clients/{client_id}/configurations", params=params)
        return Config.from_api(resp)

    # def create_config_value(self, configuration_id: str) -> ConfigValue:
    #     data = configuration_value.post()
    #     logger.debug(f"Creating configuration_value with {data}")
    #     resp = self.post(
    #         f"configurations/{configuration_id}/values", data=data)
    #     return ConfigValue.from_api(resp)

    # def update_config_value(self, configuration_id: str, value_id: str):
    #     data = configuration_value.put()
    #     logger.debug(f"Updating configuration_value {value_id} with {data}")
    #     self.put(
    #         f"configurations/{configuration_id}/values/{value_id}", data=data)

    def delete_config_value(self, configuration_id, value_id):
        # TODO: is this value_id or key?
        logger.debug(f"Deleting configuration_value {value_id}")
        self.delete(f"configurations/{configuration_id}/values{value_id}")

    def get_config_values(self, config_id: str,
                          environment_id: str) -> List[ConfigValue]:
        params = {"environment": environment_id}
        logger.debug(
            f"Fetching configuration_values for configuration {config_id} with {params}"
        )
        resp = self.get(f"configurations/{config_id}/values", params=params)
        return [ConfigValue.from_api(rec) for rec in resp]

    def get_config_values_for_worker(self, worker_id: str,
                                     environment_id: str) -> List[ConfigValue]:
        params = {"environment": environment_id}
        logger.debug(
            f"Fetching configuration_values for worker {worker_id} with {params}"
        )
        resp = self.get(
            f"workers/{worker_id}/configurations/values", params=params)
        return [ConfigValue.from_api(rec) for rec in resp]

    def start_worker_run(self, client_id: str):
        data = {"start_time": datetime.now()}
        logger.debug(f"Creating worker run with {data}")
        resp = self.post(f"clients/{client_id}/runs", data=data)
        # TODO: create a model for this response
        return resp

    def end_worker_run(self, client_id: str, run_id: str):
        data = {"end_time": datetime.now()}
        logger.debug(f"Updating run {run_id} with {data}")
        self.put(f"clients/{client_id}/runs/{run_id}", data=data)

    def create_worker_run_metric(self, run_id, key, value):
        data = {"key": key, "value": value}
        logger.debug(f"Creating worker_run_metric with {data}")
        resp = self.post(f"runs/{run_id}/metrics", data=data)
        # TODO: create a model for this response
        return resp
