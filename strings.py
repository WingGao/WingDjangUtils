# coding=utf-8
import random
import string

__author__ = 'wing'


def id_generator(size):
    """生成随机字符串
    :param size: 大小:int
    :return:
    """
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(size))
