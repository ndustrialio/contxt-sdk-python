from __future__ import annotations

from ast import literal_eval
from datetime import date, datetime
from typing import Dict, List, Optional, Set, Tuple, Union

from inflect import engine
from pytz import UTC

from contxt.services.api_client import ApiObject
from contxt.utils import make_logger

p = engine()
logger = make_logger(__name__)

# TODO: Need a way to track changed attributes

def warn_of_unknown_kwargs(cls_, kwargs):
    # Warn of unexpected kwargs
    cls_name = cls_.__class__.__name__
    for k, v in kwargs.items():
        logger.warning(f"{cls_name}: Unexpected kwarg {k}")
    # Warn of a present global
    # if hasattr(cls_, "is_global") and cls_.is_global:
    #     logger.warning(
    #         f"{cls_name}: received global (id {cls_.id}, label {cls_.label})"
    #     )


class TimeIntervals:
    hourly = "hourly"
    daily = "daily"
    weekly = "weekly"
    monthly = "monthly"
    yearly = "yearly"


class DataTypes:
    boolean = 'bool'
    datetime = 'date'
    number = 'number'
    string = 'string'


class DataParsers:
    @staticmethod
    def parse_datetime(datetime_):
        return datetime_.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    @staticmethod
    def parse_as_datetime(timestamp):
        return datetime.strptime(timestamp,
                                 '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=UTC)

    # TODO: change these as dates rather than datetimes
    @staticmethod
    def parse_date(datetime_):
        return datetime_.strftime('%Y-%m-%d')

    @staticmethod
    def parse_as_date(date):
        return datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=UTC)

    @staticmethod
    def parse_as_unknown(val):
        # First, try a general parser (supports strings, numbers, tuples,
        # lists, dicts, booleans, and None)
        try:
            return literal_eval(val)
        except (SyntaxError, ValueError) as e:
            pass
        # Next, fall back to a date parser
        try:
            return DataParsers.datetime(val)
        except (TypeError, ValueError) as e:
            pass
        # Failed, return original value
        return val

    boolean = bool
    datetime = parse_as_datetime
    date = parse_as_date
    number = float
    string = str
    unknown = parse_as_unknown


class AssetType(ApiObject):
    creatable_fields = ['label', 'description', 'organization_id', 'parent_id']
    updatable_fields = ['description', 'parent_id']
    __marker = object()

    def __init__(
            self,
            label: str,
            description: str,
            organization_id: str,
            id: Optional[str] = None,
            global_asset_type_parent_id: Optional[str] = None,
            is_global: Optional[bool] = None,
            parent_id: Optional[str] = None,
            # parent_label: Optional[str] = None,
            hierarchy_level: Optional[int] = None,
            children: Optional[Union[List[dict], List[AssetType]]] = None,
            created_at: Optional[str] = None,
            updated_at: Optional[str] = None,
            asset_attributes: Optional[Union[List[dict], List[Attribute]]] = None,
            asset_metrics: Optional[Union[List[dict], List[Metric]]] = None,
            **kwargs,
    ) -> None:
        super().__init__()

        self.id = id
        self.label = label
        self.description = description
        self.organization_id = organization_id
        self.parent_id = parent_id
        # TODO: parent_label is not an api response, but is used for migrations
        # self.parent_label = parent_label
        self.hierarchy_level = hierarchy_level
        self.global_asset_type_parent_id = global_asset_type_parent_id
        self.is_global = is_global

        asset_attributes = asset_attributes or []
        self._attributes = asset_attributes if asset_attributes and isinstance(
            asset_attributes[0],
            Attribute) else [Attribute(**attr) for attr in asset_attributes]

        asset_metrics = asset_metrics or []
        self._metrics = asset_metrics if asset_metrics and isinstance(
            asset_metrics[0],
            Metric) else [Metric(**metric) for metric in asset_metrics]

        children = children or []
        self._children = children if children and isinstance(
            children[0],
            AssetType) else [AssetType(**child) for child in children]

        self.created_at = DataParsers.datetime(
            created_at) if created_at else None
        self.updated_at = DataParsers.datetime(
            updated_at) if updated_at else None

        warn_of_unknown_kwargs(self, kwargs)

    @property
    def normalized_label(self) -> str:
        if " " not in self.label:
            return self.label
        else:
            return self.label.title().replace(' ', '')

    @property
    def plural_label(self) -> str:
        return p.plural(self.label)

    @property
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

    @property
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

    @property
    def children(self) -> List[AssetType]:
        return self._children

    @children.setter
    def children(self, children: List[AssetType]) -> None:
        self._children = children
        self._children_by_id = {}
        self._children_by_label = {}
        # Store by id/label for fast lookup
        for child in self._children:
            self._children_by_id[child.id] = child
            self._children_by_label[child.label] = child
            self._children_by_label[child.normalized_label] = child

    def attribute_with_id(self, attribute_id: str, default=__marker) -> Attribute:
        if attribute_id not in self._attributes_by_id:
            if default is self.__marker:
                raise KeyError(f"Attribute {attribute_id} not found.")
            return default
        return self._attributes_by_id[attribute_id]

    def attribute_with_label(self, attribute_label: str, default=__marker) -> Attribute:
        if attribute_label not in self._attributes_by_label:
            if default is self.__marker:
                raise KeyError(f"Attribute {attribute_label} not found.")
            return default
        return self._attributes_by_label[attribute_label]

    def metric_with_id(self, metric_id: str, default=__marker) -> Metric:
        if metric_id not in self._metrics_by_id:
            if default is self.__marker:
                raise KeyError(f"Metric {metric_id} not found.")
            return default
        return self._metrics_by_id[metric_id]

    def metric_with_label(self, metric_label: str, default=__marker) -> Metric:
        if metric_label not in self._metrics_by_label:
            if default is self.__marker:
                raise KeyError(f"Metric {metric_label} not found.")
            return default
        return self._metrics_by_label[metric_label]

    def child_with_id(self, child_id: str, default=__marker) -> AssetType:
        if child_id not in self._children_by_id:
            if default is self.__marker:
                raise KeyError(f"Child {child_id} not found.")
            return default
        return self._children_by_id[child_id]

    def child_with_label(self, child_label: str,
                         default=__marker) -> AssetType:
        if child_label not in self._children_by_label:
            if default is self.__marker:
                raise KeyError(f"Child {child_label} not found.")
            return default
        return self._children_by_label[child_label]


class Asset(ApiObject):
    creatable_fields = [
        'asset_type_id', 'label', 'description', 'organization_id', 'parent_id'
    ]
    updatable_fields = ['description', 'parent_id']

    def __init__(
            self,
            asset_type_id: str,
            label: str,
            description: str,
            organization_id: str,
            id: Optional[str] = None,
            created_at: Optional[str] = None,
            updated_at: Optional[str] = None,
            parent_id: Optional[str] = None,
            hierarchy_level: Optional[str] = None,
            asset_attribute_values: Optional[str] = None,
            asset_metric_values: Optional[str] = None,
            children: Optional[str] = None,
            **kwargs,
    ):
        super().__init__()
        self.id = id
        self.asset_type_id = asset_type_id
        self.label = label
        self.description = description
        self.organization_id = organization_id
        self.parent_id = parent_id
        self.asset_attribute_values = [
            AttributeValue(**value) for value in asset_attribute_values or []
        ]
        # TODO: include metric values with asset
        self.asset_metric_values = [
            MetricValue(**value) for value in asset_metric_values or []
        ]
        self.hierarchy_level = hierarchy_level
        self.children = [Asset(**child) for child in children or []]
        self.created_at = DataParsers.datetime(
            created_at) if created_at else None
        self.updated_at = DataParsers.datetime(
            updated_at) if updated_at else None

        warn_of_unknown_kwargs(self, kwargs)

    @property
    def normalized_label(self):
        return self.label.lower().replace(' ', '_')


class Attribute(ApiObject):
    creatable_fields = [
        'asset_type_id', 'label', 'description', 'organization_id',
        'data_type', 'is_required', 'units'
    ]
    updatable_fields = [
        'label', 'description', 'units', 'is_required', 'data_type'
    ]

    def __init__(
            self,
            asset_type_id: str,
            label: str,
            description: str,
            units: str,
            organization_id: str,
            data_type: str,
            is_required: bool,
            id: Optional[str] = None,
            global_asset_attribute_parent_id: Optional[str] = None,
            is_global: Optional[bool] = None,
            created_at: Optional[str] = None,
            updated_at: Optional[str] = None,
            **kwargs,
    ):
        super().__init__()

        self.id = id
        self.asset_type_id = asset_type_id
        self.label = label
        self.description = description
        self.units = units
        self.organization_id = organization_id
        self.data_type = data_type
        self.is_required = is_required
        self.global_asset_attribute_parent_id = global_asset_attribute_parent_id
        self.is_global = is_global
        self.created_at = DataParsers.datetime(
            created_at) if created_at else None
        self.updated_at = DataParsers.datetime(
            updated_at) if updated_at else None

        warn_of_unknown_kwargs(self, kwargs)

    @property
    def normalized_label(self):
        return self.label.lower().replace(' ', '_')


class AttributeValue(ApiObject):
    creatable_fields = [
        'asset_attribute_id', 'effective_date', 'notes', 'value'
    ]
    updatable_fields = ['effective_date', 'notes', 'value']

    def __init__(
            self,
            asset_id: str,
            asset_attribute_id: str,
            notes: str,
            value: str,
            id: Optional[str] = None,
            effective_date: Optional[str] = None,
            created_at: Optional[str] = None,
            updated_at: Optional[str] = None,
            **kwargs,
    ):
        super().__init__()
        self.id = id
        self.asset_attribute_id = asset_attribute_id
        self.asset_id = asset_id
        self.effective_date = DataParsers.date(
            effective_date) if effective_date else date.today()
        self.notes = notes
        # TODO: need to know data_type to parse
        self.value = DataParsers.unknown(value)
        self.created_at = DataParsers.datetime(
            created_at) if created_at else None
        self.updated_at = DataParsers.datetime(
            updated_at) if updated_at else None

        warn_of_unknown_kwargs(self, kwargs)


class Metric(ApiObject):
    # TODO: need to fix global metric for POST
    creatable_fields = [
        'label', 'description', 'organization_id', 'time_interval', 'units',
        'is_global'
    ]
    updatable_fields = [
        'label', 'description', 'time_interval', 'units'
    ]

    def __init__(
            self,
            asset_type_id: str,
            label: str,
            description: str,
            organization_id: str,
            time_interval: str,
            units: str,
            id: Optional[str] = None,
            global_asset_metric_parent_id: Optional[str] = None,
            is_global: Optional[bool] = None,
            created_at: Optional[str] = None,
            updated_at: Optional[str] = None,
            **kwargs,
    ):
        super().__init__()

        self.id = id
        self.asset_type_id = asset_type_id
        self.label = label
        self.description = description
        self.units = units
        self.organization_id = organization_id
        self.time_interval = time_interval
        self.global_asset_metric_parent_id = global_asset_metric_parent_id
        self.is_global = is_global
        self.created_at = DataParsers.datetime(
            created_at) if created_at else None
        self.updated_at = DataParsers.datetime(
            updated_at) if updated_at else None

        warn_of_unknown_kwargs(self, kwargs)

    @property
    def normalized_label(self):
        return self.label.lower().replace(' ', '_')


class MetricValue(ApiObject):
    creatable_fields = [
        'effective_start_date', 'effective_end_date', 'notes', 'value'
    ]
    updatable_fields = [
        'effective_start_date', 'effective_end_date', 'notes', 'value'
    ]

    def __init__(
            self,
            asset_id: str,
            asset_metric_id: str,
            effective_start_date: str,
            effective_end_date: str,
            notes: str,
            value: str,
            id: Optional[str] = None,
            asset: Optional[dict] = None,
            created_at: Optional[str] = None,
            updated_at: Optional[str] = None,
            **kwargs,
    ):
        super().__init__()
        self.id = id
        self.asset_id = asset_id
        self.asset_metric_id = asset_metric_id
        self.effective_start_date = DataParsers.datetime(
            effective_start_date) if effective_start_date else None
        self.effective_end_date = DataParsers.datetime(
            effective_end_date) if effective_end_date else None
        self.notes = notes
        self.value = DataParsers.number(value) if value else None
        self.created_at = DataParsers.datetime(created_at)
        self.updated_at = DataParsers.datetime(updated_at)
        self.asset = Asset(**asset)
