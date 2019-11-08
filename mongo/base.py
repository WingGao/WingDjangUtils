# coding=utf-8
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.codec_options import CodecOptions
from django.conf import settings
import copy


def connect():
    pass


collection_options = options = CodecOptions(tz_aware=True)


def get_db():
    client = MongoClient(settings.MONGODB['HOST'], settings.MONGODB['PORT'], connect=False, maxPoolSize=100,
                         username=settings.MONGODB['USER'], password=settings.MONGODB['PASS'])
    return client[settings.MONGODB['NAME']]


class ObjectBase(object):
    def __init__(self, collection_name, **kwargs):
        self._collection_name = collection_name
        self._collection = get_db().get_collection(collection_name, collection_options)
        self._id = None
        # 设置自动参数
        for k, v in list(kwargs.items()):
            if hasattr(self, k):
                setattr(self, k, v)

    def load_object(self, obj, include_id=False):
        for i in list(obj.keys()):
            if not i.startswith('_'):
                setattr(self, i, obj[i])
        if include_id:
            self._id = obj.get('_id')

    @property
    def collection_name(self):
        return self._collection_name

    def get_collection_inst(self):
        return self._collection

    @property
    def id(self):
        if self._id is None:
            return None
        else:
            return str(self._id)

    def _pk_name(self):
        """自定义主键
        :return: (keyname ,keytype)
        """
        return '_id', ObjectId

    def _to_pk(self, key_str):
        """提供一个可以将str转换为pk的函数
        :param key_str:
        :return:
        """
        pktype = self._pk_name()[1]
        if isinstance(pktype, list):
            for i in pktype:
                if isinstance(key_str, i):
                    return key_str
            pktype = pktype[0]

        if not isinstance(key_str, pktype):
            return pktype(key_str)

        return key_str

    def __pk(self):
        """返回主键，默认_id
        :return:
        """
        pk = self._pk_name()[0]
        return {pk: getattr(self, pk)}

    def _gen_id(self):
        if self._id is None:
            self._id = ObjectId()
            self._on_create()
        return self._id

    def _on_create(self):
        """save之前，如果是新记录，则会被调用
        :return:
        """
        pass

    def get_dict(self, with_id=False):
        # 需要拷贝，否则会被pop掉，无法二次使用
        x = copy.copy(self.__dict__)
        for i in list(x.keys()):
            if i == '_id' and with_id:
                x['_id'] = str(x['_id'])
            elif i.startswith('_'):
                x.pop(i)
            elif isinstance(x[i], list) and len(x[i]) > 0:
                for ji, j in enumerate(x[i]):
                    if hasattr(j, '__dict__'):
                        x[i][ji] = j.__dict__
        return x

    def load_by_pk(self, pk=None):
        """通过pk来加载一个item
        :param pk:
        :return: False未找到
        """
        pkname = self._pk_name()[0]
        if pk is None:
            pass
        else:
            setattr(self, pkname, pk)

        return self.load_by(self.__pk())

    def load_by(self, args):
        try:
            c = self._collection.find_one(args)
        except Exception as e:
            return False

        if c is None:
            return False

        self.load_object(c, include_id=True)
        return True

    def find_one(self, where):
        obj = self._collection.find_one(where)
        if obj is None:
            return None
        item = self.__class__()
        item.load_object(obj, include_id=True)
        return item

    def save(self, catch=True):
        self._gen_id()
        # 每个都有一个_id 所以我们包含进去
        try:
            pk = self.__pk()
            updic = self.get_dict()
            # if '_id' not in pk:
            #     updic['_id'] = self._id
            res = self._collection.update_one(pk, {'$set': updic}, upsert=True)
            if res.upserted_id is not None:
                self._id = res.upserted_id
            return True
        except Exception as e:
            if catch:
                return e
            else:
                raise e

    def delete(self):
        pk = self.__pk()
        return self._collection.remove(pk, multi=False)
