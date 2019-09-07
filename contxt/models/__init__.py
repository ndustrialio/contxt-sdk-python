from ast import literal_eval
from datetime import date as _date
from datetime import datetime as _datetime
from typing import Any

from dateutil import parser
from pytz import UTC, ZERO

from contxt.utils import make_logger

logger = make_logger(__name__)


class Parsers:
    """Parsers to deserialize from JSON"""

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
    """Formatters to serialize to JSON"""

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
    def snake_case(text: str) -> str:
        return text.lower().replace(" ", "_")

    @staticmethod
    def pascal_case(text: str) -> str:
        # TODO
        if " " not in text:
            return text
        return text.title().replace(" ", "")
