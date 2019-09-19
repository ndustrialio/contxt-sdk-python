from time import time

import pytest
from requests.exceptions import HTTPError, RetryError

from contxt.services.api import Api, ApiRetry


class TestBaseApi:
    def test_retries(self):
        retry = ApiRetry()
        api = Api("http://httpbin.org", retry=retry)
        t0 = time()
        try:
            api.get("status/500")
        except RetryError as e:
            pass
        t = time() - t0
        assert t >= sum(retry.backoff_factor * (2 ** n) for n in range(retry.total))

    def test_without_retires(self):
        api = Api("http://httpbin.org", retry=None)
        try:
            api.get("status/500")
        except HTTPError as e:
            pass


TestBaseApi().test_retries()
TestBaseApi().test_without_retires()
