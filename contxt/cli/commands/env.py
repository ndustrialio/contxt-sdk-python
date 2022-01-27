from typing import Optional
import sys
import click
from PyInquirer import prompt, Separator

from contxt.cli.clients import Clients
from contxt.utils.serializer import Serializer
from contxt.utils.config import ContextException

VALID_AUTH_PROVIDERS = ['contxtauth.com/v1', 'contxt.auth0.com', 'lineagelogistics.auth0.com']


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
@click.argument('SERVICE_NAME')
@click.pass_obj
def detail(clients: Clients, service_name: str) -> None:
    contxt_env = clients.contxt_env

    service_env = contxt_env.get_config_for_service_name(service_name)

    if not service_env:
        print(f'Service not found for: {service_name}')
        sys.exit(1)

    print(Serializer.to_pretty_cli(service_env))


@env.command()
@click.argument('SERVICE_NAME')
@click.pass_obj
def add(clients: Clients, service_name: str) -> None:
    contxt_env = clients.contxt_env

    cli_or_machine = {
        'type': 'list',
        'name': 'selected_type',
        'message': f'Choose authentication method for new context for {service_name}',
        'choices': ['CLI Auth', 'Machine Auth']
    }

    answers = prompt.prompt(cli_or_machine)

    if answers['selected_type'] == 'CLI Auth':
        questions = [
            {
                'type': 'input',
                'name': 'auth_provider',
                'message': 'Enter your auth provider (X.auth0.com usually)'
            },
            {
                'type': 'input',
                'name': 'base_url',
                'message': 'Enter base URL for service'
            },
            {
                'type': 'input',
                'name': 'client_id',
                'message': 'Enter Client ID for service'
            },
            {
                'type': 'input',
                'name': 'environment',
                'message': 'What name would you like to use for this environment?'
            }
        ]

        answers = prompt.prompt(questions)

        print(answers)

    # Machine auth
    else:
        pass




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

