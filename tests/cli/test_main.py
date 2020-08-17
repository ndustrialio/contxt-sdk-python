from unittest.mock import patch

import pytest

from contxt.cli.main import create_parser


@pytest.fixture
def parser():
    return create_parser()


def test_auth_parser(parser):
    parser.parse_args(["auth"])
    parser.parse_args(["auth", "login"])
    parser.parse_args(["auth", "logout"])


@patch("contxt.cli.commands.auth.Auth._login", return_value=True)
def test_auth_parser_login(mock_login):
    parser = create_parser()
    login_cmd = parser.parse_args(["auth", "login"])
    login_cmd.func(login_cmd)


@patch("contxt.cli.commands.auth.Auth._logout", return_value=True)
def test_auth_parser_logout(mock_logout):
    parser = create_parser()
    logout_cmd = parser.parse_args(["auth", "logout"])
    logout_cmd.func(logout_cmd)


def test_iot_groupings_parser(parser):
    parser.parse_args(["iot"])
    parser.parse_args(["iot", "groupings", "100"])


def test_iot_feeds_parser(parser):
    parser.parse_args(["iot"])
    parser.parse_args(["iot", "feeds", "-f", "100"])
    parser.parse_args(["iot", "feeds", "--facility-id", "100"])


def test_iot_fields_parser(parser):
    parser.parse_args(["iot"])
    parser.parse_args(["iot", "fields", "-f", "100"])
    parser.parse_args(["iot", "fields", "--facility-id", "100"])
    parser.parse_args(["iot", "fields", "-g", "200"])
    parser.parse_args(["iot", "fields", "--grouping-id", "200"])


def test_iot_unprovisioned_parser(parser):
    parser.parse_args(["iot"])
    parser.parse_args(["iot", "unprovisioned", "--feed_key", "100"])
    parser.parse_args(["iot", "unprovisioned", "--feed_id", "100"])
    parser.parse_args(["iot", "unprovisioned", "--feed_key", "100", "--output", "dump_file.csv"])
    parser.parse_args(["iot", "unprovisioned", "--feed_id", "100", "--output", "dump_file.csv"])
