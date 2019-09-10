from os import environ

from jose.jwt import get_unverified_claims

from contxt.services import AuthService


class TestAuthService:
    service = AuthService()

    def test_get_jwks(self):
        jwks = self.service.get_jwks()
        assert "keys" in jwks

    def test_get_token(
        self,
        identity_access_token: str = environ.get("TEST_ACCESS_TOKEN"),
        audience: str = environ.get("TEST_AUDIENCE"),
    ):
        access_token = self.service.get_token(identity_access_token, audience)[
            "access_token"
        ]
        assert access_token
        identity_claims = get_unverified_claims(identity_access_token)
        claims = get_unverified_claims(access_token)
        assert claims["sub"] == identity_claims["sub"]
        assert claims["aud"][0] == audience
        assert claims["iss"] == self.service.base_url + "/"

    def test_get_oath_token(
        self,
        client_id: str = environ.get("TEST_CLIENT_ID"),
        client_secret: str = environ.get("TEST_CLIENT_SECRET"),
        audience: str = environ.get("TEST_AUDIENCE"),
    ):
        access_token = self.service.get_oauth_token(client_id, client_secret, audience)[
            "access_token"
        ]
        assert access_token
        claims = get_unverified_claims(access_token)
        assert claims["sub"] == f"{client_id}@clients"
        assert claims["aud"] == audience
        assert claims["iss"] == self.service.base_url + "/"
