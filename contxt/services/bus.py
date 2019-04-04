from contxt.legacy.services import (GET, APIObject, APIObjectCollection,
                                    APIObjectDict, Service)
from contxt.models.bus import Channel, ChannelStats

CONFIGS_BY_ENVIRONMENT = {
    'production': {
        'base_url': 'https://bus.ndustrial.io/',
        'audience': 'T62CR77ouw4I6VPlSSlLT9VpVA1ebByx'
    },
    'staging': {
        'base_url': 'https://bus-staging.ndustrial.io/',
        'audience': 'YHCtC2dZAvvt2SdxUVwWpVdm4fSOkUdL'
    },
}


class MessageBusService(Service):

    def __init__(self, auth_module, environment='staging'):

        if environment not in CONFIGS_BY_ENVIRONMENT:
            raise Exception('Invalid environment specified')

        self.env = CONFIGS_BY_ENVIRONMENT[environment]

        super().__init__(
            base_url=self.env['base_url'],
            access_token=auth_module.get_token_for_audience(
                self.env['audience']))

    def get_channels(self, service_id: str, organization_id: str):

        req = GET(uri=f'organizations/{organization_id}/services/{service_id}/channels')
        req.api_version = None

        response = self.execute(req)

        channels = [Channel(record) for record in response]

        return APIObjectCollection(channels)

    def get_stats(self, service_id: str, organization_id: str, channel_id: str):

        req = GET(uri=f'organizations/{organization_id}/services/{service_id}/channels/{channel_id}/statistics')
        req.api_version = None

        response = self.execute(req)

        return ChannelStats(response)
