from datetime import datetime, timedelta
from functools import partial, reduce
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

import click

from contxt.utils.serializer import Serializer

NOW = datetime.now().replace(microsecond=0)
LAST_WEEK = NOW - timedelta(days=7)

# FIXME
OPTIONAL_PROMPT_KWARGS = {
    "prompt": True,
    "default": "<none>",
    "callback": lambda ctx, param, value: value if value != "<none>" else None,
}


def warn(msg: str):
    click.secho(msg, fg="red", err=True)


def print_table(
    items: List[Any], keys: Optional[List[str]] = None, sort_by: Optional[str] = None, count: bool = True
) -> None:
    if keys:
        items = pluck(keys=keys, items=items)
        sort_by = sort_by if sort_by in keys else None
    if items:
        print(Serializer.to_table(items, sort_by=sort_by))
    if count:
        print(f"Count: {len(items)}")


def print_item(item: Dict[str, Any]) -> None:
    print_table([{"key": k, "value": v} for k, v in item.items()], count=False)


def pluck(
    keys: List[str],
    items: List[Dict[str, Any]],
    key_sep: str = ".",
    key_func: Callable[[str], str] = lambda k: k,
) -> List[Dict[str, Any]]:
    """Pluck `keys` from `items`. Nested keys can be specified by concatenating with
    `key_sep` (i.e. `key1.key2`). Returned keys are set via `key_func`."""
    return [
        {
            key_func(k): reduce(
                lambda d, k: d[k] if isinstance(d, dict) else getattr(d, k), k.split(key_sep), d
            )
            for k in keys
        }
        for d in items
    ]


def csv_callback(options: List[str], all: Optional[List[str]] = None):
    def _callback(ctx, param, value):
        # Parse
        if isinstance(value, str) and value == "all":
            fields = all or options
        elif isinstance(value, str):
            fields = [f.strip() for f in value.split(",")]
        else:
            fields = value
        # Validate
        for f in fields:
            if f not in options:
                raise click.BadParameter(f"'{f}' is not valid. Choose from {', '.join(options)}.")
        return fields

    return _callback


def fields_option(func: Optional[click.Command] = None, **kwargs) -> click.Command:
    if func is None:
        return partial(fields_option, **kwargs)  # type: ignore
    return click.option(
        "--fields",
        callback=csv_callback(options=[f.attr_key for f in kwargs.pop("obj")._api_fields], all=[]),
        help="Comma-delimited list of fields to return",
        **kwargs,
    )(func)


def sort_option(func: Optional[click.Command] = None, **kwargs) -> click.Command:
    if func is None:
        return partial(sort_option, **kwargs)  # type: ignore
    return click.option("--sort", help="Field to sort by", **kwargs)(func)


# https://github.com/pallets/click/issues/405
class ClickPath(click.Path):
    def convert(self, *args, **kwargs) -> Any:
        return Path(super().convert(*args, **kwargs))


class Date(click.DateTime):
    def __init__(self) -> None:
        super().__init__(formats=["%Y-%m-%d"])

    def convert(self, *args, **kwargs) -> Any:
        return super().convert(*args, **kwargs).date()
