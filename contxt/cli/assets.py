import pandas as pd
from tabulate import tabulate
from tqdm import tqdm

from contxt.cli import ContxtCLI
from contxt.func.organizations import (OrganizationArgumentException,
                                       check_required_organization_args,
                                       get_organization_id_from_arguments)
from contxt.services import APIObjectCollection
from contxt.services.asset_framework import LazyAssetsService
from contxt.services.contxt import ContxtService
from contxt.services.facilities import FacilitiesService
from contxt.utils import make_logger
from contxt.utils.vis import run_plotly

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

        super(Assets, self).__init__(arg_parser, COMMANDS)

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

    # FIXME: needs to be converted to new-style arg parser
    def get_asset_metrics(self, args):
        if args.command == 'metrics':

            if args.subcommand == 'get':

                asset_label_to_metric_values = self.get_metrics_for_type_and_metric_label(
                    args)

                # Plot or print
                # TODO: create plot flag
                if True:
                    self.plot_asset_metrics(asset_label_to_metric_values, args.metric_name)
                else:
                    print(asset_label_to_metric_values)

            else:
                logger.critical("Invalid subcommand. Must be one of {get}")
                return

        else:
            logger.critical('Unrecognized command: {}'.format(args.command))

    def get_metrics_for_type_and_metric_label(self, args):
        # Check for expected flags
        if args.type_name is None:
            logger.critical("--type_name argument is required")
            return
        if args.metric_name is None:
            logger.critical("--metric_name argument is required")
            return

        check_required_organization_args(args, org_is_required=True)

        organization_id = get_organization_id_from_arguments(
            self.contxt_service, args)

        asset_service = LazyAssetsService(
            auth_module=self.cli.auth, organization_id=organization_id)

        # Validate and get asset type name
        if args.type_name not in asset_service.types_by_label:
            logger.critical("Type not found: {}".format(args.type_name))
            return

        type_object = asset_service.types_by_label[args.type_name]

        # Validate and get metric name
        asset_service.load_type_metrics(type_object)
        if args.metric_name not in type_object.metrics:
            logger.critical("Metric not found: {}".format(args.metric_name))
            return

        metric = asset_service.asset_metric_with_label(type_object, args.metric_name)

        # Fetch all metric values for metric
        # TODO: can be very slow
        logger.info(f'Fetching {args.type_name} asset types')
        assets = asset_service.get_assets_for_type(type_object)
        logger.info(f'Fetching all {args.metric_name} metric values')
        asset_label_to_metric_values = {
            a.label: asset_service.fetch_all_metric_values_for_asset_metric(
                a, metric)
            for a in tqdm(assets)
        }

        return asset_label_to_metric_values

    def plot_asset_metrics(self, asset_label_to_metric_values, metric_label):
        def make_title(asset_label):
            return '{} for {}'.format(metric_label, asset_label)

        def create_df(metric_values):
            filtered_dicts = []
            for mv in metric_values:
                filtered_dicts.extend([{
                    'x': mv.effective_start_date,
                    'y': mv.value
                }, {
                    'x': mv.effective_end_date,
                    'y': mv.value
                }])
            return pd.DataFrame(filtered_dicts)

        title_to_df = {
            make_title(k): create_df(v)
            for k, v in asset_label_to_metric_values.items()
        }
        run_plotly(title_to_df, x_label='x', y_label='y')
