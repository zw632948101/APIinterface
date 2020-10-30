"""
! /usr/bin/env python3
-*- coding: UTF-8 -*-
@Time:2020/10/29 9:30
@Author: he.chao
@File : brandManage.py
@Software: PyCharm
@modular:品牌管理
"""
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.goodsMP import mp_label
from utils import runlevel
from ddt import data, ddt
from faker import Faker
import unittest
import random
import os
from utils.excelRead import excelRead
from utils.changData import changData
from jsonpath import jsonpath

filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
excelpath = os.path.join(os.path.join(filepath, "caseData"), "caseData_sku.xlsx")  # 获取excel的测试用例数据文件路径
skuAdd_data = excelRead(excelpath, "skuAdd")
skuPageList_data = excelRead(excelpath, "skuPageList")
skuUpdate_data = excelRead(excelpath, "skuUpdate")


@ddt
class TestAttrManage(unittest.TestCase):
    def setUp(self):
        """
        测试前数据准备
        :return:
        """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')
    def test_(self):
        pass

    def test_(self):
        pass

    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()