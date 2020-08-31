from typing import List, Optional
import json

from contxt.auth import Auth
from contxt.services.api import ApiEnvironment, ConfiguredApi
from contxt.utils import make_logger
from contxt.models.ems import UtilityStatement, UtilityAccount, UtilityMeter
from contxt.models.resource import Resource

logger = make_logger(__name__)


class UtilitiesService(ConfiguredApi):
    """Utilities API client"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://sis.api.ndustrial.io/v1",
            client_id="rPDKeB6b9n7tBo5il9eY3XrJ8yKeF3ho",
        ),
    )

    def __init__(
        self,
        auth: Auth,
        env: str = "production",
        **kwargs,
    ) -> None:
        super().__init__(env=env, auth=auth, **kwargs)

    def get_accounts(self) -> List[Resource]:
        resp = self.get(f"utilities/accounts")
        return [rec for rec in resp]

    def get_meters(self) -> List[Resource]:
        resp = self.get("utilities/meters")
        return [rec for rec in resp]

    def get_statements(self, facility_id) -> List[UtilityStatement]:
        resp = self.get(f"facilities/{facility_id}/utilities/statements")
        return [UtilityStatement.from_api(rec) for rec in resp]

    def get_meters(self, facility_id):
        resp = self.get(f"facilities/{facility_id}/utilities/meters")
        return [UtilityMeter.from_api(rec) for rec in resp]

    def get_accounts(self, facility_id):
        resp = self.get(f"facilities/{facility_id}/utilities/accounts")
        return [UtilityAccount.from_api(rec) for rec in resp]

    def get_statement_data(self, statement_id):
        return self.get(f"utilities/statements/{statement_id}/tree")



