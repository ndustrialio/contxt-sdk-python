import pytest

from contxt.auth.cli import CliAuth
from contxt.services import MessageBusService
from tests.static.data import TestChannel


class TestMessageBusService:
    service = MessageBusService(
        auth=CliAuth(), organization_id=TestChannel.organization_id
    )

    def test_get_channel_for_service(self):
        channel = self.service.get_channel_for_service(
            TestChannel.id, TestChannel.service_id
        )
        assert channel.id == TestChannel.id
        assert channel.service_id == TestChannel.service_id
        assert channel.organization_id == self.service.organization_id

    def test_get_channels_for_service(self):
        channels = self.service.get_channels_for_service(TestChannel.service_id)
        assert channels
        assert all(
            [c.organization_id == self.service.organization_id for c in channels]
        )
        assert all([c.service_id == TestChannel.service_id for c in channels])

    @pytest.mark.skip(reason="No schemas exist for test channel")
    def test_get_schema_for_channel_and_service(self):
        schema = self.service.get_schema_for_channel_and_service(
            schema_id=TestChannel.schema_id,
            channel_id=TestChannel.id,
            service_id=TestChannel.service_id,
        )
        assert schema

    @pytest.mark.skip(reason="No schemas exist for test channel")
    def test_get_schemas_for_channel_and_service(self):
        schemas = self.service.get_schemas_for_channel_and_service(
            TestChannel.id, TestChannel.service_id
        )
        assert schemas

    @pytest.mark.skip(reason="No stats exist for test channel")
    def test_get_stats_for_channel_and_service(self):
        stats = self.service.get_stats_for_channel_and_service(
            TestChannel.id, TestChannel.service_id
        )
        assert stats
