#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/11/11 14:59
# @Author: wei.zhang
# @File : warehouse.py
# @Software: PyCharm
"""
仓库
"""
import json
from interfaces.middleground.AssetAction import assetAction
from testcase.middleground.sql.asstMpSQL import warehouseSQL
from utils import runlevel, dataDispose, timestamp
from ddt import data, ddt
from faker import Faker
import unittest
import random


@ddt
class codeBase(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = assetAction()
        self.api.set_user(mobile=15882438888)
        self.db = warehouseSQL()
        self.faker = Faker('zh_CN')

    def test_admin_warehouse_add(self):
        """
        新增仓库
        :return:
        """
        code = 'PX-%s' % random.randint(1, 9999)
        name = '萌萌站起来'
        lng = None
        lat = None
        adders = '成都市高新区天府大道南三段天府软件园E区'
        area = 999
        goodsTypeIds = 7
        managerId = self.api.user.user_id
        leaseStartTime = timestamp.get_standardtime_timestamp(type=-1, week=10)
        leaseEndTime = timestamp.get_standardtime_timestamp(type=1, week=20)
        landlord = self.faker.name()
        landlordPhone = '15388126072'
        remark = self.faker.text(200)
        imgUrls = 'http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592385518283.jpg'
        resp = self.api._admin_warehouse_add(code_=code, name_=name, lng_=lng, lat_=lat, address_=adders,
                                             area_=area, goodsTypeIds_=goodsTypeIds, managerId_=managerId,
                                             leaseStartTime_=leaseStartTime, leaseEndTime_=leaseEndTime,
                                             landlord_=landlord, landlordPhone_=landlordPhone, remark_=remark,
                                             imgUrls_=imgUrls)
        self.assertEqual(resp.get('status'), 'OK')

    def test_admin_warehouse_list_owner(self):
        """
        自己的仓库列表
        :return:
        """
        resp = self.api._admin_warehouse_list_owner()
        self.assertEqual(resp.get('status'), 'OK')
