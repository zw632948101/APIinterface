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
        self.api.set_user(mobile=15388126082)
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

    def test_mobile_move_pda_pick_submit(self):
        """
        ADMIN-拣货单 PDA分拣任务提交
        :return:
        """
        productJson = [{'id': '14', 'productCode': 'T0101020019', 'actualQuantity': 100},
                       {'id': '15', 'productCode': 'T0102020008', 'actualQuantity': 100},
                       {'id': '16', 'productCode': 'T0103010007', 'actualQuantity': 100}]
        productJson = json.dumps(productJson)
        invoiceCode = 'CK202101140041'
        code = 'JH202101140040'
        resp = self.api._mobile_move_pda_pick_submit(code_=code, invoiceCode_=invoiceCode,
                                                    productJson_=productJson)
        self.assertEqual(resp.get('status'), 'OK')

    def test_admin_pick_doc_count(self):
        """
        ADMIN-拣货单 统计
        :return:
        """
        resp = self.api._admin_pick_doc_count()
        self.assertEqual(resp.get('status'), 'OK')
        dbinfo = self.db.query_move_doc_count()
        self.assertDictEqual(resp.get('content'), dbinfo[0])

    def test_admin_pick_doc_detail(self):
        """
        ADMIN-拣货单	通知详情
        :return:
        """
        dbinfo = random.choice(self.db.query_pick_doc_info())
        orderCode = dbinfo.get('code')
        resp = self.api._admin_pick_doc_detail(orderCode_=orderCode)
        self.assertEqual(resp.get('status'), 'OK')
        self.assertDictEqual(conversion.del_dict_key(['creatorName', 'creatorPhone'], dbinfo),
                             resp.get('content'))

    def test_admin_pick_doc_page_list(self):
        """
        ADMIN-拣货单	通知单分页列表
        :return:
        """
        pn = None
        ps = 20
        orderCode = None
        status = 1
        type_ = 'CK05'
        warehouseCode = None
        operatorId = 660
        resp = self.api._admin_pick_doc_page_list(pn_=pn, ps_=ps, orderCode_=orderCode,
                                                  status_=status, type_=type_,
                                                  warehouseCode_=warehouseCode,
                                                  operatorId_=operatorId)
        self.assertEqual(resp.get('status'), 'OK')
        dbinfo = self.db.query_pick_doc_info(pn=pn, ps=ps, orderCode=orderCode, status=status,
                                             type_=type_, warehouseCode=warehouseCode,
                                             operatorId=operatorId)
        dbinfo = conversion.del_dict_value_null(dbinfo)
        if resp.get('content').get('datas'):
            for z, x in zip(resp['content']['datas'], dbinfo):
                self.assertDictEqual(z, x)

    def test_admin_pick_product_page_list(self):
        """
        ADMIN-拣货单 商品清单分页列表
        :return:
        """
        pn = None
        ps = 20
        orderCode = 'JH20210111000106'
        resp = self.api._admin_pick_product_page_list(pn_=pn, ps_=ps, orderCode_=orderCode)
        self.assertEqual(resp.get('status'), 'OK')
