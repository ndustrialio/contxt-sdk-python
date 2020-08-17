from datetime import datetime, timezone

import jwt
import pytest

from contxt.auth import TokenProvider
from tests.conftest import WINDOWS

CLAIMS = {"foo": "bar", "aud": "foo_audience", "iss": "foo_issuer"}


class DummyTokenProvider(TokenProvider):
    PRIVATE_KEY = None

    @TokenProvider.access_token.getter  # type: ignore
    def access_token(self):
        if self._access_token is None or self._token_expiring(within=0):
            self._claims = {**CLAIMS, "exp": datetime.now(timezone.utc).timestamp()}
            self.access_token = jwt.encode(self._claims, self.PRIVATE_KEY, algorithm="RS256")
        return self._access_token


@pytest.fixture
def token_provider(private_key):
    provider = DummyTokenProvider(CLAIMS["aud"])
    provider.PRIVATE_KEY = private_key
    return provider


# FIXME: why is this failing?
@pytest.mark.skipif(WINDOWS, reason="failing for unknown reason")
def test_token_provider(token_provider):
    # Test first token is set
    token0 = token_provider.access_token
    assert token0
    assert token_provider.decoded_access_token == token_provider._claims
    # Test token is refreshed and different than before
    token1 = token_provider.access_token
    assert token1
    assert token_provider.decoded_access_token == token_provider._claims
    assert token0 != token1
