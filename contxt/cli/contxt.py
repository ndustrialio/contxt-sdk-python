from contxt.services.contxt import ContxtService
from contxt.func.organizations import find_organization_by_name

from contxt.utils import make_logger

logger = make_logger(__name__)


class Contxt:

    def __init__(self, cli_module, arg_parser):
        self.cli = cli_module

        arg_parser.add_argument("command", type=str, help="The primary command to run within this Contxt module")
        arg_parser.add_argument("subcommand", type=str, help="Subcommand for an action in a module")

        arg_parser.add_argument("--organization_id", required=False, dest="organization_id", type=str,
                                help="Provide the organization_id (uuid, str) as a filter when possible")
        arg_parser.add_argument("--organization_name", required=False, dest="organization_name", type=str,
                                help="Provide the organization_name (str) as a filter when possible")

        self.contxt_service = ContxtService(self.cli.auth)

    '''
        contxt organizations get-all
    '''
    def parse_command(self, command, args):

        if args.command == 'organizations':

            if args.subcommand == 'get-all':

                print(self.contxt_service.get_organizations())

            else:
                logger.critical("Invalid subcommand. Must be one of {get-all}")
                return

        else:
            logger.critical('Unrecognized command: {}'.format(args.command))

