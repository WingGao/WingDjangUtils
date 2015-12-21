__author__ = 'wing'
import http
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def test_download():
    print http.download('http://omgmkt.qq.com/got/xz', os.path.join(BASE_DIR, 'temp', 't1', 't2', 'a'), create_dirs=True)


if __name__ == '__main__':
    test_download()
