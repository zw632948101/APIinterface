#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/8/5 11:05 
# @Author : wei.zhang
# @File : applicationExtractApply.py
# @Software: PyCharm
from unittest import TestCase
from interfaces.flowerChaser.TradeAction import TradeAction
from testcase.flowerChaser.sql.applicationExtractApplySql import applicationExtractApplySql
from utils.log import log
from random import choice, randint
from utils import DataConversion, TimestampTransform


class applicationExtractApply(TestCase):
    log.info("开始执行合作蜂友")
    ta = TradeAction()
    mobile = '18919028649'
    db = applicationExtractApplySql()
    ta.set_user(mobile)
    tt = TimestampTransform()

    def test_web_extract_apply_add(self):
        """
        添加摇蜜申请单 new：V2.4.0
        """

        user_swarm_info = choice(self.db.query_added_as_platform_befriend())
        userid = user_swarm_info.get('user_id')
        userid = self.ta.user.user_id
        province = user_swarm_info.get('province')
        city = user_swarm_info.get('city')
        county = user_swarm_info.get('county')
        address = user_swarm_info.get('address')
        lat = user_swarm_info.get('lat')
        lng = user_swarm_info.get('lng')
        extractDate = self.tt.get_standardtime_timestamp(day=randint(1, 10), formats='%Y-%m-%d')
        response = self.ta._web_extract_apply_add(userId_=userid, extractDate_=extractDate, province_=province,
                                                  city_=city, county_=county, address_=address, lng_=lng, lat_=lat)
        self.assertEqual(response.get('status'), "OK")
        extract_apply = self.db.query_extract_apply_data_info(userid=userid, status=10, extractDate=extractDate)
        self.assertEqual(userid, extract_apply.get('creator_id'))
        self.assertEqual(province, extract_apply.get('province'))
        self.assertEqual(city, extract_apply.get('city'))
        self.assertEqual(county, extract_apply.get('county'))
        self.assertEqual(address, extract_apply.get('address'))
        self.assertEqual(lat, extract_apply.get('lat'))
        self.assertEqual(lng, extract_apply.get('lng'))
        self.assertEqual(extractDate, self.tt.str_time_timestamp(extract_apply.get('extract_date'), formats='%Y-%m-%d'))

    def test_web_extract_apply_my_extract_apply(self):
        """
        我的摇蜜申请 new V2.4.0
        """
        extract_apply = self.db.query_application_for_molasses_has_been_added()
        userid = choice(extract_apply).get('creator_id')
        # userid = '6812'
        response = self.ta._web_extract_apply_my_extract_apply(userId_=userid)
        self.assertEqual(response.get('status'), "OK")

    def test_admin_extract_apply_allot(self):
        """
        POST /admin/extract-apply/allot 分配摇蜜专员
        new V2.4.0
        :return:
        """
        apply_id = 32
        charge_id = 18331
        response = self.ta._admin_extract_apply_allot(applyId_=apply_id, chargeId_=charge_id)
        self.assertEqual("OK", response["status"])