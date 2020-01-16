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


# Ref: https://docs.python.org/3/library/datetime.html#determining-if-an-object-is-aware-or-naive # noqa: E501
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
