from collections import defaultdict
from copy import deepcopy
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Iterable, List, Optional, Tuple

from requests import Request

from ..auth import Auth
from ..models import Parsers
from ..models.iot import (
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
from ..utils import is_datetime_aware, make_logger
from ..utils.object_mapper import ObjectMapper
from .api import ApiEnvironment, ConfiguredApi
from .pagination import DataPoint, PagedRecords, PagedTimeSeries, PageOptions

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
        ApiEnvironment(
            name="staging",
            base_url="https://feeds-staging.api.ndustrial.io/v1",
            client_id="m35AEcxD8hf65sq04ZU7yFxqpqVkKzES",
        ),
    )

    def __init__(self, auth: Auth, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, auth=auth, **kwargs)

    def provision_field_for_feed(self, feed_id: int, field: Field) -> Field:
        resp = self.post(f"feeds/{feed_id}/fields", data=field.post())
        return Field.from_api(resp)

    def create_grouping(
        self, facility_id: int, label: str, description: str, is_public: bool, field_category_id: str
    ) -> FieldGrouping:
        res = self.post(
            f"facilities/{facility_id}/groupings",
            json={
                "label": label,
                "description": description,
                "is_public": is_public,
                "fileds": field_category_id,
            },
        )
        return FieldGrouping.from_api(res)

    def add_field_to_grouping(self, grouping_id: int, field_id: int):
        return self.post(f"groupings/{grouping_id}/fields/{field_id}")

    def set_fields_for_grouping(self, grouping_id: str, fields: List[str]):
        return self.post(f"groupings/{grouping_id}/fields", json={"fields": fields})

    def unprovision_field(self, field_id: int):
        return self.delete(uri=f"fields/{field_id}")

    def delete_time_series_point(
        self, output_id: int, field: str, interval: Window, time: datetime
    ) -> Optional[Dict]:
        """Delete a point from the time series data by interval and timestamp"""
        return self.delete(
            f"outputs/{output_id}/fields/{field}/data/window/{interval.value}/event_time/{time}"
        )

    def get_feed_with_id(self, id: int) -> Feed:
        """Get feed with id `id`"""
        return Feed.from_api(self.get(f"feeds/{id}"))

    def get_feed_with_key(self, key: str) -> Optional[Feed]:
        """Get feed with key `key`"""
        feeds = self.get_feeds(key=key)
        N = len(feeds)  # type: ignore
        if N == 0:
            return None
        elif N == 1:
            return feeds[0]  # type: ignore
        raise KeyError(f"Expected singleton feed with key {key}, not {N}")

    def get_feeds(
        self,
        facility_id: Optional[int] = None,
        key: Optional[str] = None,
        page_options: Optional[PageOptions] = None,
    ) -> Iterable[Feed]:
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
    ) -> Iterable[Field]:
        """Get fields for facility with id `facility_id`"""
        return PagedRecords(
            api=self,
            url=f"facilities/{facility_id}/fields",
            options=page_options,
            record_parser=Field.from_api,
        )

    def get_fields_for_feed(
        self, feed_id: int, page_options: Optional[PageOptions] = None
    ) -> Iterable[Field]:
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
        start_time: datetime = None,
        window: Window = Window.RAW,
        end_time: Optional[datetime] = None,
        per_page: int = 1000,
    ) -> Iterable[DataPoint]:
        """Get time series data for field `field`"""
        # Manually validate the window choice, since our API does not return a
        # helpful error message
        assert isinstance(window, Window), "window must be of type Window"
        assert (start_time is None) == (
            end_time is None
        ), "Either both start and end time should be provided, or both should be missing"
        return PagedTimeSeries(
            api=self,
            url=f"outputs/{field.output_id}/fields/{field.field_human_name}/data",
            params={
                "timeStart": int(start_time.timestamp()) if start_time else None,
                "timeEnd": int(end_time.timestamp()) if end_time else None,
                "window": window.value,
            },
            per_page=per_page,
        )

    def get_time_series_for_fields(
        self,
        fields: List[Field],
        start_time: datetime = None,
        window: Window = Window.RAW,
        end_time: Optional[datetime] = None,
    ) -> List[FieldTimeSeries]:
        """Get complete (non-paginated) time series data for each field in `fields`"""
        assert (start_time is None) == (
            end_time is None
        ), "Either both start and end time should be provided, or both should be missing"
        # Build requests queue
        params = {
            "timeStart": int(start_time.timestamp()) if start_time else None,
            "timeEnd": int(end_time.timestamp()) if end_time else None,
            "window": window.value,
            "limit": 5000,
        }
        queue: List[Tuple[str, BatchRequest]] = [
            (
                f.field_human_name,  # type: ignore
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

    def get_time_series_for_field_grouping(
        self, grouping_id: str, **kwargs
    ) -> List[Iterable[DataPoint]]:
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
    ) -> Iterable[FieldGrouping]:
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


def format_time_series(feed_key: str, time_series: Dict[str, Dict[datetime, float]]) -> Dict:
    # Enforce all datetimes are tz-aware
    assert all(
        is_datetime_aware(dt) for time_series in time_series.values() for dt in time_series.keys()
    ), "Timezone-aware datetimes required"

    # Format for request
    return {
        "feedKey": feed_key,
        "type": "timeseries",
        "data": [
            {
                "timestamp": dt.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
                "data": {field_descriptor: {"value": str(value)}},
            }
            for field_descriptor, series in time_series.items()
            for dt, value in series.items()
        ],
    }


NgestField = str
NgestRecord = Tuple[datetime, Dict[NgestField, Any]]


class IotDataService(ConfiguredApi):
    """IOT API client v2.0

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

    def __init__(self, org_id: str, auth: Auth, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, auth=auth, **kwargs)
        self.org_id = org_id

    def get_source_data(
        self, source_key: str, start: datetime, resolution: timedelta, end: Optional[datetime] = None
    ):
        """Get the data for the given source"""
        assert start.tzinfo
        assert resolution.total_seconds() == int(resolution.total_seconds())
        params = {
            "start": int(start.timestamp()),
            "end": int(end.timestamp()) if end else int(datetime.now().timestamp()),
            "resolution": f"P{resolution.days}DT{resolution.seconds}S",
        }
        return self.get(f"org/{self.org_id}/sources/{source_key}/data", params=params)

    def get_source_cursor(self, source_key: str) -> Optional[datetime]:
        """Get the cursor for the given source"""
        body = self.get(f"org/{self.org_id}/sources/{source_key}/cursor")
        assert (
            body["source_key"] == source_key
        ), f"Got unexpected source key on response. Requested {source_key}, but got {body['source_key']}"
        epoch = body["cursor_epoch"]
        if epoch:
            return datetime.fromtimestamp(epoch, tz=timezone.utc)
        return None

    def ingest_source_data(
        self, source_key: str, data: List[NgestRecord], batch_size: int = 50
    ) -> List[Dict]:
        responses = []
        tail = data
        while tail:
            batch, tail = tail[:batch_size], tail[batch_size:]
            _data = []
            for record in batch:
                dt, field_values = record
                assert is_datetime_aware(dt), f"Ngest requires timezone-aware datetimes, got: {dt}"
                _data.append(
                    {
                        "timestamp": dt.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
                        "data": {k: {"value": str(v)} for k, v in field_values.items()},
                    }
                )
            msg = {"feedKey": source_key, "type": "timeseries", "data": _data}

            # Make request
            response = self.post(f"org/{self.org_id}/ngest/{source_key}", json=msg)
            if response["status"] != "ok":
                logger.warning(f"{self.__class__.__name__}: got status {response['status']}")
            responses.append(response)

        return responses

    # fixme: deprecated
    def send_time_series(
        self, feed_key: str, time_series: Dict[str, Dict[datetime, float]], per_request: int = 50
    ) -> List[Dict]:
        """
        This method is deprecated, use ingest_source_data instead

        Sends time series data for field(s).

        :param feed_key: feed's key
        :type feed_key: str
        :param time_series: dictionary of field descriptors to a time series dictionary
        :type time_series: Dict[str, Dict[datetime, float]]
        :param per_request: number of datapoints to send per request, defaults to 50
        :type per_request: int, optional
        :return: responses
        :rtype: List[Dict]
        """
        # Prepare data for request
        data = format_time_series(feed_key=feed_key, time_series=time_series)

        # Send the time series in chunks, partitioned by `per_request`
        responses = []
        while data["data"]:
            # Create chunk for next request
            chunk = deepcopy(data)
            chunk["data"] = data["data"][:per_request]

            # Make request
            response = self.post(f"org/{self.org_id}/ngest/{feed_key}", json=chunk)
            if response["status"] != "ok":
                logger.warning(f"{self.__class__.__name__}: got status {response['status']}")
            responses.append(response)

            # Update remaining data
            data["data"] = data["data"][per_request:]

        return responses

    def get_source_field_cursor(self, source_key: str, field_name: str = None) -> Optional[datetime]:
        """Get the cursor for the given source and field"""

        url = f"org/{self.org_id}/sources/{source_key}"
        if field_name is not None:
            url += f"/fields/{field_name}"
        url += "/cursor"

        body = self.get(url)
        assert (
            body["source_key"] == source_key
        ), f"Got unexpected source key on response. Requested {source_key}, but got {body['source_key']}"
        epoch = body["cursor_epoch"]
        if epoch:
            return datetime.fromtimestamp(epoch, tz=timezone.utc)
        return None
