import os
from pathlib import Path
import logging

from .config import write_config_class_to_file, load_config_class_from_file

logger = logging.getLogger(__name__)
logging.basicConfig(format='[%(module)s %(levelname)s:%(asctime)s] %(message)s', level=logging.INFO)


class PersistentContxtConfig:

    def __init__(self, filename, clazz):
        self.base_path = os.path.join(str(Path.home()), '.contxt')
        self.filename = os.path.join(self.base_path, filename)
        self.clazz = clazz
        self.token_config = self.load_contxt_file()

    def write_contxt_file(self):
        if not os.path.exists(self.base_path):
            os.mkdir(self.base_path)
        logger.debug(f'Writing config to file {self.filename}')
        write_config_class_to_file(self.filename, self.token_config, self.clazz)

    def load_contxt_file(self):
        if os.path.exists(self.filename):
            logger.debug(f'Loading config from file {self.filename}')
            config = load_config_class_from_file(self.filename, self.clazz)
            return config
