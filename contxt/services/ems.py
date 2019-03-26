from datetime import datetime

from contxt.services import GET, APIObject, APIObjectCollection, Service
from contxt.services.iot import Field

CONFIGS_BY_ENVIRONMENT = {
    'production': {
        'base_url': 'https://ems.api.ndustrial.io/',
        'audience': 'e2IT0Zm9RgGlDBkLa2ruEcN9Iop6dJAS'
    },
    'staging': {
        'base_url': 'https://ems-staging.api.ndustrial.io/',
        'audience': 'vMV67yaRFgjBB1JFbT3vXBOlohFdG1I4'
    }
}


class EMSService(Service):

    def __init__(self, auth_module, environment='production'):

        if environment not in CONFIGS_BY_ENVIRONMENT:
            raise Exception('Invalid environment specified')

        self.env = CONFIGS_BY_ENVIRONMENT[environment]

        super().__init__(
            base_url=self.env['base_url'],
            access_token=auth_module.get_token_for_audience(
                self.env['audience']))

    def get_main_services(self, facility_id, type=None):

        assert isinstance(facility_id, int)

        response = self.execute(
            GET(uri=f'facilities/{facility_id}'),
            execute=True
        )

        # manual filter for main services
        rows = []
        if type:
            for row in response['main_services']:
                if row['type'] == type:
                    rows.append(row)
        else:
            rows = response['main_services']

        return APIObjectCollection([FacilityMainService(row) for row in rows])

    def get_monthly_utility_spend(self, facility_id, type, date_start, date_end, pro_forma=False, exclude_account_charges=False):

        assert isinstance(facility_id, int)
        assert isinstance(type, str)
        assert isinstance(date_start, datetime)
        assert isinstance(date_end, datetime)

        params = {
            'type': type,
            'date_start': date_start.strftime('%Y-%m'),
            'date_end': date_end.strftime('%Y-%m'),
            'pro_forma': 'true' if pro_forma else 'false',
            'exclude_account_charges': 'true' if exclude_account_charges else 'false'
        }

        response = self.execute(
            GET(uri=f'facilities/{facility_id}/utility/spend/monthly').params(
                params),
            execute=True)

        return FacilityUtilitySpend(response)

    def get_monthly_utility_usage(self, facility_id, type, date_start, date_end, pro_forma=False):

        assert isinstance(facility_id, int)
        assert isinstance(type, str)
        assert isinstance(date_start, datetime)
        assert isinstance(date_end, datetime)

        params = {
            'type': type,
            'date_start': date_start.strftime('%Y-%m'),
            'date_end': date_end.strftime('%Y-%m'),
            'pro_forma': 'true' if pro_forma else 'false'
        }

        response = self.execute(GET(uri='facilities/{}/utility/usage/monthly'.format(facility_id)).params(params),
                                execute=True)

        return FacilityUtilityUsage(response)


class FacilityUtilitySpend(APIObject):

    def __init__(self, spend_api_object, keys_to_ignore=None):
        super().__init__(keys_to_ignore=keys_to_ignore)

        self.type = spend_api_object['type']
        self.currency = spend_api_object['currency']

        periods = [UtilitySpendPeriod(s) for s in spend_api_object['values']]
        self.spend_periods = APIObjectCollection(periods)

    def __str__(self):
        print(f'Utility Spend -> Type: {self.type} -- Currency: {self.currency}')
        return self.spend_periods.__str__()

    def get_dict(self):
        return {
            **super().get_dict(),
            'spend_periods': self.spend_periods.get_dicts()
        }


class UtilitySpendPeriod(APIObject):

    def __init__(self, spend_api_object, keys_to_ignore=None):
        super().__init__(keys_to_ignore=keys_to_ignore)

        self.date = spend_api_object['date']
        self.spend = spend_api_object['value']
        self.pro_forma_date = spend_api_object.get('pro_forma_date')

    def get_values(self):
        return [self.date, self.spend, self.pro_forma_date]

    def get_keys(self):
        return ['date', 'value', 'pro_forma_date']


class UtilityUsagePeriod(APIObject):

    def __init__(self, spend_api_object, keys_to_ignore=None):
        super().__init__(keys_to_ignore=keys_to_ignore)

        self.date = spend_api_object['date']
        self.value = spend_api_object['value']
        self.pro_forma_date = spend_api_object.get('pro_forma_date')

    def get_values(self):
        return [self.date, self.value, self.pro_forma_date]

    def get_keys(self):
        return ['date', 'value', 'pro_forma_date']


class FacilityUtilityUsage(APIObject):

    def __init__(self, spend_api_object, keys_to_ignore=None):
        super().__init__(keys_to_ignore=keys_to_ignore)

        self.type = spend_api_object['type']
        self.unit = spend_api_object['unit']

        periods = [UtilityUsagePeriod(s) for s in spend_api_object['values']]
        self.usage_periods = APIObjectCollection(periods)

    def __str__(self):
        print('Utility Usage -> Type: {} -- Units: {}'.format(self.type, self.unit))
        return self.usage_periods.__str__()

    def get_dict(self):
        return {
            **super().get_dict(),
            'spend_periods': self.usage_periods.get_dicts()
        }


class FacilityMainService(APIObject):

    def __init__(self, facility_main_object, keys_to_ignore=None):
        super().__init__(keys_to_ignore=keys_to_ignore)

        self.id = facility_main_object['id']
        self.facility_id = facility_main_object['facility_id']
        self.name = facility_main_object['name']
        self.type = facility_main_object['type']
        self.demand_field = Field(facility_main_object['demand_field']) if facility_main_object['demand_field'] else None
        self.usage_field = Field(facility_main_object['usage_field']) if facility_main_object['usage_field'] else None

    def get_values(self):
        return [self.facility_id,
                self.name,
                self.type,
                self.demand_field.id if self.demand_field else None,
                self.usage_field.id if self.usage_field else None
                ]

    def get_keys(self):
        return ['facility_id', 'name', 'type', 'demand_field_id', 'usage_field_id']
