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


@get.command()
def users():
    users = get_base_service().get_users()
    print(Serializer.to_table(users))


@get.command()
def my_roles():
    my_roles = get_base_service().my_roles()
    print(Serializer.to_table(my_roles))


@base.command()
@click.option('--source', required=True)
@click.option('--channel', required=True)
@click.option('--cursor', required=True, type=int)
def set_cursor(source: str, channel: str, cursor: int):
    cursor = get_base_service().set_channel_cursor(source_slug=source,
                                                   channel_name=channel,
                                                   cursor=cursor)
    print(Serializer.to_table(cursor))


@base.command()
@click.option('--user-id', required=True, type=str, prompt=True, help='ID of the user to grant the role to')
@click.option('--role', required=True, type=str, prompt=True, help='Role name')
def grant_role(user_id: str, role: str):
    get_base_service().grant_role(user_id, role)


# Getter functions
@click.group()
def create() -> None:
    """Create Functions"""


@create.command()
@click.option('--slug', help='Slugified version of the source type. This will be the primary ID', prompt=True)
@click.option('--name', help='The pretty name of the source type (this will ultimately be shown in a UI', prompt=True)
def source_type(slug: str, name: str) -> None:
    """Create a new Source Type"""
    source_type = get_base_service().create_source_type(slug=slug, name=name)
    print(Serializer.to_pretty_cli(source_type))


@click.group(context_settings=dict(help_option_names=["-h", "--help"], show_default=True))
def cli() -> None:
    pass


base.add_command(get)
base.add_command(create)
