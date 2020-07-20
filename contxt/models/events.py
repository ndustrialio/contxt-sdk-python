from dataclasses import dataclass
from datetime import datetime
from json import loads
from typing import ClassVar, Optional

from . import ApiField, ApiObject, Parsers


@dataclass
class EventType(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("name", creatable=True),
        ApiField("slug", creatable=True),
        ApiField("description", creatable=True),
        ApiField("client_id", creatable=True),
        ApiField("level", data_type=int, creatable=True),
        ApiField("is_ongoing_event", data_type=bool, optional=True),
        ApiField("is_realtime_enabled", data_type=bool, creatable=True),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    name: str
    slug: str
    description: str
    client_id: str
    level: int
    id: Optional[str] = None
    is_ongoing_event: Optional[bool] = None
    is_realtime_enabled: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class EventDefinition(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("event_id"),
        ApiField("description"),
        ApiField("parameters", data_type=lambda o: loads(o.replace('"', '"'))),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    event_id: str
    description: str
    parameters: dict
    created_at: datetime
    updated_at: datetime
    id: Optional[str] = None
    human_readable_parameters: Optional[str] = None


@dataclass
class Owner(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("first_name"),
        ApiField("last_name"),
        ApiField("email"),
        ApiField("is_machine_user", data_type=bool, optional=True),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: str
    first_name: str
    last_name: str
    email: str
    is_machine_user: bool
    created_at: datetime
    updated_at: datetime


@dataclass
class Event(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("name", creatable=True),
        ApiField("event_type_id", creatable=True),
        ApiField("EventType", attr_key="event_type", data_type=EventType, optional=True),
        ApiField("organization_id", creatable=True),
        ApiField("facility_id", data_type=int, creatable=True),
        ApiField("owner_id"),
        ApiField("Owner", attr_key="owner", data_type=Owner, optional=True),
        ApiField("topic_arn", optional=True),
        ApiField("allow_others_to_trigger", data_type=bool, creatable=True),
        ApiField("is_public", data_type=bool, creatable=True),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
        ApiField("deleted_at", data_type=Parsers.datetime),
    )

    name: str
    event_type_id: str
    organization_id: str
    allow_others_to_trigger: bool
    is_public: bool
    id: Optional[str] = None
    facility_id: Optional[int] = None
    owner_id: Optional[str] = None
    owner: Optional[Owner] = None
    event_type: Optional[EventType] = None
    topic_arn: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None


@dataclass
class TriggeredEventData(ApiObject):
    _api_fields: ClassVar = (
        ApiField("source_id"),
        ApiField("subchain_triggered_event_id"),
        ApiField("trigger_start_at", data_type=Parsers.datetime),
        ApiField("trigger_end_at", data_type=Parsers.datetime),
    )

    source_id: str
    subchain_triggered_event_id: str
    trigger_start_at: datetime
    trigger_end_at: datetime


@dataclass
class TriggeredEvent(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("event_id", creatable=True),
        ApiField("Event", data_type=Event, attr_key="event"),
        ApiField("owner_id"),
        ApiField("Owner", data_type=dict, attr_key="owner"),
        ApiField("is_public", data_type=bool),
        ApiField(
            "data",
            data_type=lambda o: [TriggeredEventData.from_api(d) for d in loads(o)],
            creatable=True,
            updatable=True,
        ),
        ApiField("trigger_start_at", data_type=Parsers.datetime, creatable=True, updatable=True),
        ApiField("trigger_end_at", data_type=Parsers.datetime, creatable=True, updatable=True),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
        ApiField("deleted_at", data_type=Parsers.datetime),
    )

    event_id: str
    trigger_start_at: datetime
    id: Optional[str]
    owner_id: Optional[str] = None
    owner: Optional[Owner] = None
    event: Optional[Event] = None
    is_public: Optional[bool] = None
    trigger_end_at: Optional[datetime] = None
    data: Optional[dict] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
