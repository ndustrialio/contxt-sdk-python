from csv import DictWriter
from pathlib import Path

from contxt.services import ContxtService


def get_org_id(name, auth):
    contxt_service = ContxtService(auth)
    return contxt_service.get_organization_with_name(name).id


def to_csv(self, filename, items):
    with Path(filename).open("w") as f:
        writer = DictWriter(f, fieldnames=vars(items[0]))
        writer.writeheader()
        for item in items:
            writer.writerow(vars(item))


class BaseParser:
    def __init__(self, subparsers):
        self.parser = self._init_parser(subparsers)

    def _init_parser(self, subparsers):
        raise NotImplementedError

    def _help(self, args):
        self.parser.print_help()
