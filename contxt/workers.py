from abc import ABC, abstractmethod
from os import environ
from typing import Any, Optional

from contxt.auth.machine import MachineAuth
from contxt.services.contxt import ContxtService
from contxt.utils import make_logger

logger = make_logger(__name__)


class BaseWorker(ABC):
    """
    An abstract base class for a worker.

    Overload this class to implement `do_work`.
    """

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        environment_id: Optional[str] = None,
    ) -> None:
        self.client_id = client_id or environ["CLIENT_ID"]
        self.client_secret = client_secret or environ["CLIENT_SECRET"]
        self.environment_id = environment_id or environ.get("ENVIRONMENT_ID")
        self.auth = MachineAuth(self.client_id, self.client_secret)
        self.contxt_service = ContxtService(self.auth)

        # Retrieve configuration from Contxt (if one exists)
        self.config = (
            self.contxt_service.get_config_for_client(
                self.client_id, self.environment_id
            )
            if self.environment_id
            else None
        )
        self.config_values = self.config.parsed_values if self.config else {}

    @abstractmethod
    def do_work(self) -> None:
        pass

    def run(self) -> None:
        self.run_id = self.contxt_service.create_worker_run(self.client_id)["id"]
        logger.info(f"Started worker run with id {self.run_id}")
        self.do_work()
        self.contxt_service.update_worker_run(self.client_id, self.run_id)

    def add_metric(self, key: str, value: Any) -> None:
        self.contxt_service.create_metric_for_worker_run(self.run_id, key, value)
