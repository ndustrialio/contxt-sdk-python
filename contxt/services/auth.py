from typing import Dict, List, Union, Optional
from pathlib import Path
import os
from .api import ApiEnvironment, ConfiguredApi
from ..auth import Auth
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


class StoredTokenCache:

    def __init__(self):
        self.token_config = self._load_token_file()

    def _write_token_file(self):
        base_contxt_dir = os.path.join(str(Path.home()), '.contxt')
        if not os.path.exists(base_contxt_dir):
            os.mkdir(base_contxt_dir)
        contxt_file_name = os.path.join(base_contxt_dir, 'auth_tokens')
        write_config_class_to_file(contxt_file_name, self.token_config, TokenConfig)

    def _load_token_file(self) -> TokenConfig:
        contxt_file_name = os.path.join(str(Path.home()), '.contxt', 'auth_tokens')
        if os.path.exists(contxt_file_name):
            config = load_config_class_from_file(contxt_file_name, TokenConfig)
            return config

    def set_token(self, client_id: str, audience: str, token: str):
        if self.token_config is None:
            self.token_config = TokenConfig(tokens=[])
        self.token_config.set_token_for_client(client_id, audience, token)
        self._write_token_file()

    def get_token(self, client_id: str, audience: str) -> str:
        if self.token_config is not None:
            tokens_for_client = self.token_config.tokens_for_client(client_id)
            if tokens_for_client:
                return tokens_for_client.get_token_for_audience(audience)


class AuthService(ConfiguredApi):
    """Auth API client"""

    def __init__(self, env: str = "production", **kwargs) -> None:
        super().__init__(env=env, **kwargs)
        self.token_cache = StoredTokenCache()

    _envs = (
        ApiEnvironment(
            name="production",
            baseUrl="https://contxtauth.com/v1",
            clientId="75wT048QcpE7ujwBJPPjr263eTHl4gEX",
        ),
        ApiEnvironment(
            name="staging",
            baseUrl="https://contxt-auth-service.staging.ndustrial.io/v1",
            clientId="7TceUsM1eC4nKmdoC717383DWyfc9QoY",
        ),
    )

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
        cached_token = self.token_cache.get_token(client_id=client_id,
                                                  audience=audience)

        if cached_token is None:
            logger.info('Token not found for client...fetching new one')
            resp = self.post(
                "oauth/token",
                json={
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "audience": audience,
                    "grant_type": "client_credentials",
                },
            )
            self.token_cache.set_token(client_id=client_id,
                                       audience=audience,
                                       token=resp['access_token'])
            return resp['access_token']
        else:
            logger.info('Using cached token')
            return cached_token
