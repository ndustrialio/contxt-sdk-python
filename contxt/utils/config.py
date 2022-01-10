import pytz
import yaml
from datetime import datetime
from yaml import load, SafeLoader, YAMLError, safe_dump
from marshmallow_dataclass import class_schema
from typing import Dict
import logging

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, ForwardRef, List, Dict, Any

logger = logging.getLogger(__name__)
logging.basicConfig(format='[%(module)s %(levelname)s:%(asctime)s] %(message)s', level=logging.INFO)


class ProjectConfigException(Exception):
    pass

class ContextException(Exception):
    pass


@dataclass
class IOTFetchConfig:
    feedKey: str
    fieldDescriptor: str


@dataclass
class ReportConfig:
    type: str
    subscribers: List[str]


@dataclass
class SuggestionConfig:
    project: str
    config: Optional[Dict[str, Any]]
    project_id: Optional[str]


@dataclass
class ComponentConfig:
    name: str
    slug: str
    iotInfo: IOTFetchConfig
    id: Optional[str]


@dataclass
class RateAlertConfig:
    warningMinPrice: float
    warningMinQuantile: float
    alertingMinPrice: float
    alertingMinQuantile: float


@dataclass
class RateFetchConfig:
    type: str
    prettySummary: str
    iotInfo: IOTFetchConfig


@dataclass
class RateConfig:
    thresholds: RateAlertConfig
    fetchInfo: List[RateFetchConfig]

    def get_feed_for_type(self, type: str) -> RateFetchConfig:
        for fetchConfig in self.fetchInfo:
            if fetchConfig.type == type:
                return fetchConfig


@dataclass
class EvaporatorConfig:
    slug: str
    label: str
    stateAttributes: Optional[Dict[str, str]] = field(default_factory=dict)


@dataclass
class BlastCellConfig:
    slug: str
    evaporatorId: Optional[str] = None
    stateAttributes: Optional[Dict[str, str]] = field(default_factory=dict)


@dataclass
class RefrigerationConfig:
    feedKey: str
    blastCells: Optional[List[BlastCellConfig]]
    evaporators: Optional[List[EvaporatorConfig]]

    def get_blast_cell_with_slug(self, slug: str) -> BlastCellConfig:
        for cell in self.blastCells:
            if cell.slug == slug:
                return cell

    def get_evaporator_with_slug(self, slug: str) -> EvaporatorConfig:
        for evap in self.evaporators:
            if evap.slug == slug:
                return evap

@dataclass
class FacilityConfig:
    name: str
    slug: str
    id: int
    timezone: str
    reports: Optional[List[ReportConfig]]
    suggestions: Optional[List[SuggestionConfig]]
    components: Optional[List[ComponentConfig]]
    rates: Optional[RateConfig] = None
    refrigeration: Optional[RefrigerationConfig] = None

    def get_facility_component_with_slug(self, slug: str):
        for component in self.components:
            if component.slug == slug:
                return component

    def get_report_with_type(self, type: str):
        for report in self.reports:
            if report.type == type:
                return report

    @property
    def current_facility_time(self) -> datetime:
        return datetime.now(pytz.timezone(self.timezone))


@dataclass
class ReportLoadConfig:
    type: str
    module: str
    classname: str


@dataclass
class Config:
    facilityConfigs: List[FacilityConfig]
    reportConfigs: Optional[List[ReportLoadConfig]]

    def get_config_by_facility_id(self, facility_id: int) -> FacilityConfig:
        for facility in self.facilityConfigs:
            if facility.id == facility_id:
                return facility

    def get_config_by_facility_slug(self, slug: str) -> FacilityConfig:
        for facility in self.facilityConfigs:
            if facility.slug == slug:
                return facility

    def get_report_config_by_type(self, type: str) -> ReportLoadConfig:
        for report_load_config in self.reportConfigs:
            if report_load_config.type == type:
                return report_load_config


@dataclass
class ApiEnvironment:
    """An environment for an API.

    Note `client_id` is only needed if authentication is required.
    """

    baseUrl: str
    clientId: str
    authProvider: str = 'contxt.auth0.com'
    authRequired: bool = True


@dataclass
class ContxtEnvironmentConfig:
    service: str
    environment: str
    clientId: str
    apiEnvironment: ApiEnvironment
    clientSecret: str = ""


@dataclass
class ContxtCliEnvironmentConfig:
    environment: str
    clientId: str
    forAuthProvider: str
    apiEnvironment: ApiEnvironment

    def to_contxt_environment_config(self) -> ContxtEnvironmentConfig:
        return ContxtEnvironmentConfig(environment=self.environment,
                                       service=self.forAuthProvider,
                                       clientId=self.clientId,
                                       apiEnvironment=self.apiEnvironment)

@dataclass
class Context:
    environment: str


@dataclass
class CurrentContext:
    environment: str


@dataclass
class CustomEnvironmentConfig:
    defaults: Dict[str, Optional[str]]
    currentContext: Dict[str, CurrentContext]
    serviceConfigs: List[ContxtEnvironmentConfig]
    cliConfigs: Optional[List[ContxtCliEnvironmentConfig]]

    def get_service_for_current_context(self, service_name: str) -> ContxtEnvironmentConfig:
        current_env = self.currentContext.get(service_name)

        if not current_env:
            raise ContextException(f'Current context not specified for {service_name}')

        for service_config in self.serviceConfigs:
            if service_config.service == service_name and service_config.environment == current_env.environment:
                return service_config

        raise ContextException(f'Environment not found for {service_name} with environment {current_env}')

    def get_cli_environment_for_auth_provider(self, auth_provider: str) -> ContxtCliEnvironmentConfig:
        for cli_config in self.cliConfigs:
            if cli_config.forAuthProvider == auth_provider:
                return cli_config

        raise ContextException(f'CLI environment for auth provider {auth_provider} is not specified in config')


def load_config_from_file(file='./../config.yml') -> Config:
    logger.info(f'Loading config from file: {file}')
    with open(file, 'r') as stream:
        try:
            config_yaml = load(stream, Loader=yaml.Loader)
        except YAMLError as e:
            logger.error(e)
            raise

    config_schema = class_schema(Config)

    result = config_schema().load(config_yaml)
    return result


def write_config_class_to_file(file: str, obj, config_class):
    logger.info(f'Writing config to file: {file}')
    with open(file, 'w') as stream:
        try:
            config_schema = class_schema(config_class)()
            result = config_schema.dump(obj)
            safe_dump(result, stream)
        except YAMLError as e:
            logger.error(e)
            raise


def load_config_class_from_file(file: str, config_class):
    logger.info(f'Loading config from file: {file}')
    with open(file, 'r') as stream:
        try:
            config_yaml = load(stream, Loader=yaml.SafeLoader)
        except YAMLError as e:
            logger.error(e)
            raise

    config_schema = class_schema(config_class)

    result = config_schema().load(config_yaml)
    return result
