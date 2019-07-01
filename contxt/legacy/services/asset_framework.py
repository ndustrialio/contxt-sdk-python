from datetime import datetime

import pytz

from contxt.legacy.services import (
    DELETE,
    GET,
    POST,
    PUT,
    APIObject,
    APIObjectCollection,
    PagedEndpoint,
    PagedResponse,
)
from contxt.legacy.services.assets import (
    Asset,
    AssetAttributeValue,
    AssetMetric,
    Assets,
    AssetType,
    InvalidAttributeException,
)
from contxt.utils import make_logger

logger = make_logger(__name__)


def datetime_zulu_format(dt):
    assert dt.tzinfo == pytz.UTC
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def datetime_zulu_parse(timestamp):
    return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ").replace(
        tzinfo=pytz.UTC
    )


def normalize_label(raw_label):
    return raw_label.lower().replace(" ", "_")


normalize_field_label = normalize_label


def datetime_zulu_now():
    return datetime_zulu_format(datetime.now(tz=pytz.UTC))


def default_effective_date():
    return (
        str(datetime(year=2018, month=1, day=1)),
    )  # set this for now until FM-200 is fixed


asset_core_fields = ["id", "label", "parent_id", "description"]


class AssetMetricValue(APIObject):
    def __init__(
        self,
        id,
        asset_id,
        asset_metric_id,
        effective_start_date,
        effective_end_date,
        value,
        **kwargs,
    ):

        super(AssetMetricValue, self).__init__()
        self.id = id
        self.asset_id = asset_id
        self.asset_metric_id = asset_metric_id
        self.effective_start_date = effective_start_date
        self.effective_end_date = effective_end_date
        self.value = value
        for k, v in kwargs.items():
            setattr(self, k, v)

    def get_keys(self):
        return ["asset_name", "effective_start_date", "effective_end_date", "value"]

    def get_values(self):
        return [
            self.Asset["label"],
            self.effective_start_date,
            self.effective_end_date,
            self.value,
        ]


class AssetTree:
    def __init__(self, root):
        self.root = root


class AssetNode:
    def __init__(self, attributes=None, children=None, meta=None, type_label=None):
        self.attributes = attributes
        self.children = children or []
        self._meta = meta or {}
        self.type_label = type_label

        self.id = meta.get("id")
        self.parent_id = meta.get("parent_id")
        self.label = meta.get("label")
        self.description = meta.get("description")

        # intersection validation
        intersect = set(asset_core_fields).intersection(set(self.attributes.iterkeys()))
        if intersect:
            logger.warn(
                f"Non empty intersection between core fields and attributes:"
                f" {intersect}. Attributes will be overwritten by core fields"
            )

    def add_child(self, child):
        self.children.append(child)

    def add_meta_data(self, meta_data):
        self._meta = meta_data

    def all_fields(self):
        fields = self.attributes.copy()
        for k in asset_core_fields:
            v = getattr(self, k)
            if v:
                fields[k] = v
        return fields


class LazyAssetsService(Assets):
    def __init__(self, organization_id, auth_module, environment="production"):
        self.types_by_label = {}
        self.types_by_uid = {}  # NOTE: Assets clears types_by_id
        Assets.__init__(
            self,
            auth_module=auth_module,
            organization_id=organization_id,
            environment=environment,
        )
        logger.info(f"Loaded asset types {self.types_by_label.keys()}")
        self._facility = None

    def baseURL(self):
        return self.config.base_url

    def audience(self):
        return self.config.audience

    def load_configuration(self):
        # BUG: Assets class loads all asset types, rather than organization-specific
        # types. This leads to asset types with the same label (i.e. globals)
        # being overwritten.

        req = GET(uri=f"organizations/{self.organization_id}/assets/types")

        asset_types = PagedResponse(
            PagedEndpoint(
                base_url=self.base_url, client=self.client, request=req, parameters={}
            )
        )

        for asset_type in asset_types:
            self._load_configuration_for_type(asset_type)

    def _load_configuration_for_type(self, asset_type_obj):
        # making 'lazy' trick to skip loading attributes and metrics
        type_class_obj = AssetType(
            assets_instance=self,
            organization_id=self.organization_id,
            type_obj=asset_type_obj,
        )
        # store asset type object by label (raw and normalized)
        raw_label = type_class_obj.label
        normalized_label = type_class_obj.label.replace(" ", "")
        type_class_obj.label = normalized_label
        for label in [raw_label, normalized_label]:
            self.types_by_label[label] = type_class_obj
        # store asset type object by id
        self.types_by_uid[type_class_obj.id] = type_class_obj

    def load_type_attributes(self, type_class_obj):
        if not type_class_obj.attributes:
            logger.info(
                f"LazyAssetsService fetching attributes for type"
                f" '{type_class_obj.label}'"
            )
            type_class_obj.set_attributes(self.get_attributes_for_type(type_class_obj))
            type_class_obj.attributes_by_id = {
                attr.id: attr for label, attr in type_class_obj.attributes.items()
            }

    def load_type_metrics(self, type_class_obj):
        if not type_class_obj.metrics:
            logger.info(
                f"LazyAssetsService fetching metrics for type '{type_class_obj.label}'"
            )
            type_class_obj.set_metrics(self.get_metrics_for_type(type_class_obj))
            type_class_obj.metrics_by_id = {
                attr.id: attr for label, attr in type_class_obj.metrics.items()
            }

    def load_type_full(self, type_class_obj):
        self.load_type_attributes(type_class_obj)
        self.load_type_metrics(type_class_obj)
        return type_class_obj

    def asset_type_with_id(self, asset_type_id):
        if asset_type_id not in self.types_by_uid:
            raise AssertionError(
                f"Asset Type with id '{asset_type_id}' not found. Was it loaded?"
            )
        return self.types_by_uid[asset_type_id]

    def asset_type_with_label(self, label):
        if label not in self.types_by_label:
            raise AssertionError(f"Asset Type with label '{label}' not found")
        return self.types_by_label[label]

    def asset_attribute_with_id(self, asset_type, asset_attribute_id):
        if asset_attribute_id not in asset_type.attributes_by_id:
            raise AssertionError(
                f"Asset Attribute with id '{asset_attribute_id}' not found."
                f" Was it loaded?"
            )
        return asset_type.attributes_by_id[asset_attribute_id]

    def asset_attribute_with_label(self, asset_type, asset_attribute_label):
        if asset_attribute_label not in asset_type.attributes:
            raise AssertionError(
                f"Asset Attribute with label '{asset_attribute_label}' not found."
                f" Was it loaded?"
            )
        return asset_type.attributes[asset_attribute_label]

    def asset_metric_with_id(self, asset_type, asset_metric_id):
        if asset_metric_id not in asset_type.metrics_by_id:
            raise AssertionError(
                f"Asset Metric with id '{asset_metric_id}' not found. Was it loaded?"
            )
        return asset_type.metrics_by_id[asset_metric_id]

    def asset_metric_with_label(self, asset_type, asset_metric_label):
        if asset_metric_label not in asset_type.metrics:
            raise AssertionError(
                f"Asset Metric with label '{asset_metric_label}' not found."
                f" Was it loaded?"
            )
        return asset_type.metrics[asset_metric_label]

    def create_asset_by_object_reflection(self, obj):
        type_name = type(obj).__name__
        at = self.asset_type_with_label(type_name)
        logger.debug(f"Saving '{type_name}' asset")
        clean_attrs = {
            k: v
            for k, v in obj.__dict__.items()
            if v is not None and k not in asset_core_fields
        }

        return self.create_asset_with_attribute_values(
            at,
            clean_attrs,
            parent_id=getattr(obj, "parent_id", None),
            asset_label=obj.label,
            description=getattr(obj, "description", obj.label),
        )

    def create_asset_with_attribute_values(
        self,
        asset_type,
        attr_values_dict,
        parent_id=None,
        asset_label=None,
        description=None,
    ):
        def create_attr_value_dict(label, value):
            return {
                "asset_attribute_id": self.asset_attribute_with_label(
                    asset_type, label
                ).id,
                "effective_date": default_effective_date(),
                "value": value,
            }

        clean_attr_values_dict = {
            k: v for k, v in attr_values_dict.items() if v is not None
        }
        api_body = {
            "label": asset_label or f"{asset_type.label} @ {datetime_zulu_now()}",
            "description": description,
            "asset_type_id": asset_type.id,
            "organization_id": self.organization_id,
            "parent_id": parent_id,
            "asset_attribute_values_to_create": [
                create_attr_value_dict(k, v) for k, v in clean_attr_values_dict.items()
            ],
        }
        # TODO: there is a bug in the ApiServices class, where .params doesn't cast
        # boolean types to json (thus ignoring parameter)
        response = self.execute(
            POST(uri="assets?with_attribute_values=true").body(api_body), execute=True
        )
        asset = Asset(
            assets_instance=self, asset_type_obj=asset_type, api_object=response
        )
        # Attach the attributes to the asset (replacing call to Asset.attributes())
        for (k, v), body in zip(
            clean_attr_values_dict.items(), api_body["asset_attribute_values_to_create"]
        ):
            asset_attr_obj = self.asset_attribute_with_id(
                asset_type, body["asset_attribute_id"]
            )
            # TODO: each attr value body is missing id, since the api doesn't return it
            asset.attribute_values[k] = AssetAttributeValue(
                assets_instance=self,
                asset_obj=asset,
                asset_attribute_obj=asset_attr_obj,
                api_object=body,
            )
            setattr(asset, k, v)
        for k in asset.asset_type.attributes.keys():
            if k not in asset.attribute_values:
                setattr(asset, k, None)
        return asset

    def create_asset_metric(
        self,
        asset_type_obj,
        label,
        description,
        time_interval="hourly",
        units=None,
        is_global=False,
    ):
        api_body = {
            "label": label,
            "description": description,
            "organization_id": self.organization_id if not is_global else None,
            "time_interval": time_interval,
            "units": units,
        }
        uri = f"/assets/types/{asset_type_obj.id}/metrics"
        response = self.execute(POST(uri=uri).body(api_body), execute=True)
        return AssetMetric(asset_type_obj=asset_type_obj, api_object=response)

    def delete_asset_metric(self, asset_type_obj, label):
        asset_metric = self.asset_metric_with_label(asset_type_obj, label)
        uri = f"/assets/metrics/{asset_metric.id}"
        response = self.execute(DELETE(uri=uri), execute=True)
        return response

    def fetch_asset_by_id(self, asset_id):
        # TODO: throw an error here when asset_id is not found
        asset_json = self.execute(GET(uri=f"assets/{asset_id}"), execute=True)
        asset_type = self.asset_type_with_id(asset_json["asset_type_id"])
        self.load_type_full(asset_type)
        asset = Asset(self, asset_type, asset_json)
        # pre fetch attributes
        # todo: revisit this attr prefetching, may be replaced by the attributes
        # coming in the asset_json
        asset.attributes()
        return asset

    @staticmethod
    def normalized_attr_pair(asset_attribute, raw_val):
        value = raw_val
        label = normalize_field_label(asset_attribute.label)
        try:
            if asset_attribute.data_type == "number":
                value = float(value)
            elif asset_attribute.data_type == "boolean":
                value = str(value).lower() == "true"
        except ValueError:
            pass
        return label, value

    def get_asset_tree_by_id(self, asset_id):
        def create_node(asset_dict):
            attr_values_dicts = asset_dict.get("asset_attribute_values", [])
            children_asset_dicts = asset_dict.get("children", [])
            asset_type = self.asset_type_with_id(asset_dict["asset_type_id"])
            attr_values_by_label = dict(
                self.normalized_attr_pair(
                    self.asset_attribute_with_id(asset_type, d["asset_attribute_id"]),
                    d["value"],
                )
                for d in attr_values_dicts
            )
            children_nodes = [create_node(d) for d in children_asset_dicts]
            return AssetNode(
                attributes=attr_values_by_label,
                children=children_nodes,
                meta=asset_dict,
                type_label=asset_type.label,
            )

        asset_json = self.execute(GET(uri=f"assets/{asset_id}"))
        root = create_node(asset_json)
        asset_tree = AssetTree(root)
        return asset_tree

    def get_assets_by_attribute_value(self, asset_type, attr_label, attr_value):
        if attr_label not in asset_type.attributes:
            raise InvalidAttributeException(
                f"Attribute {attr_label} does not exist for type {asset_type.label}"
            )
        attr = asset_type.attributes[attr_label]
        assets = PagedResponse(
            PagedEndpoint(
                base_url=self.base_url,
                client=self.client,
                request=GET(
                    uri=(
                        f"organizations/{self.organization_id}/assets"
                        f"?asset_attribute_id={attr.id}"
                        f"&asset_attribute_value={attr_value}"
                    )
                ),
                parameters={},
            )
        )
        return [
            Asset(assets_instance=self, asset_type_obj=asset_type, api_object=record)
            for record in assets
        ]

    def get_latest_assets_for_type(self, asset_type_obj, limit=1):
        parameters = {
            "asset_type_id": asset_type_obj.id,
            "orderBy": "created_at",
            "reverseOrder": True,
            "limit": limit,
        }

        assets = PagedResponse(
            PagedEndpoint(
                base_url=self.base_url,
                client=self.client,
                request=GET(uri=f"organizations/{self.organization_id}/assets"),
                parameters=parameters,
            )
        )
        return [
            Asset(
                assets_instance=self, asset_type_obj=asset_type_obj, api_object=record
            )
            for record in assets
        ]

    def get_assets_for_type(self, asset_type_obj):
        parameters = {
            "asset_type_id": asset_type_obj.id,
            # 'orderBy': 'created_at',
            # 'reverseOrder': True
        }
        assets = PagedResponse(
            PagedEndpoint(
                base_url=self.base_url,
                client=self.client,
                request=GET(uri=f"organizations/{self.organization_id}/assets"),
                parameters=parameters,
            )
        )
        return [
            Asset(
                assets_instance=self, asset_type_obj=asset_type_obj, api_object=record
            )
            for record in assets
        ]

    def create_metric_value(
        self,
        asset,
        asset_type,
        metric_label,
        metric_start_date,
        metric_end_date,
        metric_value,
    ):
        # /assets/:asset_id/metrics/:asset_metric_id/values
        if metric_label not in asset_type.metrics:
            raise AssertionError(
                f"Metric {metric_label} does not exist for type {asset_type.label}"
            )
        metric = asset_type.metrics[metric_label]
        api_body = {
            "effective_start_date": datetime_zulu_format(metric_start_date),
            "effective_end_date": datetime_zulu_format(metric_end_date),
            "value": metric_value,
        }
        self.execute(
            POST(uri=f"/assets/{asset.id}/metrics/{metric.id}/values").body(api_body),
            execute=True,
        )

    def upsert_metric_value(
        self,
        asset,
        asset_type,
        metric_label,
        metric_start_date,
        metric_end_date,
        metric_value,
    ):
        if metric_label not in asset_type.metrics:
            raise AssertionError(
                f"Metric {metric_label} does not exist for type {asset_type.label}"
            )
        metric = asset_type.metrics[metric_label]
        # Fetch metric values
        self.fetch_and_set_metric_values_for_asset(asset)
        curr_metric_value = asset.metric_values.get(metric_label)
        if curr_metric_value:
            # Update existing metric value
            if curr_metric_value != metric_value:
                # TODO: bug when passing dates here
                api_body = {
                    # 'effective_start_date': datetime_zulu_format(metric_start_date),
                    # 'effective_end_date': datetime_zulu_format(metric_end_date),
                    "value": metric_value
                }
                self.execute(
                    PUT(uri=f"/assets/metrics/values/{curr_metric_value.id}").body(
                        api_body
                    ),
                    execute=True,
                )
        else:
            # Create new metric value
            api_body = {
                "effective_start_date": datetime_zulu_format(metric_start_date),
                "effective_end_date": datetime_zulu_format(metric_end_date),
                "value": metric_value,
            }
            self.execute(
                POST(uri=f"/assets/{asset.id}/metrics/{metric.id}/values").body(
                    api_body
                ),
                execute=True,
            )

    def fetch_all_metric_values_for_asset(self, asset):
        resp = PagedResponse(
            PagedEndpoint(
                base_url=self.base_url,
                client=self.client,
                request=GET(uri=f"assets/{asset.id}/metrics/values"),
                parameters={},
            )
        )
        return APIObjectCollection([AssetMetricValue(**rec) for rec in resp.records])

    def fetch_all_metric_values_for_asset_metric(self, asset, metric):
        resp = PagedResponse(
            PagedEndpoint(
                base_url=self.base_url,
                client=self.client,
                request=GET(uri=f"assets/{asset.id}/metrics/{metric.id}/values"),
                parameters={},
            )
        )
        return APIObjectCollection([AssetMetricValue(**rec) for rec in resp.records])

    def fetch_and_set_metric_values_for_asset(self, asset, force=False):
        if getattr(asset, "metric_values", None) and not force:
            # Already fetched and not forced
            return
        # Either not yet fetched or forced
        asset_type = self.asset_type_with_id(asset.asset_type_id)
        metric_values = self.fetch_all_metric_values_for_asset(asset)
        asset.metric_values = {
            self.asset_metric_with_id(asset_type, mv.asset_metric_id).label: mv
            for mv in metric_values
        }

    def create_asset_type_with_parent(self, type_name, description, parent_id):
        asset_type_response = self.execute(
            POST(uri="/assets/types").body(
                {
                    "label": type_name,
                    "description": description,
                    "organization_id": self.organization_id,
                    "parent_id": parent_id,
                }
            ),
            execute=True,
        )
        return AssetType(
            assets_instance=self,
            organization_id=self.organization_id,
            type_obj=asset_type_response,
        )

    def update_asset_type_parent(self, type_name, parent_id):
        at = self.asset_type_with_label(type_name)
        assert at
        self.execute(
            PUT(uri=f"/assets/types/{at.id}").body({"parent_id": parent_id}),
            execute=True,
        )
        at.parent_id = parent_id
        return at

    def create_asset_with_parent(self, asset_type, asset):
        return self.create_asset(
            asset_type_obj=asset_type,
            api_body={
                "label": asset.label,
                "description": asset.description,
                "asset_type_id": asset_type.id,
                "organization_id": self.organization_id,
                "parent_id": asset.parent_id,
            },
        )

    @staticmethod
    def upsert_attribute_value(asset, attr, value):
        """Create or update an attribute value"""
        if attr in asset.attributes():
            # -- updating existing attribute value
            attr_value = asset.attribute_values[attr]
            if attr_value.value != value:
                attr_value.set(value)
        else:
            # attribute does not exits: create
            asset.withAttributes(**{attr: value})

    def update_asset(self, asset):
        fields = ("description", "parent_id")
        vrs = asset if asset is dict else vars(asset)
        api_body = {k: vrs[k] for k in fields if k in vrs}
        uri = f"/assets/{asset.id}"
        self.execute(PUT(uri=uri).body(api_body), execute=True)
        return asset

    def facility(self, facility_id, force_fetch=False):
        if not self._facility:
            fat = self.asset_type_with_label("Facility")
            self.load_type_attributes(fat)
            self._facility = self.fetch_asset_by_id(facility_id)
        elif force_fetch:
            self._facility.attributes(force_fetch=force_fetch)
        return self._facility

    def get(self, uri):
        api_call = GET(uri=uri)
        return self.execute(api_call, execute=True)
