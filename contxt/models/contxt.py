from dataclasses import dataclass
from datetime import datetime
from json import loads
from typing import ClassVar, List, Optional

from . import ApiField, ApiObject, Parsers


@dataclass
class ConfigValue(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("key"),
        ApiField("value"),
        ApiField("type"),
        ApiField("configuration_id"),
        ApiField("is_hidden", data_type=bool),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: str
    key: str
    value: str
    type: str
    configuration_id: str
    is_hidden: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    def __post_init__(self) -> None:
        self.value = self._init_value(self.value, self.type)

    def _init_value(self, value, type):
        if type == "integer":
            return int(value)
        elif type == "json":
            return loads(value)
        else:
            return str(value)


@dataclass
class Config(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("name"),
        ApiField("description"),
        ApiField("environment_id"),
        ApiField("ConfigurationValues", attr_key="config_values", data_type=ConfigValue),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: str
    name: str
    description: str
    environment_id: str
    config_values: List[ConfigValue]
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class OrganizationUser(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("user_id"),
        ApiField("organization_id"),
        ApiField("is_primary", data_type=bool),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: str
    user_id: str
    organization_id: str
    is_primary: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class Organization(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("name", creatable=True),
        ApiField("legacy_organization_id", attr_key="legacy_id", optional=True),
        ApiField("slug", optional=True),
        ApiField(
            "OrganizationUser", attr_key="organization_user", data_type=OrganizationUser, optional=True
        ),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    name: str
    id: Optional[str] = None
    legacy_id: Optional[int] = None
    slug: Optional[str] = None
    organization_user: Optional[OrganizationUser] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class UserRole(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("user_id"),
        ApiField("role_id"),
        ApiField("mapped_from_external_group", data_type=bool),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    user_id: str
    role_id: str
    mapped_from_external_group: bool
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class Role(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("name"),
        ApiField("description"),
        ApiField("organization_id"),
        ApiField("UserRole", attr_key="user_role", data_type=UserRole),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    name: str
    description: str
    organization_id: str
    user_role: UserRole
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class User(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("first_name"),
        ApiField("last_name"),
        ApiField("email"),
        ApiField("is_activated", data_type=bool),
        ApiField("Roles", attr_key="roles", data_type=Role),
        ApiField("is_superuser"),
        ApiField("organizations", data_type=Organization),
        ApiField("phone_number"),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    first_name: str
    last_name: str
    email: str
    phone_number: str
    is_activated: bool
    is_superuser: bool
    roles: List[Role]
    organizations: List[Organization]
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
