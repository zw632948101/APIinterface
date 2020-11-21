#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/11/12 11:05
# @Author: wei.zhang
# @File : mobileWarehouse.py
# @Software: PyCharm
"""
移动端-仓库模块
"""
import json
from interfaces.middleground.AssetAction import assetAction
from testcase.middleground.sql.asstMpSQL import mobileWarehouseSQL
from utils import runlevel, dataDispose, timestamp
from ddt import data, ddt
from faker import Faker
import unittest
import random


@ddt
class apply(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = assetAction()
        self.api.set_user(mobile=15388126082)
        self.db = mobileWarehouseSQL()
        self.faker = Faker('zh_CN')

    def test_mobile_warehouse_init(self):
        """
        mobile-仓库管理-初始化入库
        :return:
        """
        dbinfo = self.db.query_init_warehouse_code()
        codes = json.dumps([dbinfo[0]])
        warehouseId = 4
        supplierId = 2
        resp = self.api._mobile_warehouse_init(codes_=codes, warehouseId_=warehouseId, supplierId_=supplierId)
        self.assertEqual(resp.get('status'), 'OK')
