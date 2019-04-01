from __future__ import annotations

from datetime import date, datetime, timedelta
from json import loads
from typing import Any, Dict, List, Optional, Set, Tuple, Union

from contxt.services.api import ApiField, ApiObject, Parsers
from contxt.utils import make_logger

logger = make_logger(__name__)


class EventType(ApiObject):
    api_fields = (
        ApiField("id"),
        ApiField("name", creatable=True),
        ApiField("slug", creatable=True),
        ApiField("description", creatable=True),
        ApiField("client_id", creatable=True),
        ApiField("level", type=int, creatable=True),
        ApiField("is_ongoing_event", type=bool),
        ApiField("is_realtime_enabled", type=bool, creatable=True),
        ApiField("created_at", type=Parsers.datetime),
        ApiField("updated_at", type=Parsers.datetime)
    )

    def __init__(
            self,
            name: str,
            slug: str,
            description: str,
            client_id: str,
            level: int,
            is_ongoing_event: bool,
            id: Optional[str] = None,
            is_realtime_enabled: Optional[bool] = False,
            created_at: Optional[datetime] = None,
            updated_at: Optional[datetime] = None,
    ):
        self.id = id
        self.name = name
        self.slug = slug
        self.client_id = client_id
        self.description = description
        self.level = level
        self.is_ongoing_event = is_ongoing_event
        self.is_realtime_enabled = is_realtime_enabled
        self.created_at = created_at
        self.updated_at = updated_at


class EventDefinition(ApiObject):
    api_fields = (
        ApiField("id"),
        ApiField("event_id"),
        ApiField("description"),
        ApiField("parameters", type=lambda o: loads(o.replace('\"', '"'))),
        ApiField("created_at", type=Parsers.datetime),
        ApiField("updated_at", type=Parsers.datetime),
    )

    def __init__(
            self,
            event_id: str,
            description: str,
            parameters: dict,
            created_at: datetime,
            updated_at: datetime,
            id: Optional[str] = None,
    ):
        self.id = id
        self.event_id = event_id
        self.description = description
        self.parameters = parameters
        self.created_at = created_at
        self.updated_at = updated_at


class Event(ApiObject):
    api_fields = (
        ApiField("id"),
        ApiField("name", creatable=True),
        ApiField("event_type_id", creatable=True),
        ApiField("organization_id", creatable=True),
        ApiField("facility_id", creatable=True),
        ApiField("owner_id"),
        ApiField("allow_others_to_trigger", creatable=True),
        ApiField("is_public", creatable=True),
        ApiField("created_at", type=Parsers.datetime),
        ApiField("updated_at", type=Parsers.datetime),
        ApiField("deleted_at", type=Parsers.datetime),
    )

    def __init__(
            self,
            name: str,
            event_type_id: str,
            organization_id: str,
            allow_others_to_trigger: bool,
            is_public: bool,
            id: Optional[str] = None,
            facility_id: Optional[int] = None,
            owner_id: Optional[str] = None,
            created_at: Optional[datetime] = None,
            updated_at: Optional[datetime] = None,
            deleted_at: Optional[datetime] = None,
    ):
        self.id = id
        self.name = name
        self.event_type_id = event_type_id
        self.facility_id = facility_id
        self.organization_id = organization_id
        self.owner_id = owner_id
        self.allow_others_to_trigger = allow_others_to_trigger
        self.is_public = is_public
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at


class Owner(ApiObject):

    def __init__(self, **kwargs):
        pass


class TriggeredEvent(ApiObject):
    api_fields = (
        ApiField("id"),
        ApiField("event_id", creatable=True),
        ApiField("Event", type=Event, attr_key="event"),
        ApiField("owner_id"),
        ApiField("Owner", type=dict, attr_key="owner"),
        ApiField("is_public"),
        ApiField("data", type=lambda o: loads(o), creatable=True, updatable=True),
        ApiField("trigger_start_at", type=Parsers.datetime, creatable=True, updatable=True),
        ApiField("trigger_end_at", type=Parsers.datetime, creatable=True, updatable=True),
        ApiField("created_at", type=Parsers.datetime),
        ApiField("updated_at", type=Parsers.datetime),
        ApiField("deleted_at", type=Parsers.datetime),
    )

    def __init__(
            self,
            event_id: str,
            trigger_start_at: datetime,
            id: Optional[str],
            owner_id: Optional[str] = None,
            owner: Optional[Owner] = None,
            event: Optional[Event] = None,
            is_public: Optional[bool] = False,
            trigger_end_at: Optional[datetime] = None,
            data: Optional[dict] = None,
            created_at: Optional[datetime] = None,
            updated_at: Optional[datetime] = None,
            deleted_at: Optional[datetime] = None,
    ):
        self.id = id
        self.event_id = event_id
        self.event = event
        self.owner_id = owner_id
        self.owner = owner
        self.is_public = is_public
        self.data = data
        self.trigger_start_at = trigger_start_at
        self.trigger_end_at = trigger_end_at
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
