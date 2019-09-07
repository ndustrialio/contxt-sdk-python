from datetime import datetime
from json import JSONDecodeError, loads
from typing import Any, Dict, Optional

from contxt.models.base import UUID, BaseModel, dataclass, field
from contxt.utils import cachedproperty, make_logger

logger = make_logger(__name__)

Parameters = Dict[str, Any]


@dataclass
class EventType(BaseModel):
    id: UUID
    name: str = field(post=True)
    description: str = field(post=True)
    level: int = field(post=True)
    client_id: str = field(post=True)
    slug: str = field(post=True)
    is_ongoing_event: bool  # optional
    is_realtime_enabled: bool = field(post=True)
    created_at: datetime
    updated_at: datetime


@dataclass
class EventDefinition(BaseModel):
    id: UUID
    event_id: UUID
    description: str
    parameters: str
    created_at: datetime
    updated_at: datetime
    human_readable_parameters: Optional[str] = None

    @cachedproperty
    def parsed_parameters(self) -> Parameters:
        """Parse `parameters` as JSON"""
        try:
            return loads(self.parameters)
        except JSONDecodeError as e:
            logger.error(
                f"Failed to parse {type(self).__name__}.parameters"
                f" {self.parameters} as JSON: {e}"
            )
        return {}


@dataclass
class Owner(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    is_machine_user: bool  # optional
    created_at: datetime
    updated_at: datetime


@dataclass
class Event(BaseModel):
    id: UUID
    event_type_id: UUID = field(post=True)
    organization_id: UUID = field(post=True)
    name: str = field(post=True)
    allow_others_to_trigger: bool = field(post=True)
    created_at: datetime
    updated_at: datetime
    event_type: EventType = field(default=None, key="EventType")
    topic_arn: Optional[str] = None
    facility_id: Optional[int] = field(default=None, post=True)
    is_public: Optional[bool] = field(default=None, post=True)
    owner_id: Optional[str] = None
    owner: Optional[Owner] = field(default=None, key="Owner")
    deleted_at: Optional[datetime] = None


@dataclass
class ChainedData(BaseModel):
    source_id: str
    subchain_triggered_event_id: str
    trigger_start_at: datetime
    trigger_end_at: datetime


class TriggeredEventData(ChainedData):
    """DEPRECATED"""


@dataclass
class TriggeredEvent(BaseModel):
    id: UUID
    event_id: UUID = field(post=True)
    event: Event = field(key="Event")  # default=None
    trigger_start_at: datetime = field(post=True, put=True)
    created_at: datetime
    updated_at: datetime
    trigger_end_at: Optional[datetime] = field(default=None, post=True, put=True)
    data: Optional[str] = field(default=None, post=True, put=True)
    owner_id: Optional[str] = None
    owner: Optional[Owner] = field(default=None, key="Owner")
    is_public: Optional[bool] = None
    deleted_at: Optional[datetime] = None

    @cachedproperty
    def parsed_data(self) -> Optional[Any]:
        """Parse `data` as either JSON or `ChainedData`"""

        def _log_failure(e, guess):
            logger.error(
                f"Failed to parse {type(self).__name__}.data {self.data}"
                f" as {guess}: {e}"
            )

        if not self.data:
            return self.data

        # HACK: infer datatype (values seem to be mostly json or a
        # loosely-structured string, such as "(15>10)")
        try:
            data_json = loads(self.data)
        except JSONDecodeError as e:
            _log_failure(e, "JSON")
            return self.data

        # Got valid json, try serializing as ChainedData if it appears applicable
        if "subchain_triggered_event_id" in self.data:
            try:
                return ChainedData.from_dict(data_json, many=True)
            except Exception as e:
                _log_failure(e, "ChainedData")

        return data_json
