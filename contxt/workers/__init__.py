from os import environ

from contxt.auth.machine import MachineAuth


class WorkerConfigurationError(Exception):
    pass


class BaseWorker:

    def __init__(self, client_id=None, client_secret=None, environment_id=None):

        self.client_id = client_id or environ.get('CLIENT_ID')
        self.client_secret = client_secret or environ.get('CLIENT_SECRET')
        self.environment_id = environment_id or environ.get('ENVIRONMENT_ID')

        # Validate
        # TODO: does this pattern of raising custom exception actually provide
        # usefulness to us? will this error ever be caught? if not, in this
        # case, it's a lot simplier to do environ['CLIENT_SECRET'], which will
        # raise an exception for us
        if self.client_id is None:
            raise WorkerConfigurationError(
                f"CLIENT_ID must be provided (as a parameter or environment variable) to instantiate {self.__class__.__name__} class."
            )
        if self.client_secret is None:
            raise WorkerConfigurationError(
                f"CLIENT_SECRET must be provided (as a parameter or environment variable) to instantiate {self.__class__.__name__} class."
            )


        if self.environment_id:
            # TODO go and retrieve configurations from Contxt (if one exists)
            pass

        self.auth_module = MachineAuth(client_id=self.client_id,
                                       client_secret=self.client_secret)
