from datetime import datetime
from enum import Enum
from json import JSONDecodeError, loads
from typing import Any, Dict, List, Optional

from contxt.models.base import UUID, BaseModel, RawDict, dataclass, field
from contxt.utils import cachedproperty, make_logger

logger = make_logger(__name__)

Metric = RawDict
GroupingField = RawDict


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
class Field(BaseModel):
    id: int
    output_id: Optional[int] = field(post=True)
    name: Optional[str] = field(key="field_name")
    human_name: Optional[str] = field(key="field_human_name")
    label: Optional[str] = field(post=True, put=True)
    is_totalizer: Optional[bool]
    is_windowed: Optional[bool]
    scalar: Optional[float] = field(post=True, put=True)
    divisor: Optional[float] = field(post=True, put=True)
    units: Optional[str] = field(post=True, put=True)
    can_aggregate: Optional[bool]
    is_default: Optional[bool] = field(post=True, put=True)
    descriptor: Optional[str] = field(key="field_descriptor", post=True)
    value_type: Optional[FieldValueType] = field(post=True, enum=True)
    is_hidden: Optional[bool] = field(post=True, put=True)
    feed_key: Optional[str] = field(post=True)
    status: Optional[str]
    grouping_field: Optional[GroupingField] = field(key="FieldGroupingField")
    created_at: datetime
    updated_at: datetime

    @property
    def field_human_name(self) -> Optional[str]:
        # DEPRECATED
        return self.human_name


@dataclass
class Owner(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    created_at: datetime
    updated_at: datetime


@dataclass
class FieldCategory(BaseModel):
    id: UUID
    name: str
    description: str
    organization_id: Optional[UUID]
    parent_category_id: Optional[UUID]
    created_at: datetime
    updated_at: datetime


@dataclass
class FieldGrouping(BaseModel):
    id: UUID
    label: str
    slug: str
    description: str
    facility_id: int
    is_public: bool
    owner_id: str
    owner: Owner = field(key="Owner")
    field_category_id: Optional[UUID]
    field_category: Optional[FieldCategory] = field(key="FieldCategory")
    fields: List[Field] = field(key="Fields")
    created_at: datetime
    updated_at: datetime


@dataclass
class UnprovisionedField(BaseModel):
    field_descriptor: str
    assumed_type: str


@dataclass
class FeedStatus(BaseModel):
    id: int
    feed_id: int
    status: str
    updated_at: datetime
    feed_status_id: Optional[int]


@dataclass
class FeedType(BaseModel):
    id: int
    type: str
    down_after: int
    created_at: datetime
    updated_at: datetime


@dataclass
class Feed(BaseModel):
    id: int
    facility_id: int
    key: str
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime]
    routing_keys: str
    feed_type_id: int
    token: Optional[str]
    timezone: str
    status: str
    degraded_threshold: float
    critical_threshold: float
    is_paused: bool
    status_event_id: Optional[UUID]
    down_after: Optional[int]
    owner_id: str
    feed_type: FeedType
    feed_status: FeedStatus = field(key="FeedStatus")
    metrics: Optional[Metric] = field(key="Metrics")

    @cachedproperty
    def parsed_routing_keys(self) -> Any:
        """Parse `routing_keys` as JSON"""
        try:
            return loads(self.routing_keys)
        except JSONDecodeError as e:
            logger.error(
                f"Failed to parse {type(self).__name__}.routing_keys"
                f" {self.routing_keys} as JSON: {e}"
            )
        return self.routing_keys


@dataclass
class FieldTimeSeries:
    field: Field
    time_series: Dict[datetime, Any]
