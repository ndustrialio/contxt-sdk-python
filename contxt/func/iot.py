from datetime import datetime
import dateutil.parser
import csv
import json
import os

from contxt.services.iot import IOTService

from contxt.utils import make_logger

logger = make_logger(__name__)


class IOT:

    def __init__(self, auth_module):

        self.auth = auth_module

        self.iot_service = IOTService(self.auth)

    def get_fields_for_grouping(self, grouping_id):

        return self.iot_service.get_single_grouping(grouping_id).fields

    def get_data_for_fields(self, grouping_id, start_date, window, end_date=None):

        iso_start_date = dateutil.parser.parse(start_date)

        iso_end_date = None
        if end_date:
            iso_end_date = dateutil.parser.parse(end_date)

        grouping = self.iot_service.get_single_grouping(grouping_id)

        if grouping is None:
            logger.critical("Grouping Not Found")
            return

        export_directory = os.path.join("./", "export_{}_{}".format(grouping.slug,
                                                                    datetime.now().strftime(
                                                                        "%Y-%m-%d_%H:%M:%S")))

        self.write_field_data_to_csv(export_directory, grouping.fields, iso_start_date, iso_end_date, window)

    def write_field_data_to_csv(self, export_dir, field_list, start_date, end_date=None, window=60):

        parameter_meta = {
            'field_list': [field.field_human_name for field in field_list],
            'start_date': str(start_date),
            'end_date': str(end_date) if end_date is not None else None,
            'window': window
        }
        logger.info("Writing to files in directory: {}")
        os.makedirs(export_dir, exist_ok=False)

        logger.info("Parameters: start_date -> {}, end_date -> {}, window -> {}"
                    .format(start_date, end_date, window))

        logger.info("Pulling data for the following fields:")
        print(field_list)

        field_meta = {}
        for field in field_list:
            # TODO go get the data for this field and write to a CSV
            logger.info("Pulling data for {}".format(field.field_human_name))
            data = self.iot_service.get_data_for_field(output_id=field.output_id,
                                                       field_human_name=field.field_human_name,
                                                       start_time=start_date,
                                                       window=window,
                                                       end_time=end_date,
                                                       limit=5000)

            filename = os.path.join(export_dir, "{}.csv".format(field.field_descriptor))

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

            logger.info("Wrote {} rows to CSV".format(row_counter))

        # Write metadata file
        meta = {
            'fields': field_meta,
            'parameters': parameter_meta
        }

        with open(os.path.join(export_dir, 'meta.json'), 'w') as f:
            json.dump(meta, f, indent=4)
