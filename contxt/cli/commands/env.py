from typing import Optional
import sys
import click
from PyInquirer import prompt, Separator

from contxt.cli.clients import Clients
from contxt.utils.serializer import Serializer
from contxt.utils.config import ContextException


@click.group()
def env() -> None:
    """Contxt Environment Functions"""


@env.command()
@click.pass_obj
def current(clients: Clients) -> None:
    """Get current environment settings"""
    contxt_env = clients.contxt_env
    print('=== Defaults ===')
    for key, val in contxt_env.config.defaults.items():
        print(f'   {key} -> {val}')
    print('=== Context ====')
    for service, environment in contxt_env.config.currentContext.items():
        print(f'  {service} -> {environment.environment}')
        try:
            service_env = contxt_env.get_config_for_service_name(service)
            print(f'    {service_env.clientId}, {service_env.apiEnvironment.baseUrl}, {service_env.apiEnvironment.authProvider}')
        except ContextException:
            print(f'Context not found for service {service} and env {environment.environment}')


@env.command()
@click.pass_obj
@click.argument('SERVICE_NAME')
def set_context(clients: Clients, service_name: str) -> None:
    """Set context for a particular service"""
    contxt_env = clients.contxt_env

    service_envs = contxt_env.get_possible_configs_for_service_name(service_name)

    if not len(service_envs):
        print(f'No environments found for service: {service_name}')
        sys.exit(1)

    choices = {
        'type': 'list',
        'name': 'selected_context',
        'message': f'Choose context for {service_name}',
        'choices': [f'{env.environment}' for env in service_envs]
    }

    answers = prompt.prompt(choices)

    contxt_env.set_context_for_service_name(service_name, answers['selected_context'])

    print(answers)

