#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/9/21 11:21 
# @Author : wei.zhang
# @File : purchaseOrder.py
# @Software: PyCharm

import unittest
from interfaces.flowerChaser.TradeAction import TradeAction
from testcase.flowerChaser.sql.Bee import VisitRecordSql
from utils.fake.FakeLocation import FakeLocation
from testcase.flowerChaser.sql.Trade import ConfigProductSql
from faker import Faker
from utils.dataConversion.dataConversion import DataConversion
from utils.Timestamp.TimestampTransform import TimestampTransform as tt
import random
import json


class PurchaseOrder(unittest.TestCase, ConfigProductSql, FakeLocation, DataConversion):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    trad = TradeAction()
    pr_db = ConfigProductSql()
    vr = VisitRecordSql()
    fl = FakeLocation()
    fake = Faker(locale="zh_CN")
    trad.set_user('19982917912')

    def test_admin_purchase_order_page_list(self):
        """
        运营后台-收购单-订单-分页列表 V2.6
        """
        response = self.trad._admin_purchase_order_page_list(status_=10)
        self.assertEqual("OK", response.get("status"))

    def test_purchase_order_check_price(self):
        """
        运营后台-收购单-确认收购价格 V2.6
        """
        response = self.trad._admin_purchase_order_page_list(status_=10)
        self.assertEqual("OK", response.get("status"))
        datas = random.choice(response.get('content').get('test_case'))
        orderNo = datas.get('orderNo')
        orderNo = '2009211820022744000702'
        response = self.trad._admin_purchase_order_product_info(orderNo_=orderNo)
        self.assertEqual("OK", response.get("status"))
        products_list = response.get('content').get('products')
        for product in products_list:
            productId = product.get('productId')
            price = product.get('price')
            grade = product.get('grade')

            examineStatus = 1
            examineRemark = '接口测试审核不通过'
            response = self.trad._admin_purchase_order_check_price(productId_=productId, price_=price, grade_=grade,
                                                                   examineStatus_=examineStatus,
                                                                   examineRemark_=examineRemark)
            self.assertEqual("OK", response.get("status"))

        response = self.trad._admin_purchase_order_confirm_price(orderNo_=orderNo, contractNo_='2009211615365204000408',
                                                                 isDeduction_=1,
                                                                 isQuality_=0)
        self.assertEqual("OK", response.get("status"))

    def test_purchase_order_check_info(self):
        """
        运营后台-收购单-确认收购价格-展示信息 V2.6
        """
        orderNo = '2009211820022744000702'
        response = self.trad._admin_purchase_order_confirm_info(orderNo_=orderNo)
        self.assertEqual("OK", response.get("status"))

    def test_admin_pay_apply_add(self):
        """
        运营后台-打款申请单-新建打款申请单 V2.6
        """
        orderNo = '2009211811363554000502'
        amount = 53826
        ordertype = 2
        payMethod = 10
        payeeid = 1637
        remark = '尾款53826'
        response = self.trad._admin_pay_apply_add(orderNo_=orderNo, amount_=amount, type_=ordertype,
                                                  payMethod_=payMethod, payeeId_=payeeid, remark_=remark)
        self.assertEqual("OK", response.get("status"))

    def test_admin_managr_purchase_order_product_list(self):
        """
        订单详情-商品列表
        """
        orderNo = '2009211613381504000302'
        response = self.trad._admin_purchase_order_product_info(orderNo_=orderNo)
        self.assertEqual("OK", response.get("status"))
