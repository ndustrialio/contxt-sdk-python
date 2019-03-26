import os

from contxt.utils.auth.machine import MachineAuth


class WorkerConfigurationError(Exception):
    pass


class BaseWorker:

    def __init__(self, client_id=None, client_secret=None, environment_id=None):

        self.client_id = client_id or os.environ.get('CLIENT_ID')
        self.client_secret = client_secret or os.environ.get('CLIENT_SECRET')
        self.environment_id = environment_id or os.environ.get('ENVIRONMENT_ID')

        if self.client_id is None or self.client_secret is None:
            raise WorkerConfigurationError("CLIENT_ID and CLIENT_SECRET must be provided to instantiate a "
                                           "BaseWorker class. Must be provided as parameters or via environment "
                                           "variables.")

        if self.environment_id:
            # TODO go and retrieve configurations from Contxt (if one exists)
            pass

        self.auth_module = MachineAuth(client_id=self.client_id,
                                       client_secret=self.client_secret)


