from datetime import datetime, timedelta, timezone


def datetime_utc_now():
    return datetime.now(timezone.utc)


def datetime_zulu_now():
    return datetime_zulu_format(datetime_utc_now())


def datetime_utc_check(dt: datetime):
    assert isinstance(dt, datetime), f"Argument should be a datetime instance, got {type(dt)}"
    assert dt.utcoffset() == timedelta(), f"Expected datetime in UTC timezone, got {dt} [{dt.tzinfo}]"
    return dt


def datetime_zulu_format_short(dt: datetime):
    return datetime_utc_check(dt).strftime("%Y-%m-%dT%H:%MZ")


def datetime_zulu_parse(timestamp):
    return datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=timezone.utc)


def datetime_zulu_format(dt: datetime):
    return datetime_utc_check(dt).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
