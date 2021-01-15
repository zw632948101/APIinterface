#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/1/14 18:55
# @Author: wei.zhang
# @File : test_trade.py
# @Software: PyCharm

from interfaces.middleground.PayAction import payAction
from testcase.middleground.sql.payMpSql import TradeSql
from ddt import data, ddt
from utils import runlevel
from faker import Faker
import unittest

"""
支付中台 - 当面付
"""


@ddt
class TradeTest(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = payAction()
        self.api.set_user(mobile=15388126082, account_type='web-mp')
        self.db = TradeSql()
        self.faker = Faker('zh_CN')

    def test_open_api_trade_tradePay(self):
        """
        当面付 - 付款码支付
        :return:
        """
        authCode = '134799496115354842'
        bodyId = '0000001'
        disregardaAmount = 10
        due = 0
        mchCreateIp = '172.12.13.15'
        mchNo = '1351'
        outOrderNo = '15358884655464'
        regardaAmount = 0
        source = 'OMS'
        subject = '椴树蜜'
        totalAmount = 10
        resp = self.api._open_api_trade_tradePay(authCode_=authCode, bodyId_=bodyId,
                                                 disregardaAmount_=disregardaAmount, due_=due,
                                                 mchCreateIp_=mchCreateIp, mchNo_=mchNo,
                                                 outOrderNo_=outOrderNo,
                                                 regardaAmount_=regardaAmount,
                                                 source_=source, subject_=subject,
                                                 totalAmount_=totalAmount)
        self.assertEqual(resp.get('OK'), 'OK')
