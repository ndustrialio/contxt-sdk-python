from unittest.mock import patch

import pytest

import contxt.__main__ as contxt
from contxt.cli.parsers import AssetsParser, AuthParser, ContxtArgParser


@pytest.fixture(scope="module")
def setup_parser_args():
    parser, subparsers = contxt.create_parser()
    return parser


def test_create_parser(setup_parser_args):
    if not setup_parser_args.parse_args():
        pytest.fail("No args exist for parser")


def test_auth_parser(setup_parser_args):
    setup_parser_args.parse_args(["auth"])
    setup_parser_args.parse_args(["auth", "login"])
    setup_parser_args.parse_args(["auth", "logout"])


@patch("contxt.cli.parsers.AuthParser._login", return_value=True)
def test_auth_parser_login(mock_login):
    parser, subparsers = contxt.create_parser()
    login_cmd = parser.parse_args(["auth", "login"])
    login_cmd.func(login_cmd)


@patch("contxt.cli.parsers.AuthParser._logout", return_value=True)
def test_auth_parser_login(mock_logout):
    parser, subparsers = contxt.create_parser()
    logout_cmd = parser.parse_args(["auth", "logout"])
    logout_cmd.func(logout_cmd)


def test_iot_groupings_parser(setup_parser_args):
    setup_parser_args.parse_args(["iot"])
    setup_parser_args.parse_args(["iot", "groupings", "100"])


def test_iot_feeds_parser(setup_parser_args):
    setup_parser_args.parse_args(["iot"])
    args = setup_parser_args.parse_args(["iot", "feeds", "-f", "100"])
    setup_parser_args.parse_args(["iot", "feeds", "--facility-id", "100"])


def test_iot_fields_parser(setup_parser_args):
    setup_parser_args.parse_args(["iot"])
    setup_parser_args.parse_args(["iot", "fields", "-f", "100"])
    setup_parser_args.parse_args(["iot", "fields", "--facility-id", "100"])
    setup_parser_args.parse_args(["iot", "fields", "-g", "200"])
    setup_parser_args.parse_args(["iot", "fields", "--grouping-id", "200"])


def test_iot_unprovisioned_parser(setup_parser_args):
    setup_parser_args.parse_args(["iot"])
    setup_parser_args.parse_args(["iot", "unprovisioned", "--feed_key", "100"])
    setup_parser_args.parse_args(["iot", "unprovisioned", "--feed_id", "100"])
    setup_parser_args.parse_args(
        ["iot", "unprovisioned", "--feed_key", "100", "--output", "dump_file.csv"]
    )
    setup_parser_args.parse_args(
        ["iot", "unprovisioned", "--feed_id", "100", "--output", "dump_file.csv"]
    )
