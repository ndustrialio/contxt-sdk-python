import sys

import pytest

WINDOWS = sys.platform.startswith("win")


@pytest.fixture
def public_key():
    return """\
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC1MZ30SIuWmPgbZcjhoyjauGw4
mkzuds/QPGxqhykAs5+3iIzgzJSLehb9LLrGNzufl2OPu5Bza8LEXpprO8sevajf
yOQ45SZ1Kbm0ILrYaLfl1yvFr6MqHrO07HWsiW9zoHDFU31sd2CoGJsu35fTils1
/9Cq7+oWErNfJ61ZPQIDAQAB
-----END PUBLIC KEY-----
"""


@pytest.fixture
def private_key():
    return """\
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
