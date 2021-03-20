#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import unittest
import json
import random
from testcase.middleground.WMS.prepare.login import login
from testcase.middleground.WMS.common.Pash import Header_mkdir # 存放header值得配置文件
from testcase.middleground.WMS.common.Pash import Public_mkdir
from testcase.middleground.WMS.common.config import read_config
from testcase.middleground.WMS.common.Mysql import mp_label
from testcase.middleground.WMS.datas.warehouse_data import warehouse_data
from ddt import data, ddt
from testcase.middleground.WMS.common.Http import Request

# class student(unittest.TestCase):
#     def __init__(self,name,score):
#             self.name = self
#             self.score = self
#
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score <= 60:
#             return 'B'
#         else:
#             return 'C'


class Stu:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def run(self):
        print("{name} is running".format(name=self.name))

s =Stu('张三',18)
s.run()

class Stu:
    def __init__(self,name,age):
        print("在__init__的方法中",id(self))
        self.name = self
        self.age = age

    def run(self):
        print("在__init__的方法中",id(self))
        print("{name} is running".format(name=self.name))

s = Stu('小明',18)
print('s的内存地址',id(s))
s.run()

class Stu:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print("{name}今年{age}".format(name=self.name,age=self.age))

    def run(self):
        print("{name} is running".format(name=self.name))

    def print(self):
        print('ok')

s = Stu('小刚',18)
s.info()

print(s.name)
s.age = 20
s.info()

if __name__ == '__main__':
   unittest.main()

