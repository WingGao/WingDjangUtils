from .base import ObjectBase


class KVItem(ObjectBase):
    def __init__(self, **kwargs):
        self.key = None
        self.value = None
        super().__init__('kv', **kwargs)

    def _pk_name(self):
        return 'key', str

    @classmethod
    def exist(cls, key):
        return KVItem().find_one({'key': key})

    @classmethod
    def set(cls, key, value):
        return KVItem(key=key, value=value).save()


def kv_index():
    KVItem().get_collection_inst().create_index('key', unique=True)
