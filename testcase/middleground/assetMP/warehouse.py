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
from utils import runlevel, dataDispose, timestamp, conversion
from ddt import data, ddt
from faker import Faker
import unittest
import random


@ddt
class warehouse(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = assetAction()
        self.api.set_user(mobile=15388126082)
        self.db = warehouseSQL()
        self.faker = Faker('zh_CN')

    def test_admin_warehouse_add(self):
        """
        新增仓库
        :return:
        """
        code = 'DD-%s' % random.randint(1, 9999)
        name = '豆豆1'
        lng_ = 126.548078
        lat_ = 45.816896
        province_ = 230000
        city_ = 230100
        county_ = 230102
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
        resp = self.api._admin_warehouse_add(code_=code, name_=name, lng_=lng_, lat_=lat_, address_=adders,
                                             area_=area, goodsTypeIds_=goodsTypeIds, managerId_=managerId,
                                             leaseStartTime_=leaseStartTime, leaseEndTime_=leaseEndTime,
                                             landlord_=landlord, landlordPhone_=landlordPhone, remark_=remark,
                                             imgUrls_=imgUrls, province_=province_, city_=city_, county_=county_)
        self.assertEqual(resp.get('status'), 'OK')

    def test_admin_warehouse_list_owner(self):
        """
        自己的仓库列表
        :return:
        """
        resp = self.api._admin_warehouse_list_owner()
        self.assertEqual(resp.get('status'), 'OK')

    def test_admin_warehouse_out_warehouse(self):
        """
        仓库-出库
        :return:
        """
        applyinfo = self.db.query_asset_apply_status_data(applicantid=self.api.user.user_id)[0]
        codeinfo = self.db.query_status_product_warehouse_aseet_code(warehouseid=applyinfo.get('warehouse_id'),
                                                                     product_id=applyinfo.get('product_id'))
        id = applyinfo.get('id')
        codes = conversion.data_assemble('code', codeinfo, applyinfo.get('total'))
        resp = self.api._admin_warehouse_out_warehouse(id_=id, codes_=codes)
        self.assertEqual(resp.get('status'), 'OK')
