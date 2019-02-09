from contxt.services import Service, GET, APIObject, APIObjectCollection
from contxt.services.contxt import Organization

CONFIGS_BY_ENVIRONMENT = {
    'production': {
        'base_url': 'https://facilities.api.ndustrial.io/',
        'audience': 'SgbCopArnGMa9PsRlCVUCVRwxocntlg0'
    },
    'staging': {
        'base_url': 'https://facilities-staging.api.ndustrial.io/',
        'audience': 'xG775XHIOZVUn84seNeHXi0Qe55YuR5w'
    }
}


class FacilitiesService(Service):

    def __init__(self, auth_module, environment='production'):

        if environment not in CONFIGS_BY_ENVIRONMENT:
            raise Exception('Invalid environment specified')

        self.env = CONFIGS_BY_ENVIRONMENT[environment]

        super(FacilitiesService, self).__init__(base_url=self.env['base_url'],
                                                access_token=auth_module.get_token_for_client(self.env['audience']))

    def get_facilities(self, organization_id=None):

        uri = 'facilities'

        if organization_id:
            assert isinstance(organization_id, str)
            uri = 'organizations/{}/facilities'.format(organization_id)

        response = self.execute(GET(uri=uri))

        facilities = []
        for org in response:
            facilities.append(Facility(org))

        return APIObjectCollection(facilities)


class Facility(APIObject):

    def __init__(self, facility_api_object):

        super(Facility, self).__init__()

        self.id = facility_api_object['id']
        self.name = facility_api_object['name']
        self.organization_id = facility_api_object['organization_id']
        self.address1 = facility_api_object['address1']
        self.address2 = facility_api_object['address2']
        self.city = facility_api_object['city']
        self.state = facility_api_object['state']
        self.zip = facility_api_object['zip']
        self.timezone = facility_api_object['timezone']
        self.geometry_id = facility_api_object['geometry_id']
        self.asset_id = facility_api_object['asset_id']
        self.tags = facility_api_object['tags']
        self.created_at = facility_api_object['created_at']
        self.Organization = Organization(facility_api_object['Organization'])
        self.Info = facility_api_object['Info']

    def get_values(self):
        return [self.id, self.name, self.city, self.state, self.zip, self.timezone, self.organization_id, self.Organization.name, self.created_at]

    def get_keys(self):
        return ['id', 'name', 'city', 'state', 'zip', 'timezone', 'organization_id', 'organization_name', 'created_at']

