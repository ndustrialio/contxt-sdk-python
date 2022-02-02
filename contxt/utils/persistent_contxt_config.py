import os
from pathlib import Path
import logging

from .config import write_config_class_to_file, load_config_class_from_file

logger = logging.getLogger(__name__)
logging.basicConfig(format='[%(module)s %(levelname)s:%(asctime)s] %(message)s', level=logging.INFO)


class ContxtConfigurationError(Exception):
    pass


class PersistentContxtConfig:

    def __init__(self, filename, clazz, use_default_path: bool = True, initialize_if_not_exists: bool = True):
        self.use_default_path = use_default_path
        if self.use_default_path:
            self.base_path = os.path.join(str(Path.home()), '.contxt')
            self.filename = os.path.join(self.base_path, filename)
        else:
            self.filename = filename
        logger.debug(f'Using config file {self.filename}')
        self.clazz = clazz
        self.config = self.load_contxt_file(initialize_if_not_exists)

    def _create_file(self):
        if not os.path.exists(self.base_path):
            os.mkdir(self.base_path)
        if not os.path.exists(self.filename):
            Path(self.filename).touch()

    def write_contxt_file(self):
        if self.use_default_path and not os.path.exists(self.base_path):
            os.mkdir(self.base_path)
        logger.debug(f'Writing config to file {self.filename}')
        write_config_class_to_file(self.filename, self.config, self.clazz)

    def load_contxt_file(self, initialize_if_not_exists: bool):
        if not initialize_if_not_exists and not os.path.exists(self.filename):
            raise ContxtConfigurationError(f'Config file does not exist: {self.filename}')
        elif not os.path.exists(self.filename) and initialize_if_not_exists:
            self._create_file()

        logger.debug(f'Loading config from file {self.filename}')
        config = load_config_class_from_file(self.filename, self.clazz)
        return config
