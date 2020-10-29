import re


def changData(data, cls):
    """
    使用正则，替换#号内的参数值，替换为类属性
    """
    while re.search("#(.+?)#", data):
        item = re.search("#(.+?)#", data)
        old = item.group()
        key = item.group(1)
        new = getattr(cls, key)
        data = re.sub(old, str(new), data)
    return data
