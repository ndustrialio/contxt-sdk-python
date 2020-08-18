import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Union

from jwt import PyJWTError, algorithms, decode, get_unverified_header

from ..services import AuthService
from ..utils import make_logger

logger = make_logger(__name__)


class InvalidTokenError(Exception):
    """Invalid JWT"""


@dataclass
class TokenValidator:
    audience: str
    issuer: str
    public_key: Union[str, Dict]
    algorithms: List[str] = field(default_factory=lambda: ["RS256"])

    def _get_public_key(self, token: str) -> str:
        if isinstance(self.public_key, dict):
            header = get_unverified_header(token)
            return self.public_key[header["kid"]]
        return self.public_key

    def validate(self, token: str, **kwargs) -> Dict[str, Any]:
        """Validates `token`"""
        try:
            return decode(
                jwt=token,
                key=self._get_public_key(token),
                algorithms=self.algorithms,
                audience=self.audience,
                issuer=self.issuer,
                **kwargs,
            )
        except PyJWTError as e:
            logger.exception(e)
            raise InvalidTokenError(f"INVALID_TOKEN: {str(e)}")
        except Exception as e:
            logger.exception(e)
            raise InvalidTokenError("MALFORMED_TOKEN: failed to parse token")


class ContxtTokenValidator(TokenValidator):
    def __init__(self, audience: str) -> None:
        api = AuthService()
        super().__init__(
            audience=audience,
            issuer=api.base_url,
            public_key={
                jwk["kid"]: algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))
                for jwk in api.get_jwks()["keys"]
            },
            algorithms=["RS256"],
        )
