from contxt.utils.auth import BaseAuth
from contxt.utils import Config, make_logger

logger = make_logger(__name__)


class MachineAuth(BaseAuth):

    def __init__(self, client_id, client_secret):
        super().__init__(client_id=client_id, client_secret=client_secret)

        self.client_id = client_id
        self.client_secret = client_secret

        self.get_auth_token()
