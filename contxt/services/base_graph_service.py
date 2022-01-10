from os import path
import json
from auth0.v3.authentication import GetToken
from sgqlc.operation import Operation
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.introspection import query as introspection_query, variables
from sgqlc.codegen.schema import CodeGen, load_schema

from contxt.utils.config import ContxtEnvironmentConfig
from contxt.services.api import ApiEnvironment
from contxt.services.auth import StoredTokenCache


class BaseGraphService:

    def __init__(self, contxt_env: ContxtEnvironmentConfig):
        self.service_name = contxt_env.service
        self.endpoint = None
        self.env = contxt_env.apiEnvironment
        self.url = self.env.baseUrl
        self.client_id = contxt_env.clientId
        self.client_secret = contxt_env.clientSecret
        self.audience = self.env.clientId
        self.token_cache = StoredTokenCache()

    def _get_endpoint(self):
        if not self.endpoint:
            self.endpoint = HTTPEndpoint(self.url, {'Authorization': f'Bearer {self.get_auth_token()}'})
        return self.endpoint

    def get_auth_token(self):
        cached_token = self.token_cache.get_token(client_id=self.client_id,
                                                  audience=self.audience)

        if cached_token:
            return cached_token

        if self.env.authRequired:
            print(f'Getting token for {self.client_id}: {self.client_secret} against {self.audience} at'
                  f' auth provider: {self.env.authProvider}')
            req = GetToken(self.env.authProvider)
            token = req.client_credentials(client_id=self.client_id, client_secret=self.client_secret,
                                           audience=self.audience)
            self.token_cache.set_token(client_id=self.client_id,
                                       audience=self.audience,
                                       token=token['access_token'])
            return token['access_token']

    def update_schema(self, service_name=None):
        data = self._get_endpoint()(introspection_query, variables())

        schema_name = service_name if service_name else self.service_name

        base_file_path = path.dirname(__file__)
        json_schema_filepath = path.abspath(path.join(base_file_path, schema_name, f"{schema_name}_schema.json"))
        with open(json_schema_filepath, 'w') as f:
            print(f'Writing schema to {json_schema_filepath}')
            json.dump(data, f, sort_keys=True, indent=2, default=str)

        python_schema_filepath = path.abspath(path.join(base_file_path, schema_name, f'{schema_name}_schema.py'))
        print('Generating code for schema')
        with open(json_schema_filepath, 'r') as json_file:
            schema = load_schema(json_file)
            with open(python_schema_filepath, 'w') as schema_file:
                gen = CodeGen(schema_name, schema, schema_file.write, docstrings=True)
                gen.write()
            print('Schema and types updated!')

    def run(self, op: Operation):

        data = self._get_endpoint()(op)

        if 'errors' in data:
            print(data)
            raise Exception(data['errors'][0]['message'])

        return data
