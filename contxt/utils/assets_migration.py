from typing import List, Optional

from contxt.models.assets import (
    Asset,
    AssetType,
    Attribute,
    AttributeValue,
    Metric,
    MetricValue,
)
from contxt.services.assets import AssetsService
from contxt.utils import make_logger

logger = make_logger(__name__)


# TODO: methods for creating assets, attribute_values, metric_values
class AssetSchema:
    def __init__(
        self,
        name: str,
        asset_types: List[AssetType],
        assets: Optional[List[Asset]] = None,
    ):
        self.name = name
        self.asset_types = asset_types
        self.assets = assets


class AssetMigrationManager:
    def __init__(self, assets_service: AssetsService, asset_schema: AssetSchema):
        self.assets_service = assets_service
        self.schema = asset_schema

    def create(self):
        logger.info(f"Creating assets_schema {self.schema.name}")

        # Create asset types (including attributes, metrics, and children)
        for asset_type in self.schema.asset_types:
            self.create_asset_type(asset_type)

        # TODO: Create assets
        # for asset in self.schema.assets:
        #     new_asset = self.create_asset(asset)

        #     # Create attribute values
        #     for attribute_value in asset.attribute_values:
        #         self.create_attribute_value(new_asset, attribute_value)

        #     # Create metric values
        #     for metric_value in asset.metric_values:
        #         self.create_attribute_value(new_asset, metric_value)

    def create_asset_type(self, asset_type, parent=None):
        # Check if asset_type already exists
        logger.info(f"Processing asset_type {asset_type.label}")
        existing_asset_type = self.assets_service.asset_type_with_label(
            asset_type.label, None
        )

        if existing_asset_type:
            # Asset type already exists, just check parent link
            if parent and parent.id != existing_asset_type.parent_id:
                # Update parent asset_type id
                logger.info(
                    f"Updating parent of {existing_asset_type.label} to {parent.label}"
                )
                existing_asset_type.parent_id = parent.id
                self.assets_service.update_asset_type(existing_asset_type)
        else:
            # Create asset type
            parent_msg = ""
            if parent:
                asset_type.parent_id = parent.id
                parent_msg = f" with parent {parent.label}"
            logger.info(f"Creating asset_type {asset_type.label}{parent_msg}")
            existing_asset_type = self.assets_service.create_asset_type(asset_type)

        # Cache the attributes and metrics
        self.assets_service._cache_attributes(existing_asset_type)
        self.assets_service._cache_metrics(existing_asset_type)

        # Create attributes
        for attribute in asset_type.attributes:
            self.create_attribute(existing_asset_type, attribute)

        # Create metrics
        for metric in asset_type.metrics:
            self.create_metric(existing_asset_type, metric)

        # Create children
        for child in asset_type.children:
            self.create_asset_type(child, parent=existing_asset_type)

    def create_attribute(self, asset_type: AssetType, attribute: Attribute):
        # For the existing asset_type, create the attribute
        if attribute.label not in asset_type._attributes_by_label:
            logger.info(f"Creating attribute {asset_type.label}::{attribute.label}")
            attribute.asset_type_id = asset_type.id
            self.assets_service.create_attribute(attribute)
        else:
            logger.info(
                f"Attribute {asset_type.label}::{attribute.label} already exists"
            )

    def create_metric(self, asset_type: AssetType, metric: Metric):
        # For the existing asset_type, create the metric
        if metric.label not in asset_type._metrics_by_label:
            logger.info(f"Creating metric {asset_type.label}::{metric.label}")
            metric.asset_type_id = asset_type.id
            self.assets_service.create_metric(metric)
        else:
            logger.info(f"Metric {asset_type.label}::{metric.label} already exists")

    def create_asset(self, asset: Asset):
        pass

    def create_attribute_value(self, asset: Asset, attribute_value: AttributeValue):
        pass

    def create_metric_value(self, asset: Asset, metric_value: MetricValue):
        pass

    def delete(self):
        logger.info(f"Deleting assets_schema {self.schema.name}")

        # Delete asset types, which also deletes attributes, metrics, and values
        for asset_type in self.schema.asset_types:
            # First, delete children
            for child in asset_type.children:
                created_child = self.assets_service.asset_type_with_label(child.label)
                self.assets_service.delete_asset_type(created_child)

            # Delete parent
            created_asset_type = self.assets_service.asset_type_with_label(
                asset_type.label
            )
            self.assets_service.delete_asset_type(created_asset_type)
