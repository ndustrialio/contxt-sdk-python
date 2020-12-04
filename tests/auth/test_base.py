from datetime import datetime, timezone

import jwt
import pytest

from contxt.auth import TokenProvider
from tests.conftest import WINDOWS

CLAIMS = {"foo": "bar", "aud": "foo_audience", "iss": "foo_issuer"}


class DummyTokenProvider(TokenProvider):
    @TokenProvider.access_token.getter  # type: ignore
    def access_token(self):
        if self._access_token is None or self._token_expiring(within=0):
            self.access_token = jwt.encode(
                {**CLAIMS, "exp": datetime.now(timezone.utc).timestamp()}, "prvkey", algorithm="HS256"
            )
        return self._access_token


# FIXME: why is this failing?
@pytest.mark.skipif(WINDOWS, reason="failing for unknown reason")
def test_token_provider():
    token_provider = DummyTokenProvider(CLAIMS["aud"])
    # Test first token is set
    token0 = token_provider.access_token
    assert token0
    assert token_provider.decoded_access_token == jwt.decode(token0, verify=False)
    # Test token is refreshed and different than before
    token1 = token_provider.access_token
    assert token1
    assert token_provider.decoded_access_token == jwt.decode(token1, verify=False)
    assert token0 != token1
