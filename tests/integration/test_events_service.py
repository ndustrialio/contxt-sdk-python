from contxt.auth.cli import CliAuth
from contxt.models.events import EventType
from contxt.services import EventsService
from tests.static.data import TestTriggeredEvent


class TestEventsService:
    service = EventsService(CliAuth())

    def test_get_sentence_from_parameters(self):
        event_definition = self.service.get_event_definition(
            TestTriggeredEvent.event_id
        )
        self.service.set_human_readable_parameters(event_definition)
        assert event_definition.human_readable_parameters
        assert isinstance(event_definition.human_readable_parameters, str)

    def test_get_event_types(self):
        event_types = self.service.get_event_types()
        assert all([isinstance(e, EventType) for e in event_types])

    def test_create_event_type(self):
        pass
        # created_event_type = self.service.create_event_type(event_type)
        # assert created_event_type

    def test_get_event(self):
        event = self.service.get_event(TestTriggeredEvent.event_id)
        assert event.id == TestTriggeredEvent.event_id
        assert event.event_type_id == TestTriggeredEvent.event_type_id

    def test_create_event(self):
        pass
        # created_event = self.service.create_event(event)
        # assert created_event

    def test_update_event(self):
        pass
        # self.service.update_event(event)

    def test_delete_event(self):
        pass
        # self.service.delete_event(event)

    def test_get_events_for_type(self):
        events = self.service.get_events_for_type(TestTriggeredEvent.event_type_id)
        assert events
        assert all(e.event_type_id == TestTriggeredEvent.event_type_id for e in events)

    # TODO: figure out a valid client_id
    def test_get_events_for_client(self):
        pass
        # events = self.service.get_events_for_client()
        # assert events

    def test_get_event_definition(self):
        event_definition = self.service.get_event_definition(
            TestTriggeredEvent.event_id
        )
        assert event_definition.event_id == TestTriggeredEvent.event_id

    def test_create_triggered_event(self):
        pass
        # new_triggered_event = TriggeredEvent()
        # created_triggered_event = self.service.create_triggered_event(
        #     new_triggered_event
        # )
        # assert created_triggered_event

    def test_get_triggered_event(self):
        triggered_event = self.service.get_triggered_event(TestTriggeredEvent.id)
        assert triggered_event.id == TestTriggeredEvent.id
        assert triggered_event.event_id == TestTriggeredEvent.event_id
        assert triggered_event.event.event_type_id == TestTriggeredEvent.event_type_id

    def test_update_triggered_event(self):
        pass
        # self.service.update_triggered_event(TestTriggeredEvent.id)

    def test_delete_triggered_event(self):
        pass
        # self.service.delete_triggered_event(TestTriggeredEvent.id)

    def test_get_triggered_events_for_event(self):
        triggered_events = self.service.get_triggered_events_for_event(
            TestTriggeredEvent.event_id
        )
        assert triggered_events
        assert all(
            [t.event_id == TestTriggeredEvent.event_id for t in triggered_events]
        )

    # TODO: find a valid field_id
    def test_get_triggered_events_for_field(self):
        pass
        # triggered_events = self.service.get_triggered_events_for_field(field_id)
        # assert triggered_events
