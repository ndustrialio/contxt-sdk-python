from datetime import datetime
from enum import Enum
from typing import List, Optional

from contxt.models.base import UUID, BaseModel, dataclass, field
from contxt.models.iot import Field


class ResourceType(Enum):
    COMBINED = "combined"
    ELECTRIC = "electric"
    GAS = "gas"
    WATER = "water"


@dataclass
class Baseline(BaseModel):
    id: int
    start_month: int
    start_year: int
    end_month: int
    end_year: int
    created_at: datetime
    updated_at: datetime


@dataclass
class MainService(BaseModel):
    id: int
    facility_id: int
    name: str
    resource_type: ResourceType = field(key="type", enum=True)
    demand_field_id: int
    usage_field_id: int
    demand_field: Field
    usage_field: Field
    created_at: datetime
    updated_at: datetime


@dataclass
class Facility(BaseModel):
    id: int
    name: str
    asset_id: UUID
    organization_id: UUID
    baseline: Baseline
    main_services: List[MainService]
    created_at: datetime
    updated_at: datetime


@dataclass
class UtilityValue(BaseModel):
    date: str
    value: Optional[float]
    pro_forma_date: Optional[str] = None


@dataclass
class UtilitySpend(BaseModel):
    type: ResourceType = field(enum=True)
    currency: str
    values: List[UtilityValue]


@dataclass
class UtilityUsage(BaseModel):
    type: ResourceType = field(enum=True)
    unit: str
    values: List[UtilityValue]
