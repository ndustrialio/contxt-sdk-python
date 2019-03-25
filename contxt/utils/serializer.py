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
            data = {
                k: Serializer.to_dict(v, cls_key)
                for k, v in obj.__dict__.items()
                if not callable(v) and key_filter(k)
            }
            if cls_key is not None and hasattr(obj, "__class__"):
                data[cls_key] = obj.__class__.__name__
            return data
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
        return tabulate([d.values()], headers="keys", **kwargs)

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

        d = Serializer.to_dict(obj)
        with path.open("w") as f:
            writer = DictWriter(f, fieldnames=d.keys(), **kwargs)
            if header:
                writer.writeheader()
            writer.writerows(d)


if __name__ == "__main__":
    import jsonpickle
    import json
    from pprint import pprint
    from time import time
    auth = CLIAuth()
    af = AssetFramework(auth, "a8e526e4-cb2d-4188-ac25-294e76f9f467", types_to_fully_load=["Facility"])
    complete_asset = af.get_complete_asset("78125c40-3429-4191-873b-06ce2ad7dfe1")

    t = time()
    pickled = jsonpickle.encode(complete_asset)
    # pprint(json.dumps(pickled))
    print(time() - t)

    t = time()
    d = Serializer.to_dict(complete_asset.asset, "cls")
    print(time() - t)

    pprint(d)
    json.dumps(d)

    a = complete_asset.asset
    d = Serializer.to_dict(a)
    j = Serializer.to_json(a, path=Path("test.json"))
    t = Serializer.to_table(a.attribute_values)
    print(t)
    Serializer.to_csv(a.attribute_values, Path("test.csv"))

    print("done")
