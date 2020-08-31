from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar, Optional

from . import ApiField, ApiObject, Parsers


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
