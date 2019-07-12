from contxt.legacy.models.iot import Field
from contxt.legacy.services import APIObject, APIObjectCollection


class FacilityUtilitySpend(APIObject):
    def __init__(self, spend_api_object, keys_to_ignore=None):
        super().__init__(keys_to_ignore=keys_to_ignore)

        self.type = spend_api_object["type"]
        self.currency = spend_api_object["currency"]

        periods = [UtilitySpendPeriod(s) for s in spend_api_object["values"]]
        self.spend_periods = APIObjectCollection(periods)

    def __str__(self):
        print(f"Utility Spend -> Type: {self.type} -- Currency: {self.currency}")
        return self.spend_periods.__str__()

    def get_dict(self):
        return {**super().get_dict(), "spend_periods": self.spend_periods.get_dicts()}


class UtilitySpendPeriod(APIObject):
    def __init__(self, spend_api_object, keys_to_ignore=None):
        super().__init__(keys_to_ignore=keys_to_ignore)

        self.date = spend_api_object["date"]
        self.spend = spend_api_object["value"]
        self.pro_forma_date = spend_api_object.get("pro_forma_date")

    def get_values(self):
        return [self.date, self.spend, self.pro_forma_date]

    def get_keys(self):
        return ["date", "value", "pro_forma_date"]


class UtilityUsagePeriod(APIObject):
    def __init__(self, spend_api_object, keys_to_ignore=None):
        super().__init__(keys_to_ignore=keys_to_ignore)

        self.date = spend_api_object["date"]
        self.value = spend_api_object["value"]
        self.pro_forma_date = spend_api_object.get("pro_forma_date")

    def get_values(self):
        return [self.date, self.value, self.pro_forma_date]

    def get_keys(self):
        return ["date", "value", "pro_forma_date"]


class FacilityUtilityUsage(APIObject):
    def __init__(self, spend_api_object, keys_to_ignore=None):
        super().__init__(keys_to_ignore=keys_to_ignore)

        self.type = spend_api_object["type"]
        self.unit = spend_api_object["unit"]

        periods = [UtilityUsagePeriod(s) for s in spend_api_object["values"]]
        self.usage_periods = APIObjectCollection(periods)

    def __str__(self):
        print("Utility Usage -> Type: {} -- Units: {}".format(self.type, self.unit))
        return self.usage_periods.__str__()

    def get_dict(self):
        return {**super().get_dict(), "spend_periods": self.usage_periods.get_dicts()}


class FacilityMainService(APIObject):
    def __init__(self, facility_main_object, keys_to_ignore=None):
        super().__init__(keys_to_ignore=keys_to_ignore)

        self.id = facility_main_object["id"]
        self.facility_id = facility_main_object["facility_id"]
        self.name = facility_main_object["name"]
        self.type = facility_main_object["type"]
        self.demand_field = (
            Field(facility_main_object["demand_field"])
            if facility_main_object["demand_field"]
            else None
        )
        self.usage_field = (
            Field(facility_main_object["usage_field"])
            if facility_main_object["usage_field"]
            else None
        )

    def get_values(self):
        return [
            self.facility_id,
            self.name,
            self.type,
            self.demand_field.id if self.demand_field else None,
            self.usage_field.id if self.usage_field else None,
        ]

    def get_keys(self):
        return ["facility_id", "name", "type", "demand_field_id", "usage_field_id"]
