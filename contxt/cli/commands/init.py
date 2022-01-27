from os import path
import click

import contxt.schemas as schemas
from contxt.services.base_graph_service import BaseGraphService
from contxt.utils.contxt_environment import ContxtEnvironment


@click.command()
def init():
    """Initialize all schemas"""
    print('Updating schemas')
    config = ContxtEnvironment()
    schema_dir = path.dirname(schemas.__file__)
    for env in config.config.get_graph_environments():
        base_graph = BaseGraphService(env, load_schema=False)
        base_graph.update_schema(service_name=env.service, base_file_path=schema_dir)
