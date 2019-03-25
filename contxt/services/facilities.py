from contxt.legacy.services import GET, APIObject, APIObjectCollection, Service
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

        super().__init__(
            base_url=self.env['base_url'],
            access_token=auth_module.get_token_for_audience(
                self.env['audience']))

    def get_facilities(self, organization_id=None):

        uri = 'facilities'

        if organization_id:
            assert isinstance(organization_id, str)
            uri = f'organizations/{organization_id}/facilities'

        response = self.execute(GET(uri=uri))

        facilities = []
        for org in response:
            facilities.append(Facility(org))

        return APIObjectCollection(facilities)

    def get_facility_by_id(self, facility_id):

        assert isinstance(facility_id, int)

        return Facility(self.execute(GET(uri=f'facilities/{facility_id}')))


class Facility(APIObject):

    def __init__(self, facility_api_object, keys_to_ignore=None):

        super().__init__(
            keys_to_ignore=keys_to_ignore if keys_to_ignore is not None else [
                'address1', 'address2', 'geometry_id', 'tags',
                'Organization', 'Info'
            ])

        self.id = facility_api_object['id']
        self.name = facility_api_object['name']
        self.address1 = facility_api_object['address1']
        self.address2 = facility_api_object['address2']
        self.city = facility_api_object['city']
        self.state = facility_api_object['state']
        self.zip = facility_api_object['zip']
        self.timezone = facility_api_object['timezone']
        self.geometry_id = facility_api_object['geometry_id']
        self.asset_id = facility_api_object['asset_id']
        self.tags = facility_api_object['tags']
        self.organization_id = facility_api_object['organization_id']
        self.Organization = Organization(facility_api_object['Organization'])
        self.created_at = facility_api_object['created_at']
        self.Info = facility_api_object['Info']

    def get_dict(self):
        return {
            **super().get_dict(),
            'organization_name': self.Organization.name
        }
