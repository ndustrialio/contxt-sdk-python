import jwt
import pytest

from contxt.auth.jwt import ContxtTokenValidator, InvalidTokenError, TokenValidator


def test_token_validator(public_key, private_key):
    audience = "foo_audience"
    issuer = "foo_issuer"
    claims = {"foo": "bar", "aud": audience, "iss": issuer}
    token = jwt.encode(claims, private_key, algorithm="RS256")
    validator = TokenValidator(audience=audience, issuer=issuer, public_key=public_key)
    payload = validator.validate(token)
    assert claims == payload


def test_contxt_token_validator():
    token_validator = ContxtTokenValidator(audience="foo_audience")
    with pytest.raises(InvalidTokenError):
        token_validator.validate("bad_token")
