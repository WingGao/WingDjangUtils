# coding=utf-8
__author__ = 'wing'
from django.utils import timezone
import datetime


def get_local_day_min(dt):
    if timezone.is_aware(dt):
        tm = timezone.make_naive(dt)
    else:
        tm = dt

    tm = datetime.datetime.combine(tm, datetime.time.min)
    # 计算后的tm没有tzinfo
    tm = timezone.make_aware(tm)
    tm = timezone.make_naive(tm, timezone.utc)
    return tm
