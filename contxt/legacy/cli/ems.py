import csv

from tabulate import tabulate
from contxt.legacy.cli import ContxtCLI
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
                            'type': str,
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
                },
                {
                    # ./contxt.py ems utilities get-spend -h
                    'command': 'get-spend-vs-metric',
                    'print_handler': 'print_facility_spend_vs_metric',
                    'method_call_info': {
                        'module': 'contxt.functions.ems',
                        'class': 'EMS',
                        'method': 'get_facility_spend_vs_monthly_metric',
                    },
                    'args': [
                        {
                            'arg': 'facility_id',
                            'required': True,
                            'type': int,
                            'help': 'Provide the facility_id of the facility you want to use'
                        },
                        {
                            'arg': 'metric',
                            'required': True,
                            'type': str,
                            'help': 'Provide the metric you want to normalize against'
                        },
                        {
                            'arg': 'interval',
                            'required': True,
                            'type': str,
                            'help': "Provide the interval to perform the calculation. 'monthly' is the only "
                                    "option currently",
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
                            'arg': 'proforma',
                            'required': False,
                            'type': bool,
                            'help': 'Include proforma calculations'
                        }
                    ]
                },
                {
                    # ./contxt.py ems utilities get-spend -h
                    'command': 'get-organization-spend-vs-metric',
                    'print_handler': 'print_organization_spend_vs_metric',
                    'method_call_info': {
                        'module': 'contxt.functions.ems',
                        'class': 'EMS',
                        'method': 'get_organization_spend_vs_monthly_metric',
                    },
                    'to_file_handler': 'to_csv_organization_spend_vs_metric',
                    'args': [
                        {
                            'arg': 'organization_id',
                            'required': False,
                            'type': str,
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
                            'arg': 'metric',
                            'required': True,
                            'type': str,
                            'help': 'Provide the metric you want to normalize against'
                        },
                        {
                            'arg': 'interval',
                            'required': True,
                            'type': str,
                            'help': "Provide the interval to perform the calculation. 'monthly' is the only "
                                    "option currently",
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
                            'arg': 'proforma',
                            'required': False,
                            'type': bool,
                            'help': 'Include proforma calculations'
                        }
                    ]
                },
                {
                    # ./contxt.py ems utilities get-spend -h
                    'command': 'get-usage-vs-metric',
                    'print_handler': 'print_facility_usage_vs_metric',
                    'method_call_info': {
                        'module': 'contxt.functions.ems',
                        'class': 'EMS',
                        'method': 'get_facility_usage_vs_monthly_metric',
                    },
                    'args': [
                        {
                            'arg': 'facility_id',
                            'required': True,
                            'type': int,
                            'help': 'Provide the facility_id of the facility you want to use'
                        },
                        {
                            'arg': 'metric',
                            'required': True,
                            'type': str,
                            'help': 'Provide the metric you want to normalize against'
                        },
                        {
                            'arg': 'interval',
                            'required': True,
                            'type': str,
                            'help': "Provide the interval to perform the calculation. 'monthly' is the only "
                                    "option currently",
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
                        }
                    ]
                }
            ]
        }
}


class EMS(ContxtCLI):

    def __init__(self, arg_parser):
        super().__init__(arg_parser, COMMANDS)

    @staticmethod
    def print_facility_spend_vs_metric(normalized_spend_by_date):

        normalized_to_print = []

        for date, data in normalized_spend_by_date.items():
            # TODO clean this up when we can properly filter metric value data by start->end date
            if 'spend' in data:
                normalized_to_print.append([date.strftime('%Y-%m'),
                                            data['spend'],
                                            data['metric_value'],
                                            data['normalized'],
                                            data['spend_proforma_date']])

        print(tabulate(normalized_to_print, headers=['date', 'spend', 'metric-value', 'normalized', 'spend_proforma_date']))

    @staticmethod
    def print_organization_spend_vs_metric(normalized_spend_by_facility):

        normalized_to_print = []
        headers = []

        overall_spend_data = {}
        for facility, data in normalized_spend_by_facility.items():

            for date, spend_data in data.items():
                pass


        print(tabulate(normalized_to_print))


    @staticmethod
    def to_csv_organization_spend_vs_metric(normalized_spend_by_facility):

        to_csv_data = []

        unique_dates = []
        by_facility = {}

        # gotta organize by date so that all the dates match across facilities
        for facility_name, data in normalized_spend_by_facility.items():

            by_facility[facility_name] = {}
            for date, spend in data.items():
                if date not in unique_dates:
                    unique_dates.append(date)

                by_facility[facility_name][date] = spend['normalized']

        facility_data = {}
        for date in sorted(unique_dates):
            for facility_name, date_data in by_facility.items():
                if facility_name not in facility_data:
                    facility_data[facility_name] = {}
                if date not in date_data:
                    facility_data[facility_name] = None
                else:
                    facility_data[facility_name][date] = date_data[date]

        for facility, date_dict in facility_data.items():

            date_dict['facility_name'] = facility
            to_csv_data.append(date_dict)

        with open('./org_dollars_per_pound.csv', 'w') as f:

            fields = ['facility_name']
            fields.extend(unique_dates)

            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()

            for row in to_csv_data:
                writer.writerow(row)

    @staticmethod
    def print_facility_usage_vs_metric(normalized_usage_by_date):

        normalized_to_print = []

        for date, data in normalized_usage_by_date.items():
            # TODO clean this up when we can properly filter metric value data by start->end date
            if 'usage' in data:
                normalized_to_print.append([date.strftime('%Y-%m'),
                                            data['usage'],
                                            data['metric_value'],
                                            data['normalized'],
                                            data['usage_proforma_date'] if 'usage_proforma_date' in data else None])

        print(tabulate(normalized_to_print,
                       headers=['date', 'usage', 'metric-value', 'normalized', 'spend_proforma_date']))

    #@staticmethod
    #def csv_facility_spend_vs_metric(normalized_spend_by_date):
