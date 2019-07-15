from abc import ABC, abstractmethod
from ast import literal_eval
from copy import deepcopy
from datetime import date as _date
from datetime import datetime as _datetime
from importlib import import_module
from typing import Any, Callable, Dict, Optional, Tuple, Union

from dateutil import parser
from pytz import UTC, ZERO

from contxt.utils import make_logger
from contxt.utils.serializer import Serializer

logger = make_logger(__name__)


class Parsers:
    """
    Parsers to deserialize JSON as Python.
    """

    boolean = bool
    number = float
    string = str

    @staticmethod
    def date(datestamp: str) -> _date:
        return _date.fromisoformat(datestamp)

    @staticmethod
    def datetime(timestamp: str, strict: bool = True) -> _datetime:
        if strict:
            return _datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ").replace(
                tzinfo=UTC
            )
        return parser.parse(timestamp)

    @staticmethod
    def unknown(value: Any) -> Any:
        # First, try a general parser (supports strings, numbers, tuples,
        # lists, dicts, booleans (True/False strings only), and None)
        try:
            return literal_eval(value)
        except (SyntaxError, ValueError):
            pass
        # Next, fall back to a strict datetime parser
        try:
            return Parsers.datetime(value)
        except (TypeError, ValueError):
            pass
        # Next, fall back to a general datetime parser
        try:
            return Parsers.datetime(value, strict=False)
        except (TypeError, ValueError):
            pass
        # Next, convert bool-type strings
        try:
            if value.lower() in ("yes", "true"):
                return True
            elif value.lower() in ("no", "false"):
                return False
        except (AttributeError, TypeError, ValueError):
            pass
        # Failed, return original value
        return value


class Formatters:
    """
    Formatters to serialize Python as JSON.
    """

    @staticmethod
    def date(d: _date) -> str:
        return d.isoformat()

    @staticmethod
    def datetime(dt: _datetime, strict: bool = True) -> str:
        if dt.utcoffset() != ZERO and strict:
            # Require timezone to be UTC
            raise AssertionError(f"Datetime must be UTC, not {dt.tzinfo}")
        # NOTE: almost exactly the same as isoformat(), but ensures
        # microseconds are always represented
        return dt.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

    @staticmethod
    def normalize_label(text: str) -> str:
        return text.lower().replace(" ", "_")


# TODO: Need a way to track changed attributes
# TODO: This custom schema-validation can be replaced by a more robust
# (although slower) implementation: see https://github.com/marshmallow-code/marshmallow
class ApiField:
    """
    A field retrieved from an API service.

    `api_key` is the expected key, `attr_key` is the desired class attribute key,
    `data_type` is the object type.
    """

    def __init__(
        self,
        api_key: str,
        attr_key: Optional[str] = None,
        data_type: Union[Callable, str] = str,
        creatable: bool = False,
        updatable: bool = False,
        optional: bool = False,
    ):
        self.api_key = api_key
        self.attr_key = attr_key or api_key
        self._data_type = data_type
        self.creatable = creatable
        self.updatable = updatable
        self.optional = optional

    @property
    def data_type(self):
        if isinstance(self._data_type, str):
            # Load callable from str
            # NOTE: this is to delay the type assignment to instance creation,
            # as the type might not yet be defined at class creation
            modname, qualname_separator, qualname = self._data_type.partition(":")
            obj = import_module(modname)
            if qualname_separator:
                for attr in qualname.split("."):
                    obj = getattr(obj, attr)
            self._data_type = obj
        return self._data_type


class ApiObject(ABC):
    """
    An abstract base class for a response from an API. This class serves to
    take a raw response from an API and create a parsed Python object.
    """

    # _creatable_fields = None
    # _updatable_fields = None

    def __str__(self):
        return Serializer.to_table(self)

    @property
    @classmethod
    @abstractmethod
    def _api_fields(cls) -> Tuple[ApiField, ...]:
        pass

    @property
    def creatable_fields(self) -> Dict[str, ApiField]:
        cls = type(self)
        if not hasattr(cls, "_creatable_fields"):
            cls._creatable_fields = {
                f.attr_key: f for f in cls._api_fields if f.creatable
            }
        return cls._creatable_fields

    @property
    def updatable_fields(self) -> Dict[str, ApiField]:
        cls = type(self)
        if not hasattr(cls, "_updatable_fields"):
            cls._updatable_fields = {
                f.attr_key: f for f in cls._api_fields if f.updatable
            }
        return cls._updatable_fields

    @classmethod
    def from_api(cls, api_dict: Dict):
        api_dict = deepcopy(api_dict)
        # Create clean dictionary to pass to init
        clean_dict = {}
        for field in cls._api_fields:
            if field.api_key not in api_dict and not field.optional:
                raise KeyError(
                    f"Required API field '{field.api_key}' is missing from"
                    f" response: {api_dict}"
                )
            clean_dict[field.attr_key] = cls.clean_api_value(
                field=field, value=api_dict.pop(field.api_key, None)
            )

        # Warn of any unused keys
        for k in api_dict.keys():
            logger.warning(f"{cls.__name__}: Unexpected key from api {k}")

        # Return new instance
        return cls(**clean_dict)

    @classmethod
    def clean_api_value(cls, field: ApiField, value: Any):
        if value is None:
            # No value
            return value
        elif isinstance(value, (list, tuple)):
            # Value is a list, clean each item
            return [cls.clean_api_value(field, v) for v in value]
        # elif issubclass(field.data_type, ApiObject):
        elif callable(getattr(field.data_type, "from_api", None)):
            # Type is an ApiObject, apply from_api instead of init
            return field.data_type.from_api(value)
        else:
            # Apply type
            return field.data_type(value)

    def get_dict(self):
        # TODO: deprecate, call Serializer directly
        return Serializer.to_dict(self)

    def get_df(self):
        # TODO: deprecate, call Serializer directly
        return Serializer.to_df(self)

    def post(self):
        """Gets data for a POST request"""
        # Transform api fields to dict
        d = Serializer.to_dict(
            self, key_filter=lambda k: k in set(self.creatable_fields.keys())
        )
        # Swap attr_keys for api_keys
        return {self.creatable_fields[k].api_key: v for k, v in d.items()}

    def put(self):
        """Gets data for a PUT request"""
        # Transform api fields to dict
        d = Serializer.to_dict(
            self, key_filter=lambda k: k in set(self.updatable_fields.keys())
        )
        # Swap attr_keys for api_keys
        return {self.updatable_fields[k].api_key: v for k, v in d.items()}
