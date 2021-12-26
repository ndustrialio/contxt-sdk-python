from datetime import date
from typing import List, Optional

from contxt.auth import Auth
from contxt.models.ems import UtilityAccount, UtilityMeter, UtilityStatement
from contxt.models.sis import FileRead
from contxt.services.api import ApiEnvironment, ConfiguredLegacyApi
from contxt.utils import make_logger
from contxt.utils.config import ContxtEnvironmentConfig


logger = make_logger(__name__)


class SisService(ConfiguredLegacyApi):
    """Legacy SIS API client"""

    def __init__(self, auth: Auth, env_config: ContxtEnvironmentConfig, **kwargs) -> None:
        super().__init__(env_config=env_config, auth=auth, **kwargs)

    def request_read_file(self, file_id) -> FileRead:
        resp = self.get(f"files/{file_id}/read")
        return FileRead.from_api(resp)

    def get_statements(
        self, facility_id: int, start: Optional[date] = None, end: Optional[date] = None
    ) -> List[UtilityStatement]:
        resp = self.get(f"facilities/{facility_id}/utilities/statements")
        statements = [UtilityStatement.from_api(rec) for rec in resp]
        if start or end:
            statements = [
                s
                for s in statements
                if (start or s.interval_start) <= s.interval_start
                and s.interval_end <= (end or s.interval_end)
            ]
        return statements

    def get_meters(self, facility_id: int) -> List[UtilityMeter]:
        resp = self.get(f"facilities/{facility_id}/utilities/meters")
        return [UtilityMeter.from_api(rec) for rec in resp]

    def get_accounts(self, facility_id: int) -> List[UtilityAccount]:
        resp = self.get(f"facilities/{facility_id}/utilities/accounts")
        return [UtilityAccount.from_api(rec) for rec in resp]

    def get_statement_data(self, statement_id: int):
        return self.get(f"utilities/statements/{statement_id}/tree")
