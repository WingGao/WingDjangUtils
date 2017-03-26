import unittest
import requests
from .http import auto_encoding


class HTTPTest(unittest.TestCase):
    def test_auto_encoding(self):
        rep = requests.Response()
        rep._content = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312">
<meta name="keywords" content="" />
<meta name="description" content="" />'''
        auto_encoding(rep)
        print rep.encoding

        rep._content = '''
        <!DOCTYPE html>

<html lang="en" ng-app="myApp">
<head>
    <meta charset="utf-8">
    <title>PyPersonalCollection</title>
        '''
        auto_encoding(rep)
        print rep.encoding
