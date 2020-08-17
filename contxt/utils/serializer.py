from csv import DictWriter
from datetime import date, datetime
from enum import Enum
from json import dump, dumps
from pathlib import Path
from typing import Any, Callable, Iterable, Optional

from tabulate import tabulate


class Serializer:
    """Serializer to transform a Python object to common data formats"""

    @staticmethod
    def _keys(obj):
        if isinstance(obj, dict):
            return obj.keys()
        elif isinstance(obj, (list, tuple)) and obj:
            return list(set().union(*(Serializer._keys(i) for i in obj)))
        else:
            return []

    @staticmethod
    def to_dict(obj: Any, cls_key: str = None, key_filter: Callable = None):
        """Serializes `obj` to a `dict`. To use a custom format, overload
        `obj.to_dict()`.

        :param obj: object to serialize
        :type obj: Any
        :param cls_key: if provided, set dict[key] = `cls.__name__`, defaults to None
        :param cls_key: str, optional
        :param key_filter: callable filter to keep a subset of keys, of the form
        f(key) = keep?, defaults to ignore "hidden" variables (i.e. starting with "_")
        :param key_filter: bool, optional
        :return: dictionary
        :rtype: `dict`
        """
        from contxt.models import Formatters

        # TODO: this may not return a dict but instead a list, or a native type
        # (for example, if passed an int, it will return it). this is likely
        # an unexpected behavior for callers
        # NOTE: alternative (but slower) implementations:
        # 1. d = json.dumps(d, default=lambda o: getattr(o, "__dict__", str(o)))
        # 2. d = jsonpickle.encode(d, unpicklable=False))
        # >> json.loads(d)

        def default_filter(key: str) -> bool:
            return not key.startswith("_")

        # Create default key filter (ignore _ vars)
        key_filter = key_filter or default_filter

        # Serialize
        if hasattr(obj, "to_dict"):
            # User-defined method
            return obj.to_dict()
        if isinstance(obj, dict):
            # Dictionary
            return {k: Serializer.to_dict(v, cls_key=cls_key) for k, v in obj.items()}
        elif isinstance(obj, datetime):
            # Datetime
            return Formatters.datetime(obj)
        elif isinstance(obj, date):
            # Date
            return Formatters.date(obj)
        elif isinstance(obj, Enum):
            return obj.value
        elif hasattr(obj, "_ast"):
            # Abstract syntax tree
            return Serializer.to_dict(obj._ast())
        elif hasattr(obj, "__iter__") and not isinstance(obj, str):
            # Iterables (except strings)
            return [Serializer.to_dict(v, cls_key) for v in obj]
        elif hasattr(obj, "__dict__"):
            # General object
            d = {
                k: Serializer.to_dict(v, cls_key)
                for k, v in obj.__dict__.items()
                if not callable(v) and key_filter(k)
            }
            if cls_key is not None and hasattr(obj, "__class__"):
                d[cls_key] = obj.__class__.__name__
            return d
        else:
            # Fallback to self
            return obj

    @staticmethod
    def to_json(obj: Any, path: Optional[Path] = None, **kwargs):
        """Serializes `obj` to JSON.

        :param obj: object to serialize
        :type obj: Any
        :param path: path for dumping, defaults to None
        :param path: Path, optional
        :return: JSON
        :rtype: str
        """
        # Set default args
        kwargs.setdefault("indent", "\t")
        kwargs.setdefault("sort_keys", True)

        # Dump
        d = Serializer.to_dict(obj)
        if path:
            with path.open("w") as f:
                return dump(d, f, **kwargs)
        return dumps(d, **kwargs)

    @staticmethod
    def to_table(obj: Any, path: Optional[Path] = None, **kwargs):
        """Serializes `obj` to a table.

        :param obj: object to serialize
        :type obj: Any
        :param path: path for dumping, defaults to None
        :param path: Path, optional
        :return: table
        :rtype: tabulate
        """

        d = Serializer.to_dict(obj)

        # TODO: The above may be a list, so handle it here
        if not isinstance(d, (list, tuple)):
            d = [d]

        table = tabulate(d, headers="keys", **kwargs)
        if path:
            with path.open("w") as f:
                return f.write(table)
        return table

    @staticmethod
    def to_csv(obj: Any, path: Path, header: bool = True, **kwargs):
        """Serializes `obj` to CSV.

        :param obj: object to serialize
        :type obj: Any
        :param path: path to export
        :type path: Path
        :param header: write header row, defaults to True
        :param header: bool, optional
        """

        # Get dict
        d = Serializer.to_dict(obj)

        # Write
        with path.open("w") as f:
            writer = DictWriter(f, fieldnames=Serializer._keys(d), **kwargs)
            if header:
                writer.writeheader()
            if isinstance(d, (list, tuple)):
                # Write list
                writer.writerows(d)
            else:
                # TODO: may not actually be a dict
                # Write dict
                writer.writerow(d)

    @staticmethod
    def to_file(
        obj: Any, path: Optional[Path] = None, valid_exts: Iterable[str] = (".csv", ".json", ".txt"),
    ):
        """Write an object to a file (or stdout).

        If path is not provided, `obj` is sent to stdout. Otherwise, the file
        extension is used to determine the data format of `obj` before exporting.
        Supported file extensions are csv (calls `Serializer.to_csv`),
        json (calls `Serializer.to_json`), or txt (calls `Serializer.to_table`).

        :param obj: object to output
        :type obj: Any
        :param path: path to export, defaults to None
        :param path: Optional[Path], optional
        :param valid_exts: supported file extensions, defaults to
        (".csv", ".json", ".txt")
        :param valid_exts: Optional[List[str]], optional
        """

        # If path unspecified, default to stdout
        if path is None:
            obj_to_print = (
                Serializer.to_table(obj) if isinstance(obj, (list, tuple)) else Serializer.to_json(obj)
            )
            print(obj_to_print)
            return

        # Validate file extension
        if path.suffix not in valid_exts:
            raise RuntimeError(
                f"Unsupported filetype: '{path.suffix}'. Choose from {', '.join(valid_exts)}"
            )

        # Dump to file
        if path.suffix == ".csv":
            Serializer.to_csv(obj, path)
        elif path.suffix == ".json":
            Serializer.to_json(obj, path)
        else:
            Serializer.to_table(obj, path)
