from datetime import datetime, timedelta
from dateutil import parser
from typing import Any, Dict, Iterable, List

import pandas as pd
from sgqlc.operation import Operation

from ..models.iot import (
    MetricField,
    MetricWindow,
    FacilityMetricField,
    IOTRequest
)
from ..utils import make_logger
from ..utils.config import ContxtEnvironmentConfig
from .base_graph_service import BaseGraphService, SchemaMissingException

try:
    import contxt.schemas.nionic.nionic_schema as schema
    from contxt.schemas.nionic.nionic_schema import MetricData
except ImportError:
    raise SchemaMissingException('[ERROR] Schema is not generated for GraphQL -- run `contxt init` to '
                                 'initialize then re-run the command')

logger = make_logger(__name__)


class IOTRequestException(Exception):
    pass


class IotNionicHelper(BaseGraphService):

    def __init__(self, contxt_env: ContxtEnvironmentConfig):
        super().__init__(contxt_env)

    def _page_through_response(self, metric_data):
        parsed_data = []
        time_index = []

        for d in metric_data.nodes:
            time_index.append(parser.parse(d.time))
            try:
                parsed_data.append(float(d.data))
            except ValueError as e:
                parsed_data.append(d.data)

        return parsed_data, time_index

    def get_latest_states(self, fields: List[MetricField]) -> Dict[str, schema.MetricData]:
        op = Operation(schema.Query)

        field_aliases = []

        for field in fields:
            field_alias = field.label if field.alias is None else field.alias.replace('-', '_')
            field_aliases.append(field_alias)
            metric_data = op.metric_data(label=field.label, source_id=field.sourceId, window='1min',
                                         order_by=[schema.MetricDataOrderBy.TIME_DESC], first=1,
                                         to=str(datetime.utcnow()), from_=str(datetime.utcnow() - timedelta(days=1)),
                                         __alias__=field_alias)
            metric_data.nodes().time()
            metric_data.nodes().data()

        data = self.run(op)

        metric_data = (op + data)

        result_data = {}
        for field in field_aliases:
            res = metric_data[field]
            if len(res.nodes):
                result_data[field] = res.nodes[0]
            else:
                result_data[field] = None

        return result_data

    def get_bulk_iot_data(self, requests: List[IOTRequest]) -> Dict[str, pd.Series]:
        op = Operation(schema.Query)

        req_aliases = []

        for req in requests:
            alias = req.alias.replace('-', '_')
            req_aliases.append(alias)
            if req.window is not MetricWindow.RAW:
                metric_data = op.metric_data(label=req.field.label, source_id=req.field.sourceId, window=req.window.value,
                                             aggregation=req.aggregation,
                                             order_by=[schema.MetricDataOrderBy.TIME_ASC],
                                             to=str(req.endTime), from_=str(req.startTime),
                                             __alias__=alias)
            else:
                metric_data = op.metric_data(label=req.field.label, source_id=req.field.sourceId,
                                             order_by=[schema.MetricDataOrderBy.TIME_ASC],
                                             to=str(req.endTime), from_=str(req.startTime),
                                             __alias__=alias)
            metric_data.nodes().time()
            metric_data.nodes().data()

            # page info
            metric_data.page_info().has_next_page()

        data = self.run(op)

        metric_data = (op + data)

        result_data = {}
        for alias in req_aliases:
            res = metric_data[alias]

            parsed_data, time_index = self._page_through_response(res)

            result_data[alias] = pd.Series(parsed_data, time_index)

        return result_data

    def get_iot_data(self, field: MetricField, start_time: datetime, end_time: datetime,
                     window: MetricWindow = MetricWindow.MINUTELY, order_by=[schema.MetricDataOrderBy.TIME_ASC],
                     aggregation: schema.MetricDataAggregationMethod = 'AVG'
                     ) -> schema.MetricData:
        op = Operation(schema.Query)
        if window is not MetricWindow.RAW:
            metric_data = op.metric_data(label=field.label, source_id=field.sourceId, window=window.value,
                                         order_by=order_by, from_=str(start_time), to=str(end_time),
                                         aggregation=aggregation)
        else:
            metric_data = op.metric_data(label=field.label, source_id=field.sourceId, window=window.value,
                                         order_by=order_by, from_=str(start_time), to=str(end_time))
        metric_data.nodes().time()
        metric_data.nodes().data()

        # page info
        metric_data.page_info().has_next_page()
        print(op)
        data = self.run(op)

        return (op + data).metric_data

    def get_facility_metric_data(self, field: FacilityMetricField, start_time: datetime, end_time: datetime) -> schema.MetricData:
        op = Operation(schema.Query)

        metric_data = op.facility(id=field.facilityId).metric_data(label=field.label,
                                                                   from_=str(start_time),
                                                                   to=str(end_time))

        metric_data.nodes().time()
        metric_data.nodes().data()

        # page info
        metric_data.page_info().has_next_page()
        data = self.run(op)

        return (op + data).facility.metric_data

    def get_iot_data_series(self, field: MetricField, start_time: datetime, end_time: datetime,
                               window: MetricWindow = MetricWindow.MINUTELY, order_by=[schema.MetricDataOrderBy.TIME_ASC],
                               aggregation: str = 'AVG'
                               ) -> pd.Series:

        if aggregation not in schema.MetricDataAggregationMethod.__choices__:
            raise IOTRequestException(f'Aggregation method {aggregation} not a valid aggregation method')

        agg_method = schema.MetricDataAggregationMethod(aggregation)

        all_data = []
        full_index = []
        while True:
            data = self.get_iot_data(field, start_time, end_time, window, order_by, aggregation=agg_method)

            has_another_page = data.page_info.has_next_page

            parsed_data, time_index = self._page_through_response(data)
            all_data.extend(parsed_data)
            full_index.extend(time_index)

            if not has_another_page:
                break

            start_time = time_index[-1]

        ds = pd.Series(all_data, full_index)
        return ds

    def get_metric_data_series(self, field: FacilityMetricField, start_time: datetime, end_time: datetime) -> pd.Series:

        all_data = []
        full_index = []
        while True:
            data = self.get_facility_metric_data(field, start_time, end_time)

            has_another_page = data.page_info.has_next_page

            parsed_data, time_index = self._page_through_response(data)

            all_data.extend(parsed_data)
            full_index.extend(time_index)

            if not has_another_page:
                break

            start_time = time_index[-1]

        ds = pd.Series(all_data, full_index)
        return ds
