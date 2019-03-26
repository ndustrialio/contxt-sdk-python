from contxt.legacy.services import GET, APIObject, APIObjectCollection, APIObjectDict, Service

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


class Channel(APIObject):

    def __init__(self, channel_api_object):

        super().__init__()

        self.id = channel_api_object['id']
        self.name = channel_api_object['name']
        self.organization_id = channel_api_object['organization_id']
        self.service_id = channel_api_object['service_id']

    def __str__(self):
        return self.pretty_print()


class PublisherStatsCollection(APIObjectCollection):

    def __str__(self):
        return self.pretty_print()


class ChannelStats(APIObject):

    def __init__(self, channel_stats_object):

        super().__init__()

        self.msg_rate_in = channel_stats_object['msgRateIn']
        self.msg_rate_out = channel_stats_object['msgRateOut']
        self.average_msg_size = channel_stats_object['averageMsgSize']
        self.storage_size = channel_stats_object['storageSize']
        self.publishers = PublisherStatsCollection([PublisherStats(publisher) for publisher in channel_stats_object['publishers']])

        self.subscriptions = SubscriptionsDict({key: SubscriberStats(channel_stats_object['subscriptions'][key]) for key in channel_stats_object['subscriptions']})

    def __str__(self):
        return self.pretty_print()


class SubscriptionsDict(APIObjectDict):

    def __str__(self):
        return self.pretty_print()


class PublisherStats(APIObject):

    def __init__(self, publisher_stats_object):

        super().__init__()

        self.msg_rate_in = publisher_stats_object['msgRateIn']
        self.producer_id = publisher_stats_object['producerId']
        self.connected_since = publisher_stats_object['connectedSince']

    def __str__(self):
        return self.pretty_print()


class ConsumerStatsCollection(APIObjectCollection):

    def __str__(self):
        return self.pretty_print()


class SubscriberStats(APIObject):

    def __init__(self, subscriber_stats_object):

        super().__init__()

        self.msg_rate_out = subscriber_stats_object['msgRateOut']
        self.msg_rate_redeliver = subscriber_stats_object['msgRateRedeliver']
        self.msg_backlog = subscriber_stats_object['msgBacklog']
        self.blocked_subscription_on_unacked_msgs = subscriber_stats_object['blockedSubscriptionOnUnackedMsgs']
        self.unacked_messages = subscriber_stats_object['unackedMessages']

        self.consumers = ConsumerStatsCollection([ConsumerStats(consumer) for consumer in subscriber_stats_object['consumers'] ])

    def __str__(self):
        return self.pretty_print()


class ConsumerStats(APIObject):

    def __init__(self, consumer_stats_object):

        super().__init__()

        self.msg_rate_out = consumer_stats_object['msgRateOut']
        self.msg_rate_redeliver = consumer_stats_object['msgRateRedeliver']
        self.unacked_messages = consumer_stats_object['unackedMessages']
        self.blocked_consumer_on_unacked_msgs = consumer_stats_object['blockedConsumerOnUnackedMsgs']
        self.connected_since = consumer_stats_object['connectedSince']

    def __str__(self):
        return self.pretty_print()
