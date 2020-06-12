from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from . import __version__
from .auth.cli import CliAuth
from .cli.parsers import ContxtArgParser


def create_parser() -> ArgumentParser:
    # Setup parser
    parser = ArgumentParser(description="Contxt CLI", formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    parser.set_defaults(func=lambda auth, args: parser.print_help())

    # Register subparsers
    parsers = parser.add_subparsers(title="subcommands", dest="command")
    [cls(parsers) for cls in ContxtArgParser.__subclasses__()]
    return parser


def cli() -> None:
    """Main CLI"""
    parser = create_parser()
    args = parser.parse_args()

    # Launch the command
    if "func" in args:
        args.func(args, CliAuth())


if __name__ == "__main__":
    cli()
