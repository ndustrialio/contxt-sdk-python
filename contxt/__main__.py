#!/usr/bin/env python3

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
from typing import List, Tuple

from contxt import __version__
from contxt.cli.parsers import ContxtArgParser


def create_parser() -> Tuple[ArgumentParser, List[ContxtArgParser]]:
    # Setup parser
    root_parser = ArgumentParser(description="Contxt CLI", formatter_class=ArgumentDefaultsHelpFormatter)
    root_parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {__version__}")
    root_parser.set_defaults(func=lambda auth, args: root_parser.print_help())

    # Setup our subparsers, which are subclassed from ContxtArgParser
    parsers = root_parser.add_subparsers(title="subcommands", dest="command")
    subparsers = [cls(parsers) for cls in ContxtArgParser.__subclasses__()]

    return root_parser, subparsers


def main() -> None:
    """Main CLI"""
    parser, subparsers = create_parser()
    args = parser.parse_args()

    # Launch the command
    if "func" in args:
        from contxt.auth.cli import CliAuth

        args.func(args, CliAuth())


if __name__ == "__main__":
    main()
