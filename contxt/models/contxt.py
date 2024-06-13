from dataclasses import dataclass
from datetime import datetime
from json import loads
from typing import Any, ClassVar, List, Optional

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
        ApiField("slug", optional=True),
        ApiField(
            "OrganizationUser", attr_key="organization_user", data_type=OrganizationUser, optional=True
        ),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    name: str
    id: Optional[str] = None
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
        ApiField("UserRole", attr_key="user_role", data_type=UserRole, optional=True),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    name: str
    description: str
    organization_id: str
    user_role: Optional[UserRole] = None
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
        ApiField("Roles", attr_key="roles", data_type=Role, optional=True),
        ApiField("is_superuser"),
        ApiField("organizations", data_type=Organization, optional=True),
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
    roles: Optional[List[Role]] = None
    organizations: Optional[List[Organization]] = None
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class ServiceEnvironmentVariable(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("service_id"),
        ApiField("environment"),
        ApiField("key"),
        ApiField("value"),
        ApiField("is_protected"),
        ApiField("config_map_value_id"),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: int
    service_id: int
    environment: str
    key: str
    value: str
    is_protected: bool
    config_map_value_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class Domain(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("name"),
        ApiField("cert_name"),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: int
    name: str
    cert_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class Frontend(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("service_id"),
        ApiField("vhost"),
        ApiField("force_ssl"),
        ApiField("domain_id"),
        ApiField("domain", data_type=Domain),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: int
    service_id: int
    vhost: str
    force_ssl: bool
    domain_id: int
    domain: Optional[Domain] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class Image(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("provider"),
        ApiField("image_name"),
        ApiField("image_tag_id"),
        ApiField("image_secret_id"),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: int
    provider: str
    image_name: str
    image_tag_id: str
    image_secret_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class Service(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id", data_type=int),
        ApiField("name"),
        ApiField("slug"),
        ApiField("type"),
        ApiField("project_id", data_type=int),
        ApiField("description"),
        ApiField("deployment_strategy"),
        ApiField("created_at", data_type=Parsers.datetime),
    )

    id: int
    name: str
    slug: str
    type: str
    project_id: int
    description: str
    deployment_strategy: str
    created_at: Optional[datetime] = None


@dataclass
class ServiceInstance(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id", data_type=int, optional=True),
        ApiField("name"),
        ApiField("organization_id"),
        ApiField("slug", optional=True),
        ApiField("description", optional=True),
        ApiField("descriptor", optional=True),
        ApiField("service_id", data_type=int, optional=True),
        ApiField("project_environment_id", optional=True),
        ApiField("client_id"),
        ApiField("command", optional=True),
        ApiField("arguments", optional=True),
        ApiField("last_deployed_at", optional=True),
        ApiField("last_configured_at", optional=True),
        ApiField("service_env_variables", data_type=ServiceEnvironmentVariable, optional=True),
        ApiField("frontend", data_type=Frontend, optional=True),
        ApiField("image", data_type=Image, optional=True),
        ApiField("service_type", optional=True),
        ApiField("created_at", data_type=Parsers.datetime, optional=True),
    )

    name: str
    client_id: str
    organization_id: str
    id: Optional[int] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    descriptor: Optional[str] = None
    service_id: Optional[int] = None
    project_environment_id: Optional[str] = None
    command: Optional[str] = None
    arguments: Optional[str] = None
    last_deployed_at: Optional[datetime] = None
    last_configured_at: Optional[datetime] = None
    service_type: Optional[str] = None
    service_env_variables: Optional[List[ServiceEnvironmentVariable]] = None
    frontend: Optional[Frontend] = None
    image: Optional[Image] = None
    created_at: Optional[datetime] = None


@dataclass
class Project(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id", data_type=int),
        ApiField("name"),
        ApiField("slug"),
        ApiField("description"),
        ApiField("type"),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("Roles", attr_key="roles", data_type=Role, optional=True),
        ApiField("Services", attr_key="services", data_type=Service, optional=True),
    )

    id: int
    name: str
    slug: str
    description: str
    type: str
    roles: Optional[List[Role]] = None
    services: Optional[List[Service]] = None
    created_at: Optional[datetime] = None


@dataclass
class ProjectEnvironment(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id", data_type=int),
        ApiField("slug"),
        ApiField("project_id", data_type=int),
        ApiField("cluster_id"),
        ApiField("cluster_slug"),
        ApiField("name"),
        ApiField("description"),
        ApiField("type"),
        ApiField("archived"),
        ApiField("created_at", data_type=Parsers.datetime),
    )

    id: int
    slug: str
    project_id: int
    cluster_id: str
    cluster_slug: str
    name: str
    description: str
    type: str
    created_at: Optional[datetime] = None


@dataclass
class EdgeNode(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id", data_type=str),
        ApiField("name"),
        ApiField("project_id"),
        ApiField("organization_id"),
        ApiField("description"),
        ApiField("client_id"),
        ApiField("created_at", data_type=Parsers.datetime),
    )

    id: str
    name: str
    project_id: int
    organization_id: str
    description: str
    client_id: str
    created_at: Optional[datetime] = None


@dataclass
class Cluster(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("description", creatable=True),
        ApiField("infrastructure_id", creatable=True),
        ApiField("organization_id", creatable=True),
        ApiField("region", creatable=True),
        ApiField("slug", creatable=True),
        ApiField("host", creatable=True),
        ApiField("type", creatable=True),
        ApiField("certificate_authority", creatable=True),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    description: str
    infrastructure_id: int
    organization_id: str
    region: str
    slug: str
    type: str
    host: Optional[str] = None
    id: Optional[str] = None
    certificate_authority: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class ServiceInstanceScope(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("service_instance_id"),
        ApiField("label"),
        ApiField("service_instance_grant_scopes", optional=True),
        ApiField("description"),
        ApiField("created_at"),
        ApiField("updated_at"),
    )

    id: str
    service_instance_id: int
    label: str
    description: str
    service_instance_grant_scopes: Optional[Any] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class ServiceInstanceGrant(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("from_service_instance_id", creatable=True),
        ApiField("to_service_instance_id", creatable=True),
        ApiField("auth0_id"),
        ApiField("ServiceInstanceScopes", data_type=ServiceInstanceScope, optional=True),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    from_service_instance_id: int
    to_service_instance_id: int
    auth0_id: Optional[str] = None
    id: Optional[str] = None
    ServiceInstanceScopes: Optional[List[ServiceInstanceScope]] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class ServiceInstanceGrantScope(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("service_instance_grant_id"),
        ApiField("service_instance_scope_id"),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: str
    service_instance_grant_id: str
    service_instance_scope_id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
