#!/usr/bin/env python

import argparse

from contxt.cli import ContxtCLI
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
'''
auth_args = sub_parsers.add_parser("auth", help="Authentication CLI Module Commands")
auth_args.add_argument("subcommand")
'''

# iot arg parser


iot_subparser = stack_subparser.add_parser("iot", help="IOT CLI Module Commands")
ems_subparser = stack_subparser.add_parser("ems", help="EMS CLI Module Commands")
#assets_arg_parser = sub_parsers.add_parser("assets", help="Assets CLI Module Commands")
#contxt_arg_parser = sub_parsers.add_parser("contxt", help="Contxt CLI Module Commands")
#bus_arg_parser = sub_parsers.add_parser("bus", help="Bus CLI Module Commands")

# initialize the auth module for clis
cli_auth = CLIAuth()

# initialize the overall cli instance
#cli = ContxtCLI(iot_arg_parser)

# initialize the iot cli module
iot_cli = IOT(iot_subparser)

# initialize the ems cli module
ems_cli = EMS(ems_subparser)

# initialize the assets cli module
#assets_cli = Assets(cli, assets_arg_parser)

# initialize the contxt cli module
#contxt_cli = Contxt(cli, contxt_arg_parser)

# initialize the message bus cli module
#bus_cli = Bus(cli, bus_arg_parser)

args = parser.parse_args()

if args.cli_cmd == "auth":

    if args.subcommand == "login":
        cli_auth.login()
        print('Success!')

    elif args.subcommand == 'reset':
        cli_auth.reset()
        print('Successfully reset tokens')

    else:
        print('Unknown command: {}'.format(args.subcommand))

elif args.cli_cmd == "iot":

    iot_cli.parse_command(args)

elif args.cli_cmd == "ems":

    ems_cli.parse_command(args)

elif args.cli_cmd == 'assets':

    assets_cli.parse_command(args)

elif args.cli_cmd == "contxt":
    contxt_cli.parse_command(args)

elif args.cli_cmd == "bus":
    bus_cli.parse_command(args)
