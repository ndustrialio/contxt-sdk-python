from typing import List

from contxt.auth import Auth
from contxt.models.ems import UtilityAccount, UtilityMeter, UtilityStatement
from contxt.models.sis import FileRead
from contxt.services.api import ApiEnvironment, ConfiguredApi
from contxt.utils import make_logger

logger = make_logger(__name__)


class SisService(ConfiguredApi):
    """Legacy SIS API client"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://sis.api.ndustrial.io/v1",
            client_id="rPDKeB6b9n7tBo5il9eY3XrJ8yKeF3ho",
        ),
    )

    def __init__(self, auth: Auth, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, auth=auth, **kwargs)

    def request_read_file(self, file_id) -> FileRead:
        resp = self.get(f"files/{file_id}/read")
        return FileRead.from_api(resp)

    def get_statements(self, facility_id: int) -> List[UtilityStatement]:
        resp = self.get(f"facilities/{facility_id}/utilities/statements")
        return [UtilityStatement.from_api(rec) for rec in resp]

    def get_meters(self, facility_id: int) -> List[UtilityMeter]:
        resp = self.get(f"facilities/{facility_id}/utilities/meters")
        return [UtilityMeter.from_api(rec) for rec in resp]

    def get_accounts(self, facility_id: int) -> List[UtilityAccount]:
        resp = self.get(f"facilities/{facility_id}/utilities/accounts")
        return [UtilityAccount.from_api(rec) for rec in resp]

    def get_statement_data(self, statement_id: int):
        return self.get(f"utilities/statements/{statement_id}/tree")
