from typing import Dict, List, Union, Any
from json import dump, load
from pathlib import Path

from ..utils import make_logger
from .api import ApiEnvironment, ConfiguredApi

logger = make_logger(__name__)


class AuthService(ConfiguredApi):
    """Auth API client"""

    _envs = (
        ApiEnvironment(
            name="production",
            base_url="https://contxtauth.com/v1",
            client_id="https://auth.opencontxt.com",
        ),
    )

    def __init__(self, env: str = "production",
                 cache_file: str = Path.home() / ".contxt" / "tokens",
                 **kwargs) -> None:
        super().__init__(env=env, **kwargs)
        self._cache_file = cache_file
        self._tokens = {}
        self._init_from_cache()

    def _init_from_cache(self) -> None:
        if self._cache_file:
            # Load the cache
            cache = self.read_cache()

            if cache:
                # Config file exists, let's set our local tokens
                logger.info("Setting tokens from cache")
                self._tokens = cache
            else:
                logger.info("Token cache not found")

    def read_cache(self) -> Dict[str, Any]:
        if self._cache_file:
            logger.debug(f"Reading cache {self._cache_file}")
            if self._cache_file.is_file():
                with self._cache_file.open("r") as f:
                    return load(f)
        return {}

    def update_cache(self) -> None:
        if self._cache_file:
            logger.info(f"Updating cache {self._cache_file}")
            self._cache_file.parent.mkdir(parents=True, exist_ok=True)
            with self._cache_file.open("w") as f:
                dump(self._tokens, f, indent=4)

    def clear_cache(self) -> None:
        if self._cache_file:
            logger.debug(f"Clearing cache {self._cache_file}")
            if self._cache_file.is_file():
                self._cache_file.unlink()

    def get_jwks(self) -> Dict:
        return self.get(".well-known/jwks.json")

    def get_token(self, access_token: str, audiences: Union[str, List[str]]) -> Dict:
        audiences = [audiences] if isinstance(audiences, str) else audiences
        aud = audiences[0]
        if aud in self._tokens:
            logger.debug("Using cached token")
            #ContxtTokenValidator(aud).validate(self._tokens["access_token"])
            return self._tokens[aud]
        logger.debug("Requesting new token")
        resp = self.post(
            "token", json={"audiences": audiences}, headers={"Authorization": f"Bearer {access_token}"}
        )
        self._tokens[aud] = resp
        self.update_cache()
        return resp

    def get_oauth_token(self, client_id: str, client_secret: str, audience: str) -> Dict:
        print(f'Getting token for ${client_id}')
        return self.post(
            "oauth/token",
            json={
                "client_id": client_id,
                "client_secret": client_secret,
                "audience": audience,
                "grant_type": "client_credentials",
            },
        )
