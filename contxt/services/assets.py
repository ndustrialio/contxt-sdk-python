from typing import Any, Dict, Iterable, List, Optional

from ..auth import Auth
from ..models.assets import (
    Asset,
    AssetType,
    Attribute,
    AttributeValue,
    CompleteAsset,
    Metric,
    MetricValue,
)
from .api import ApiEnvironment, ConfiguredApi
from .pagination import PagedRecords, PageOptions


class AssetsService(ConfiguredApi):
    """Assets API client"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://facilities.api.ndustrial.io/v1",
            client_id="SgbCopArnGMa9PsRlCVUCVRwxocntlg0",
        ),
        ApiEnvironment(
            name="staging",
            base_url="https://facilities-staging.api.ndustrial.io/v1",
            client_id="xG775XHIOZVUn84seNeHXi0Qe55YuR5w",
        ),
    )

    def __init__(
        self,
        auth: Auth,
        organization_id: Optional[str] = None,
        env: str = "production",
        load_types: bool = True,
        types_to_fully_load: Optional[List[str]] = None,
        **kwargs,
    ) -> None:
        super().__init__(env=env, auth=auth, **kwargs)
        # TODO: handle multiple orgs
        self.organization_id = organization_id
        self.types: Dict[str, AssetType] = {}
        self.types_by_id: Dict[str, AssetType] = {}

        # Cache asset types
        if load_types and organization_id:
            full_types = types_to_fully_load or []
            for asset_type in self.get_asset_types(self.organization_id):
                # if not asset_type.is_global:
                full = asset_type.label in full_types or asset_type.normalized_label in full_types
                self._cache_asset_type(asset_type, with_attributes=full, with_metrics=full)

    def _cache_asset_type(
        self, asset_type: AssetType, with_attributes: bool = False, with_metrics: bool = False
    ) -> None:
        # TODO: should we replace label with normalized label?
        # Store asset_type by id, label, and normalized label
        self.types_by_id[asset_type.id] = asset_type  # type: ignore
        self.types[asset_type.label] = asset_type
        self.types[asset_type.normalized_label] = asset_type

        # Cache attributes/metrics, if requested
        if with_attributes:
            self._cache_attributes(asset_type)
        if with_metrics:
            self._cache_metrics(asset_type)

    def _cache_asset_type_full(self, asset_type: AssetType) -> None:
        # TODO: deprecate this
        self._cache_asset_type(asset_type, with_attributes=True, with_metrics=True)

    def _uncache_asset_type(self, asset_type: AssetType) -> None:
        self.types_by_id.pop(asset_type.id)  # type: ignore
        self.types.pop(asset_type.label)
        self.types.pop(asset_type.normalized_label, None)

    def _cache_attributes(self, asset_type: AssetType) -> None:
        if not asset_type.attributes:
            asset_type.attributes = self.get_attributes(asset_type.id)  # type: ignore

    def _cache_metrics(self, asset_type: AssetType) -> None:
        if not asset_type.metrics:
            asset_type.metrics = self.get_metrics(asset_type.id)  # type: ignore

    def _build_asset(
        self, asset: Asset, with_attribute_values: bool = False, with_metric_values: bool = False
    ) -> Asset:
        # Fetch attribute/metric values, if requested
        if with_attribute_values and not asset.attribute_values:
            asset.attribute_values = self.get_attribute_values(asset.id)  # type: ignore
        if with_metric_values and not asset.metric_values:
            # NOTE: this is a paged response, so fetch all records
            asset.metric_values = [mv for mv in self.get_metric_values(asset.id)]  # type: ignore

        # Attach asset type
        if not asset.asset_type:
            # BUG: sometimes we encounter global types, which we did not load
            # on startup so this lookup fails
            asset.asset_type = self.asset_type_with_id(asset.asset_type_id, None)

        # Repeat for each child
        for child in asset.children or []:
            self._build_asset(
                child, with_attribute_values=with_attribute_values, with_metric_values=with_metric_values
            )

        # TODO: should automatically check if we need to cache any attributes/metrics
        return asset

    def asset_type_with_id(self, asset_type_id: str, default: Any = ...) -> AssetType:
        if asset_type_id not in self.types_by_id:
            if default is ...:
                raise KeyError(f"Asset type {asset_type_id} not found.")
            return default
        return self.types_by_id[asset_type_id]

    def asset_type_with_label(self, asset_type_label: str, default: Any = ...) -> AssetType:
        if asset_type_label not in self.types:
            if default is ...:
                raise KeyError(f"Asset type {asset_type_label} not found.")
            return default
        return self.types[asset_type_label]

    # Abstractions
    def get_complete_asset(self, asset_id: str, with_metric_values: bool = True) -> CompleteAsset:
        """High-level abstraction of an asset, complete with attributes,
        attribute values, metrics, and metric values."""
        asset = self.get_asset(asset_id, with_metric_values=with_metric_values)
        asset_type = self.asset_type_with_id(asset.asset_type_id)
        return CompleteAsset(asset, asset_type)

    def sync_complete_asset(self, asset: CompleteAsset) -> None:
        """Push any changes to the abstracted CompleteAsset to the Asset
        Framework API"""
        # Update attribute values
        # TODO: probably better to do a set calculation here instead of
        # multiple list comprehensions
        attribute_values_to_create = [v for v in asset.edited_attribute_values if v.id is None]
        attribute_values_to_update = [
            v for v in asset.edited_attribute_values if v.id is not None and v.value is not None
        ]
        attribute_values_to_delete = [
            v for v in asset.edited_attribute_values if v.id is not None and v.value is None
        ]
        self.upsert_attribute_values(attribute_values_to_create + attribute_values_to_update)
        self.delete_attribute_values(attribute_values_to_delete)
        asset.edited_attribute_values.clear()

        # Update metric values
        metric_values_to_create = [v for v in asset.edited_metric_values if v.id is None]
        metric_values_to_update = [
            v for v in asset.edited_metric_values if v.id is not None and v.value is not None
        ]
        metric_values_to_delete = [
            v for v in asset.edited_metric_values if v.id is not None and v.value is None
        ]
        self.create_metric_values(metric_values_to_create)
        self.update_metric_values(metric_values_to_update)
        self.delete_metric_values(metric_values_to_delete)
        asset.edited_metric_values.clear()

    # Single asset types
    def create_asset_type(self, asset_type: AssetType) -> AssetType:
        data = asset_type.post()
        resp = self.post("assets/types", data=data)
        new_asset_type = AssetType.from_api(resp)
        self._cache_asset_type(new_asset_type)
        return new_asset_type

    def get_asset_type(self, asset_type_id: str) -> AssetType:
        resp = self.get(f"assets/types/{asset_type_id}")
        return AssetType.from_api(resp)

    def update_asset_type(self, asset_type: AssetType) -> None:
        data = asset_type.put()
        self.put(f"assets/types/{asset_type.id}", data=data)

    def delete_asset_type(self, asset_type: AssetType) -> None:
        self.delete(f"assets/types/{asset_type.id}")
        self._uncache_asset_type(asset_type)

    # Batch asset types
    def create_asset_types(self, asset_types: List[AssetType]) -> List[AssetType]:
        # TODO: batch create
        return [self.create_asset_type(asset_type) for asset_type in asset_types]

    def get_asset_types(
        self, organization_id: Optional[str] = None, page_options: Optional[PageOptions] = None
    ) -> Iterable[AssetType]:
        url = f"organizations/{organization_id}/assets/types" if organization_id else "assets/types"
        return PagedRecords(api=self, url=url, options=page_options, record_parser=AssetType.from_api)

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
        params = {"with_attribute_values": str(bool(asset.attribute_values)).lower()}
        # Create asset with attribute_values, if present
        resp = self.post("assets", params=params, json=data)
        new_asset = Asset.from_api(resp)

        # Fetch attribute_values, if posted (needed because response does not
        # contain them)
        if asset.attribute_values:
            new_asset.attribute_values = self.get_attribute_values(new_asset.id)

        # Create metric_values, if present
        if asset.metric_values:
            for metric_value in asset.metric_values:
                metric_value.asset_id = new_asset.id
            new_asset.metric_values = self.create_metric_values(asset.metric_values)

        # Create children, if present
        if asset.children:
            for child in asset.children:
                child.parent_id = new_asset.id
            new_asset.children = self.create_assets(asset.children)

        return new_asset

    def get_asset(
        self, asset_id: str, with_attribute_values: bool = True, with_metric_values: bool = False
    ) -> Asset:
        resp = self.get(f"assets/{asset_id}")
        return self._build_asset(
            Asset.from_api(resp),
            with_attribute_values=with_attribute_values,
            with_metric_values=with_metric_values,
        )

    def get_asset_with_label(
        self,
        asset_label: str,
        asset_type_label: Optional[str] = None,
        with_attribute_values: bool = True,
        with_metric_values: bool = False,
    ) -> Optional[Asset]:
        asset_type_id = self.asset_type_with_label(asset_type_label).id if asset_type_label else None
        for asset in self.get_assets(asset_type_id=asset_type_id):
            if asset.label.upper() == asset_label.upper():
                return self._build_asset(
                    asset,
                    with_attribute_values=with_attribute_values,
                    with_metric_values=with_metric_values,
                )
        return None

    def get_asset_for_organization_with_label(
        self,
        asset_label: str,
        asset_type_label: Optional[str] = None,
        with_attribute_values: bool = True,
        with_metric_values: bool = False,
    ) -> Optional[Asset]:
        asset_type_id = self.asset_type_with_label(asset_type_label).id if asset_type_label else None
        for asset in self.get_assets_for_organization(asset_type_id=asset_type_id):
            if asset.label.upper() == asset_label.upper():
                return self._build_asset(
                    asset,
                    with_attribute_values=with_attribute_values,
                    with_metric_values=with_metric_values,
                )
        return None

    def update_asset(self, asset: Asset) -> None:
        data = asset.put()
        self.put(f"assets/{asset.id}", data=data)

    def delete_asset(self, asset: Asset) -> None:
        self.delete(f"assets/{asset.id}")

    # Batch assets
    def create_assets(self, assets: List[Asset]) -> List[Asset]:
        # TODO: batch create
        return [self.create_asset(asset) for asset in assets]

    def get_assets(
        self,
        asset_type_id: Optional[str] = None,
        with_attribute_values: bool = False,
        with_metric_values: bool = False,
        page_options: Optional[PageOptions] = None,
    ) -> Iterable[Asset]:
        def _build_asset(record: Dict) -> Asset:
            return self._build_asset(
                Asset.from_api(record),
                with_attribute_values=with_attribute_values,
                with_metric_values=with_metric_values,
            )

        return PagedRecords(
            api=self,
            url="assets",
            params={"asset_type_id": asset_type_id},
            options=page_options,
            record_parser=_build_asset,
        )

    def get_assets_for_organization(
        self,
        asset_type_id: Optional[str] = None,
        attribute_id: Optional[str] = None,
        attribute_value: Optional[str] = None,
        organization_id: Optional[str] = None,
        with_attribute_values: bool = False,
        with_metric_values: bool = False,
        page_options: Optional[PageOptions] = None,
    ) -> Iterable[Asset]:
        # BUG: this endpoint returns globals when type_id is None
        organization_id = organization_id or self.organization_id

        def _build_asset(record: Dict) -> Asset:
            return self._build_asset(
                Asset.from_api(record),
                with_attribute_values=with_attribute_values,
                with_metric_values=with_metric_values,
            )

        return PagedRecords(
            api=self,
            url=f"organizations/{organization_id}/assets",
            params={
                "asset_type_id": asset_type_id,
                "asset_attribute_id": attribute_id,
                "asset_attribute_value": attribute_value,
            },
            options=page_options,
            record_parser=_build_asset,
        )

    def update_assets(self, assets: List[Asset]) -> None:
        # TODO: batch update
        for asset in assets:
            self.update_asset(asset)

    def delete_assets(self, assets: List[Asset]) -> None:
        # TODO: batch delete
        for asset in assets:
            self.delete_asset(asset)

    # Single attribute
    def create_attribute(self, attribute: Attribute) -> Attribute:
        data = attribute.post()
        resp = self.post(f"assets/types/{attribute.asset_type_id}/attributes", data=data)
        return Attribute.from_api(resp)

    def get_attribute(self, attribute_id: str) -> Attribute:
        resp = self.get(f"assets/attributes/{attribute_id}")
        return Attribute.from_api(resp)

    def update_attribute(self, attribute: Attribute) -> None:
        data = attribute.put()
        self.put(f"assets/attributes/{attribute.id}", data=data)

    def delete_attribute(self, attribute: Attribute) -> None:
        self.delete(f"assets/attributes/{attribute.id}")

    # Batch attributes
    def create_attributes(self, attributes: List[Attribute]) -> List[Attribute]:
        # TODO: batch create
        return [self.create_attribute(attribute) for attribute in attributes]

    def get_attributes(
        self, asset_type_id: str, page_options: Optional[PageOptions] = None
    ) -> Iterable[Attribute]:
        return PagedRecords(
            api=self,
            url=f"assets/types/{asset_type_id}/attributes",
            options=page_options,
            record_parser=Attribute.from_api,
        )

    def update_attributes(self, attributes: List[Attribute]) -> None:
        # TODO: batch update
        for attribute in attributes:
            self.update_attribute(attribute)

    def delete_attributes(self, attributes: List[Attribute]) -> None:
        # TODO: batch delete
        for attribute in attributes:
            self.delete_attribute(attribute)

    # Single attribute value
    def create_attribute_value(self, attribute_value: AttributeValue) -> AttributeValue:
        data = attribute_value.post()
        resp = self.post(
            (f"assets/{attribute_value.asset_id}/attributes" f"/{attribute_value.attribute_id}/values"),
            data=data,
        )
        return AttributeValue.from_api(resp)

    def get_attribute_value(self, attribute_value: AttributeValue) -> Optional[AttributeValue]:
        # HACK: work around since you cannot fetch a single attribute value
        attribute_values = self.get_attribute_values(attribute_value.asset_id)
        for value in attribute_values:
            if attribute_value.id == value.id:
                return value
        return None

    def update_attribute_value(self, attribute_value: AttributeValue) -> None:
        data = attribute_value.put()
        self.put(f"assets/attributes/values/{attribute_value.id}", data=data)

    def delete_attribute_value(self, attribute_value: AttributeValue) -> None:
        self.delete(f"assets/attributes/values/{attribute_value.id}")

    # Batch attribute values
    def create_attribute_values(self, attribute_values: List[AttributeValue]) -> List[AttributeValue]:
        # TODO: batch create
        return [self.create_attribute_value(attribute_value) for attribute_value in attribute_values]

    def get_attribute_values(self, asset_id: str) -> List[AttributeValue]:
        return [AttributeValue.from_api(rec) for rec in self.get(f"assets/{asset_id}/attributes/values")]

    def update_attribute_values(self, attribute_values: List[AttributeValue]) -> None:
        # TODO: batch update
        for attribute_value in attribute_values:
            self.update_attribute_value(attribute_value)

    def upsert_attribute_values(self, attribute_values: List[AttributeValue]) -> List[AttributeValue]:
        # Verify list is non-empty
        if not attribute_values:
            return []

        # Verify list contains values of the same asset
        asset_id = attribute_values[0].asset_id
        if not all(asset_id == v.asset_id for v in attribute_values):
            raise ValueError("Endpoint only supports attribute_values belonging to the same asset")

        # Upsert values
        # NOTE: response is [(json: Dict, created?: bool), ...]
        return [
            AttributeValue.from_api(rec[0])
            for rec in self.put(
                f"assets/{asset_id}/attributes/values",
                json={"asset_attribute_values": [v.upsert() for v in attribute_values]},
            )
        ]

    def delete_attribute_values(self, attribute_values: List[AttributeValue]) -> None:
        # TODO: batch delete
        for attribute_value in attribute_values:
            self.delete_attribute_value(attribute_value)

    # Single metric
    def create_metric(self, metric: Metric) -> Metric:
        data = metric.post()
        resp = self.post(f"assets/types/{metric.asset_type_id}/metrics", data=data)
        return Metric.from_api(resp)

    def get_metric(self, metric_id: str) -> Metric:
        resp = self.get(f"assets/metrics/{metric_id}")
        return Metric.from_api(resp)

    def update_metric(self, metric: Metric) -> None:
        data = metric.put()
        self.put(f"assets/metrics/{metric.id}", data=data)

    def delete_metric(self, metric: Metric) -> None:
        self.delete(f"assets/metrics/{metric.id}")

    # Batch metrics
    def create_metrics(self, metrics: List[Metric]) -> List[Metric]:
        # TODO: batch create
        return [self.create_metric(metric_value) for metric_value in metrics]

    def get_metrics(
        self, asset_type_id: str, page_options: Optional[PageOptions] = None
    ) -> Iterable[Metric]:
        return PagedRecords(
            api=self,
            url=f"assets/types/{asset_type_id}/metrics",
            options=page_options,
            record_parser=Metric.from_api,
        )

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
        data = metric_value.post()
        resp = self.post(
            (f"assets/{metric_value.asset_id}/metrics" f"/{metric_value.asset_metric_id}/values"),
            data=data,
        )
        return MetricValue.from_api(resp)

    def get_metric_value(self, metric_value: MetricValue) -> Optional[MetricValue]:
        # HACK: work around since you cannot fetch a single metric value
        metric_values = self.get_metric_values(metric_value.asset_id, metric_value.asset_metric_id)
        for value in metric_values:
            if metric_value.id == value.id:
                return value
        return None

    def update_metric_value(self, metric_value: MetricValue) -> None:
        data = metric_value.put()
        self.put(f"assets/metrics/values/{metric_value.id}", data=data)

    def delete_metric_value(self, metric_value: MetricValue) -> None:
        self.delete(f"assets/metrics/values/{metric_value.id}")

    # Batch metric values
    def create_metric_values(self, metric_values: List[MetricValue]) -> List[MetricValue]:
        # TODO: batch create
        return [self.create_metric_value(metric_value) for metric_value in metric_values]

    def get_metric_values(
        self, asset_id: str, metric_id: Optional[str] = None, page_options: Optional[PageOptions] = None
    ) -> Iterable[MetricValue]:
        url = (
            f"assets/{asset_id}/metrics/{metric_id}/values"
            if metric_id
            else f"assets/{asset_id}/metrics/values"
        )
        return PagedRecords(api=self, url=url, options=page_options, record_parser=MetricValue.from_api)

    def update_metric_values(self, metric_values: List[MetricValue]) -> None:
        # TODO: batch update
        for metric_value in metric_values:
            self.update_metric_value(metric_value)

    def delete_metric_values(self, metric_values: List[MetricValue]) -> None:
        # TODO: batch delete
        for metric_value in metric_values:
            self.delete_metric_value(metric_value)
