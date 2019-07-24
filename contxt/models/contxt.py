from datetime import datetime
from json import loads
from typing import List, Optional

from contxt.models import ApiField, ApiObject, Parsers


class ConfigValue(ApiObject):
    _api_fields = (
        ApiField("id"),
        ApiField("key"),
        ApiField("value"),
        ApiField("type"),
        ApiField("configuration_id"),
        ApiField("is_hidden", data_type=bool),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    def __init__(
        self,
        id: str,
        key: str,
        value: str,
        type: str,
        configuration_id: str,
        is_hidden: bool,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        super().__init__()
        self.id = id
        self.key = key
        self.value = self._init_value(value, type)
        self.type = type
        self.configuration_id = configuration_id
        self.is_hidden = is_hidden
        self.created_at = created_at
        self.updated_at = updated_at

    def _init_value(self, value, type):
        if type == "integer":
            return int(value)
        elif type == "json":
            return loads(value)
        else:
            return str(value)


class Config(ApiObject):
    _api_fields = (
        ApiField("id"),
        ApiField("name"),
        ApiField("description"),
        ApiField("environment_id"),
        ApiField(
            "ConfigurationValues", attr_key="config_values", data_type=ConfigValue
        ),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    def __init__(
        self,
        id: str,
        name: str,
        description: str,
        environment_id: str,
        config_values: List[ConfigValue],
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.description = description
        self.environment_id = environment_id
        self.config_values = config_values
        self.created_at = created_at
        self.updated_at = updated_at


class OrganizationUser(ApiObject):
    _api_fields = (
        ApiField("id"),
        ApiField("user_id"),
        ApiField("organization_id"),
        ApiField("is_primary", data_type=bool),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    def __init__(
        self,
        id: str,
        user_id: str,
        organization_id: str,
        is_primary: bool,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        super().__init__()
        self.id = id
        self.user_id = user_id
        self.organization_id = organization_id
        self.is_primary = is_primary
        self.created_at = created_at
        self.updated_at = updated_at


# TODO: hide organization_user, updated_at
class Organization(ApiObject):
    _api_fields = (
        ApiField("id"),
        ApiField("name", creatable=True),
        ApiField("legacy_organization_id", attr_key="legacy_id", optional=True),
        ApiField(
            "OrganizationUser",
            attr_key="organization_user",
            data_type=OrganizationUser,
            optional=True,
        ),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    def __init__(
        self,
        name: str,
        id: Optional[str] = None,
        legacy_id: Optional[int] = None,
        organization_user: Optional[OrganizationUser] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        super().__init__()
        self.id = id
        self.legacy_id = legacy_id
        self.name = name
        self.organization_user = organization_user
        self.created_at = created_at
        self.updated_at = updated_at


class UserRole(ApiObject):
    _api_fields = (
        ApiField("id"),
        ApiField("user_id"),
        ApiField("role_id"),
        ApiField("mapped_from_external_group", data_type=bool),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    def __init__(
        self,
        user_id: str,
        role_id: str,
        mapped_from_external_group: bool,
        id: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        super().__init__()
        self.id = id
        self.user_id = user_id
        self.role_id = role_id
        self.mapped_from_external_group = mapped_from_external_group
        self.created_at = created_at
        self.updated_at = updated_at


# TODO: hide created_at, updated_at
class Role(ApiObject):
    _api_fields = (
        ApiField("id"),
        ApiField("name"),
        ApiField("description"),
        ApiField("organization_id"),
        ApiField("UserRole", attr_key="user_role", data_type=UserRole),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    def __init__(
        self,
        name: str,
        description: str,
        organization_id: str,
        user_role: UserRole,
        id: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.description = description
        self.organization_id = organization_id
        self.user_role = user_role
        self.created_at = created_at
        self.updated_at = updated_at


# TODO: hide email, phone_number, is_superuser, roles (transform to list of
# role.name), organizations, created_at, updated_at
class User(ApiObject):
    _api_fields = (
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

    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        phone_number: str,
        is_activated: bool,
        is_superuser: bool,
        roles: List[Role],
        organizations: List[Organization],
        id: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        super().__init__()
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.is_activated = is_activated
        self.is_superuser = is_superuser
        self.roles = roles
        self.organizations = organizations
        self.created_at = created_at
        self.updated_at = updated_at
