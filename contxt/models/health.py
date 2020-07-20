from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import ClassVar

from . import ApiField, ApiObject, Parsers


class HealthStatus(Enum):
    """Valid health status values"""

    GOOD = "healthy"
    BAD = "unhealthy"


@dataclass
class Health(ApiObject):
    _api_fields: ClassVar = (
        ApiField("status", data_type=HealthStatus, creatable=True),
        ApiField("timestamp", data_type=Parsers.datetime, creatable=True),
    )

    status: HealthStatus
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
