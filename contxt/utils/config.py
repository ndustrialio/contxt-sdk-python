from yaml import load, SafeLoader, YAMLError
from marshmallow_dataclass import class_schema
from typing import Dict

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, ForwardRef, List, Dict, Any


class ProjectConfigException(Exception):
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
class BlastCellConfig:
    slug: str
    timerField: str
    stateField: str


@dataclass
class RefrigerationConfig:
    feedKey: str
    blastCells: Optional[List[BlastCellConfig]]

    def get_blast_cell_with_slug(self, slug: str) -> BlastCellConfig:
        for cell in self.blastCells:
            if cell.slug == slug:
                return cell


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


def load_config_from_file(file='./../config.yml') -> Config:
    print(f'Loading config from file: {file}')
    with open(file, 'r') as stream:
        try:
            config_yaml = load(stream, Loader=SafeLoader)
        except YAMLError as e:
            print(e)
            raise

    config_schema = class_schema(Config)

    result = config_schema().load(config_yaml)
    return result


def load_config_class_from_file(file: str, config_class):
    print(f'Loading config from file: {file}')
    with open(file, 'r') as stream:
        try:
            config_yaml = load(stream, Loader=SafeLoader)
        except YAMLError as e:
            print(e)
            raise

    config_schema = class_schema(config_class)

    result = config_schema().load(config_yaml)
    return result
