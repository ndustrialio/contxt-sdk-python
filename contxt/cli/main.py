"""Main CLI"""

import logging
import sys

from pathlib import Path
from typing import Optional

import click
from requests import RequestException

from contxt import __version__
from contxt.cli.clients import Clients
from contxt.cli.log import init as init_logger
from contxt.services.base_graph_service import SchemaMissingException
from contxt.utils.contxt_environment import ContxtEnvironment, ContxtConfigurationError

logger = logging.getLogger()
COMMAND_DIR = Path(__file__).parent / "commands"


class Cli(click.MultiCommand):
    def list_commands(self, ctx):
        return sorted([p.stem.replace("_", "-") for p in COMMAND_DIR.glob("*.py")])

    def get_command(self, ctx, name):
        name = name.replace("-", "_")
        f = COMMAND_DIR / f"{name}.py"
        if not f.exists():
            return None
        ns = {}
        code = compile(f.read_text(), f, "exec")
        try:
            eval(code, ns, ns)
        except SchemaMissingException:
            print(f'Missing schema for {name}')
            return None
        return ns[name]

    def __call__(self, *args, **kwargs):
        try:
            return self.main(*args, **kwargs)
        except RequestException as e:
            logger.error(f"{e} (response: {e.response.content})")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            raise


@click.group(cls=Cli, name="contxt", context_settings=dict(help_option_names=["-h", "--help"]))
@click.option("--org", envvar="CONTXT_ORG", help="Organization slug")
@click.option("-v", "--verbose", count=True, help="Increase verbosity")
@click.version_option(__version__, "-V", "--version")
@click.pass_context
def cli(ctx: click.Context, org: Optional[str], verbose: int) -> None:
    """Contxt CLI"""
    init_logger(verbose)
    try:
        env = ContxtEnvironment()
        ctx.obj = Clients(contxt_env=env, org_slug=org)
    except ContxtConfigurationError:
        print('Configuration error has occurred. Make sure you have ran `contxt init`')
        print('If this is the first time running the SDK, run `contxt init '
              '--fresh-from-file ./docs/configs/basic_config.yml')


if __name__ == "__main__":
    cli()
