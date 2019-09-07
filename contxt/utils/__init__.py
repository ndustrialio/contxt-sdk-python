import logging
from datetime import datetime
from time import time
from typing import Dict, Optional, Set

logger = logging.getLogger(__name__)


def make_logger(name: str, level: Optional[str] = None) -> logging.Logger:
    logger = logging.getLogger(name)
    if level:
        logger.setLevel(level.upper())
    return logger


def timed(func):
    def wrapper(*args, **kwargs):
        t0 = time()
        return_val = func(*args, **kwargs)
        logger.info(f"{func.__name__}'s elapsed time: {time() - t0} s")
        return return_val

    return wrapper


def is_datetime_aware(dt: datetime) -> bool:
    return dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None


class Timer:
    def __enter__(self) -> "Timer":
        self.start = time()
        return self

    def __exit__(self, *args) -> None:
        self.stop = time()
        self.elapsed = self.stop - self.start


class Utils:
    @staticmethod
    def dict_to_set(dict_: Dict) -> Set:
        # TODO: this does not handle nested dicts

        def flatten(obj):
            if isinstance(obj, (list, tuple)):
                return tuple([flatten(o) for o in obj])
            elif isinstance(obj, dict):
                return tuple([(flatten(k), flatten(v)) for k, v in sorted(obj.items())])
            return obj

        return set(flatten(dict_))

    @staticmethod
    def set_to_dict(set_: Set) -> Dict:
        def expand(obj):
            if isinstance(obj, (set, tuple)):
                return {k: expand(v) for k, v in obj}
            return obj

        return expand(set_)
