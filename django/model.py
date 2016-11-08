import copy
from django.db import models
from django.core import serializers
from django.core.exceptions import ValidationError
from django.utils import timezone

WING_JSON_FORMAT = 'wing_json'
serializers.register_serializer(WING_JSON_FORMAT, __package__ + '.serializer_json')


def create_model_from_request(mod, request):
    if request.method == 'GET':
        data = request.GET
    elif request.method == 'POST':
        data = request.POST
    else:
        raise Exception('unsupported method')

    return create_model_from_dict(mod, data)


ESCAPE_KEYS = ['id']


def create_model_from_dict(mod, dicta):
    m = mod()
    for k, v in dicta.items():
        if k in ESCAPE_KEYS:
            continue

        if hasattr(m, k):
            try:
                matt = getattr(m, k)
                if isinstance(matt, models.IntegerField) or isinstance(matt, models.SmallIntegerField) or \
                        isinstance(matt, int):
                    nv = int(v)
                else:
                    nv = v
                setattr(m, k, nv)
            except:
                pass

    return m


def is_clean(mod, exclude=None):
    try:
        mod.clean_fields(exclude)
        return True
    except ValidationError, e:
        return False


def to_json(objs):
    if isinstance(objs, models.Model):
        return serializers.serialize(WING_JSON_FORMAT, [objs])[1:-1]
    return serializers.serialize(WING_JSON_FORMAT, objs)


def auto_now(obj, field):
    if getattr(obj, field) is None:
        setattr(obj, field, timezone.now())
