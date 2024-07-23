import time
from datetime import datetime


def parse_datetime(dt: str) -> int:
    dt_format = "%Y-%m-%d %H:%M:%S"

    try:
        dt_object = datetime.strptime(dt, dt_format)
    except ValueError as e:
        print(f"Format date-time error: {e}")
        return False

    unix_time = int(time.mktime(dt_object.timetuple()))
    return unix_time
