# coding=utf-8
from __future__ import absolute_import
import calendar
import time


def get_utc_seconds(t):
    return calendar.timegm(t.utctimetuple())


def get_datetime_milliseconds(t, utc=False):
    """将datetime转换为utc毫秒值
    :param t: datetime
    :param utc: 是否转化为utc
    :return: int
    """
    if utc:
        tup = t.utctimetuple()
    else:
        tup = t.timetuple()
    return int(time.mktime(tup))
