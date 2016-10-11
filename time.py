import calendar


def get_utc_seconds(t):
    return calendar.timegm(t.utctimetuple())
