from contxt.services import Service, GET, APIObject, APIObjectCollection
from datetime import datetime

CONFIGS_BY_ENVIRONMENT = {
    'production': {
        'base_url': 'https://contxt.api.ndustrial.io/',
        'audience': '8qY2xJob1JAxhmVhIDLCNnGriTM9bct8'
    },
    'staging': {
        'base_url': 'https://contxt-staging.api.ndustrial.io/',
        'audience': '8qY2xJob1JAxhmVhIDLCNnGriTM9bct8'
    }
}


class ContxtService(Service):

    def __init__(self, auth_module, environment='production'):

        if environment not in CONFIGS_BY_ENVIRONMENT:
            raise Exception('Invalid environment specified')

        self.env = CONFIGS_BY_ENVIRONMENT[environment]

        super(ContxtService, self).__init__(base_url=self.env['base_url'],
                                            access_token=auth_module.get_token_for_client(self.env['audience']))

    def get_organizations(self):

        response = self.execute(GET(uri='organizations'))

        organizations = []
        for org in response:
            organizations.append(Organization(org))
        return APIObjectCollection(organizations)


class Organization(APIObject):

    def __init__(self, organization_api_object):

        super(Organization, self).__init__()

        self.id = organization_api_object['id']
        self.name = organization_api_object['name']
        if 'legacy_organization_id' in organization_api_object:
            self.legacy_organization_id = organization_api_object['legacy_organization_id']
        else:
            self.legacy_organization_id = None
        self.created_at = organization_api_object['created_at']
        self.updated_at = organization_api_object['updated_at']

    def get_values(self):
        return [self.id, self.name, self.legacy_organization_id, self.created_at]

    def get_keys(self):
        return ['id', 'name', 'legacy_organization_id', 'created_at']

