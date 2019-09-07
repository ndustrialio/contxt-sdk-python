import logging
from datetime import datetime
from time import time
from typing import Any, Callable, Dict, Optional, Set

logger = logging.getLogger(__name__)


def make_logger(name: str, level: Optional[str] = None) -> logging.Logger:
    """Get logger with `name`, and optionally set `level`"""
    logger = logging.getLogger(name)
    if level:
        logger.setLevel(level.upper())
    return logger


def is_datetime_aware(dt: datetime) -> bool:
    """Returns if datetime `dt` is timezone-aware"""
    return dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None


def dict_to_set(d: Dict) -> Set:
    """Flattens dictionary `d` to a set."""

    def flatten(obj: Any) -> Any:
        if isinstance(obj, (list, tuple)):
            return tuple([flatten(o) for o in obj])
        elif isinstance(obj, dict):
            return tuple([(flatten(k), flatten(v)) for k, v in sorted(obj.items())])
        return obj

    return set(flatten(d))


def set_to_dict(s: Set) -> Dict:
    """Expands set `s` to a dictionary"""

    def expand(obj: Any) -> Any:
        if isinstance(obj, (set, tuple)):
            return {k: expand(v) for k, v in obj}
        return obj

    return expand(s)


def dict_diff(d1: Dict, d2: Dict) -> Dict:
    """Compute the set difference `d1` - `d2`"""
    # FIXME: does not handle nested dictionaries
    return set_to_dict(dict_to_set(d1) - dict_to_set(d2))


def timed(func: Callable) -> Callable:
    """Decorator to time `func`'s evaluation time"""

    def _timed(*args, **kwargs) -> Any:
        t0 = time()
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__}'s elapsed time: {time() - t0} s")
        return result

    return _timed


# Source: https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#cachedproperty # noqa: E501
class cachedproperty(object):
    """The ``cachedproperty`` is used similar to :class:`property`, except
    that the wrapped method is only called once. This is commonly used
    to implement lazy attributes.

    After the property has been accessed, the value is stored on the
    instance itself, using the same name as the cachedproperty. This
    allows the cache to be cleared with :func:`delattr`, or through
    manipulating the object's ``__dict__``.
    """

    def __init__(self, func):
        self.__doc__ = getattr(func, "__doc__")
        self.__isabstractmethod__ = getattr(func, "__isabstractmethod__", False)
        self.func = func

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value

    def __repr__(self):
        return f"<{self.__class__.__name__} func={self.func}>"


class Timer:
    """Context manager to measure elapsed time"""

    def __enter__(self) -> "Timer":
        self.start = time()
        return self

    def __exit__(self, *args) -> None:
        self.stop = time()
        self.elapsed = self.stop - self.start
