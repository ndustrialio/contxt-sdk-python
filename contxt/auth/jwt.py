from typing import NamedTuple

import requests
from jose import jwt
from jose.constants import ALGORITHMS


# NOTE: this code was originally stolen from https://auth0.com/docs/quickstart/backend/python/01-authorization
#       then tweaked for convenience


# Error handler
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


TokenPayload = dict


class AuthTokenValidator(NamedTuple):
    audience: str
    issuer: str
    public_key: str

    def validate(self, token: str) -> TokenPayload:
        try:
            return jwt.decode(token=token, key=self.public_key, algorithms=ALGORITHMS.RS256, audience=self.audience,
                              issuer=self.issuer)
        except jwt.ExpiredSignatureError:
            raise AuthError({"code": "token_expired",
                             "description": "token is expired"}, 401)
        except jwt.JWTClaimsError:
            raise AuthError({"code": "invalid_claims",
                             "description":
                                 "incorrect claims,"
                                 "please check the audience and issuer"}, 401)
        except jwt.JWTError:
            raise AuthError({"code": "invalid_token",
                             "description":
                                 "invalid token, "
                                 "please check the token"}, 401)
        except Exception:
            raise AuthError({"code": "invalid_header",
                             "description":
                                 "Unable to parse authentication"
                                 " token."}, 401)


class ContxtAuthTokenValidator:
    AUTH0_ISSUER = "https://contxtauth.com/v1/"
    AUTH0_JWKS_URL = f"{AUTH0_ISSUER}.well-known/jwks.json"

    AUTH0_JWKS = None

    def __init__(self, audience: str):
        self.delegate = AuthTokenValidator(audience=audience, issuer=ContxtAuthTokenValidator.AUTH0_ISSUER,
                                           public_key=ContxtAuthTokenValidator._get_jwks())

    @staticmethod
    def _get_jwks() -> str:
        global AUTH0_JWKS
        global AUTH0_JWKS_URL
        if AUTH0_JWKS is None:
            resp = requests.get(AUTH0_JWKS_URL)
            AUTH0_JWKS = resp.content
        return AUTH0_JWKS

    def validate(self, token: str) -> TokenPayload:
        return self.delegate.validate(token)
