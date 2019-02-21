import pandas as pd
from tqdm import tqdm

from contxt.functions.organizations import get_organization_id_from_arguments
from contxt.services import APIObjectCollection
from contxt.services.asset_framework import LazyAssetsService
from contxt.services.contxt import ContxtService
from contxt.utils import make_logger
from contxt.utils.vis import run_plotly

logger = make_logger(__name__)

class Assets:

    def __init__(self, auth_module):

        self.auth = auth_module

        self.contxt_service = ContxtService(self.auth)

    def _initialize_asset_service(self, organization_id=None, organization_name=None):
        organization_id = get_organization_id_from_arguments(contxt_service=self.contxt_service,
                                                             organization_id=organization_id,
                                                             organization_name=organization_name)

        asset_service = LazyAssetsService(auth_module=self.auth,
                                          organization_id=organization_id,
                                          environment='staging')

        asset_service.load_configuration()

        return asset_service, organization_id

    def get_asset_types(self, organization_id=None, organization_name=None):

        asset_service, _ = self._initialize_asset_service(organization_id, organization_name)

        return APIObjectCollection(list(asset_service.types_by_label.values()))

    def get_asset_type_info(self, type, organization_id=None, organization_name=None):

        asset_service, _ = self._initialize_asset_service(organization_id, organization_name)

        if type not in asset_service.types_by_label:
            logger.critical(f'Type not found: {type}')
            return None

        type_object = asset_service.types_by_label[type]

        asset_service.load_type_full(type_object)

        return type_object

    def get_assets_for_type(self, type, organization_id=None, organization_name=None):

        asset_service, organization_id = self._initialize_asset_service(organization_id, organization_name)

        asset_type = self.get_asset_type_info(type, organization_id=organization_id)

        assets = asset_service.get_assets_for_type(asset_type)

        return APIObjectCollection(list(assets))

    def get_metric_values_for_asset(self, metric, asset_id, organization_id=None, organization_name=None):

        asset_service, organization_id = self._initialize_asset_service(organization_id, organization_name)

        asset_object = asset_service.fetch_asset_by_id(asset_id)

        asset_service.load_type_metrics(asset_object.asset_type)

        if metric not in asset_object.asset_type.metrics:
            logger.critical("No such metric for asset type")
            return

        metric_object = asset_object.asset_type.metrics[metric]

        metric_values = asset_service.fetch_all_metric_values_for_asset_metric(asset_object, metric_object)

        return metric_object, metric_values

    def get_metric_values_for_asset_type(self,
                                         metric_label,
                                         asset_type_label,
                                         organization_id=None,
                                         organization_name=None,
                                         plot=False):

        asset_service, organization_id = self._initialize_asset_service(
            organization_id, organization_name)

        asset_object = asset_service.fetch_asset_by_id(asset_type_label)

        asset_service.load_type_metrics(asset_object.asset_type)

        # Validate and get asset type name
        if asset_type_label not in asset_service.types_by_label:
            logger.critical(f"Type not found: {asset_type_label}")
            return

        type_object = asset_service.types_by_label[asset_type_label]

        # Validate and get metric name
        asset_service.load_type_metrics(type_object)
        if metric_label not in type_object.metrics:
            logger.critical(f"Metric not found: {metric_label}")
            return

        metric = asset_service.asset_metric_with_label(type_object,
                                                       metric_label)

        # Fetch all metric values for metric
        # TODO: can be very slow
        logger.info(f'Fetching {asset_type_label} asset types')
        assets = asset_service.get_assets_for_type(type_object)
        logger.info(f'Fetching all {metric_label} metric values')
        asset_label_to_metric_values = {
            a.label: asset_service.fetch_all_metric_values_for_asset_metric(
                a, metric)
            for a in tqdm(assets)
        }

        if plot:
            self.plot_asset_metrics(asset_label_to_metric_values, metric_label)

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
