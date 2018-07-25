from urllib.parse import urljoin
import html.parser
import requests
import re

__author__ = 'wing'
html_parser = html.parser.HTMLParser()


def full_url(root, url):
    return html.unescape(urljoin(root, url))


def my_ip():
    r = requests.get('http://1212.ip138.com/ic.asp')
    ip = re.findall('\d+\.\d+\.\d+\.\d+', r.text)
    return ip[0]
