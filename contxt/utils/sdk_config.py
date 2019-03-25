from contxt.utils import make_logger
from pathlib import Path
import json

logger = make_logger(__name__)


class SDKConfig:

    class __SDKConfig:

        def __init__(self):
            self.contxt_config_path = Path.home() / '.contxt'
            self.config_file = self.contxt_config_path / 'config'

            self.config = self.load_configuration()

        def load_configuration(self):
            logger.debug(f"Loading config from {self.config_file}")
            self.contxt_config_path.mkdir(parents=True, exist_ok=True)

            try:
                with self.config_file.open('r') as f:
                    config = json.load(f)
            except FileNotFoundError:
                print('Config file has not been created yet')
                return {}

            logger.debug("Found config")
            return config

        def store_config_keypair(self, config_category, key, value):

            assert isinstance(config_category, str)

            if config_category not in self.config:
                self.config[config_category] = {}

            self.config[config_category][key] = value

        def store_config(self):
            logger.debug(f"Persisting config file to {self.config_file}")
            with self.config_file.open('w') as f:
                json.dump(self.config, f, indent=4)

        def clear_config(self):
            logger.debug(f"Removing config file {self.config_file}")
            self.config_file.unlink()

    instance = None

    def __init__(self):
        if not SDKConfig.instance:
            SDKConfig.instance = SDKConfig.__SDKConfig()

