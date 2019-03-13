from contxt.legacy.cli import ContxtCLI
from contxt.utils import make_logger

logger = make_logger(__name__)

COMMANDS = {
    'organizations': {
        'info': 'Organizations CLI',
        'functions': [
            {
                'command': 'get-all',
                'method_call_info': {
                    'module': 'contxt.services.contxt',
                    'class': 'ContxtService',
                    'method': 'get_organizations'
                },
                'args': []
            },
            {
                'command': 'get-users',
                'method_call_info': {
                    'module': 'contxt.functions.organizations',
                    'class': 'Organizations',
                    'method': 'get_organization_users'
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
                ]
            },
            {
                'command': 'add-user',
                'method_call_info': {
                    'module': 'contxt.services.contxt',
                    'class': 'ContxtService',
                    'method': 'add_user_to_organization'
                },
                'args': [
                    {
                        'arg': 'organization_id',
                        'required': True,
                        'type': str,
                        'help': 'Provide the organization_id (uuid) to add the user to'
                    },
                    {
                        'arg': 'user_id',
                        'required': True,
                        'type': str,
                        'help': 'Provide the user_id (string) of the user to add to the organization'
                    },
                ]
            },
            {
                'command': 'create',
                'method_call_info': {
                    'module': 'contxt.functions.organizations',
                    'class': 'Organizations',
                    'method': 'create_organization'
                },
                'args': [
                    {
                        'arg': 'organization_name',
                        'required': True,
                        'type': str,
                        'help': 'Provide the name of the new organization (surround with quotes if the name has spaces)'
                    }
                ]
            }
        ]
    }
}


class Contxt(ContxtCLI):

    def __init__(self, arg_parser):

        super().__init__(arg_parser, COMMANDS)
