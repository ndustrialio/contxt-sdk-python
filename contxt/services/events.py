from typing import List, Optional

from contxt.auth import Auth
from contxt.models.events import Event, EventDefinition, EventType, TriggeredEvent
from contxt.services.api import ApiEnvironment, ConfiguredApi
from contxt.services.pagination import PagedRecords, PageOptions
from contxt.utils import make_logger

logger = make_logger(__name__)


class EventsService(ConfiguredApi):
    """
    Service to interact with our Events API.
    """

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="http://events.api.ndustrial.io/v1",
            client_id="7jzwfE20O2XZ4aq3cO1wmk63G9GzNc8j",
        ),
        ApiEnvironment(
            name="staging",
            base_url="http://events-staging.api.ndustrial.io/v1",
            client_id="dn4MaocJFdKtsBy9sFFaTeuJWL1nt5xu",
        ),
    )

    def __init__(self, auth: Auth, env: str = "production"):
        super().__init__(env=env, auth=auth)

    def set_human_readable_parameters(self, event_definition: EventDefinition) -> None:
        statement = ""
        for k, v in event_definition.parameters.items():
            if k == "$chain":
                for d1, d2 in zip(v[:-1], v[1:]):
                    event1 = self.get_event(d1.get("event_id"))
                    event2 = self.get_event(d2.get("event_id"))
                    mins = d1.get("overlap_variance") / 60
                    statement += (
                        f"Event {event1.name} overlaps with {event2.name}"
                        f" within {mins} min "
                    )
        event_definition.human_readable_parameters = statement

    def get_event_types(
        self, page_options: Optional[PageOptions] = None
    ) -> List[EventType]:
        return PagedRecords(
            api=self,
            url="types",
            options=page_options,
            record_parser=EventType.from_api,
        )

    def create_event_type(self, event: Event) -> EventType:
        data = event.post()
        logger.debug(f"Creating event_type with {data}")
        resp = self.post("types", data=data)
        return EventType.from_api(resp)

    def get_event(self, event_id: str) -> Event:
        logger.debug(f"Fetching event {event_id}")
        resp = self.get(f"events/{event_id}")
        return Event.from_api(resp)

    def create_event(self, event: Event) -> Event:
        data = event.post()
        logger.debug(f"Creating event with {data}")
        resp = self.post("events", data=data)
        return Event.from_api(resp)

    def update_event(self, event: Event) -> None:
        # TODO: what are updatable field for an event?
        data = event.put()
        logger.debug(f"Updating event {event.id} with {data}")
        self.put(f"events/{event.id}", data=data)

    def delete_event(self, event: Event) -> None:
        logger.debug(f"Deleting event {event.id}")
        self.delete(f"events/{event.id}")

    def get_events_for_type(
        self, event_type_id: str, page_options: Optional[PageOptions] = None
    ) -> List[Event]:
        logger.debug(f"Fetching events for type {event_type_id}")
        return PagedRecords(
            api=self,
            url=f"types/{event_type_id}/events",
            options=page_options,
            record_parser=Event.from_api,
        )

    def get_events_for_client(self, client_id: str) -> List[Event]:
        logger.debug(f"Fetching events for client {client_id}")
        resp = self.get(f"clients/{client_id}/events")
        return [Event.from_api(rec) for rec in resp]

    def get_event_definition(self, event_id: str) -> EventDefinition:
        logger.debug(f"Fetching definition for event {event_id}")
        resp = self.get(f"events/{event_id}/definition")
        return EventDefinition.from_api(resp)

    def create_triggered_event(self, triggered_event: TriggeredEvent) -> TriggeredEvent:
        data = triggered_event.post()
        logger.debug(f"Creating triggered_event with {data}")
        resp = self.post(f"events/{triggered_event.event_id}/trigger", data=data)
        return TriggeredEvent.from_api(resp)

    def get_triggered_event(self, triggered_event_id: str) -> TriggeredEvent:
        logger.debug(f"Fetching triggered_event {triggered_event_id}")
        resp = self.get(f"triggered/{triggered_event_id}")
        return TriggeredEvent.from_api(resp)

    def update_triggered_event(self, triggered_event: TriggeredEvent) -> None:
        data = triggered_event.put()
        logger.debug(f"Updating triggered_event {triggered_event.id} with {data}")
        self.put(f"triggered/{triggered_event.id}", data=data)

    def delete_triggered_event(self, triggered_event: TriggeredEvent) -> None:
        logger.debug(f"Deleting triggered_event {triggered_event.id}")
        self.delete(f"triggered/{triggered_event.id}")

    def get_triggered_events_for_event(
        self, event_id: str, page_options: Optional[PageOptions] = None
    ) -> List[TriggeredEvent]:
        logger.debug(f"Fetching triggered_events for event {event_id}")
        return PagedRecords(
            api=self,
            url=f"events/{event_id}/triggered",
            options=page_options,
            record_parser=TriggeredEvent.from_api,
        )

    def get_triggered_events_for_field(self, field_id: str) -> List[TriggeredEvent]:
        logger.debug(f"Fetching triggered_events for field {field_id}")
        resp = self.get(f"fields/{field_id}/triggered")
        return [TriggeredEvent.from_api(rec) for rec in resp]
