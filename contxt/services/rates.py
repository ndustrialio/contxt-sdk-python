from typing import Dict, List, Optional, Iterable

from ..models.rates import UtilityProvider, RateSchedule
from .api import ConfiguredLegacyApi
from ..utils.config import ContxtEnvironmentConfig
from .pagination import PagedRecords, PageOptions


class UtilityRatesService(ConfiguredLegacyApi):
    """Utility Rates API client"""

    def __init__(self, env_config: ContxtEnvironmentConfig, **kwargs) -> None:
        super().__init__(env_config=env_config, **kwargs)

    def get_providers(
            self,
            page_options: Optional[PageOptions] = None
    ) -> Iterable[UtilityProvider]:
        return PagedRecords(
            api=self,
            url='providers',
            params={},
            options=page_options,
            record_parser=UtilityProvider.from_api,
            is_v2=True
        )

    def get_schedules_for_provider(
            self,
            utility_provider_id: int,
            page_options: Optional[PageOptions] = None
    ) -> Iterable[RateSchedule]:
        return PagedRecords(
            api=self,
            url='schedules',
            params={'utility_provider_id': utility_provider_id},
            options=page_options,
            record_parser=RateSchedule.from_api,
            is_v2=True
        )

    def get_schedule(self, rate_schedule_id: int) -> RateSchedule:
        resp = self.get(f'schedules/{rate_schedule_id}')
        return RateSchedule.from_api(resp)

    '''
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
    '''
