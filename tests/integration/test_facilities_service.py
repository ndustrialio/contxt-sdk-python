from contxt.auth.cli import CliAuth
from contxt.models.facilities import Facility
from contxt.services import FacilitiesService
from tests.static.data import TestFacility


class TestFacilitiesService:
    service = FacilitiesService(CliAuth())

    def get_facilities(self):
        facilities = self.service.get_facilities()
        assert facilities
        assert all([isinstance(f, Facility) for f in facilities])

    def get_facilities_for_organization(
        self, organization_id: str = TestFacility.organization_id
    ):
        facilities = self.service.get_facilities(organization_id)
        assert facilities
        assert all([f.organization_id == organization_id for f in facilities])

    def get_facility_with_id(self, facility_id: int = TestFacility.id):
        facility = self.service.get_facility_with_id(facility_id)
        assert facility
        assert facility.id == facility_id

    def get_facility_with_name(self, facility_name: str = TestFacility.name):
        facility = self.service.get_facility_with_name(facility_name)
        assert facility
        assert facility.name.lower() == facility_name.lower()

    def get_facility_with_asset_id(self, asset_id: str = TestFacility.asset_id):
        facility = self.service.get_facility_with_asset_id(asset_id)
        assert facility
        assert facility.asset_id == asset_id
