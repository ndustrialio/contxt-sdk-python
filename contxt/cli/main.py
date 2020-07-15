"""Main CLI"""

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from contxt import __version__
from contxt.auth.cli import CliAuth

from .commands import Assets, Auth, Bus, Contxt, Ems, Iot


def create_parser() -> ArgumentParser:
    # Setup parser
    parser = ArgumentParser(description="Contxt CLI", formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    parser.set_defaults(func=lambda args: parser.print_help())

    # Register subparsers
    parsers = parser.add_subparsers(title="subcommands", dest="command")
    [cls(parsers) for cls in [Assets, Auth, Bus, Contxt, Ems, Iot]]
    return parser


def cli() -> None:
    # Parse args
    parser = create_parser()
    args = parser.parse_args()

    # Launch command
    if "func" in args:
        args.auth = CliAuth()
        args.func(args)


if __name__ == "__main__":
    cli()
