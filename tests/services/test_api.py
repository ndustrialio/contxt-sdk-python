from time import time

import pytest
from requests.exceptions import HTTPError

from contxt.services.api import Api, ApiRetry


@pytest.mark.skip(reason="Mock this instead")
def test_retries(self):
    retry = ApiRetry()
    api = Api("https://httpbin.org", retry=retry)
    t0 = time()
    with pytest.raises(HTTPError) as e:
        api.get("status/500")
    t = time() - t0
    assert e.value.response.status_code == 500
    assert t >= sum(retry.backoff_factor * (2 ** n) for n in range(retry.total))


@pytest.mark.skip(reason="Mock this instead")
def test_without_retries(self):
    api = Api("https://httpbin.org", retry=None)
    with pytest.raises(HTTPError) as e:
        api.get("status/500")
    assert e.value.response.status_code == 500
