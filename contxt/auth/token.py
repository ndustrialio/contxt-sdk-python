from typing import NamedTuple

import jwt
import requests

# NOTE: this code was originally stolen from https://auth0.com/docs/quickstart/backend/python/01-authorization
#       then tweaked for convenience


# Error handler
class AuthError(Exception):
    def __init__(self, message):
        self.message = message


class Algorithms:
    RS256 = "RS256"


TokenPayload = dict


class AuthTokenValidator(NamedTuple):
    audience: str
    issuer: str
    public_key: str

    def validate(self, token: str) -> TokenPayload:
        try:
            return jwt.decode(jwt=token, key=self.public_key, algorithms=Algorithms.RS256,
                              audience=self.audience, issuer=self.issuer)
        except jwt.PyJWTError as e:
            raise AuthError(f"INVALID_TOKEN: {str(e)}")
        except Exception:
            raise AuthError("INVALID_HEADER: Unable to parse authentication")


CONTXT_AUTH0_ISSUER = "https://contxtauth.com/v1/"
CONTXT_AUTH0_JWKS_URL = f"{CONTXT_AUTH0_ISSUER}.well-known/jwks.json"


def _get_jwks() -> str:
    try:
        return _get_jwks.jwks
    except AttributeError:
        # caching the jwks
        resp = requests.get(CONTXT_AUTH0_JWKS_URL)
        _get_jwks.jwks = resp.content
        return _get_jwks.jwks


class ContxtAuthTokenValidator:

    def __init__(self, audience: str):
        self.delegate = AuthTokenValidator(audience=audience, issuer=CONTXT_AUTH0_ISSUER,
                                           public_key=_get_jwks())

    def validate(self, token: str) -> TokenPayload:
        return self.delegate.validate(token)
