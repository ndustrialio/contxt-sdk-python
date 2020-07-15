from dataclasses import InitVar, dataclass, field
from datetime import date, datetime, timedelta
from typing import Any, ClassVar, Dict, List, Optional, Set

from ..utils import dict_diff, make_logger
from . import ApiField, ApiObject, Formatters, Parsers

logger = make_logger(__name__)


# TODO: make these enums
class TimeIntervals:
    """Valid time intervals for a MetricValue"""

    hourly = "hourly"
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"
    yearly = "yearly"
    sparse = "sparse"


class DataTypes:
    """Valid data types for an Attribute"""

    boolean = "boolean"
    datetime = "date"
    number = "number"
    string = "string"


@dataclass
class Attribute(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("asset_type_id", creatable=True),
        ApiField("label", creatable=True, updatable=True),
        ApiField("description", creatable=True, updatable=True),
        ApiField("units", creatable=True, updatable=True),
        ApiField("organization_id", creatable=True),
        ApiField("data_type", creatable=True, updatable=True),
        ApiField("is_required", data_type=bool, creatable=True, updatable=True),
        ApiField("is_global", data_type=bool),
        ApiField("global_asset_attribute_parent_id"),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    asset_type_id: str
    label: str
    description: str
    units: str
    organization_id: str
    data_type: str
    is_required: bool
    id: Optional[str] = None
    global_asset_attribute_parent_id: Optional[str] = None
    is_global: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @property
    def normalized_label(self) -> str:
        return Formatters.normalize_label(self.label)


@dataclass
class AttributeValue(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("asset_id"),
        ApiField("asset_attribute_id", attr_key="attribute_id", creatable=True),
        ApiField("notes", creatable=True, updatable=True),
        ApiField("value", data_type=Parsers.unknown, creatable=True, updatable=True),
        ApiField("effective_date", data_type=Parsers.date, creatable=True, updatable=True),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    asset_id: str
    attribute_id: str
    notes: str
    value: Any
    id: Optional[str] = None
    attribute: Optional[Attribute] = None
    effective_date: date = field(default_factory=date.today)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def upsert(self) -> Dict:
        # HACK: handle special case of upserting attribute_values
        # TODO: if upserting becomes common, this method be moved to the base
        # class
        return {**self.put(), "id": self.id, "asset_attribute_id": self.attribute_id}


@dataclass
class Metric(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("asset_type_id"),
        ApiField("label", creatable=True, updatable=True),
        ApiField("description", creatable=True, updatable=True),
        ApiField("organization_id", creatable=True),
        ApiField("time_interval", creatable=True, updatable=True),
        ApiField("units", creatable=True, updatable=True),
        ApiField("global_asset_metric_parent_id"),
        ApiField("is_global", data_type=bool, creatable=True),
        ApiField("is_calculated", data_type=bool),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    asset_type_id: str
    label: str
    description: str
    organization_id: str
    time_interval: str
    units: str
    id: Optional[str] = None
    global_asset_metric_parent_id: Optional[str] = None
    is_global: Optional[bool] = None
    is_calculated: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @property
    def normalized_label(self) -> str:
        return Formatters.normalize_label(self.label)


@dataclass
class MetricValue(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("asset_id"),
        ApiField("Asset", attr_key="asset", data_type=f"{__name__}:Asset", optional=True),
        ApiField("asset_metric_id"),
        ApiField("effective_start_date", data_type=Parsers.datetime, creatable=True, updatable=True),
        ApiField("effective_end_date", data_type=Parsers.datetime, creatable=True, updatable=True),
        ApiField("notes", creatable=True, updatable=True),
        ApiField("value", data_type=float, creatable=True, updatable=True),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    asset_id: str
    asset_metric_id: str
    effective_start_date: datetime
    effective_end_date: datetime
    notes: str
    value: str
    id: Optional[str] = None
    asset: Optional["Asset"] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class AssetType(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("label", creatable=True),
        ApiField("description", creatable=True, updatable=True),
        ApiField("organization_id", creatable=True),
        ApiField("global_asset_type_parent_id"),
        ApiField("is_global", data_type=bool),
        ApiField("parent_id", creatable=True, updatable=True),
        ApiField("hierarchy_level", data_type=int),
        ApiField("asset_attributes", attr_key="attributes", data_type=Attribute, optional=True),
        ApiField("asset_metrics", attr_key="metrics", data_type=Metric, optional=True),
        ApiField("children", data_type=f"{__name__}:AssetType", optional=True),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    label: str
    description: str
    organization_id: str
    id: Optional[str] = None
    is_global: Optional[bool] = None
    global_asset_type_parent_id: Optional[str] = None
    parent_id: Optional[str] = None
    hierarchy_level: Optional[int] = None
    attributes: InitVar[List[Attribute]] = field(default_factory=list)
    metrics: InitVar[List[Metric]] = field(default_factory=list)
    children: InitVar[List["AssetType"]] = field(default_factory=list)
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self, attributes, metrics, children) -> None:
        self._attributes = attributes
        self._metrics = metrics
        self._children = children

    @property
    def normalized_label(self) -> str:
        if " " not in self.label:
            return self.label
        else:
            return self.label.title().replace(" ", "")

    @property  # type: ignore
    def attributes(self) -> List[Attribute]:
        return self._attributes

    @attributes.setter
    def attributes(self, attributes: List[Attribute]) -> None:
        self._attributes = attributes
        self._attributes_by_id = {}
        self._attributes_by_label = {}
        # Store by id/label for fast lookup
        for attribute in self._attributes:
            self._attributes_by_id[attribute.id] = attribute
            self._attributes_by_label[attribute.label] = attribute
            self._attributes_by_label[attribute.normalized_label] = attribute

    @property  # type: ignore
    def metrics(self) -> List[Metric]:
        return self._metrics

    @metrics.setter
    def metrics(self, metrics: List[Metric]) -> None:
        self._metrics = metrics
        self._metrics_by_id = {}
        self._metrics_by_label = {}
        # Store by id/label for fast lookup
        for metric in self._metrics:
            self._metrics_by_id[metric.id] = metric
            self._metrics_by_label[metric.label] = metric
            self._metrics_by_label[metric.normalized_label] = metric

    @property  # type: ignore
    def children(self) -> List["AssetType"]:
        return self._children

    @children.setter
    def children(self, children: List["AssetType"]) -> None:
        self._children = children
        self._children_by_id = {}
        self._children_by_label = {}
        # Store by id/label for fast lookup
        for child in self._children:
            self._children_by_id[child.id] = child
            self._children_by_label[child.label] = child
            self._children_by_label[child.normalized_label] = child

    def attribute_with_id(self, attribute_id: str, default: Any = ...) -> Attribute:
        if attribute_id not in self._attributes_by_id:
            if default is ...:
                raise KeyError(f"Attribute {attribute_id} not found.")
            return default
        return self._attributes_by_id[attribute_id]

    def attribute_with_label(self, attribute_label: str, default: Any = ...) -> Attribute:
        if attribute_label not in self._attributes_by_label:
            if default is ...:
                raise KeyError(f"Attribute {attribute_label} not found.")
            return default
        return self._attributes_by_label[attribute_label]

    def metric_with_id(self, metric_id: str, default: Any = ...) -> Metric:
        if metric_id not in self._metrics_by_id:
            if default is ...:
                raise KeyError(f"Metric {metric_id} not found.")
            return default
        return self._metrics_by_id[metric_id]

    def metric_with_label(self, metric_label: str, default: Any = ...) -> Metric:
        if metric_label not in self._metrics_by_label:
            if default is ...:
                raise KeyError(f"Metric {metric_label} not found.")
            return default
        return self._metrics_by_label[metric_label]

    def child_with_id(self, child_id: str, default: Any = ...) -> "AssetType":
        if child_id not in self._children_by_id:
            if default is ...:
                raise KeyError(f"Child {child_id} not found.")
            return default
        return self._children_by_id[child_id]

    def child_with_label(self, child_label: str, default: Any = ...) -> "AssetType":
        if child_label not in self._children_by_label:
            if default is ...:
                raise KeyError(f"Child {child_label} not found.")
            return default
        return self._children_by_label[child_label]


@dataclass
class Asset(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("asset_type_id", creatable=True),
        ApiField("label", creatable=True),
        ApiField("description", creatable=True, updatable=True),
        ApiField("organization_id", creatable=True),
        ApiField("parent_id", creatable=True, updatable=True),
        ApiField("hierarchy_level", data_type=int),
        ApiField(
            "asset_attribute_values",
            attr_key="attribute_values",
            data_type=AttributeValue,
            optional=True,
        ),
        ApiField("asset_metric_values", attr_key="metric_values", data_type=MetricValue, optional=True),
        ApiField("children", data_type=f"{__name__}:Asset", optional=True),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    asset_type_id: str
    label: str
    description: str
    organization_id: str
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    parent_id: Optional[str] = None
    hierarchy_level: Optional[str] = None
    attribute_values: List[AttributeValue] = field(default_factory=list)
    metric_values: List[MetricValue] = field(default_factory=list)
    children: List["Asset"] = field(default_factory=list)
    asset_type: Optional[AssetType] = None

    @property
    def normalized_label(self) -> str:
        return Formatters.normalize_label(self.label)

    def post(self) -> Dict:
        """Get data for a post request"""
        d = super().post()
        # HACK: handle special case of posting attribute_values
        if self.attribute_values:
            d.update({"asset_attribute_values_to_create": [av.post() for av in self.attribute_values]})
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
        self.edited_attribute_values: Set[AttributeValue] = set()
        self.edited_metric_values: Set[MetricValue] = set()

    def _init_attribute_values(self) -> Dict:
        # Fetch attribute labels to use as keys
        attribute_values_by_label: Dict[str, Optional[AttributeValue]] = {
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
        metric_values_by_label: Dict[str, Dict[datetime, MetricValue]] = {
            m.normalized_label: {} for m in self.asset_type.metrics
        }

        for mv in self.asset.metric_values:
            label = self.asset_type.metric_with_id(mv.asset_metric_id).normalized_label
            metric_values_by_label[label][mv.effective_start_date] = mv

        return metric_values_by_label

    def _effective_end_date(self, effective_start_date: date, time_interval: str) -> date:
        if time_interval == TimeIntervals.hourly:
            delta = timedelta(hours=1, microseconds=-1)
        elif time_interval == TimeIntervals.daily:
            delta = timedelta(days=1, microseconds=-1)
        elif time_interval == TimeIntervals.weekly:
            delta = timedelta(weeks=1, microseconds=-1)
        elif time_interval == TimeIntervals.monthly:
            d = effective_start_date
            m = (d.month + 1) % 12
            delta = (d.replace(month=m, year=d.year + int(m == 1)) - d) + timedelta(microseconds=-1)
        elif time_interval == TimeIntervals.yearly:
            delta = timedelta(days=364 + int(effective_start_date.year % 4 != 0), microseconds=-1)
        elif time_interval == TimeIntervals.sparse:
            delta = timedelta()
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
        return {k: v.value if v else None for k, v in self._attribute_values_by_label.items()}

    @attributes.setter
    def attributes(self, attributes: Dict) -> None:
        # Determine attributes that changed, by performing a set difference on
        # the two dictionaries
        new_attribute_values = dict(set(attributes.items()) - set(self.attributes.items()))

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
                asset_id=self.asset.id, attribute_id=attribute.id, notes="", value=None  # type: ignore
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
        new_metrics = dict_diff(metrics, curr_metrics)

        # Determine each change
        for label, start_date_to_value in new_metrics.items():
            # Validate metric label
            if label not in self._metric_values_by_label:
                raise KeyError(
                    f"Metric {label} does not exist for AssetType" f" {self.asset_type.normalized_label}"
                )

            # Determine metric values that changed
            metric = self.asset_type.metric_with_label(label)
            metric_values = self._metric_values_by_label[label]
            new_metric_values = dict_diff(start_date_to_value, curr_metrics[label])

            for start_date, new_value in new_metric_values.items():
                # Make the change, and mark as changed
                metric_value = metric_values.get(start_date) or MetricValue(
                    asset_id=self.asset.id,  # type: ignore
                    asset_metric_id=metric.id,  # type: ignore
                    effective_start_date=start_date,
                    effective_end_date=self._effective_end_date(
                        start_date, metric.time_interval
                    ),  # type: ignore
                    notes="",
                    value=None,  # type: ignore
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
                    logger.debug(f"Changed {label} {start_date}: {prev_value} -> {new_value}")

        # Refresh internal list of metric values
        self._metric_values_by_label = self._init_metric_values()
