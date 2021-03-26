from dataclasses import dataclass
from typing import Optional

import click

from contxt.auth.cli import CliAuth
from contxt.services import (
    AssetsService,
    ContxtDeploymentService,
    ContxtService,
    EmsService,
    EventsService,
    FacilitiesService,
    HealthService,
    IotService,
    SisService,
)
from contxt.utils import cachedproperty


@dataclass
class Clients:
    """Holds a user and all client API's"""

    env: str
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
    def auth(self) -> CliAuth:
        return CliAuth(env=self.env)

    @cachedproperty
    def assets(self) -> AssetsService:
        return AssetsService(auth=self.auth, env=self.env)

    @cachedproperty
    def contxt(self) -> ContxtService:
        return ContxtService(auth=self.auth, env=self.env)

    @cachedproperty
    def contxt_deployments(self) -> ContxtDeploymentService:
        return ContxtDeploymentService(auth=self.auth, env=self.env)

    @cachedproperty
    def ems(self) -> EmsService:
        return EmsService(auth=self.auth, env=self.env)

    @cachedproperty
    def events(self) -> EventsService:
        return EventsService(auth=self.auth, env=self.env)

    @cachedproperty
    def facilities(self) -> FacilitiesService:
        return FacilitiesService(auth=self.auth, env=self.env)

    @cachedproperty
    def health(self) -> HealthService:
        return HealthService(auth=self.auth, env=self.env)

    @cachedproperty
    def iot(self) -> IotService:
        return IotService(auth=self.auth, env=self.env)

    @cachedproperty
    def sis(self) -> SisService:
        return SisService(auth=self.auth, env=self.env)
