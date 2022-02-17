from datetime import datetime, timedelta
from typing import Any, Dict, Iterable, List

import pandas as pd
from sgqlc.operation import Operation

from ..models.iot import (
    MetricField,
    MetricWindow,
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


class IotNionicHelper(BaseGraphService):

    def __init__(self, contxt_env: ContxtEnvironmentConfig):
        super().__init__(contxt_env)

    def get_latest_states(self, fields: List[MetricField]) -> Dict[str, schema.MetricData]:
        op = Operation(schema.Query)

        for field in fields:
            metric_data = op.metric_data(label=field.label, source_id=field.sourceId, window='1min',
                                         order_by=[schema.MetricDataOrderBy.TIME_DESC], first=1,
                                         to=str(datetime.utcnow()), from_=str(datetime.utcnow() - timedelta(days=1)),
                                         __alias__=field.label)
            metric_data.nodes().time()
            metric_data.nodes().data()

        data = self.run(op)

        metric_data = (op + data)

        result_data = {}
        for field in fields:
            res = metric_data[field.label]
            if len(res.nodes):
                result_data[field.label] = res.nodes[0]

        return result_data

    def get_metric_data(self, field: MetricField, start_time: datetime, end_time: datetime,
                        window: MetricWindow = MetricWindow.MINUTELY, order_by=[schema.MetricDataOrderBy.TIME_ASC]
                        ) -> List[schema.MetricData]:
        op = Operation(schema.Query)
        metric_data = op.metric_data(label=field.label, source_id=field.sourceId, window=window,
                                     order_by=order_by, from_=str(start_time), to=str(end_time))
        metric_data.nodes().time()
        metric_data.nodes().data()

        data = self.run(op)

        return (op + data).metric_data.nodes

    def get_metric_data_df(self, field: MetricField, start_time: datetime, end_time: datetime,
                           window: MetricWindow = MetricWindow.MINUTELY, order_by=[schema.MetricDataOrderBy.TIME_ASC]
                           ) -> pd.DataFrame:

        data = self.get_metric_data(field, start_time, end_time, window, order_by)

        return pd.DataFrame([{'time': d.time, 'value': d.data} for d in data])

