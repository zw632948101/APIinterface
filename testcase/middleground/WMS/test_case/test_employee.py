#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/1/7 12:00
# @Author: wei.zhang
# @File : test_employee.py
# @Software: PyCharm

from interfaces.middleground.Wms_apiAction import wms_apiAction
from testcase.middleground.sql.shopMP import mpShopSql
from ddt import data, ddt
from utils import runlevel
from faker import Faker
import unittest

"""
中台接口测试- 公司/运营主体
"""


@ddt
class Employee(unittest.TestCase):
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

    def test_admin_employee_list(self):
        """
        admin-员工-列表
        :return:
        """
        resp = self.api._admin_employee_list()
        self.assertEqual(resp.get('status'), 'OK')
