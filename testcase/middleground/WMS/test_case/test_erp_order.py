#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/1/7 13:38
# @Author: wei.zhang
# @File : test_erp_order.py
# @Software: PyCharm
from interfaces.middleground.Wms_apiAction import wms_apiAction
from testcase.middleground.sql.shopMP import mpShopSql
from ddt import data, ddt
from utils import runlevel
from faker import Faker
import unittest

"""
中台接口测试- ERP未结清订单
"""


@ddt
class ErpUnclearedOrder(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = wms_apiAction()
        self.api.set_user(mobile=15388126082, account_type='web-mp')
        self.db = mpShopSql()
        self.faker = Faker('zh_CN')

    def tearDown(self) -> None: pass

    @unittest.skipIf(runlevel(1), '采购列表')
    def test_admin_erp_uncleared_order_purchase_list(self):
        """
        admin-ERP未结清	采购列表
        :return:
        """
        companyCode = 'tongren'
        resp = self.api._admin_erp_uncleared_order_purchase_list(companyCode_=companyCode)
        self.assertEqual(resp.get('status'), 'OK')
