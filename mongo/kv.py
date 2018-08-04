from .base import ObjectBase


class KVItem(ObjectBase):
    def __init__(self, **kwargs):
        self.key = None
        self.value = None
        super().__init__('kv', **kwargs)


def kv_index():
    KVItem().get_collection_inst().create_index('key', unique=True)
