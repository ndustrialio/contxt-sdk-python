from datetime import datetime
from tqdm import tqdm
import csv
from importlib import import_module

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
                    'method_call_info': {
                        'module': 'contxt.func.ems',
                        'class': 'EMS',
                        'method': 'get_facility_spend',
                    },
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
                    'method_call_info': {
                        'module': 'contxt.func.ems',
                        'class': 'EMS',
                        'method': 'get_organization_spend'
                    },
                    'args': [
                        {
                            'arg': 'organization_id',
                            'required': False,
                            'type': int,
                            'help': 'Provide the organization_id (uuid, str) as a filter when possible',
                            'required_if_not': 'organization_name'
                        },
                        {
                            'arg': 'organization_name',
                            'required': False,
                            'type': int,
                            'help': 'Provide the organization_name (str) as a filter when possible',
                            'required_if_not': 'organization_id'
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

    function_call_map = {}

    ems_subparser = subparser.add_subparsers(dest='module_command')

    for command, command_info in COMMANDS.items():

        function_call_map[command] = {}
        ems_cmd_parser = ems_subparser.add_parser(command, help=command_info['info'])

        ems_subcommand_subparser = ems_cmd_parser.add_subparsers(dest="module_subcommand".format(command))

        for func in command_info['functions']:

            function_call_map[command][func['command']] = func

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
                                                 choices=arg_dict['valid_values'] if 'valid_values' in arg_dict else None,
                                                 type=arg_dict['type'],
                                                 help=arg_dict['help'])

    return function_call_map


def form_method_arguments(func_definition, args):

    method_arguments = {}

    for arg_config in func_definition['args']:
        arg_name = arg_config['arg']

        method_arguments[arg_name] = args.__getattribute__(arg_name)

    return method_arguments


def call_function(func_map, args, auth_module):

    if args.module_command not in func_map:
        logger.critical("Cannot locate function for command")
        return

    if args.module_subcommand not in func_map[args.module_command]:
        logger.critical("Cannot locate function for command")
        return

    func_definition = func_map[args.module_command][args.module_subcommand]

    method_info = func_definition['method_call_info']

    func_module = import_module(method_info['module'])
    module_class = getattr(func_module, method_info['class'])

    instance = module_class(auth_module)

    module_method = getattr(instance, method_info['method'])

    method_args = form_method_arguments(func_definition, args)

    # call the method
    module_method(**method_args)


class EMS:

    def __init__(self, cli_module, arg_parser):
        self.cli = cli_module

        self.func_map = init_cli_commands(arg_parser)

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

        call_function(self.func_map, args, self.cli.auth)

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
