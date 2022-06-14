from datetime import datetime, timedelta
import pandas as pd

from contxt.utils.contxt_environment import ContxtEnvironment
from contxt.models.iot import MetricWindow, MetricField

from contxt.services.nionic_iot import IotNionicHelper
from contxt.services.ems import EmsService
from contxt.services.iot import IotService

env: ContxtEnvironment = ContxtEnvironment()

iotMeta: IotService = IotService(env.get_config_for_service_name('iot'))
iot: IotNionicHelper = IotNionicHelper(env.get_config_for_service_name('nionic'))
ems: EmsService = EmsService(env.get_config_for_service_name('ems'))

facility_fields = {}
for field in iotMeta.get_fields_for_facility(47):
    facility_fields[field.id] = field

df = pd.DataFrame()
for main in ems.get_main_services(facility_id=47):
    field_meta = facility_fields.get(main.demand_field.id)
    field = MetricField(label=field_meta.field_descriptor, sourceId=field_meta.feed_key)
    df[main.name] = iot.get_iot_data_series(field=field, start_time=datetime.now() - timedelta(days=90),
                                            end_time=datetime.now(), window=MetricWindow.QUARTER_HOURLY)

print(df)
