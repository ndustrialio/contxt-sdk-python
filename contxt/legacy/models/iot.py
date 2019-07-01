from contxt.legacy.services import APIObject, APIObjectCollection


class FieldGrouping(APIObject):
    def __init__(
        self,
        grouping_api_object,
        owner_obj,
        category_obj,
        field_obj_list,
        keys_to_ignore=None,
    ):
        super().__init__(
            keys_to_ignore=keys_to_ignore
            if keys_to_ignore is not None
            else [
                "owner_id",
                "is_public",
                "created_at",
                "updated_at",
                "owner",
                "category",
                "fields",
            ]
        )

        self.id = grouping_api_object["id"]
        self.label = grouping_api_object["label"]
        self.slug = grouping_api_object["slug"]
        self.description = grouping_api_object["description"]
        self.facility_id = grouping_api_object["facility_id"]
        self.owner_id = grouping_api_object["owner_id"]
        self.is_public = grouping_api_object["is_public"]
        self.created_at = grouping_api_object["created_at"]
        self.updated_at = grouping_api_object["updated_at"]
        self.field_category_id = grouping_api_object["field_category_id"]
        self.owner = owner_obj
        self.category = category_obj
        self.fields = APIObjectCollection(field_obj_list)

    def get_dict(self):
        return {
            **super().get_dict(),
            "field_category_name": self.category.name if self.category else None,
            "field_count": len(self.fields),
        }


class UnprovisionedField(APIObject):
    def __init__(self, unprovisioned_api_object):
        super().__init__()

        self.field_descriptor = unprovisioned_api_object["field_descriptor"]
        self.assumed_type = unprovisioned_api_object["assumed_type"]


class FieldCategory(APIObject):
    def __init__(self, category_api_object):
        super().__init__()

        self.id = category_api_object["id"]
        self.name = category_api_object["name"]
        self.description = category_api_object["description"]
        self.organization_id = category_api_object["organization_id"]
        self.parent_category_id = category_api_object["parent_category_id"]
        self.created_at = category_api_object["created_at"]
        self.updated_at = category_api_object["updated_at"]


class FieldGroupingOwner(APIObject):
    def __init__(self, owner_api_object):
        super().__init__()

        self.id = owner_api_object["id"]
        self.first_name = owner_api_object["first_name"]
        self.last_name = owner_api_object["last_name"]


class Field(APIObject):
    def __init__(self, field_api_object):
        super().__init__()

        self.id = field_api_object["id"]
        self.label = field_api_object["label"]
        self.output_id = field_api_object["output_id"]
        self.field_descriptor = field_api_object["field_descriptor"]
        self.field_human_name = field_api_object["field_human_name"]
        self.is_hidden = (
            field_api_object["is_hidden"] if "is_hidden" in field_api_object else None
        )
        self.status = (
            field_api_object["status"] if "status" in field_api_object else None
        )
        self.units = field_api_object["units"]


class Feed(APIObject):
    def __init__(self, feed_api_object):
        super().__init__()

        self.id = feed_api_object["id"]
        self.feed_type_id = feed_api_object["feed_type_id"]
        self.down_after = feed_api_object["down_after"]
        self.key = feed_api_object["key"]
        self.facility_id = feed_api_object["facility_id"]
        self.timezone = feed_api_object["timezone"]
        self.token = feed_api_object["token"]
        self.status = feed_api_object["status"]
        self.degraded_threshold = feed_api_object["degraded_threshold"]
        self.critical_threshold = feed_api_object["critical_threshold"]
        self.status_event_id = feed_api_object["status_event_id"]
        self.created_at = feed_api_object["created_at"]
