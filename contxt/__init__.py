#!/usr/bin/env python3
# PYTHON_ARGCOMPLETE_OK

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from argcomplete import autocomplete

from contxt.cli.parsers import ArgParser


def main():
    # Setup parser and our subparsers, which are subclassed from ArgParser
    root_parser = ArgumentParser(
        description="Contxt CLI",
        formatter_class=ArgumentDefaultsHelpFormatter)
    parsers = root_parser.add_subparsers(title="subcommands", dest="command")
    subparsers = [cls(parsers) for cls in ArgParser.__subclasses__()]

    # Setup tab autocompletion and parse args
    autocomplete(root_parser)
    args = root_parser.parse_args()

    # Launch the command
    if "func" in args:
        from contxt.utils.auth import CLIAuth
        auth = CLIAuth()
        args.func(args, auth)
    else:
        # Subcommand not specified, print all subparser usages as help
        for p in subparsers:
            p.parser.print_usage()


if __name__ == "__main__":
    main()
