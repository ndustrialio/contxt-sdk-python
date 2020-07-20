from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from json import loads
from typing import Any, ClassVar, Dict, List, Optional

from requests import Request

from . import ApiField, ApiObject, Parsers
from .events import Owner


class Window(Enum):
    RAW = 0
    MINUTELY = 60
    QUARTER_HOURLY = 900
    HOURLY = 3600


class FieldValueType(Enum):
    BOOLEAN = "boolean"
    NUMERIC = "numeric"
    STRING = "string"


@dataclass
class Field(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id", data_type=int),
        ApiField("field_name", attr_key="name", optional=True),
        ApiField("label", creatable=True, updatable=True),
        ApiField("output_id", data_type=int, creatable=True),
        ApiField("field_descriptor", creatable=True),
        ApiField("field_human_name"),
        ApiField("units", creatable=True, updatable=True),
        ApiField("scalar", data_type=float, optional=True, creatable=True, updatable=True),
        ApiField("divisor", data_type=float, optional=True, creatable=True, updatable=True),
        ApiField("value_type", data_type=FieldValueType, optional=True, creatable=True),
        ApiField("feed_key", optional=True, creatable=True),
        ApiField("FieldGroupingField", attr_key="field_grouping_field", data_type=dict, optional=True),
        ApiField("is_hidden", data_type=bool, creatable=True, updatable=True, optional=True),
        ApiField("is_default", data_type=bool, optional=True, creatable=True, updatable=True),
        ApiField("is_totalizer", data_type=bool, optional=True),
        ApiField("can_aggregate", data_type=bool, optional=True),
        ApiField("is_windowed", data_type=bool, optional=True),
        ApiField("status", optional=True),
        ApiField("created_at", data_type=Parsers.datetime, optional=True),
        ApiField("updated_at", data_type=Parsers.datetime, optional=True),
    )

    label: str
    output_id: str
    field_descriptor: str
    units: str
    id: Optional[int] = None
    name: Optional[str] = None
    field_human_name: Optional[str] = None
    feed_key: Optional[str] = None
    field_grouping_field: Optional[Dict] = None
    value_type: Optional[FieldValueType] = None
    scalar: Optional[float] = None
    divisor: Optional[float] = None
    is_hidden: Optional[bool] = None
    is_totalizer: Optional[bool] = None
    is_windowed: Optional[bool] = None
    is_default: Optional[bool] = None
    can_aggregate: Optional[bool] = None
    status: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class FieldCategory(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("name"),
        ApiField("description"),
        ApiField("organization_id"),
        ApiField("parent_category_id"),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: str
    name: str
    description: str
    organization_id: str
    parent_category_id: str
    created_at: datetime
    updated_at: datetime


@dataclass
class FieldGrouping(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("label"),
        ApiField("slug"),
        ApiField("description"),
        ApiField("facility_id", data_type=int),
        ApiField("owner_id"),
        ApiField("is_public", data_type=bool),
        ApiField("field_category_id"),
        ApiField("Owner", attr_key="owner", data_type=Owner),
        ApiField("FieldCategory", attr_key="field_category", data_type=FieldCategory),
        ApiField("Fields", attr_key="fields", data_type=Field),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: str
    label: str
    slug: str
    description: str
    facility_id: int
    is_public: bool
    owner_id: str
    owner: Owner
    field_category_id: str
    field_category: FieldCategory
    fields: List[Field]
    created_at: datetime
    updated_at: datetime


@dataclass
class UnprovisionedField(ApiObject):
    _api_fields: ClassVar = (ApiField("field_descriptor"), ApiField("assumed_type"))

    field_descriptor: str
    assumed_type: str


@dataclass
class Feed(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id", data_type=int),
        ApiField("feed_type_id", data_type=int),
        ApiField("down_after"),
        ApiField("key"),
        ApiField("facility_id", data_type=int),
        ApiField("timezone"),
        ApiField("token"),
        ApiField("status"),
        ApiField("degraded_threshold", data_type=float),
        ApiField("critical_threshold", data_type=float),
        ApiField("status_event_id"),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
        ApiField("routing_keys", data_type=lambda o: loads(o)),
        ApiField("is_paused", data_type=bool),
        ApiField("owner_id"),
        ApiField("owner", data_type=Owner),
        ApiField("feed_type", data_type=dict),
        ApiField("FeedStatus", attr_key="feed_status", data_type=dict),
        ApiField("Metrics", attr_key="metrics", data_type=dict, optional=True),
    )

    id: int
    facility_id: int
    feed_type_id: int
    down_after: str
    key: str
    timezone: str
    token: str
    status: str
    degraded_threshold: float
    critical_threshold: float
    status_event_id: str
    created_at: datetime
    updated_at: datetime
    routing_keys: str
    is_paused: bool
    owner_id: str
    feed_type: str
    owner: Owner
    feed_status: str
    metrics: Optional[Dict] = None


@dataclass
class FieldTimeSeries:
    field: Field
    time_series: Dict[datetime, Any]


@dataclass
class BatchRequest:
    method: str
    uri: str
    body: Optional[str] = None

    @staticmethod
    def from_request(request: Request) -> "BatchRequest":
        # NOTE: this handles url-encoding parameters and other low-level translations
        r = request.prepare()
        return BatchRequest(method=r.method, uri=r.url, body=r.body)  # type: ignore

    def to_api(self) -> Dict[str, str]:
        d = {"method": self.method, "uri": self.uri}
        if self.body:
            d["body"] = self.body
        return d


BatchRequests = Dict[str, BatchRequest]


@dataclass
class BatchResponse:
    body: Any
    headers: Dict[str, Any]
    statusCode: int

    @property
    def ok(self) -> bool:
        return self.statusCode == 200


BatchResponses = Dict[str, BatchResponse]
