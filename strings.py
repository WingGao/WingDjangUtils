# coding=utf-8
import random
import string

__author__ = 'wing'


def id_generator(size, ascii=True, digits=True):
    """生成随机字符串
    :param size: 大小:int
    :return:
    """
    r = ''
    if ascii:
        r += string.uppercase
    if digits:
        r += string.digits

    return ''.join(random.SystemRandom().choice(r) for _ in list(range(size)))


def get_int(obj, defval=0):
    try:
        return int(obj)
    except:
        return defval


def startswith(o, s):
    r = o
    if isinstance(o, str):
        r = o.encode('utf8')
    return r.startswith(s)


def is_empty(s):
    """
    判断是否为None或者空字符串，空白也算0
    :param str s:
    :return bool:
    """
    return s is None or len(s.strip()) == 0
