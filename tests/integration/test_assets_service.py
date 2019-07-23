from contxt.auth.cli import CliAuth
from contxt.models.assets import (
    Asset,
    AssetType,
    Attribute,
    AttributeValue,
    Metric,
    MetricValue,
)
from contxt.services.assets import AssetsService
from tests.static.data import TestAsset, TestAssetType


class TestAssetsService:
    service = AssetsService(
        auth=CliAuth(),
        organization_id=TestAsset.organization_id,
        load_types=True,
        types_to_fully_load=[TestAssetType.label],
    )

    def test_get_asset_type(self, asset_type_id: str = TestAssetType.id):
        asset_type = self.service.get_asset_type(asset_type_id)
        assert isinstance(asset_type, AssetType)
        assert asset_type.id == asset_type_id

    def test_get_attribute(self, attribute_id: str = TestAssetType.attribute_id):
        attribute = self.service.get_attribute(attribute_id)
        assert isinstance(attribute, Attribute)
        assert attribute.id == attribute_id

    def test_get_metric(self, metric_id: str = TestAssetType.metric_id):
        metric = self.service.get_metric(metric_id)
        assert isinstance(metric, Metric)
        assert metric.id == metric_id

    def test_get_asset(self, asset_id: str = TestAsset.id):
        asset = self.service.get_asset(asset_id)
        assert isinstance(asset, Asset)
        assert asset.id == asset_id
        assert asset.organization_id == self.service.organization_id

    def test_get_attribute_values(self, asset_id: str = TestAsset.id):
        attribute_values = self.service.get_attribute_values(asset_id)
        assert all([isinstance(av, AttributeValue) for av in attribute_values])
        assert all([av.asset_id == asset_id for av in attribute_values])

    def test_get_metric_values(self, asset_id: str = TestAsset.id):
        metric_values = self.service.get_metric_values(asset_id)
        assert all([isinstance(mv, MetricValue) for mv in metric_values])
        assert all([mv.asset_id == asset_id for mv in metric_values])
