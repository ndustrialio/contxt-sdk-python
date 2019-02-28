from datetime import datetime

from contxt.services import GET, APIObject, APIObjectCollection, Service

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

    def __init__(self, auth_module, environment='staging'):

        if environment not in CONFIGS_BY_ENVIRONMENT:
            raise Exception('Invalid environment specified')

        self.env = CONFIGS_BY_ENVIRONMENT[environment]

        super().__init__(
            base_url=self.env['base_url'],
            access_token=auth_module.get_token_for_client(
                self.env['audience']))

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
        self.pro_forma_date = spend_api_object['pro_forma_date']

    def get_values(self):
        return [self.date, self.spend, self.pro_forma_date]

    def get_keys(self):
        return ['date', 'value', 'pro_forma_date']
