from typing import Dict, List, Optional, Set, Tuple

from contxt.services.api import ApiService
from contxt.services.asset_models import (Asset, AssetType, Attribute,
                                          AttributeValue, CompleteAsset,
                                          DataTypes, Metric, MetricValue,
                                          TimeIntervals)
from contxt.utils import make_logger
from contxt.utils.auth.cli import CLIAuth

logger = make_logger(__name__)


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
            load_types: bool = True,
            types_to_fully_load: Optional[List[str]] = None,
    ):
        config = self._init_config(env)
        access_token = auth.get_token_for_audience(config['audience'])
        super().__init__(config['base_url'], access_token)
        # TODO: handle multiple orgs
        self.organization_id = organization_id
        self.types = {}
        self.types_by_id = {}

        # Cache asset types
        if load_types:
            full_types = types_to_fully_load or []
            for asset_type in self.get_asset_types(self.organization_id):
                # if not asset_type.is_global:
                if asset_type.label in full_types or asset_type.normalized_label in full_types:
                    self._cache_asset_type_full(asset_type)
                else:
                    self._cache_asset_type(asset_type)

        if self.types_by_id:
            logger.info(
                f"Cached asset types {[at.label for at in self.types_by_id.values()]}"
            )

    def _init_config(self, env: str, default=__marker):
        if env not in self.configs_by_env:
            if default is self.__marker:
                raise KeyError(
                    f"Invalid environment '{env}'. Expected one of {', '.join(self.configs_by_env.keys())}."
                )
            return default
        return self.configs_by_env[env]

    def _cache_asset_type(self, asset_type: AssetType):
        # TODO: should we replace label with normalized label?
        self.types_by_id[asset_type.id] = asset_type
        self.types[asset_type.label] = asset_type
        self.types[asset_type.normalized_label] = asset_type

    def _uncache_asset_type(self, asset_type: AssetType):
        self.types_by_id.pop(asset_type.id)
        self.types.pop(asset_type.label)
        self.types.pop(asset_type.normalized_label, None)

    def _cache_asset_type_full(self, asset_type: AssetType):
        self._cache_asset_type(asset_type)
        self._cache_attributes(asset_type)
        self._cache_metrics(asset_type)

    def _cache_attributes(self, asset_type: AssetType):
        if not asset_type.attributes:
            logger.info(f"Caching attributes for asset_type {asset_type.label}")
            asset_type.attributes = self.get_attributes(asset_type.id)

    def _cache_metrics(self, asset_type: AssetType):
        if not asset_type.metrics:
            logger.info(f"Caching metrics for asset_type {asset_type.label}")
            asset_type.metrics = self.get_metrics(asset_type.id)

    def asset_type_with_id(self, asset_type_id: str,
                           default=__marker) -> AssetType:
        if asset_type_id not in self.types_by_id:
            if default is self.__marker:
                raise KeyError(f"Asset type {asset_type_id} not found.")
            return default
        return self.types_by_id[asset_type_id]

    def asset_type_with_label(self, asset_type_label: str,
                              default=__marker) -> AssetType:
        if asset_type_label not in self.types:
            if default is self.__marker:
                raise KeyError(f"Asset type {asset_type_label} not found.")
            return default
        return self.types[asset_type_label]

    # Abstractions
    def get_complete_asset(self, asset_id: str):
        """High-level abstraction of an asset, complete with attributes,
        attribute values, metrics, and metric values."""
        asset = self.get_asset(asset_id, with_metric_values=True)
        asset_type = self.asset_type_with_id(asset.asset_type_id)
        return CompleteAsset(asset, asset_type)

    def sync_complete_asset(self, asset: CompleteAsset):
        """Push any changes to the abstracted CompleteAsset to the Asset
        Framework API """
        # Update attribute values
        # TODO: probably better to do a set calculation here instead of
        # multiple list comprehensions
        attribute_values_to_create = [
            v for v in asset.edited_attribute_values if v.id is None
        ]
        attribute_values_to_update = [
            v for v in asset.edited_attribute_values
            if v.id is not None and v.value is not None
        ]
        attribute_values_to_delete = [
            v for v in asset.edited_attribute_values
            if v.id is not None and v.value is None
        ]
        self.create_attribute_values(attribute_values_to_create)
        self.update_attribute_values(attribute_values_to_update)
        self.delete_attribute_values(attribute_values_to_delete)
        asset.edited_attribute_values.clear()

        # Update metric values
        metric_values_to_create = [
            v for v in asset.edited_metric_values if v.id is None
        ]
        metric_values_to_update = [
            v for v in asset.edited_metric_values
            if v.id is not None and v.value is not None
        ]
        metric_values_to_delete = [
            v for v in asset.edited_metric_values
            if v.id is not None and v.value is None
        ]
        self.create_metric_values(metric_values_to_create)
        self.update_metric_values(metric_values_to_update)
        self.delete_metric_values(metric_values_to_delete)
        asset.edited_metric_values.clear()

    # Single asset types
    def create_asset_type(self, asset_type: AssetType) -> AssetType:
        data = asset_type.post()
        logger.debug(f"Creating asset_type with {data}")
        new_asset_type = AssetType(**self.post("assets/types", data=data))
        self._cache_asset_type(new_asset_type)
        return new_asset_type

    def get_asset_type(self, asset_type_id: str) -> AssetType:
        logger.debug(f"Fetching asset_type {asset_type_id}")
        return AssetType(**self.get(f"assets/types/{asset_type_id}"))

    def update_asset_type(self, asset_type: AssetType) -> None:
        data = asset_type.put()
        logger.debug(f"Updating asset_type {asset_type.id} with {data}")
        self.put(f"assets/types/{asset_type.id}", data=data)

    def delete_asset_type(self, asset_type: AssetType) -> None:
        logger.debug(f"Deleting asset_type {asset_type.id}")
        self.delete(f"assets/types/{asset_type.id}")
        self._uncache_asset_type(asset_type)

    # Batch asset types
    def create_asset_types(self,
                           asset_types: List[AssetType]) -> List[AssetType]:
        # TODO: batch create
        logger.debug(f"Creating {len(asset_types)} asset_types")
        return [
            self.create_asset_type(asset_type) for asset_type in asset_types
        ]

    def get_asset_types(self, organization_id: Optional[str] = None) -> List[AssetType]:
        if organization_id:
            logger.debug(
                f"Fetching asset_types for organization {organization_id}")
            return [
                AssetType(**rec) for rec in self.get(
                    f"organizations/{organization_id}/assets/types")
            ]
        else:
            logger.debug(f"Fetching asset_types")
            return [AssetType(**rec) for rec in self.get(f"assets/types")]

    def update_asset_types(self, asset_types: List[AssetType]) -> None:
        # TODO: batch update
        logger.debug(f"Updating {len(asset_types)} asset_types")
        for asset_type in asset_types:
            self.update_asset_type(asset_type)

    def delete_asset_types(self, asset_types: List[AssetType]) -> None:
        # TODO: batch delete
        logger.debug(f"Deleting {len(asset_types)} asset_types")
        for asset_type in asset_types:
            self.delete_asset_type(asset_type)

    # Single asset
    def create_asset(self, asset: Asset) -> Asset:
        data = asset.post()
        logger.debug(f"Creating asset with {data}")
        return Asset(**self.post("assets", data=data))

    def get_asset(self,
                  asset_id: str,
                  with_attribute_values=True,
                  with_metric_values=False) -> Asset:
        logger.debug(f"Fetching asset {asset_id}")
        metric_values = self.get_metric_values(asset_id) if with_metric_values else None
        return Asset(**self.get(f"assets/{asset_id}"), asset_metric_values=metric_values)

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
        logger.debug(f"Creating {len(assets)} assets")
        return [self.create_asset(asset) for asset in assets]

    def get_assets(self) -> List[Asset]:
        logger.debug(f"Fetching assets")
        return [Asset(**rec) for rec in self.get("assets")]

    def get_assets_for_organization(
            self,
            organization_id: str,
            asset_type_id: Optional[str] = None,
    ) -> List[Asset]:
        # BUG: this endpoint returns globals when type_id is None
        # TODO: we can add asset_attribute_id and asset_attribute_value as params
        logger.debug(
            f"Fetching assets for organization {organization_id} and asset_type {asset_type_id}"
        )
        return [
            Asset(**rec) for rec in self.get(
                f"organizations/{organization_id}/assets",
                params={"asset_type_id": asset_type_id})
        ]

    def update_assets(self, assets: List[Asset]) -> None:
        # TODO: batch update
        logger.debug(f"Updating {len(assets)} assets")
        for asset in assets:
            self.update_asset(asset)

    def delete_assets(self, assets: List[Asset]) -> None:
        # TODO: batch delete
        logger.debug(f"Deleting {len(assets)} assets")
        for asset in assets:
            self.delete_asset(asset)

    # Single attribute
    def create_attribute(self, attribute: Attribute) -> Attribute:
        data = attribute.post()
        logger.debug(f"Creating attribute with {data}")
        return Attribute(**self.post(
            f"assets/types/{attribute.asset_type_id}/attributes", data=data))

    def get_attribute(self, attribute_id: str) -> Attribute:
        logger.debug(f"Fetching attribute {attribute_id}")
        return Attribute(**self.get(f"assets/attributes/{attribute_id}"))

    def update_attribute(self, attribute: Attribute) -> None:
        data = attribute.put()
        logger.debug(f"Updating attribute {attribute.id} with {data}")
        self.put(f"assets/attributes/{attribute.id}", data=data)

    def delete_attribute(self, attribute: Attribute) -> None:
        logger.debug(f"Deleting attribute {attribute.id}")
        self.delete(f"assets/attributes/{attribute.id}")

    # Batch attributes
    def create_attributes(self,
                          attributes: List[Attribute]) -> List[Attribute]:
        # TODO: batch create
        logger.debug(f"Creating {len(attributes)} attributes")
        return [self.create_attribute(attribute) for attribute in attributes]

    def get_attributes(self, asset_type_id: str) -> List[Attribute]:
        logger.debug(f"Fetching attributes for asset_type {asset_type_id}")
        return [
            Attribute(**rec)
            for rec in self.get(f"assets/types/{asset_type_id}/attributes")
        ]

    def update_attributes(self, attributes: List[Attribute]) -> None:
        # TODO: batch update
        logger.debug(f"Updating {len(attributes)} attributes")
        for attribute in attributes:
            self.update_attribute(attribute)

    def delete_attributes(self, attributes: List[Attribute]) -> None:
        # TODO: batch delete
        logger.debug(f"Deleting {len(attributes)} attributes")
        for attribute in attributes:
            self.delete_attribute(attribute)

    # Single attribute value
    def create_attribute_value(
            self, attribute_value: AttributeValue) -> AttributeValue:
        # TODO: why do we need both ids?
        data = attribute_value.post()
        logger.debug(f"Creating attribute_value with {data}")
        return AttributeValue(**self.post(
            f"assets/{attribute_value.asset_id}/attributes/{attribute_value.asset_attribute_id}/values",
            data=data))

    # TODO: this endpoint does not exist
    # def get_attribute_value(self, attribute_value_id: str) -> AttributeValue:
    #     logger.debug(f"Fetching attribute_value {attribute_value_id}")
    #     return AttributeValue(
    #         **self.get(f"assets/attributes/values/{attribute_value_id}"))

    def get_attribute_value(self, attribute_value: AttributeValue) -> AttributeValue:
        # HACK: work around since you cannot fetch a single attribute value
        logger.debug(f"Fetching attribute_value {attribute_value.id}")
        attribute_values = self.get_attribute_values(attribute_value.asset_id)
        for value in attribute_values:
            if attribute_value.id == value.id:
                return value
        return None

    def update_attribute_value(self, attribute_value: AttributeValue) -> None:
        data = attribute_value.put()
        logger.debug(f"Updating attribute_value {attribute_value.id} with {data}")
        self.put(f"assets/attributes/values/{attribute_value.id}", data=data)

    def delete_attribute_value(self, attribute_value: AttributeValue) -> None:
        logger.debug(f"Deleting attribute_value {attribute_value.id}")
        self.delete(f"assets/attributes/values/{attribute_value.id}")

    # Batch attribute values
    def create_attribute_values(self, attribute_values: List[AttributeValue]
                                ) -> List[AttributeValue]:
        # TODO: batch create
        logger.debug(f"Creating {len(attribute_values)} attribute_values")
        return [
            self.create_attribute_value(attribute_value)
            for attribute_value in attribute_values
        ]

    def get_attribute_values(self, asset_id: str) -> List[AttributeValue]:
        # TODO: can pass attribute label
        # TODO: clean this up
        # https://contxt.readme.io/v1.0/reference#get-effective-values-by-asset-id
        # https://contxt.readme.io/v1.0/reference#get-values-by-attribute-id
        logger.debug(f"Fetching attribute_values for asset {asset_id}")
        return [
            AttributeValue(**rec)
            for rec in self.get(f"assets/{asset_id}/attributes/values")
        ]

    def update_attribute_values(
            self, attribute_values: List[AttributeValue]) -> None:
        # TODO: batch update
        logger.debug(f"Updating {len(attribute_values)} attribute_values")
        for attribute_value in attribute_values:
            self.update_attribute_value(attribute_value)

    def delete_attribute_values(
            self, attribute_values: List[AttributeValue]) -> None:
        # TODO: batch delete
        logger.debug(f"Deleting {len(attribute_values)} attribute_values")
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
        logger.debug(f"Updating metric {metric.id} with {data}")
        self.put(f"assets/metrics/{metric.id}", data=data)

    def delete_metric(self, metric: Metric) -> None:
        logger.debug(f"Deleting metric {metric.id}")
        self.delete(f"assets/metrics/{metric.id}")

    # Batch metrics
    def create_metrics(self, metrics: List[Metric]) -> List[Metric]:
        # TODO: batch create
        logger.debug(f"Creating {len(metrics)} metrics")
        return [self.create_metric(metric_value) for metric_value in metrics]

    def get_metrics(self, asset_type_id: str) -> List[Metric]:
        logger.debug(f"Fetching metrics for asset_type {asset_type_id}")
        return [
            Metric(**rec)
            for rec in self.get(f"assets/types/{asset_type_id}/metrics")
        ]

    def update_metrics(self, metrics: List[Metric]) -> None:
        # TODO: batch update
        logger.debug(f"Updating {len(metrics)} metrics")
        for metric in metrics:
            self.update_metric(metric)

    def delete_metrics(self, metrics: List[Metric]) -> None:
        # TODO: batch delete
        logger.debug(f"Deleting {len(metrics)} metrics")
        for metric in metrics:
            self.delete_metric(metric)

    # Single metric value
    def create_metric_value(self, metric_value: MetricValue) -> MetricValue:
        # TODO: why do we need both ids?
        data = metric_value.post()
        logger.debug(f"Creating metric_value with {data}")
        return MetricValue(**self.post(
            f"assets/{metric_value.asset_id}/metrics/{metric_value.asset_metric_id}/values",
            data=data))

    # TODO: this endpoint does not exist
    # def get_metric_value(self, metric_value_id: str) -> MetricValue:
    #     logger.debug(f"Fetching metric_value {metric_value_id}")
    #     return MetricValue(**self.get(f"assets/metrics/values/{metric_value_id}"))

    def get_metric_value(self, metric_value: MetricValue) -> MetricValue:
        # HACK: work around since you cannot fetch a single metric value
        logger.debug(f"Fetching metric_value {metric_value.id}")
        metric_values = self.get_metric_values(metric_value.asset_id, metric_value.asset_metric_id)
        for value in metric_values:
            if metric_value.id == value.id:
                return value
        return None

    def update_metric_value(self, metric_value: MetricValue) -> None:
        data = metric_value.put()
        logger.debug(f"Updating metric_value {metric_value.id} with {data}")
        self.put(f"assets/metrics/values/{metric_value.id}", data=data)

    def delete_metric_value(self, metric_value: MetricValue) -> None:
        logger.debug(f"Deleting metric {metric_value.id}")
        self.delete(f"assets/metrics/values/{metric_value.id}")

    # Batch metric values
    def create_metric_values(
            self, metric_values: List[MetricValue]) -> List[MetricValue]:
        # TODO: batch create
        logger.debug(f"Creating {len(metric_values)} metric_values")
        return [
            self.create_metric_value(metric_value)
            for metric_value in metric_values
        ]

    def get_metric_values(self, asset_id: str,
                          metric_id: Optional[str] = None) -> List[MetricValue]:
        # TODO: why do we need both ids?
        if metric_id:
            logger.debug(
                f"Fetching metric_values for asset {asset_id} and metric {metric_id}"
            )
            return [
                MetricValue(**rec, asset=rec['Asset']) for rec in self.get(
                    f"assets/{asset_id}/metrics/{metric_id}/values")
            ]
        else:
            logger.debug(f"Fetching metric_values for asset {asset_id}")
            return [
                MetricValue(**rec, asset=rec['Asset'])
                for rec in self.get(f"assets/{asset_id}/metrics/values")
            ]

    def update_metric_values(self, metric_values: List[MetricValue]) -> None:
        # TODO: batch update
        logger.debug(f"Updating {len(metric_values)} metric_values")
        for metric_value in metric_values:
            self.update_metric_value(metric_value)

    def delete_metric_values(self, metric_values: List[MetricValue]) -> None:
        # TODO: batch delete
        logger.debug(f"Deleting {len(metric_values)} metric_values")
        for metric_value in metric_values:
            self.delete_metric_value(metric_value)


if __name__ == "__main__":
    auth = CLIAuth()
    organization_id = "02efa741-a96f-4124-a463-ae13a704b8fc"
    af = AssetFramework(
        auth,
        organization_id,
        env='staging',
        load_types=True,
        types_to_fully_load=['UtilityMeter'])
    asset_framework = af

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
