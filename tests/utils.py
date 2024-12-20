try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo
from dateutil.zoneinfo import get_zonefile_instance


def make_full_tz_list():
    dateutil_zones = set(get_zonefile_instance().zones)
    zoneinfo_zones = set(zoneinfo.available_timezones())
    return dateutil_zones.union(zoneinfo_zones)


def assert_datetime_equality(dt1, dt2, within=10):
    assert dt1.tzinfo == dt2.tzinfo
    assert abs((dt1 - dt2).total_seconds()) < within
