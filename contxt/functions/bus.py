from contxt.functions.organizations import get_organization_id_from_arguments
from contxt.services.bus import MessageBusService
from contxt.services.contxt import ContxtService
from contxt.utils import make_logger
from contxt.exceptions import (ChannelArgumentException, ChannelNotFoundException)

logger = make_logger(__name__)


class Bus:

    def __init__(self, auth_module):
        self.auth = auth_module
        self.contxt_service = ContxtService(self.auth)
        self.mb_service = MessageBusService(self.auth)

    def get_all_channels_for_service(self, service_id, organization_id=None, organization_name=None):

        organization_id = get_organization_id_from_arguments(contxt_service=self.contxt_service,
                                                             organization_id=organization_id,
                                                             organization_name=organization_name)

        return self.mb_service.get_channels(service_id, organization_id)

    def get_stats_for_channel(self, service_id, organization_id=None, organization_name=None, channel_id=None, channel_name=None):

        if channel_id is None and channel_name is None:
            raise ChannelArgumentException("Neither channel_id nor channel_name provided. One is required.")

        organization_id = get_organization_id_from_arguments(contxt_service=self.contxt_service,
                                                             organization_id=organization_id,
                                                             organization_name=organization_name)

        if channel_id is None:
            channels = self.get_all_channels_for_service(service_id, organization_id=organization_id)

            channel_id = next((channel.id for channel in channels if channel.name == channel_name), None)

            if channel_id is None:
                raise ChannelNotFoundException("Channel not found")

        return self.mb_service.get_stats(service_id, organization_id, channel_id)
