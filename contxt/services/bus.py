from typing import Dict, List

from contxt.auth import Auth
from contxt.models.bus import Channel, ChannelStats
from contxt.services.api import ApiEnvironment, ConfiguredApi
from contxt.utils import make_logger

logger = make_logger(__name__)


class MessageBusService(ConfiguredApi):
    """
    Service to interact with our Message Bus API.
    """

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
        logger.debug(f"Fetching channel {channel_id} for service {service_id}")
        resp = self.get(f"{self._channels_url(service_id)}/{channel_id}")
        return Channel.from_api(resp)

    def get_channels_for_service(self, service_id: str) -> List[Channel]:
        logger.debug(f"Fetching channels for service {service_id}")
        resp = self.get(self._channels_url(service_id))
        return [Channel.from_api(rec) for rec in resp]

    def get_schema_for_channel_and_service(
        self, schema_id: str, channel_id: str, service_id: str
    ) -> Dict:
        # TODO: create model for this response
        logger.debug(f"Fetching channel {channel_id} for service {service_id}")
        resp = self.get(f"{self._channels_url(service_id)}/{channel_id}/schemas")
        return resp

    def get_schemas_for_channel_and_service(
        self, channel_id: str, service_id: str
    ) -> List[Dict]:
        # TODO: create model for this response
        logger.debug(
            f"Fetching schemas for channel {channel_id} and service {service_id}"
        )
        resp = self.get(f"{self._channels_url(service_id)}/{channel_id}/schemas")
        return resp

    def get_stats_for_channel_and_service(
        self, channel_id: str, service_id: str
    ) -> ChannelStats:
        logger.debug(
            f"Fetching stats for channel {channel_id} and service {service_id}"
        )
        resp = self.get(f"{self._channels_url(service_id)}/{channel_id}/statistics")
        return ChannelStats.from_api(resp)
