from dataclasses import dataclass

import pytest

from contxt.utils.object_mapper import ObjectMapper


@dataclass
class Foo:
    foo: int
    bar: float
    baz: str


@pytest.mark.parametrize(
    "cls, raw",
    [(Foo, {"foo": 1, "bar": 42.31, "baz": "baz"}), (Foo, {"foo": 1, "bar": 4, "baz": "baz"})],
)
def test_load(cls, raw):
    actual = ObjectMapper.load(raw, cls)
    assert raw == vars(actual)


@pytest.mark.parametrize("cls, raw", [(Foo, {"foo": 1, "bar": 4, "baz": "baz"})])
def test_load_and_dump(cls, raw):
    actual = ObjectMapper.dump(ObjectMapper.load(raw, cls))
    assert raw == actual
