from typing import List, Optional

from .persistent_contxt_config import PersistentContxtConfig
from .config import CustomEnvironmentConfig, ContxtEnvironmentConfig, ContxtCliEnvironmentConfig


class EnvironmentConfigurationException(Exception):
    pass


class ContxtEnvironment(PersistentContxtConfig):

    # default location is ~/.contxt/defaults.yml unless otherwise specified in arguments
    def __init__(self, filename: Optional[str]):
        if filename:
            super().__init__(filename, CustomEnvironmentConfig, use_default_path=False)
        else:
            super().__init__('defaults.yml', CustomEnvironmentConfig)
        self.config: CustomEnvironmentConfig = self.load_contxt_file()

    def __str__(self):
        return str(self.config)

    def get_config_for_service_name(self, service: str) -> ContxtEnvironmentConfig:
        if self.config:
            return self.config.get_service_for_current_context(service)
        else:
            raise EnvironmentConfigurationException(f"Config not found for service '{service}'. Not "
                                                    f"found in environment file {self.filename}")

    def get_cli_config_for_service(self, service: str) -> ContxtCliEnvironmentConfig:
        service_config = self.get_config_for_service_name(service)

        return self.config.get_cli_environment_for_auth_provider(service_config.apiEnvironment.authProvider)

    def get_possible_configs_for_service_name(self, service_name: str) -> List[ContxtEnvironmentConfig]:
        return self.config.get_configs_for_service(service_name=service_name)

    def set_context_for_service_name(self, service: str, environment_name: str):
        service_config = self.config.get_config_for_service_environment(service_name=service,
                                                                        environment_name=environment_name)

        if not service_config:
            raise EnvironmentConfigurationException(f'Service / Environment is not registered ({service}:{environment_name})')

        self.config.set_context_for_service(service_name=service,
                                            environment=environment_name)

        self.write_contxt_file()

