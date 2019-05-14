from contxt.auth import BaseAuth, TokenProvider


class MachineTokenProvider(TokenProvider):
    pass


class MachineAuth(BaseAuth):
    """
    Same as `BaseAuth`, but specifically for a non-human client, such as a
    service, api, or worker.
    """

    def get_token_provider(self, audience: str) -> MachineTokenProvider:
        """Get `MachineTokenProvider` for audience `audience`"""
        return MachineTokenProvider(self.client_id, self.client_secret, audience)
