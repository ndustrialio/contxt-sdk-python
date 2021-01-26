import os
from dataclasses import dataclass

from dotenv import load_dotenv

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

    auth: CliAuth
    load_dotenv()
    env: str = os.getenv("env", "production")

    @cachedproperty
    def assets(self) -> AssetsService:
        return AssetsService(self.auth, env=self.env)

    @cachedproperty
    def contxt(self) -> ContxtService:
        return ContxtService(self.auth, env=self.env)

    @cachedproperty
    def contxt_deployments(self) -> ContxtDeploymentService:
        return ContxtDeploymentService(self.auth, env=self.env)

    @cachedproperty
    def ems(self) -> EmsService:
        return EmsService(self.auth, env=self.env)

    @cachedproperty
    def events(self) -> EventsService:
        return EventsService(self.auth, env=self.env)

    @cachedproperty
    def facilities(self) -> FacilitiesService:
        return FacilitiesService(self.auth, env=self.env)

    @cachedproperty
    def health(self) -> HealthService:
        return HealthService(self.auth, env=self.env)

    @cachedproperty
    def iot(self) -> IotService:
        return IotService(self.auth, env=self.env)

    @cachedproperty
    def sis(self) -> SisService:
        return SisService(self.auth, env=self.env)
