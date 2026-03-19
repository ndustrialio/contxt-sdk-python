from unittest.mock import MagicMock, patch

import pytest

from contxt.generated.nionic_queries import Operations as nionic_operations
from contxt.models.ems import ResourceType
from contxt.services.nionic import NionicService


def _make_datapoint(id, name, data_source_name="ds1", alias=None, data_type="FLOAT"):
    return {
        "id": id,
        "dataSourceName": data_source_name,
        "name": name,
        "alias": alias or name,
        "dataType": data_type,
    }


def _make_main_service(
    id,
    facility_id,
    name,
    type_,
    usage=None,
    demand=None,
    meter_usage=None,
    meter_demand=None,
    grid_usage=None,
    grid_demand=None,
):
    return {
        "id": id,
        "facilityId": facility_id,
        "name": name,
        "type": type_,
        "usage": usage,
        "demand": demand,
        "meterUsage": meter_usage,
        "meterDemand": meter_demand,
        "gridUsage": grid_usage,
        "gridDemand": grid_demand,
        "createdAt": "2024-01-01T00:00:00",
        "updatedAt": "2024-01-01T00:00:00",
    }


ELECTRIC_SERVICE = _make_main_service(
    id=1,
    facility_id=100,
    name="Main Electric",
    type_="ELECTRIC",
    usage=_make_datapoint(10, "electric_usage"),
    demand=_make_datapoint(11, "electric_demand"),
    meter_usage=_make_datapoint(12, "electric_meter_usage"),
    meter_demand=_make_datapoint(13, "electric_meter_demand"),
    grid_usage=_make_datapoint(14, "electric_grid_usage"),
    grid_demand=_make_datapoint(15, "electric_grid_demand"),
)

SOLAR_SERVICE = _make_main_service(
    id=2,
    facility_id=100,
    name="Main Solar",
    type_="SOLAR",
    usage=_make_datapoint(20, "solar_usage"),
    demand=_make_datapoint(21, "solar_demand"),
    meter_usage=None,
    meter_demand=None,
    grid_usage=None,
    grid_demand=None,
)


def _mock_run_response(services):
    """Build the raw JSON dict that NionicService.run() would return from the endpoint."""
    return {"data": {"mainServices": {"nodes": services}}}


@pytest.fixture
def nionic_service():
    """Create a NionicService with mocked auth, bypassing real HTTP setup."""
    mock_auth = MagicMock()
    mock_auth.get_token.return_value = "fake-token"
    with patch.object(NionicService, "__init__", lambda self, *a, **kw: None):
        svc = NionicService.__new__(NionicService)
    return svc


class TestGetMainServices:
    def test_returns_all_services(self, nionic_service):
        response = _mock_run_response([ELECTRIC_SERVICE, SOLAR_SERVICE])
        with patch.object(nionic_service, "run", return_value=response):
            results = nionic_service.get_main_services(facility_id=100)

        assert len(results) == 2
        assert results[0].name == "Main Electric"
        assert results[1].name == "Main Solar"

    def test_all_datapoint_fields_populated(self, nionic_service):
        response = _mock_run_response([ELECTRIC_SERVICE])
        with patch.object(nionic_service, "run", return_value=response):
            results = nionic_service.get_main_services(facility_id=100)

        svc = results[0]
        assert svc.usage.id == 10
        assert svc.demand.id == 11
        assert svc.meter_usage.id == 12
        assert svc.meter_demand.id == 13
        assert svc.grid_usage.id == 14
        assert svc.grid_demand.id == 15

    def test_datapoint_subfields(self, nionic_service):
        response = _mock_run_response([ELECTRIC_SERVICE])
        with patch.object(nionic_service, "run", return_value=response):
            results = nionic_service.get_main_services(facility_id=100)

        dp = results[0].meter_usage
        assert dp.data_source_name == "ds1"
        assert dp.name == "electric_meter_usage"
        assert dp.alias == "electric_meter_usage"
        assert dp.data_type == "FLOAT"

    def test_filters_by_resource_type(self, nionic_service):
        response = _mock_run_response([ELECTRIC_SERVICE, SOLAR_SERVICE])
        with patch.object(nionic_service, "run", return_value=response):
            results = nionic_service.get_main_services(
                facility_id=100, resource_type=ResourceType.ELECTRIC
            )

        assert len(results) == 1
        assert results[0].name == "Main Electric"

    def test_filters_by_solar_type(self, nionic_service):
        response = _mock_run_response([ELECTRIC_SERVICE, SOLAR_SERVICE])
        with patch.object(nionic_service, "run", return_value=response):
            results = nionic_service.get_main_services(
                facility_id=100, resource_type=ResourceType.SOLAR
            )

        assert len(results) == 1
        assert results[0].name == "Main Solar"

    def test_null_datapoints(self, nionic_service):
        """When meter/grid fields are null, sgqlc returns empty falsy DataPoint objects."""
        response = _mock_run_response([SOLAR_SERVICE])
        with patch.object(nionic_service, "run", return_value=response):
            results = nionic_service.get_main_services(facility_id=100)

        svc = results[0]
        assert svc.usage.id == 20
        assert svc.demand.id == 21
        # sgqlc deserializes null relationships as empty DataPoint objects (falsy, no attributes)
        assert not svc.meter_usage
        assert not svc.meter_demand
        assert not svc.grid_usage
        assert not svc.grid_demand
