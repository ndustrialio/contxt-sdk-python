from typing import List, Optional

from ..models.facilities import Facility
from ..utils.config import ContxtEnvironmentConfig
from .api import ConfiguredLegacyApi


class FacilitiesService(ConfiguredLegacyApi):
    """Facilities API client"""

    def __init__(self, env_config: ContxtEnvironmentConfig, **kwargs) -> None:
        super().__init__(env_config=env_config, **kwargs)

    def get_facilities(self, organization_id: Optional[str] = None) -> List[Facility]:
        uri = (
            f"organizations/{organization_id}/facilities"
            if organization_id is not None
            else "facilities"
        )
        resp = self.get(uri)
        return [Facility.from_api(rec) for rec in resp]

    def get_facility_with_id(self, facility_id: int) -> Facility:
        resp = self.get(f"facilities/{facility_id}")
        return Facility.from_api(resp)

    def get_facility_with_name(
        self, name: str, organization_id: Optional[str] = None
    ) -> Optional[Facility]:
        for facility in self.get_facilities(organization_id=organization_id):
            if facility.name.lower() == name.lower():
                return facility
        return None

    def get_facility_with_asset_id(
        self, asset_id: str, organization_id: Optional[str] = None
    ) -> Optional[Facility]:
        for facility in self.get_facilities(organization_id=organization_id):
            if facility.asset_id == asset_id:
                return facility
        return None
