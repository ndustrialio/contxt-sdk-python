import csv
import json
import logging
from contextlib import closing
from typing import TextIO

import websocket
from requests.exceptions import HTTPError

from contxt.message_bus import MessageBus
from contxt.services.api import Api

from .auth.machine import MachineAuth

logger = logging.getLogger()


class DlqConsumer:
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        base_socket_url: str,
        org_id: str,
        etl_mgmt_api_base_url: str,
        etl_mgmt_api_client_id: str,
        channel: str,
        subscription_name: str,
        acknowledge: bool,
        receive_timeout=5,
    ) -> None:
        self.auth = MachineAuth(client_id, client_secret)
        self.base_socket_url = base_socket_url
        self.org_id = org_id
        self.etl_mgmt_api_base_url = etl_mgmt_api_base_url
        self.etl_mgmt_api_client_id = etl_mgmt_api_client_id
        self.channel = channel
        self.subscription_name = subscription_name
        self.acknowledge = acknowledge
        self.receive_timeout = receive_timeout

    def pullData(self, dst: TextIO, fields, headers=True, limit=0):
        bearer_token = self.auth.get_token_provider(self.etl_mgmt_api_client_id).access_token

        channelAuthApi = Api(self.etl_mgmt_api_base_url)
        channel_token_resp = channelAuthApi.raw_post(
            "channels/authorizations",
            headers={"Authorization": "Bearer " + bearer_token},
            json={"resources": [{"resource": self.channel, "actions": ["subscribe"]}]},
        )
        try:
            # Raise any error
            channel_token_resp.raise_for_status()
        except HTTPError:
            # Catch the error, to log the response's message, and reraise
            # Try to decode the response as json, else fall back to raw text
            response_json = channel_token_resp.json()
            msg = response_json.get("message") or response_json or channel_token_resp.text
            logger.debug(f"HTTP Error: {channel_token_resp.reason} - {msg}")
            raise

        socketURL = self.base_socket_url + "/organizations/" + self.org_id + "/stream"

        logger.debug(f"connecting to {socketURL}")
        websocket.enableTrace(logger.level <= 10)
        # connect to message bus websocket
        with closing(
            websocket.create_connection(socketURL, header={"Authorization": "Bearer " + bearer_token})
        ) as ws:

            logger.info("connected to message bus")
            ws.settimeout(self.receive_timeout)

            mb = MessageBus(ws)
            if not mb.authorize(channel_token_resp.text):
                return
            if not mb.subscribe(self.etl_mgmt_api_client_id, self.channel, self.subscription_name):
                return

            # set timeout for receiving in order to detect end of stream
            ws.settimeout(self.receive_timeout)

            logger.info("streaming DLQ data")

            queue_message = None
            if fields is None or len(fields) == 0:
                # infer the fields from the first message
                logger.debug("waiting for DLQ row from message bus")
                try:
                    queue_message = json.loads(ws.recv())
                except websocket.WebSocketTimeoutException:
                    logger.info("timeout waiting for first DLQ row from message bus. Closing connection")
                    # end of queue if timeout received?
                    return

                if (
                    queue_message is not None
                    and "result" in queue_message
                    and "body" in queue_message["result"]
                ):
                    fields = queue_message["result"]["body"].keys()
                else:
                    logger.error("unable to determine columns from first message")
                    return

            writer = csv.DictWriter(dst, fieldnames=fields)
            if headers:
                writer.writeheader()
            count = 0

            if queue_message is not None and "result" in queue_message:
                # logger.debug
                print(f"writing DLQ message {queue_message['result']['id']}")
                writer.writerow(queue_message["result"]["body"])
                count += 1

                if self.acknowledge:
                    # logger.debug
                    print(f"acknowledging DLQ message {queue_message['id']}")
                    mb.acknowledge(queue_message["id"])

            while limit == 0 or count < limit:
                queue_message = None
                logger.debug("waiting for DLQ message from message bus")
                try:
                    queue_message = json.loads(ws.recv())
                except websocket.WebSocketTimeoutException:
                    logger.info(
                        "timeout waiting for next DLQ message from message bus. Closing connection"
                    )
                    # end of queue if timeout received?
                    break

                if queue_message is not None and "result" in queue_message:
                    logger.debug(f"writing DLQ message {queue_message['id']}")
                    writer.writerow(queue_message["result"]["body"])
                    count += 1

                    if self.acknowledge:
                        logger.debug(f"acknowledging DLQ message {queue_message['id']}")
                        mb.acknowledge(queue_message["id"])
