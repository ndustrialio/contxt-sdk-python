from datetime import datetime
from enum import Enum
from typing import Optional

from pytz import UTC

from contxt.models import ApiField, ApiObject, Parsers


class HealthStatus(Enum):
    """Valid health status values"""

    GOOD = "healthy"
    BAD = "unhealthy"


class Health(ApiObject):
    _api_fields = (
        ApiField("status", data_type=HealthStatus, creatable=True),
        ApiField("timestamp", data_type=Parsers.datetime, creatable=True),
    )

    def __init__(
        self,
        status: HealthStatus,
        timestamp: Optional[datetime] = datetime.now(UTC),
    ) -> None:
        super().__init__()
        self.status = status
        self.timestamp = timestamp
