from datetime import datetime
from enum import Enum
from json import loads
from typing import Any, Dict, List, Optional

from contxt.models.base import UUID, BaseModel, dataclass, field
from contxt.utils import cachedproperty, make_logger

logger = make_logger(__name__)


class ConfigValueType(Enum):
    FLOAT = "float"
    INTEGER = "integer"
    JSON = "json"
    STRING = "string"


@dataclass
class ConfigValue(BaseModel):
    id: UUID
    configuration_id: UUID
    key: str
    value: str
    type: ConfigValueType = field(enum=True)
    is_hidden: bool
    created_at: datetime
    updated_at: datetime

    @cachedproperty
    def parsed_value(self) -> Any:
        """Parse `value` based on `type`"""
        try:
            if self.type == ConfigValueType.FLOAT:
                return float(self.value)
            elif self.type == ConfigValueType.INTEGER:
                return int(self.value)
            elif self.type == ConfigValueType.JSON:
                return loads(self.value)
            elif self.type == ConfigValueType.STRING:
                return str(self.value)
        except Exception as e:
            logger.error(
                f"Failed to parse {type(self).__name__} {self.value} as"
                f" {self.type.value}: {e}"
            )
        return self.value


@dataclass
class Config(BaseModel):
    id: UUID
    environment_id: UUID
    name: str
    values: List[ConfigValue] = field(key="ConfigurationValues")
    created_at: datetime
    updated_at: datetime
    description: Optional[str]

    @cachedproperty
    def parsed_values(self) -> Dict[str, Any]:
        return {v.key: v.parsed_value for v in self.values}


@dataclass
class OrganizationUser(BaseModel):
    id: UUID
    organization_id: UUID
    user_id: str
    created_at: datetime
    updated_at: datetime
    is_primary: Optional[bool]


@dataclass
class Organization(BaseModel):
    id: UUID
    name: Optional[str] = field(post=True)
    created_at: datetime
    updated_at: datetime
    legacy_id: Optional[int] = field(key="legacy_organization_id")
    slug: str
    organization_user: Optional[OrganizationUser] = field(key="OrganizationUser")


@dataclass
class UserRole(BaseModel):
    id: UUID
    role_id: UUID
    user_id: str
    mapped_from_external_group: bool
    created_at: datetime
    updated_at: datetime


@dataclass
class Role(BaseModel):
    id: UUID
    name: str
    description: str
    user_role: UserRole = field(key="UserRole")
    created_at: datetime
    updated_at: datetime
    organization_id: Optional[str]


@dataclass
class User(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str
    is_superuser: bool
    is_activated: bool
    created_at: datetime
    updated_at: datetime
    phone_number: Optional[str]
    # roles: List[Role] = field(key="Roles")
    # organizations: List[Organization]
