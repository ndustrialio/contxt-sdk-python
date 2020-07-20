from dataclasses import dataclass
from datetime import datetime
from math import ceil
from typing import Any, Callable, Dict, Generic, Iterator, List, Optional, Tuple, TypeVar, Union

from ..models import Parsers
from ..utils.object_mapper import ObjectMapper
from .api import Api

T = TypeVar("T")
Record = Dict[str, Any]
DataPoint = Tuple[datetime, Any]


@dataclass
class PageOptions:
    per_page: int = 1000
    order_by: Optional[str] = None  # NOTE: ideally this should be an enum, if possible
    reverse_order: Optional[bool] = None

    def __post_init__(self) -> None:
        assert self.per_page > 0, f"per_page must be a positive integer, not {self.per_page}"

    def to_api(self, index: int) -> Dict:
        return {
            "offset": self.per_page * index,
            "limit": self.per_page,
            "orderBy": self.order_by,
            "reverseOrder": self.reverse_order,
        }


@dataclass
class PageMetadata:
    totalRecords: int
    offset: int = 0


@dataclass
class Page:
    records: List[Record]
    _metadata: PageMetadata

    def __len__(self) -> int:
        return len(self.records)

    def __iter__(self) -> Iterator[Record]:
        yield from self.records

    def __getitem__(self, index: Union[int, slice]) -> Union[Record, List[Record]]:
        return self.records[index]


class PagedRecords(Generic[T]):
    def __init__(
        self,
        api: Api,
        url: str,
        params: Optional[Dict] = None,
        options: Optional[PageOptions] = None,
        record_parser: Optional[Callable[[Record], T]] = None,
    ):
        self.api = api
        self.url = url
        self.params = params or {}
        self.options = options or PageOptions()
        self.record_parser = record_parser or (lambda x: x)  # type: ignore

        # Fetch first page
        self.page_index = 0
        self.page = self.get_page(index=self.page_index, force=True)

    def __len__(self) -> int:
        return self.total_records

    def __iter__(self) -> Iterator[T]:
        for page_index in range(self.total_pages):
            yield from self.get_page(page_index)  # type: ignore

    def __getitem__(self, index: Union[int, slice]) -> Union[T, List[T]]:
        if isinstance(index, int):
            return self._get_item(index)
        elif isinstance(index, slice):
            return self._get_slice(index)
        raise TypeError(f"Record index must be int or slice, not {type(index).__name__}")

    def _get_item(self, index: int) -> T:
        if not 0 <= index < self.total_records:
            raise IndexError(f"Record index {index} out of range")
        page = index // self.per_page
        item = index % self.per_page
        return self.get_page(page)[item]  # type: ignore

    def _get_slice(self, index: slice) -> List[T]:
        # TODO: we could optimize this by not fetching unneeded pages, i.e. pages[0:1]
        # would only need the first page fetched
        records = [r for r in self]
        return records[index]

    def _get_page(self, index: int) -> Page:
        resp = self.api.get(uri=self.url, params={**self.params, **self.options.to_api(index)})
        page = ObjectMapper.tree_to_object(resp, Page)
        # NOTE: this post processing is not ideal, but works for now
        page.records = [self.record_parser(rec) for rec in page.records]  # type: ignore
        return page

    def get_page(self, index: int, force: bool = False) -> Page:
        # Validate index
        if not force:
            if not 0 <= index < self.total_pages:
                raise IndexError(f"Page index {index} out of range")
            elif index == self.page_index:
                return self.page

        # Fetch page
        self.page_index = index
        self.page = self._get_page(self.page_index)
        return self.page

    @property
    def total_pages(self) -> int:
        return ceil(self.total_records / self.per_page)

    @property
    def total_records(self) -> int:
        return self.page._metadata.totalRecords

    @property
    def per_page(self) -> int:
        return self.options.per_page


@dataclass
class TimeSeriesPageMetadata:
    count: int
    has_more: bool
    next_page_url: str
    next_record_time: int


@dataclass
class TimeSeriesPage:
    records: List[Record]
    meta: TimeSeriesPageMetadata

    def __len__(self) -> int:
        return len(self.records)

    def __iter__(self) -> Iterator[Record]:
        yield from self.records

    def __getitem__(self, index: Union[int, slice]) -> Union[Record, List[Record]]:
        return self.records[index]


class PagedTimeSeries:
    def __init__(self, api: Api, url: str, params: Optional[Dict] = None, per_page: int = 1000):
        self.api = api
        self.url = url
        self.params = params or {}
        self.params.setdefault("limit", per_page)

        # Fetch first page
        self.page_index = 0
        self.page = self._get_page(url=self.url, params=self.params)

    def __iter__(self):
        # HACK: Reset to first page
        if self.page_index != 0:
            self.page_index = 0
            self.page = self._get_page(url=self.url, params=self.params)
        yield from self.page
        while self.next_page_url:
            yield from self.get_next_page()

    def _get_page(self, url: str, params: Optional[Dict] = None) -> TimeSeriesPage:
        resp = self.api.get(url, params=params)
        page = ObjectMapper.tree_to_object(resp, TimeSeriesPage)
        # NOTE: this post processing is not ideal, but works for now
        page.records = [self._record_parser(rec) for rec in page.records]  # type: ignore
        return page

    def _record_parser(self, record: Dict) -> DataPoint:
        return Parsers.datetime(record["event_time"]), Parsers.unknown(record["value"])

    def get_next_page(self) -> TimeSeriesPage:
        if not self.next_page_url:
            raise IndexError("No next page")
        self.page_index += 1
        self.page = self._get_page(url=self.next_page_url)
        return self.page

    @property
    def next_page_url(self) -> Optional[str]:
        if not self.page.meta.next_page_url:
            return None
        return self.page.meta.next_page_url.replace(self.api.base_url, "")

    @property
    def per_page(self) -> int:
        return self.params["limit"]
