from dataclasses import dataclass

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
    env: str

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
