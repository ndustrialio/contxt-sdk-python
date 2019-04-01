from contxt.auth import BaseAuth
from contxt.utils import Config, make_logger

logger = make_logger(__name__)


class MachineAuth(BaseAuth):
    """
    Authentication for a service or worker
    """

    def __init__(self, client_id, client_secret):
        super().__init__(client_id=client_id, client_secret=client_secret)
        # self.get_auth_token()
