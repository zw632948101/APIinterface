#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/11/12 09:36
# @Author: wei.zhang
# @File : apply.py
# @Software: PyCharm

import json
from interfaces.middleground.AssetAction import assetAction
from testcase.middleground.sql.asstMpSQL import applySQL
from utils import runlevel, dataDispose, timestamp
from ddt import data, ddt
from faker import Faker
import unittest
import random


@ddt
class apply(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = assetAction()
        self.api.set_user(mobile=15388126082)
        self.db = applySQL()
        self.faker = Faker('zh_CN')

    def test_mobile_apply_add(self):
        """
        资产申请 - 新增申请单
        :return:
        """
        consigneeId_ = self.api.user.user_id
        consigneeType_ = 0
        productId_ = 2
        total_ = 10
        reason_ = self.faker.text(10)
        province_ = 510000
        city_ = 510100
        county_ = 510107
        address_ = '成都市武侯区天府大道南段天府软件园E区'
        lng_ = '104.06845004146564'
        lat_ = '30.537992903651553'
        resp = self.api._mobile_apply_add(consigneeId_=consigneeId_, consigneeType_=consigneeType_,
                                          productId_=productId_, total_=total_, reason_=reason_,
                                          province_=province_, city_=city_, county_=county_,
                                          address_=address_, lng_=lng_, lat_=lat_)
        self.assertEqual(resp.get('status'), 'OK')
