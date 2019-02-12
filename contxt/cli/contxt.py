from contxt.services.contxt import ContxtService
from contxt.func.organizations import find_organization_by_name
from contxt.services import UnauthorizedException

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
        arg_parser.add_argument("--user_id", required=False, dest="user_id", type=str,
                                help="Provide the user_id (str) when required by the subcommand")

        self.contxt_service = ContxtService(self.cli.auth)

    '''
        contxt organizations get-all
        contxt organizations create --organization_name "<name>"
        contxt organizations add-user --organization_id <organization_id> --user_id <user_id>
        contxt organizations get-users (--organization_id <organization_id OR --organization_name <organization_name>)
    '''
    def parse_command(self, command, args):

        if args.command == 'organizations':

            if args.subcommand == 'get-all':

                print(self.contxt_service.get_organizations())

            elif args.subcommand == 'create':

                if args.organization_name is None:
                    logger.critical("--organization_name is required")
                    return
                try:

                    current_user_id = self.contxt_service.get_logged_in_user_id()

                    new_organization = self.contxt_service.create_organization(organization_name=args.organization_name)
                    print(new_organization)

                    print('Adding you to list of organization users')
                    print(self.contxt_service.add_user_to_organization(organization_id=new_organization.id,
                                                                       user_id=current_user_id))

                except UnauthorizedException as e:
                    logger.critical(e)
                    return

            elif args.subcommand == 'add-user':

                if args.organization_id is None or args.user_id is None:
                    logger.critical("--organization_id and user_id are required")
                    return

                try:
                    print(self.contxt_service.add_user_to_organization(organization_id=args.organization_id,
                                                                       user_id=args.user_id))
                except UnauthorizedException as e:
                    logger.critical(e)
                    return

            elif args.subcommand == 'get-users':

                if args.organization_id is None and args.organization_name is None:
                    logger.critical("one of --organization_id or --organization_name must be provided")
                    return

                if args.organization_name:
                    org = find_organization_by_name(self.contxt_service, args.organization_name)
                    if org is None:
                        logger.critical("Organization not found")
                        return
                    organization_id = org.id
                else:
                    organization_id = args.organization_id

                print(self.contxt_service.get_organization_users(organization_id=organization_id))

            else:
                logger.critical("Invalid subcommand. Must be one of {get-all}")
                return

        else:
            logger.critical('Unrecognized command: {}'.format(args.command))

