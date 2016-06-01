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

    return ''.join(random.SystemRandom().choice(r) for _ in range(size))
