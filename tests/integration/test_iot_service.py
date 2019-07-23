from datetime import datetime, timedelta

from pytz import UTC

from contxt.auth.cli import CliAuth
from contxt.models.iot import Field, UnprovisionedField
from contxt.services import IotService
from tests.static.data import TestField


class TestIotService:
    service = IotService(CliAuth())

    def test_get_feed_with_id(self, feed_id: int = TestField.feed_id):
        feed = self.service.get_feed_with_id(feed_id)
        assert feed.id == feed_id

    def test_get_feed_with_key(self, feed_key: str = TestField.feed_key):
        feed = self.service.get_feed_with_key(feed_key)
        assert feed
        # assert feed.id == KnownField.feed_id

    def test_get_feeds(self, facility_id: int = TestField.facility_id):
        feeds = self.service.get_feeds(facility_id)
        assert feeds
        assert all([f.facility_id == facility_id for f in feeds])

    def test_get_fields_for_facility(self, facility_id: int = TestField.facility_id):
        fields = self.service.get_fields_for_facility(facility_id)
        assert fields
        assert all([isinstance(f, Field) for f in fields])

    def test_get_fields_for_feed(self, feed_id: int = TestField.feed_id):
        fields = self.service.get_fields_for_feed(feed_id)
        assert fields
        assert all([isinstance(f, Field) for f in fields])

    def test_get_time_series_for_field(self, field: Field = TestField):
        start_time = datetime.now(UTC) - timedelta(days=30)
        field_data = self.service.get_time_series_for_field(
            field=field, start_time=start_time
        )
        assert field_data
        # assert field_data.field_human_name == TestField.field_human_name
        # assert field_data.output_id == TestField.output_id
        # assert field_data.time_series
        # assert min(field_data.time_series.keys()) >= start_time

    def test_get_time_series_for_field_grouping(self):
        pass

    def test_get_unprovisioned_fields_for_feed_id(
        self, feed_id: int = TestField.feed_id
    ):
        fields = self.service.get_unprovisioned_fields_for_feed_id(feed_id)
        assert fields
        assert all([isinstance(f, UnprovisionedField) for f in fields])

    def test_get_unprovisioned_fields_for_feed_key(
        self, feed_key: str = TestField.feed_key
    ):
        fields = self.service.get_unprovisioned_fields_for_feed_key(feed_key)
        assert fields

    def test_get_field_grouping(self, grouping_id: str = TestField.grouping_id):
        grouping = self.service.get_field_grouping(grouping_id)
        assert grouping
        assert grouping.id == grouping_id

    def test_get_field_groupings_for_facility(
        self, facility_id: int = TestField.facility_id
    ):
        groupings = self.service.get_field_groupings_for_facility(facility_id)
        assert groupings
        assert all([g.facility_id == facility_id for g in groupings])
