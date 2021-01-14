#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/1/14 14:01
# @Author: wei.zhang
# @File : test_pda_receipt.py
# @Software: PyCharm

import json
import random

from interfaces.middleground.Wms_apiAction import wms_apiAction
from testcase.middleground.sql.mpWmsSql import ReeciptProduct
from ddt import data, ddt
from utils import runlevel, conversion
from faker import Faker
import unittest

"""
中台接口测试- 入库单
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
        self.api.set_user(mobile=15388126082)
        self.db = ReeciptProduct()
        self.faker = Faker('zh_CN')

    def test_mobile_pdareceopt_list(self):
        """
        admin-PDA入库单 入库单-列表
        :return:
        """
        pn = None
        ps = None
        status = 0
        type_ = None
        shopCode = None
        resp = self.api._mobile_pda_receipt_list(pn_=pn, ps_=ps, status_=status, type_=type_,
                                                 shopCode_=shopCode)
        self.assertEqual(resp.get('status'), 'OK')

    def test_mobile_pda_receipt_product_list(self):
        """
        admin-PDA入库单 入库商品清单-列表
        :return:
        """
        code = 'RK202101140032'
        resp = self.api._mobile_pda_receipt_product_list(code_=code)
        self.assertEqual(resp.get('status'), 'OK')

    def test_mobile_pda_receipt_product_submit(self):
        """
        admin-PDA入库单 提交入库
        :return:
        """
        code = 'RK202101140032'
        dbifno = self.db.query_pda_receipt_product_list(ordercode=code)
        productInfo = [{"actualQuantity": 10000, "productCode": "T0101020019"},
                       {"actualQuantity": 10000, "productCode": "T0102020008"},
                       {"actualQuantity": 10000, "productCode": "T0103010007"}]
        productInfo = json.dumps(productInfo)
        qualityResult = None
        receiptQualityInfo = None
        resp = self.api._mobile_receipt_pda_product_submit(code_=code, productInfo_=productInfo,
                                                           qualityResult_=qualityResult,
                                                           receiptQualityInfo_=receiptQualityInfo)
        self.assertEqual(resp.get('status'), 'OK')
