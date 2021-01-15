#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/1/13 16:56
# @Author: wei.zhang
# @File : test_transfer.py
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
中台接口测试- 调拨单
"""


@ddt
class TransferOrder(unittest.TestCase):
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

    def test_admin_transfer_apply_add(self):
        """
        admin-调拨申请  新建调拨申请
        :return:
        """
        details = [{"productCode": "T0103010007", "planQuantity": 100},
                   {"productCode": "T0102020008", "planQuantity": 100},
                   {"productCode": "T0101020019", "planQuantity": 100}]
        relevanceCode = 'GYLTOCS0001'
        source = 'GYL'
        type_ = 'DB06'
        fromOrg = 100002
        fromWarehouse = 30015
        toOrg = 100002
        toWarehouse = 40010
        possessor = 660
        arriveTime = 1610759833954
        remark = self.faker.text(300)
        itemList = json.dumps(details)
        resp = self.api._admin_transfer_apply_add(relevanceCode_=relevanceCode, source_=source,
                                                  type_=type_, fromOrg_=fromOrg,
                                                  fromWarehouse_=fromWarehouse, toOrg_=toOrg,
                                                  toWarehouse_=toWarehouse, possessor_=possessor,
                                                  arriveTime_=arriveTime, remark_=remark,
                                                  itemList_=itemList)
        self.assertEqual(resp.get('status'), 'OK')

    def test_admin_transfer_apply_confirm(self):
        """
        admin-调拨申请  确认调拨申请
        :return:
        """
        orderCode = 'DB202101140034'
        transferMethod = 2
        fromOrg = 100002
        fromWarehouse = 30015
        resp = self.api._admin_transfer_apply_confirm(orderCode_=orderCode,
                                                      transferMethod_=transferMethod,
                                                      fromOrg_=fromOrg,
                                                      fromWarehouse_=fromWarehouse)
        self.assertEqual(resp.get('status'), 'OK')
