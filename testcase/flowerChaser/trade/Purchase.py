#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2020 2020/8/06 17:10
收购单流程
"""
import json
import unittest
from interfaces.flowerChaser.TradeAction import TradeAction
from testcase.flowerChaser.sql.Bee import VisitRecordSql
from utils.fake.FakeLocation import FakeLocation
from utils.log import log
from testcase.flowerChaser.sql.Trade import ConfigProductSql
from faker import Faker
from random import choice
from utils.dataConversion.dataConversion import DataConversion
import datetime, time
import random
import json


class WorkbenchMain(unittest.TestCase, ConfigProductSql, FakeLocation, DataConversion):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    trad = TradeAction()
    pr_db = ConfigProductSql()
    vr = VisitRecordSql()
    fl = FakeLocation()
    fake = Faker(locale="zh_CN")
    trad.set_user('15200000033')

    def test_mobile_purchase_order_add(self):
        """
        V2.4.0 POST /mobile/purchase-order/add  订单生成
        :param self:
        :return:
        """
        remark = '接口测试备注'
        province, city, county, address, lng, lat = self.fl.fake_location()
        seller_id = self.pr_db.query_product_seller_id().get('seller_id')
        product_info = self.pr_db.query_product_info_by_seller_id(seller_id)
        catagory = product_info['parent_key']
        product_p = self.trad._mobile_purchase_order_product_grade_list(catagory_=catagory)
        i = random.randrange(0, 3)
        grade = product_p["content"][i]["grade"]
        price = product_p["content"][i]["price"]
        product_id = product_info['id']
        product_json = [{"grade": grade, "price": price, "productId": product_id}]
        product_json = json.dumps(product_json)
        response = self.trad._mobile_purchase_order_add(userId_=seller_id, province_=province, city_=city, county_=county,
                                                        address_=address, lng_=lng, lat_=lat, remark_=remark,
                                                        productJson_=product_json)
        self.assertEqual("OK", response["status"])

    def test_admin_purchase_order_product_info(self):
        """
        订单详情-商品信息
        :return:
        """
        order_no = 2008061337539221600802
        response = self.trad._admin_purchase_order_product_info(orderNo_=order_no)
        self.assertEqual("OK", response["status"])

    def test_admin_purchase_order_base_info(self):
        """
        POST /admin/purchase-order/base-info 订单详情-基本信息
        :return:
        """
        order_no = 2008061337539221600802
        response = self.trad._admin_purchase_order_base_info(orderNo_=order_no)
        self.assertEqual("OK", response["status"])

    def test_admin_purchase_order_status_count(self):
        """
        POST /admin/purchase-order/status-count 订单-状态分类统计
        :return:
        """
        response = self.trad._admin_purchase_order_status_count()
        db_response = self.pr_db.query_purchase_order_status_count()[0]
        self.assertEqual(db_response['全部'], response['content']["totalNum"])
        self.assertEqual(db_response['待审核'], response['content']["reviewedNum"])
        self.assertEqual(db_response['待质检'], response['content']["qualityNum"])
        self.assertEqual(db_response['待确认'], response['content']["unConfirmNum"])
        self.assertEqual(db_response['待结算尾款'], response['content']["unSettledNum"])
        self.assertEqual(db_response['已完成'], response['content']["finishNum"])

    def test_admin_extract_apply_allot(self):
        """
        POST /admin/extract-apply/allot 分配摇蜜专员
        :return:
        """
        apply_id = 35
        charge_id = 18331
        response = self.trad._admin_extract_apply_allot(applyId_=apply_id, chargeId_=charge_id)
        self.assertEqual("OK", response["status"])




