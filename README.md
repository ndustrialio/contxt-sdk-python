# Contxt Python SDK

This project **requires** Python 3.5+.

## Installation 
To install `contxt-sdk`, just use pip:

```
$ pip install contxt-sdk
```

This also installs a command line interface (cli) available via `contxt`, as long as your active python environment has installed the package. To see the list of supported commands, run the following:

```
$ contxt -h
```

 Additionally, there is support for command line tab completion via [argcomplete](https://github.com/kislyuk/argcomplete). To active, run the following and refresh your bash environment:

```
$ activate-global-python-argcomplete
```

## Command Line Interface

### Getting Started
In order to access any Contxt API, we first need to login. To do so, run the following:

```
$ contxt auth login
```

It will prompt you for your username and password, which is the same login you use for your Contxt applications.

### Available Commands

#### Auth
```
$ contxt auth -h
usage: contxt auth [-h] {login,logout} ...

optional arguments:
  -h, --help      show this help message and exit

subcommands:
  {login,logout}
    login         Login to contxt
    logout        Logout of contxt
```

#### IOT

```
$ contxt iot -h 
usage: contxt iot [-h] {groupings,feeds,fields,unprovisioned,field-data} ...

optional arguments:
  -h, --help            show this help message and exit

subcommands:
  {groupings,feeds,fields,unprovisioned,field-data}
    groupings           Get groupings
    feeds               Get feeds
    fields              Get fields
    unprovisioned       Unprovisioned fields
    field-data          Get field data
```

#### EMS
```
$ contxt ems -h 
usage: contxt ems [-h]
                  {util-spend,util-usage,util-spend-metrics,util-usage-metrics}
                  ...

optional arguments:
  -h, --help            show this help message and exit

subcommands:
  {util-spend,util-usage,util-spend-metrics,util-usage-metrics}
    util-spend          Utility spend
    util-usage          Utility usage
    util-spend-metrics  Utility spend metrics
    util-usage-metrics  Utility usage metrics
```

#### Assets
```
$ contxt assets -h 
usage: contxt assets [-h]
                     {facilities,types,assets,attr,attr-vals,metrics,metric-vals}
                     ...

optional arguments:
  -h, --help            show this help message and exit

subcommands:
  {facilities,types,assets,attr,attr-vals,metrics,metric-vals}
    facilities          Get facility assets
    types               Get asset types
    assets              Get assets
    attr                Get asset attributes
    attr-vals           Get asset attribute values
    metrics             Get asset metrics
    metric-vals         Get asset metric values

```

#### Contxt
```
$ contxt contxt -h
usage: contxt contxt [-h] {orgs,mk-org,users,add-user} ...

optional arguments:
  -h, --help            show this help message and exit

subcommands:
  {orgs,mk-org,users,add-user}
    orgs                Get organizations
    mk-org              Create organization
    users               Get users
    add-user            Add user to an organization
```

#### Bus
```
$ contxt bus -h
usage: contxt bus [-h] {channels} ...

optional arguments:
  -h, --help  show this help message and exit

subcommands:
  {channels}
    channels  Get channels
```

### Examples

#### Exporting IOT Data

You can export field data from the IOT service with the following command:

```
$ contxt iot field-data -h
usage: contxt iot field-data [-h] [-e END_DATE] [-p]
                             grouping_id start_date {0,60,900,3600}
```

For example:
```
$ contxt iot field-data "09d26434-7b5b-448f-911c-2deb5e9a78ce" "2019-02-01" 60
```

This command will create the directory `export_<grouping_slug>_<current_time>` with csv files of the associated records each field within the grouping and within the specified time range. There is also a `meta.json` file which contains specific information about the export like row counts, field ids, and units.
