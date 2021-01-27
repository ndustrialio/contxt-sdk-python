from typing import Iterable, List, Optional

from ..auth import Auth
from ..models.events import Event, EventDefinition, EventType, TriggeredEvent
from .api import ApiEnvironment, ConfiguredApi
from .pagination import PagedRecords, PageOptions


class EventsService(ConfiguredApi):
    """Events API client"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://events.api.ndustrial.io/v1",
            client_id="7jzwfE20O2XZ4aq3cO1wmk63G9GzNc8j",
        ),
        ApiEnvironment(
            name="staging",
            base_url="https://events-staging.api.ndustrial.io/v1",
            client_id="dn4MaocJFdKtsBy9sFFaTeuJWL1nt5xu",
        ),
    )

    def __init__(self, auth: Auth, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, auth=auth, **kwargs)

    def set_human_readable_parameters(self, event_definition: EventDefinition) -> None:
        statement = ""
        for k, v in event_definition.parameters.items():
            if k == "$chain":
                for d1, d2 in zip(v[:-1], v[1:]):
                    event1 = self.get_event(d1.get("event_id"))
                    event2 = self.get_event(d2.get("event_id"))
                    mins = d1.get("overlap_variance") / 60
                    statement += f"Event {event1.name} overlaps with {event2.name} within {mins} min "
        event_definition.human_readable_parameters = statement

    def get_event_types(self, page_options: Optional[PageOptions] = None) -> Iterable[EventType]:
        return PagedRecords(
            api=self, url="types", options=page_options, record_parser=EventType.from_api
        )

    def create_event_type(self, event_type: EventType) -> EventType:
        resp = self.post("types", data=event_type.post())
        return EventType.from_api(resp)

    def get_event(self, event_id: str) -> Event:
        resp = self.get(f"events/{event_id}")
        return Event.from_api(resp)

    def create_event(self, event: Event) -> Event:
        resp = self.post("events", data=event.post())
        return Event.from_api(resp)

    def update_event(self, event: Event) -> None:
        self.put(f"events/{event.id}", data=event.put())

    def delete_event(self, event: Event) -> None:
        self.delete(f"events/{event.id}")

    def get_events_for_type(
        self, event_type_id: str, page_options: Optional[PageOptions] = None
    ) -> Iterable[Event]:
        return PagedRecords(
            api=self,
            url=f"types/{event_type_id}/events",
            options=page_options,
            record_parser=Event.from_api,
        )

    def get_events_for_client(self, client_id: str) -> List[Event]:
        resp = self.get(f"clients/{client_id}/events")
        return [Event.from_api(rec) for rec in resp]

    def get_event_definition(self, event_id: str) -> EventDefinition:
        resp = self.get(f"events/{event_id}/definition")
        return EventDefinition.from_api(resp)

    def create_triggered_event(self, triggered_event: TriggeredEvent) -> TriggeredEvent:
        resp = self.post(f"events/{triggered_event.event_id}/trigger", data=triggered_event.post())
        return TriggeredEvent.from_api(resp)

    def get_triggered_event(self, triggered_event_id: str) -> TriggeredEvent:
        resp = self.get(f"triggered/{triggered_event_id}")
        return TriggeredEvent.from_api(resp)

    def update_triggered_event(self, triggered_event: TriggeredEvent) -> None:
        self.put(f"triggered/{triggered_event.id}", data=triggered_event.put())

    def delete_triggered_event(self, triggered_event: TriggeredEvent) -> None:
        self.delete(f"triggered/{triggered_event.id}")

    def get_triggered_events_for_event(
        self, event_id: str, page_options: Optional[PageOptions] = None
    ) -> Iterable[TriggeredEvent]:
        return PagedRecords(
            api=self,
            url=f"events/{event_id}/triggered",
            options=page_options,
            record_parser=TriggeredEvent.from_api,
        )

    def get_triggered_events_for_field(self, field_id: str) -> List[TriggeredEvent]:
        resp = self.get(f"fields/{field_id}/triggered")
        return [TriggeredEvent.from_api(rec) for rec in resp]
