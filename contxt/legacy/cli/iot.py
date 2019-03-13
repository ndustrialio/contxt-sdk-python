from contxt.legacy.cli import ContxtCLI
from contxt.utils import make_logger

logger = make_logger(__name__)

COMMANDS = {
    'groupings': {
        'info': 'IOT Groupings CLI',
        'functions': [
            {
                'command': 'get-all',
                'method_call_info': {
                    'module': 'contxt.services.iot',
                    'class': 'IOTService',
                    'method': 'get_all_groupings'
                },
                'args': [
                    {
                        'arg': 'facility_id',
                        'required': True,
                        'type': int,
                        'help': 'Grab groupings by their facility_id'
                    },
                ],
                'print_result': True
            },
            {
                'command': 'get-fields',
                'method_call_info': {
                    'module': 'contxt.functions.iot',
                    'class': 'IOT',
                    'method': 'get_fields_for_grouping'
                },
                'args': [
                    {
                        'arg': 'grouping_id',
                        'required': True,
                        'type': str,
                        'help': 'Grouping ID'
                    }
                ],
                'print_result': True
            },
            {
                'command': 'get-data-for-fields',
                'method_call_info': {
                    'module': 'contxt.functions.iot',
                    'class': 'IOT',
                    'method': 'get_data_for_fields'
                },
                'args': [
                    {
                        'arg': 'grouping_id',
                        'required': True,
                        'type': str,
                        'help': 'Grouping ID'
                    },
                    {
                        'arg': 'start_date',
                        'required': True,
                        'type': str,
                        'help': 'Start date of the data query'
                    },
                    {
                        'arg': 'end_date',
                        'required': False,
                        'type': str,
                        'help': 'End date of the data query'
                    },
                    {
                        'arg': 'window',
                        'required': True,
                        'type': int,
                        'help': 'Specify the data windowing period',
                        'valid_values': [0, 60, 900, 3600]
                    },
                    {
                        'arg': 'plot',
                        'required': False,
                        'type': bool,
                        'help': 'Plot',
                    },
                ]
            }
        ]
    },
    'feeds': {
        'info': 'IOT Feeds CLI',
        'functions': [
            {
                'command': 'get-all',
                'method_call_info': {
                    'module': 'contxt.services.iot',
                    'class': 'IOTService',
                    'method': 'get_all_feeds'
                },
                'args': [
                    {
                        'arg': 'facility_id',
                        'required': False,
                        'type': int,
                        'help': 'Grab feeds by their facility_id'
                    },
                ],
                'print_result': True
            }
        ]
    },
    'fields': {
        'info': 'IOT Fields CLI',
        'functions': [
            {
                'command': 'get-all',
                'method_call_info': {
                    'module': 'contxt.services.iot',
                    'class': 'IOTService',
                    'method': 'get_all_fields'
                },
                'args': [
                    {
                        'arg': 'facility_id',
                        'required': True,
                        'type': int,
                        'help': 'Grab fields by their facility_id'
                    },
                ],
                'print_result': True
            }
        ]
    }
}


class IOT(ContxtCLI):

    def __init__(self, arg_parser):

        super().__init__(arg_parser, COMMANDS)
