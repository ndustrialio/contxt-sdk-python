from datetime import date, timedelta

import pytest

from contxt.auth.cli import CliAuth
from contxt.models.ems import Facility, ResourceType
from contxt.services import EmsService
from tests.static.data import TestFacility


class TestEmsServices:
    service = EmsService(CliAuth())

    def test_get_valid_facility(self, facility_id: int = TestFacility.id):
        facility = self.service.get_facility(facility_id)
        assert isinstance(facility, Facility)
        assert facility.id == facility_id

    def test_get_invalid_facility(self, facility_id: int = -1):
        with pytest.raises(Exception):
            self.service.get_facility(facility_id)

    def test_get_main_services_without_type(self, facility_id: int = TestFacility.id):
        main_services = self.service.get_main_services(facility_id)
        assert all([s.facility_id == facility_id for s in main_services])

    def test_get_main_services_with_resource_type(
        self,
        facility_id: int = TestFacility.id,
        resource_type: ResourceType = ResourceType.ELECTRIC,
    ):
        main_services = self.service.get_main_services(facility_id, resource_type)
        assert all([s.resource_type == resource_type for s in main_services])

    def test_get_monthly_utility_spend(self, facility_id: int = TestFacility.id):
        utility_spend = self.service.get_monthly_utility_spend(
            facility_id, start_date=date.today() - timedelta(days=30)
        )
        assert utility_spend.currency == "$"
        assert utility_spend.type == ResourceType.ELECTRIC
        assert utility_spend.periods

    def test_get_monthly_utility_usage(self, facility_id: int = TestFacility.id):
        utility_usage = self.service.get_monthly_utility_usage(
            facility_id, start_date=date.today() - timedelta(days=30)
        )
        assert utility_usage.unit.lower() == "kwh"
        assert utility_usage.type == ResourceType.ELECTRIC
        assert utility_usage.periods
