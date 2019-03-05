import logging
from typing import Dict, List, Optional, Set, Tuple

from contxt.services.api_client import ApiObject, ApiService
from contxt.services.asset_models import (Asset, AssetType, Attribute,
                                          AttributeValue, DataTypes, Metric,
                                          MetricValue, TimeIntervals)
from contxt.utils import make_logger
from contxt.utils.auth import CLIAuth

logger = make_logger(__name__)
logger.setLevel(logging.DEBUG)


# TODO: create a class for this
# class ServiceConfig:

#     def __init__(self, base_url, audience):
#         self.base_url = base_url
#         self.audience = audience


# class ServiceConfigs:

#     def __init__(self, **kwargs):
#         for k, v in kwargs.items():
#             setattr(self, k, v)

#     def config(self, env):
#         c = getattr(self, env, None)
#         if not c:
#             raise KeyError(f"Invalid environment {env}. Expected {CONFIG_BY_ENV.keys()}")
#         return c


class AssetFramework(ApiService):
    configs_by_env = {
        'production':
        dict(
            base_url='https://facilities.api.ndustrial.io',
            audience='SgbCopArnGMa9PsRlCVUCVRwxocntlg0'),
        'staging':
        dict(
            base_url='https://facilities-staging.api.ndustrial.io',
            audience='xG775XHIOZVUn84seNeHXi0Qe55YuR5w')
    }
    __marker = object()

    def __init__(
            self,
            auth: CLIAuth,
            organization_id: str = "02efa741-a96f-4124-a463-ae13a704b8fc",
            env: str = 'production',
            load_all_types: bool = True,
    ):
        config = self._init_config(env)
        access_token = auth.get_token_for_client(config['audience'])
        super().__init__(config['base_url'], access_token)

        # TODO: handle multiple orgs
        self.organization_id = organization_id

        # Optionally load asset types
        self.types_by_id = {}
        self.types_by_label = {}

        if load_all_types:
            for asset_type in self.get_asset_types(self.organization_id):
                # if not asset_type.is_global:
                self._cache_asset_type_with_attributes_and_metrics(asset_type)
                # self._cache_asset_type(asset_type)

        # self._init_asset_type_with_attributes_and_metrics(
        #     self.asset_type_with_label("Facility"))
        if self.types_by_id:
            logger.info(f"Cached asset types {[at.label for at in self.types_by_id.values()]}")

    def _init_config(self, env: str, default=__marker):
        if env not in self.configs_by_env:
            if default is self.__marker:
                raise KeyError(f"Invalid environment '{env}'. Expected one of {', '.join(self.configs_by_env.keys())}.")
            return default
        return self.configs_by_env[env]

    def _cache_asset_type(self, asset_type: AssetType):
        # TODO: should we replace label with normalized label?
        # Store type by id, label, and normalized label
        self.types_by_id[asset_type.id] = asset_type
        self.types_by_label[asset_type.label] = asset_type
        self.types_by_label[asset_type.normalized_label] = asset_type

    def _cache_asset_type_with_attributes_and_metrics(self, asset_type):
        # TODO: clean this up
        self._cache_asset_type(asset_type)
        self._init_attributes(asset_type)
        self._init_metrics(asset_type)

    def _init_attributes(self, asset_type: AssetType):
        if not asset_type.attributes:
            logger.info(f"Fetching attributes for type {asset_type.label}")
            attributes = self.get_attributes(asset_type.id)
            asset_type.set_attributes(attributes)

    def _init_metrics(self, asset_type: AssetType):
        if not asset_type.metrics:
            logger.info(f"Fetching metrics for type {asset_type.label}")
            metrics = self.get_metrics(asset_type.id)
            asset_type.set_metrics(metrics)

    def asset_type_with_id(self, asset_type_id: str,
                           default=__marker) -> AssetType:
        if asset_type_id not in self.types_by_id:
            if default is self.__marker:
                raise KeyError(f"Asset type {asset_type_id} not found.")
            return default
        return self.types_by_id[asset_type_id]

    def asset_type_with_label(self, asset_type_label: str,
                              default=__marker) -> AssetType:
        if asset_type_label not in self.types_by_label:
            if default is self.__marker:
                raise KeyError(f"Asset type {asset_type_label} not found.")
            return default
        return self.types_by_label[asset_type_label]

    # Single asset types
    def create_asset_type(self, asset_type: AssetType) -> AssetType:
        data = asset_type.post()
        logger.debug(f"Creating asset_type with {data}")
        new_asset_type = AssetType(**self.post("assets/types", data=data))
        self._cache_asset_type(new_asset_type)
        return new_asset_type

    def get_asset_type(self, asset_type_id: str) -> AssetType:
        logger.debug(f"Fetching asset types for asset_type_id {asset_type_id}")
        return AssetType(**self.get(f"assets/types/{asset_type_id}"))

    def update_asset_type(self, asset_type: AssetType) -> None:
        data = asset_type.put()
        logger.debug(f"Updating asset_type {asset_type.id} with {data}")
        self.put(f"assets/types/{asset_type.id}", data=data)

    def delete_asset_type(self, asset_type: AssetType) -> None:
        logger.debug(f"Deleting asset_type {asset_type.id}")
        self.delete(f"assets/types/{asset_type.id}")
        # Clear cache
        self.types_by_id.pop(asset_type.id)
        self.types_by_label.pop(asset_type.label)
        self.types_by_label.pop(asset_type.normalized_label, None)

    # Batch asset types
    def create_asset_types(self,
                           asset_types: List[AssetType]) -> List[AssetType]:
        # TODO: batch create
        return [
            self.create_asset_type(asset_type) for asset_type in asset_types
        ]

    def get_asset_types(self, organization_id: str = None) -> List[AssetType]:
        if organization_id:
            logger.debug(
                f"Fetching asset types for organization_id {organization_id}")
            return [
                AssetType(**rec) for rec in self.get(
                    f"organizations/{organization_id}/assets/types")
            ]
        else:
            logger.debug(f"Fetching asset types")
            return [AssetType(**rec) for rec in self.get(f"assets/types")]

    def update_asset_types(self, asset_types: List[AssetType]) -> None:
        # TODO: batch update
        for asset_type in asset_types:
            self.update_asset_type(asset_type)

    def delete_asset_types(self, asset_types: List[AssetType]) -> None:
        # TODO: batch delete
        for asset_type in asset_types:
            self.delete_asset_type(asset_type)

    # Single asset
    def create_asset(self, asset: Asset) -> Asset:
        data = asset.post()
        logger.debug(f"Creating asset with {data}")
        return Asset(**self.post("assets", data=data))

    def get_asset(self, asset_id: str) -> Asset:
        logger.debug(f"Fetching asset {asset_id}")
        return Asset(**self.get(f"assets/{asset_id}"))

    def update_asset(self, asset: Asset) -> None:
        data = asset.put()
        logger.debug(f"Updating asset {asset.id} with {data}")
        self.put(f"assets/{asset.id}", data=data)

    def delete_asset(self, asset: Asset) -> None:
        logger.debug(f"Deleting asset {asset.id}")
        self.delete(f"assets/{asset.id}")

    # Batch assets
    def create_assets(self, assets: List[Asset]) -> List[Asset]:
        # TODO: batch create
        return [self.create_asset(asset) for asset in assets]

    def get_assets(self) -> List[Asset]:
        logger.debug(f"Fetching assets")
        return [Asset(**rec) for rec in self.get("assets")]

    def update_assets(self, assets: List[Asset]) -> None:
        # TODO: batch update
        for asset in assets:
            self.update_asset(asset)

    def delete_assets(self, assets: List[Asset]) -> None:
        # TODO: batch delete
        for asset in assets:
            self.delete_asset(asset)

    def get_assets_for_type(self, asset_type_id: str, organization_id: str) -> List[Asset]:
        logger.debug(
            f"Fetching assets of asset_type_id {asset_type_id} and organization_id {organization_id}"
        )
        return [
            Asset(**rec) for rec in self.get(
                f"/organizations/{organization_id}/assets",
                params={"asset_type_id": asset_type_id})
        ]

    # Single attribute
    def create_attribute(self, attribute: Attribute) -> Attribute:
        data = attribute.post()
        logger.debug(f"Creating attribute with {data}")
        return Attribute(**self.post(f"assets/types/{attribute.asset_type_id}/attributes", data=data))

    def get_attribute(self, attribute_id: str) -> Attribute:
        logger.debug(f"Fetching attribute {attribute_id}")
        return Attribute(**self.get(f"assets/attributes/{attribute_id}"))

    def update_attribute(self, attribute: Attribute) -> None:
        data = attribute.put()
        logger.debug(f"Updating attribute with {data}")
        self.put(f"assets/attributes/{attribute.id}", data=data)

    def delete_attribute(self, attribute: Attribute) -> None:
        logger.debug(f"Deleting attribute {attribute.id}")
        self.delete(f"assets/attributes/{attribute.id}")

    # Batch attributes
    def create_attributes(self, attributes: List[Attribute]) -> List[Attribute]:
        # TODO: batch create
        return [self.create_attribute(attribute) for attribute in attributes]

    def get_attributes(self, asset_type_id: str) -> List[Attribute]:
        logger.debug(f"Fetching attributes for asset_type_id {asset_type_id}")
        return [
            Attribute(**rec)
            for rec in self.get(f"assets/types/{asset_type_id}/attributes")
        ]

    def update_attributes(self, attributes: List[Attribute]) -> None:
        # TODO: batch update
        for attribute in attributes:
            self.update_attribute(attribute)

    def delete_attributes(self, attributes: List[Attribute]) -> None:
        # TODO: batch delete
        for attribute in attributes:
            self.delete_attribute(attribute)

    # Single attribute value
    # TODO: why do we need both ids?
    def create_attribute_value(self, attribute_value: AttributeValue) -> AttributeValue:
        data = attribute_value.post()
        logger.debug(f"Creating attribute_value with {data}")
        return AttributeValue(**self.post(
            f"assets/{attribute_value.asset_id}/attributes/{attribute_value.asset_attribute_id}/values", data=data
        ))

    def get_attribute_value(self, attribute_value_id: str) -> AttributeValue:
        logger.debug(f"Fetching attribute_value {attribute_value_id}")
        return AttributeValue(
            **self.get(f"assets/attribute_values/{attribute_value_id}"))

    def update_attribute_value(self, attribute_value: AttributeValue) -> None:
        data = attribute_value.put()
        logger.debug(f"Updating attribute_value with {data}")
        self.put(f"assets/attributes/values/{attribute_value.id}", data=data)

    def delete_attribute_value(self, attribute_value: AttributeValue) -> None:
        logger.debug(f"Deleting attribute_value {attribute_value.id}")
        self.delete(f"assets/attributes/values/{attribute_value.id}")

    # Batch attribute values
    def create_attribute_values(self, attribute_values: List[AttributeValue]) -> List[AttributeValue]:
        # TODO: batch create
        return [
            self.create_attribute_value(attribute_value)
            for attribute_value in attribute_values
        ]

    def get_attribute_values(self, asset_type_id: str) -> List[AttributeValue]:
        logger.debug(f"Fetching attribute_values for asset_type_id {asset_type_id}")
        raise NotImplementedError

    def update_attribute_values(self, attribute_values: List[AttributeValue]) -> None:
        # TODO: batch update
        for attribute_value in attribute_values:
            self.update_attribute_value(attribute_value)

    def delete_attribute_values(self, attribute_values: List[AttributeValue]) -> None:
        # TODO: batch delete
        for attribute_value in attribute_values:
            self.delete_attribute_value(attribute_value)

    # Single metric
    def create_metric(self, metric: Metric) -> Metric:
        data = metric.post()
        logger.debug(f"Creating metric with {data}")
        return Metric(**self.post(
            f"assets/types/{metric.asset_type_id}/metrics", data=data))

    def get_metric(self, metric_id: str) -> Metric:
        logger.debug(f"Fetching metric {metric_id}")
        return Metric(**self.get(f"assets/metrics/{metric_id}"))

    def update_metric(self, metric: Metric) -> None:
        data = metric.put()
        logger.debug(f"Updating metric with {data}")
        self.put(f"assets/metrics/{metric.id}", data=data)

    def delete_metric(self, metric: Metric) -> None:
        logger.debug(f"Deleting metric {metric.id}")
        self.delete(f"assets/metrics/{metric.id}")

    # Batch metrics
    def create_metrics(self, metrics: List[Metric]) -> List[Metric]:
        # TODO: batch create
        return [self.create_metric(metric) for metric in metrics]

    def get_metrics(self, asset_type_id: str) -> List[Metric]:
        logger.debug(f"Fetching metrics for asset_type_id {asset_type_id}")
        return [Metric(**rec) for rec in self.get(f"assets/types/{asset_type_id}/metrics")]

    def update_metrics(self, metrics: List[Metric]) -> None:
        # TODO: batch update
        for metric in metrics:
            self.update_metric(metric)

    def delete_metrics(self, metrics: List[Metric]) -> None:
        # TODO: batch delete
        for metric in metrics:
            self.delete_metric(metric)

    # Single metric value
    def create_metric_value(self, metric_value: MetricValue) -> MetricValue:
        raise NotImplementedError

    def get_metric_value(self, metric_value_id: str) -> MetricValue:
        raise NotImplementedError

    def update_metric_value(self, metric_value: MetricValue) -> None:
        raise NotImplementedError

    def delete_metric_value(self, metric_value: MetricValue) -> None:
        raise NotImplementedError

    # Batch metric values
    def create_metric_values(self, metric_values: List[MetricValue]) -> List[MetricValue]:
        # TODO: batch create
        return [self.create_metric_value(metric_value) for metric_value in metric_values]

    def get_metric_values(self, asset_id: str, metric_id: str) -> List[MetricValue]:
        # TODO: why do we need to specify both?
        logger.debug(
            f"Fetching metric values for asset_id {asset_id} and metric_id {metric_id}"
        )
        return [
            MetricValue(**rec, asset=rec['Asset']) for rec in self.get(
                f"assets/{asset_id}/metrics/{metric_id}/values")
        ]

    def update_metric_values(self, metric_values: List[MetricValue]) -> None:
        # TODO: batch update
        for metric_value in metric_values:
            self.update_metric_value(metric_value)

    def delete_metric_values(self, metric_values: List[MetricValue]) -> None:
        # TODO: batch delete
        for metric_value in metric_values:
            self.delete_metric_value(metric_value)


if __name__ == "__main__":
    auth = CLIAuth()
    organization_id = "02efa741-a96f-4124-a463-ae13a704b8fc"
    af = AssetFramework(auth, organization_id, env='staging', load_all_types=True)

    # Create metric
    asset_type = af.asset_type_with_label('UtilityMeter')
    metric = Metric(
        asset_type_id=asset_type.id,
        label="test_label",
        description="Test description",
        organization_id="null",
        # organization_id=af.organization_id,
        time_interval=TimeIntervals.daily,
        units="?",
        is_global=True)
    created_metric = af.create_metric(metric)

    # Update metric
    created_metric.label = "updated_label"
    created_metric.description = "updated description"
    created_metric.time_interval = TimeIntervals.weekly
    created_metric.units = "??"
    af.update_metric(created_metric)
    updated_metric = af.get_metric(created_metric.id)

    # Delete metric
    af.delete_metric(updated_metric)

    # Attribute value
    # asset = af.get_asset("8d9ec95e-c574-48f6-ae8d-2eb35e8ae97a")
    # attribute = af.get_attribute("b0446d26-c4e2-4e5d-aa7c-e6f13591f9fc")
    # af.delete_attribute_value(asset.asset_attribute_values[0])
    # attribute = af.get_attribute("8d9ec95e-c574-48f6-ae8d-2eb35e8ae97a")
    # attribute_value = AttributeValue(
    #     asset_id=asset.id,
    #     asset_attribute_id=attribute.id,
    #     notes='Test note',
    #     value=2)
    # at = af.create_attribute_value(attribute_value)
    print("done")
