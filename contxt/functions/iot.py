import csv
import json
import os
from datetime import datetime

import dateutil.parser
import pandas as pd
from plotly import graph_objs as go

from contxt.services.iot import IOTService
from contxt.utils import make_logger
from contxt.utils.vis import DataVisualizer

logger = make_logger(__name__)


class IOT:

    def __init__(self, auth_module):

        self.auth = auth_module

        self.iot_service = IOTService(self.auth)

    def get_fields_for_grouping(self, grouping_id):

        return self.iot_service.get_single_grouping(grouping_id).fields

    def get_data_for_fields(self, grouping_id, start_date, window, end_date=None, plot=False):

        iso_start_date = dateutil.parser.parse(start_date)

        iso_end_date = None
        if end_date:
            iso_end_date = dateutil.parser.parse(end_date)

        grouping = self.iot_service.get_single_grouping(grouping_id)

        if grouping is None:
            logger.critical("Grouping Not Found")
            return

        # TODO: add flag to plot
        # TODO: field_data is undefined, looks like we lost code in fixing 
        # merge conflicts 
        if plot:
            self.plot_field_data(grouping.fields, field_data)
        else:
            export_directory = os.path.join("./", "export_{}_{}".format(grouping.slug,
                                                                        datetime.now().strftime(
                                                                            "%Y-%m-%d_%H:%M:%S")))

            self.write_field_data_to_csv(export_directory, grouping.fields, iso_start_date, iso_end_date, window)

    def plot_field_data(self, fields, field_data):

        def create_graph(field_name, field_data):
            # TODO: need to parse datetime and value
            df = pd.DataFrame.from_dict(field_data.records)
            if not df.empty:
                df = df.sort_values('event_time')
            return go.Scatter(
                x=df.get('event_time'),
                y=df.get('value'),
                name=field_name,
                line=dict(shape='spline'))

        # Create graphs
        labeled_graphs = {
            f.field_human_name: create_graph(f.field_human_name, d)
            for f, d in zip(fields, field_data)
        }

        # Plot
        data_vis = DataVisualizer(multi_plots=False)
        data_vis.run(labeled_graphs, title='IOT Field Data')

    def write_field_data_to_csv(self, export_dir, field_list, start_date, end_date=None, window=60):

        parameter_meta = {
            'field_list': [field.field_human_name for field in field_list],
            'start_date': str(start_date),
            'end_date': str(end_date) if end_date is not None else None,
            'window': window
        }
        logger.info(f"Writing to files in directory: {export_dir}")
        os.makedirs(export_dir, exist_ok=False)

        logger.info(f"Parameters: start_date -> {start_date}, end_date -> {end_date}, window -> {window}")

        logger.info("Pulling data for the following fields:")
        print(field_list)

        field_meta = {}
        for field in field_list:
            # TODO go get the data for this field and write to a CSV
            logger.info(f"Pulling data for {field.field_human_name}")
            data = self.iot_service.get_data_for_field(output_id=field.output_id,
                                                       field_human_name=field.field_human_name,
                                                       start_time=start_date,
                                                       window=window,
                                                       end_time=end_date,
                                                       limit=5000)

            filename = os.path.join(export_dir,
                                    f"{field.field_descriptor}.csv")

            row_counter = 0
            with open(filename, 'w') as f:
                writer = csv.DictWriter(f, fieldnames=["event_time", "value"])
                writer.writeheader()

                for record in data:
                    writer.writerow(record)
                    row_counter += 1

            field_meta[field.field_human_name] = {
                'row_count': row_counter,
                'filename': filename,
                'units': field.units,
                'field_id': field.id
            }

            logger.info(f"Wrote {row_counter} rows to CSV")

        # Write metadata file
        meta = {
            'fields': field_meta,
            'parameters': parameter_meta
        }

        with open(os.path.join(export_dir, 'meta.json'), 'w') as f:
            json.dump(meta, f, indent=4)
