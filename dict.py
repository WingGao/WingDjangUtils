# coding=utf-8
def getitem(dictObj, key, default_value=None):
    """
    获取字典的对应value
    :param dictObj:
    :param key:
    :param default_value:
    :return:
    """
    try:
        return dictObj.get(key, default_value)
    except:
        return default_value
