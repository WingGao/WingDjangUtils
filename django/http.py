# coding=utf-8
from django.http import HttpResponse
import json
from ..strings import get_int


class JSONResponse(HttpResponse):
    def __init__(self, obj):
        if isinstance(obj, dict):
            _json_str = json.dumps(obj)
        else:
            _json_str = obj
        super(JSONResponse, self).__init__(_json_str, content_type="application/json")


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
