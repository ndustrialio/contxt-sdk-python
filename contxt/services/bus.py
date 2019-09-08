from typing import List, Optional

from contxt.auth import Auth
from contxt.models.base import RawDict
from contxt.models.bus import Channel, ChannelStats
from contxt.services.api import ApiEnvironment, ConfiguredApi
from contxt.utils import make_logger

logger = make_logger(__name__)


class MessageBusService(ConfiguredApi):
    """Wrapper around our Message Bus API"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://bus.ndustrial.io",
            client_id="T62CR77ouw4I6VPlSSlLT9VpVA1ebByx",
        ),
        ApiEnvironment(
            name="staging",
            base_url="https://bus-staging.ndustrial.io",
            client_id="YHCtC2dZAvvt2SdxUVwWpVdm4fSOkUdL",
        ),
    )

    def __init__(
        self, auth: Auth, organization_id: str, env: str = "production"
    ) -> None:
        super().__init__(env=env, auth=auth)
        self.organization_id = organization_id

    def _channels_url(self, service_id: str) -> str:
        return f"organizations/{self.organization_id}/services/{service_id}/channels"

    def get_channel_for_service(self, channel_id: str, service_id: str) -> Channel:
        """Get channel `channel_id` for service `service_id`"""
        url = f"{self._channels_url(service_id)}/{channel_id}"
        resp = self.get(url)
        return Channel.from_api(resp)

    def get_channel_with_name_for_service(
        self, channel_name: str, service_id: str
    ) -> Optional[Channel]:
        """Get channel `channel_name` for service `service_id`"""
        for channel in self.get_channels_for_service(service_id):
            if channel.name.lower() == channel_name.lower():
                return channel
        logger.warning(f"Failed to find channel with name {channel_name}")
        return None

    def get_channels_for_service(self, service_id: str) -> List[Channel]:
        """Get channels for service `service_id`"""
        url = self._channels_url(service_id)
        resp = self.get(url)
        return Channel.from_api(resp, many=True)

    def get_schema_for_channel_and_service(
        self, schema_id: str, channel_id: str, service_id: str
    ) -> RawDict:
        """Get schema `schema_id` for channel `channel_id` and service `service_id`"""
        # TODO: create model for this response
        url = f"{self._channels_url(service_id)}/{channel_id}/schemas/{schema_id}"
        return self.get(url)

    def get_schemas_for_channel_and_service(
        self, channel_id: str, service_id: str
    ) -> List[RawDict]:
        """Get schemas for channel `channel_id` and service `service_id`"""
        # TODO: create model for this response
        url = f"{self._channels_url(service_id)}/{channel_id}/schemas"
        return self.get(url)

    def get_stats_for_channel_and_service(
        self, channel_id: str, service_id: str
    ) -> ChannelStats:
        """Get stats for channel `channel_id` and service `service_id`"""
        url = f"{self._channels_url(service_id)}/{channel_id}/statistics"
        resp = self.get(url)
        return ChannelStats.from_api(resp)
