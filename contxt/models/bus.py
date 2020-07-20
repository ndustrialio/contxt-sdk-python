from dataclasses import dataclass
from pprint import pformat
from typing import Any, ClassVar, List, Optional

from ..utils.serializer import Serializer
from . import ApiField, ApiObject


def pretty_print(obj: Any) -> str:
    d = Serializer.to_dict(obj)
    return pformat(d, indent=4)


@dataclass
class PublisherStats(ApiObject):
    _api_fields: ClassVar = (
        ApiField("msgRateIn", attr_key="msg_rate_in"),
        ApiField("producerId", attr_key="producer_id"),
        ApiField("connectedSince", attr_key="connected_since"),
    )

    msg_rate_in: str
    producer_id: str
    connected_since: str

    def __str__(self) -> str:
        return pretty_print(self)


@dataclass
class ConsumerStats(ApiObject):
    _api_fields: ClassVar = (
        ApiField("msgRateOut", attr_key="msg_rate_out", data_type=float),
        ApiField("msgRateRedeliver", attr_key="msg_rate_redeliver", data_type=float),
        ApiField("unackedMessages", attr_key="unacked_messages", data_type=int),
        ApiField(
            "blockedConsumerOnUnackedMsgs", attr_key="blocked_consumer_on_unacked_msgs", data_type=bool
        ),
        ApiField("connectedSince", attr_key="connected_since"),
    )

    msg_rate_out: float
    msg_rate_redeliver: float
    unacked_messages: int
    blocked_consumer_on_unacked_msgs: bool
    connected_since: str

    def __str__(self) -> str:
        return pretty_print(self)


@dataclass
class SubscriberStats(ApiObject):
    _api_fields: ClassVar = (
        ApiField("name", optional=True),
        ApiField("msgRateOut", attr_key="msg_rate_out", data_type=float),
        ApiField("msgRateRedeliver", attr_key="msg_rate_redeliver", data_type=float),
        ApiField("msgBacklog", attr_key="msg_backlog", data_type=int),
        ApiField(
            "blockedSubscriptionOnUnackedMsgs",
            attr_key="blocked_subscription_on_unacked_msgs",
            data_type=bool,
        ),
        ApiField("unackedMessages", attr_key="unacked_messages", data_type=int),
        ApiField("consumers", data_type=ConsumerStats),
    )

    msg_rate_out: float
    msg_rate_redeliver: float
    msg_backlog: int
    blocked_subscription_on_unacked_msgs: bool
    unacked_messages: int
    consumers: List[ConsumerStats]
    name: Optional[str] = None

    def __str__(self) -> str:
        return pretty_print(self)


@dataclass
class Channel(ApiObject):
    _api_fields: ClassVar = (
        ApiField("id"),
        ApiField("name"),
        ApiField("organization_id"),
        ApiField("service_id"),
    )

    id: str
    name: str
    organization_id: str
    service_id: str

    def __str__(self) -> str:
        return pretty_print(self)


@dataclass
class ChannelStats(ApiObject):
    _api_fields: ClassVar = (
        ApiField("msgRateIn", attr_key="msg_rate_in", data_type=float),
        ApiField("msgRateOut", attr_key="msg_rate_out", data_type=float),
        ApiField("msgThroughputIn", attr_key="msg_throughput_in", data_type=float),
        ApiField("msgThroughputOut", attr_key="msg_throughput_out", data_type=float),
        ApiField("averageMsgSize", attr_key="avg_msg_size", data_type=float),
        ApiField("storageSize", attr_key="storage_size", data_type=float),
        ApiField("replication", data_type=dict),
        ApiField("deduplicationStatus", attr_key="deduplication_status"),
        ApiField("publishers", data_type=PublisherStats),
        ApiField(
            "subscriptions",
            data_type=lambda o: [SubscriberStats.from_api({**v, "name": k}) for k, v in o.items()],
        ),
    )

    msg_rate_in: float
    msg_rate_out: float
    msg_throughput_in: float
    msg_throughput_out: float
    avg_msg_size: float
    storage_size: float
    replication: dict
    deduplication_status: str
    publishers: List[PublisherStats]
    subscriptions: List[SubscriberStats]

    def __str__(self) -> str:
        return pretty_print(self)
