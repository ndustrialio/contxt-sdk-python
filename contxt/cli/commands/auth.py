from .common import BaseParser


class Auth(BaseParser):
    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("auth", help="Authentication")
        parser.set_defaults(func=self._help)
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Login
        login_parser = _subparsers.add_parser("login", help="Login to contxt")
        login_parser.set_defaults(func=self._login)

        # Logout
        logout_parser = _subparsers.add_parser("logout", help="Logout of contxt")
        logout_parser.set_defaults(func=self._logout)

        return parser

    def _login(self, args):
        args.auth.login()

    def _logout(self, args):
        args.auth.logout()
