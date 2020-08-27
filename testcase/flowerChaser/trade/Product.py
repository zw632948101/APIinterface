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
    # workbench.set_user('15200000003')
    trad.set_user(mobile)

    def test_mobile_product_add(self):
        """
        V2.4.0 POST /mobile/product/add 添加商品
        :return:
        """
        pics = "http://a0.att.hudong.com/78/52/01200000123847134434529793168.jpg"
        user_id = 1315
        category_dict = {1001401: '蜂蜜', 1001402: '蜂花粉', 1001403: '蜂王浆'}
        # category_list = [1001401, 1001402, 1001403]
        category = random.choice((list(category_dict)))
        variety = self.pr_db.query_variety(category)['key']
        weight_range = self.fake.pyfloat(left_digits=random.randint(1, 6), right_digits=2, positive=True)
        # random.uniform(0.10, 999999.99)
        weight = round(weight_range, 2)
        purity_dict = {'1001501': '纯度<60%', '1001502': '70%纯度', '1001503': '80%纯度', '1001504': '90%纯度',
                       '1001505': '95%纯度'}
        purity = random.choice(list(purity_dict))
        consistence = None
        humidity = None
        if category == 1001401:
            consistence = random.randint(50, 99)
            humidity = None
        elif category == 1001402:
            consistence = None
            humidity = random.randint(20, 60)
        elif category == 1001403:
            consistence = None
            humidity = None
        province, city, county, address, lng, lat = self.fl.fake_location()
        remark = self.fake.text(max_nb_chars=200)
        response = self.trad._mobile_product_add(pics_=pics, sellerId_=647, category_=1001401, variety_=1001401001,
                                                 weight_=weight, purity_=purity, consistence_=consistence, humidity_=humidity,
                                                 province_=province, city_=city,
                                                 county_=county, manufactureDate_=1596607200000, remark_=remark)
        self.assertEqual("OK", response["status"])

    def test_mobile_purchase_order_product_grade_list(self):
        """
        POST /mobile/purchase-order/product-grade-list 定价标准列表
        :return:
        """
        cataegory = 1001403
        response = self.trad._mobile_purchase_order_product_grade_list(category_=cataegory)
        self.assertEqual("OK", response["status"])

    def test_mobile_product_list(self):
        """
         V2.4.0POST /mobile/product/list  商品列表
        :return:
        """
        manufactureDateStart = 1596211200
        manufactureDateEnd = 1596988800
        searchKey = 199
        response = self.trad._mobile_product_list(province_=None, city_=None, county_=None, category_=1001403, variety_=1001402001,
                                       status_=2, pn_=1, ps_=20, manufactureDateStart_=None,
                                       manufactureDateEnd_=None, searchKey_=199)
        self.assertEqual("OK", response["status"])

    def test_mobile_product_edit(self):
        """
        V2.4.0 POST /mobile/product/edit 编辑商品
        :return:
        """
        pics = "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/trade/product/1596615992350.jpg"
        product_id = self.pr_db.query_product_by_status().get('id')
        user_id = 1315
        category_dict = {1001401: '蜂蜜', 1001402: '蜂花粉', 1001403: '蜂王浆'}
        # category_list = [1001401, 1001402, 1001403]
        category = random.choice((list(category_dict)))
        variety = self.pr_db.query_variety(category)['key']
        weight_range = self.fake.pyfloat(left_digits=random.randint(1, 6), right_digits=2, positive=True)
        # random.uniform(0.10, 999999.99)
        weight = round(weight_range, 2)
        purity_dict = {'1001501': '纯度<60%', '1001502': '70%纯度', '1001503': '80%纯度', '1001504': '90%纯度',
                       '1001505': '95%纯度'}
        purity = random.choice(list(purity_dict))
        consistence = None
        humidity = None
        if category == 1001401:
            consistence = random.randint(50, 99)
            humidity = None
        elif category == 1001402:
            consistence = None
            humidity = random.randint(20, 60)
        elif category == 1001403:
            consistence = None
            humidity = None
        province, city, county, address, lng, lat = self.fl.fake_location()
        remark = self.fake.text(max_nb_chars=200)
        self.trad._mobile_product_edit(pics_=pics, id_=31, sellerId_=user_id, category_=category,
                                       variety_=variety, weight_=weight, purity_=purity, consistence_=consistence,
                                       humidity_=humidity, province_=province, city_=city, county_=county,
                                       manufactureDate_=1596607200000, remark_=remark)

    def test_mobile_product_del(self):
        """
        V 2.4.0 POST /mobile/product/del  删除商品
        :return:
        """
        self.trad._mobile_product_del(productId_=1)

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
        category = product_info['parent_key']
        product_p = self.trad._mobile_purchase_order_product_grade_list(category_=category)
        i = random.randrange(0, 3)
        grade = product_p["content"][i]["grade"]
        price = product_p["content"][i]["price"]*100
        product_id = product_info['id']
        product_json = [{"grade": grade, "price": price, "productId": product_id}]
        product_json = json.dumps(product_json)
        response = self.trad._mobile_purchase_order_add(userId_=seller_id, province_=province, city_=city, county_=county,
                                                        address_=address, lng_=lng, lat_=lat, remark_=remark,
                                                        productJson_=product_json)
        self.assertEqual("OK", response["status"])

    def test_mobile_purchase_order_edit(self):
        """
        V 2.4.0 POST /mobile/purchase-order/edit  订单编辑
        :return:
        """
        province, city, county, address, lng, lat = self.fl.fake_location()
        order_product_info = self.pr_db.query_product_in_order_by_order_id(order_id=35)
        category = order_product_info['parent_key']
        product_p = self.trad._mobile_purchase_order_product_grade_list(category_=category)
        i = random.randrange(0, 3)
        grade = product_p["content"][i]["grade"]
        price = product_p["content"][i]["price"] * 100
        product_id = order_product_info.get('id')
        product_json = [{"grade": grade, "price": price, "productId": product_id}]
        product_json = json.dumps(product_json)
        response = self.trad._mobile_purchase_order_edit(orderId_=35, province_=province, city_=city, county_=county,
                                                         address_=address, lng_=lng, lat_=lat, remark_='5555',
                                                         productJson_=product_json)
        self.assertEqual("OK", response["status"])

    def test_mobile_purchase_order_friend_list(self):
        """
        V 2.4.0 POST /mobile/purchase-order/friend-list  蜂友选择列表
        :return:
        """
        province, city, county, address, lng, lat = self.fl.fake_location()
        response = self.trad._mobile_purchase_order_friend_list(lng_=89.28338965094464, lat_=31.45070601118345)
        self.assertEqual("OK", response["status"])

    def test_mobile_purchase_order_product_sale_list(self):
        """
        V 2.4.0 POST /mobile/purchase-order/product-sale-list  蜂友待售商品列表
        :return:
        """
        seller_id = self.pr_db.query_product_seller_id().get('seller_id')
        self.trad._mobile_purchase_order_product_sale_list(sellerId_=seller_id)

    def test_mobile_purchase_order_page_list(self):
        """
         V 2.4.0 POST /mobile/purchase-order/page-list  管理端-订单列表
        :return:
        """
        status_dict = {10: '待审核', 20: '待质检', 30: '待客户确认', 40: '待尾款结算', 50: '已完成'}
        status = random.choice(list(status_dict))
        province, city, county, address, lng, lat = self.fl.fake_location()
        location = str(str(province) + '-' + str(city) + '-' + str(county))
        order_no = '2008071719290591600702'
        user_info = 199
        seller_id = self.pr_db.query_product_seller_id().get('seller_id')
        sort_dict = {'ASC': '升序', 'DESC': '降序'}
        sort = random.choice(list(sort_dict))
        self.trad._mobile_purchase_order_page_list(status_=None, pn_=1, ps_=20, startDate_=None,
                                                   endDate_=None, location_=None, orderNo_=order_no,
                                                   userInfo_=None, provence_=None, city_=None, county_=None,
                                                   sellerId_=None)


















