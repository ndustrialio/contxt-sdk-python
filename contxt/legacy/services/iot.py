from datetime import datetime
from typing import Optional

from contxt.legacy.models.iot import (
    Feed,
    Field,
    FieldCategory,
    FieldGrouping,
    FieldGroupingOwner,
    UnprovisionedField,
)
from contxt.legacy.services import (
    GET,
    APIObjectCollection,
    DataResponse,
    PagedEndpoint,
    PagedResponse,
    Service,
)
from contxt.utils import Utils

CONFIGS_BY_ENVIRONMENT = {
    "production": {
        "base_url": "https://feeds.api.ndustrial.io/",
        "audience": "iznTb30Sfp2Jpaf398I5DN6MyPuDCftA",
    }
}


class IOTService(Service):
    """
    Service to interact with our IOT API.
    """

    def __init__(self, auth, environment="production"):

        if environment not in CONFIGS_BY_ENVIRONMENT:
            raise Exception("Invalid environment specified")

        self.env = CONFIGS_BY_ENVIRONMENT[environment]

        super().__init__(
            base_url=self.env["base_url"],
            access_token=auth.get_token_provider(self.env["audience"]).access_token,
        )

    def get_all_groupings(self, facility_id: int):

        response = PagedResponse(
            PagedEndpoint(
                base_url=self.base_url,
                client=self.client,
                request=GET(uri=f"facilities/{facility_id}/groupings"),
                parameters={},
            )
        )

        groupings = [
            FieldGrouping(
                record,
                owner_obj=FieldGroupingOwner(record["Owner"]),
                category_obj=FieldCategory(record["FieldCategory"])
                if record["FieldCategory"] is not None
                else None,
                field_obj_list=[Field(field) for field in record["Fields"]],
            )
            for record in response
        ]
        return APIObjectCollection(groupings)

    def get_single_grouping(self, grouping_id: str):

        response = self.execute(GET(uri=f"groupings/{grouping_id}"))

        if response:
            return FieldGrouping(
                response,
                owner_obj=FieldGroupingOwner(response["Owner"]),
                category_obj=FieldCategory(response["FieldCategory"])
                if response["FieldCategory"] is not None
                else None,
                field_obj_list=[Field(field) for field in response["Fields"]],
            )
        else:
            return None

    def get_data_for_field(
        self,
        output_id: int,
        field_human_name: str,
        start_time: datetime,
        window: int,
        end_time: Optional[datetime] = None,
        limit: int = 1000,
    ):

        params = {
            "timeStart": str(Utils.get_epoch_time(start_time)),
            "window": str(window),
            "limit": limit,
        }

        if end_time:
            params["timeEnd"] = str(Utils.get_epoch_time(end_time))

        return DataResponse(
            data=self.execute(
                GET(uri=f"outputs/{output_id}/fields/{field_human_name}/data").params(
                    params
                ),
                execute=True,
            ),
            client=self.client,
        )

    def get_field_descriptors(self, feed_id, limit=100, offset=0, execute=True):
        assert isinstance(feed_id, int)
        # assert isinstance(limit, int)
        # assert isinstance(offset, int)

        params = {"limit": limit, "offset": offset}

        return self.execute(
            GET(uri=f"feeds/{feed_id}/fields").params(params), execute=True
        )

    def get_feeds_collection(
        self, facility_id: Optional[int] = None, key: Optional[str] = None
    ):

        params = {}

        if facility_id:
            params["facility_id"] = facility_id

        if key:
            params["key"] = key

        response = PagedResponse(
            PagedEndpoint(
                base_url=self.base_url,
                client=self.client,
                request=GET(uri="feeds"),
                parameters=params,
            )
        )

        return (
            APIObjectCollection([Feed(record) for record in response])
            if response
            else None
        )

    def get_all_fields(self, facility_id: int):
        response = PagedResponse(
            PagedEndpoint(
                base_url=self.base_url,
                client=self.client,
                request=GET(uri=f"facilities/{facility_id}/fields"),
                parameters={},
            )
        )

        return (
            APIObjectCollection([Field(record) for record in response])
            if response
            else None
        )

    def get_unprovisioned_fields(self, feed_id: int):
        response = self.execute(GET(uri=f"feeds/{feed_id}/fields/unprovisioned"))

        return (
            APIObjectCollection([UnprovisionedField(record) for record in response])
            if response
            else None
        )
