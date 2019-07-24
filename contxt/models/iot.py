from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from json import loads
from typing import Any, Dict, List, Optional

from contxt.models import ApiField, ApiObject, Parsers
from contxt.models.events import Owner


class Window(Enum):
    RAW = 0
    MINUTELY = 60
    QUARTER_HOURLY = 900
    HOURLY = 3600


class FieldValueType(Enum):
    BOOLEAN = "boolean"
    NUMERIC = "numeric"
    STRING = "string"


class Field(ApiObject):
    _api_fields = (
        ApiField("id", data_type=int),
        ApiField("field_name", attr_key="name", optional=True),
        ApiField("label", creatable=True, updatable=True),
        ApiField("output_id", data_type=int, creatable=True),
        ApiField("field_descriptor", creatable=True),
        ApiField("field_human_name"),
        ApiField("units", creatable=True, updatable=True),
        ApiField(
            "scalar", data_type=float, optional=True, creatable=True, updatable=True
        ),
        ApiField(
            "divisor", data_type=float, optional=True, creatable=True, updatable=True
        ),
        ApiField("value_type", data_type=FieldValueType, optional=True, creatable=True),
        ApiField("feed_key", optional=True, creatable=True),
        ApiField(
            "FieldGroupingField",
            attr_key="field_grouping_field",
            data_type=dict,
            optional=True,
        ),
        ApiField(
            "is_hidden", data_type=bool, creatable=True, updatable=True, optional=True
        ),
        ApiField(
            "is_default", data_type=bool, optional=True, creatable=True, updatable=True
        ),
        ApiField("is_totalizer", data_type=bool, optional=True),
        ApiField("can_aggregate", data_type=bool, optional=True),
        ApiField("is_windowed", data_type=bool, optional=True),
        ApiField("status", optional=True),
        ApiField("created_at", data_type=Parsers.datetime, optional=True),
        ApiField("updated_at", data_type=Parsers.datetime, optional=True),
    )

    def __init__(
        self,
        label: str,
        output_id: str,
        field_descriptor: str,
        units: str,
        id: Optional[int] = None,
        name: Optional[str] = None,
        field_human_name: Optional[str] = None,
        feed_key: Optional[str] = None,
        field_grouping_field: Optional[Dict] = None,
        value_type: Optional[FieldValueType] = None,
        scalar: Optional[float] = None,
        divisor: Optional[float] = None,
        is_hidden: Optional[bool] = None,
        is_totalizer: Optional[bool] = None,
        is_windowed: Optional[bool] = None,
        is_default: Optional[bool] = None,
        can_aggregate: Optional[bool] = None,
        status: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.label = label
        self.output_id = output_id
        self.field_descriptor = field_descriptor
        self.field_human_name = field_human_name
        self.scalar = scalar
        self.divisor = divisor
        self.value_type = value_type
        self.feed_key = feed_key
        self.is_hidden = is_hidden
        self.is_totalizer = is_totalizer
        self.is_windowed = is_windowed
        self.is_default = is_default
        self.can_aggregate = can_aggregate
        self.status = status
        self.units = units
        self.field_grouping_field = field_grouping_field
        self.created_at = created_at
        self.updated_at = updated_at


class FieldCategory(ApiObject):
    _api_fields = (
        ApiField("id"),
        ApiField("name"),
        ApiField("description"),
        ApiField("organization_id"),
        ApiField("parent_category_id"),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        organization_id: str,
        parent_category_id: str,
        created_at: datetime,
        updated_at: datetime,
    ) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.description = description
        self.organization_id = organization_id
        self.parent_category_id = parent_category_id
        self.created_at = created_at
        self.updated_at = updated_at


class FieldGrouping(ApiObject):
    _api_fields = (
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

    def __init__(
        self,
        id: str,
        label: str,
        slug: str,
        description: str,
        facility_id: int,
        is_public: bool,
        owner_id: str,
        owner: Owner,
        field_category_id: str,
        field_category: FieldCategory,
        fields: List[Field],
        created_at: datetime,
        updated_at: datetime,
    ) -> None:
        super().__init__()
        self.id = id
        self.label = label
        self.slug = slug
        self.description = description
        self.facility_id = facility_id
        self.owner_id = owner_id
        self.is_public = is_public
        self.field_category_id = field_category_id
        self.owner = owner
        self.category = field_category
        self.fields = fields
        self.created_at = created_at
        self.updated_at = updated_at


class UnprovisionedField(ApiObject):
    _api_fields = (ApiField("field_descriptor"), ApiField("assumed_type"))

    def __init__(self, field_descriptor: str, assumed_type: str) -> None:
        super().__init__()
        self.field_descriptor = field_descriptor
        self.assumed_type = assumed_type


class Feed(ApiObject):
    _api_fields = (
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

    def __init__(
        self,
        id: int,
        facility_id: int,
        feed_type_id: int,
        down_after: str,
        key: str,
        timezone: str,
        token: str,
        status: str,
        degraded_threshold: float,
        critical_threshold: float,
        status_event_id: str,
        created_at: datetime,
        updated_at: datetime,
        routing_keys: str,
        is_paused: bool,
        owner_id: str,
        feed_type: str,
        owner: Owner,
        feed_status: str,
        metrics: Optional[Dict] = None,
    ) -> None:
        super().__init__()
        self.id = id
        self.feed_type_id = feed_type_id
        self.down_after = down_after
        self.key = key
        self.facility_id = facility_id
        self.timezone = timezone
        self.token = token
        self.status = status
        self.degraded_threshold = degraded_threshold
        self.critical_threshold = critical_threshold
        self.status_event_id = status_event_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.routing_keys = routing_keys
        self.is_paused = is_paused
        self.owner_id = owner_id
        self.feed_type = feed_type
        self.owner = owner
        self.feed_status = feed_status
        self.metrics = metrics


@dataclass
class FieldTimeSeries:
    field: Field
    time_series: Dict[datetime, Any]
