from datetime import datetime
from typing import Dict, List, Optional, Set, Tuple
from contxt.legacy.services import (GET, POST, DELETE, APIObjectCollection, DataResponse,
                                    PagedEndpoint, PagedResponse, Service, ApiRequest, APIObject)
from contxt.models.iot import (Feed, Field, FieldCategory, FieldGrouping,
                               FieldGroupingOwner, UnprovisionedField)
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

    def __init__(self, auth_module, environment='production'):

        if environment not in CONFIGS_BY_ENVIRONMENT:
            raise Exception("Invalid environment specified")

        self.env = CONFIGS_BY_ENVIRONMENT[environment]

        super().__init__(
            base_url=self.env['base_url'],
            access_token=auth_module.get_token_for_audience(
                self.env['audience']))
    """
    Groupings Operations
    """

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

    def create_grouping(self, grouping_obj):
        assert isinstance(grouping_obj, FieldGrouping)

        return FieldGrouping(self.execute(POST(uri=f'facilities/{grouping_obj.facility_id}/groupings')
                                          .body(grouping_obj.get_create_dict())),
                             owner_obj=None,
                             category_obj=None,
                             field_obj_list=[])

    def add_field_to_grouping(self, grouping_id, field_id):

        return self.execute(POST(uri=f'groupings/{grouping_id}/fields/{field_id}'))

    def set_fields_for_grouping(self, grouping_id, field_list):
        assert isinstance(grouping_id, str)
        assert isinstance(field_list, list)

        body = {'fields': field_list}

        return self.execute(POST(uri=f'groupings/{grouping_id}/fields')
                            .body(body))

    """
    Field Data Operations
    """
    def get_data_for_field(
            self,
            output_id: int,
            field_human_name: str,
            start_time: datetime,
            window: int,
            end_time: Optional[datetime] = None,
            limit: Optional[int] = 1000,
    ):

        params = {
            "timeStart": str(Utils.get_epoch_time(start_time)),
            "window": str(window),
            "limit": limit,
        }

        if end_time:
            params['timeEnd'] = str(Utils.get_epoch_time(end_time))

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

        return self.execute(GET(uri=f"feeds/{feed_id}/fields").params(params), execute=True)

    def get_feeds_collection(self, facility_id: Optional[int] = None, key: Optional[str] = None):

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
        response = self.execute(GET(uri=f'feeds/{feed_id}/fields/unprovisioned'))

        return APIObjectCollection([UnprovisionedField(record) for record in response]) if response else None

    def provision_field_for_feed(self, feed_id, field_obj):

        assert isinstance(feed_id, int)
        assert isinstance(field_obj, Field)

        return self.execute(POST(uri=f'feeds/{feed_id}/fields').body(field_obj.get_dict())
                            .content_type(ApiRequest.URLENCODED_CONTENT_TYPE))

    def get_fields_for_feed(self, feed_id):

        assert isinstance(feed_id, int)
        response = PagedResponse(
            PagedEndpoint(
                base_url=self.base_url,
                client=self.client,
                request=GET(uri=f'feeds/{feed_id}/fields'),
                parameters={}))

        return APIObjectCollection([Field(record) for record in response]) if response else None

    def unprovision_field(self, field_id):

        assert isinstance(field_id, int)

        return self.execute(DELETE(uri=f'fields/{field_id}'))

class FieldGrouping(APIObject):

    def __init__(self, grouping_api_object, owner_obj, category_obj, field_obj_list, keys_to_ignore=None):
        super().__init__(
            keys_to_ignore=keys_to_ignore if keys_to_ignore is not None else [
                'owner_id', 'is_public', 'created_at', 'updated_at', 'owner',
                'category', 'fields'
            ])

        self.id = grouping_api_object.get('id')
        self.label = grouping_api_object.get('label')
        self.slug = grouping_api_object.get('slug')
        self.description = grouping_api_object.get('description')
        self.facility_id = grouping_api_object.get('facility_id')
        self.owner_id = grouping_api_object.get('owner_id')
        self.is_public = grouping_api_object.get('is_public')
        self.created_at = grouping_api_object.get('created_at')
        self.updated_at = grouping_api_object.get('updated_at')
        self.field_category_id = grouping_api_object.get('field_category_id')
        self.owner = owner_obj
        self.category = category_obj
        self.fields = APIObjectCollection(field_obj_list)

    def get_dict(self):
        return {
            **super().get_dict(),
            'field_category_name': self.category.name if self.category else None,
            'field_count': len(self.fields)
        }

    def get_create_dict(self):
        create_dict = {
            "label": self.label,
            "description": self.description,
            "is_public": self.is_public,
        }

        # API can't handle sending None / null for field_category_id at the moment. remove when able to
        if self.field_category_id:
            create_dict["field_category_id"] = self.field_category_id

        return create_dict

class UnprovisionedField(APIObject):

    def __init__(self, unprovisioned_api_object):
        super().__init__()

        self.field_descriptor = unprovisioned_api_object['field_descriptor']
        self.assumed_type = unprovisioned_api_object['assumed_type']


class FieldCategory(APIObject):

    def __init__(self, category_api_object):
        super().__init__()

        self.id = category_api_object['id']
        self.name = category_api_object['name']
        self.description = category_api_object['description']
        self.organization_id = category_api_object['organization_id']
        self.parent_category_id = category_api_object['parent_category_id']
        self.created_at = category_api_object['created_at']
        self.updated_at = category_api_object['updated_at']


class FieldGroupingOwner(APIObject):

    def __init__(self, owner_api_object):
        super().__init__()

        self.id = owner_api_object['id']
        self.first_name = owner_api_object['first_name']
        self.last_name = owner_api_object['last_name']


class Field(APIObject):

    def __init__(self, field_api_object):
        super().__init__()

        self.id = field_api_object.get('id')
        self.label = field_api_object.get('label')
        self.output_id = field_api_object.get('output_id')
        self.field_descriptor = field_api_object.get('field_descriptor')
        self.field_human_name = field_api_object.get('field_human_name')
        self.is_hidden = field_api_object.get('is_hidden')
        self.status = field_api_object.get('status')
        self.units = field_api_object.get('units')
        self.value_type = field_api_object.get('value_type')
        self.feed_key = field_api_object.get('feed_key')


class Feed(APIObject):

    def __init__(self, feed_api_object):
        super().__init__()

        self.id = feed_api_object['id']
        self.feed_type_id = feed_api_object['feed_type_id']
        self.down_after = feed_api_object['down_after']
        self.key = feed_api_object['key']
        self.facility_id = feed_api_object['facility_id']
        self.timezone = feed_api_object['timezone']
        self.token = feed_api_object['token']
        self.status = feed_api_object['status']
        self.degraded_threshold = feed_api_object['degraded_threshold']
        self.critical_threshold = feed_api_object['critical_threshold']
        self.status_event_id = feed_api_object['status_event_id']
        self.created_at = feed_api_object['created_at']
