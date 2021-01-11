#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/1/9 16:38
# @Author: wei.zhang
# @File : test_picking_order.py
# @Software: PyCharm

import json
import random

from interfaces.middleground.Wms_apiAction import wms_apiAction
from testcase.middleground.sql.mpWmsSql import MpMoveSql
from ddt import data, ddt
from utils import runlevel, conversion
from faker import Faker
import unittest

"""
中台接口测试- 拣货单
"""


@ddt
class PickingOrder(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.maxDiff = None
        self.api = wms_apiAction()
        self.api.set_user(mobile=15388126082, account_type='web-mp')
        self.db = MpMoveSql()
        self.faker = Faker('zh_CN')

    def tearDown(self) -> None:
        pass

    def test_admin_move_pad_pick_list(self):
        """
        ADMIN-拣货单 PDA分拣任务列表
        :return:
        """
        resp = self.api._admin_move_pda_pick_list(status_=0)
        self.assertEqual(resp.get('status'), 'OK')
        dbinfo = conversion.del_dict_value_null(self.db.query_move_code())
        for z, x in zip(dbinfo, resp.get('content')):
            self.assertDictEqual(z, x)

    def test_admin_move_pda_pick_detail_list(self):
        """
        ADMIN-拣货单 PDA分拣任务列表
        :return:
        """
        movelist = random.choice(self.db.query_move_code())
        orderCode = movelist.get('code')
        resp = self.api._admin_move_pda_pick_detail_list(orderCode_=orderCode)
        self.assertEqual(resp.get('status'), 'OK')
        dbinfo = self.db.query_move_detail_list(orderCode=orderCode)
        for z, x in zip(dbinfo, resp.get('content')):
            self.assertDictEqual(z, x)

    def test_admin_move_pda_pick_submit(self):
        """
        ADMIN-拣货单 PDA分拣任务提交
        :return:
        """
        productJson = []
        invoiceCode = ''
        code = ''
        resp = self.api._admin_move
