from datetime import datetime
from typing import List, Optional

from contxt.models.base import UUID, BaseModel, RawDict, dataclass, field

CostCenter = RawDict
Info = RawDict


@dataclass
class Tag(BaseModel):
    id: int
    facility_id: int
    name: Optional[str]
    created_at: datetime
    updated_at: datetime


@dataclass
class Organization(BaseModel):
    id: UUID
    name: str
    created_at: datetime
    updated_at: datetime


@dataclass
class Facility(BaseModel):
    id: int
    name: str
    slug: str
    timezone: str
    tags: List[Tag]
    organization_id: UUID
    organization: Organization = field(key="Organization")
    info: Info = field(key="Info")
    created_at: datetime
    # updated_at: datetime
    deleted_at: Optional[datetime]
    address1: Optional[str]
    address2: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]
    asset_id: Optional[UUID]
    geometry_id: Optional[UUID]
    weather_location_id: Optional[int]
    cost_centers: List[CostCenter] = field(default_factory=list)
