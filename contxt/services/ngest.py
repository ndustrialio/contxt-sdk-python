from copy import deepcopy
from datetime import datetime, timezone
from typing import Dict, List

from ..utils import is_datetime_aware, make_logger
from ..utils.orgs import get_slug_or_org_id
from .api import ApiEnvironment, ConfiguredApi

logger = make_logger(__name__)


class NgestService(ConfiguredApi):
    """Ngest API client"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://{tenant}.api.ndustrial.io/rest/data/v1",
            client_id="AhVAWkq2FEoQtWAP7EidZ9uzrc4ED1Dx",
        ),
    )

    def __init__(self, org_id: str, env: str = "production", **kwargs) -> None:
        self.env = env
        super().__init__(env=env, **kwargs)
        tenant = get_slug_or_org_id(org_id)
        self.base_url = self.base_url.format(tenant=tenant)

    @staticmethod
    def specialize(
        feed_key: str, feed_token: str, org_id: str, env: str = "production"
    ) -> "SpecializedNgestService":
        return SpecializedNgestService(env=env, feed_key=feed_key, feed_token=feed_token, org_id=org_id)

    def _format_time_series(self, feed_key: str, time_series: Dict[str, Dict[datetime, float]]) -> Dict:
        # Enforce all datetimes are tz-aware
        assert all(
            is_datetime_aware(dt) for time_series in time_series.values() for dt in time_series.keys()
        ), "Timezone-aware datetimes required"

        # Format for request
        return {
            "feedKey": feed_key,
            "type": "timeseries",
            "data": [
                {
                    "timestamp": dt.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
                    "data": {field_descriptor: {"value": str(value)}},
                }
                for field_descriptor, series in time_series.items()
                for dt, value in series.items()
            ],
        }

    def send_time_series(
        self,
        feed_key: str,
        feed_token: str,
        time_series: Dict[str, Dict[datetime, float]],
        per_request: int = 50,
    ) -> List[Dict]:
        """Sends time series data for field(s).

        :param feed_key: feed's key
        :type feed_key: str
        :param feed_token: feed's token
        :type feed_token: str
        :param time_series: dictionary of field descriptors to a time series dictionary
        :type time_series: Dict[str, Dict[datetime, float]]
        :param per_request: number of datapoints to send per request, defaults to 50
        :type per_request: int, optional
        :return: responses
        :rtype: List[Dict]
        """
        # Prepare data for request
        data = self._format_time_series(feed_key=feed_key, time_series=time_series)

        # Send the time series in chunks, partitioned by `per_request`
        responses = []
        while data["data"]:
            # Create chunk for next request
            chunk = deepcopy(data)
            chunk["data"] = data["data"][:per_request]

            # Make request
            response = self.post(f"{feed_token}/ngest/{feed_key}", json=chunk)
            if response["status"] != "ok":
                logger.warning(f"{self.__class__.__name__}: got status {response['status']}")
            responses.append(response)

            # Update remaining data
            data["data"] = data["data"][per_request:]

        return responses


class SpecializedNgestService(NgestService):
    def __init__(self, feed_key: str, feed_token: str, org_id: str, env: str = "production") -> None:
        super().__init__(env=env, org_id=org_id)
        self.feed_key = feed_key
        self.feed_token = feed_token

    def send_time_series(  # type: ignore
        self, time_series: Dict[str, Dict[datetime, float]], per_request: int = 50
    ) -> List[Dict]:
        return super().send_time_series(
            feed_key=self.feed_key,
            feed_token=self.feed_token,
            time_series=time_series,
            per_request=per_request,
        )
