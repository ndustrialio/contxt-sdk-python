from abc import ABC
from typing import Dict, List, Union, Optional
from pathlib import Path
import os
from auth0.v3.authentication import GetToken
from .api import ApiEnvironment, ConfiguredLegacyApi, ConfiguredGraphApi
from ..auth import Auth
from ..utils.config import ContxtEnvironmentConfig
from ..utils.stored_file import PersistentContxtConfig
import jwt
import logging

from dataclasses import dataclass
from contxt.utils.config import load_config_class_from_file, write_config_class_to_file


logger = logging.getLogger(__name__)
logging.basicConfig(format='[%(module)s %(levelname)s:%(asctime)s] %(message)s', level=logging.INFO)


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
        if client_config is None:
            self.tokens.append(MachineClientConfig(clientId=client_id, audiences={audience: token}))
        else:
            client_config.audiences[audience] = token


class StoredTokenCache(PersistentContxtConfig):

    def __init__(self):
        super().__init__('auth_tokens', TokenConfig)
        self.token_config = self.load_contxt_file()

    def set_token(self, client_id: str, audience: str, token: str):
        if self.token_config is None:
            self.token_config = TokenConfig(tokens=[])
        self.token_config.set_token_for_client(client_id, audience, token)
        self.write_contxt_file()

    def get_token(self, client_id: str, audience: str) -> str:
        if self.token_config is not None:
            tokens_for_client = self.token_config.tokens_for_client(client_id)
            if tokens_for_client:
                return tokens_for_client.get_token_for_audience(audience)


class AuthService(ConfiguredGraphApi, ABC):
    """Auth API client"""

    def __init__(self, contxt_env: ContxtEnvironmentConfig, **kwargs) -> None:
        super().__init__(contxt_env=contxt_env, **kwargs)
        self.service_env = contxt_env
        self.token_cache = StoredTokenCache()

    def get_jwks(self) -> Dict:
        return self.get(".well-known/jwks.json")

    def get_token(self, access_token: str, audiences: Union[str, List[str]]) -> Dict:
        audiences = [audiences] if isinstance(audiences, str) else audiences
        return self.post(
            "token", json={"audiences": audiences}, headers={"Authorization": f"Bearer {access_token}"}
        )

    def get_cluster_config(self, access_token: str, host: str) -> Dict:
        return self.post(
            "clusterconfig", headers={"Authorization": f"Bearer {access_token}"}, json={"host": host}
        )

    def get_oauth_token(self, client_id: str, client_secret: str, audience: str) -> str:
        cached_token = self.token_cache.get_token(client_id=self.service_env.clientId,
                                                  audience=self.service_env.apiEnvironment.clientId)
        if cached_token is None:
            logger.info('Token not found for client...fetching new one')
            req = GetToken(self.service_env.apiEnvironment.authProvider)
            print(self.service_env.apiEnvironment.authProvider, self.service_env.clientId, self.service_env.clientSecret, self.service_env.apiEnvironment.clientId)
            token = req.client_credentials(client_id=self.service_env.clientId,
                                           client_secret=self.service_env.clientSecret,
                                           audience=self.service_env.apiEnvironment.clientId)
            self.token_cache.set_token(client_id=self.service_env.clientId,
                                       audience=self.service_env.apiEnvironment.clientId,
                                       token=token['access_token'])

            print(token)
            return token['access_token']
        else:
            logger.info('Using cached token')
            return cached_token
