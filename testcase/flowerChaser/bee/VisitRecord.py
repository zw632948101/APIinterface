#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log.logger import logger
from testcase.flowerChaser.sql.Bee  import VisitRecordSql
from utils.fake.FakeLocation import FakeLocation
import random
import json
from faker import Faker
import datetime, time
import re


class VisitRecordMain(unittest.TestCase):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    visit_record = BeeAction()
    config_db = VisitRecordSql()
    fl = FakeLocation()
    log = logger('FarmInformationMain').logger
    log.info("开始执行拜访记录测试用例")
    fake = Faker(locale="zh_CN")
    visit_record.set_user('yaxin.guan@worldfarm.com', '123456')

    def test_mobile_visit_record_add(self):
        """
        POST /mobile/visit-record/add 添加拜访记录
        :return:
        """
        customer_list = self.config_db.sql_all_customer()
        if customer_list[0]["id"] is not None:
            num = random.randrange(0, len(customer_list))
            customer_id = customer_list[num]["id"]
            visit_purpose = random.randint(1, 2)
            province_id, city_id, district_id, address, lng, lat = self.fl.fake_location()
            sale_intention = random.randint(1, 3)
            colony = random.randint(1, 3)
            price = random.randint(1, 999999)
            price = price*100
            intention_price = random.choice([-1, price])
            remark = self.fake.text(max_nb_chars=50)
            response = self.visit_record._mobile_visit_record_add(beeFriendId_=customer_id, visitPurpose_=visit_purpose,
                                                                  province_=province_id, city_=city_id,
                                                                  county_=district_id, address_=address, lng_=lng,
                                                                  lat_=lat, saleIntention_=sale_intention,
                                                                  colony_=colony, intentionPrice_=intention_price,
                                                                  remark_=remark)
            self.assertEqual(response['status'], "OK")
        else:
            self.assertTrue(False, "暂无客户")

    def test_mobile_visit_record_list(self):
        """
        POST /mobile/visit-record/list 拜访记录列表
        :return:
        """
        customer_list = self.config_db.sql_all_customer()
        if customer_list[0]["id"] is not None:
            num = random.randrange(0, len(customer_list))
            customer_id = customer_list[num]["id"]
            response = self.visit_record._mobile_visit_record_list(beeFriendId_=customer_id)
            self.assertEqual(response['status'], "OK")
        else:
            self.assertTrue(False, "暂无客户")



