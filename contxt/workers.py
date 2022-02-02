from abc import ABC, abstractmethod

from contxt.utils.contxt_environment import ContxtEnvironment


class BaseWorker(ABC):
    """Abstract base class for a worker. Overload this class to implement `do_work()`"""

    def __init__(
        self
    ) -> None:
        self.env = ContxtEnvironment()

    @abstractmethod
    def do_work(self) -> None:
        """Main method"""
