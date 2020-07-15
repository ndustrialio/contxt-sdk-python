from jwt import decode

from contxt.services import AuthService


class TestAuthService:
    service = AuthService()

    def test_get_jwks(self):
        jwks = self.service.get_jwks()
        assert "keys" in jwks

    def test_get_token(
        self, identity_access_token: str, audience: str,
    ):
        access_token = self.service.get_token(identity_access_token, audience)["access_token"]
        assert access_token
        identity_claims = decode(identity_access_token, verify=False)
        claims = decode(access_token, verify=False)
        assert claims["sub"] == identity_claims["sub"]
        assert claims["aud"][0] == audience
        assert claims["iss"] == self.service.base_url + "/"

    def test_get_oath_token(
        self, client_id: str, client_secret: str, audience: str,
    ):
        access_token = self.service.get_oauth_token(client_id, client_secret, audience)["access_token"]
        assert access_token
        claims = decode(access_token, verify=False)
        assert claims["sub"] == f"{client_id}@clients"
        assert claims["aud"] == audience
        assert claims["iss"] == self.service.base_url + "/"
