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

### Running the code

#### Logging In
In order to make some calls to the Contxt APIs, we first need to login for the first time. To do that, type in the following:
```
python main.py auth login
```

It will prompt you for your username and password, which is the same as the login you would use to login to any one of your Contxt applications.
You should see output such as below:

```
(novo-cli) Johns-MacBook-Pro-3:novo-cli john$ python main.py auth login
Token file has not been created yet
2019-02-07 01:22:18,515 INFO     [novo.utils.auth]  Token doesn't exist or can't be refreshed. Please re-authenticate (auth.py:121)
Contxt Username: novozymes@ndustrial.io
Contxt Password:
```

Next, let's make a call to get the field groupings from a particular facility:

```
python main.py iot groupings get-all --facility_id 184
```

This will reach out to the IOT service and retrieve all field groupings at the facility (184 in this case), and print them to the screen. The output of this will look something like below:

```
(novo-cli) Johns-MacBook-Pro-3:novo-cli john$ python main.py iot groupings get-all --facility_id 184
id                                    label                     slug                      description              facility_id  field_category_id                     field_category_name      field_count
------------------------------------  ------------------------  ------------------------  ---------------------  -------------  ------------------------------------  ---------------------  -------------
0117625f-d464-48d6-9feb-4324e16b30a8  Batch Ethanol Fields      batch-ethanol-fields      Ethanol Fields                   184  e9cab7e2-7b8b-4a97-aa54-bca11e2e7b13  Overall Batch                     12
02d16dbe-8e11-4770-93b8-ee0840475070  Yeast Fields              yeast-fields              Yeast Fields                     184                                                                           7
09d26434-7b5b-448f-911c-2deb5e9a78ce  Fermentation Tank #1      fermentation-tank-1       Fermentation Tank #1             184  ad29cb46-ed83-41b0-9dbb-eb22cd6adce0  Ferm                              17
1529bb3a-a97e-48c2-a527-c33271a94d4c  Batch Viability Fields    batch-viability-fields    Batch Viability                  184  e9cab7e2-7b8b-4a97-aa54-bca11e2e7b13  Overall Batch                     10
15b8d6a3-39e5-444c-a968-5c8f34059727  Batch Maltose Fields      batch-maltose-fields      Batch Maltose                    184  e9cab7e2-7b8b-4a97-aa54-bca11e2e7b13  Overall Batch                     10
26f15290-10e0-4299-ac17-99cf55ba5f67  Fermentation Tank #4      fermentation-tank-4       Ferm 4                           184  ad29cb46-ed83-41b0-9dbb-eb22cd6adce0  Ferm                              12
563f625d-3b87-45ef-a47b-c50e7b1817ea  Novo DS TS                novo-ds-ts                Novo DS TS                       184                                                                          13
601358e2-501a-437f-a438-7d591ca3f53d  Batch DP3 Fields          batch-dp3-fields          Batch DP3                        184  e9cab7e2-7b8b-4a97-aa54-bca11e2e7b13  Overall Batch                     10
67f7e972-b63a-4b02-a118-9d19baf1d91c  Slurry Fields             slurry-fields             Slurry field grouping            184  99ce5f67-5f3f-4e82-b206-46c8aaa5a2ce  Slurry                             7
6d174afc-de8a-4e6b-b2e2-312449751669  Flash Tank                flash-tank                Flash tank fields                184                                                                           3
7240d5aa-c12b-4dd4-a8f4-7dde81da3483  Fermentation Tank #5      fermentation-tank-5       Ferm 5                           184  ad29cb46-ed83-41b0-9dbb-eb22cd6adce0  Ferm                              11
79b05c30-821a-4f0c-96a6-70dbbcc1a1ab  Batch Count Fields        batch-count-fields        Batch Count Fields               184  e9cab7e2-7b8b-4a97-aa54-bca11e2e7b13  Overall Batch                     10
85268e0f-a7c5-4b6a-b0ab-e44f3b5c505f  Fermentation Tank #3      fermentation-tank-3       Ferm 3                           184  ad29cb46-ed83-41b0-9dbb-eb22cd6adce0  Ferm                              11
b342ddd2-c784-4154-8989-01427efcf2f5  Batch Brix Fields         batch-brix-fields         Batch Brix                       184  e9cab7e2-7b8b-4a97-aa54-bca11e2e7b13  Overall Batch                     10
b4474677-d9a8-4add-814c-e96c94905447  Batch Fields              batch-fields              Batch fields                     184                                                                          20
bfd495cd-a686-4c56-998b-8b1b507c119e  Fermentation Tank Levels  fermentation-tank-levels  Fermentation Grouping            184                                                                           5
c679ae6e-c5a3-4617-8453-b83b9a4177cd  Propagation Tank          propagation-tank          Prop Tank Fields                 184  02f0a671-9718-4b95-bc70-1a28c0f0a5a8  Prop                              14
cece18d4-0db1-47c8-96c4-5050e292a2da  Batch Budding Fields      batch-budding-fields      Batch budding                    184  e9cab7e2-7b8b-4a97-aa54-bca11e2e7b13  Overall Batch                     10
d6f4a029-78cb-44ca-ab82-d94a6dc2ae25  Batch Glycerol Fields     batch-glycerol-fields     Batch Glycerol                   184  e9cab7e2-7b8b-4a97-aa54-bca11e2e7b13  Overall Batch                     10
de207930-813a-45ea-8b55-c29ab5fbcce7  Batch Glucose Fields      batch-glucose-fields      Batch Glucose fields             184  e9cab7e2-7b8b-4a97-aa54-bca11e2e7b13  Overall Batch                     10
e23f93e5-43cc-4bf4-8d82-bb87b9be8273  Batch pH Fields           batch-ph-fields           Batch pH                         184  e9cab7e2-7b8b-4a97-aa54-bca11e2e7b13  Overall Batch                     10
e56cd116-167c-4628-9437-900e50c064f1  Batch Solids Fields       batch-solids-fields       Batch Solids                     184  e9cab7e2-7b8b-4a97-aa54-bca11e2e7b13  Overall Batch                     10
e5c93458-f699-4cd8-8009-7847cdb32f38  Liquefaction              liquefaction              Liquefaction fields              184                                                                           2
ee40ecde-6c04-40c5-9053-94cd5bba83fa  Batch Acetic Fields       batch-acetic-fields       Batch Acetic                     184  e9cab7e2-7b8b-4a97-aa54-bca11e2e7b13  Overall Batch                     10
ee92a7fd-4c76-4665-bf12-a4adf97b0299  Batch Total Sugar         batch-total-sugar         Batch Total Sugar                184  e9cab7e2-7b8b-4a97-aa54-bca11e2e7b13  Overall Batch                     10
eeb13404-dc29-4993-beb7-23c05e64a0ea  Batch DP4 Fields          batch-dp4-fields          Batch DP4                        184  e9cab7e2-7b8b-4a97-aa54-bca11e2e7b13  Overall Batch                     10
f3628a48-dbfd-4512-9e66-20ed2df7856b  Fermentation Tank #2      fermentation-tank-2       Ferm 2                           184  ad29cb46-ed83-41b0-9dbb-eb22cd6adce0  Ferm                              24
f45cf86e-dacd-459d-b03f-b4825dcc3a8a  Batch Lactic Fields       batch-lactic-fields       Batch Lactic Fields              184  e9cab7e2-7b8b-4a97-aa54-bca11e2e7b13  Overall Batch                     10
f8aed46b-c318-4e87-b24b-7c5d00fafcef  Batch Temp Fields         batch-temp-fields         Batch Temps                      184  e9cab7e2-7b8b-4a97-aa54-bca11e2e7b13  Overall Batch                     10
```

It prints out all the information in a table format so you can easily copy and paste needed values for other commands.

### Current list of commands:

#### IOT CLI:
```
iot groupings get-all --facility_id <facility_id>
iot groupings get-fields --id <grouping_id>
iot groupings get-data-for-fields --id <grouping_id> --start_date <iso8601 Date> --end_date <iso8601 Date> --window <0, 60, 900, 3600>
```

#### Auth CLI:
```
auth login
auth reset
```


### Exporting Data

In order to export some data from the IOT service, you will need an ID of a field grouping you want to extract data for. For example, given the output above,
I want to pull data for February 2019 so far from the "Fermentation Tank #1" grouping. The command to do so would be the following:

```
python main.py iot groupings get-data-for-fields --id 09d26434-7b5b-448f-911c-2deb5e9a78ce --start_date 2019-02-01 --window 60
```

In the above command, I'm using the `get-data-for-fields` command and specifying the grouping ID via `id`, the start date via `start_date`, and the window (in seconds) via `window`. Notice that we did not specify
 `end_date` -- if this parameter is not provided, it will always assume the current time as the end date.

The output of this command is a directory in the format of `export_<grouping_slug>_<current_time>` filled with .CSV files of the records pulled for each of the fields within that grouping within the specified time range.
There is also a `meta.json` file which contains specific information about the export like row counts, field IDs (for future use), and units.

The output of this command on the terminal should look like the following:

```
(novo-cli) Johns-MacBook-Pro-3:novo-cli john$ python main.py iot groupings get-data-for-fields --id 09d26434-7b5b-448f-911c-2deb5e9a78ce --start_date 2019-02-01 --window 60
2019-02-07 01:30:11,555 INFO     [novo.cli.iot]  Writing to files in directory: {} (iot.py:107)
2019-02-07 01:30:11,556 INFO     [novo.cli.iot]  Parameters: start_date -> 2019-02-01 00:00:00, end_date -> None, window -> 60 (iot.py:111)
2019-02-07 01:30:11,556 INFO     [novo.cli.iot]  Pulling data for the following fields: (iot.py:113)
    id  label                      output_id  field_descriptor                       field_human_name                       is_hidden    status       units
------  -----------------------  -----------  -------------------------------------  -------------------------------------  -----------  -----------  -------
131621  F1_Ethanol                      8697  WPE.MDE.F1_BATCH_ETHANOL               wpe.mde.f1_batch_ethanol               False        Out-of-Date
131631  F1_Slurry pH Target             8697  WPE.MDE.F1_Batch_Slurry_pH_Target      wpe.mde.f1_batch_slurry_ph_target      False        Active
131632  F1_Slurry Solids Target         8697  WPE.MDE.F1_Batch_Slurry_Solids_Target  wpe.mde.f1_batch_slurry_solids_target  False        Active
131624  F1_Glucose                      8697  WPE.MDE.F1_BATCH_GLUCOSE               wpe.mde.f1_batch_glucose               False        Out-of-Date
131635  F1_Total Sugar                  8697  WPE.MDE.F1_Batch_TotalSugar            wpe.mde.f1_batch_totalsugar            False        Out-of-Date
131626  F1_Lactic                       8697  WPE.MDE.F1_Batch_Lactic                wpe.mde.f1_batch_lactic                False        Out-of-Date
131629  F1_pH                           8697  WPE.MDE.F1_Batch_pH                    wpe.mde.f1_batch_ph                    False        Active
131523  pH                              8697  WPE.FERM_MDE.BATCH_PH                  wpe.ferm_mde.batch_ph                  False        Active
131518  Ethanol                         8697  WPE.FERM_MDE.BATCH_ETHANOL             wpe.ferm_mde.batch_ethanol             False        Out-of-Date
131006  ferm #1 level                   8697  WPE.CAPHIST.LI_3101-PV                 wpe.caphist.li_3101-pv                 False        Active       %LVL
131438  ferm #1 temp                    8697  WPE.CAPHIST.TIC_3101-VL                wpe.caphist.tic_3101-vl                False        Out-of-Date  PCT
131481  Ferm #1 Temp Control SP         8697  WPE.CAPHIST.TTIC_3101-S_SP             wpe.caphist.ttic_3101-s_sp             False        Active       degF
131437  ferm #1 temp                    8697  WPE.CAPHIST.TIC_3101-PV                wpe.caphist.tic_3101-pv                False        Out-of-Date  degF
131482  Ferm #1 Temp Control OP         8697  WPE.CAPHIST.TTIC_3101-S_VL             wpe.caphist.ttic_3101-s_vl             False        Active       PCT
131478  Ferm #1 Temp Control PV         8697  WPE.CAPHIST.TTIC_3101-P_PV             wpe.caphist.ttic_3101-p_pv             False        Active       degF
131479  Ferm #1 Temp Control SP         8697  WPE.CAPHIST.TTIC_3101-P_SP             wpe.caphist.ttic_3101-p_sp             False        Active       degF
131480  Ferm #1 Temp Control PV         8697  WPE.CAPHIST.TTIC_3101-S_PV             wpe.caphist.ttic_3101-s_pv             False        Active       degF
2019-02-07 01:30:11,558 INFO     [novo.cli.iot]  Pulling data for wpe.mde.f1_batch_ethanol (iot.py:119)
2019-02-07 01:30:14,413 INFO     [novo.cli.iot]  Wrote 0 rows to CSV (iot.py:145)
2019-02-07 01:30:14,413 INFO     [novo.cli.iot]  Pulling data for wpe.mde.f1_batch_slurry_ph_target (iot.py:119)
2019-02-07 01:30:15,513 INFO     [novo.cli.iot]  Wrote 139 rows to CSV (iot.py:145)
2019-02-07 01:30:15,513 INFO     [novo.cli.iot]  Pulling data for wpe.mde.f1_batch_slurry_solids_target (iot.py:119)
2019-02-07 01:30:17,492 INFO     [novo.cli.iot]  Wrote 139 rows to CSV (iot.py:145)
2019-02-07 01:30:17,493 INFO     [novo.cli.iot]  Pulling data for wpe.mde.f1_batch_glucose (iot.py:119)
2019-02-07 01:30:18,688 INFO     [novo.cli.iot]  Wrote 0 rows to CSV (iot.py:145)
2019-02-07 01:30:18,689 INFO     [novo.cli.iot]  Pulling data for wpe.mde.f1_batch_totalsugar (iot.py:119)
2019-02-07 01:30:20,199 INFO     [novo.cli.iot]  Wrote 0 rows to CSV (iot.py:145)
2019-02-07 01:30:20,199 INFO     [novo.cli.iot]  Pulling data for wpe.mde.f1_batch_lactic (iot.py:119)
2019-02-07 01:30:21,746 INFO     [novo.cli.iot]  Wrote 0 rows to CSV (iot.py:145)
2019-02-07 01:30:21,747 INFO     [novo.cli.iot]  Pulling data for wpe.mde.f1_batch_ph (iot.py:119)
2019-02-07 01:30:22,940 INFO     [novo.cli.iot]  Wrote 139 rows to CSV (iot.py:145)
2019-02-07 01:30:22,941 INFO     [novo.cli.iot]  Pulling data for wpe.ferm_mde.batch_ph (iot.py:119)
2019-02-07 01:30:24,391 INFO     [novo.cli.iot]  Wrote 139 rows to CSV (iot.py:145)
2019-02-07 01:30:24,391 INFO     [novo.cli.iot]  Pulling data for wpe.ferm_mde.batch_ethanol (iot.py:119)
2019-02-07 01:30:27,386 INFO     [novo.cli.iot]  Wrote 0 rows to CSV (iot.py:145)
2019-02-07 01:30:27,387 INFO     [novo.cli.iot]  Pulling data for wpe.caphist.li_3101-pv (iot.py:119)
2019-02-07 01:30:32,464 INFO     [novo.cli.iot]  Wrote 8343 rows to CSV (iot.py:145)
2019-02-07 01:30:32,464 INFO     [novo.cli.iot]  Pulling data for wpe.caphist.tic_3101-vl (iot.py:119)
2019-02-07 01:30:34,335 INFO     [novo.cli.iot]  Wrote 0 rows to CSV (iot.py:145)
2019-02-07 01:30:34,335 INFO     [novo.cli.iot]  Pulling data for wpe.caphist.ttic_3101-s_sp (iot.py:119)
2019-02-07 01:30:35,696 INFO     [novo.cli.iot]  Wrote 138 rows to CSV (iot.py:145)
2019-02-07 01:30:35,696 INFO     [novo.cli.iot]  Pulling data for wpe.caphist.tic_3101-pv (iot.py:119)
2019-02-07 01:30:37,601 INFO     [novo.cli.iot]  Wrote 0 rows to CSV (iot.py:145)
2019-02-07 01:30:37,601 INFO     [novo.cli.iot]  Pulling data for wpe.caphist.ttic_3101-s_vl (iot.py:119)
2019-02-07 01:30:39,303 INFO     [novo.cli.iot]  Wrote 138 rows to CSV (iot.py:145)
2019-02-07 01:30:39,303 INFO     [novo.cli.iot]  Pulling data for wpe.caphist.ttic_3101-p_pv (iot.py:119)
2019-02-07 01:30:42,390 INFO     [novo.cli.iot]  Wrote 138 rows to CSV (iot.py:145)
2019-02-07 01:30:42,391 INFO     [novo.cli.iot]  Pulling data for wpe.caphist.ttic_3101-p_sp (iot.py:119)
2019-02-07 01:30:43,530 INFO     [novo.cli.iot]  Wrote 138 rows to CSV (iot.py:145)
2019-02-07 01:30:43,530 INFO     [novo.cli.iot]  Pulling data for wpe.caphist.ttic_3101-s_pv (iot.py:119)
2019-02-07 01:30:45,520 INFO     [novo.cli.iot]  Wrote 138 rows to CSV (iot.py:145)

```
