from dataclasses import dataclass, field
from datetime import datetime
from json import loads
from typing import ClassVar, Optional, List

from . import ApiField, ApiObject, Parsers


@dataclass
class UtilityProvider(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("label", creatable=True),
        ApiField("createdAt", data_type=Parsers.datetime),
        ApiField("updatedAt", data_type=Parsers.datetime),
    )

    id: int
    label: str
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


@dataclass
class RateScheduleApplicability(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("rate_schedule_id"),
        ApiField("min_demand"),
        ApiField("max_demand"),
        ApiField("demand_history"),
        ApiField("min_consumption"),
        ApiField("max_consumption"),
        ApiField("consumption_history"),
        ApiField("min_voltage"),
        ApiField("max_voltage"),
        ApiField("voltage_category"),
        ApiField("phase_wiring")
    )

    id: int
    rate_schedule_id: int
    min_demand: int
    max_demand: int
    demand_history: str
    min_consumption: int
    max_consumption: int
    consumption_history: str
    min_voltage: int
    max_voltage: int
    voltage_category: str
    phase_wiring: str


@dataclass
class RateScheduleAttribute(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id")
    )

    id: int


@dataclass
class RateScheduleFixedCharge(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("rate_schedule_id"),
        ApiField("name"),
        ApiField("amount"),
        ApiField("createdAt", data_type=Parsers.datetime),
        ApiField("updatedAt", data_type=Parsers.datetime),
    )

    id: int
    rate_schedule_id: int
    name: str
    amount: int
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


@dataclass
class DemandTierRate(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id")
    )

    id: int


@dataclass
class DemandSeasonPeriod(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id")
    )

    id: int


@dataclass
class DemandSeason(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id")
    )

    id: int


@dataclass
class EnergyTierRate(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("energy_season_period_id"),
        ApiField("unit_start_value"),
        ApiField("unit_stop_value"),
        ApiField("unit"),
        ApiField("rate"),
        ApiField("adjustment"),
        ApiField("energySeasonPeriodId"),
    )

    id: int
    energy_season_period_id: int
    energySeasonPeriodId: int
    unit_start_value: int
    unit_stop_value: int
    unit: str
    rate: int
    adjustment: Optional[int] = None


@dataclass
class EnergySeasonPeriod(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("energy_season_id"),
        ApiField("day_of_week_start"),
        ApiField("hour_start"),
        ApiField("minute_start"),
        ApiField("day_of_week_end"),
        ApiField("hour_end"),
        ApiField("minute_end"),
        ApiField("period_name"),
        ApiField("energySeasonId"),
        ApiField("energy_tier_rates"),
    )

    id: int
    energy_season_id: int
    day_of_week_start: int
    hour_start: int
    minute_start: int
    day_of_week_end: int
    hour_end: int
    minute_end: int
    period_name: str
    energySeasonId: int
    energy_tier_rates: EnergyTierRate


@dataclass
class EnergySeason(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("rate_schedule_id"),
        ApiField("season_name"),
        ApiField("season_type"),
        ApiField("start_month"),
        ApiField("start_day"),
        ApiField("end_month"),
        ApiField("end_day"),
        ApiField("energy_season_periods")
    )

    id: int
    rate_schedule_id: int
    season_name: str
    season_type: str
    start_month: int
    start_day: int
    end_month: int
    end_day: int
    energy_season_periods: List[EnergySeasonPeriod]


@dataclass
class RateSchedule(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("label", creatable=True),
        ApiField("description", creatable=True),
        ApiField("rate_schedule_type_id", creatable=True),
        ApiField("effective_start_date", data_type=Parsers.datetime, creatable=True),
        ApiField("effective_end_date", data_type=Parsers.datetime, creatable=True),
        ApiField("utility_provider_id", creatable=True),
        ApiField("sector", creatable=True),
        ApiField("source", creatable=True),
        ApiField("uri", creatable=True),
        ApiField("supersedes_rate_schedule_id", creatable=True),
        ApiField("openei_id", creatable=True),
        ApiField("is_rtp_rate", creatable=True),
        ApiField("is_published", creatable=True),
        ApiField("facility_id", creatable=True),
        ApiField("utility_contract_id", creatable=True),
        ApiField("utility_provider", data_type=UtilityProvider),
        ApiField("rate_schedule_applicability", data_type=RateScheduleApplicability),
        ApiField("rate_schedule_attributes", data_type=RateScheduleAttribute),
        ApiField("rate_schedule_fixed_charges", data_type=RateScheduleFixedCharge),
        ApiField("energy_seasons", data_type=EnergySeason),
        ApiField("demand_seasons", data_type=DemandSeason),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("updated_at", data_type=Parsers.datetime),
    )

    id: int
    label: str
    description: str
    rate_schedule_type_id: int
    effective_start_date: datetime
    utility_provider_id: int
    sector: str
    is_rtp_rate: bool
    is_published: bool
    utility_provider: UtilityProvider
    rate_schedule_applicability: Optional[RateScheduleApplicability] = None
    rate_schedule_attributes: Optional[List[RateScheduleAttribute]] = field(default_factory=list)
    rate_schedule_fixed_charges: Optional[List[RateScheduleFixedCharge]] = field(default_factory=list)
    energy_seasons: Optional[List[EnergySeason]] = field(default_factory=list)
    demand_seasons: Optional[List[DemandSeason]] = field(default_factory=list)
    facility_id: Optional[int] = None
    utility_contract_id: Optional[int] = None
    openei_id: Optional[str] = None
    supersedes_rate_schedule_id: Optional[int] = None
    uri: Optional[str] = None
    source: Optional[str] = None
    effective_end_date: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

