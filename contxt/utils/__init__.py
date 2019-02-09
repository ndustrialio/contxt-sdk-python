from os import environ

import logging
import os
import sys

# TODO: it would be nice if our python library had a default logger (to
# encourage use in other python projects)

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


def get_environ_var(var, default=None):
    if var not in environ:
        if default is None:
            raise EnvironmentError("Variable {} is not present in the environment, "
                                   "and no default value has been provided".format(var))
        return default
    return environ[var]

def formatter_message(message, use_color=True):
    if use_color:
        message = message.replace("$RESET", RESET_SEQ).replace("$BOLD", BOLD_SEQ)
    else:
        message = message.replace("$RESET", "").replace("$BOLD", "")
    return message


class Environments(object):
    staging = '4a9cfc2b-2580-4d01-8e67-0ea176296746'
    production = 'production'


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


class Configuration(object):
    DEFAULT_ORG_ID = 'a8e526e4-cb2d-4188-ac25-294e76f9f467'
    AUTH_AUDIENCE_ID = '75wT048QcpE7ujwBJPPjr263eTHl4gEX'
    ENV = get_environ_var('WORKER_ENV', Environments.staging)

    CLI_CLIENT_ID = 'bleED0RUwb7CJ9j7D48tqSiSZRZn29AV'
    CLI_CLIENT_SECRET = '0s8VNQ26QrteS3H5KXIIPvkDcNL5PfT-_pWwAVNI4MpDaDg86O2XUH8lT19KLNiZ'


class EnvDrivenConfig:

    def __init__(self, slug, env_id, base_url, audience):
        self.slug = slug
        self.env_id = env_id
        self.base_url = base_url
        self.audience = audience


if os.environ.get('WORKER_ENV') is not Environments.production:
    logging.setLoggerClass(ColoredLogger)
else:
    logging.basicConfig(format="%(asctime)s %(levelname)-8s [%(name)s]  %(message)s (%(filename)s:%(lineno)d)",
                        stream=sys.stdout, level=logging.INFO)


def make_logger(name):
    return logging.getLogger(name)


def get_config(env):
    return CONFIG_BY_ENV[env]



CONFIG_BY_ENV = {
    Environments.staging: EnvDrivenConfig(slug=Environments.staging,
                                          env_id='4a9cfc2b-2580-4d01-8e67-0ea176296746',
                                          base_url='https://facilities-staging.api.ndustrial.io',
                                          audience='xG775XHIOZVUn84seNeHXi0Qe55YuR5w'),
    Environments.production: EnvDrivenConfig(slug=Environments.production,
                                             env_id='64c6dde7-7830-47c1-a411-6c39c158ec79',
                                             base_url='https://facilities.api.ndustrial.io',
                                             audience='SgbCopArnGMa9PsRlCVUCVRwxocntlg0')
}