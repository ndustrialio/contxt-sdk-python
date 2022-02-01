from typing import Dict, List

from ..utils.persistent_contxt_config import PersistentContxtConfig
import jwt
import logging

from dataclasses import dataclass

logger = logging.getLogger(__name__)
logging.basicConfig(format='[%(module)s %(levelname)s:%(asctime)s] %(message)s', level=logging.INFO)


class SetTokenException(Exception):
    pass

@dataclass
class MachineTokenConfig:
    audience: str
    token: str


@dataclass
class MachineClientConfig:
    clientId: str
    audiences: Dict[str, str]

    def get_token_for_audience(self, audience) -> str:
        token = self.audiences.get(audience)
        if token:
            # decode the token to get some extra info
            try:
                jwt.decode(token, audience=audience, options={"verify_signature": False})
                return token
            except jwt.ExpiredSignatureError:
                logger.info('Expired token detected')


@dataclass
class TokenConfig:
    tokens: List[MachineClientConfig]

    def tokens_for_client(self, client_id: str):
        for client in self.tokens:
            if client.clientId == client_id:
                return client

    def set_token_for_client(self, client_id: str, audience: str, token: str):
        client_config = self.tokens_for_client(client_id)
        if token is None:
            raise SetTokenException('Token cannot be null')
        if client_config is None:
            self.tokens.append(MachineClientConfig(clientId=client_id, audiences={audience: token}))
        else:
            client_config.audiences[audience] = token


class StoredTokenCache(PersistentContxtConfig):

    def __init__(self):
        super().__init__('auth_tokens', TokenConfig)
        self.config = self.load_contxt_file()

    def set_token(self, client_id: str, audience: str, token: str):
        if self.config is None:
            self.config = TokenConfig(tokens=[])
        self.config.set_token_for_client(client_id, audience, token)
        self.write_contxt_file()

    def get_token(self, client_id: str, audience: str) -> str:
        if self.config is not None:
            tokens_for_client = self.config.tokens_for_client(client_id)
            if tokens_for_client:
                return tokens_for_client.get_token_for_audience(audience)

