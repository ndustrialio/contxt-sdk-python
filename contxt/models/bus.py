from pprint import pformat
from typing import Any, Dict, List, Optional, Set, Tuple, Union

from contxt.services.api import ApiField, ApiObject
from contxt.utils.serializer import Serializer


def pretty_print(obj):
    d = Serializer.to_dict(obj)
    return pformat(d, indent=4)


class PublisherStats(ApiObject):
    _api_fields = (
        ApiField("msgRateIn", attr_key="msg_rate_in"),
        ApiField("producerId", attr_key="producer_id"),
        ApiField("connectedSince", attr_key="connected_since"),
    )

    def __init__(
            self,
            msg_rate_in: str,
            producer_id: str,
            connected_since: str,
    ):
        super().__init__()
        self.msg_rate_in = msg_rate_in
        self.producer_id = producer_id
        self.connected_since = connected_since

    def __str__(self):
        return pretty_print(self)


class ConsumerStats(ApiObject):
    _api_fields = (
        ApiField("msgRateOut", attr_key="msg_rate_out", type=float),
        ApiField("msgRateRedeliver", attr_key="msg_rate_redeliver", type=float),
        ApiField("unackedMessages", attr_key="unacked_messages", type=int),
        ApiField("blockedConsumerOnUnackedMsgs", attr_key="blocked_consumer_on_unacked_msgs", type=bool),
        ApiField("connectedSince", attr_key="connected_since"),
    )

    def __init__(
            self,
            msg_rate_out: float,
            msg_rate_redeliver: float,
            unacked_messages: int,
            blocked_consumer_on_unacked_msgs: bool,
            connected_since: str,
    ):
        super().__init__()
        self.msg_rate_out = msg_rate_out
        self.msg_rate_redeliver = msg_rate_redeliver
        self.unacked_messages = unacked_messages
        self.blocked_consumer_on_unacked_msgs = blocked_consumer_on_unacked_msgs
        self.connected_since = connected_since

    def __str__(self):
        return pretty_print(self)


class SubscriberStats(ApiObject):
    _api_fields = (
        ApiField("name", optional=True),
        ApiField("msgRateOut", attr_key="msg_rate_out", type=float),
        ApiField("msgRateRedeliver", attr_key="msg_rate_redeliver", type=float),
        ApiField("msgBacklog", attr_key="msg_backlog", type=int),
        ApiField("blockedSubscriptionOnUnackedMsgs", attr_key="blocked_subscription_on_unacked_msgs", type=bool),
        ApiField("unackedMessages", attr_key="unacked_messages", type=int),
        ApiField("consumers", type=ConsumerStats)
    )

    def __init__(
            self,
            msg_rate_out: float,
            msg_rate_redeliver: float,
            msg_backlog: int,
            blocked_subscription_on_unacked_msgs: bool,
            unacked_messages: int,
            consumers: List[ConsumerStats],
            name: Optional[str] = None
    ):
        super().__init__()
        self.name = name
        self.msg_rate_out = msg_rate_out
        self.msg_rate_redeliver = msg_rate_redeliver
        self.msg_backlog = msg_backlog
        self.blocked_subscription_on_unacked_msgs = blocked_subscription_on_unacked_msgs
        self.unacked_messages = unacked_messages
        self.consumers = consumers

    def __str__(self):
        return pretty_print(self)


class Channel(ApiObject):
    _api_fields = (
        ApiField("id"),
        ApiField("name"),
        ApiField("organization_id"),
        ApiField("service_id"),
    )

    def __init__(
            self,
            id: str,
            name: str,
            organization_id: str,
            service_id: str,
    ):
        super().__init__()
        self.id = id
        self.name = name
        self.organization_id = organization_id
        self.service_id = service_id

    def __str__(self):
        return pretty_print(self)


class ChannelStats(ApiObject):
    _api_fields = (
        ApiField("msgRateIn", attr_key="msg_rate_in", type=float),
        ApiField("msgRateOut", attr_key="msg_rate_out", type=float),
        ApiField("msgThroughputIn", attr_key="msg_throughput_in", type=float),
        ApiField("msgThroughputOut", attr_key="msg_throughput_out", type=float),
        ApiField("averageMsgSize", attr_key="avg_msg_size", type=float),
        ApiField("storageSize", attr_key="storage_size", type=float),
        ApiField("replication", type=dict),
        ApiField("deduplicationStatus", attr_key="deduplication_status"),
        ApiField("publishers", type=PublisherStats),
        ApiField("subscriptions", type=lambda o: [SubscriberStats.from_api({**v, "name": k}) for k, v in o.items()]),
    )

    def __init__(
            self,
            msg_rate_in: float,
            msg_rate_out: float,
            msg_throughput_in: float,
            msg_throughput_out: float,
            avg_msg_size: float,
            storage_size: float,
            replication: Any,
            deduplication_status: str,
            publishers: List[PublisherStats],
            subscriptions: List[SubscriberStats],
    ):
        super().__init__()
        self.msg_rate_in = msg_rate_in
        self.msg_rate_out = msg_rate_out
        self.msg_throughput_in = msg_throughput_in
        self.msg_throughput_out = msg_throughput_out
        self.avg_msg_size = avg_msg_size
        self.storage_size = storage_size
        self.replication = replication
        self.deduplication_status = deduplication_status
        self.publishers = publishers
        self.subscriptions = subscriptions

    def __str__(self):
        return pretty_print(self)
