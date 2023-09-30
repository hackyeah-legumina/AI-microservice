import uuid

from datetime import timezone, datetime, timedelta
import datetime


def utc_converter(dt):
    dt = datetime.datetime.now(timezone.utc)
    utc_time = dt.replace(tzinfo=timezone.utc)
    utc_timestamp = utc_time.timestamp()
    return utc_timestamp


class Session:
    def __init__(self):
        self.id = uuid.uuid1()
        self.tags_dict = {}
        self.expiration_time = self.__get_expiration_time()

    def __get_expiration_time(self):
        _now = datetime.datetime.now()
        _end = _now + timedelta(seconds=10)

        return _end
