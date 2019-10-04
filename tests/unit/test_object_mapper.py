from dataclasses import dataclass

from contxt.utils.object_mapper import ObjectMapper as om


@dataclass
class Foo:
    foo: int
    bar: float
    foe: str


class TestObjectMapper:
    def test__tree_to_object(self):
        bar = {"foo": 1, "bar": 42.31, "foe": "feo"}
        foo = om.tree_to_object(bar, Foo)
        assert vars(foo) == bar

    def test__tree_to_object__int_to_float(self):
        bar = {"foo": 1, "bar": 4, "foe": "feo"}
        foo = om.tree_to_object(bar, Foo)
        assert vars(foo) == bar

    def test__round_trip(self):
        bar = {"foo": 1, "bar": 4, "foe": "feo"}
        foo = om.object_to_tree(om.tree_to_object(bar, Foo))
        assert foo == bar


if __name__ == "__main__":
    TestObjectMapper().test__round_trip()
