#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/11/3 15:49
# @Author: wei.zhang
# @File : shop.py
# @Software: PyCharm
from utils.log import log
import time
import random
import warnings
from interfaces.wxshop.MallAction import MallAction
#from testcase.middleground.sql.brandMP import mp_label as
from testcase.shop.sql.webMP import mp_label
from testcase.shop.caseData.applet_data import applet_api,submit_order
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest
import requests
import json
import random
class shop(unittest.TestCase):
    def setUp(self):
        """
        测试前数据准备
        :return:
        """
        self.api = MallAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')

    def test_api_shop_get(self):
        res = self.api._api_shop_get(shopId_=1)
        # self.assertEqual('OK',res.get('status'))
        print(res.get('content'))

    # def test_api_shop_list(self):
    #     pass
    #
    # def test_api_shop_list_by_ids(self):
    #     pass

if __name__ == '__main__':
    unittest.main()
