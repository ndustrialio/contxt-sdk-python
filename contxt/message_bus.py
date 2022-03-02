import json
import logging
import uuid
from typing import Dict

import websocket

logger = logging.getLogger()


class MessageBus:
    def __init__(self, ws: websocket.WebSocket) -> None:
        self.ws = ws
        self.acks: Dict[uuid.UUID, str] = {}

    def authorize(self, token: str):
        logger.debug("sending authorization to message bus")
        self.ws.send(
            json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "MessageBus.Authorize",
                    "params": {"token": token},
                    "id": str(uuid.uuid4()),
                }
            )
        )

        # receive data
        logger.debug("waiting for message bus authorization response")
        try:
            response = json.loads(self.ws.recv())
        except websocket.WebSocketTimeoutException:
            logger.warn("Timeout waiting for message bus authorization response")
            return False
        except Exception as e:
            logger.error("Error waiting for authorization response", e)
            return False
        logger.debug(f"message bus authorization response ${response}")
        return True

    def subscribe(self, service_client_id: str, channel: str, group: str):
        subscription_id = str(uuid.uuid4())
        logger.debug(f"sending channel {channel} subscription to message bus")
        self.ws.send(
            json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "MessageBus.Subscribe",
                    "params": {
                        "service_id": service_client_id,
                        "channel": channel,
                        "group": group,
                    },
                    "id": subscription_id,
                }
            )
        )

        logger.debug(f"waiting for channel {channel} subscription response")
        try:
            response = json.loads(self.ws.recv())
        except websocket.WebSocketTimeoutException:
            logger.warn(f"Timeout waiting for channel {channel} subscription response")
            return None
        except Exception as e:
            logger.error(f"Error waiting for channel {channel} subscription response", e)
            return None
        logger.debug(f"channel {channel} subscription response: {response}")
        return response["result"]["subscription"]

    def acknowledge(self, msg_id: str):
        ackId = uuid.uuid4()
        self.acks[ackId] = msg_id
        self.ws.send(
            json.dumps(
                {
                    "jsonrpc": "2.0",
                    "method": "MessageBus.Acknowledge",
                    "params": {"message_id": msg_id},
                    "id": str(ackId),
                }
            )
        )

    def recv(self, subscription_id):
        receipt = json.loads(self.ws.recv())
        while "id" in receipt and receipt["id"] != subscription_id:
            if uuid.UUID(receipt["id"]) in self.acks:
                logger.debug(f"removing ack {receipt['id']}")
                if "error" in receipt:
                    logger.warn(
                        f"Error received from acknowledgement of message {self.acks[receipt['id']]}",
                        receipt["error"],
                    )
                self.acks.remove(receipt["id"])
            receipt = json.loads(self.ws.recv())

        return receipt
