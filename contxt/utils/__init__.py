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


def timed(
    func: Optional[Callable] = None, *, printer: Callable[[str], None] = print
) -> Callable:
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


# Define logger
# TODO: add loggly support
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN = range(7)
WHITE = 37

# The background is set with 40 plus the number of the color, and the foreground with 30

# These are the sequences need to get colored ouput
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[0;%dm"
BOLD_SEQ = "\033[1m"

COLORS = {"WARNING": YELLOW, "INFO": WHITE, "DEBUG": BLUE, "CRITICAL": RED, "ERROR": RED}


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
