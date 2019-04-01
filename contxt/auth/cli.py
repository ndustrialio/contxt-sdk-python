from getpass import getpass

from contxt.auth import BaseAuth
from contxt.services.auth import ContxtAuthService
from contxt.utils import Config, make_logger

logger = make_logger(__name__)


class CLIAuth(BaseAuth):
    """
    Authentication for a CLI user
    """

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

        # Check login is needed
        if self.get_auth_token() is not None:
            if not self._query_user("Already logged in. Continue?"):
                return

        # Prompt for username/password
        username = input("Contxt Username: ")
        password = getpass("Contxt Password: ")

        # Login
        token = self.auth0.login(
            client_id=Config.CLI_CLIENT_ID,
            client_secret=Config.CLI_CLIENT_SECRET,
            username=username,
            password=password,
            scope='offline_access',
            audience=Config.AUTH_AUDIENCE_ID,
            grant_type='password',
            realm='')

        # Store token
        self.store_service_token(
            audience=Config.AUTH_AUDIENCE_ID,
            access_token=token['access_token'],
            refresh_token=token['refresh_token'])

    def reset(self):
        self.clear_tokens()
