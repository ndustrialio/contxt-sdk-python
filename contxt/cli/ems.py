from datetime import datetime
from tqdm import tqdm
import csv
import argparse

from contxt.services.ems import EMSService
from contxt.services.contxt import ContxtService
from contxt.services.facilities import FacilitiesService

from contxt.func.organizations import find_organization_by_name

from contxt.utils import make_logger

logger = make_logger(__name__)

COMMANDS = {
    # ./contxt.py ems utilities -h
    'utilities':
        {
            'info': 'EMS Utilities CLI',
            'functions': [
                {
                    # ./contxt.py ems utilities get-spend -h
                    'command': 'get-spend',
                    'function': 'get_spend',
                    'args': [
                        {
                            'arg': 'facility_id',
                            'required': True,
                            'type': int,
                            'help': 'Provide the facility_id (integer) as a filter when possible'
                        },
                        {
                            'arg':'interval',
                            'required': True,
                            'type': str,
                            'help': "Provide the interval ('monthly', 'daily') as a filter when possible",
                            'valid_values': ['daily', 'monthly']
                        },
                        {
                            'arg': 'resource_type',
                            'required': True,
                            'type': str,
                            'help': "Provide the type of resource for spend",
                            'valid_values': ['electric', 'gas', 'combined']
                        },
                        {
                            'arg':'start_date',
                            'required': True,
                            'type': str,
                            'help': 'Provide the start month for spend in YYYY-MM format'
                        },
                        {
                            'arg':'end_date',
                            'required': True,
                            'type': str,
                            'help': 'Provide the end month for spend in YYYY-MM format'
                        },
                        {
                            'arg': 'proforma',
                            'required': False,
                            'type': bool,
                            'help': 'Include proforma calculations'
                        }
                    ]
                },
                {
                    'command': 'get-organization-spend',
                    'function': 'get_organization_spend',
                    'args': [
                        {
                            'arg': 'organization_id',
                            'required': True,
                            'type': int,
                            'help': 'Provide the organization_id (uuid, str) as a filter when possible',
                            'not_required_if': 'organization_name'
                        },
                        {
                            'arg': 'organization_name',
                            'required': True,
                            'type': int,
                            'help': 'Provide the organization_name (str) as a filter when possible',
                            'not_required_if': 'organization_id'
                        },
                        {
                            'arg': 'interval',
                            'required': True,
                            'type': str,
                            'help': "Provide the interval ('monthly', 'daily') as a filter when possible",
                            'valid_values': ['daily', 'monthly']
                        },
                        {
                            'arg': 'resource_type',
                            'required': True,
                            'type': str,
                            'help': "Provide the type of resource for spend",
                            'valid_values': ['electric', 'gas', 'combined']
                        },
                        {
                            'arg': 'start_date',
                            'required': True,
                            'type': str,
                            'help': 'Provide the start month for spend in YYYY-MM format'
                        },
                        {
                            'arg': 'end_date',
                            'required': True,
                            'type': str,
                            'help': 'Provide the end month for spend in YYYY-MM format'
                        }
                    ]
                }
            ]
        }
}


def init_cli_commands(subparser):

    ems_subparser = subparser.add_subparsers(dest='subcommand')

    # OLD CODE
    '''
    ems_parser = ems_subparser.add_parser('utilities')

    utilities_subparser = ems_parser.add_subparsers(dest="utilities-cmd")
    spend_parser = utilities_subparser.add_parser('get-spend')
    spend_parser.add_argument("--facility_id")
    spend_parser.add_argument("--interval")
    spend_parser.add_argument("--resource_type")
    spend_parser.add_argument("--start_date")
    spend_parser.add_argument("--end_date")

    org_spend_parser = utilities_subparser.add_parser('get-org-spend')
    org_spend_parser.add_argument("--organization_id")
    org_spend_parser.add_argument("--resource_type")
    '''

    # NEW CODE

    for command, command_info in COMMANDS.items():

        ems_cmd_parser = ems_subparser.add_parser(command, help=command_info['info'])

        ems_subcommand_subparser = ems_cmd_parser.add_subparsers(dest="{}-cmd".format(command))

        for func in command_info['functions']:

            func_cmd_parser = ems_subcommand_subparser.add_parser(func['command'])

            for arg_dict in func['args']:

                if arg_dict['type'] == bool:
                    func_cmd_parser.add_argument("--{}".format(arg_dict['arg']),
                                                 action="store_true",
                                                 help=arg_dict['help'])
                else:
                    func_cmd_parser.add_argument("--{}".format(arg_dict['arg']),
                                                 required=arg_dict['required'],
                                                 dest=arg_dict['arg'],
                                                 type=arg_dict['type'],
                                                 help=arg_dict['help'])


class EMS:

    def __init__(self, cli_module, arg_parser):
        self.cli = cli_module

        init_cli_commands(arg_parser)
        '''
        arg_parser.add_argument("command", type=str, help="The primary command to run within this EMS module")
        arg_parser.add_argument("subcommand", type=str, help="Subcommand for an action in a module")

        arg_parser.add_argument("--facility_id", required=False, dest="facility_id", type=int,
                                help="Provide the facility_id (integer) as a filter when possible")
        arg_parser.add_argument("--organization_id", required=False, dest="organization_id", type=str,
                                help="Provide the organization_id (uuid, str) as a filter when possible")
        arg_parser.add_argument("--organization_name", required=False, dest="organization_name", type=str,
                                help="Provide the organization name (str) as a filter when possible")
        arg_parser.add_argument("--interval", required=False, dest="interval", type=str,
                                help="Provide the interval ('monthly', 'daily') as a filter when possible")
        arg_parser.add_argument("--resource_type", required=False, dest="resource_type", type=str,
                                help="Provide the resource type (electric, gas, combined)")
        arg_parser.add_argument("--metric", required=False, dest="metric", type=str,
                                help="Provide the metric name")
        arg_parser.add_argument("--month", required=False, dest="month", type=int,
                                help="Provide the Month as a filter when possible")
        arg_parser.add_argument("--year", required=False, dest="month", type=int,
                                help="Provide the Month as a filter when possible")
        arg_parser.add_argument("--proforma", action="store_true",
                                help="Include proforma logic for applicable commands")
        arg_parser.add_argument("--exclude_account_charges", action="store_true",
                                help="Exclude account charges from applicable commands")
        arg_parser.add_argument("--start_date", required=False, dest="start_date", type=str,
                                help="When querying for spend data, this is a required field. Needs to be in YYYY-DD "
                                     "format")
        arg_parser.add_argument("--end_date", required=False, dest="end_date", type=str,
                                help="When querying for spend data, this is an required field. Needs to be in YYYY-DD "
                                     "format")
        arg_parser.add_argument("--to_csv", required=False, dest="to_csv", type=str,
                                help="Name of CSV to export results to")
        '''

        self.ems_service = EMSService(self.cli.auth)
        self.contxt_service = ContxtService(self.cli.auth)
        self.facilities_service = FacilitiesService(self.cli.auth)

    '''
        ems utilities get-spend --facility_id <facility_id> --interval <monthly, daily> --resource_type <electric> --start_date <YYYY-MM> --end_date <YYYY-MM>
        ems utilities get-organization-spend --organization_id <organization_id> --interval <monthly> --resource_type <electric> --start_date <YYYY-MM> --end_date <YYYY-MM>
        -- ems utilities get-usage --facility_id <facility_id> --interval <monthly, daily> --resource_type <electric> --start_date <YYYY-MM> --end_date <YYYY-MM>
        -- ems utilities get-monthly-metrics --metric <metric_name> --facility_id <facility_id> --month <month_int> --year <year_int>
    '''
    def parse_command(self, args):

        if args.command == 'utilities':

            if args.subcommand == 'get-spend':

                if args.facility_id is None or args.interval is None or args.resource_type is None or args.start_date is None or args.end_date is None:
                    logger.critical("--facility_id, --interval, --type, --start_date, --end_date is required for "
                                    "utilities get-spend command")
                    return

                start_date = datetime.strptime(args.start_date, "%Y-%m")
                end_date = datetime.strptime(args.end_date, "%Y-%m")

                if args.resource_type not in ['electric', 'gas', 'combined']:
                    logger.critical("--resource_type must be one of 'electrical','gas','combined'")
                    return

                if args.interval == 'monthly':

                    print(args.proforma)

                    print(self.ems_service.get_monthly_utility_spend(facility_id=args.facility_id,
                                                                     type=args.resource_type,
                                                                     date_start=start_date,
                                                                     date_end=end_date,
                                                                     proforma=args.proforma))

                elif args.interval == 'daily':
                    pass

                else:
                    print("Invalid interval provided: {}. Must be 'monthly' or 'daily'")

            elif args.subcommand == 'get-organization-spend':

                self.get_organization_spend(args)

            else:
                logger.critical("Invalid subcommand. Must be one of {get-spend}")
                return

        else:
            logger.critical('Unrecognized command: {}'.format(args.command))

    def get_organization_spend(self, args):

        if (args.organization_id is None and args.organization_name is None) or args.resource_type is None or args.start_date is None or args.end_date is None:
            logger.critical("(--organization_id or --organization_name), --type, --start_date, --end_date is "
                            "required for utilities get-organization-spend command")
            return

        if args.interval is not None:
            logger.critical("--interval is not required for organization utility spend (monthly-only)")
            return

        start_date = datetime.strptime(args.start_date, "%Y-%m")
        end_date = datetime.strptime(args.end_date, "%Y-%m")

        if args.to_csv is None:
            logger.critical("--to_csv is required for this subcommand")
            return

        if args.resource_type not in ['electric', 'gas', 'combined']:
            logger.critical("--resource_type must be one of 'electrical','gas','combined'")
            return

        if args.organization_name:
            org = find_organization_by_name(self.contxt_service,
                                            organization_name=args.organization_name)
            if org is None:
                logger.critical("Organization not found")
                return

            organization_id = org.id
        else:
            organization_id = args.organization_id

        # Get all facilities for this organization
        facilities = self.facilities_service.get_facilities(organization_id)

        organization_spend = {}
        logger.info("Loading data for facilities")
        for facility in tqdm(facilities):
            spend = self.ems_service.get_monthly_utility_spend(facility_id=facility.id,
                                                               type=args.resource_type,
                                                               date_start=start_date,
                                                               date_end=end_date)
            organization_spend[facility.name] = {}
            for period in spend.spend_periods:
                organization_spend[facility.name][period.date] = period.spend

        # write this to the CSV file
        field_names = ['facility']
        field_names.extend(organization_spend[list(organization_spend.keys())[0]].keys())
        with open(args.to_csv, 'w') as f:
            csv_writer = csv.DictWriter(f, fieldnames=field_names)

            csv_writer.writeheader()

            for facility_name, spend_dict in organization_spend.items():
                row = spend_dict
                row['facility'] = facility_name
                csv_writer.writerow(row)
