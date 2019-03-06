from contxt.services.asset_migration import AssetSchema
from contxt.services.asset_models import (Asset, AssetType, Attribute,
                                          AttributeValue, DataTypes, Metric,
                                          MetricValue, TimeIntervals)


class AssetSchemas:

    def __init__(self, organization_id):

        # Build temporary list
        schemas = [
            AssetSchema(
                name='TestSchema',
                asset_types=[
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
                ],
                assets=[
                    # TODO: how to link asset to types, values to attrs/metrics?
                    Asset(
                        asset_type_id=None,
                        label="TestAsset",
                        description="Test description",
                        organization_id=organization_id,
                        asset_attribute_values=[
                            # AttributeValue(notes=, value=)
                        ],
                        asset_metric_values=[
                            # MetricValue(notes=, value=)
                        ])
                ])
        ]

        # Store schemas in dictionary
        self.schemas = {s.name: s for s in schemas}

    def get(self, name):
        return self.schemas.get(name, None)
