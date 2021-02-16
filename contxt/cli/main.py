"""Main CLI"""

from pathlib import Path

import click

from contxt import __version__
from contxt.cli.clients import Clients

COMMAND_DIR = Path(__file__).parent / "commands"


class Cli(click.MultiCommand):
    def list_commands(self, ctx):
        return sorted([p.stem for p in COMMAND_DIR.glob("*.py")])

    def get_command(self, ctx, name):
        f = COMMAND_DIR / f"{name}.py"
        if not f.exists():
            return None
        ns = {}
        code = compile(f.read_text(), f, "exec")
        eval(code, ns, ns)
        return ns[name]


@click.group(cls=Cli, name="contxt", context_settings=dict(help_option_names=["-h", "--help"]))
@click.option(
    "--env",
    type=click.Choice(["production", "staging"]),
    default="production",
    help="Environment for all API's",
)
@click.version_option(__version__, "-v", "--version")
@click.pass_context
def cli(ctx: click.Context, env: str) -> None:
    """Contxt CLI"""
    ctx.obj = Clients(env=env)


if __name__ == "__main__":
    cli()
