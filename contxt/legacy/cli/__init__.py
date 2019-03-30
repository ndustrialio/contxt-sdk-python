from importlib import import_module

from contxt.utils import make_logger
from contxt.auth.cli import CLIAuth

logger = make_logger(__name__)

# TODO: contxt.cli files are not longer user, remove them
logger.warning('Deprecating ContxtCLI class')


class ContxtCLI:

    def __init__(self, arg_parser, cli_config):

        self.cli_config = cli_config
        self.auth = CLIAuth()
        self.func_definitions = self.init_cli_commands(arg_parser)

    @staticmethod
    def form_method_arguments(func_definition, args):

        method_arguments = {}

        for arg_config in func_definition['args']:
            arg_name = arg_config['arg']

            method_arguments[arg_name] = args.__getattribute__(arg_name)

        return method_arguments

    def init_cli_commands(self, subparser):

        function_call_map = {}

        module_subparser = subparser.add_subparsers(dest='module_command')

        for command, command_info in self.cli_config.items():

            function_call_map[command] = {}
            ems_cmd_parser = module_subparser.add_parser(command, help=command_info['info'])

            ems_subcommand_subparser = ems_cmd_parser.add_subparsers(dest="module_subcommand")

            for func in command_info['functions']:

                function_call_map[command][func['command']] = func

                func_cmd_parser = ems_subcommand_subparser.add_parser(func['command'])

                for arg_dict in func['args']:

                    if arg_dict['type'] == bool:
                        func_cmd_parser.add_argument(
                            f"--{arg_dict['arg']}",
                            action="store_true",
                            help=arg_dict['help'])
                    else:
                        func_cmd_parser.add_argument(
                            f"--{arg_dict['arg']}",
                            required=arg_dict['required'],
                            dest=arg_dict['arg'],
                            choices=arg_dict['valid_values']
                            if 'valid_values' in arg_dict else None,
                            type=arg_dict['type'],
                            help=arg_dict['help'])

        return function_call_map

    def token_for_service(self, audience):
        self.auth.authenticate_to_service(audience)

    def call_function(self, args):

        if args.module_command not in self.func_definitions:
            logger.critical("Cannot locate function for command")
            return

        if args.module_subcommand not in self.func_definitions[args.module_command]:
            logger.critical("Cannot locate function for command")
            return

        func_definition = self.func_definitions[args.module_command][args.module_subcommand]

        method_info = func_definition['method_call_info']

        func_module = import_module(method_info['module'])
        module_class = getattr(func_module, method_info['class'])

        instance = module_class(self.auth)

        module_method = getattr(instance, method_info['method'])

        method_args = self.form_method_arguments(func_definition, args)

        # call the method
        res = module_method(**method_args)

        if 'print_result' in func_definition:
            if func_definition['print_result']:
                print(res)
        elif 'print_handler' in func_definition:
            print_handler = getattr(self, func_definition['print_handler'])
            print_handler(res)
        else:
            print(res)

        if 'to_file_handler' in func_definition:
            file_handler = getattr(self, func_definition['to_file_handler'])
            file_handler(res)

    def parse_command(self, args):

        self.call_function(args)
