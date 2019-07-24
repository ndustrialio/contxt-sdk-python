import pandas as pd
from tqdm import tqdm

from contxt.functions.organizations import get_organization_id_from_arguments
from contxt.legacy.services import APIObjectCollection
from contxt.legacy.services.asset_framework import (
    LazyAssetsService,
    datetime_zulu_parse,
)
from contxt.services.contxt import ContxtService
from contxt.utils import make_logger
from contxt.utils.vis import DataVisualizer

logger = make_logger(__name__)


class Assets:
    def __init__(self, auth_module):

        self.auth = auth_module

        self.contxt_service = ContxtService(self.auth)

    def initialize_asset_service(self, organization_id=None, organization_name=None):
        organization_id = get_organization_id_from_arguments(
            contxt_service=self.contxt_service,
            organization_id=organization_id,
            organization_name=organization_name,
        )

        asset_service = LazyAssetsService(
            auth_module=self.auth,
            organization_id=organization_id,
            environment="production",
        )

        asset_service.load_configuration()

        return asset_service, organization_id

    def get_asset_types(self, organization_id=None, organization_name=None):

        asset_service, _ = self.initialize_asset_service(
            organization_id, organization_name
        )

        return APIObjectCollection(list(asset_service.types_by_label.values()))

    def get_asset_type_info(self, type, organization_id=None, organization_name=None):

        asset_service, _ = self.initialize_asset_service(
            organization_id, organization_name
        )

        if type not in asset_service.types_by_label:
            logger.critical(f"Type not found: {type}")
            return None

        type_object = asset_service.types_by_label[type]

        asset_service.load_type_full(type_object)

        return type_object

    def get_assets_for_type(self, type, organization_id=None, organization_name=None):

        asset_service, organization_id = self.initialize_asset_service(
            organization_id, organization_name
        )

        asset_type = self.get_asset_type_info(type, organization_id=organization_id)

        assets = asset_service.get_assets_for_type(asset_type)

        return APIObjectCollection(list(assets))

    def get_metric_values_for_asset(
        self,
        metric,
        asset_id,
        organization_id=None,
        organization_name=None,
        asset_instance=None,
    ):

        if asset_instance is None:
            asset_service, _ = self.initialize_asset_service(
                organization_id, organization_name
            )
        else:
            asset_service = asset_instance

        asset_object = asset_service.fetch_asset_by_id(asset_id)

        asset_service.load_type_full(asset_object.asset_type)

        if metric not in asset_object.asset_type.metrics:
            logger.critical("No such metric for asset type")
            return

        metric_object = asset_object.asset_type.metrics[metric]

        metric_values = asset_service.fetch_all_metric_values_for_asset_metric(
            asset_object, metric_object
        )

        return metric_object, metric_values

    def get_asset_info(
        self,
        asset_id,
        organization_id=None,
        organization_name=None,
        asset_instance=None,
    ):

        if asset_instance is None:
            asset_service, _ = self.initialize_asset_service(
                organization_id, organization_name
            )
        else:
            asset_service = asset_instance

        asset_object = asset_service.fetch_asset_by_id(asset_id)

        asset_service.load_type_full(asset_object.asset_type)

        return asset_object

    def get_metric_values_for_asset_type(
        self,
        asset_type_label,
        metric_label,
        organization_id=None,
        organization_name=None,
        plot=False,
        asset_instance=None,
    ):

        if asset_instance is None:
            asset_service, _ = self.initialize_asset_service(
                organization_id, organization_name
            )
        else:
            asset_service = asset_instance

        # Validate and get asset type name
        if asset_type_label not in asset_service.types_by_label:
            logger.critical(f"Type not found: {asset_type_label}")
            return

        type_object = asset_service.asset_type_with_label(asset_type_label)

        # Validate and get metric name
        asset_service.load_type_metrics(type_object)
        if metric_label not in type_object.metrics:
            logger.critical(f"Metric not found: {metric_label}")
            return

        metric = asset_service.asset_metric_with_label(type_object, metric_label)

        # Fetch all metric values for metric
        # TODO: can be very slow
        logger.info(f"Fetching {asset_type_label} asset types")
        assets = asset_service.get_assets_for_type(type_object)
        logger.info(f"Fetching all {metric_label} metric values")
        asset_label_to_metric_values = {
            a.label: asset_service.fetch_all_metric_values_for_asset_metric(a, metric)
            for a in tqdm(assets)
        }

        if plot:
            self.plot_multi_asset_metrics({metric_label: asset_label_to_metric_values})

        return asset_label_to_metric_values

    def compare_metric_values_for_asset_type(
        self,
        asset_type_label,
        metric_labels,
        organization_id=None,
        organization_name=None,
        plot=False,
    ):
        metric_labels_to_asset_labels_to_values = {}
        # TODO: this reloads the same assets service on each call
        for metric_label in metric_labels:
            metric_labels_to_asset_labels_to_values[
                metric_label
            ] = self.get_metric_values_for_asset_type(
                asset_type_label=asset_type_label,
                metric_label=metric_label,
                organization_id=organization_id,
                organization_name=organization_name,
                plot=False,
            )

        if plot:
            self.plot_multi_asset_metrics(metric_labels_to_asset_labels_to_values)

        return metric_labels_to_asset_labels_to_values

    # TODO: fix this nested dictionary argument to something more elegant
    def plot_multi_asset_metrics(self, metric_labels_to_asset_labels_to_values):
        def create_df(metric_values):
            filtered_dicts = []
            for mv in metric_values:
                filtered_dicts.extend(
                    [
                        {
                            "x": datetime_zulu_parse(mv.effective_start_date),
                            "y": float(mv.value),
                        },
                        {
                            "x": datetime_zulu_parse(mv.effective_end_date),
                            "y": float(mv.value),
                        },
                    ]
                )
            return pd.DataFrame(filtered_dicts)

        data_vis = DataVisualizer(multi_plots=True)

        # Create graphs
        labeled_graphs = {
            f"{a}'s {m}": data_vis._create_scatter_plot(
                df=create_df(v),
                x_label="x",
                y_label="y",
                name=f"{a}'s {m}",
                line=dict(shape="spline"),
            )
            for m, d in metric_labels_to_asset_labels_to_values.items()
            for a, v in d.items()
        }

        # Plot
        data_vis.run(labeled_graphs)

    def get_asset_tree(self, asset_id, organization_id=None, organization_name=None):
        asset_service, organization_id = self._initialize_asset_service(
            organization_id, organization_name
        )

        return asset_service.get_asset_tree_by_id(asset_id).root
