from datetime import date, datetime, timedelta

import pytest
from pytz import UTC

from contxt.auth import CliAuth
from contxt.models.assets import (Asset, AssetType, Attribute, AttributeValue,
                                  DataTypes, Metric, MetricValue,
                                  TimeIntervals)
from contxt.services.assets import AssetsService
from contxt.utils.assets_migration import AssetMigrationManager, AssetSchema
from tests.static.asset_schema import AssetSchemas


def init_schema():
    organization_id = "02efa741-a96f-4124-a463-ae13a704b8fc"
    asset_framework = AssetsService(
        auth=CliAuth(),
        organization_id=organization_id,
        env="staging",
        load_types=True)
    schemas = AssetSchemas(asset_framework.organization_id)
    test_schema = schemas.get('TestSchema')
    migrator = AssetMigrationManager(asset_framework, test_schema)
    migrator.create()
    # Create an asset
    asset_type = asset_framework.asset_type_with_label("TestParentType")
    asset = Asset(
        asset_type_id=asset_type.id,
        label="Test Asset",
        description="Test asset description",
        organization_id=asset_framework.organization_id)
    # HACK: return the test asset until we incorporate assets into the schema
    new_asset = asset_framework.create_asset(asset)
    asset_framework._cache_attributes(asset_type)
    return new_asset


# Create test schema
TEST_ASSET = init_schema()


@pytest.fixture
def cli_auth():
    return CliAuth()


@pytest.fixture
def asset_framework(cli_auth: CliAuth,
                    organization_id="02efa741-a96f-4124-a463-ae13a704b8fc"):
    return AssetsService(cli_auth, organization_id, env="staging", load_types=True, types_to_fully_load=['TestParentType'])


@pytest.fixture
def parent_asset_type(asset_framework):
    return asset_framework.asset_type_with_label("TestParentType")


@pytest.fixture
def child_asset_type(asset_framework):
    return asset_framework.asset_type_with_label("TestChildType")


@pytest.fixture
def attribute(asset_framework: AssetsService):
    return asset_framework.asset_type_with_label("TestParentType").attribute_with_label("test_attr_label")


@pytest.fixture
def metric(asset_framework: AssetsService):
    return asset_framework.asset_type_with_label(
        "TestParentType").metric_with_label("test_met_label")


# TODO: need to split these tests up, and test for errors, globals, different orgs
class TestAssetsService:

    def test_asset_type_crud_endpoints(self, asset_framework: AssetsService):
        """Test create, retrieve, update, and delete asset_type"""
        # Test create_asset_type
        asset_type = AssetType(
            label="TestAssetType",
            description="Test description",
            organization_id=asset_framework.organization_id)
        created_asset_type = asset_framework.create_asset_type(asset_type)
        # Check created type has the same fields
        assert created_asset_type.label == asset_type.label
        assert created_asset_type.description == asset_type.description
        assert created_asset_type.organization_id == asset_type.organization_id
        # Check created type was also cached within the AssetsService instance
        assert asset_framework.asset_type_with_id(created_asset_type.id) == created_asset_type
        assert asset_framework.asset_type_with_label(created_asset_type.label) == created_asset_type
        assert asset_framework.asset_type_with_label(
            created_asset_type.normalized_label) == created_asset_type

        # Test update_asset_type
        created_asset_type.description = "Test new description"
        asset_framework.update_asset_type(created_asset_type)
        updated_asset_type = asset_framework.get_asset_type(
            created_asset_type.id)
        # Check the field was updated
        assert updated_asset_type.description == created_asset_type.description
        # Check upated type was also cached within the AssetsService instance
        assert asset_framework.asset_type_with_id(
            created_asset_type.id) == created_asset_type
        assert asset_framework.asset_type_with_label(
            created_asset_type.label) == created_asset_type
        assert asset_framework.asset_type_with_label(
            created_asset_type.normalized_label) == created_asset_type

        # Test delete_asset_type
        asset_framework.delete_asset_type(updated_asset_type)
        # Check the asset type was actually deleted
        with pytest.raises(Exception) as e:
            asset_framework.get_asset_type(updated_asset_type.id)
        # Check the cached type was also removed from the AssetsService instance
        assert asset_framework.asset_type_with_id(created_asset_type.id,
                                                  None) is None
        assert asset_framework.asset_type_with_label(created_asset_type.label,
                                                     None) is None
        assert asset_framework.asset_type_with_label(
            created_asset_type.normalized_label, None) is None

    def test_asset_crud_endpoints(self, asset_framework: AssetsService, child_asset_type):
        """Test create, retrieve, update, and delete asset"""
        # Test create_asset
        asset = Asset(
            asset_type_id=child_asset_type.id,
            label="Test asset label",
            description="Test asset description",
            organization_id=asset_framework.organization_id)

        created_asset = asset_framework.create_asset(asset)
        # Check created asset has the same fields
        assert created_asset.asset_type_id == asset.asset_type_id
        assert created_asset.label == asset.label
        assert created_asset.description == asset.description
        assert created_asset.organization_id == asset.organization_id
        assert created_asset.parent_id == asset.parent_id

        # Test update_asset and get_asset
        created_asset.description = "Test new description"
        asset_framework.update_asset(created_asset)
        updated_asset = asset_framework.get_asset(created_asset.id)
        # Check the field was updated
        assert updated_asset.description == created_asset.description

        # Test delete_asset
        asset_framework.delete_asset(updated_asset)
        # Check the asset was actually deleted
        with pytest.raises(Exception) as e:
            asset_framework.get_asset(updated_asset.id)

    def test_attribute_crud_endpoints(self, asset_framework, parent_asset_type):
        """Test create, retrieve, update, and delete attribute"""
        # Test create_attribute
        attribute = Attribute(
            asset_type_id=parent_asset_type.id,
            label="test_attribute_label",
            description="test attribute description",
            units="?",
            organization_id=asset_framework.organization_id,
            is_required=False,
            data_type=DataTypes.string)
        created_attribute = asset_framework.create_attribute(attribute)
        # Check created asset has the same fields
        assert created_attribute.asset_type_id == attribute.asset_type_id
        assert created_attribute.label == attribute.label
        assert created_attribute.description == attribute.description
        assert created_attribute.units == attribute.units
        assert created_attribute.organization_id == attribute.organization_id
        assert created_attribute.is_required == attribute.is_required
        assert created_attribute.data_type == attribute.data_type

        # Test update_attribute and get_attribute
        created_attribute.label = "edited_test_attribute_label"
        created_attribute.description = "edited test attribute description"
        created_attribute.units = "??"
        created_attribute.is_required = True
        created_attribute.data_type = DataTypes.number
        asset_framework.update_attribute(created_attribute)
        updated_attribute = asset_framework.get_attribute(created_attribute.id)
        assert updated_attribute.label == created_attribute.label
        assert updated_attribute.description == created_attribute.description
        assert updated_attribute.units == created_attribute.units
        assert updated_attribute.is_required == created_attribute.is_required
        assert updated_attribute.data_type == created_attribute.data_type

        # Test delete_asset
        asset_framework.delete_attribute(updated_attribute)
        # Check the asset was actually deleted
        with pytest.raises(Exception) as e:
            asset_framework.get_asset(updated_attribute.id)

    def test_attribute_value_crud_endpoints(self, asset_framework: AssetsService, attribute):
        """Test create, retrieve, update, and delete attribute_value"""
        # TODO: we need a schema that creates assets too
        # Test create_attribute_value
        attribute_value = AttributeValue(
            asset_id=TEST_ASSET.id,
            attribute_id=attribute.id,
            notes="test note",
            value="test_value")
        created_attribute_value = asset_framework.create_attribute_value(
            attribute_value)
        assert created_attribute_value.asset_id == attribute_value.asset_id
        assert created_attribute_value.attribute_id == attribute_value.attribute_id
        assert created_attribute_value.effective_date == attribute_value.effective_date
        assert created_attribute_value.notes == attribute_value.notes
        assert created_attribute_value.value == attribute_value.value

        # Test update_attribute_value and get_attribute_value
        created_attribute_value.notes = "edited test note"
        created_attribute_value.value = "edited test value"
        # created_attribute_value.effective_date = "2018-01-01"
        asset_framework.update_attribute_value(created_attribute_value)
        updated_attribute_value = asset_framework.get_attribute_value(
            created_attribute_value)
        assert updated_attribute_value.notes == created_attribute_value.notes
        assert updated_attribute_value.value == created_attribute_value.value
        # assert updated_attribute_value.effective_date == created_attribute_value.effective_date

        # Test delete_attribute_value
        asset_framework.delete_attribute_value(updated_attribute_value)
        # Check the asset was actually deleted
        assert asset_framework.get_attribute_value(updated_attribute_value) is None
        # with pytest.raises(Exception) as e:
        #     asset_framework.get_attribute_value(updated_attribute_value)

    def test_metric_crud_endpoints(self, asset_framework, parent_asset_type):
        """Test create, retrieve, update, and delete metric"""
        # Test create_metric
        metric = Metric(
            asset_type_id=parent_asset_type.id,
            label="test_label",
            description="Test description",
            organization_id=asset_framework.organization_id,
            time_interval=TimeIntervals.daily,
            units="?")
        created_metric = asset_framework.create_metric(metric)
        # Check created metric has the same fields
        assert created_metric.asset_type_id == metric.asset_type_id
        assert created_metric.label == metric.label
        assert created_metric.description == metric.description
        assert created_metric.organization_id == metric.organization_id
        assert created_metric.time_interval == metric.time_interval
        assert created_metric.units == metric.units

        # Test update_metric and get_metric
        created_metric.label = "edited_test_label"
        created_metric.description = "edited test description"
        created_metric.time_interval = TimeIntervals.weekly
        created_metric.units = "??"
        asset_framework.update_metric(created_metric)
        updated_metric = asset_framework.get_metric(created_metric.id)
        assert updated_metric.label == created_metric.label
        assert updated_metric.description == created_metric.description
        assert updated_metric.time_interval == created_metric.time_interval
        assert updated_metric.units == created_metric.units

        # Test delete_metric
        asset_framework.delete_metric(updated_metric)
        # Check the asset was actually deleted
        with pytest.raises(Exception) as e:
            asset_framework.get_asset(updated_metric.id)

    def test_metric_value_crud_endpoints(self, asset_framework, metric):
        """Test create, retrieve, update, and delete metric_value"""
        # Test create_attribute_value
        # TODO: need an easier way to specify date ranges
        def get_end_date(start_date):
            return start_date + timedelta(weeks=1) - timedelta(milliseconds=1)

        start_date = datetime(2018, 3, 1, tzinfo=UTC)
        metric_value = MetricValue(
            asset_id=TEST_ASSET.id,
            asset_metric_id=metric.id,
            effective_start_date=start_date,
            effective_end_date=get_end_date(start_date),
            notes="test note",
            value=1)
        print(f"WARN: {metric_value.post()}")
        created_metric_value = asset_framework.create_metric_value(
            metric_value)
        assert created_metric_value.asset_id == metric_value.asset_id
        assert created_metric_value.asset_metric_id == metric_value.asset_metric_id
        assert created_metric_value.effective_start_date == metric_value.effective_start_date
        assert created_metric_value.effective_end_date == metric_value.effective_end_date
        assert created_metric_value.notes == metric_value.notes
        assert created_metric_value.value == metric_value.value

        # Test update_metric_value and get_metric_value
        new_start_date = datetime(2018, 3, 8, tzinfo=UTC)
        created_metric_value.effective_start_date = new_start_date
        created_metric_value.effective_end_date = get_end_date(new_start_date)
        created_metric_value.notes = "edited test note"
        created_metric_value.value = 2
        asset_framework.update_metric_value(created_metric_value)
        updated_metric_value = asset_framework.get_metric_value(
            created_metric_value)
        assert updated_metric_value.effective_start_date == created_metric_value.effective_start_date
        assert updated_metric_value.effective_end_date == created_metric_value.effective_end_date
        assert updated_metric_value.notes == created_metric_value.notes
        assert updated_metric_value.value == created_metric_value.value

        # Test delete_metric_value
        asset_framework.delete_metric_value(updated_metric_value)
        # Check the asset was actually deleted
        assert asset_framework.get_metric_value(updated_metric_value) is None


if __name__ == "__main__":
    auth = CliAuth()
    organization_id = "02efa741-a96f-4124-a463-ae13a704b8fc"
    af = AssetsService(auth, organization_id, env="staging")
