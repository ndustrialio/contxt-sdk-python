from contxt.utils import get_epoch_time

from datetime import datetime

from contxt.services import (GET, APIObject, APIObjectCollection, DataResponse,
                             PagedEndpoint, PagedResponse, Service)

CONFIGS_BY_ENVIRONMENT = {
    'production': {
        'base_url': 'https://feeds.api.ndustrial.io/',
        'audience': 'iznTb30Sfp2Jpaf398I5DN6MyPuDCftA'
    }
}


class IOTService(Service):

    def __init__(self, auth_module, environment='production'):

        if environment not in CONFIGS_BY_ENVIRONMENT:
            raise Exception('Invalid environment specified')

        self.env = CONFIGS_BY_ENVIRONMENT[environment]

        super().__init__(
            base_url=self.env['base_url'],
            access_token=auth_module.get_token_for_client(
                self.env['audience']))

    def get_all_groupings(self, facility_id):

        assert isinstance(facility_id, int)

        params = {}

        response = PagedResponse(PagedEndpoint(base_url=self.base_url,
                                               client=self.client,
                                               request=GET(uri='facilities/{}/groupings'.format(facility_id)),
                                               parameters=params))

        groupings = []
        for record in response:

            groupings.append(FieldGrouping(record,
                                           owner_obj=FieldGroupingOwner(record['Owner']),
                                           category_obj=FieldCategory(record['FieldCategory']) if record['FieldCategory'] is not None else None,
                                           field_obj_list=[Field(field) for field in record['Fields']]
                                           ))

        return APIObjectCollection(groupings)

    def get_single_grouping(self, grouping_id):

        assert isinstance(grouping_id, str)

        response = self.execute(GET(uri='groupings/{}'.format(grouping_id)), execute=True)

        if response:
            return FieldGrouping(response,
                                 owner_obj=FieldGroupingOwner(response['Owner']),
                                 category_obj=FieldCategory(response['FieldCategory']) if response['FieldCategory'] is not None else None,
                                 field_obj_list=[Field(field) for field in response['Fields']]
                                 )
        else:
            return None

    def get_data_for_field(self, output_id, field_human_name, start_time, window, end_time=None, limit=1000):

        assert isinstance(start_time, datetime)
        assert isinstance(output_id, int)
        assert isinstance(field_human_name, str)
        assert isinstance(window, int)
        assert isinstance(limit, int)

        params = {'timeStart': str(get_epoch_time(start_time)),
                  'window': str(window),
                  'limit': limit
                  }

        if end_time:
            assert isinstance(end_time, datetime)
            params['timeEnd'] = str(get_epoch_time(end_time))

        data = DataResponse(data=self.execute(GET(uri='outputs/{}/fields/{}/data'.format(output_id, field_human_name))
                                              .params(params), execute=True),
                            client=self.client)
        return data

    def get_all_feeds(self, facility_id=None):

        params = {}
        if facility_id:
            assert isinstance(facility_id, int)
            params['facility_id'] = facility_id

        print('Getting all feeds')
        response = PagedResponse(PagedEndpoint(base_url=self.base_url,
                                               client=self.client,
                                               request=GET(uri='feeds'),
                                               parameters=params))

        feeds = []
        if response:
            for record in response:
                feeds.append(Feed(record))

            return APIObjectCollection(feeds)
        else:
            return None

    def get_all_fields(self, facility_id):

        params = {}

        response = PagedResponse(PagedEndpoint(base_url=self.base_url,
                                               client=self.client,
                                               request=GET(uri='facilities/{}/fields'.format(facility_id)),
                                               parameters=params))

        fields = []
        if response:
            for record in response:
                fields.append(Field(record))

            return APIObjectCollection(fields)
        else:
            return None


class FieldGrouping(APIObject):

    def __init__(self, grouping_api_object, owner_obj, category_obj, field_obj_list, keys_to_ignore=None):
        super().__init__(
            keys_to_ignore=keys_to_ignore if keys_to_ignore is not None else [
                'owner_id', 'is_public', 'created_at', 'updated_at', 'owner',
                'category', 'fields'
            ])

        self.id = grouping_api_object['id']
        self.label = grouping_api_object['label']
        self.slug = grouping_api_object['slug']
        self.description = grouping_api_object['description']
        self.facility_id = grouping_api_object['facility_id']
        self.owner_id = grouping_api_object['owner_id']
        self.is_public = grouping_api_object['is_public']
        self.created_at = grouping_api_object['created_at']
        self.updated_at = grouping_api_object['updated_at']
        self.field_category_id = grouping_api_object['field_category_id']
        self.owner = owner_obj
        self.category = category_obj
        self.fields = APIObjectCollection(field_obj_list)

    def get_dict(self):
        return {
            **super().get_dict(),
            'field_category_name': self.category.name if self.category else None,
            'field_count': len(self.fields)
        }


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

        self.id = field_api_object['id']
        self.label = field_api_object['label']
        self.output_id = field_api_object['output_id']
        self.field_descriptor = field_api_object['field_descriptor']
        self.field_human_name = field_api_object['field_human_name']
        self.is_hidden = field_api_object['is_hidden']
        self.status = field_api_object['status']
        self.units = field_api_object['units']


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
