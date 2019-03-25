from getpass import getpass

from contxt.services.auth import ContxtAuthService
from contxt.utils.auth import BaseAuth
from contxt.utils import Config, make_logger

logger = make_logger(__name__)


class CLIAuth(BaseAuth):

    def __init__(self, force_login=True):
        super().__init__(client_id=Config.CLI_CLIENT_ID, cli_mode=True)

        if self.get_auth_token() is None and force_login:
            logger.info("Token doesn't exist or can't be refreshed. Please re-authenticate")
            self.login()

    def _query_user(self, question):
        accepted_answers = ["y", "n"]
        ans = input(f"{question} ({'/'.join(accepted_answers)}) ").lower()[0:1]
        while ans not in accepted_answers:
            ans = input(
                f"Please enter {' or '.join(accepted_answers)}. ").lower()[0:1]
        return ans == "y"

    def login(self):

        if self.get_auth_token() is not None:
            proceed = self._query_user("Already logged in. Do you wish to continue?")
            if not proceed:
                return

        username = input("Contxt Username: ")
        password = getpass("Contxt Password: ")

        token = self.auth0.login(
            client_id=Config.CLI_CLIENT_ID,
            client_secret=Config.CLI_CLIENT_SECRET,
            username=username,
            password=password,
            scope='offline_access',
            audience=Config.AUTH_AUDIENCE_ID,
            grant_type='password',
            realm='')

        self.store_service_token(
            audience=Config.AUTH_AUDIENCE_ID,
            access_token=token['access_token'],
            refresh_token=token['refresh_token'])

    def reset(self):
        self.clear_tokens()
