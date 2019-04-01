from typing import Any, Callable, Dict, List, Optional, Set, Tuple

from contxt.services.api import ApiField, ApiObject, Parsers


class ConfigValue(ApiObject):
    api_fields = (
        ApiField("value_id"),
        ApiField("key", creatable=True, updatable=True),
        ApiField("value", creatable=True, updatable=True),
        ApiField("value_type", creatable=True, updatable=True),
    )

    def __init__(
            self,
            key: str,
            value: Any,
            value_type: str,
            value_id: Optional[str] = None,
    ):
        self.value_id = value_id
        self.key = key
        self.value = value
        self.value_type = value_type


class OrganizationUser(ApiObject):
    api_fields = (
        ApiField("id"),
        ApiField("user_id"),
        ApiField("organization_id"),
        ApiField("is_primary"),
        ApiField("created_at"),
        ApiField("updated_at"),
    )

    def __init__(
            self,
            id: str,
            user_id: str,
            organization_id: str,
            is_primary: bool,
            created_at: Optional[str] = None,
            updated_at: Optional[str] = None,
    ):
        super().__init__()
        self.id = id
        self.user_id = user_id
        self.organization_id = organization_id
        self.is_primary = is_primary
        self.created_at = created_at
        self.updated_at = updated_at


# TODO: hide organization_user, updated_at
class Organization(ApiObject):
    api_fields = (
        ApiField("id"),
        ApiField("name"),
        ApiField("legacy_organization_id"),
        ApiField("OrganizationUser", attr_key="organization_user", optional=True),
        ApiField("created_at"),
        ApiField("updated_at"),
    )

    def __init__(
            self,
            name: str,
            id: Optional[str] = None,
            legacy_organization_id: Optional[int] = None,
            organization_user: Optional[OrganizationUser] = None,
            created_at: Optional[str] = None,
            updated_at: Optional[str] = None,
    ):
        super().__init__()
        self.id = id
        self.legacy_id = legacy_organization_id
        self.name = name
        self.organization_user = organization_user
        self.created_at = created_at
        self.updated_at = updated_at


# TODO: hide created_at, updated_at
class Role(ApiObject):

    def __init__(
            self,
            id: str,
            name: str,
            description: str,
            organization_id: str,
            created_at: Optional[str] = None,
            updated_at: Optional[str] = None,
    ):
        super().__init__()
        self.id = id
        self.name = name
        self.description = description
        self.organization_id = organization_id
        self.created_at = created_at
        self.updated_at = updated_at


# TODO: hide email, roles, organizations
class User(ApiObject):

    def __init__(
            self,
            id: str,
            first_name: str,
            last_name: str,
            email: str,
            is_activated: str,
            roles: List[Role],  # Roles
            is_superuser: bool,
            organizations: List[Organization],
            phone_number: str,
            created_at: Optional[str] = None,
            updated_at: Optional[str] = None,
    ):
        super().__init__()
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_activated = is_activated
        self.roles = roles
        self.organizations = organizations

    # def get_dict(self):
    #     return {
    #         **super().get_dict(),
    #         'roles': ', '.join([role.name for role in self.roles]),
    #     }
