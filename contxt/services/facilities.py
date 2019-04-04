from typing import Any, Callable, Dict, List, Optional, Set, Tuple

from contxt.auth.cli import CLIAuth
from contxt.models.facilities import Facility
from contxt.services.api import ConfiguredApiService
from contxt.services.assets import AssetsService
from contxt.utils import make_logger

logger = make_logger(__name__)


class FacilitiesService(ConfiguredApiService):
    """
    Service to interact with our Facilities API.

    NOTE: The facility_id in this service is the legacy integer id.
    """
    _configs = AssetsService._configs

    def __init__(self, auth: CLIAuth, env: str = "production"):
        super().__init__(auth, env)

    def get_facilities(self, organization_id: Optional[str] = None):
        logger.debug(f"Fetching facilities for organization {organization_id}")
        uri = f"organizations/{organization_id}/facilities" if organization_id is not None else "facilities"
        resp = self.get(uri)
        # TODO: handle not found errors here, and return None instead of raising an error
        return [Facility.from_api(rec) for rec in resp]

    def get_facility_with_id(self, facility_id: int):
        logger.debug(f"Fetching facility {facility_id}")
        resp = self.get(f"facilities/{facility_id}")
        # TODO: handle not found errors here, and return None instead of raising an error
        return Facility.from_api(resp)

    def get_facility_with_name(self, name: str, organization_id: Optional[str] = None):
        logger.debug(f"Fetching facility {name}")
        # Filter by name
        for facility in self.get_facilities(organization_id=organization_id):
            if facility.name.lower() == name.lower():
                return facility
        logger.warning(f"Failed to find facility with name {name}")

    def get_facility_with_asset_id(self,
                                   asset_id: str,
                                   organization_id: Optional[str] = None):
        logger.debug(f"Fetching facility {asset_id}")
        # Filter by asset_id
        for facility in self.get_facilities(organization_id=organization_id):
            if facility.asset_id == asset_id:
                return facility
        logger.warning(f"Failed to find facility with asset_id {asset_id}")
