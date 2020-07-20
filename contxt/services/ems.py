from datetime import date, timedelta
from typing import Iterable, List, Optional

from ..auth import Auth
from ..models.ems import Facility, MainService, ResourceType, UtilityContract, UtilitySpend, UtilityUsage
from .api import ApiEnvironment, ConfiguredApi
from .pagination import PagedRecords


class EmsService(ConfiguredApi):
    """EMS API client"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://ems.api.ndustrial.io/v1",
            client_id="e2IT0Zm9RgGlDBkLa2ruEcN9Iop6dJAS",
        ),
        ApiEnvironment(
            name="staging",
            base_url="https://ems-staging.api.ndustrial.io/v1",
            client_id="vMV67yaRFgjBB1JFbT3vXBOlohFdG1I4",
        ),
    )

    def __init__(self, auth: Auth, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, auth=auth, **kwargs)

    def get_facility(self, id: int) -> Facility:
        return Facility.from_api(self.get(f"facilities/{id}"))

    def get_main_services(
        self, facility_id: int, resource_type: Optional[ResourceType] = None
    ) -> List[MainService]:
        facility = self.get_facility(facility_id)
        main_services = facility.main_services

        # Manually filter on resource type
        if resource_type:
            main_services = [s for s in main_services if s.resource_type == resource_type]
        return main_services

    def get_monthly_utility_spend(
        self,
        facility_id: int,
        resource_type: ResourceType = ResourceType.ELECTRIC,
        start_date: date = date.today() - timedelta(days=3600),
        end_date: date = date.today(),
        pro_forma: bool = False,
        exclude_account_charges: bool = False,
    ) -> UtilitySpend:
        """Get monthly utility spend for facility `facility_id` and resource
        `resource_type` (for now, this must be "electric" but will be expanded).
        Note `start_date` defaults to 10 years ago (the API's maximum limit) and
        `end_date` defaults to today."""
        resp = self.get(
            f"facilities/{facility_id}/utility/spend/monthly",
            params={
                "type": resource_type.value,
                "date_start": start_date.strftime("%Y-%m"),
                "date_end": end_date.strftime("%Y-%m"),
                "pro_forma": pro_forma,
                "exclude_account_charges": exclude_account_charges,
            },
        )
        return UtilitySpend.from_api(resp)

    def get_monthly_utility_usage(
        self,
        facility_id: int,
        resource_type: ResourceType = ResourceType.ELECTRIC,
        start_date: date = date.today() - timedelta(days=3600),
        end_date: date = date.today(),
        pro_forma: bool = False,
    ) -> UtilityUsage:
        """Get monthly utility usage for facility `facility_id` and resource
        `resource_type` (for now, this must be "electric" but will be expanded).
        Note `start_date` defaults to 10 years ago (the API's maximum limit) and
        `end_date` defaults to today."""
        resp = self.get(
            f"facilities/{facility_id}/utility/usage/monthly",
            params={
                "type": resource_type.value,
                "date_start": start_date.strftime("%Y-%m"),
                "date_end": end_date.strftime("%Y-%m"),
                "pro_forma": pro_forma,
            },
        )
        return UtilityUsage.from_api(resp)

    def get_utility_contracts_for_facility(self, facility_id: int) -> Iterable[UtilityContract]:
        return PagedRecords(
            api=self, url=f"facilities/{facility_id}/contracts", record_parser=UtilityContract.from_api
        )
