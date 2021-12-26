from .persistent_contxt_config import PersistentContxtConfig
from .config import CustomEnvironmentConfig


class EnvironmentConfigurationException(Exception):
    pass


class ContxtEnvironment(PersistentContxtConfig):

    # default location is ~/.contxt/defaults.yml unless otherwise specified in arguments
    def __init__(self, filename='defaults.yml', relative_path=None):
        if relative_path:
            super().__init__(filename, CustomEnvironmentConfig, relative_path=relative_path)
        else:
            super().__init__(filename, CustomEnvironmentConfig)
        self.config: CustomEnvironmentConfig = self.load_contxt_file()

    def __str__(self):
        return str(self.config)

    def get_config_for_service_name(self, service: str):
        if self.config:
            return self.config.get_service_for_current_context(service)
        else:
            raise EnvironmentConfigurationException(f"Config not found for service '{service}'. Not "
                                                    f"found in environment file {self.filename}")
