from contxt.services import Service, GET, POST, APIObject, APIObjectCollection

CONFIGS_BY_ENVIRONMENT = {
    'production': {
        'base_url': 'https://bus.ndustrial.io/',
        'audience': 'T62CR77ouw4I6VPlSSlLT9VpVA1ebByx'
    },
    'staging': {
        'base_url': 'https://bus-staging.ndustrial.io/',
        'audience': 'YHCtC2dZAvvt2SdxUVwWpVdm4fSOkUdL'
    }
}


class MessageBusService(Service):

    def __init__(self, auth_module, environment='staging'):

        if environment not in CONFIGS_BY_ENVIRONMENT:
            raise Exception('Invalid environment specified')

        self.env = CONFIGS_BY_ENVIRONMENT[environment]

        super(MessageBusService, self).__init__(base_url=self.env['base_url'],
                                                access_token=auth_module.get_token_for_client(self.env['audience']))

    def get_channels(self, service_id, organization_id):

        assert isinstance(service_id, str)
        assert isinstance(organization_id, str)

        req = GET(uri='organizations/{}/services/{}/channels'.format(organization_id, service_id))
        req.api_version = None

        response = self.execute(req)

        channels = []
        for record in response:
            channels.append(Channel(record))

        return APIObjectCollection(channels)


class Channel(APIObject):

    def __init__(self, channel_api_object):

        super(Channel, self).__init__()

        self.id = channel_api_object['id']
        self.name = channel_api_object['name']
        self.organization_id = channel_api_object['organization_id']
        self.service_id = channel_api_object['service_id']
