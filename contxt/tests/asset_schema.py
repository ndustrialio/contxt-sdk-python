from contxt.services.asset_migration import AssetSchema
from contxt.services.asset_models import (Asset, AssetType, Attribute,
                                          AttributeValue, DataTypes, Metric,
                                          MetricValue, TimeIntervals)


def get_test_schema(organization_id):
    asset_types = [
        AssetType(
            label="TestParentType",
            description="Test description",
            organization_id=organization_id,
            asset_attributes=[
                Attribute(
                    asset_type_id=None,
                    label="test_attr_label",
                    description="Test description",
                    units="?",
                    organization_id=organization_id,
                    data_type=DataTypes.string,
                    is_required=False)
            ],
            asset_metrics=[
                Metric(
                    asset_type_id=None,
                    label="test_met_label",
                    description="Test description",
                    organization_id=organization_id,
                    time_interval=TimeIntervals.weekly,
                    units="?")
            ],
            children=[
                AssetType(
                    label="TestChildType",
                    description="Test description",
                    organization_id=organization_id)
            ])
    ]
    assets = [
        Asset(
            asset_type_id=None,
            label="TestAsset",
            description="Test description",
            organization_id=organization_id)
    ]
    return AssetSchema('TestSchema', asset_types, assets)
