from contxt.functions.organizations import get_organization_id_from_arguments

from contxt.utils import make_logger

from contxt.services.asset_framework import LazyAssetsService
from contxt.services import APIObjectCollection
from contxt.services.contxt import ContxtService

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
            logger.critical('Type not found: {}'.format(type))
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
