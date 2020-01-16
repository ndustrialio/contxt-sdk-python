from collections import defaultdict
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

import pytz
from requests import Request

from contxt.auth import Auth
from contxt.models import Parsers
from contxt.models.iot import (
    BatchRequest,
    BatchRequests,
    BatchResponses,
    Feed,
    Field,
    FieldGrouping,
    FieldTimeSeries,
    UnprovisionedField,
    Window,
)
from contxt.services.api import ApiEnvironment, ConfiguredApi
from contxt.services.pagination import PagedRecords, PagedTimeSeries, PageOptions
from contxt.utils import make_logger
from contxt.utils.object_mapper import ObjectMapper

logger = make_logger(__name__)


class IotService(ConfiguredApi):
    """IOT API client

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

    def __init__(self, auth: Auth, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, auth=auth, **kwargs)

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
            api=self, url=f"feeds/{feed_id}/fields", options=page_options, record_parser=Field.from_api
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
        """Get time series data for field `field`"""
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

    def get_time_series_for_fields(
        self,
        fields: List[Field],
        start_time: datetime,
        window: Window = Window.RAW,
        end_time: Optional[datetime] = None,
    ) -> List[FieldTimeSeries]:
        """Get complete (non-paginated) time series data for each field in `fields`"""
        # Build requests queue
        params = {
            "timeStart": int(start_time.timestamp()),
            "timeEnd": int(end_time.timestamp()) if end_time else None,
            "window": window.value,
            "limit": 5000,
        }
        queue: List[Tuple[str, BatchRequest]] = [
            (
                f.field_human_name,
                BatchRequest.from_request(
                    Request(
                        method="GET",
                        url=self._url(f"outputs/{f.output_id}/fields/{f.field_human_name}/data"),
                        params=params,
                    )
                ),
            )
            for f in fields
        ]

        # Make all requests in queue
        MAX_BATCH_REQUESTS = 200
        records: Dict[str, Dict[datetime, str]] = defaultdict(dict)
        while queue:
            # Make next batch of requests
            requests = dict(queue[:MAX_BATCH_REQUESTS])
            del queue[:MAX_BATCH_REQUESTS]
            logger.info(f"Making {len(requests)} batched requests to IOT API")
            responses = self._batch_request(requests)
            any_success = False

            # Process responses
            for name, resp in responses.items():
                if resp.ok:
                    any_success = True
                    series = {
                        Parsers.datetime(r["event_time"]): Parsers.unknown(r["value"])
                        for r in resp.body["records"]
                    }
                    records[name].update(series)
                    # Add request for next page
                    next_page_url = resp.body["meta"]["next_page_url"]
                    if next_page_url:
                        queue.append((name, BatchRequest(method="GET", uri=next_page_url)))
                else:
                    # Retry request
                    logger.warning(f"Got bad response from IOT API ({resp.body}). Retrying...")
                    queue.append((name, requests[name]))

            if not any_success:
                raise IOError(f"All {len(requests)} batched requests to IOT API failed")

        fields_by_name = {f.field_human_name: f for f in fields}
        return [
            FieldTimeSeries(field=fields_by_name[name], time_series=series)
            for name, series in records.items()
        ]

    def get_time_series_for_field_grouping(self, grouping_id: str, **kwargs) -> List[Dict]:
        """Get time series data for fields in grouping with id `grouping_id`"""
        grouping = self.get_field_grouping(grouping_id)
        return [self.get_time_series_for_field(field=f, **kwargs) for f in grouping.fields]

    def get_unprovisioned_fields_for_feed_id(self, feed_id: int) -> List[UnprovisionedField]:
        """Get unprovisioned fields for feed with id `feed_id`"""
        return [
            UnprovisionedField.from_api(rec) for rec in self.get(f"feeds/{feed_id}/fields/unprovisioned")
        ]

    def get_unprovisioned_fields_for_feed_key(self, feed_key: str) -> Optional[List[UnprovisionedField]]:
        """Get unprovisioned fields for feed with key `feed_key`"""
        feed = self.get_feed_with_key(key=feed_key)
        if not feed:
            return None
        return [
            UnprovisionedField.from_api(rec) for rec in self.get(f"feeds/{feed.id}/fields/unprovisioned")
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

    def _batch_request(self, requests: BatchRequests) -> BatchResponses:
        prepared_requests = {label: req.to_api() for label, req in requests.items()}
        resp = self.post("batch", json=prepared_requests)
        return ObjectMapper.tree_to_object(resp, BatchResponses)


class IotDataService(ConfiguredApi):
    """IOT API client

    Terminology
        - Feed: Data source (i.e. utility meter) with a set of fields
        - Field: A specific time series data from a feed
        - Grouping: Group of fields
    """

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://iot.api.ndustrial.io/v2/",
            client_id="ZPrYMWVCcsyYaKKK2uiFLS71X1MB7zJP",
        ),
        ApiEnvironment(
            name="development",
            base_url="http://localhost:8080/v2/",
            client_id="ZPrYMWVCcsyYaKKK2uiFLS71X1MB7zJP",
        ),
    )

    def __init__(self, auth: Auth, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, auth=auth, **kwargs)

    def get_source_data(
        self, source_key: str, start: datetime, resolution: timedelta, end: Optional[datetime] = None
    ):
        """Get the data for the given source"""
        assert start.tzinfo
        assert resolution.total_seconds() == int(resolution.total_seconds())
        params = {
            "start": int(start.timestamp()),
            "end": end or int(datetime.now().timestamp()),
            "resolution": f"P{resolution.days}DT{resolution.seconds}S",
        }
        return self.get(f"sources/{source_key}/data", params=params)

    def get_source_cursor(self, source_key: str) -> datetime:
        """Get the cursor for the given source"""
        body = self.get(f"sources/{source_key}/cursor")
        assert (
            body["source_key"] == source_key
        ), f"Got unexpected source key on response. Requested {source_key}, but got {body['source_key']}"
        epoch = body["cursor_epoch"]
        if epoch:
            return datetime.fromtimestamp(epoch, tz=pytz.UTC)
        return None
