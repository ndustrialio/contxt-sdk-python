from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import ClassVar, Dict, List, Optional

from . import ApiField, ApiObject, Parsers
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
        ApiField("date"),
        ApiField("value"),
        ApiField("pro_forma_date", optional=True),
    )

    date: str
    value: str
    pro_forma_date: Optional[str] = None


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
    values: Dict

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
