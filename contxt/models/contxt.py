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
    key: str
    value: str
    type: ConfigValueType = field(enum=True)
    configuration_id: UUID
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
    name: str
    description: Optional[str]
    values: List[ConfigValue] = field(key="ConfigurationValues")
    environment_id: UUID
    created_at: datetime
    updated_at: datetime

    @cachedproperty
    def parsed_values(self) -> Dict[str, Any]:
        return {v.key: v.parsed_value for v in self.values}


@dataclass
class User(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    phone_number: Optional[str]
    is_superuser: bool
    is_activated: bool
    created_at: datetime
    updated_at: datetime


@dataclass
class OrganizationUser(BaseModel):
    id: UUID
    user_id: str
    organization_id: UUID
    is_primary: bool
    created_at: datetime
    updated_at: datetime


@dataclass
class Organization(BaseModel):
    id: UUID
    name: str = field(post=True)
    slug: str = field(post=True)
    legacy_id: Optional[int] = field(key="legacy_organization_id")
    created_at: datetime
    updated_at: datetime
    organization_user: Optional[OrganizationUser] = field(key="OrganizationUser")
