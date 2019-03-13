from tabulate import tabulate

from contxt.legacy.cli import ContxtCLI
from contxt.legacy.services import APIObjectCollection
from contxt.utils import make_logger

logger = make_logger(__name__)

COMMANDS = {
    'facilities': {
        'info': 'Facilities CLI',
        'functions': [
            {
                'command': 'get-all',
                'method_call_info': {
                    'module': 'contxt.functions.facilities',
                    'class': 'Facilities',
                    'method': 'get_all_facilities'
                },
                'args': [
                    {
                        'arg': 'organization_id',
                        'required': False,
                        'type': int,
                        'help': 'Provide the organization_id (uuid, str) as a filter'
                    },
                    {
                        'arg': 'organization_name',
                        'required': False,
                        'type': str,
                        'help': 'Provide the organization_name (str) as a filter'
                    }
                ],
            }
        ]
    },
    'types': {
        'info': 'Asset Types CLI',
        'functions': [
            {
                'command': 'get-all',
                'method_call_info': {
                    'module': 'contxt.functions.assets',
                    'class': 'Assets',
                    'method': 'get_asset_types'
                },
                'args': [
                    {
                        'arg': 'organization_id',
                        'required': False,
                        'type': int,
                        'help': 'Provide the organization_id (uuid, str) as a filter'
                    },
                    {
                        'arg': 'organization_name',
                        'required': False,
                        'type': str,
                        'help': 'Provide the organization_name (str) as a filter'
                    }
                ],
            },
            {
                'command': 'get',
                'method_call_info': {
                    'module': 'contxt.functions.assets',
                    'class': 'Assets',
                    'method': 'get_asset_type_info'
                },
                'args': [
                    {
                        'arg': 'organization_id',
                        'required': False,
                        'type': int,
                        'help': 'Provide the organization_id (uuid, str) as a filter'
                    },
                    {
                        'arg': 'organization_name',
                        'required': False,
                        'type': str,
                        'help': 'Provide the organization_name (str) as a filter'
                    },
                    {
                        'arg': 'type',
                        'required': True,
                        'type': str,
                        'help': 'Provide the type label'
                    }
                ],
                'print_handler': 'print_asset_type_handler'
            },
            {
                'command': 'get-assets',
                'method_call_info': {
                    'module': 'contxt.functions.assets',
                    'class': 'Assets',
                    'method': 'get_assets_for_type'
                },
                'args': [
                    {
                        'arg': 'organization_id',
                        'required': False,
                        'type': int,
                        'help': 'Provide the organization_id (uuid, str) as a filter'
                    },
                    {
                        'arg': 'organization_name',
                        'required': False,
                        'type': str,
                        'help': 'Provide the organization_name (str) as a filter'
                    },
                    {
                        'arg': 'type',
                        'required': True,
                        'type': str,
                        'help': 'Provide the type label'
                    }
                ],
            }
        ]
    },
    'assets': {
        'info': 'Asset CLI',
        'functions': [
            {
                'command': 'get-metric',
                'method_call_info': {
                    'module': 'contxt.functions.assets',
                    'class': 'Assets',
                    'method': 'get_metric_values_for_asset'
                },
                'args': [
                    {
                        'arg': 'organization_id',
                        'required': False,
                        'type': int,
                        'help': 'Provide the organization_id (uuid, str) as a filter'
                    },
                    {
                        'arg': 'organization_name',
                        'required': False,
                        'type': str,
                        'help': 'Provide the organization_name (str) as a filter'
                    },
                    {
                        'arg': 'asset_id',
                        'required': True,
                        'type': str,
                        'help': 'Provide the organization_name (str) as a filter'
                    },
                    {
                        'arg': 'metric',
                        'required': True,
                        'type': str,
                        'help': 'Provide the organization_name (str) as a filter'
                    }
                ],
                'print_handler': 'print_asset_metric_values'
            },
            {
                'command': 'get-metric-for-type',
                'method_call_info': {
                    'module': 'contxt.functions.assets',
                    'class': 'Assets',
                    'method': 'get_metric_values_for_asset_type'
                },
                'args': [
                    {
                        'arg': 'organization_id',
                        'required': False,
                        'type': int,
                        'help': 'Provide the organization_id (uuid, str) as a filter'
                    },
                    {
                        'arg': 'organization_name',
                        'required': False,
                        'type': str,
                        'help': 'Provide the organization_name (str) as a filter'
                    },
                    {
                        'arg': 'asset_type_label',
                        'required': True,
                        'type': str,
                        'help': 'Provide the organization_name (str) as a filter'
                    },
                    {
                        'arg': 'metric_label',
                        'required': True,
                        'type': str,
                        'help': 'Provide the organization_name (str) as a filter'
                    },
                    {
                        'arg': 'plot',
                        'required': False,
                        'type': bool,
                        'help': 'Provide the organization_name (str) as a filter'
                    }
                ]
            }
        ]
    },
    'metrics': {
        'info': 'Metrics CLI',
        'functions': [
            {
                'command': 'get',
                'method_call_info': {
                    'module': 'contxt.functions.facilities',
                    'class': 'Facilities',
                    'method': 'get_all_facilities'
                },
                'args': [
                    {
                        'arg': 'organization_id',
                        'required': False,
                        'type': int,
                        'help': 'Provide the organization_id (uuid, str) as a filter'
                    },
                    {
                        'arg': 'organization_name',
                        'required': False,
                        'type': str,
                        'help': 'Provide the organization_name (str) as a filter'
                    }
                ],
            }
        ]
    },

}


class Assets(ContxtCLI):

    def __init__(self, arg_parser):
        super().__init__(arg_parser, COMMANDS)

    @staticmethod
    def print_asset_type_handler(type_object):

        print('Type Information:')
        print(type_object)
        print('\nAttributes: \n')
        print(APIObjectCollection(list(type_object.attributes.values())))
        print('\nMetrics: \n')
        print(APIObjectCollection(list(type_object.metrics.values())))

    @staticmethod
    def print_asset_metric_values(result_tuple):

        metric_obj = result_tuple[0]
        values_collection = result_tuple[1]

        items = []
        for val in values_collection:
            values = val.get_values()
            values.append(metric_obj.label)
            values.append(metric_obj.units)
            items.append(values)

        if len(values_collection) > 0:
            keys = values_collection[0].get_keys()
            keys.extend(['label', 'units'])
            print(tabulate(items, headers=keys))
        else:
            print(values_collection)
