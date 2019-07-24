from datetime import datetime
from typing import Dict, List, Optional

from contxt.auth import Auth
from contxt.models.iot import (
    Feed,
    Field,
    FieldGrouping,
    FieldTimeSeries,
    UnprovisionedField,
    Window,
)
from contxt.services.api import ApiEnvironment, ConfiguredApi
from contxt.services.pagination import PagedRecords, PagedTimeSeries, PageOptions


class IotService(ConfiguredApi):
    """
    Service to interact with our IOT API.

    Terminology
        - Feed: Data source (i.e. utility meter) with a set of fields
        - Field: A specific time series data from a feed
        - Grouping: Group of fields
    """

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://feeds.api.ndustrial.io/v1",
            client_id="iznTb30Sfp2Jpaf398I5DN6MyPuDCftA",
        ),
    )

    def __init__(self, auth: Auth, env: str = "production"):
        super().__init__(env=env, auth=auth)

    def get_feed_with_id(self, id: int) -> Feed:
        """Get feed with id `id`"""
        return Feed.from_api(self.get(f"feeds/{id}"))

    def get_feed_with_key(self, key: str) -> Optional[Feed]:
        """Get feed with key `key`"""
        feeds = self.get_feeds(key=key)
        if len(feeds) == 0:
            return None
        elif len(feeds) == 1:
            return feeds[0]
        raise KeyError(f"Expected singleton feed with key {key}, not {len(feeds)}")

    def get_feeds(
        self,
        facility_id: Optional[int] = None,
        key: Optional[str] = None,
        page_options: Optional[PageOptions] = None,
    ) -> List[Feed]:
        """Get feeds with facility id `facility_id` and/or key `key`"""
        return PagedRecords(
            api=self,
            url="feeds",
            params={"facility_id": facility_id, "key": key},
            options=page_options,
            record_parser=Feed.from_api,
        )

    def get_fields_for_facility(
        self, facility_id: int, page_options: Optional[PageOptions] = None
    ) -> List[Field]:
        """Get fields for facility with id `facility_id`"""
        return PagedRecords(
            api=self,
            url=f"facilities/{facility_id}/fields",
            options=page_options,
            record_parser=Field.from_api,
        )

    def get_fields_for_feed(
        self, feed_id: int, page_options: Optional[PageOptions] = None
    ) -> List[Field]:
        """Get fields for feed with id `feed_id`"""
        return PagedRecords(
            api=self,
            url=f"feeds/{feed_id}/fields",
            options=page_options,
            record_parser=Field.from_api,
        )

    def create_field(self, field: Field) -> Field:
        """Create field"""
        data = field.post()
        resp = self.post(f"outputs/{field.output_id}/fields", data=data)
        return Field.from_api(resp)

    def get_time_series_for_field(
        self,
        field: Field,
        start_time: datetime,
        window: Window = Window.RAW,
        end_time: Optional[datetime] = None,
        per_page: int = 1000,
    ) -> FieldTimeSeries:
        """Get time series data for field `Field`"""
        # Manually validate the window choice, since our API does not return a
        # helpful error message
        assert isinstance(window, Window), "window must be of type Window"
        return PagedTimeSeries(
            api=self,
            url=f"outputs/{field.output_id}/fields/{field.field_human_name}/data",
            params={
                "timeStart": int(start_time.timestamp()),
                "timeEnd": int(end_time.timestamp()) if end_time else None,
                "window": window.value,
            },
            per_page=per_page,
        )

    def get_time_series_for_field_grouping(
        self, grouping_id: str, **kwargs
    ) -> List[Dict]:
        """Get time series data for fields in grouping with id `grouping_id`"""
        grouping = self.get_field_grouping(grouping_id)
        return [
            self.get_time_series_for_field(field=f, **kwargs) for f in grouping.fields
        ]

    def get_unprovisioned_fields_for_feed_id(
        self, feed_id: int
    ) -> List[UnprovisionedField]:
        """Get unprovisioned fields for feed with id `feed_id`"""
        return [
            UnprovisionedField.from_api(rec)
            for rec in self.get(f"feeds/{feed_id}/fields/unprovisioned")
        ]

    def get_unprovisioned_fields_for_feed_key(
        self, feed_key: str
    ) -> Optional[List[UnprovisionedField]]:
        """Get unprovisioned fields for feed with key `feed_key`"""
        feed = self.get_feed_with_key(key=feed_key)
        if not feed:
            return None
        return [
            UnprovisionedField.from_api(rec)
            for rec in self.get(f"feeds/{feed.id}/fields/unprovisioned")
        ]

    def get_field_grouping(self, id: str) -> FieldGrouping:
        """Get field grouping with id `id`"""
        return FieldGrouping.from_api(self.get(f"groupings/{id}"))

    def get_field_groupings_for_facility(
        self, facility_id: int, page_options: Optional[PageOptions] = None
    ) -> List[FieldGrouping]:
        """Get field groupings for facility with id `facility_id`"""
        return PagedRecords(
            api=self,
            url=f"facilities/{facility_id}/groupings",
            options=page_options,
            record_parser=FieldGrouping.from_api,
        )
