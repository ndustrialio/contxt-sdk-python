#!/usr/bin/env python

import argparse

from contxt.cli.iot import IOT
from contxt.cli.ems import EMS
from contxt.cli.assets import Assets
from contxt.cli.contxt import Contxt
from contxt.cli.bus import Bus
from contxt.utils import make_logger
from contxt.utils.auth import CLIAuth

logger = make_logger(__name__)

parser = argparse.ArgumentParser(description='Contxt CLI')

stack_subparser = parser.add_subparsers(help="Action SubCommand Help", dest="cli_cmd")

cli_auth = CLIAuth()
cli_auth.setup_parser(stack_subparser.add_parser("auth", help="Auth CLI Module"))

subparsers = {
    'auth': cli_auth,
    'iot': IOT(stack_subparser.add_parser("iot", help="IOT CLI Module Commands")),
    'ems': EMS(stack_subparser.add_parser("ems", help="EMS CLI Module Commands")),
    'assets': Assets(stack_subparser.add_parser("assets", help="Assets CLI Module Commands")),
    'contxt': Contxt(stack_subparser.add_parser("contxt", help="Contxt CLI Module Commands")),
    'bus': Bus(stack_subparser.add_parser("bus", help="Bus CLI Module Commands"))
}

args = parser.parse_args()

'''
if args.cli_cmd == "auth":

    if args.subcommand == "login":
        cli_auth.login()
        print('Success!')

    elif args.subcommand == 'reset':
        cli_auth.reset()
        print('Successfully reset tokens')
'''
if args.cli_cmd in subparsers:

    subparsers[args.cli_cmd].parse_command(args)

else:
    logger.critical("Unrecognized command")
