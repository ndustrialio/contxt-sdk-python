import inspect
from enum import Enum
from typing import Type, TypeVar

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

        if tree is None:
            return tree
        # detecting generic types
        # note: this check is hacky, don't have a better way to detect generics
        elif type(annotation).__name__ == "_GenericAlias":
            origin = getattr(annotation, "__origin__")
            if origin is list:
                assert isinstance(tree, list), failure_msg()
                attrs = getattr(annotation, "__args__")
                assert len(attrs) == 1
                generic_param = attrs[0]
                return [
                    ObjectMapper.tree_to_object(item, generic_param) for item in tree
                ]
            elif origin is dict:
                assert isinstance(tree, dict)
                attrs = getattr(annotation, "__args__")
                assert len(attrs) == 2
                key_ann, value_ann = attrs
                return {
                    ObjectMapper.tree_to_object(
                        k, key_ann
                    ): ObjectMapper.tree_to_object(v, value_ann)
                    for k, v in tree.items()
                }
        elif inspect.isclass(annotation):
            if isinstance(tree, annotation):
                return tree
            elif issubclass(annotation, Enum):
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
