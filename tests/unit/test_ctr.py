import pytest

from contxt.models.changetrackingrecord import ChangeTrackingRecord, CTRHeader


def test_ctr_wrong_topic():
    with pytest.raises(AttributeError):
        ChangeTrackingRecord(404, 1020304, 0, "soruce", "table", "db", {"a": 1, "b": 2, "c": 3})


def test_ctr_wrong_version_str():
    with pytest.raises(AttributeError):
        ChangeTrackingRecord("Mytopic", "1.1.0", 0, "soruce", "table", "db", {"a": 1, "b": 2, "c": 3})


def test_ctr_wrong_version_float():
    with pytest.raises(AttributeError):
        ChangeTrackingRecord(
            "Mytopic", 534543.9457, 0, "soruce", "table", "db", {"a": 1, "b": 2, "c": 3}
        )


def test_ctr_wrong_operation():
    with pytest.raises(AttributeError):
        ChangeTrackingRecord("Mytopic", 120304, 9, "soruce", "table", "db", {"a": 1, "b": 2, "c": 3})


def test_ctr_wrong_host():
    with pytest.raises(AttributeError):
        ChangeTrackingRecord("Mytopic", 1020304, 0, 3480, "table", "db", {"a": 1, "b": 2, "c": 3})


def test_ctr_wrong_table():
    with pytest.raises(AttributeError):
        ChangeTrackingRecord(404, 1020304, 0, "soruce", 766, "db", {"a": 1, "b": 2, "c": 3})


def test_ctr_wrong_db():
    with pytest.raises(AttributeError):
        ChangeTrackingRecord(404, 1020304, 0, "soruce", "table", 404, {"a": 1, "b": 2, "c": 3})


def test_get_json_string():
    ctr = ChangeTrackingRecord("myTopic", 1020304, 0, "soruce", "table", "db", {"a": 1, "b": 2, "c": 3})
    expected = '{"topic": "myTopic", "version": 1020304, "operation": 0, "source_host": "soruce", "source_table": "table", "source_database": "db", "tuple": {"a": 1, "b": 2, "c": 3}, "headers": {"forwardable": true, "deduplicatable": true}, "addlParams": {}}'
    assert ctr.getJSONString() == expected


def test_set_headers():
    ctr = ChangeTrackingRecord(
        "myTopic",
        1020304,
        0,
        "soruce",
        "table",
        "db",
        {"a": 1, "b": 2, "c": 3},
        CTRHeader(forwardable=False, deduplicatable=False),
    )
    expected = '{"topic": "myTopic", "version": 1020304, "operation": 0, "source_host": "soruce", "source_table": "table", "source_database": "db", "tuple": {"a": 1, "b": 2, "c": 3}, "headers": {"forwardable": false, "deduplicatable": false}, "addlParams": {}}'
    assert ctr.getJSONString() == expected


def test_get_json_string():
    ctr = ChangeTrackingRecord("myTopic", 1020304, 0, "soruce", "table", "db", {"a": 1, "b": 2, "c": 3})
    ctr.addlParams = {"forwardChannel": "canonical-fwd"}
    expected = '{"topic": "myTopic", "version": 1020304, "operation": 0, "source_host": "soruce", "source_table": "table", "source_database": "db", "tuple": {"a": 1, "b": 2, "c": 3}, "headers": {"forwardable": true, "deduplicatable": true}, "addlParams": {"forwardChannel": "canonical-fwd"}}'
    assert ctr.getJSONString() == expected
