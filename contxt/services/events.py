from typing import Any, Dict, List, Optional, Set, Tuple, Union

from contxt.auth.cli import CLIAuth
from contxt.models.events import (Event, EventDefinition, EventType,
                                  TriggeredEvent)
from contxt.services.api import ApiServiceConfig, ConfiguredApiService
from contxt.utils import make_logger

logger = make_logger(__name__)


class EventsService(ConfiguredApiService):
    """
    Service to interact with our Events API.
    """
    _configs = (
        ApiServiceConfig(
            name="production",
            base_url="http://events.api.ndustrial.io",
            audience="7jzwfE20O2XZ4aq3cO1wmk63G9GzNc8j"),
        ApiServiceConfig(
            name="staging",
            base_url="http://events-staging.api.ndustrial.io",
            audience="dn4MaocJFdKtsBy9sFFaTeuJWL1nt5xu"),
    )

    def __init__(
            self,
            auth: CLIAuth,
            env: str = "production"
    ):
        super().__init__(auth, env)

    def event_definition_parameters_to_human_readable_format(self, event_definition: EventDefinition):
        statement = ""
        for k, v in event_definition.parameters.items():
            if k == "$chain":
                for d1, d2 in zip(v[:-1], v[1:]):
                    event1 = self.get_event(d1.get("event_id"))
                    event2 = self.get_event(d2.get("event_id"))
                    mins = d1.get("overlap_variance") / 60
                    statement += f"Event {event1.name} overlaps with {event2.name} within {mins} min "
        return statement

    def get_event_types(self) -> List[EventType]:
        resp = self.get("types")
        return [EventType.from_api(rec) for rec in resp]

    def create_event_type(self, event) -> EventType:
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

    def update_event(self, event: Event):
        # TODO: what are updatable field for an event?
        data = event.put()
        logger.debug(f"Updating event {event.id} with {data}")
        self.put(f"events/{event.id}", data=data)

    def delete_event(self, event: Event):
        logger.debug(f"Deleting event {event.id}")
        self.delete(f"events/{event.id}")

    def get_events_for_type(self, event_type_id: str) -> List[EventType]:
        logger.debug(f"Fetching events for type {event_type_id}")
        resp = self.get(f"types/{event_type_id}/events")
        return [EventType.from_api(rec) for rec in resp]

    def get_events_for_client(self, client_id: str) -> List[EventType]:
        logger.debug(f"Fetching events for client {client_id}")
        resp = self.get(f"clients/{client_id}/events")
        return [EventType.from_api(rec) for rec in resp]

    def get_event_definition(self, event_id: str) -> EventDefinition:
        logger.debug(f"Fetching definition for event {event_id}")
        resp = self.get(f"events/{event_id}/definition")
        return EventDefinition.from_api(resp)

    def create_triggered_event(
            self, triggered_event: TriggeredEvent) -> TriggeredEvent:
        data = triggered_event.post()
        logger.debug(f"Creating triggered_event with {data}")
        resp = self.post(
            f"events/{triggered_event.event_id}/trigger", data=data)
        return TriggeredEvent.from_api(resp)

    def get_triggered_event(self, triggered_event_id: str) -> TriggeredEvent:
        logger.debug(f"Fetching triggered_event {triggered_event_id}")
        resp = self.get(f"triggered/{triggered_event_id}")
        return TriggeredEvent.from_api(resp)

    def update_triggered_event(self, triggered_event):
        data = triggered_event.put()
        logger.debug(
            f"Updating triggered_event {triggered_event.id} with {data}")
        self.put(f"triggered/{triggered_event.id}", data=data)

    def delete_triggered_event(self, triggered_event: TriggeredEvent):
        logger.debug(f"Deleting triggered_event {triggered_event.id}")
        self.delete(f"triggered/{triggered_event.id}")

    def get_triggered_events_for_event(self,
                                       event_id: str) -> List[TriggeredEvent]:
        logger.debug(f"Fetching triggered_events for event {event_id}")
        resp = self.get(f"events/{event_id}/triggered")
        return [TriggeredEvent.from_api(rec) for rec in resp]

    def get_triggered_events_for_field(self, field_id):
        logger.debug(f"Fetching triggered_events for field {field_id}")
        resp = self.get(f"fields/{field_id}/triggered")
        return [TriggeredEvent.from_api(rec) for rec in resp]
