import logging
import sys
from datetime import datetime
from os import environ

import pytz
from tzlocal import get_localzone


def make_logger(name, level=None):
    logger = logging.getLogger(name)
    if level:
        logger.setLevel(level.upper())
    return logger


class Utils:
    __marker = object()

    @staticmethod
    def get_environ_var(var, default=__marker):
        if var not in environ:
            if default is Utils.__marker:
                raise EnvironmentError(
                    f'Variable {var} is missing from the environment')
            return default
        return environ[var]

    @staticmethod
    def delocalize_datetime(dt_object):
        localized_dt = get_localzone().localize(dt_object)
        return localized_dt.astimezone(pytz.utc)

    @staticmethod
    def get_epoch_time(dt_object):
        if dt_object.tzinfo is None:
            # assuming an naive datetime is in the callers timezone
            # as set on the system,
            dt_object = get_localzone().localize(dt_object)

        utc_1970 = datetime(1970, 1, 1).replace(tzinfo=pytz.utc)

        return int((dt_object.astimezone(pytz.utc) - utc_1970).total_seconds())

    @staticmethod
    def dict_to_set(dict_):
        # TODO: this does not handle nested dicts

        def flatten(obj):
            if isinstance(obj, (list, tuple)):
                return tuple([flatten(o) for o in obj])
            elif isinstance(obj, dict):
                return tuple([(flatten(k), flatten(v)) for k, v in sorted(obj.items())])
            return obj

        return set(flatten(dict_))

    @staticmethod
    def set_to_dict(set_):

        def expand(obj):
            if isinstance(obj, (set, tuple)):
                return {k: expand(v) for k, v in obj}
            return obj

        return expand(set_)


class Envs:
    staging = '4a9cfc2b-2580-4d01-8e67-0ea176296746'
    production = 'production'


class Config:
    ENV = Utils.get_environ_var('WORKER_ENV', Envs.staging)     # TODO: no longer used
    AUTH_AUDIENCE_ID = '75wT048QcpE7ujwBJPPjr263eTHl4gEX'
    CLI_CLIENT_ID = 'bleED0RUwb7CJ9j7D48tqSiSZRZn29AV'
    CLI_CLIENT_SECRET = '0s8VNQ26QrteS3H5KXIIPvkDcNL5PfT-_pWwAVNI4MpDaDg86O2XUH8lT19KLNiZ'


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
    'WARNING': YELLOW,
    'INFO': WHITE,
    'DEBUG': BLUE,
    'CRITICAL': RED,
    'ERROR': RED
}


def formatter_message(message, use_color=True):
    if use_color:
        message = message.replace("$RESET", RESET_SEQ).replace(
            "$BOLD", BOLD_SEQ)
    else:
        message = message.replace("$RESET", "").replace("$BOLD", "")
    return message


class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, use_color=True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        level_color = COLOR_SEQ % (30 + COLORS[record.levelname])
        log = logging.Formatter.format(self, record).replace('$COLOR', level_color)
        return log


# Custom logger class with multiple destinations
class ColoredLogger(logging.Logger):
    FORMAT = "$COLOR%(asctime)s $BOLD$COLOR%(levelname)-8s$RESET$COLOR [%(name)s]  %(message)s (%(filename)s:%(" \
             "lineno)d)$RESET "
    COLOR_FORMAT = formatter_message(FORMAT, True)

    def __init__(self, name):
        logging.Logger.__init__(self, name, logging.INFO)

        color_formatter = ColoredFormatter(self.COLOR_FORMAT)

        console = logging.StreamHandler(stream=sys.stdout)
        console.setFormatter(color_formatter)

        self.addHandler(console)


if environ.get('WORKER_ENV') is not [Envs.production]:
    logging.setLoggerClass(ColoredLogger)
else:
    logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(name)s]  %(message)s (%(filename)s:%(lineno)d)",
                        stream=sys.stdout, level=logging.INFO)
