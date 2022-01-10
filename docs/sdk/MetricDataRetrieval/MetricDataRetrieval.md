# Goal: Extract facility metric data using the Contxt Python SDK

Contxt organizes its data in a Customer to Facility to Metric hierarchy. To retrieve metric data for all facilities, the general operation flow is:
1. Instance customer client
1. Locate customer facilities
1. Locate customer metric definitions
1. Retrieve metrics for each customer facility.

This document demonstrates this flow using the [Contxt Python SDK](https://github.com/ndustrialio/contxt-sdk-python).

Note: this example is functional but not optimized. At a minimum, multiprocessing could be used to speed up the data request for a large number of facilities.


```python
from contxt.cli.clients import Clients
from contxt.utils.serializer import Serializer

import argparse
import os, sys
from random import randint
from pathlib import Path
from datetime import datetime, timedelta
import pytz
```

# How long ago should we look for data?

The metric data retrieval service allows bounding a time window for returned data with `effective_start_time` and `effective_end_time` parameters. These values must be reported as ISO 8601 strings matching the `"%Y-%m-%dT%H:%M:%SZ"` format.

In this document, we're going to retrieve all data between now and the date in the `earliest_date` variable we declare below.


```python
earliest_date = datetime(2022, 1, 1, tzinfo=pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
```

# Initialize SDK client

If you are in a newly installed environment, you will need to configure your environment's Contxt authentication secrets with the CLI command: `contxt auth login` before running this notebook any further.


```python
clients = Clients(env="production", org_slug="lineage")
```

# Get organization facilities

The next cell retrieves all of the organization's facilities.


```python
facilities = clients.facilities.get_facilities()
len(facilities)
```




    576



We'll use a randomly selected facility for the rest of the notebook


```python
facilities = [facilities[randint(0, len(facilities))]]
```

# Retrieve Customer Metrics

## Locate the facility type definition

Contxt's dynamic nature allows for many asset types, but also leads to each organization having a unique definition for their asset types. The below code cell scans the asset type definitions for the organization and locates the definition for the `Facility` asset type. Most critically, later code will depend on the `Facility` asset type definition's unique id.


```python
asset_types = clients.assets.get_asset_types()
facility_type = [atype for atype in asset_types if atype.label == 'Facility'][0]
facility_type
```




    AssetType(label='Facility', description='Physical Facility Locations', organization_id='02efa741-a96f-4124-a463-ae13a704b8fc', id='616eee50-5dd3-4009-b8a3-dedfd8a7d56d', is_global=True, global_asset_type_parent_id='5f310899-d8f9-4dac-ae82-cedb2048a8ef', parent_id=None, hierarchy_level=1, created_at=datetime.datetime(2018, 11, 15, 16, 34, 17, 41000, tzinfo=datetime.timezone.utc), updated_at=datetime.datetime(2018, 11, 15, 16, 34, 17, 41000, tzinfo=datetime.timezone.utc))



## Retrieve Metric Definitions

A call to the SDK client's `get_metrics` function with the facility_type id will retrieve the full list of metric definitions. The below code cell demonstrates this with a filter applied to drop an unwanted definition.


```python
metric_definitions = [mdef for mdef in clients.assets.get_metrics(facility_type.id) if mdef.label != "Blended Rate"]
print(f"Number of definitions: {len(metric_definitions)}")
```

    Number of definitions: 69


## Retrieving Metric Values

Below, we make a python dataclass from our selected metrics. This will allow a degree of data validation as we build the full dataset over relying on simple dictionaries of data.


```python
from dataclasses import make_dataclass, field
from typing import Any


FacilityEntry = make_dataclass(
    'FacilityEntry',
   ["facility", "date"] + [(mdef.label, Any, field(default=None)) for mdef in metric_definitions])
```

Next, we iterate over each metric for each facility to build out the full data set. Much of the work in this next code cell is in reorganizing the data returned by Contxt into a structure that allows building a single unified table. In this case, that structure is a list of items where each item is all of a Facility's metrics for a given date.

As written, this code can take about ~10 seconds per facility.


```python
all_facility_data = []

# For each facility
for idx, facility in enumerate(facilities):
    facility_data = {}
    
    # For each metric of each facility
    for metric_def in metric_definitions:
        
        # Try to retrieve metric data, and skip this metric if it fails
        try:
            metric_values = clients.ems.get_metric_values(
                facility.asset_id, metric_def.label, params={"effective_start_date": earliest_date})
        except Exception:
            # print(f"\t{metric_def.label} not found for {facility.name}")
            continue
            
        # Reformat metric data into table structure
        for metric_value in metric_values:
            if metric_value.effective_start_date not in facility_data:
                facility_data[metric_value.effective_start_date] = {metric_def.label: metric_value.value}
            else:
                facility_data[metric_value.effective_start_date][metric_def.label] = metric_value.value
    all_facility_data.extend([FacilityEntry(facility.name, date, **fe) for date, fe in facility_data.items()])
    # print(f"Retrieve data for {facility.name}")
print(f"Retrieved {len(all_facility_data) * len(metric_definitions)} data points")
```

    Retrieved 690 data points


# Now you have your data!

At this point, the facility data has been pulled into the python environment and can be manipulated or handed off to other tools. For example, this list of `FacilityEntry` can be converted directly to a Pandas dataframe like so:


```python
import pandas
df = pandas.DataFrame(all_facility_data)
df.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>facility_daily_co2_factor</th>
      <th>facility_daily_co2_tons</th>
      <th>facility_daily_cubic_footage</th>
      <th>facility_daily_electricity_spend</th>
      <th>facility_daily_electricity_usage</th>
      <th>facility_daily_iot_electricity_usage</th>
      <th>facility_daily_kwh_per_cuft</th>
      <th>facility_daily_rolling_average_blended_rate</th>
      <th>facility_monthly_co2_factor</th>
      <th>facility_monthly_co2_tons</th>
      <th>facility_monthly_cubic_footage</th>
      <th>facility_monthly_cubic_foot_eui</th>
      <th>facility_monthly_electricity_spend</th>
      <th>facility_monthly_electricity_usage</th>
      <th>facility_monthly_kwh_per_cuft</th>
      <th>facility_monthly_max_cuft</th>
      <th>facility_monthly_rolling_year_cubic_footage</th>
      <th>facility_monthly_rolling_year_elec_kbtu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.0</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1.00000</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.823639</td>
      <td>17.210435</td>
      <td>4050000.0</td>
      <td>3708.307724</td>
      <td>41791.210000</td>
      <td>41791.210000</td>
      <td>0.010319</td>
      <td>0.088734</td>
      <td>0.823639</td>
      <td>172.104352</td>
      <td>4050000.0</td>
      <td>32.884494</td>
      <td>37083.07724</td>
      <td>417912.1</td>
      <td>0.103188</td>
      <td>4050000.0</td>
      <td>4050000.0</td>
      <td>1.331822e+08</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.000000</td>
      <td>5.976534</td>
      <td>0.0</td>
      <td>1287.689112</td>
      <td>14512.509633</td>
      <td>14512.509633</td>
      <td>0.003583</td>
      <td>0.000007</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.823639</td>
      <td>2.085577</td>
      <td>4050000.0</td>
      <td>449.323113</td>
      <td>5064.300000</td>
      <td>5064.300000</td>
      <td>0.001250</td>
      <td>0.088724</td>
      <td>0.823639</td>
      <td>172.104352</td>
      <td>4050000.0</td>
      <td>32.884494</td>
      <td>37083.07724</td>
      <td>417912.1</td>
      <td>0.103188</td>
      <td>4050000.0</td>
      <td>4050000.0</td>
      <td>1.331822e+08</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.823639</td>
      <td>16.681511</td>
      <td>4050000.0</td>
      <td>3594.506823</td>
      <td>40506.850000</td>
      <td>40506.850000</td>
      <td>0.010002</td>
      <td>0.088729</td>
      <td>0.823639</td>
      <td>172.104352</td>
      <td>4050000.0</td>
      <td>32.884494</td>
      <td>37083.07724</td>
      <td>417912.1</td>
      <td>0.103188</td>
      <td>4050000.0</td>
      <td>4050000.0</td>
      <td>1.331822e+08</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.823639</td>
      <td>18.511245</td>
      <td>4050000.0</td>
      <td>3988.573420</td>
      <td>44949.900000</td>
      <td>44949.900000</td>
      <td>0.011099</td>
      <td>0.088734</td>
      <td>0.823639</td>
      <td>172.104352</td>
      <td>4050000.0</td>
      <td>32.884494</td>
      <td>37083.07724</td>
      <td>417912.1</td>
      <td>0.103188</td>
      <td>4050000.0</td>
      <td>4050000.0</td>
      <td>1.331822e+08</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>0.823639</td>
      <td>19.830880</td>
      <td>4050000.0</td>
      <td>4273.229547</td>
      <td>48154.300000</td>
      <td>48154.300000</td>
      <td>0.011890</td>
      <td>0.088739</td>
      <td>0.823639</td>
      <td>172.104352</td>
      <td>4050000.0</td>
      <td>32.884494</td>
      <td>37083.07724</td>
      <td>417912.1</td>
      <td>0.103188</td>
      <td>4050000.0</td>
      <td>4050000.0</td>
      <td>1.331822e+08</td>
    </tr>
    <tr>
      <th>max</th>
      <td>0.823639</td>
      <td>23.099903</td>
      <td>4050000.0</td>
      <td>4976.840397</td>
      <td>56092.300000</td>
      <td>56092.300000</td>
      <td>0.013850</td>
      <td>0.088744</td>
      <td>0.823639</td>
      <td>172.104352</td>
      <td>4050000.0</td>
      <td>32.884494</td>
      <td>37083.07724</td>
      <td>417912.1</td>
      <td>0.103188</td>
      <td>4050000.0</td>
      <td>4050000.0</td>
      <td>1.331822e+08</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
