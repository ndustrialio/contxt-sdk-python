from enum import Enum

from contxt.models import ApiField, ApiObject, Parsers


class HealthStatus(Enum):
    """Valid health status values"""

    GOOD = "healthy"
    BAD = "unhealthy"


class Health(ApiObject):
    _api_fields = (
        ApiField("id"),
        ApiField("status", data_type=HealthStatus),
        ApiField("timestamp", data_type=Parsers.datetime, optional=True),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    def __init__(
        self,
        id: str,
        status: string,
        timestamp: Optional[datetime] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        super().__init__()
        self.id = id
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
