from typing import List, Optional
import json

from contxt.auth import Auth
from contxt.services.api import ApiEnvironment, ConfiguredApi
from contxt.utils import make_logger
from contxt.models.files import FileRead

logger = make_logger(__name__)


class LegacyFilesService(ConfiguredApi):
    """Legacy Files API client"""

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

    def request_read_file(self, file_id) -> FileRead:
        resp = self.get(f"files/{file_id}/read")
        return FileRead.from_api(resp)
