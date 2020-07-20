from abc import ABC, abstractmethod
from os import environ
from typing import Any, Dict, Optional, Tuple

from .auth.machine import MachineAuth
from .models.contxt import Config
from .services import ContxtService


class BaseWorker(ABC):
    """Abstract base class for a worker. Overload this class to implement `do_work()`"""

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
        self.config, self.config_values = self._init_configuration()

    def _init_configuration(self) -> Tuple[Optional[Config], Dict[str, Any]]:
        if not self.environment_id:
            # No env specified, no values to fetch
            return None, {}

        # Fetch contxt config
        config = self.contxt_service.get_config_for_client(self.client_id, self.environment_id)

        # Cache values in a simple dict for easy consumption
        config_values = {v.key: v.value for v in config.config_values} if config else {}

        return config, config_values

    @abstractmethod
    def do_work(self) -> None:
        """Main method"""
