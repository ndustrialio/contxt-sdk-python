from datetime import datetime

import pandas as pd

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
        arg_parser.add_argument("--metric_name", required=False, dest="metric_name", type=str,
                                help="Provide the name of the asset metric as a filter when possible")

        self.facilities_service = FacilitiesService(self.cli.auth)
        self.contxt_service = ContxtService(self.cli.auth)


    '''
        assets facilities get-all --organization_id <organization_id> --organization_name <organization_name>
        assets types get-all (--organization_id <organization_id> OR --organization_name "Lineage Logistics")
        assets types get --type_name <name> (--organization_id <organization_id> OR --organization_name "Lineage Logistics")
        assets metrics get --type_name <name> --metric_name <name> (--organization_id <organization_id> OR --organization_name "Lineage Logistics")
    '''
    def parse_command(self, command, args):
        # TODO: this should only handle parsing the args and call a
        # dedicated function

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

        elif args.command == 'metrics':

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
        assets = asset_service.get_assets_for_type(type_object)
        asset_label_to_metric_values = {
            a.label: [
                mv for mv in
                asset_service.fetch_all_metric_values_for_asset(a)
                if mv.asset_metric_id == metric.id
            ]
            for a in assets
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
