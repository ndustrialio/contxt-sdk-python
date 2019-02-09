from datetime import datetime

from contxt.services.facilities import FacilitiesService
from contxt.services.contxt import ContxtService
from contxt.func.organizations import find_organization_by_name

from contxt.utils import make_logger

logger = make_logger(__name__)


class Assets:

    def __init__(self, cli_module, arg_parser):
        self.cli = cli_module

        arg_parser.add_argument("command", type=str, help="The primary command to run within this Assets module")
        arg_parser.add_argument("subcommand", type=str, help="Subcommand for an action in a module")

        arg_parser.add_argument("--facility_id", required=False, dest="facility_id", type=int,
                                help="Provide the facility_id (integer) as a filter when possible")
        arg_parser.add_argument("--organization_id", required=False, dest="organization_id", type=str,
                                help="Provide the organization_id (uuid, str) as a filter when possible")
        arg_parser.add_argument("--organization_name", required=False, dest="organization_name", type=str,
                                help="Provide the organization_name (str) as a filter when possible")

        self.facilities_service = FacilitiesService(self.cli.auth)
        self.contxt_service = ContxtService(self.cli.auth)

    '''
        assets facilities get-all --organization_id <organization_id> --organization_name <organization_name>
    '''
    def parse_command(self, command, args):

        if args.command == 'facilities':

            if args.subcommand == 'get-all':

                if args.organization_id is not None and args.organization_name is not None:
                    logger.critical("Specify organization_id OR organization_name. Not both.")
                    return

                if args.organization_id:
                    print(self.facilities_service.get_facilities(organization_id=args.organization_id))

                elif args.organization_name:

                    organization_object = find_organization_by_name(contxt_service=self.contxt_service,
                                                                    organization_name=args.organization_name)
                    if organization_object:
                        print(self.facilities_service.get_facilities(organization_id=organization_object.id))
                    else:
                        logger.warn("Organization not found")

                else:
                    print(self.facilities_service.get_facilities())

            else:
                logger.critical("Invalid subcommand. Must be one of {get-spend}")
                return

        else:
            logger.critical('Unrecognized command: {}'.format(args.command))

