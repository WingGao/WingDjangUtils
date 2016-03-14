from urlparse import urljoin
import HTMLParser

__author__ = 'wing'
html_parser = HTMLParser.HTMLParser()


def full_url(root, url):
    return html_parser.unescape(urljoin(root, url))
