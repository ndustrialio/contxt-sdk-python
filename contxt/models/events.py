from datetime import datetime
from json import loads
from typing import Optional

from contxt.models import ApiField, ApiObject, Parsers
from contxt.utils import make_logger

logger = make_logger(__name__)


class EventType(ApiObject):
    _api_fields = (
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

    def __init__(
        self,
        name: str,
        slug: str,
        description: str,
        client_id: str,
        level: int,
        id: Optional[str] = None,
        is_ongoing_event: Optional[bool] = None,
        is_realtime_enabled: Optional[bool] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        super().__init__()
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
    _api_fields = (
        ApiField("id"),
        ApiField("event_id"),
        ApiField("description"),
        ApiField("parameters", data_type=lambda o: loads(o.replace('"', '"'))),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    def __init__(
        self,
        event_id: str,
        description: str,
        parameters: dict,
        created_at: datetime,
        updated_at: datetime,
        id: Optional[str] = None,
        human_readable_parameters: Optional[str] = None,
    ) -> None:
        super().__init__()
        self.id = id
        self.event_id = event_id
        self.description = description
        self.parameters = parameters
        self.human_readable_parameters = human_readable_parameters
        self.created_at = created_at
        self.updated_at = updated_at


class Owner(ApiObject):
    _api_fields = (
        ApiField("id"),
        ApiField("first_name"),
        ApiField("last_name"),
        ApiField("email"),
        ApiField("is_machine_user", data_type=bool, optional=True),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    def __init__(
        self,
        id: str,
        first_name: str,
        last_name: str,
        email: str,
        is_machine_user: bool,
        created_at: datetime,
        updated_at: datetime,
    ) -> None:
        super().__init__()
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_machine_user = is_machine_user
        self.created_at = created_at
        self.updated_at = updated_at


class Event(ApiObject):
    _api_fields = (
        ApiField("id"),
        ApiField("name", creatable=True),
        ApiField("event_type_id", creatable=True),
        ApiField(
            "EventType", attr_key="event_type", data_type=EventType, optional=True
        ),
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
        owner: Optional[Owner] = None,
        event_type: Optional[EventType] = None,
        topic_arn: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        deleted_at: Optional[datetime] = None,
    ) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.event_type_id = event_type_id
        self.event_type = event_type
        self.facility_id = facility_id
        self.organization_id = organization_id
        self.owner_id = owner_id
        self.owner = owner
        self.topic_arn = topic_arn
        self.allow_others_to_trigger = allow_others_to_trigger
        self.is_public = is_public
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at


class TriggeredEventData(ApiObject):
    _api_fields = (
        ApiField("source_id"),
        ApiField("subchain_triggered_event_id"),
        ApiField("trigger_start_at", data_type=Parsers.datetime),
        ApiField("trigger_end_at", data_type=Parsers.datetime),
    )

    def __init__(
        self,
        source_id: str,
        subchain_triggered_event_id: str,
        trigger_start_at: datetime,
        trigger_end_at: datetime,
    ) -> None:
        super().__init__()
        self.source_id = source_id
        self.subchain_triggered_event_id = subchain_triggered_event_id
        self.trigger_start_at = trigger_start_at
        self.trigger_end_at = trigger_end_at


class TriggeredEvent(ApiObject):
    _api_fields = (
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
        ApiField(
            "trigger_start_at",
            data_type=Parsers.datetime,
            creatable=True,
            updatable=True,
        ),
        ApiField(
            "trigger_end_at", data_type=Parsers.datetime, creatable=True, updatable=True
        ),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
        ApiField("deleted_at", data_type=Parsers.datetime),
    )

    def __init__(
        self,
        event_id: str,
        trigger_start_at: datetime,
        id: Optional[str],
        owner_id: Optional[str] = None,
        owner: Optional[Owner] = None,
        event: Optional[Event] = None,
        is_public: Optional[bool] = None,
        trigger_end_at: Optional[datetime] = None,
        data: Optional[dict] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        deleted_at: Optional[datetime] = None,
    ) -> None:
        super().__init__()
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
