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
        authCode = '283685125040405890'  # 付款码id
        bodyId = '0000001'  # 渠道id
        disregardaAmount = 1  # 优惠后金额
        due = 0  # 优惠金额
        mchCreateIp = '172.12.13.15'  # 商户地址
        mchNo = '2088041261907815'  # 商户号
        outOrderNo = '25358884655469'  # 外部订单号
        regardaAmount = 0  #
        source = 'POS'  # 来源渠道
        subject = '椴树蜜'  # 商品名称
        totalAmount = 1  # 实收金额
        resp = self.api._open_api_trade_tradePay(authCode_=authCode, bodyId_=bodyId,
                                                 disregardaAmount_=disregardaAmount, due_=due,
                                                 mchCreateIp_=mchCreateIp, mchNo_=mchNo,
                                                 outOrderNo_=outOrderNo,
                                                 regardaAmount_=regardaAmount,
                                                 source_=source, subject_=subject,
                                                 totalAmount_=totalAmount)
        self.assertEqual(resp.get('status'), 'OK')

    def test_open_api_trade_refund(self):
        """
        退款
        :return:
        """
        bodyId = '0000001'
        outOrderNo = '25358884655462'
        outRefundOrderNo = '4200000834202101155906249399'
        refundAmount = 1
        refundType = 'WX_PAY'
        source = 'POS'
        self.api._open_api_trade_refund(bodyId_=bodyId, outOrderNo_=outOrderNo,
                                        outRefundOrderNo_=outRefundOrderNo,
                                        refundAmount_=refundAmount, refundType_=refundType,
                                        source_=source)

    def test_open_api_trade_casshOrderPay(self):
        """
        现金交易
        :return:
        """
        input_ = {
            "bodyId": '0000001',
            "disregardaAmount": 1,
            "due": 0,
            "mchCreateIp": '172.12.13.15',
            "mchNo": "2088041261907815",
            "outOrderNo": "25358884655463",
            "regardaAmount": 0,
            "source": 'POS',
            "subject": "椴树蜜",
            "totalAmount": 1
        }
        resp = self.api._open_api_trade_cashOrderPay(input_=input_)
        self.assertEqual(resp.get('status'), 'OK')
