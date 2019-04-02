from contxt.cli.parsers import ArgParser, AssetsParser, AuthParser
import contxt.__main__ as contxt
import pytest

@pytest.fixture()
def setup_parser():
    return contxt.create_parser()

def test_create_parser(setup_parser):
    args = setup_parser.parse_args()
    if not args:
        pytest.fail("No args exist for parser")

def test_facility_parser(setup_parser):
    pass

def test_iot_parser(setup_parser):
    pass