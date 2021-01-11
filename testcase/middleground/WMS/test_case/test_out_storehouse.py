#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/1/7 14:21
# @Author: wei.zhang
# @File : test_out_storehouse.py
# @Software: PyCharm
import json
import random

from interfaces.middleground.Wms_apiAction import wms_apiAction
from testcase.middleground.sql.mpWmsSql import OutStorehouseSql
from ddt import data, ddt
from utils import runlevel, conversion
from faker import Faker
import unittest

"""
中台接口测试- 出库单 出库通知单
"""


@ddt
class OutStorehouse(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = wms_apiAction()
        self.api.set_user(mobile=15388126082, account_type='web-mp')
        self.db = OutStorehouseSql()
        self.faker = Faker('zh_CN')

    def tearDown(self) -> None:
        pass

    def test_admin_invoice_count(self):
        """
        出库单-统计
        :return:
        """
        resp = self.api._admin_invoice_count()
        self.assertEqual(resp.get('status'), 'OK')
        count_info = self.db.query_invoice_count()
        self.assertDictEqual(resp.get('content'), count_info[0])

    def test_admin_invoice_notice_count(self):
        """
        出库通知单	统计
        :return:
        """
        resp = self.api._admin_invoice_notice_count()
        self.assertEqual(resp.get('status'), 'OK')
        count_info = self.db.query_invoice_count()
        self.assertDictEqual(resp.get('content'), count_info[0])

    def test_admin_invoice_notice_detail(self):
        """
        出库通知单	通知详情
        :return:
        """
        dbinfo = random.choice(self.db.query_admin_invoice_notice_info())
        orderCode = dbinfo.get('code')
        resp = self.api._admin_invoice_notice_detail(orderCode_=orderCode)
        self.assertEqual(resp.get('status'), 'OK')
        content = resp.get('content')
        self.assertDictEqual(content, dbinfo)

    def test_admin_invoice_notice_page_list(self):
        """
        出库通知单	通知单分页列表
        :return:
        """
        pn_ = 2
        ps_ = 10
        orderCode_ = None
        relevanceCode_ = None
        status_ = 0
        type_ = None
        warehouseCode_ = None
        operatorId_ = None
        resp = self.api._admin_invoice_notice_page_list(pn_=pn_, ps_=ps_, orderCode_=orderCode_,
                                                        relevanceCode_=relevanceCode_,
                                                        status_=status_, type_=type_,
                                                        warehouseCode_=warehouseCode_,
                                                        operatorId_=operatorId_)
        self.assertEqual(resp.get('status'), 'OK')
        dbinfo = self.db.query_admin_invoice_notice_info(pn=pn_, ps=ps_, code=orderCode_,
                                                         relevanceCode=relevanceCode_,
                                                         status=status_, type_=type_,
                                                         warehouseCode=warehouseCode_,
                                                         operatorId=operatorId_)
        datas = resp.get('content').get('datas')
        for r, d in zip(dbinfo, datas):
            self.assertDictEqual(r, d)

    def test_admin_invoice_notice_product_page_list(self):
        """
        出库通知单	商品清单分页列表
        :return:
        """
        pn_ = None
        ps_ = 20
        orderCode = 'CT20201231000017'
        resp = self.api._admin_invoice_notice_product_page_list(pn_=pn_, ps_=ps_,
                                                                orderCode_=orderCode)
        self.assertEqual(resp.get('status'), "OK")
        dbinfo = self.db.query_order_code_prdouct_info(order_code=orderCode)
        dbinfo = conversion.del_dict_value_null(dbinfo)
        datas = resp.get('content').get('datas')
        for i, j in zip(dbinfo, datas):
            self.assertDictEqual(i, j)

    def test_admin_invoice_notice_confirm(self):
        """
        出库通知单	确认通知单
        :return:
        """
        orderCode = 'CT202012190001'
        resp = self.api._admin_invoice_notice_confirm(orderCode_=orderCode)
        self.assertEqual(resp.get('status'), 'OK')
        dbinfo = self.db.query_admin_invoice_notice_info(code=orderCode)
        self.assertEqual(dbinfo[0].get('statusName'), '已确认')

    def test_admin_invoice_notice_add(self):
        """
        出库通知单 - 新建出库通知单
        :return:
        """
        details = {'planQuantity': '99999999', 'productCode': 'T0101010012',
                   'sourceList': [{'productCode': 'T0101010012',
                                   'tracingCode': 'SKU0004', 'quantity': 99999999}]}
        itemList = json.dumps([details])
        possessor = self.api.user.user_id
        purchasingCompany = '001'
        relevanceCode = '20210105172928000006'
        remark = self.faker.text(200)
        source = 'ZC'
        supplier = 'None'
        warehouseCode = 'None'
        type_ = 'CK01'
        resp = self.api._admin_invoice_notice_add(itemList_=itemList,
                                                  possessor_=possessor,
                                                  purchasingCompany_=purchasingCompany,
                                                  relevanceCode_=relevanceCode, remark_=remark,
                                                  source_=source, supplier_=supplier, type_=type_,
                                                  warehouseCode_=warehouseCode)
        self.assertEqual(resp.get('status'), 'OK')

    def test_admin_invoice_detail(self):
        """
        出库单	通知详情
        :return:
        """
        dbinfo = random.choice(self.db.query_admin_invoice_info())
        orderCode = dbinfo.get('code')
        # orderCode = None
        resp = self.api._admin_invoice_detail(orderCode_=orderCode)
        self.assertEqual(resp.get('status'), 'OK')
        content = resp.get('content')
        self.assertDictEqual(content, dbinfo)

    def test_admin_invoice_page_list(self):
        """
        出库单	通知单分页列表
        :return:
        """
        pn_ = 2
        ps_ = 10
        orderCode_ = None
        status_ = None
        type_ = None
        warehouseCode_ = None
        operatorId_ = None
        resp = self.api._admin_invoice_page_list(pn_=pn_, ps_=ps_, orderCode_=orderCode_,
                                                 status_=status_, type_=type_,
                                                 warehouseCode_=warehouseCode_,
                                                 operatorId_=operatorId_)
        self.assertEqual(resp.get('status'), 'OK')
        dbinfo = self.db.query_admin_invoice_info(pn=pn_, ps=ps_, code=orderCode_,
                                                  status=status_, type_=type_,
                                                  warehouseCode=warehouseCode_,
                                                  operatorId=operatorId_)
        dbinfo = conversion.del_dict_key('erpSyncStatus', dbinfo)
        datas = resp.get('content').get('datas')
        for r, d in zip(dbinfo, datas):
            self.assertDictEqual(r, d)

    def test_admin_invoice_sync_rep(self):
        """
        出库单 同步ERP
        :return:
        """
        dbinfo = random.choice(self.db.query_admin_invoice_info(status=0))
        code = dbinfo.get('code')
        resp = self.api._admin_invoice_sync_erp(code_=code)
        self.assertEqual(resp.get('status'), 'OK')
