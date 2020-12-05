#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/11/12 16:13
# @Author: wei.zhang
# @File : asset.py
# @Software: PyCharm

import json
from interfaces.middleground.AssetAction import assetAction
from testcase.middleground.sql.asstMpSQL import assetSQL
from utils import runlevel, dataDispose, timestamp
from ddt import data, ddt
from faker import Faker
import unittest
import random


@ddt
class asset(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = assetAction()
        self.api.set_user(mobile=15388126082)
        self.db = assetSQL()
        self.faker = Faker('zh_CN')

    def test_admin_asset_init(self):
        """
        初始化资产
        :return:
        """
        codeinfo = self.db.query_code_base_all_code(productid=3)
        rfid = self.db.query_code_base_all_rfidcode(productid=3)
        codes = json.dumps([dict(i, **k) for i, k in zip(codeinfo, rfid)])
        warehouseId = 9
        supplierId = 6
        resp = self.api._admin_asset_init(codes_=codes, warehouseId_=warehouseId, supplierId_=supplierId)
        self.assertEqual(resp.get('status'), 'OK')
