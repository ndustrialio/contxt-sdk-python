"""General utilities"""

from datetime import datetime
from functools import partial, wraps
from logging import Logger, getLogger
from time import time
from typing import Callable, Dict, Optional


def make_logger(name: str, level: Optional[str] = None) -> Logger:
    """Get logger with name `name` and level `level`"""
    logger = getLogger(name)
    if level:
        logger.setLevel(level.upper())
    return logger


# Ref: https://docs.python.org/3/library/datetime.html#determining-if-an-object-is-aware-or-naive
def is_datetime_aware(dt: datetime) -> bool:
    """Returns if datetime `dt` is timezone-aware"""
    return dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None


def timed(func: Optional[Callable] = None, *, printer: Callable[[str], None] = print) -> Callable:
    """Decorator to print `func`'s runtime, via `printer`"""

    if func is None:
        return partial(timed, printer=printer)

    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time()
        res = func(*args, **kwargs)
        printer(f"{func.__name__}'s elapsed time: {time() - t0} s")
        return res

    return wrapper


# FIXME: does not handle nested dictionaries
def dict_diff(d1: Dict, d2: Dict) -> Dict:
    """Compute the set difference `d1` - `d2`"""

    def flatten(obj):
        if isinstance(obj, (list, tuple)):
            return tuple([flatten(o) for o in obj])
        elif isinstance(obj, dict):
            return tuple([(flatten(k), flatten(v)) for k, v in sorted(obj.items())])
        return obj

    def expand(obj):
        if isinstance(obj, (set, tuple)):
            return {k: expand(v) for k, v in obj}
        return obj

    return expand(set(flatten(d1)) - set(flatten(d2)))


# Source: https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#cachedproperty
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
