from pprint import pformat
from typing import Any, Dict, List, Optional

from contxt.models.base import BaseModel, dataclass, field
from contxt.utils.serializer import Serializer


class Printable(BaseModel):
    def __str__(self) -> str:
        d = Serializer.to_dict(self)
        return pformat(d, indent=4)


@dataclass
class PublisherStats(Printable):
    msg_rate_in: str = field(key="msgRateIn")
    producer_id: str = field(key="producerId")
    connected_since: str = field(key="connectedSince")


@dataclass
class ConsumerStats(Printable):
    msg_rate_out: float = field(key="msgRateOut")
    msg_rate_redeliver: float = field(key="msgRateRedeliver")
    unacked_messages: int = field(key="unackedMessages")
    blocked_consumer_on_unacked_msgs: bool = field(key="blockedConsumerOnUnackedMsgs")
    connected_since: str = field(key="connectedSince")


@dataclass
class SubscriberStats(Printable):
    msg_rate_out: float = field(key="msgRateOut")
    msg_rate_redeliver: float = field(key="msgRateRedeliver")
    msg_backlog: int = field(key="msgBacklog")
    blocked_subscription_on_unacked_msgs: bool = field(
        key="blockedSubscriptionOnUnackedMsgs"
    )
    unacked_messages: int = field(key="unackedMessages")
    consumers: List[ConsumerStats]
    name: Optional[str] = None


@dataclass
class Channel(Printable):
    id: str
    name: str
    organization_id: str
    service_id: str


@dataclass
class ChannelStats(Printable):
    msg_rate_in: float = field(key="msgRateIn")
    msg_rate_out: float = field(key="msgRateOut")
    msg_throughput_in: float = field(key="msgThroughputIn")
    msg_throughput_out: float = field(key="msgThroughputOut")
    avg_msg_size: float = field(key="averageMsgSize")
    storage_size: float = field(key="storageSize")
    replication: Dict[str, Any]
    deduplication_status: str = field(key="deduplicationStatus")
    publishers: List[PublisherStats]
    subscriptions: Dict[str, SubscriberStats]
