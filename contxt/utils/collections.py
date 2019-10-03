from collections import defaultdict
from typing import Callable, Dict, Iterable, Iterator, List, TypeVar

T = TypeVar("T")
U = TypeVar("U")


class IteratorWrapper(Iterable[T]):
    def __init__(self, iterator_provider: Callable[[], Iterator[T]]):
        self.iterator_provider = iterator_provider

    def __iter__(self) -> Iterator[T]:
        return self.iterator_provider()


def partition_by(iterable: Iterable[T], key: Callable[[T], U]) -> Dict[U, List[T]]:
    """
    Partitions an iterable based on the given key selector
    :param iterable: iterable to partition
    :param key: function to apply to each item in the iterable sequence
    :return: dictionary of items partitioned by the key function
    """
    res = defaultdict(lambda: [])
    for it in iterable:
        res[key(it)].append(it)
    return res


def unique(lst: List) -> bool:
    return len(lst) == len(set(lst))
