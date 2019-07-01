from datetime import datetime
from typing import Optional

from contxt.legacy.models.ems import (
    FacilityMainService,
    FacilityUtilitySpend,
    FacilityUtilityUsage,
)
from contxt.legacy.services import GET, APIObjectCollection, Service

CONFIGS_BY_ENVIRONMENT = {
    "production": {
        "base_url": "https://ems.api.ndustrial.io/",
        "audience": "e2IT0Zm9RgGlDBkLa2ruEcN9Iop6dJAS",
    },
    "staging": {
        "base_url": "https://ems-staging.api.ndustrial.io/",
        "audience": "vMV67yaRFgjBB1JFbT3vXBOlohFdG1I4",
    },
}


class EMSService(Service):
    """
    Service to interact with our EMS API.
    """

    def __init__(self, auth, environment="production"):

        if environment not in CONFIGS_BY_ENVIRONMENT:
            raise Exception("Invalid environment specified")

        self.env = CONFIGS_BY_ENVIRONMENT[environment]

        super().__init__(
            base_url=self.env["base_url"],
            access_token=auth.get_token_provider(self.env["audience"]).access_token,
        )

    def get_main_services(self, facility_id: int, type: Optional[str] = None):

        response = self.execute(GET(uri=f"facilities/{facility_id}"), execute=True)

        # manual filter for main services
        rows = []
        if type:
            for row in response["main_services"]:
                if row["type"] == type:
                    rows.append(row)
        else:
            rows = response["main_services"]

        return APIObjectCollection([FacilityMainService(row) for row in rows])

    def get_monthly_utility_spend(
        self,
        facility_id: int,
        type: str,
        date_start: datetime,
        date_end: datetime,
        pro_forma: bool = False,
        exclude_account_charges: bool = False,
    ):
        params = {
            "type": type,
            "date_start": date_start.strftime("%Y-%m"),
            "date_end": date_end.strftime("%Y-%m"),
            "pro_forma": "true" if pro_forma else "false",
            "exclude_account_charges": "true" if exclude_account_charges else "false",
        }

        response = self.execute(
            GET(uri=f"facilities/{facility_id}/utility/spend/monthly").params(params),
            execute=True,
        )

        return FacilityUtilitySpend(response)

    def get_monthly_utility_usage(
        self,
        facility_id: int,
        type: str,
        date_start: datetime,
        date_end: datetime,
        pro_forma: bool = False,
    ):

        params = {
            "type": type,
            "date_start": date_start.strftime("%Y-%m"),
            "date_end": date_end.strftime("%Y-%m"),
            "pro_forma": "true" if pro_forma else "false",
        }

        response = self.execute(
            GET(uri="facilities/{}/utility/usage/monthly".format(facility_id)).params(
                params
            ),
            execute=True,
        )

        return FacilityUtilityUsage(response)
