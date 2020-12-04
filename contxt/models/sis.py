import logging
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import ClassVar, Optional

import requests

from . import ApiField, ApiObject, Parsers

logger = logging.getLogger(__name__)


@dataclass
class FileRead(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("file_id"),
        ApiField("temporary_url"),
        ApiField("expires_at"),
        ApiField("action"),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
        ApiField("file_created_at", data_type=Parsers.datetime),
    )

    id: int
    file_id: int
    temporary_url: str
    expires_at: datetime
    action: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    file_created_at: Optional[datetime] = None

    def download(self, path: Path, attempts: int = 1) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        attempt = 1
        while attempt <= attempts:
            try:
                r = requests.get(self.temporary_url)
                with path.open("wb") as f:
                    f.write(r.content)
                return
            except requests.exceptions.HTTPError as e:
                logger.warning(f"Exception raised during download {e}")
                attempt += 1
        raise RuntimeError(f"Failed to download file from {self.temporary_url}")
