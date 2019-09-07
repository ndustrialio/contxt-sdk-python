from dataclasses import InitVar
from datetime import date, datetime
from enum import Enum
from typing import Any, Dict, List, Optional

from dateutil.relativedelta import relativedelta

from contxt.models import Formatters, Parsers
from contxt.models.base import UUID, BaseModel, dataclass, field
from contxt.utils import Utils, cachedproperty, make_logger

logger = make_logger(__name__)


class MetricTimeInterval(Enum):
    hourly = "hourly"
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"
    yearly = "yearly"
    sparse = "sparse"


class AttributeDataType(Enum):
    boolean = "boolean"
    datetime = "date"
    number = "number"
    string = "string"


class DataTypes(AttributeDataType):
    """DEPRECATED"""


@dataclass
class Attribute(BaseModel):
    id: UUID
    asset_type_id: UUID = field(post=True)
    label: str = field(post=True, put=True)
    units: Optional[str] = field(post=True, put=True)  # default=""
    organization_id: Optional[UUID] = field(post=True)
    description: str = field(post=True, put=True)  # default=label
    is_required: bool = field(post=True, put=True)  # # default=False
    created_at: datetime
    updated_at: datetime
    data_type: AttributeDataType = field(post=True, put=True, enum=True)
    global_asset_attribute_parent_id: Optional[UUID]
    is_global: bool

    @property
    def normalized_label(self) -> str:
        return Formatters.snake_case(self.label)


@dataclass
class AttributeValue(BaseModel):
    id: UUID
    asset_id: UUID
    attribute_id: UUID = field(key="asset_attribute_id", post=True)
    value: str = field(post=True, put=True)
    notes: Optional[str] = field(post=True, put=True)
    created_at: datetime
    updated_at: datetime
    effective_date: date = field(default_factory=date.today, post=True, put=True)
    attribute: Optional[Attribute] = None

    @cachedproperty
    def parsed_value(self) -> Any:
        # TODO: replace value
        return Parsers.unknown(self.value)

    def upsert(self) -> Dict:
        # HACK: handle special case of upserting attribute_values
        return {**self.put(), "id": self.id, "asset_attribute_id": self.attribute_id}


@dataclass
class Metric(BaseModel):
    id: UUID
    asset_type_id: UUID
    description: str = field(post=True, put=True)
    label: str = field(post=True, put=True)
    organization_id: Optional[UUID] = field(post=True)
    time_interval: MetricTimeInterval = field(post=True, put=True, enum=True)
    units: Optional[str] = field(post=True, put=True)
    created_at: datetime
    updated_at: datetime
    global_asset_metric_parent_id: Optional[UUID]
    is_global: bool = field(post=True)
    is_calculated: bool

    @property
    def normalized_label(self) -> str:
        return Formatters.snake_case(self.label)


@dataclass
class MetricValue(BaseModel):
    id: UUID
    asset_id: UUID
    asset_metric_id: UUID
    effective_start_date: datetime = field(post=True, put=True)
    effective_end_date: datetime = field(post=True, put=True)
    notes: Optional[str] = field(post=True, put=True)
    value: str = field(post=True, put=True)
    created_at: datetime
    updated_at: datetime
    asset: Optional["Asset"] = field(default=None, key="Asset")
    # TODO: post-process value as float


@dataclass
class AssetType(BaseModel):
    id: UUID
    label: str = field(post=True)
    organization_id: Optional[UUID] = field(post=True)
    description: str = field(post=True, put=True)
    created_at: datetime
    updated_at: datetime
    hierarchy_level: Optional[int]
    parent_id: Optional[UUID] = field(post=True, put=True)
    global_asset_type_parent_id: Optional[UUID]
    is_global: bool
    # FIXME: come up with more elegant solution
    attributes: InitVar[Optional[List[Attribute]]] = field(
        default=None, key="asset_attributes"
    )
    metrics: InitVar[Optional[List[Metric]]] = field(default=None, key="asset_metrics")
    children: InitVar[Optional[List["AssetType"]]] = field(default=None)

    def __post_init__(self, attributes, metrics, children) -> None:
        self._attributes = attributes or []
        self._metrics = metrics or []
        self._children = children or []

    @property
    def normalized_label(self) -> str:
        return Formatters.pascal_case(self.label)

    @property
    def attributes(self) -> List[Attribute]:
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: List[Attribute]) -> None:
        """Store attributes by `id`, `label`, and `normalized_label`"""
        self._attributes = attributes
        self._attributes_by_id: Dict[UUID, Attribute] = {}
        self._attributes_by_label: Dict[str, Attribute] = {}
        for attribute in self._attributes:
            self._attributes_by_id[attribute.id] = attribute
            self._attributes_by_label[attribute.label] = attribute
            self._attributes_by_label[attribute.normalized_label] = attribute

    @property
    def metrics(self) -> List[Metric]:
        return self._metrics

    @metrics.setter
    def metrics(self, metrics: List[Metric]) -> None:
        """Store metrics by `id`, `label`, and `normalized_label`"""
        self._metrics = metrics
        self._metrics_by_id: Dict[UUID, Metric] = {}
        self._metrics_by_label: Dict[str, Metric] = {}
        for metric in self._metrics:
            self._metrics_by_id[metric.id] = metric
            self._metrics_by_label[metric.label] = metric
            self._metrics_by_label[metric.normalized_label] = metric

    @property
    def children(self) -> List["AssetType"]:
        return self._children

    @children.setter
    def children(self, children: List["AssetType"]) -> None:
        """Store children by `id`, `label`, and `normalized_label`"""
        self._children = children
        self._children_by_id: Dict[UUID, AssetType] = {}
        self._children_by_label: Dict[str, AssetType] = {}
        for child in self._children:
            self._children_by_id[child.id] = child
            self._children_by_label[child.label] = child
            self._children_by_label[child.normalized_label] = child

    def _cache_look_up(
        self, name: str, key: Any, dct: Dict[Any, Any], default: Any
    ) -> Any:
        """Get `dct[key]` if available, or `default` if specified, or raise `KeyError`"""
        if key not in dct:
            if default is ...:
                raise KeyError(f"{name} {key} not found.")
            return default
        return dct[key]

    def attribute_with_id(self, id: str, default: Any = ...) -> Attribute:
        """Get attribute with id `id`"""
        return self._cache_look_up(
            name="Attribute", key=id, dct=self._attributes_by_id, default=default
        )

    def attribute_with_label(self, label: str, default: Any = ...) -> Attribute:
        """Get attribute with label `label`"""
        return self._cache_look_up(
            name="Attribute", key=label, dct=self._attributes_by_label, default=default
        )

    def metric_with_id(self, id: str, default: Any = ...) -> Metric:
        """Get metric with id `id`"""
        return self._cache_look_up(
            name="Metric", key=id, dct=self._metrics_by_id, default=default
        )

    def metric_with_label(self, label: str, default: Any = ...) -> Metric:
        """Get metric with label `label`"""
        return self._cache_look_up(
            name="Metric", key=label, dct=self._metrics_by_label, default=default
        )

    def child_with_id(self, id: str, default: Any = ...) -> "AssetType":
        """Get child `AssetType` with id `id`"""
        return self._cache_look_up(
            name="Child", key=id, dct=self._children_by_id, default=default
        )

    def child_with_label(self, label: str, default: Any = ...) -> "AssetType":
        """Get child `AssetType` with label `label`"""
        return self._cache_look_up(
            name="Child", key=label, dct=self._children_by_label, default=default
        )


@dataclass
class Asset(BaseModel):
    id: UUID
    asset_type_id: UUID = field(post=True)
    label: str = field(post=True)
    description: Optional[str] = field(post=True, put=True)
    organization_id: UUID = field(post=True)
    created_at: datetime
    updated_at: datetime
    hierarchy_level: Optional[int]
    parent_id: Optional[UUID] = field(post=True, put=True)
    # TODO: mayne default to None so we can determine if we just haven't fetched values yet
    attribute_values: List[AttributeValue] = field(
        default_factory=list, key="asset_attribute_values"
    )
    metric_values: List[MetricValue] = field(
        default_factory=list, key="asset_metric_values"
    )
    children: Optional[List["Asset"]] = field(default_factory=list)
    asset_type: Optional[AssetType] = None

    @property
    def normalized_label(self) -> str:
        return Formatters.snake_case(self.label)

    def post(self) -> Dict:
        """Serialize instance for POST request"""
        d = super().post()
        # HACK: handle special case of posting attribute_values
        if self.attribute_values:
            d["asset_attribute_values_to_create"] = [
                av.post() for av in self.attribute_values
            ]
        return d


class CompleteAsset:
    """High-level abstraction of an asset"""

    def __init__(self, asset: Asset, asset_type: AssetType):
        # Asset
        self.asset = asset
        self.asset_type = asset_type

        # Labeled attribute/metric values
        self._attribute_values_by_label = self._init_attribute_values()
        self._metric_values_by_label = self._init_metric_values()

        # Use two sets to track changes to values
        # TODO: figure out a more elegant way to track this
        self.edited_attribute_values = set()
        self.edited_metric_values = set()

    def _init_attribute_values(self) -> Dict:
        # Fetch attribute labels to use as keys
        attribute_values_by_label = {
            a.normalized_label: None for a in self.asset_type.attributes
        }

        # TODO: this is sorted to only store the attribute value with the
        # latest effective_date. However, we may later need to keep the
        # complete list.
        for av in sorted(self.asset.attribute_values, key=lambda av: av.effective_date):
            label = self.asset_type.attribute_with_id(av.attribute_id).normalized_label
            attribute_values_by_label[label] = av

        return attribute_values_by_label

    def _init_metric_values(self) -> Dict:
        # Fetch metric labels to use as keys
        metric_values_by_label = {
            m.normalized_label: {} for m in self.asset_type.metrics
        }

        for mv in self.asset.metric_values:
            label = self.asset_type.metric_with_id(mv.asset_metric_id).normalized_label
            metric_values_by_label[label][mv.effective_start_date] = mv

        return metric_values_by_label

    def _effective_end_date(
        self, effective_start_date: date, time_interval: MetricTimeInterval
    ) -> date:
        if time_interval == MetricTimeInterval.hourly:
            delta = relativedelta(hours=1, microseconds=-1)
        elif time_interval == MetricTimeInterval.daily:
            delta = relativedelta(days=1, microseconds=-1)
        elif time_interval == MetricTimeInterval.weekly:
            delta = relativedelta(weeks=1, microseconds=-1)
        elif time_interval == MetricTimeInterval.monthly:
            delta = relativedelta(months=1, microseconds=-1)
        elif time_interval == MetricTimeInterval.yearly:
            delta = relativedelta(years=1, microseconds=-1)
        elif time_interval == MetricTimeInterval.sparse:
            delta = relativedelta()
        else:
            raise KeyError(f"Unrecognized time interval: {time_interval}")
        return effective_start_date + delta

    def attribute(self, label: str) -> Any:
        attr = self._attribute_values_by_label[label]
        return attr.value if attr else attr

    @property
    def attributes(self) -> Dict:
        """Get dict of key (Attribute label) value (value of AttributeValue
        with latest effective_date) pairs"""
        return {
            k: v.value if v else None
            for k, v in self._attribute_values_by_label.items()
        }

    @attributes.setter
    def attributes(self, attributes: Dict) -> None:
        # Determine attributes that changed, by performing a set difference on
        # the two dictionaries
        new_attribute_values = dict(
            set(attributes.items()) - set(self.attributes.items())
        )

        # Handle each change
        for label, new_value in new_attribute_values.items():
            # Validate attribute label
            if label not in self._attribute_values_by_label:
                raise KeyError(
                    f"Attribute {label} does not exist for AssetType"
                    f" {self.asset_type.normalized_label}"
                )

            # Make the change, and mark as changed
            attribute = self.asset_type.attribute_with_label(label)
            attribute_value = self._attribute_values_by_label[label] or AttributeValue(
                asset_id=self.asset.id, attribute_id=attribute.id, notes="", value=None
            )
            prev_value = attribute_value.value
            attribute_value.value = new_value
            self.edited_attribute_values.add(attribute_value)

            # Log the change and handle any bookkeeping
            if new_value is None:
                logger.debug(f"Deleted {label}")
                # self.asset.attribute_values.remove(attribute_value)
            elif prev_value is None:
                logger.debug(f"Set {label}: {new_value}")
                self.asset.attribute_values.append(attribute_value)
            else:
                logger.debug(f"Changed {label}: {prev_value} -> {new_value}")

        # Refresh internal list of attribute values
        self._attribute_values_by_label = self._init_attribute_values()

    def metric(self, label: str) -> Dict:
        return self._metric_values_by_label[label]

    @property
    def metrics(self) -> Dict:
        """Get dict of key (Metric label) value (dict of effective_start_date
        to value of MetricValue) pairs"""
        return {
            k: {kk: vv.value if vv else None for kk, vv in v.items()}
            for k, v in self._metric_values_by_label.items()
        }

    @metrics.setter
    def metrics(self, metrics: Dict) -> None:
        # Determine metrics that changed, by performing a set difference on
        # the two dictionaries
        # TODO: this only identifies the label, since this is a nested dict
        curr_metrics = self.metrics
        new_metrics = Utils.set_to_dict(
            Utils.dict_to_set(metrics) - Utils.dict_to_set(curr_metrics)
        )

        # Determine each change
        for label, start_date_to_value in new_metrics.items():
            # Validate metric label
            if label not in self._metric_values_by_label:
                raise KeyError(
                    f"Metric {label} does not exist for AssetType"
                    f" {self.asset_type.normalized_label}"
                )

            # Determine metric values that changed
            metric = self.asset_type.metric_with_label(label)
            metric_values = self._metric_values_by_label[label]
            new_metric_values = Utils.set_to_dict(
                Utils.dict_to_set(start_date_to_value)
                - Utils.dict_to_set(curr_metrics[label])
            )

            for start_date, new_value in new_metric_values.items():
                # Make the change, and mark as changed
                metric_value = metric_values.get(start_date) or MetricValue(
                    asset_id=self.asset.id,
                    asset_metric_id=metric.id,
                    effective_start_date=start_date,
                    effective_end_date=self._effective_end_date(
                        start_date, metric.time_interval
                    ),
                    notes="",
                    value=None,
                )
                prev_value = metric_value.value
                metric_value.value = new_value
                self.edited_metric_values.add(metric_value)

                # Log the change and handle any bookkeeping
                if new_value is None:
                    logger.debug(f"Deleted {label} {start_date}")
                    # self.asset.metric_values.remove(metric_value)
                elif prev_value is None:
                    logger.debug(f"Set {label} {start_date}: {new_value}")
                    self.asset.metric_values.append(metric_value)
                else:
                    logger.debug(
                        f"Changed {label} {start_date}: {prev_value} -> {new_value}"
                    )

        # Refresh internal list of metric values
        self._metric_values_by_label = self._init_metric_values()
