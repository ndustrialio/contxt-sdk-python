from contxt.services import Service, GET, POST, APIObject, APIObjectCollection

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

    def create_organization(self, organization_name):

        assert isinstance(organization_name, str)

        body = {
            'name': organization_name
        }

        return Organization(self.execute(POST(uri='organizations').body(body)))

    def add_user_to_organization(self, user_id, organization_id):

        assert isinstance(organization_id, str)
        assert isinstance(user_id, str)

        return OrganizationUser(self.execute(POST(uri='organizations/{}/users/{}'.format(organization_id, user_id))))

    def get_organization_users(self, organization_id):

        assert isinstance(organization_id, str)

        users = []
        for user in self.execute(GET(uri='organizations/{}/users'.format(organization_id))):
            users.append(User(user))
        return APIObjectCollection(users)


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


class OrganizationUser(APIObject):

    def __init__(self, organization_user_api_object):

        super(OrganizationUser, self).__init__()

        self.id = organization_user_api_object['id']
        self.organization_id = organization_user_api_object['organization_id']
        self.user_id = organization_user_api_object['user_id']

    def get_values(self):
        return [self.id, self.user_id, self.organization_id]

    def get_keys(self):
        return ['id', 'user_id', 'organization_id']


class User(APIObject):

    def __init__(self, user_api_object):

        super(User, self).__init__()

        self.id = user_api_object['id']
        self.first_name = user_api_object['first_name']
        self.last_name = user_api_object['last_name']
        self.email = user_api_object['email']
        self.is_activated = user_api_object['is_activated']
        self.Roles = [Role(role) for role in user_api_object['Roles']]

    def get_values(self):
        return [self.id, self.first_name, self.last_name, self.is_activated, ','.join([role.name for role in self.Roles])]

    def get_keys(self):
        return ['id', 'first_name', 'last_name', 'is_activated', 'roles']


class Role(APIObject):

    def __init__(self, role_api_object):

        super(Role, self).__init__()

        self.id = role_api_object['id']
        self.name = role_api_object['name']
        self.description = role_api_object['description']
        self.organization_id = role_api_object['organization_id']
        self.created_at = role_api_object['created_at']
        self.updated_at = role_api_object['updated_at']

    def get_values(self):
        return [self.id, self.name, self.description, self.organization_id]

    def get_keys(self):
        return ['id','name','description','organization_id']
