# Contxt Python SDK
[![wercker status](https://app.wercker.com/status/960b7b32c2d94d12a3a5c89ca17e13ba/s/ "wercker status")](https://app.wercker.com/project/byKey/960b7b32c2d94d12a3a5c89ca17e13ba)

## Dependencies
This project **requires** Python 3.6+.

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

## Contributing
Please refer to the [release guide](docs/release.md).

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

## Workers 

### Machine Authentication
Since the CLI interface is just a wrapper around different functions in the SDK, users can also leverage these
functions in their own code. Within Contxt we have a concept of a machine user that is identified by a unique
client_id / client_secret pair (instead of a user/pass combination like regular users). When writing code that
will eventually go to production that will need to call other APIs (this is obviously quite common), your service
will automatically be given a unique client_id / client_secret pair within Contxt. When you create this service,
you can use these credentials in your local development environment as well.

### Base Worker Class
In order to make development easier, we have a Worker Base Class we provide in the SDK to abstract away the
nuance of the authentication process (if you're curious, [here](https://contxt.readme.io/docs/machine-to-machine-authentication) is a link to the documentation on this process, in
case you're really REALLY bored and looking for some "light" reading). In the root path of this SDK, you'll
see an "examples" directory that contains a few example of how to do various tasks. In the file "sample_worker.py",
you will see a very simple example of how to implement the BaseWorker class.

In this sample worker file, you will see just a few lines of code, to get started. It is vitally important, however,
to set your environment variables for CLIENT_ID and CLIENT_SECRET. We provide these in the environment for 2
reasons:
- You never want to put your client_id / client_secret pair in your code to be committed anywhere. This is a
major no-no as these should be regarded the same as user credentials
- Contxt will automatically set these in the environment upon deployment to a Contxt environment (staging, prod, etc.)
so setting this up in development will make it seamless upon deployment

Looking at this [example](examples/worker.py), you can see that we're implementing the `BaseWorker` class. Behind
the scenes, that class is doing all the work around getting tokens, refreshing tokens, etc. so you don't have to. In
this example, we're going to make a call to the Contxt Facilities (Assets) Service to get a list of facilities available
to this worker (machine user). To do so, we must instantiate the Facilities class and pass in `self.auth`.

Next, in the `do_work` method, it's just making a simple
call to `get_facilities`. You can iterate over this list, or just print it to
the console (like we've done here).

From here, you can continue to code up your application logic to perform whatever tasks you need using all the SDK
functions available to you.

## CLI Examples

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
