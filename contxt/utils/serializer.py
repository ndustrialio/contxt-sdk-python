from csv import DictWriter
from datetime import date, datetime
from json import dump, dumps
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set, Tuple

from tabulate import tabulate

from contxt.services.asset_framework import AssetFramework
from contxt.utils.auth import CLIAuth


class Serializer:
    """
    A general serializer to transform a Python object to common data formats.
    """

    @staticmethod
    def to_dict(obj: Any,
                cls_key: str = None,
                key_filter: Callable = None):
        """Serializes `obj` to a `dict`. To use a custom format, overload
        `obj.to_dict()`.

        :param obj: object to serialize
        :type obj: Any
        :param cls_key: if provided, set dict[key] = `cls.__name__`, defaults to None
        :param cls_key: str, optional
        :param key_filter: callable filter to keep a subset of keys, of the form f(key) = keep?, defaults to ignore "hidden" variables (i.e. starting with "_")
        :param key_filter: bool, optional
        :return: dictionary
        :rtype: `dict`
        """
        # TODO: this may not return a dict but instead a list, or a native type
        # (for example, if passed an int, it will return it). this is likely
        # an unexpected behavior for callers

        # Create default key filter (ignore _ vars)
        if key_filter is None:
            key_filter = lambda k: not k.startswith("_")

        # Serialize
        if hasattr(obj, "to_dict"):
            # User-defined method
            return obj.to_dict()
        if isinstance(obj, dict):
            # Dictionary
            return {
                k: Serializer.to_dict(v, cls_key=cls_key)
                for k, v in obj.items()
            }
        elif isinstance(obj, (date, datetime)):
            # Date/datetime (default to iso)
            return obj.isoformat()
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
        else:
            return dumps(d, **kwargs)

    @staticmethod
    def to_table(obj: Any, **kwargs):
        """Serializes `obj` to a table.
        
        :param obj: object to serialize
        :type obj: Any
        :return: table
        :rtype: tabulate
        """

        d = Serializer.to_dict(obj)

        # TODO: The above may be a list, so handle it here
        if not isinstance(d, (list, tuple)):
            d = [d]

        return tabulate(d, headers="keys", **kwargs)

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
        def keys(o):
            if isinstance(o, dict):
                return o.keys()
            elif isinstance(o, (list, tuple)) and o:
                # TODO: in this case, we assume the entire list has identical keys
                return keys(o[0])
            else:
                return []

        # Get dict
        d = Serializer.to_dict(obj)

        # Write
        with path.open("w") as f:
            writer = DictWriter(f, fieldnames=keys(d), **kwargs)
            if header:
                writer.writeheader()
            if isinstance(d, (list, tuple)):
                # Write list
                writer.writerows(d)
            else:
                # TODO: may not actually be a dict
                # Write dict
                writer.writerow(d)
