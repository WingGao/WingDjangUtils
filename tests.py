__author__ = 'wing'
from . import http
import os
import unittest
from . import web

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class MyTest(unittest.TestCase):
    def test_ip(self):
        print((web.my_ip()))

    def test_download(self):
        print(http.download('http://omgmkt.qq.com/got/xz', os.path.join(BASE_DIR, 'temp', 't1', 't2', 'a'),
                            create_dirs=True))
