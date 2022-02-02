from os import path
import click

import contxt.schemas as schemas
from contxt.services.base_graph_service import BaseGraphService
from contxt.utils.contxt_environment import ContxtEnvironment


@click.command()
@click.option('--fresh-from-file', type=str, help='Overwrite/init from a specific environment file')
def init(fresh_from_file: str):
    """Initialize all schemas"""
    if fresh_from_file:
        print(f'Loading fresh config from file: {fresh_from_file}')
        config = ContxtEnvironment(filename=fresh_from_file)
        config.rewrite_to_default_file()
        print('Config file has been initialized')
    print('Updating schemas')
    config = ContxtEnvironment()
    schema_dir = path.dirname(schemas.__file__)
    for env in config.config.get_graph_environments_for_current_context():
        base_graph = BaseGraphService(env, load_schema=False)
        base_graph.update_schema(service_name=env.service, base_file_path=schema_dir)
