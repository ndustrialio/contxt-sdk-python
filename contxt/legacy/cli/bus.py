from contxt.legacy.cli import ContxtCLI
from contxt.utils import make_logger

logger = make_logger(__name__)

COMMANDS = {
    'channels': {
        'info': 'Channels CLI',
        'functions': [
            {
                'command': 'get-all',
                'method_call_info': {
                    'module': 'contxt.functions.bus',
                    'class': 'Bus',
                    'method': 'get_all_channels_for_service'
                },
                'args': [
                    {
                        'arg': 'organization_id',
                        'required': False,
                        'type': int,
                        'help': 'Provide the organization_id (uuid, str) as a filter'
                    },
                    {
                        'arg': 'organization_name',
                        'required': False,
                        'type': str,
                        'help': 'Provide the organization_name (str) as a filter'
                    },
                    {
                        'arg': 'service_id',
                        'required': True,
                        'type': str,
                        'help': 'Provide the ID (client_id) of the service'
                    }
                ],
            }
        ]
    },
}


class Bus(ContxtCLI):

    def __init__(self, arg_parser):

        super().__init__(arg_parser, COMMANDS)
