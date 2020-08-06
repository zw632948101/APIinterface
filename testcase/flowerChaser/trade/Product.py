#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2020 2020/3/31 17:10
工作台-蜂友资料
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
    user_id = 630
    mobile = (vr.query_contact_number_buy_user(user_id=user_id))[0].get('contact_number')
    fake = Faker(locale="zh_CN")
    # workbench.set_user('15200000033')
    trad.set_user(mobile)

    def test_mobile_product_add(self):
        """
        V2.4.0 POST /mobile/product/add 添加商品
        :return:
        """
        pics = "http://a0.att.hudong.com/78/52/01200000123847134434529793168.jpg"
        user_id = 569
        category_dict = {'1001401': '蜂蜜', '1001402': '蜂花粉', '1001403': '蜂王浆'}
        category = random.choice(list(category_dict))
        variety = self.pr_db.query_variety(category).get('key')
        weight_range = random.uniform(0.10, 999999.99)
        weight = round(weight_range, 2)
        purity_dict = {'1001501': '纯度<60%', '1001502': '70%纯度', '1001503': '80%纯度', '1001504': '90%纯度',
                       '1001505': '95%纯度'}
        purity = random.choice(list(purity_dict))
        province = self.pr_db.query_province().get('id')
        city = self.pr_db.query_city(province).get('id')
        remark = self.fake.text(max_nb_chars=200)
        response = self.trad._mobile_product_add(pics_=pics, sellerId_=user_id, category_=category, variety_=variety,
                                                 weight_=weight, purity_=purity, province_=province, city_=city,
                                                 manufactureDate_=1596643200, remark_=remark)
        self.assertEqual("OK", response["status"])

    def test_mobile_purchase_order_product_grade_list(self):
        """
        POST /mobile/purchase-order/product-grade-list 定价标准列表
        :return:
        """
        catagory = 1001403
        response = self.trad._mobile_purchase_order_product_grade_list(catagory_=catagory)
        self.assertEqual("OK", response["status"])

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





















