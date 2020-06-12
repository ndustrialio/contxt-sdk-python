from dataclasses import dataclass
from typing import ClassVar

from . import ApiField, ApiObject, Parsers
from .contxt import Organization


@dataclass
class Facility(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id", data_type=int),
        ApiField("name"),
        ApiField("address1"),
        ApiField("address2"),
        ApiField("city"),
        ApiField("state"),
        ApiField("zip"),
        ApiField("timezone"),
        ApiField("geometry_id"),
        ApiField("asset_id"),
        ApiField("tags"),
        ApiField("organization_id"),
        ApiField("Organization", attr_key="organization", data_type=Organization),
        ApiField(
            "Info", attr_key="info", data_type=lambda o: {k: Parsers.unknown(v) for k, v in o.items()}
        ),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("weather_location_id"),
        ApiField("slug"),
    )

    id: int
    name: str
    address1: str
    address2: str
    city: str
    state: str
    zip: str
    timezone: str
    geometry_id: str
    asset_id: str
    tags: list
    organization_id: str
    organization: Organization
    info: dict
    weather_location_id: str
    created_at: str
    slug: str
