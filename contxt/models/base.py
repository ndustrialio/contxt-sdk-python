import dataclasses
from time import time
from typing import Any, ClassVar, Dict, Optional, Type

from marshmallow import Schema as _Schema
from marshmallow_dataclass import dataclass

from contxt.utils import Timer, make_logger

__all__ = ["BaseModel", "dataclass", "field", "RawDict", "UUID"]

logger = make_logger(__name__)

UUID = str  # NOTE: may eventually want actual `uuid`
RawDict = Dict[str, Optional[Any]]


def is_field_creatable(f: dataclasses.Field) -> bool:
    """Returns if field `f` is a valid POST parameter"""
    return f.metadata.get("post", False)


def is_field_updatable(f: dataclasses.Field) -> bool:
    """Returns if field `f` is a valid PUT parameter"""
    return f.metadata.get("put", False)


# TODO:
# (1) Enhance instantiating new classes
# (2) Freeze fields that are not editable
@dataclasses.dataclass
class BaseModel:
    Schema: ClassVar[Type[_Schema]] = _Schema

    @classmethod
    def make(cls, **kwargs) -> "BaseModel":
        """Recommended initializer when creating a temporary instance to send
        as parameters in a POST request. Validates that only creatable fields
        are specified.
        """
        # Check for invalid (non-creatable) keys
        post_keys = {f.name for f in dataclasses.fields(cls) if is_field_creatable(f)}
        invalid_keys = set(kwargs.keys()) - post_keys
        assert not invalid_keys, (
            f"Tried to create {cls.__name__} with non-creatable fields {invalid_keys}."
            f" Creatable keys are {post_keys}."
        )

        # Create dictionary to pass to `cls.__init__`
        # NOTE: we set non-specified keys to `None`, ignoring `Field.default` and
        # `Field.default_factory` since this is just a temporary instance
        clean_dict = {f.name: kwargs.get(f.name) for f in dataclasses.fields(cls)}
        return cls(**clean_dict)

    @classmethod
    def from_dict(cls, data: Any, **kwargs) -> Any:
        """Deserialize a dictionary to a class instance"""
        with Timer() as t:
            instance = cls.Schema(**kwargs).load(data)
        N = len(data) if isinstance(data, list) else 1
        logger.info(f"Deserialized {N} items of type {cls.__name__} in {t.elapsed} s")
        return instance

    def to_dict(self, **kwargs) -> RawDict:
        """Serialize instance to a dictionary"""
        with Timer() as t:
            d = self.Schema(**kwargs).dump(self)
        logger.info(f"Serialized 1 item of type {type(self).__name__} in {t.elapsed} s")
        return d

    def post(self) -> RawDict:
        """Serialize instance for POST request"""
        # TODO: maybe cache these keys
        post_keys = tuple(
            f.name for f in dataclasses.fields(self) if is_field_creatable(f)
        )
        return self.to_dict(only=post_keys)

    def put(self) -> RawDict:
        """Serialize instance for PUT request"""
        # TODO: maybe cache these keys
        put_keys = tuple(
            f.name for f in dataclasses.fields(self) if is_field_updatable(f)
        )
        return self.to_dict(only=put_keys)


def field(
    default: Any = dataclasses.MISSING,
    default_factory: Any = dataclasses.MISSING,
    init: bool = True,
    repr: bool = True,
    hash: Optional[bool] = None,
    compare: bool = True,
    post: bool = False,
    put: bool = False,
    key: Optional[str] = None,
    enum: Optional[bool] = None,
):
    """Convenience alias to forward custom annotations to `metadata`.
    Custom behavior:
     - `post`: denotes field is a valid parameter in a POST request
     - `put`: denotes field is a valid parameter in a PUT request

    Options forwarded to associated `marshmallow.Field`:
     - `key`: defines key to load[dump] from[to]
     - `enum`: denotes field is an `Enum` (supported by `marshmallow_enum`)
    """
    # Build metadata
    metadata: Dict[str, Any] = {"post": post, "put": put}
    if enum:
        metadata["by_value"] = True
    if key:
        metadata["data_key"] = key

    # Forward to dataclasses.field
    return dataclasses.field(
        default=default,
        default_factory=default_factory,
        init=init,
        repr=repr,
        hash=hash,
        compare=compare,
        metadata=metadata,
    )
