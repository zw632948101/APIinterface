#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/1/6 17:54
# @Author: wei.zhang
# @File : test_company.py
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
class Company(unittest.TestCase):
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

    @unittest.skipIf(runlevel(1), "admin-公司/运营主体 列表")
    def test_admin_company_list(self):
        """
        admin-公司/运营主体 列表
        :return:
        """
        resp = self.api._admin_company_list()
        self.assertEqual(resp.get('status'), 'OK')
        content = resp.get('content')
        subjectinfo = self.db.query_wms_subject_info()
        for ct, sj in zip(content, subjectinfo):
            self.assertDictEqual(ct, sj)
