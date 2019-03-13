from contxt.legacy.services import POST, ApiRequest, Service

CONFIGS_BY_ENVIRONMENT = {
    'production': {
        'base_url': 'https://contxtauth.com',
        'audience': '75wT048QcpE7ujwBJPPjr263eTHl4gEX'
    }
}


class ContxtAuthService(Service):

    def __init__(self, access_token, environment='production'):

        if environment not in CONFIGS_BY_ENVIRONMENT:
            raise Exception('Invalid environment specified')

        self.env = CONFIGS_BY_ENVIRONMENT[environment]

        super().__init__(
            base_url=self.env['base_url'], access_token=access_token)

    def get_new_token_for_client_id(self, client_id):

        body = {
            'audiences': [client_id]
        }

        response = self.execute(POST(uri='token').body(body)
                            .content_type(ApiRequest.URLENCODED_CONTENT_TYPE), execute=True)

        return response['access_token']
