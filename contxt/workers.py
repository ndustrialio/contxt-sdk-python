from abc import ABC, abstractmethod
from typing import List

from .auth.machine import MachineAuth
from .utils.config import ContxtEnvironmentConfig


class BaseWorker(ABC):
    """Abstract base class for a worker. Overload this class to implement `do_work()`"""

    def __init__(
        self,
        env_configs: List[ContxtEnvironmentConfig],
    ) -> None:
        self.env_configs = env_configs
        # possibly removing this since there can be multiple configs
        #self.auth = MachineAuth(self.env_config)

    @abstractmethod
    def do_work(self) -> None:
        """Main method"""
