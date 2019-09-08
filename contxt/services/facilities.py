from typing import List, Optional

from contxt.auth import Auth
from contxt.models.facilities import Facility
from contxt.services.api import ConfiguredApi
from contxt.services.assets import AssetsService
from contxt.utils import make_logger

logger = make_logger(__name__)


class FacilitiesService(ConfiguredApi):
    """Wrapper around our Facilities API"""

    _envs = AssetsService._envs

    def __init__(self, auth: Auth, env: str = "production") -> None:
        super().__init__(env=env, auth=auth)

    def get_facilities(self, organization_id: Optional[str] = None) -> List[Facility]:
        """Get all facilities (optionally, for organization `organization_id`)"""
        uri = (
            f"organizations/{organization_id}/facilities"
            if organization_id is not None
            else "facilities"
        )
        resp = self.get(uri)
        return Facility.from_api(resp, many=True)

    def get_facility_with_id(self, facility_id: int) -> Facility:
        """Get facility with id `facility_id`"""
        resp = self.get(f"facilities/{facility_id}")
        return Facility.from_api(resp)

    def get_facility_with_name(
        self, name: str, organization_id: Optional[str] = None
    ) -> Optional[Facility]:
        """Get facility with name `name`, within organization `organization_id`"""
        for facility in self.get_facilities(organization_id):
            if facility.name.lower() == name.lower():
                return facility
        logger.warning(f"Failed to find facility with name {name}")
        return None

    def get_facility_with_asset_id(
        self, asset_id: str, organization_id: Optional[str] = None
    ) -> Optional[Facility]:
        """Get facility with asset id `asset_id`, within organization `organization_id`"""
        for facility in self.get_facilities(organization_id):
            if facility.asset_id == asset_id:
                return facility
        logger.warning(f"Failed to find facility with asset_id {asset_id}")
        return None
