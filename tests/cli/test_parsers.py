from contxt.cli.parsers import ArgParser, AssetsParser, AuthParser
import contxt.__main__ as contxt
import pytest

@pytest.fixture()
def setup_parser_args():
    parser = contxt.create_parser()
    return parser.parse_args()

def test_create_parser(setup_parser_args):
    if not setup_parser_args:
        pytest.fail("No args exist for parser")

def test_facility_parser(setup_parser_args):
    pass
    
    
def test_iot_parser(setup_parser_args):
    pass