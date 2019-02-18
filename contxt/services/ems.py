from contxt.services import Service, GET, APIObject, APIObjectCollection
from datetime import datetime

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

        super(EMSService, self).__init__(base_url=self.env['base_url'],
                                         access_token=auth_module.get_token_for_client(self.env['audience']))

    def get_monthly_utility_spend(self, facility_id, type, date_start, date_end, proforma=False, exclude_account_charges=False):

        assert isinstance(facility_id, int)
        assert isinstance(type, str)
        assert isinstance(date_start, datetime)
        assert isinstance(date_end, datetime)

        params = {
            'type': type,
            'date_start': date_start.strftime('%Y-%m'),
            'date_end': date_end.strftime('%Y-%m'),
            'proforma': 'true' if proforma else 'false',
            'exclude_account_charges': 'true' if exclude_account_charges else 'false'
        }

        response = self.execute(GET(uri='facilities/{}/utility/spend/monthly'.format(facility_id)).params(params),
                                execute=True)

        return FacilityUtilitySpend(response)


class FacilityUtilitySpend(APIObject):

    def __init__(self, spend_api_object):

        super(FacilityUtilitySpend, self).__init__()

        self.type = spend_api_object['type']
        self.currency = spend_api_object['currency']

        periods = []
        for obj in spend_api_object['values']:
            periods.append(UtilitySpendPeriod(obj))

        self.spend_periods = APIObjectCollection(periods)

    def __str__(self):
        print('Utility Spend -> Type: {} -- Currency: {}'.format(self.type, self.currency))
        return self.spend_periods.__str__()

    def get_values(self):
        return self.__dict__.values()

    def get_keys(self):
        return self.__dict__.keys()


class UtilitySpendPeriod(APIObject):

    def __init__(self, spend_api_object):

        super(UtilitySpendPeriod, self).__init__()

        self.date = spend_api_object['date']
        self.spend = spend_api_object['value']
        self.proforma_date = spend_api_object['proforma_date']

    def get_values(self):
        return [self.date, self.spend, self.proforma_date]

    def get_keys(self):
        return ['date', 'spend', 'proforma_date']
