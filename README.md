# Contxt Python SDK

## Getting Started
Create a virtual env on your machine for this python project and clone this repo

**IMPORTANT**: Requires Python 3.5+

```
# Make sure virtualenv is installed
pip install virtualenv

# Create a new virtual environment for this project
virtualenv python-sdk --python=python3

# Move into the new created directory
cd python-sdk/

# Clone this GitHub repo
git clone https://github.com/ndustrialio/contxt-sdk-python.git

# Move into the clone repo directory
cd contxt-sdk-python
```

In order to run the CLI, you must first install the dependencies (in the `requirements.txt` file) and setup your environment.

```
# Install the dependencies
pip install -r requirements.txt
```

Additionally, there is support for command line tab completion via [argcomplete](https://github.com/kislyuk/argcomplete). To active, run the following and refresh your bash environment:
```
activate-global-python-argcomplete
```

### Running the code

#### Logging In
In order to make some calls to the Contxt APIs, we first need to login for the first time. To do that, type in the following:
```
python main.py auth login
```

It will prompt you for your username and password, which is the same as the login you would use to login to any one of your Contxt applications.
You should see output such as below:

```
(cli) Johns-MacBook-Pro-3:cli john$ python main.py auth login
Token file has not been created yet
2019-02-07 01:22:18,515 INFO     [novo.utils.auth]  Token doesn't exist or can't be refreshed. Please re-authenticate (auth.py:121)
Contxt Username: <user>@<email>
Contxt Password:
```

### Current list of commands:

#### IOT CLI:
```
iot groupings get-all --facility_id <facility_id>
iot groupings get-fields --id <grouping_id>
iot groupings get-data-for-fields --id <grouping_id> --start_date <iso8601 Date> --end_date <iso8601 Date> --window <0, 60, 900, 3600>
iot feeds get-all --facility_id <facility_id>
```

#### Auth CLI:
```
auth login
auth reset
```

#### Contxt CLI:
```
contxt organizations get-all
contxt organizations create --organization_name "<name>"
contxt organizations add-user --organization_id <organization_id> --user_id <user_id>
contxt organizations get-users (--organization_id <organization_id OR --organization_name <organization_name>)
```

#### EMS CLI:
```
ems utilities get-spend --facility_id <facility_id> --interval <monthly, daily> --resource_type <electric> --start_date <YYYY-MM> --end_date <YYYY-MM>
ems utilities get-organization-spend --organization_id <organization_id> --interval <monthly> --resource_type <electric> --start_date <YYYY-MM> --end_date <YYYY-MM>
```

#### Assets CLI:
```
assets facilities get-all --organization_id <organization_id> --organization_name <organization_name>

```

### Exporting IOT Data

In order to export some data from the IOT service, you will need an ID of a field grouping you want to extract data for. For example, given the output above,
I want to pull data for February 2019 so far from a grouping. The command to do so would be the following:

```
python main.py iot groupings get-data-for-fields --id 09d26434-7b5b-448f-911c-2deb5e9a78ce --start_date 2019-02-01 --window 60
```

In the above command, I'm using the `get-data-for-fields` command and specifying the grouping ID via `id`, the start date via `start_date`, and the window (in seconds) via `window`. Notice that we did not specify
 `end_date` -- if this parameter is not provided, it will always assume the current time as the end date.

The output of this command is a directory in the format of `export_<grouping_slug>_<current_time>` filled with .CSV files of the records pulled for each of the fields within that grouping within the specified time range.
There is also a `meta.json` file which contains specific information about the export like row counts, field IDs (for future use), and units.
