# coding=utf-8
from functools import wraps
from django.http import HttpResponse, HttpResponseNotAllowed
import json
from django.utils.decorators import available_attrs
from ..strings import get_int
import os


class JSONResponse(HttpResponse):
    def __init__(self, obj, sort_keys=False):
        if isinstance(obj, dict) or isinstance(obj, list):
            _json_str = json.dumps(obj, sort_keys=sort_keys)
        else:
            _json_str = obj
        super(JSONResponse, self).__init__(_json_str, content_type="application/json")


class FileResponse(HttpResponse):
    TYPE = {
        'txt': 'text/plain',
        'csv': 'text/csv',
    }

    def __init__(self, filename, data):
        name, ext = filename.rsplit('.')
        content_type = FileResponse.TYPE[ext]
        super(FileResponse, self).__init__(data, content_type=content_type)
        self['Content-Disposition'] = 'attachment;filename="%s"' % filename


class Params(object):
    PARAMS_TYPE_STR = "string"
    PARAMS_TYPE_INT = "int"

    def __init__(self, pdict):
        self.pdict = pdict

    def get_param(self, name, defv=None, deft=PARAMS_TYPE_STR):
        """获取对应参数
        :param name:
        :param defv:
        :param deft:
        :return:
        """
        v = self.pdict.get(name, defv)
        if deft == Params.PARAMS_TYPE_STR:
            v = v.strip()
        elif deft == Params.PARAMS_TYPE_INT:
            v = get_int(v, defv)

        if v is None:
            return defv
        else:
            return v

    def get_param_int(self, name, defv=None):
        return self.get_param(name, defv=defv, deft=Params.PARAMS_TYPE_INT)


def get_ip(request, all_ips=False):
    meta_keys = ['HTTP_X_FORWARDED_FOR', 'X_FORWARDED_FOR']
    for key in meta_keys:
        value = request.META.get(key, request.META.get(key.replace('_', '-'), '')).strip()
        if value:
            ips = [ip.strip().lower() for ip in value.split(',')]
            count = len(ips)
            if count > 1:
                if all_ips:
                    return ips
                return ips[0]
    return request.META.get('REMOTE_ADDR')


# 装饰器
def require_IP(ip):
    def _require_IP(func):
        @wraps(func, assigned=available_attrs(func))
        def inner(request, *args, **kwargs):
            if get_ip(request) in [ip, '127.0.0.1']:
                return func(request, *args, **kwargs)
            else:
                return HttpResponseNotAllowed(['IP'])

        return inner

    return _require_IP


def clear_request_meta(request):
    """获得清爽的request.META
    :param request:
    :return:
    """
    d = {}
    for k, v in request.META.items():
        if k not in os.environ and not k.startswith('wsgi.'):
            d[k] = v
    return d
