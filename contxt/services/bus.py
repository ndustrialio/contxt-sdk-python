from typing import Dict, List, Optional

from ..auth import Auth
from ..models.bus import Channel, ChannelStats
from .api import ConfiguredApi


class MessageBusService(ConfiguredApi):
    """Message Bus API client"""

    _envs = ()

    def __init__(self, auth: Auth, organization_id: str, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, auth=auth, **kwargs)
        self.organization_id = organization_id

    def _channels_url(self, service_id: str) -> str:
        return f"organizations/{self.organization_id}/services/{service_id}/channels"

    def get_channel_for_service(self, channel_id: str, service_id: str) -> Channel:
        resp = self.get(f"{self._channels_url(service_id)}/{channel_id}")
        return Channel.from_api(resp)

    def create_channel_for_service(self, channel: Channel) -> Channel:
        data = {"name": channel.name}
        resp = self.post(f"{self._channels_url(channel.service_id)}", json=data)
        return Channel.from_api(resp)

    def get_channel_with_name_for_service(self, channel_name: str, service_id: str) -> Optional[Channel]:
        for channel in self.get_channels_for_service(service_id):
            if channel.name.lower() == channel_name.lower():
                return channel
        return None

    def get_channels_for_service(self, service_id: str) -> List[Channel]:
        resp = self.get(self._channels_url(service_id))
        return [Channel.from_api(rec) for rec in resp]

    def get_schema_for_channel_and_service(
        self, schema_id: str, channel_id: str, service_id: str
    ) -> Dict:
        # TODO: create model for this response
        return self.get(f"{self._channels_url(service_id)}/{channel_id}/schemas")

    def get_schemas_for_channel_and_service(self, channel_id: str, service_id: str) -> List[Dict]:
        # TODO: create model for this response
        return self.get(f"{self._channels_url(service_id)}/{channel_id}/schemas")  # type: ignore

    def get_stats_for_channel_and_service(self, channel_id: str, service_id: str) -> ChannelStats:
        resp = self.get(f"{self._channels_url(service_id)}/{channel_id}/statistics")
        return ChannelStats.from_api(resp)

    def peek_messages_for_subscription_and_channel_and_service(
        self, subscription: str, channel_id: str, service_id: str
    ) -> Dict:
        return self.get(f"{self._channels_url(service_id)}/{channel_id}/peek/{subscription}")
