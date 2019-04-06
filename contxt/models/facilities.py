from contxt.models.contxt import Organization
from contxt.services.api import ApiField, ApiObject, Parsers


# Hide: address1, address2, geometry_id, tags, organization, info, weather_location_id
class Facility(ApiObject):
    _api_fields = (
        ApiField("id", type=int),
        ApiField("name"),
        ApiField("address1"),
        ApiField("address2"),
        ApiField("city"),
        ApiField("state"),
        ApiField("zip", type=int),
        ApiField("timezone"),
        ApiField("geometry_id"),
        ApiField("asset_id"),
        ApiField("tags"),
        ApiField("organization_id"),
        ApiField("Organization", attr_key="organization", type=Organization),
        ApiField("Info", attr_key="info", type=lambda o: {k: Parsers.unknown(v) for k, v in o.items()}),
        ApiField("created_at", type=Parsers.datetime),
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
            created_at: str,
            weather_location_id: str = None,
    ):
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

    # def get_dict(self):
    #     return {
    #         **super().get_dict(), 'organization_name': self.organization.name
    #     }
