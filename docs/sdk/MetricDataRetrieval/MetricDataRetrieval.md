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

from random import randint
from datetime import datetime
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
facilities = [facilities[randint(0, len(facilities) - 1)]]
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
      <th>facility_daily_active_meters</th>
      <th>facility_daily_co2_factor</th>
      <th>facility_daily_co2_per_unit</th>
      <th>facility_daily_co2_tons</th>
      <th>facility_daily_cubic_footage</th>
      <th>facility_daily_electricity_spend</th>
      <th>facility_daily_electricity_usage</th>
      <th>facility_daily_energy_spend_per_lbs</th>
      <th>facility_daily_energy_spend_per_unit</th>
      <th>facility_daily_inbound_volume</th>
      <th>...</th>
      <th>facility_monthly_energy_spend_per_unit</th>
      <th>facility_monthly_inbound_volume</th>
      <th>facility_monthly_kwh_per_cuft</th>
      <th>facility_monthly_kwh_per_lbs</th>
      <th>facility_monthly_kwh_per_unit</th>
      <th>facility_monthly_max_cuft</th>
      <th>facility_monthly_outbound_volume</th>
      <th>facility_monthly_production_units</th>
      <th>facility_monthly_rolling_year_cubic_footage</th>
      <th>facility_monthly_rolling_year_elec_kbtu</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>10.0</td>
      <td>10.000000</td>
      <td>5.000000</td>
      <td>10.000000</td>
      <td>10.0</td>
      <td>10.000000</td>
      <td>10.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>...</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>1.0</td>
      <td>1.00</td>
      <td>1.00000</td>
      <td>1.0</td>
      <td>1.000000e+00</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>3619.0</td>
      <td>1.255483</td>
      <td>9.543199</td>
      <td>4.219586</td>
      <td>6398483.0</td>
      <td>460.039586</td>
      <td>6721.852316</td>
      <td>0.520232</td>
      <td>0.520232</td>
      <td>660649.000000</td>
      <td>...</td>
      <td>0.853233</td>
      <td>3303245.0</td>
      <td>0.010505</td>
      <td>12.466984</td>
      <td>12.466984</td>
      <td>6398483.0</td>
      <td>2088477.84</td>
      <td>5391.72284</td>
      <td>6398483.0</td>
      <td>1.997479e+07</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.0</td>
      <td>0.000000</td>
      <td>2.853221</td>
      <td>1.373131</td>
      <td>0.0</td>
      <td>149.705105</td>
      <td>2187.414873</td>
      <td>0.155564</td>
      <td>0.155564</td>
      <td>203818.602634</td>
      <td>...</td>
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
      <td>3619.0</td>
      <td>1.255483</td>
      <td>7.140593</td>
      <td>0.413424</td>
      <td>6398483.0</td>
      <td>45.061345</td>
      <td>658.590323</td>
      <td>0.389232</td>
      <td>0.389232</td>
      <td>390799.000000</td>
      <td>...</td>
      <td>0.853233</td>
      <td>3303245.0</td>
      <td>0.010505</td>
      <td>12.466984</td>
      <td>12.466984</td>
      <td>6398483.0</td>
      <td>2088477.84</td>
      <td>5391.72284</td>
      <td>6398483.0</td>
      <td>1.997479e+07</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>3619.0</td>
      <td>1.255483</td>
      <td>7.204442</td>
      <td>4.403425</td>
      <td>6398483.0</td>
      <td>480.176541</td>
      <td>7014.710533</td>
      <td>0.392691</td>
      <td>0.392691</td>
      <td>540796.000000</td>
      <td>...</td>
      <td>0.853233</td>
      <td>3303245.0</td>
      <td>0.010505</td>
      <td>12.466984</td>
      <td>12.466984</td>
      <td>6398483.0</td>
      <td>2088477.84</td>
      <td>5391.72284</td>
      <td>6398483.0</td>
      <td>1.997479e+07</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>3619.0</td>
      <td>1.255483</td>
      <td>8.912080</td>
      <td>4.526398</td>
      <td>6398483.0</td>
      <td>493.397874</td>
      <td>7210.607752</td>
      <td>0.485875</td>
      <td>0.485875</td>
      <td>654527.000000</td>
      <td>...</td>
      <td>0.853233</td>
      <td>3303245.0</td>
      <td>0.010505</td>
      <td>12.466984</td>
      <td>12.466984</td>
      <td>6398483.0</td>
      <td>2088477.84</td>
      <td>5391.72284</td>
      <td>6398483.0</td>
      <td>1.997479e+07</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3619.0</td>
      <td>1.255483</td>
      <td>10.427902</td>
      <td>4.875402</td>
      <td>6398483.0</td>
      <td>531.529215</td>
      <td>7766.576172</td>
      <td>0.568454</td>
      <td>0.568454</td>
      <td>841124.000000</td>
      <td>...</td>
      <td>0.853233</td>
      <td>3303245.0</td>
      <td>0.010505</td>
      <td>12.466984</td>
      <td>12.466984</td>
      <td>6398483.0</td>
      <td>2088477.84</td>
      <td>5391.72284</td>
      <td>6398483.0</td>
      <td>1.997479e+07</td>
    </tr>
    <tr>
      <th>max</th>
      <td>3619.0</td>
      <td>1.255483</td>
      <td>14.030978</td>
      <td>5.094992</td>
      <td>6398483.0</td>
      <td>555.514539</td>
      <td>8116.385280</td>
      <td>0.764909</td>
      <td>0.764909</td>
      <td>875999.000000</td>
      <td>...</td>
      <td>0.853233</td>
      <td>3303245.0</td>
      <td>0.010505</td>
      <td>12.466984</td>
      <td>12.466984</td>
      <td>6398483.0</td>
      <td>2088477.84</td>
      <td>5391.72284</td>
      <td>6398483.0</td>
      <td>1.997479e+07</td>
    </tr>
  </tbody>
</table>
<p>8 rows × 36 columns</p>
</div>




```python

```
