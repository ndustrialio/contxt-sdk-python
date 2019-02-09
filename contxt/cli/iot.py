from contxt.services.iot import IOTService
from datetime import datetime
import dateutil.parser
import csv
import json
import os

from contxt.utils import make_logger

logger = make_logger(__name__)


class IOT:

    def __init__(self, cli_module, arg_parser):
        self.cli = cli_module

        arg_parser.add_argument("command", type=str, help="The primary command to run within this IOT module")
        arg_parser.add_argument("subcommand")

        arg_parser.add_argument("--facility_id", required=False, dest="facility_id", type=int,
                                help="Provide the facility_id (integer) as a filter when possible")
        arg_parser.add_argument("--id", required=False, dest="entity_id",
                                help="ID of the entity being requested. Required for some subcommands.")
        arg_parser.add_argument("--start_date", required=False, dest="start_date", type=str,
                                help="When querying for data, this is a required field. This is the start date of the "
                                     "data being queried.")
        arg_parser.add_argument("--end_date", required=False, dest="end_date", type=str,
                                help="When querying for data, this is an optional field. This is the end date of the "
                                     "data being queried. If not provided, this defaults to the current time.")
        arg_parser.add_argument("--window", required=False, dest="window", type=int,
                                help="When querying for data, this is an optional field. This is the time window of "
                                     "the data being queried in seconds. The window is the interval in which data "
                                     "is sliced.")

        self.iot_service = IOTService(self.cli.auth)

    '''
        iot groupings get-all --facility_id <facility_id>
        iot groupings get-fields --id <grouping_id>
        iot groupings get-data-for-fields --id <grouping_id> --start_date <iso8601 Date> --end_date <iso8601 Date> --window <0, 60, 900, 3600>
        iot fields get-all --facility_id <facility_id>
        iot fields get-data --id <field_id>
    '''
    def parse_command(self, command, args):

        if args.command == 'groupings':
            if args.subcommand is None:
                if args.facility_id is None:
                    logger.critical("--facility_id required for groupings get-all call")
                    return

            elif args.subcommand == 'get-fields':
                if args.entity_id is None:
                    logger.critical("--id required for groupings get-fields call to indicate the grouping id")
                    return

                print('Getting fields for grouping with id {}'.format(args.entity_id))

                print(self.iot_service.get_single_grouping(args.entity_id).fields if not None else 'Grouping Not Found')

            elif args.subcommand == 'get-data-for-fields':
                if args.entity_id is None:
                    logger.critical("--id required for groupings get-data-for-fields call to indicate the grouping id")
                    return

                if args.start_date is None:
                    logger.critical("--start_date required for groupings get-data-for-fields call to indicate the "
                                    "data start date")
                    return

                iso_start_date = dateutil.parser.parse(args.start_date)

                iso_end_date = None
                if args.end_date:
                    iso_end_date = dateutil.parser.parse(args.end_date)

                grouping = self.iot_service.get_single_grouping(args.entity_id)

                if grouping is None:
                    logger.critical("Grouping Not Found")
                    return

                export_directory = os.path.join("./", "export_{}_{}".format(grouping.slug,
                                                                            datetime.now().strftime(
                                                                                "%Y-%m-%d_%H:%M:%S")))

                self.write_field_data_to_csv(export_directory, grouping.fields, iso_start_date, iso_end_date, args.window)

            elif args.subcommand == 'get-all':
                # General call to get groupings
                if args.facility_id is None:
                    logger.critical("--facility_id required for groupings get-all call to indicate the grouping id")
                    return
                print(self.iot_service.get_all_groupings(facility_id=int(args.facility_id)))

            else:
                logger.critical("Invalid subcommand. Must be one of {get-all, get-data-for-fields, get-fields}")
                return
        elif args.command == 'feeds':
            if args.subcommand is None or args.subcommand == 'get-all':
                print(self.iot_service.get_all_feeds(facility_id=args.facility_id))
            else:
                logger.critical("Invalid subcommand. Must be one of {get-all}")
                return
        else:
            logger.critical('Unrecognized command: {}'.format(args.command))

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
