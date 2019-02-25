import json
import os
from datetime import datetime
from getpass import getpass
from pathlib import Path

import jwt
from auth0.v3.authentication.get_token import GetToken

from contxt.services.authentication import ContxtAuthService
from contxt.utils import Config, Utils, make_logger

logger = make_logger(__name__)

AUTH_AUDIENCE = '75wT048QcpE7ujwBJPPjr263eTHl4gEX'


class BaseAuth:

    def __init__(self, client_id, cli_mode=False, client_secret=None):
        self.client_id = client_id
        self.cli_mode = cli_mode
        self.client_secret = client_secret
        self.auth0 = GetToken('ndustrial.auth0.com')

        home_dir = str(Path.home())
        self.contxt_config_dir = os.path.join(home_dir, '.contxt')
        self.token_file = os.path.join(self.contxt_config_dir, 'tokens')

        # load up the tokens we have
        self.tokens = self.load_tokens()

        if AUTH_AUDIENCE in self.tokens:
            self.auth_access_token = self.get_token_for_client(AUTH_AUDIENCE)
        else:
            self.auth_access_token = None

        self.contxt_auth = ContxtAuthService(self.auth_access_token, 'production')

    def get_auth_token(self):
        return self.auth_access_token

    def set_auth_token(self, access_token, refresh_token=None):
        self.auth_access_token = access_token
        self.store_service_token(client_id=AUTH_AUDIENCE,
                                 access_token=access_token,
                                 refresh_token=refresh_token)

    def refresh_contxt_auth_token(self):
        refresh_token = self.tokens[AUTH_AUDIENCE]['refresh_token']
        token = self.auth0.refresh_token(client_id=self.client_id,
                                         client_secret=self.client_secret if self.client_secret else '',
                                         refresh_token=refresh_token)

        # store the new access token and re-store the existing refresh token
        self.store_service_token(AUTH_AUDIENCE, token['access_token'], refresh_token)

    def authenticate_to_service(self, service_audience):
        print(f"Getting new token for {service_audience}")
        token = self.contxt_auth.get_new_token_for_client_id(service_audience)
        self.store_service_token(service_audience, token)

        return token

    def get_token_for_client(self, client_id):
        '''
        # special logic if it's the primary auth audience we're trying to get a token for
        if client_id == AUTH_AUDIENCE:
            if client_id in self.tokens:
                # if this client has a refresh token, use it to get a new token
                refresh_token = self.tokens['refresh_token']

                token = self.get_new_token_from_refresh_token(refresh_token)
                self.store_service_token(client_id=client_id,
                                         access_token=token['access_token'],
                                         refresh_token=token['refresh_token'])
            elif self.cli_mode:
                logger.warning('Never authenticated via CLI. Please run `auth login` command.')
                raise Exception('Never authenticated via CLI. Please run `auth login` command.')
            else:
                # TODO implement me
                logger.critical('Need to implement client_id/client_secret authentication')
                raise NotImplementedError('Need to implement client_id/client_secret authentication')
        '''

        # check to see if we've gotten a token for this service or not
        if client_id not in self.tokens:
            # try to get a token, whether it's a refresh or not
            self.authenticate_to_service(client_id)

        # check to see if have the token, but needs to be refreshed
        if self.token_is_expired_for_client(client_id):
            logger.warn(f'Token expired for client {client_id} -- Refreshing')

            # if it's the contxt auth client, we need to follow the other refresh route via Auth0
            if client_id == AUTH_AUDIENCE:
                self.refresh_contxt_auth_token()
            else:
                self.authenticate_to_service(client_id)

        access_token = self.tokens[client_id]['token']
        return access_token

    def token_is_expired_for_client(self, client_id):

        access_token = self.tokens[client_id]['token']

        decoded_token = jwt.decode(access_token, verify=False)

        token_expiration_epoch = decoded_token['exp']

        if token_expiration_epoch <= Utils.get_epoch_time(datetime.now()):
            return True

        return False

    def load_tokens(self):
        os.makedirs(self.contxt_config_dir, exist_ok=True)

        try:
            with open(self.token_file, 'r') as f:
                tokens = json.load(f)
        except FileNotFoundError:
            print('Token file has not been created yet')
            return {}

        return tokens

    def store_service_token(self, client_id, access_token, refresh_token=None):
        self.tokens[client_id] = {'token': access_token,
                                  'refresh_token': refresh_token
                                  }

        self.store_tokens()

    def store_tokens(self):
        with open(self.token_file, 'w') as f:
            json.dump(self.tokens, f, indent=4)

    def clear_tokens(self):
        os.remove(self.token_file)


class CLIAuth(BaseAuth):

    def __init__(self):
        super().__init__(client_id=Config.CLI_CLIENT_ID, cli_mode=True)

        if self.get_auth_token() is None:
            logger.info("Token doesn't exist or can't be refreshed. Please re-authenticate")
            self.login()

    def setup_parser(self, arg_parser):
        auth_subparser = arg_parser.add_subparsers(dest="auth_subcommand")

        auth_subparser.add_parser("login")
        auth_subparser.add_parser("reset")

    def parse_command(self, args):

        if args.auth_subcommand == "login":
            self.login()
        elif args.auth_subcommand == "reset":
            self.reset()
        else:
            print(f"Unrecognized subcommand {args.auth_subcommand}")

    def login(self):

        username = input("Contxt Username: ")
        password = getpass("Contxt Password: ")

        token = self.auth0.login(client_id=Config.CLI_CLIENT_ID,
                                 client_secret=Config.CLI_CLIENT_SECRET,
                                 username=username,
                                 password=password,
                                 scope='offline_access',
                                 audience=Config.AUTH_AUDIENCE_ID,
                                 grant_type='password',
                                 realm='')

        self.store_service_token(Config.AUTH_AUDIENCE_ID,
                                 access_token=token['access_token'],
                                 refresh_token=token['refresh_token'])

    def reset(self):
        self.clear_tokens()
