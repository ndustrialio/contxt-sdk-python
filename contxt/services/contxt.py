from contxt.legacy.services import GET, POST, APIObject, APIObjectCollection, Service

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

        super().__init__(
            base_url=self.env['base_url'],
            access_token=auth_module.get_token_for_audience(
                self.env['audience']))

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

        return OrganizationUser(self.execute(POST(uri=f'organizations/{organization_id}/users/{user_id}')))

    def get_organization_users(self, organization_id):

        assert isinstance(organization_id, str)

        users = []
        for user in self.execute(
                GET(uri=f'organizations/{organization_id}/users')):
            users.append(User(user))
        return APIObjectCollection(users)


class Organization(APIObject):

    def __init__(self, organization_api_object, keys_to_ignore=None):
        super().__init__(keys_to_ignore=keys_to_ignore
                         if keys_to_ignore is not None else ['updated_at'])

        self.id = organization_api_object['id']
        self.name = organization_api_object['name']
        self.legacy_organization_id = organization_api_object.get(
            'legacy_organization_id', None)
        self.created_at = organization_api_object['created_at']
        self.updated_at = organization_api_object['updated_at']


class OrganizationUser(APIObject):

    def __init__(self, organization_user_api_object, keys_to_ignore=None):
        super().__init__(keys_to_ignore=keys_to_ignore)
        self.id = organization_user_api_object['id']
        self.user_id = organization_user_api_object['user_id']
        self.organization_id = organization_user_api_object['organization_id']


class User(APIObject):

    def __init__(self, user_api_object, keys_to_ignore=None):
        super().__init__(keys_to_ignore=keys_to_ignore
                         if keys_to_ignore is not None else ['email', 'Roles'])

        self.id = user_api_object['id']
        self.first_name = user_api_object['first_name']
        self.last_name = user_api_object['last_name']
        self.email = user_api_object['email']
        self.is_activated = user_api_object['is_activated']
        self.Roles = [Role(role) for role in user_api_object['Roles']]

    def get_dict(self):
        return {
            **super().get_dict(),
            'roles': ','.join([role.name for role in self.Roles])
        }


class Role(APIObject):

    def __init__(self, role_api_object, keys_to_ignore=None):
        super().__init__(
            keys_to_ignore=keys_to_ignore
            if keys_to_ignore is not None else ['created_at', 'updated_at'])

        self.id = role_api_object['id']
        self.name = role_api_object['name']
        self.description = role_api_object['description']
        self.organization_id = role_api_object['organization_id']
        self.created_at = role_api_object['created_at']
        self.updated_at = role_api_object['updated_at']
