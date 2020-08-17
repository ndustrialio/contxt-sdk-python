import inspect
from enum import Enum
from typing import Any, Type, TypeVar, Union

T = TypeVar("T")
_PRIMITIVES = (bool, int, float, str, type(None))


class Null:
    """Null marker"""


class ObjectMapper:
    @staticmethod
    def tree_to_object(tree: object, annotation: Type[T]) -> T:
        """Loads JSON-like structure `tree` into an instance of `annotation`"""

        def failure_msg():
            return f"Failed to parse '{annotation}' from tree: {tree}"

        if tree is None or annotation == Any:
            return tree  # type: ignore
        # detecting generic types
        # note: this check is hacky, don't have a better way to detect generics
        elif type(annotation).__name__ == "_GenericAlias":
            origin = getattr(annotation, "__origin__")
            args = getattr(annotation, "__args__")
            if origin is list:
                assert isinstance(tree, list), failure_msg()
                assert len(args) == 1
                generic_param = args[0]
                return [
                    ObjectMapper.tree_to_object(item, generic_param) for item in tree  # type: ignore
                ]
            elif origin is dict:
                assert isinstance(tree, dict), failure_msg()
                assert len(args) == 2
                key_ann, value_ann = args
                return {
                    ObjectMapper.tree_to_object(k, key_ann): ObjectMapper.tree_to_object(v, value_ann)
                    for k, v in tree.items()
                }  # type: ignore
            elif origin is Union:
                assert any(t for t in args if isinstance(tree, t)), failure_msg()
                return tree  # type: ignore
        elif annotation in _PRIMITIVES:
            try:
                conv = annotation(tree)  # type: ignore
                assert conv == tree
                return conv
            except Exception as e:
                raise AssertionError(failure_msg(), e)
        elif inspect.isclass(annotation):
            if isinstance(tree, annotation):
                return tree
            elif issubclass(annotation, Enum):
                # try to map by enum entry name
                by_name = getattr(annotation, str(tree), None)
                if by_name:
                    return by_name
                # try to map by enum entry value
                assert isinstance(
                    tree, _PRIMITIVES
                ), "Only primitives are supported as Enum values. " + (failure_msg())
                return annotation(tree)  # type: ignore
            elif isinstance(tree, dict):
                # parse as regular class
                args = {}
                # get signature of constructor
                for param in inspect.signature(annotation).parameters.values():
                    raw = tree.get(param.name, Null)
                    if raw is Null:
                        assert param.default is not inspect.Parameter.empty, (
                            f"Missing value for required parameter; "
                            f"type: {annotation}, param: {param}, tree: {tree}. {failure_msg()}"
                        )
                    else:
                        args[param.name] = ObjectMapper.tree_to_object(raw, param.annotation)
                if len(tree) > len(args):
                    # there seem to be some extraneous keys
                    extraneous_keys = [k for k in tree.keys() if k not in args]
                    raise AssertionError(
                        f"Unexpected keys were found while parsing {annotation}. "
                        f"Extraneous keys: {extraneous_keys}, tree: {tree}"
                    )

                # instantiate the annotation class
                return annotation(**args)  # type: ignore

        raise NotImplementedError(failure_msg())

    load = tree_to_object

    @staticmethod
    def object_to_tree(obj):
        """Dumps `obj` to a JSON-like structure"""
        if isinstance(obj, _PRIMITIVES):
            return obj
        elif isinstance(obj, list):
            return list(map(ObjectMapper.object_to_tree, obj))
        elif isinstance(obj, Enum):
            return obj.value
        elif inspect.isclass(obj):
            return obj.__name__
        else:
            dic = obj if isinstance(obj, dict) else vars(obj)
            return {
                ObjectMapper.object_to_tree(k): ObjectMapper.object_to_tree(v) for k, v in dic.items()
            }

    dump = object_to_tree
