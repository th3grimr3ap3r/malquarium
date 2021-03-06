from datetime import datetime

import pytz

from malquarium.settings import TIME_ZONE


def get_datetime_now():
    return datetime.now(tz=pytz.timezone(TIME_ZONE))


def get_date_now():
    return get_datetime_now().date()


def timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp, tz=pytz.timezone(TIME_ZONE))
