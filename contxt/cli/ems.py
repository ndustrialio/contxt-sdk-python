from contxt.cli import ContxtCLI

import csv
from datetime import datetime

from tqdm import tqdm

from contxt.functions.organizations import find_organization_by_name
from contxt.services.contxt import ContxtService
from contxt.services.ems import EMSService
from contxt.services.facilities import FacilitiesService
from contxt.utils import make_logger

logger = make_logger(__name__)

'''
    ems utilities get-spend --facility_id <facility_id> --interval <monthly, daily> --resource_type <electric> --start_date <YYYY-MM> --end_date <YYYY-MM>
    ems utilities get-organization-spend --organization_id <organization_id> --interval <monthly> --resource_type <electric> --start_date <YYYY-MM> --end_date <YYYY-MM>
    -- ems utilities get-usage --facility_id <facility_id> --interval <monthly, daily> --resource_type <electric> --start_date <YYYY-MM> --end_date <YYYY-MM>
    -- ems utilities get-monthly-metrics --metric <metric_name> --facility_id <facility_id> --month <month_int> --year <year_int>
'''
COMMANDS = {
    # ./contxt.py ems utilities -h
    'utilities':
        {
            'info': 'EMS Utilities CLI',
            'functions': [
                {
                    # ./contxt.py ems utilities get-spend -h
                    'command': 'get-spend',
                    'print_result': True,
                    'method_call_info': {
                        'module': 'contxt.functions.ems',
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
                        'module': 'contxt.functions.ems',
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
                            'type': str,
                            'help': 'Provide the organization_name (str) as a filter when possible',
                            'required_if_not': 'organization_id'
                        },
                        {
                            'arg': 'interval',
                            'required': True,
                            'type': str,
                            'help': "Provide the interval ('monthly', 'daily') as a filter when possible",
                            'valid_values': ['monthly']
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
                        },
                        {
                            'arg': 'to_csv',
                            'required': True,
                            'type': str,
                            'help': 'The filename to write to for saving the output to CSV'
                        },
                        {
                            'arg': 'proforma',
                            'required': False,
                            'type': bool,
                            'help': 'Include proforma calculations'
                        }
                    ]
                }
            ]
        }
}


class EMS(ContxtCLI):

    def __init__(self, arg_parser):

        super(EMS, self).__init__(arg_parser, COMMANDS)
