from datetime import datetime

from jose import jwt
from jose.constants import ALGORITHMS
from pytz import UTC

from contxt.auth import TokenProvider
from contxt.auth.jwt import AuthError, AuthTokenValidator, ContxtAuthTokenValidator

PRIVATE_KEY = """\
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQC1MZ30SIuWmPgbZcjhoyjauGw4mkzuds/QPGxqhykAs5+3iIzg
zJSLehb9LLrGNzufl2OPu5Bza8LEXpprO8sevajfyOQ45SZ1Kbm0ILrYaLfl1yvF
r6MqHrO07HWsiW9zoHDFU31sd2CoGJsu35fTils1/9Cq7+oWErNfJ61ZPQIDAQAB
AoGAQbAWMmxmZpdYQx54YAy1j+2SFkciIsVh+30cVNZhMAbunSvc3tZr99CwKuKf
Z6K4c9f/WSlHagCkIGqnkr6fmQ4ZhzWkmlkVUdfcK1WVWSidnugivm4Poino3RRG
1YNVYKPa0bgRIsC0ELnNYSd6zH8nK+tsCImpW+Q1qUz6t6ECQQDhSa8KmnwiGEiU
Lgm1sqku18LUmoEaixyx5kUR8f/XOtMxu0yaItgByo0egOVdPFB59C96hNbGfZyg
/L7KmVvFAkEAzeUY2oUr7fmo3AjbU+8f+uNXj8ld1HtXJAoe/1rDw2dHlJad8Q+6
l+J72CvnjnKG/1awo3zl3kJnQshrxn0HGQJBAMt/QUu0q7goczbWNxMXJNcZMfXU
8hVF30+ajn1dORnzGt3rL5BzNOa5TatmBsinOJJQTaq/3zlAMYEBjF15FXkCQA+q
3kBKn/Qk6leMCPyTFrDludUEMrKnjBL+/iraQklNQ6In7+7XDpDeOCRT+vPY/TLS
6vAV4fwOu4LWc3UQMIkCQBRsQj3boQlTGm47AreLBP7kUZ73Kq3RiuaYa14pmMFn
V2Ll5aCxsfioYdKx+8BIyFLgxGPw0ePpwbmIWeDIa3k=
-----END RSA PRIVATE KEY-----
"""

PUBLIC_KEY = """\
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC1MZ30SIuWmPgbZcjhoyjauGw4
mkzuds/QPGxqhykAs5+3iIzgzJSLehb9LLrGNzufl2OPu5Bza8LEXpprO8sevajf
yOQ45SZ1Kbm0ILrYaLfl1yvFr6MqHrO07HWsiW9zoHDFU31sd2CoGJsu35fTils1
/9Cq7+oWErNfJ61ZPQIDAQAB
-----END PUBLIC KEY-----
"""


class TestAuthTokenValidator:
    def main(self):
        self.test_auth()

    def test_auth(self):
        audience = "foo_audience"
        issuer = "foo_issuer"
        claims = {"foo": "bar", "aud": audience, "iss": issuer}
        token = jwt.encode(claims, PRIVATE_KEY, algorithm=ALGORITHMS.RS256)
        validator = AuthTokenValidator(
            audience=audience, issuer=issuer, public_key=PUBLIC_KEY
        )
        payload = validator.validate(token)
        assert claims == payload


class TestContxtAuthTokenValidator:
    def main(self):
        self.test_contxt_auth()

    def test_contxt_auth(self):
        token_validator = ContxtAuthTokenValidator(audience="foo_audience")
        try:
            token_validator.validate("bad_token")
            raise AssertionError(
                "Token validation should have raised a token error before"
            )
        except AuthError:
            pass


class TestTokenProvider:
    claims = {"foo": "bar", "aud": "foo_audience", "iss": "foo_issuer"}

    class DummyTokenProvider(TokenProvider):
        @TokenProvider.access_token.getter
        def access_token(self):
            if self._access_token is None or self._token_expiring(within=0):
                self._claims = {
                    **TestTokenProvider.claims,
                    "exp": datetime.now(UTC).timestamp(),
                }
                self.access_token = jwt.encode(
                    self._claims, PRIVATE_KEY, algorithm=ALGORITHMS.RS256
                )
            return self._access_token

    def main(self):
        self.test_token_provider()

    def test_token_provider(self):
        token_provider = self.DummyTokenProvider(audience=self.claims["aud"])
        # Test first token is set
        token0 = token_provider.access_token
        assert token0
        assert token_provider.decoded_access_token == token_provider._claims
        # Test token is refreshed and different than before
        token1 = token_provider.access_token
        assert token1
        assert token_provider.decoded_access_token == token_provider._claims
        assert token0 != token1


if __name__ == "__main__":
    TestAuthTokenValidator().main()
    TestContxtAuthTokenValidator().main()
    TestTokenProvider().main()
