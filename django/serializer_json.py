"""
Serialize data to/from JSON
"""

# Avoid shadowing the standard library json module
from __future__ import absolute_import, unicode_literals

import datetime
import decimal
import json
import sys
import uuid

from django.core.serializers.base import DeserializationError
from django.core.serializers.python import (
    Deserializer as PythonDeserializer, Serializer as PythonSerializer,
)
from django.core.serializers.json import (
    Deserializer as pDeserializer, DjangoJSONEncoder, Serializer as pSerializer
)

__author__ = 'wing'


class Serializer(pSerializer):
    def end_object(self, obj):
        # self._current has the field data
        indent = self.options.get("indent")
        if not self.first:
            self.stream.write(",")
            if not indent:
                self.stream.write(" ")
        if indent:
            self.stream.write("\n")
        dobj = self.get_dump_object(obj)
        nobj = dobj['fields']
        nobj['id'] = dobj['pk']
        json.dump(nobj, self.stream,
                  cls=DjangoJSONEncoder, **self.json_kwargs)
        self._current = None


def Deserializer(stream_or_string, **options):
    # todo
    return pDeserializer(stream_or_string, **options)
