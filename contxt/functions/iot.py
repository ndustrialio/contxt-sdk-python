import csv
import json
from datetime import datetime
from pathlib import Path

import pandas as pd
from tqdm import tqdm

from contxt.legacy.services.iot import IOTService
from contxt.utils import make_logger
from contxt.utils.vis import DataVisualizer

logger = make_logger(__name__)


class FeedArgumentException(Exception):
    pass


class FeedNotFoundException(Exception):
    pass


class IOT:
    def __init__(self, auth):
        self.iot_service = IOTService(auth)

    def get_feed_id_from_key(self, feed_key):
        feeds = self.iot_service.get_feeds_collection(key=feed_key)
        if len(feeds) > 0:
            return feeds[0]
        else:
            return None

    def get_unprovisioned_fields_for_feed(self, feed_id=None, feed_key=None):

        if feed_id is None and feed_key is None:
            raise FeedArgumentException("Must provide either feed_key or feed_id")

        if feed_id is None:
            feed = self.get_feed_id_from_key(feed_key)
            if not feed:
                raise FeedNotFoundException(f"Feed with key {feed_key} not found")
            feed_id = feed.id

        return self.iot_service.get_unprovisioned_fields(feed_id)

    def get_fields_for_grouping(self, grouping_id):
        return self.iot_service.get_single_grouping(grouping_id).fields

    def get_field_data_for_grouping(
        self, grouping_id, start_date, window, end_date=None, plot=False
    ):
        def parse_date_str(date_str):
            return datetime.strptime(date_str, "%Y-%m")

        # Get grouping
        grouping = self.iot_service.get_single_grouping(grouping_id)

        if grouping is None:
            logger.critical(f"Grouping {grouping_id} not found")
            return

        # Get data for fields in grouping
        self.iot_service.get_feeds_collection(2)
        logger.info(f"Pulling data for fields: \n{grouping.fields}")
        iso_start_date = parse_date_str(start_date)
        iso_end_date = parse_date_str(end_date) if end_date else None
        field_data = [
            self.iot_service.get_data_for_field(
                output_id=f.output_id,
                field_human_name=f.field_human_name,
                start_time=iso_start_date,
                window=window,
                end_time=iso_end_date,
                limit=5000,
            )
            for f in tqdm(grouping.fields)
        ]

        # Plot or dump to csv
        if plot:
            self.plot_field_data(grouping.fields, field_data)
        else:
            curr_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
            export_path = Path(f"export_{grouping.slug}_{curr_time}")
            self.export_field_data(
                export_path=export_path,
                field_list=grouping.fields,
                data_list=field_data,
                start_date=start_date,
                end_date=end_date,
                window=window,
            )

    def export_field_data(
        self, export_path, field_list, data_list, start_date, end_date, window
    ):
        logger.info(f"Writing files to {export_path}")
        export_path.mkdir(parents=True)

        # Write data
        field_meta = {}
        for field, data in zip(field_list, data_list):
            filepath = export_path / f"{field.field_descriptor}.csv"
            row_counter = 0
            with filepath.open("w") as f:
                writer = csv.DictWriter(f, fieldnames=["event_time", "value"])
                writer.writeheader()
                for record in data:
                    writer.writerow(record)
                    row_counter += 1

            logger.info(f"Wrote {row_counter} rows to csv")
            field_meta[field.field_human_name] = {
                "filename": str(filepath),
                "row_count": row_counter,
                "field_id": field.id,
                "units": field.units,
            }

        # Write metadata file
        meta = {
            "fields": field_meta,
            "parameters": {
                "field_list": [field.field_human_name for field in field_list],
                "start_date": str(start_date),
                "end_date": str(end_date) if end_date is not None else None,
                "window": window,
            },
        }

        meta_filepath = export_path / "meta.json"
        with meta_filepath.open("w") as f:
            json.dump(meta, f, indent=4)

    def plot_field_data(self, fields, field_data):
        data_vis = DataVisualizer(multi_plots=False)

        # Create graphs
        labeled_graphs = {
            f.field_human_name: data_vis._create_scatter_plot(
                df=pd.DataFrame.from_dict(d.records),
                x_label="event_time",
                y_label="value",
                name=f.field_human_name,
                line=dict(shape="spline"),
            )
            for f, d in zip(fields, field_data)
        }

        # Plot
        data_vis.run(labeled_graphs, title="IOT Field Data")
