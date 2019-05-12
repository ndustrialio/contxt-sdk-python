from contxt.auth import BaseAuth


# TODO: remove this class, as its just an alias around BaseAuth
class MachineAuth(BaseAuth):
    """
    Authentication for a non-human client, such as a service, api, or worker
    """
