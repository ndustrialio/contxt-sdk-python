from time import time

import pytest
from requests.exceptions import HTTPError

from contxt.services.api import Api, ApiRetry


def test_retries():
    retry = ApiRetry()
    api = Api("https://httpbin.org", retry=retry)
    t0 = time()
    with pytest.raises(HTTPError) as e:
        api.get("status/500")
    t = time() - t0
    assert e.value.response.status_code == 500
    assert t >= sum(retry.backoff_factor * (2**n) for n in range(retry.total)) * 0.9


def test_without_retries():
    api = Api("https://httpbin.org", retry=None)
    with pytest.raises(HTTPError) as e:
        api.get("status/500")
    assert e.value.response.status_code == 500
