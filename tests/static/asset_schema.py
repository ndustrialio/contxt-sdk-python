from contxt.models.assets import (
    Asset,
    AssetType,
    Attribute,
    DataTypes,
    Metric,
    TimeIntervals,
)
from contxt.utils.assets_migration import AssetSchema


class AssetSchemas:
    def __init__(self, organization_id):

        # Build temporary list
        schemas = [
            AssetSchema(
                name="TestSchema",
                asset_types=[
                    AssetType(
                        label="TestParentType",
                        description="Test description",
                        organization_id=organization_id,
                        attributes=[
                            Attribute(
                                asset_type_id=None,
                                label="test_attr_label",
                                description="Test description",
                                units="?",
                                organization_id=organization_id,
                                data_type=DataTypes.string,
                                is_required=False,
                            )
                        ],
                        metrics=[
                            Metric(
                                asset_type_id=None,
                                label="test_met_label",
                                description="Test description",
                                organization_id=organization_id,
                                time_interval=TimeIntervals.weekly,
                                units="?",
                            )
                        ],
                        children=[
                            AssetType(
                                label="TestChildType",
                                description="Test description",
                                organization_id=organization_id,
                            )
                        ],
                    )
                ],
                assets=[
                    # TODO: how to link asset to types, values to attrs/metrics?
                    Asset(
                        asset_type_id=None,
                        label="TestAsset",
                        description="Test description",
                        organization_id=organization_id,
                        attribute_values=[
                            # AttributeValue(notes=, value=)
                        ],
                        metric_values=[
                            # MetricValue(notes=, value=)
                        ],
                    )
                ],
            )
        ]

        # Store schemas in dictionary
        self.schemas = {s.name: s for s in schemas}

    def get(self, name, value=None):
        return self.schemas.get(name, value)
