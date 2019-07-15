import inspect
from enum import Enum
from typing import Any, Type, TypeVar, Union

_PRIMITIVES = (bool, int, float, str, type(None))


class Null:
    """Null marker"""


T = TypeVar("T")


class ObjectMapper:
    @staticmethod
    def tree_to_object(tree: object, annotation: Type[T]) -> T:
        """
        Maps a JSON like tree to an object of the class specified by the type
        annotation `annotation`
        :param tree: input object to recursively parse, tree should have a
            JSON-like structure:
            - List
            - Dict
            - Primitive
        :param annotation: output type description to use for parsing,
        if a string is received a type with the given name will be parsed
        :return: parsed object
        """

        def failure_msg():
            return f"Failed to parse '{annotation}' from tree: {tree}"

        if tree is None or annotation == Any:
            return tree
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
                    ObjectMapper.tree_to_object(item, generic_param) for item in tree
                ]
            elif origin is dict:
                assert isinstance(tree, dict), failure_msg()
                assert len(args) == 2
                key_ann, value_ann = args
                return {
                    ObjectMapper.tree_to_object(
                        k, key_ann
                    ): ObjectMapper.tree_to_object(v, value_ann)
                    for k, v in tree.items()
                }
            elif origin is Union:
                assert any(t for t in args if isinstance(tree, t)), failure_msg()
                return tree
        elif annotation in _PRIMITIVES:
            assert isinstance(tree, annotation), failure_msg()
            return tree
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
                return annotation(tree)
            elif isinstance(tree, dict):
                # parse as regular class
                args = {}
                # get signature of constructor
                for param in inspect.signature(annotation).parameters.values():
                    raw = tree.get(param.name, Null)
                    if raw is Null:
                        assert param.default is not inspect.Parameter.empty, (
                            f"Missing value for required parameter; "
                            f"type: {annotation}, param: {param}, tree: {tree}."
                            + " "
                            + failure_msg()
                        )
                    else:
                        args[param.name] = ObjectMapper.tree_to_object(
                            raw, param.annotation
                        )
                if len(tree) > len(args):
                    # there seem to be some extraneous keys
                    extraneous_keys = [k for k in tree.keys() if k not in args]
                    raise AssertionError(
                        f"Unexpected keys were found while parsing {annotation}. "
                        f"Extraneous keys: {extraneous_keys}, tree: {tree}"
                    )

                # instantiate the annotation class
                return annotation(**args)

        raise NotImplementedError(failure_msg())

    @staticmethod
    def object_to_tree(obj):
        """
        Maps an object to a JSON like tree
        :return: JSON like tree
        """
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
                ObjectMapper.object_to_tree(k): ObjectMapper.object_to_tree(v)
                for k, v in dic.items()
            }
