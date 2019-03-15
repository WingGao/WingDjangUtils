# coding=utf-8
import urllib

import requests
import re


def build_qrcode(url):
    """
    生产二维码
    Args:
        url (str):

    Returns:

    """
    u = url.split('://')[1]
    r = requests.get('https://cli.im/api/qrcode/code?text=//%s&mhid=skvHDl7tm50hMHcoK9JdPK8' % urllib.quote(u))
    qru = re.findall(r'qrcode_plugins_img ="(.*?)"', r.text)[0]
    return qru
