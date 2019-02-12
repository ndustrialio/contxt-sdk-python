from datetime import datetime

from contxt.services.facilities import FacilitiesService
from contxt.services.contxt import ContxtService
from contxt.services.asset_framework import LazyAssetsService
from contxt.func.organizations import get_organization_id_from_arguments, \
    check_required_organization_args, OrganizationArgumentException
from contxt.services import APIObjectCollection

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
        arg_parser.add_argument("--type_name", required=False, dest="type_name", type=str,
                                help="Provide the name of the asset type as a filter when possible")

        self.facilities_service = FacilitiesService(self.cli.auth)
        self.contxt_service = ContxtService(self.cli.auth)


    '''
        assets facilities get-all --organization_id <organization_id> --organization_name <organization_name>
        assets types get-all (--organization_id <organization_id> OR --organization_name "Lineage Logistics")
        assets types get --type_name <name> (--organization_id <organization_id> OR --organization_name "Lineage Logistics")
    '''
    def parse_command(self, command, args):

        if args.command == 'facilities':

            if args.subcommand == 'get-all':

                check_required_organization_args(args, org_is_required=False)

                if args.organization_id is not None or args.organization_name is not None:

                    organization_id = get_organization_id_from_arguments(self.contxt_service, args)

                    print(self.facilities_service.get_facilities(organization_id=organization_id))

                else:
                    print(self.facilities_service.get_facilities())

        elif args.command == 'types':

            if args.subcommand == 'get-all':

                check_required_organization_args(args, org_is_required=True)

                organization_id = get_organization_id_from_arguments(self.contxt_service, args)

                asset_service = LazyAssetsService(auth_module=self.cli.auth, organization_id=organization_id)

                asset_service.load_configuration()

                print(APIObjectCollection(list(asset_service.types_by_label.values())))

            elif args.subcommand == 'get':

                if args.type_name is None:
                    logger.critical("--type_name argument is required")
                    return

                check_required_organization_args(args, org_is_required=True)

                organization_id = get_organization_id_from_arguments(self.contxt_service, args)

                asset_service = LazyAssetsService(auth_module=self.cli.auth, organization_id=organization_id)

                if args.type_name not in asset_service.types_by_label:
                    logger.critical("Type not found: {}".format(args.type_name))
                    return

                type_object = asset_service.types_by_label[args.type_name]

                print('Type Information:')
                print(asset_service.load_type_full(type_object))
                print('\nAttributes: \n')
                print(APIObjectCollection(list(type_object.attributes.values())))
                print('\nMetrics: \n')
                print(APIObjectCollection(list(type_object.metrics.values())))

            else:
                logger.critical("Invalid subcommand. Must be one of {get-spend}")
                return

        else:
            logger.critical('Unrecognized command: {}'.format(args.command))

