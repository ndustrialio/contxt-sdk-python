

class ContxtCLI:

    def __init__(self, auth_module):

        self.auth = auth_module

    def token_for_service(self, audience):
        self.auth.authenticate_to_service(audience)
