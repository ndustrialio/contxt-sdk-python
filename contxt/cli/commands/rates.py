from typing import Optional

import click

from contxt.cli.clients import Clients
from contxt.utils.serializer import Serializer


@click.group()
def rates() -> None:
    """Utility Rates"""


@rates.command()
@click.pass_obj
def providers(clients: Clients) -> None:
    """Get Utility Providers"""
    provider_list = clients.rates.get_providers()

    providers = [p for p in provider_list]
    print(Serializer.to_table(providers))


@rates.command()
@click.option('--provider-id', type=int, required=True, help='Utility provider ID')
@click.pass_obj
def schedules(clients: Clients, provider_id: int) -> None:
    """Get Rate Schedules for Provider"""
    schedules_list = clients.rates.get_schedules_for_provider(utility_provider_id=provider_id)

    schedules = [s for s in schedules_list]
    print(Serializer.to_table(schedules, exclude_keys=['utility_provider_id', 'description', 'sector',
                                                       'utility_provider', 'utility_contract_id', 'openei_id', 'uri',
                                                       'source', 'created_at', 'updated_at']))


@rates.command()
@click.argument('SCHEDULE_ID', type=int)
@click.pass_obj
def schedule(clients: Clients, schedule_id: int) -> None:
    """Get Rate Schedule"""
    schedule = clients.rates.get_schedule(rate_schedule_id=schedule_id)

    print(Serializer.to_pretty_cli(schedule))
