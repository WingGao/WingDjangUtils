from django.http import HttpResponse
import json


class JSONResponse(HttpResponse):
    def __init__(self, obj):
        super(JSONResponse, self).__init__(json.dumps(obj), content_type="application/json")
