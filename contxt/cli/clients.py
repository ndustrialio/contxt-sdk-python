from dataclasses import dataclass
from typing import Optional

import click

from contxt.services import (
    AssetsService,
    ContxtDeploymentService,
    ContxtService,
    EmsService,
    EventsService,
    FacilitiesService,
    HealthService,
    IotService,
    UtilityRatesService,
    SisService,
)
from contxt.utils import cachedproperty
from contxt.utils.config import ContxtEnvironmentConfig
from contxt.utils.contxt_environment import ContxtEnvironment


@dataclass
class Clients:
    """Holds a user and all client API's"""

    contxt_env: ContxtEnvironment
    org_slug: Optional[str]

    @cachedproperty
    def org_id(self) -> str:
        if not self.org_slug:
            # Check if user only has access to a single org
            token = self.contxt.session.auth.token_provider.decoded_access_token
            orgs = token.get("organizations", [])
            if len(orgs) != 1:
                raise click.ClickException("Organization required. Try again with `contxt --org=...`.")
            return orgs[0]
        for org in self.contxt.get("organizations"):
            if org["slug"] == self.org_slug:
                return org["id"]
        raise click.ClickException(f"Organization {self.org_slug!r} does not exist.")

    @cachedproperty
    def assets(self) -> AssetsService:
        return AssetsService(env_config=self.contxt_env.get_config_for_service_name('assets'))

    @cachedproperty
    def contxt(self) -> ContxtService:
        return ContxtService(env_config=self.contxt_env.get_config_for_service_name('contxt'))

    @cachedproperty
    def contxt_deployments(self) -> ContxtDeploymentService:
        return ContxtDeploymentService(env_config=self.contxt_env.get_config_for_service_name('contxt'))

    @cachedproperty
    def ems(self) -> EmsService:
        return EmsService(env_config=self.contxt_env.get_config_for_service_name('ems'))

    @cachedproperty
    def events(self) -> EventsService:
        return EventsService(env_config=self.contxt_env.get_config_for_service_name('events'))

    @cachedproperty
    def facilities(self) -> FacilitiesService:
        return FacilitiesService(env_config=self.contxt_env.get_config_for_service_name('assets'))

    @cachedproperty
    def health(self) -> HealthService:
        return HealthService(env_config=self.contxt_env.get_config_for_service_name('health'))

    @cachedproperty
    def iot(self) -> IotService:
        return IotService(env_config=self.contxt_env.get_config_for_service_name('iot'))

    @cachedproperty
    def sis(self) -> SisService:
        return SisService(env_config=self.contxt_env.get_config_for_service_name('sis'))

    @cachedproperty
    def rates(self) -> UtilityRatesService:
        return UtilityRatesService(env_config=self.contxt_env.get_config_for_service_name('rates'))
