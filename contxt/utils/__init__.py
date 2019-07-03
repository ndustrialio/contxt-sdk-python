import logging
from datetime import datetime
from os import environ
from sys import stdout
from time import time
from typing import Dict, Optional, Set

from pytz import UTC
from tzlocal import get_localzone


def make_logger(name: str, level: Optional[str] = None):
    logger = logging.getLogger(name)
    if level:
        logger.setLevel(level.upper())
    return logger


def timed(func):
    def wrapper(*args, **kwargs):
        t0 = time()
        return_val = func(*args, **kwargs)
        print(f"{func.__name__}'s elapsed time: {time() - t0} s")
        return return_val

    return wrapper


def is_datetime_aware(dt: datetime) -> bool:
    return dt.tzinfo is not None and dt.tzinfo.utcoffset(dt) is not None


class Utils:
    @staticmethod
    def delocalize_datetime(dt: datetime) -> datetime:
        localized_dt = get_localzone().localize(dt)
        return localized_dt.astimezone(UTC)

    @staticmethod
    def get_epoch_time(dt: datetime) -> int:
        if dt.tzinfo is None:
            # assuming an naive datetime is in the callers timezone
            # as set on the system,
            dt = get_localzone().localize(dt)

        utc_1970 = datetime(1970, 1, 1).replace(tzinfo=UTC)

        return int((dt.astimezone(UTC) - utc_1970).total_seconds())

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


# Define logger
# TODO: add loggly support
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN = range(7)
WHITE = 37

# The background is set with 40 plus the number of the color, and the foreground with 30

# These are the sequences need to get colored ouput
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[0;%dm"
BOLD_SEQ = "\033[1m"

COLORS = {
    "WARNING": YELLOW,
    "INFO": WHITE,
    "DEBUG": BLUE,
    "CRITICAL": RED,
    "ERROR": RED,
}


def formatter_message(message, use_color=True):
    if use_color:
        message = message.replace("$RESET", RESET_SEQ).replace("$BOLD", BOLD_SEQ)
    else:
        message = message.replace("$RESET", "").replace("$BOLD", "")
    return message


class ColoredFormatter(logging.Formatter):
    def __init__(self, msg: str, use_color: bool = True) -> None:
        super().__init__(msg)
        self.use_color = use_color

    def format(self, record):
        level_color = COLOR_SEQ % (30 + COLORS[record.levelname])
        log = super().format(record).replace("$COLOR", level_color)
        return log


# Custom logger class with multiple destinations
class ColoredLogger(logging.Logger):
    FORMAT = (
        "$COLOR%(asctime)s $BOLD$COLOR%(levelname)-8s$RESET$COLOR [%(name)s]"
        "  %(message)s (%(filename)s:%(lineno)d)$RESET "
    )
    COLOR_FORMAT = formatter_message(FORMAT, use_color=True)
    DEFAULT_LEVEL = environ.get("LOG_LEVEL", logging.INFO)

    def __init__(self, name: str) -> None:
        super().__init__(name, level=self.DEFAULT_LEVEL)
        color_formatter = ColoredFormatter(self.COLOR_FORMAT)
        console = logging.StreamHandler(stream=stdout)
        console.setFormatter(color_formatter)
        self.addHandler(console)
