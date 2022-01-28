from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import ClassVar, List, Optional

from . import ApiField, ApiObject, Formatters, Parsers
from .events import Event
from .iot import Field


class ResourceType(Enum):
    COMBINED = "combined"
    ELECTRIC = "electric"
    GAS = "gas"
    WATER = "water"


@dataclass
class MainService(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id", data_type=int),
        ApiField("facility_id", data_type=int),
        ApiField("name"),
        ApiField("type", attr_key="resource_type", data_type=ResourceType),
        ApiField("demand_field_id", data_type=int),
        ApiField("usage_field_id", data_type=int),
        ApiField("demand_field", data_type=Field),
        ApiField("usage_field", data_type=Field),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: int
    facility_id: int
    name: str
    resource_type: ResourceType
    demand_field_id: int
    usage_field_id: int
    demand_field: Field
    usage_field: Field
    created_at: datetime
    updated_at: datetime


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
        ApiField("id", optional=True),
        ApiField("effective_start_date", data_type=Parsers.datetime, creatable=True, updatable=True),
        ApiField("effective_end_date", data_type=Parsers.datetime, creatable=True, updatable=True),
        ApiField("value", data_type=float, creatable=True, updatable=True),
        ApiField("created_at", data_type=Parsers.datetime, optional=True),
        ApiField("updated_at", data_type=Parsers.datetime, optional=True),
        ApiField("is_estimated", data_type=bool, optional=True),
    )

    effective_start_date: datetime
    effective_end_date: datetime
    value: str
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    is_estimated: Optional[bool] = None


@dataclass
class Facility(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id", data_type=int),
        ApiField("name"),
        ApiField("asset_id"),
        ApiField("organization_id"),
        ApiField("baseline", data_type=dict),
        ApiField("main_services", data_type=MainService),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: int
    name: str
    asset_id: str
    organization_id: str
    baseline: dict
    main_services: List[MainService]
    created_at: datetime
    updated_at: datetime


@dataclass
class UtilityPeriod(ApiObject):
    _api_fields: ClassVar = (
        ApiField("event_time", data_type=Parsers.datetime),
        ApiField("value", data_type=int),
    )

    event_time: datetime
    value: int


UtilitySpendPeriod = UtilityPeriod
UtilityUsagePeriod = UtilityPeriod


@dataclass
class UtilitySpend(ApiObject):
    _api_fields: ClassVar = (
        ApiField("type"),
        ApiField("currency"),
        ApiField("values", data_type=UtilitySpendPeriod),
    )

    type: str
    currency: str
    values: List[UtilitySpendPeriod]

    @property
    def periods(self):
        return self.values


@dataclass
class UtilityUsage(ApiObject):
    _api_fields: ClassVar = (
        ApiField("type"),
        ApiField("unit"),
        ApiField("values", data_type=UtilityUsagePeriod),
    )

    type: str
    unit: str
    values: List[UtilityUsagePeriod]

    @property
    def periods(self):
        return self.values


@dataclass
class UtilityContractReminder(ApiObject):
    _api_fields: ClassVar = (
        ApiField("utility_contract_id", data_type=int),
        ApiField("user_id", data_type=str),
        ApiField("user_event_subscription_id", data_type=str),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    utility_contract_id: int
    user_id: str
    user_event_subscription_id: str
    created_at: datetime
    updated_at: datetime


@dataclass
class UtilityContract(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id", data_type=int),
        ApiField("name"),
        ApiField("facility_id", data_type=int),
        ApiField("status"),
        ApiField("start_date", data_type=Parsers.date),
        ApiField("end_date", data_type=Parsers.date),
        ApiField("rate_narrative"),
        ApiField("file_id"),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
        ApiField("created_by"),
        ApiField("utility_contract_reminders", data_type=UtilityContractReminder),
        ApiField("report_event_id"),
        ApiField("report_event", data_type=Event),
    )

    id: int
    name: str
    facility_id: int
    status: str
    start_date: datetime
    end_date: datetime
    rate_narrative: str
    file_id: str
    created_at: datetime
    updated_at: datetime
    created_by: str
    utility_contract_reminders: List[UtilityContractReminder]
    report_event_id: str
    report_event: Event


@dataclass
class UtilityStatement(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id", data_type=int),
        ApiField("utility_meter_id", data_type=int),
        ApiField("statement_month", data_type=str),
        ApiField("statement_year", data_type=str),
        ApiField("interval_start", data_type=Parsers.date),
        ApiField("interval_end", data_type=Parsers.date),
        ApiField("file_id", data_type=int),
        ApiField("is_validated", data_type=bool),
        ApiField("pm_id", data_type=int),
        ApiField("uploaded_to_pm", data_type=bool),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: int
    utility_meter_id: int
    statement_month: str
    statement_year: str
    interval_start: date
    interval_end: date
    file_id: int
    is_validated: bool
    pm_id: int
    uploaded_to_pm: bool
    created_at: datetime
    updated_at: datetime


@dataclass
class UtilityMeter(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id", data_type=int),
        ApiField("label", data_type=str),
        ApiField("utility_account_id", data_type=int),
        ApiField("building_id", data_type=int),
        ApiField("service_type", data_type=str),
        ApiField("logical_meter_id", data_type=str),
        ApiField("meter_number", data_type=str),
        ApiField("active_start", data_type=Parsers.date),
        ApiField("active_end", data_type=Parsers.date),
        ApiField("pm_id", data_type=int),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: int
    label: str
    utility_account_id: int
    building_id: int
    service_type: str
    logical_meter_id: str
    meter_number: str
    active_start: date
    active_end: date
    pm_id: int
    created_at: datetime
    updated_at: datetime


@dataclass
class UtilityAccount(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id", data_type=int),
        ApiField("logical_account_id", data_type=str),
        ApiField("facility_id", data_type=int),
        ApiField("account_number", data_type=str),
        ApiField("label", data_type=str),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: int
    logical_account_id: int
    facility_id: int
    account_number: str
    label: str
    created_at: datetime
    updated_at: datetime
