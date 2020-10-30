import re
import random
import string
import faker

def changData(data,cls):
    #替换@号内的参数，随机生成入参值，避免重复数据被后端限制
    if re.search("@(.+?)@", data):
        item = re.search("@(.+?)@", data)
        old = item.group()
        key1 = item.group(1)
        if isinstance(key1, float):
            new = random.uniform(1, 100)
        elif isinstance(key1, int) and key1 > 0:
            new = random.randint(1, 9999)
        elif isinstance(key1, int) and key1 < 0:
            new = random.randint(-9999,-1)
        elif key1 == "%":
            new = random.choice("~!@#$%^&*(){}:?></.,\=-`;")
        elif isinstance(key1, str) and len(key1) == 1:
            new = random.choice(string.ascii_letters)
        elif isinstance(key1, str) and len(key1) != 1:
            fa = faker.Faker("zh_CN")
            new = fa.pystr(min_chars=len(key1), max_chars=len(key1))
        data = re.sub(old, str(new), data)
    #使用正则，替换#号内的参数值，替换为类属性
    while re.search("#(.+?)#", data):
        item = re.search("#(.+?)#", data)
        old = item.group()
        key2 = item.group(1)
        new = getattr(cls, key2)
        data = re.sub(old, str(new), data)
    return data

