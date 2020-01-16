# Authentication
In order to access any Contxt API, we first need to provide our Contxt credentials. To do so, run the following:
```console
$ contxt auth login
```

This will prompt you for your Contxt username and password.

# Commands

## auth
```console
$ contxt auth -h
usage: contxt auth [-h] {login,logout} ...

optional arguments:
  -h, --help      show this help message and exit

subcommands:
  {login,logout}
    login         Login to contxt
    logout        Logout of contxt
```

## assets
```console
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

## bus
```console
$ contxt bus -h
usage: contxt bus [-h] {channels} ...

optional arguments:
  -h, --help  show this help message and exit

subcommands:
  {channels}
    channels  Get channels
```

## contxt
```console
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

## ems
```console
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

## iot
```console
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

# Examples

## Exporting IOT Data
You can export field data from the IOT service with the following command:
```console
$ contxt iot field-data -h
usage: contxt iot field-data [-h] [-e END_DATE] [-p]
                             grouping_id start_date {0,60,900,3600}
```

For example:
```console
$ contxt iot field-data "09d26434-7b5b-448f-911c-2deb5e9a78ce" "2019-02-01" 60
```

This command will create the directory `export_<grouping_slug>_<current_time>` with csv files of the associated records each field within the grouping and within the specified time range. There is also a `meta.json` file which contains specific information about the export like row counts, field ids, and units.