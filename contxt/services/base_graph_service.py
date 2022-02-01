import os.path
from os import path
import json
from sgqlc.operation import Operation
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.introspection import query as introspection_query, variables
from sgqlc.codegen.schema import CodeGen, load_schema
from importlib import import_module

from contxt.services.api import ConfiguredGraphApi
from contxt.utils.config import ContxtEnvironmentConfig


class SchemaMissingException(Exception):
    pass


class BaseGraphService(ConfiguredGraphApi):

    def __init__(self, contxt_env: ContxtEnvironmentConfig, schema_path=None, load_schema=True):
        super().__init__(contxt_env)
        self.service_name = contxt_env.service
        self.url = contxt_env.apiEnvironment.baseUrl
        self.schema_name = self.service_name.replace("-", "_")
        self.endpoint = None
        if load_schema:
            self.schema = self._load_schema(schema_path)

    def _load_schema(self, schema_path):
        if not schema_path:
            module_path = f'contxt.schemas.{self.schema_name}.{self.schema_name}_schema'
        else:
            module_path = f'{schema_path.replace("/",".")}.{self.schema_name}.{self.schema_name}_schema'
        return import_module(module_path)

    def _get_endpoint(self):
        if not self.endpoint:
            self.endpoint = HTTPEndpoint(self.url, {'Authorization': f'Bearer {self.token_provider.access_token}'})
        return self.endpoint

    def update_schema(self, service_name=None, base_file_path=None):
        print(f'Loading schema for {service_name} at {self.url}')
        data = self._get_endpoint()(introspection_query, variables())

        service_name = service_name.replace('-','_')
        schema_name = service_name if service_name else self.service_name

        # if base file path is not specified, write the schema in the same directory
        if not base_file_path:
            base_file_path = path.dirname(__file__)

        schema_dir = os.path.join(base_file_path, service_name)
        if not os.path.exists(schema_dir):
            os.makedirs(schema_dir)

        json_schema_filepath = path.abspath(path.join(schema_dir, f"{schema_name}_schema.json"))
        with open(json_schema_filepath, 'w') as f:
            print(f'Writing schema to {json_schema_filepath}')
            json.dump(data, f, sort_keys=True, indent=2, default=str)

        python_schema_filepath = path.abspath(path.join(schema_dir, f'{schema_name}_schema.py'))
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
