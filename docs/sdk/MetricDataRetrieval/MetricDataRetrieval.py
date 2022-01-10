#!/usr/bin/env python
# coding: utf-8

# # Goal: Extract facility metric data using the Contxt Python SDK
#
# Contxt organizes its data in a Customer to Facility to Metric hierarchy. To retrieve metric data
# for all facilities, the general operation flow is:
# 1. Instance customer client
# 1. Locate customer facilities
# 1. Locate customer metric definitions
# 1. Retrieve metrics for each customer facility.
#
# This document demonstrates this flow using the
# [Contxt Python SDK](https://github.com/ndustrialio/contxt-sdk-python).
#
# Note: this example is functional but not optimized. At a minimum, multiprocessing could be used
# to speed up the data request for a large number of facilities.

# In[1]:


from dataclasses import field, make_dataclass
from datetime import datetime
from random import randint
from typing import Any

import pytz

from contxt.cli.clients import Clients

# # How long ago should we look for data?
#
# The metric data retrieval service allows bounding a time window for returned data with
# `effective_start_time` and `effective_end_time` parameters. These values must be reported as
# ISO 8601 strings matching the `"%Y-%m-%dT%H:%M:%SZ"` format.
#
# In this document, we're going to retrieve all data between now and the date in the
# `earliest_date` variable we declare below.

# In[2]:


earliest_date = datetime(2022, 1, 1, tzinfo=pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


# # Initialize SDK client
#
# If you are in a newly installed environment, you will need to configure your environment's
# Contxt authentication secrets with the CLI command: `contxt auth login` before running this
# notebook any further.

# In[3]:


clients = Clients(env="production", org_slug="lineage")


# # Get organization facilities
#
# The next cell retrieves all of the organization's facilities.

# In[4]:


facilities = clients.facilities.get_facilities()
len(facilities)


# We'll use a randomly selected facility for the rest of the notebook

# In[5]:


facilities = [facilities[randint(0, len(facilities))]]


# # Retrieve Customer Metrics

# ## Locate the facility type definition
#
# Contxt's dynamic nature allows for many asset types, but also leads to each organization having
# a unique definition for their asset types. The below code cell scans the asset type definitions
# for the organization and locates the definition for the `Facility` asset type. Most critically,
# later code will depend on the `Facility` asset type definition's unique id.

# In[6]:


asset_types = clients.assets.get_asset_types()
facility_type = [atype for atype in asset_types if atype.label == "Facility"][0]
facility_type


# ## Retrieve Metric Definitions
#
# A call to the SDK client's `get_metrics` function with the facility_type id will retrieve the
# full list of metric definitions. The below code cell demonstrates this with a filter applied to
# drop an unwanted definition.

# In[7]:


metric_definitions = [
    mdef for mdef in clients.assets.get_metrics(facility_type.id) if mdef.label != "Blended Rate"
]
print(f"Number of definitions: {len(metric_definitions)}")


# ## Retrieving Metric Values
#
# Below, we make a python dataclass from our selected metrics. This will allow a degree of data
# validation as we build the full dataset over relying on simple dictionaries of data.

# In[8]:

FacilityEntry = make_dataclass(
    "FacilityEntry",
    ["facility", "date"]
    + [(mdef.label, Any, field(default=None)) for mdef in metric_definitions],  # type: ignore
)


# Next, we iterate over each metric for each facility to build out the full data set. Much of the
# work in this next code cell is in reorganizing the data returned by Contxt into a structure that
# allows building a single unified table. In this case, that structure is a list of items where
# each item is all of a Facility's metrics for a given date.
#
# As written, this code can take about ~10 seconds per facility.

# In[9]:


all_facility_data = []

# For each facility
for idx, facility in enumerate(facilities):
    facility_data = {}

    # For each metric of each facility
    for metric_def in metric_definitions:

        # Try to retrieve metric data, and skip this metric if it fails
        try:
            metric_values = clients.ems.get_metric_values(
                facility.asset_id, metric_def.label, params={"effective_start_date": earliest_date}
            )
        except Exception:
            # print(f"\t{metric_def.label} not found for {facility.name}")
            continue

        # Reformat metric data into table structure
        for metric_value in metric_values:
            if metric_value.effective_start_date not in facility_data:
                facility_data[metric_value.effective_start_date] = {metric_def.label: metric_value.value}
            else:
                facility_data[metric_value.effective_start_date][metric_def.label] = metric_value.value
    all_facility_data.extend(
        [FacilityEntry(facility.name, date, **fe) for date, fe in facility_data.items()]
    )
    # print(f"Retrieve data for {facility.name}")
print(f"Retrieved {len(all_facility_data) * len(metric_definitions)} data points")


# # Now you have your data!
#
# At this point, the facility data has been pulled into the python environment and can be
# manipulated or handed off to other tools. For example, this list of `FacilityEntry` can be
# converted directly to a Pandas dataframe like so:

# In[10]:


# import pandas
#
# df = pandas.DataFrame(all_facility_data)
# df.describe()
