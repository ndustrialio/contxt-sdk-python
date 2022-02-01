import click

from contxt.services.base.base import BaseService
from contxt.utils.contxt_environment import ContxtEnvironment
from contxt.utils.serializer import Serializer


def get_base_service():
    # load configuration file
    contxt_env = ContxtEnvironment()
    return BaseService(contxt_env=contxt_env.get_config_for_service_name('foundry-graph'))


@click.group()
def base() -> None:
    """Base Contxt Functions"""


# Getter functions
@click.group()
def get() -> None:
    """Get Functions"""


@get.command()
def sources():
    sources = get_base_service().get_sources()
    print(Serializer.to_table(sources))


@get.command()
@click.argument('source-slug', type=str)
def channels(source_slug: str):
    channels = get_base_service().get_channels(source_slug)
    print(Serializer.to_table(channels))


@base.command()
@click.option('--source', required=True)
@click.option('--channel', required=True)
@click.option('--cursor', required=True, type=int)
def set_cursor(source: str, channel: str, cursor: int):
    cursor = get_base_service().set_channel_cursor(source_slug=source,
                                                   channel_name=channel,
                                                   cursor=cursor)
    print(Serializer.to_table(cursor))


@click.group(context_settings=dict(help_option_names=["-h", "--help"], show_default=True))
def cli() -> None:
    pass


base.add_command(get)