import pytest

from contxt.asset_framework_new import AssetFramework
from contxt.services.asset_models import (Asset, AssetType, Attribute,
                                          AttributeValue, DataTypes, Metric,
                                          MetricValue)
from contxt.utils.auth import CLIAuth


@pytest.fixture
def cli_auth():
    return CLIAuth()


@pytest.fixture
def asset_framework(cli_auth: CLIAuth,
                    organization_id="02efa741-a96f-4124-a463-ae13a704b8fc"):
    return AssetFramework(cli_auth, organization_id, env="staging", load_all_types=False)

@pytest.fixture
def asset_type(asset_framework):
    asset_type = AssetType(
        label="TestAssetType",
        description="Test description",
        organization_id=asset_framework.organization_id)
    return asset_framework.create_asset_type(asset_type)


class TestAssetFramework:

    def test_asset_type_crud_endpoints(self, asset_framework: AssetFramework):
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
        # Check created type was also cached within the AssetFramework instance
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
        # Check upated type was also cached within the AssetFramework instance
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
        # Check the cached type was also removed from the AssetFramework instance
        assert asset_framework.asset_type_with_id(created_asset_type.id,
                                                  None) is None
        assert asset_framework.asset_type_with_label(created_asset_type.label,
                                                     None) is None
        assert asset_framework.asset_type_with_label(
            created_asset_type.normalized_label, None) is None

    def test_asset_crud_endpoints(self, asset_framework: AssetFramework, asset_type):
        # Test create_asset
        asset = Asset(
            asset_type_id=asset_type.id,
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

        # Delete the test asset_type
        asset_framework.delete_asset_type(asset_type)

    def test_attribute_crud_endpoints(self, asset_framework, asset_type):
        # Test create_attribute
        attribute = Attribute(
            asset_type_id=asset_type.id,
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

        # Delete the test asset_type
        asset_framework.delete_asset_type(asset_type)

    def test_attribute_value_crud_endpoints(self, asset_framework, asset_type):
        pass

    def test_metric_crud_endpoints(self, asset_framework, asset_type):
        pass
    
    def test_metric_value_crud_endpoints(self, asset_framework, asset_type):
        pass
