from contxt.models import ApiField, ApiObject, Parsers
from contxt.models.contxt import Organization


class Facility(ApiObject):
    _api_fields = (
        ApiField("id", data_type=int),
        ApiField("name"),
        ApiField("address1"),
        ApiField("address2"),
        ApiField("city"),
        ApiField("state"),
        ApiField("zip", data_type=int),
        ApiField("timezone"),
        ApiField("geometry_id"),
        ApiField("asset_id"),
        ApiField("tags"),
        ApiField("organization_id"),
        ApiField("Organization", attr_key="organization", data_type=Organization),
        ApiField(
            "Info",
            attr_key="info",
            data_type=lambda o: {k: Parsers.unknown(v) for k, v in o.items()},
        ),
        ApiField("created_at", data_type=Parsers.datetime),
        ApiField("weather_location_id"),
    )

    def __init__(
        self,
        id: int,
        name: str,
        address1: str,
        address2: str,
        city: str,
        state: str,
        zip: str,
        timezone: str,
        geometry_id: str,
        asset_id: str,
        tags: list,
        organization_id: str,
        organization: Organization,
        info: dict,
        weather_location_id: str,
        created_at: str,
    ) -> None:
        super().__init__()
        self.id = id
        self.name = name
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zip = zip
        self.timezone = timezone
        self.geometry_id = geometry_id
        self.asset_id = asset_id
        self.tags = tags
        self.organization_id = organization_id
        self.organization = organization
        self.weather_location_id = weather_location_id
        self.info = info
        self.created_at = created_at
