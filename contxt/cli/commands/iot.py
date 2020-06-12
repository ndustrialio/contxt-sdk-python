from pathlib import Path

from contxt.models import Parsers
from contxt.models.iot import Window
from contxt.services import IotService
from contxt.utils.serializer import Serializer

from .common import BaseParser, to_csv


class Iot(BaseParser):
    def _init_parser(self, subparsers):
        parser = subparsers.add_parser("iot", help="IOT service")
        parser.set_defaults(func=self._help)
        _subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

        # Groupings
        groupings_parser = _subparsers.add_parser("groupings", help="Get groupings")
        groupings_parser.add_argument("facility_id", type=int, help="Facility id")
        groupings_parser.set_defaults(func=self._groupings)

        # Feeds
        feeds_parser = _subparsers.add_parser("feeds", help="Get feeds")
        feeds_parser.add_argument("-f", "--facility-id", type=int, help="Facility id")
        feeds_parser.set_defaults(func=self._feeds)

        # Fields
        fields_parser = _subparsers.add_parser("fields", help="Get fields")
        fields_group = fields_parser.add_mutually_exclusive_group(required=True)
        fields_group.add_argument("-f", "--facility-id", type=int, help="Facility id")
        fields_group.add_argument("-g", "--grouping-id", help="Grouping id")
        fields_parser.set_defaults(func=self._fields)

        # Unprovisioned Fields
        unprovisioned_fields_parser = _subparsers.add_parser(
            "unprovisioned", help="Unprovisioned fields"
        )
        feeds_group = unprovisioned_fields_parser.add_mutually_exclusive_group(required=True)
        feeds_group.add_argument("--feed_key", help="Provide feed key")
        feeds_group.add_argument("--feed_id", type=int, help="Provide feed id")
        unprovisioned_fields_parser.add_argument("--output", help="Dump results to csv if desired")
        unprovisioned_fields_parser.set_defaults(func=self._unprovisioned)

        # Field data
        field_data_parser = _subparsers.add_parser("field-data", help="Get field data")
        field_data_parser.add_argument("grouping_id", help="Grouping id")
        field_data_parser.add_argument("start_time", type=Parsers.datetime, help="Data start time")
        field_data_parser.add_argument(
            "window", type=lambda x: Window(int(x)), help="Data windowing period"
        )
        field_data_parser.add_argument("-e", "--end-time", type=Parsers.datetime, help="Data end time")
        field_data_parser.add_argument("-o", "--output", type=Path, help="File for output")
        field_data_parser.set_defaults(func=self._field_data)

        return parser

    def _groupings(self, args):
        iot_service = IotService(args.auth)
        groupings = iot_service.get_field_groupings_for_facility(args.facility_id)
        print(groupings)

    def _feeds(self, args):
        iot_service = IotService(args.auth)
        feeds = iot_service.get_feeds(args.facility_id)
        print(feeds)

    def _fields(self, args):
        iot_service = IotService(args.auth)
        if args.facility_id:
            # Get fields for facility
            fields = iot_service.get_fields_for_facility(args.facility_id)
        else:
            # Get fields for grouping
            fields = iot_service.get_field_grouping(args.grouping_id).fields
        print(fields)

    def _unprovisioned(self, args):
        iot_service = IotService(args.auth)
        fields = (
            iot_service.get_unprovisioned_fields_for_feed_id(args.feed_id)
            if args.feed_id
            else iot_service.get_unprovisioned_fields_for_feed_key(args.feed_key)
        )

        if args.output:
            to_csv(args.output, fields)
        else:
            print(fields)

    def _field_data(self, args):
        iot_service = IotService(args.auth)
        fields = iot_service.get_field_grouping(args.grouping_id).fields
        print(f"Fetching iot data for {len(fields)} tags for {args.start_time}" f" - {args.end_time}...")
        try:
            field_data = {}
            for field in fields:
                for d in iot_service.get_time_series_for_field(
                    field=field, start_time=args.start_time, end_time=args.end_time, window=args.window
                ):
                    field_data.setdefault(d[0], {})[field.field_human_name] = d[1]
        except MemoryError:
            print("ERROR: Ran out of memory. Trying fetching a smaller date range.")

        # Output to csv
        print(f"Writing field data to {args.output}...")
        data = [{"timestamp": k, **v} for k, v in field_data.items()]
        Serializer.to_csv(data, args.output)
