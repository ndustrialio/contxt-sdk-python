from datetime import datetime
from functools import wraps

from .datetime import datetime_zulu_format


class Printable:
    def __str__(self) -> str:
        return Printable.pprint(self)

    def __repr__(self) -> str:
        return str(self)

    @staticmethod
    def pprint(obj: object) -> str:
        return str(
            {k: datetime_zulu_format(v) if type(v) is datetime else v for k, v in vars(obj).items()}
        )


def decorate_all_methods(decorator):
    """ Decorator factory to decorate all methods of a class
        Note the target of this factory is a class, sample usage:

        @decorate_all_methods(my_awesome_decorator)
        class Foo:
            ...
    """

    def decorate(cls):
        for attr, member in vars(cls).items():
            if callable(member):
                setattr(cls, attr, decorator(member))
        return cls

    return decorate


def cached(fn):
    """
    Decorator that makes caches the result of a property or monadic method.
    So its body is executed only once and the value is saved for subsequent calls.
    """
    attr_name = "_lazy_" + fn.__name__

    @wraps(fn)
    def _lazy(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return _lazy
