from dataclasses import dataclass

from contxt.auth.cli import CliAuth
from contxt.services import (
    AssetsService,
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

    @cachedproperty
    def assets(self) -> AssetsService:
        return AssetsService(self.auth)

    @cachedproperty
    def contxt(self) -> ContxtService:
        return ContxtService(self.auth)

    @cachedproperty
    def ems(self) -> EmsService:
        return EmsService(self.auth)

    @cachedproperty
    def events(self) -> EventsService:
        return EventsService(self.auth)

    @cachedproperty
    def facilities(self) -> FacilitiesService:
        return FacilitiesService(self.auth)

    @cachedproperty
    def health(self) -> HealthService:
        return HealthService(self.auth)

    @cachedproperty
    def iot(self) -> IotService:
        return IotService(self.auth)

    @cachedproperty
    def sis(self) -> SisService:
        return SisService(self.auth)
