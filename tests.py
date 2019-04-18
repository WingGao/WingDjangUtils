__author__ = 'wing'
from . import http
import os
import unittest
from . import qrcode
from . import web

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class MyTest(unittest.TestCase):
    def test_ip(self):
        print((web.my_ip()))

    def test_download(self):
        print(http.download('http://omgmkt.qq.com/got/xz', os.path.join(BASE_DIR, 'temp', 't1', 't2', 'a'),
                            create_dirs=True))

    def test_qrcode(self):
        url = qrcode.build_qrcode("https://www.a.com/1/2/3?a=b&c=d")
        print(url)
