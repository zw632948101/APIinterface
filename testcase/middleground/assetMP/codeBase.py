#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/11/7 18:01
# @Author: wei.zhang
# @File : codeBase.py
# @Software: PyCharm
import random

from utils.log import log
from interfaces.middleground.AssetAction import assetAction
from testcase.middleground.sql.asstMpSQL import codeBaseSQL
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest
import inspect


@ddt
class codeBase(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = assetAction()
        self.api.set_user(mobile=15388126072)
        self.db = codeBaseSQL()
        self.faker = Faker('zh_CN')

    def test_admin_code_base_add(self):
        """
        编码库-添加
        :return:
        """
        codeType = 2
        productId = 1
        number = 10
        supplierId = 1
        response = self.api._admin_code_base_add(codeType_=codeType, productId_=productId, number_=number, supplierId_=supplierId)
        self.assertEqual(response.get('status'), 'OK')

    def test_admin_code_base_page(self):
        """
        编码库-铭牌分页列表
        :return:
        """
        pn = None
        ps = None
        code = None
        suplierIds = None
        statuses = 10
        response = self.api._admin_code_base_page(pn_=pn, ps_=ps, code_=code, supplierIds_=suplierIds, statuses_=statuses)
        self.assertEqual(response.get('status'), 'OK')

    def test_admin_code_rfid_page(self):
        """
        编码库-分页列表
        :return:
        """
        pn = None
        ps = None
        code = None
        suplierIds = None
        statuses = 10
        response = self.api._admin_rfid_page(pn_=pn, ps_=ps, code_=code, supplierIds_=suplierIds, statuses_=statuses)
        self.assertEqual(response.get('status'), 'OK')