from typing import Dict, List, Optional, Set, Tuple

from contxt.auth import BaseAuth
from contxt.models.bus import Channel, ChannelStats
from contxt.services.api import ApiServiceConfig, ConfiguredApiService
from contxt.utils import make_logger

logger = make_logger(__name__)


class MessageBusService(ConfiguredApiService):
    """
    Service to interact with our Message Bus API.
    """
    _configs = (
        ApiServiceConfig(
            name="production",
            base_url="https://bus.ndustrial.io",
            # base_url="http://bus.lineageapi.com/",
            audience="T62CR77ouw4I6VPlSSlLT9VpVA1ebByx"),
        ApiServiceConfig(
            name="staging",
            base_url="https://bus-staging.ndustrial.io",
            audience="YHCtC2dZAvvt2SdxUVwWpVdm4fSOkUdL"),
    )

    def __init__(
            self,
            auth: BaseAuth,
            organization_id: str,
            env: Optional[str] = "production",
    ):
        super().__init__(auth, env, api_version=None)
        self.organization_id = organization_id

    def _channels_url(self, service_id):
        return f"organizations/{self.organization_id}/services/{service_id}/channels"

    def get_channel_for_service(self, channel_id: str, service_id: str):
        logger.debug(f"Fetching channel {channel_id} for service {service_id}")
        resp = self.get(f"{self._channels_url(service_id)}/{channel_id}")
        return Channel.from_api(resp)

    def get_channels_for_service(self, service_id: str):
        logger.debug(f"Fetching channels for service {service_id}")
        resp = self.get(self._channels_url(service_id))
        return [Channel.from_api(rec) for rec in resp]

    def get_schema_for_channel_and_service(self, schema_id: str, channel_id: str, service_id: str):
        logger.debug(f"Fetching channel {channel_id} for service {service_id}")
        resp = self.get(
            f"{self._channels_url(service_id)}/{channel_id}/schemas")
        return resp

    def get_schemas_for_channel_and_service(self, channel_id: str, service_id: str):
        logger.debug(
            f"Fetching schemas for channel {channel_id} and service {service_id}"
        )
        resp = self.get(
            f"{self._channels_url(service_id)}/{channel_id}/schemas")
        return resp

    def get_stats_for_channel_and_service(self, channel_id: str, service_id: str):
        logger.debug(
            f"Fetching stats for channel {channel_id} and service {service_id}"
        )
        resp = self.get(
            f"{self._channels_url(service_id)}/{channel_id}/statistics")
        return ChannelStats.from_api(resp)
