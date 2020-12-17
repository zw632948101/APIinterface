#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/11/12 11:05
# @Author: wei.zhang
# @File : Warehouse.py
# @Software: PyCharm
"""
移动端-仓库模块
"""
import json
from interfaces.middleground.AssetAction import assetAction
from testcase.middleground.sql.asstMpSQL import mobileWarehouseSQL
from utils import runlevel, dataDispose, timestamp, FakeLocation, conversion
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
        self.db = mobileWarehouseSQL()
        self.faker = Faker('zh_CN')
        self.fa = FakeLocation()

    @unittest.skipIf(runlevel(1), '仓库-新增仓库')
    def test_admin_warehouse_add(self):
        """
        仓库-新增仓库
        :return:
        """
        typedict = self.db.query_admin_type_dict(typeid=2)
        typeid = conversion.data_assemble('id', typedict, random.randint(1, len(typedict)))
        code_ = 'JKCE-%s' % random.randint(1, 9999)
        province, city, district, address, lng, lat = self.fa.fake_location()
        name_ = self.faker.name()
        type_ = random.choice([10, 20, 30, 40, 50])  # 10-自有仓 20-临时仓 30-城市仓 40-商超门店 50-社区门店
        area_ = 999999
        capacity = 999999
        goodsTypeIds = typeid[0] if len(typeid) > 1 else ','.join(map(str, typeid))
        managerIds = self.api.user.user_id
        if random.choice([1, 2, 3]) == 1:
            leaseStartTime = timestamp.get_standardtime_timestamp(type=-1, week=20)
            leaseEndTime = timestamp.get_standardtime_timestamp(week=29)
            landlord = self.faker.name()
            landlordphoen = self.faker.phone_number()
            rent = random.randint(100, 999) * 10000
            rentUnit = random.choice(['元/月', '元/年'])
        else:
            leaseStartTime = leaseEndTime = landlord = landlordphoen = rent = rentUnit = None
        remark = self.faker.text(200)
        imgurls = 'https://dnkj-mp-asset-prod.oss-cn-beijing.aliyuncs.com/data/qa/mp-asset/1606891875667.jpg,' \
                  'https://dnkj-mp-asset-prod.oss-cn-beijing.aliyuncs.com/data/qa/mp-asset/1606891902220.jpg,' \
                  'https://dnkj-mp-asset-prod.oss-cn-beijing.aliyuncs.com/data/qa/mp-asset/1606891928597.jpg'
        response = self.api._admin_warehouse_add(code_=code_, name_=name_, type_=type_, lng_=lng,
                                                 lat_=lat,
                                                 province_=province, city_=city, county_=district,
                                                 address_=address,
                                                 area_=area_, capacity_=capacity,
                                                 goodsTypeIds_=goodsTypeIds,
                                                 managerIds_=managerIds,
                                                 leaseStartTime_=leaseStartTime,
                                                 leaseEndTime_=leaseEndTime, landlord_=landlord,
                                                 landlordPhone_=landlordphoen, rent_=rent,
                                                 rentUnit_=rentUnit,
                                                 remark_=remark, imgUrls_=imgurls)
        if response.get('status') == 'OK':
            self.assertEqual(response.get('status'), 'OK')
            dbinfo = self.db.query_warehouse_detail(code=code_, name=name_)
            self.assertEqual(len(dbinfo), 1)
        else:
            self.assertEqual(response.get('status'), 'ERROR')
            if response.get('errorCode') == '11050003':
                self.assertIn(response.get('errorMsg'),
                              ['照片Url集不能为空', '库管人不能为空', '存放货物类型不能为空', '容量不能为空', '仓库面积不能为空',
                               '仓库代码不能为空', '仓库名称超过长度限制(30)', '仓库名称不能为空', '仓库类型不能为空'])
            elif response.get('errorCode') == '11050001':
                self.assertIn(response.get('errorMsg'), ['系统繁忙，请稍后再试'])
            elif response.get('errorCode') == '11050101':
                self.assertIn(response.get('errorMsg'), ['可存放货物类型不存在'])

    @unittest.skipIf(runlevel(1), '仓库-仓库详情')
    def test_admin_warehouse_detail(self):
        """
        仓库-仓库详情
        :return:
        """
        dbinfo = random.choice(self.db.query_warehouse_detail())
        id_ = dbinfo.get('id')
        response = self.api._admin_warehouse_detail(id_=id_)
        if response.get('status') == 'OK':
            self.assertEqual(response.get('status'), 'OK')
            typedict = self.db.query_admin_type_dict(typeid=2)
            attach = conversion.data_assemble('url', self.db.query_asset_biz_attach(bizid=id_))
            typeid = dbinfo.get('goodsType').split(',')
            baseinfo = conversion.data_assemble('name',
                                                self.db.query_warehouse_user_base(warid=id_))
            goodsType = []
            for i in typedict:
                if str(i.get('id')) in typeid:
                    goodsType.append(i.get('name'))
            dbinfo['goodsType'] = ','.join(goodsType)
            dbinfo['imgUrls'] = sorted(attach, reverse=True)
            dbinfo['manager'] = ','.join(baseinfo)
            dbinfo['curStock'] = 0
            dbinfo['typeDesc'] = ''
            content = response.get('content')
            self.assertDictEqual(content, dbinfo)
        else:
            if response.get('errorCode') == '11050102':
                self.assertEqual(response.get('errorMsg'), '仓库不存在')
            elif response.get('errorCode') == '11050001':
                self.assertEqual(response.get('errorMsg'), '系统繁忙，请稍后再试')

    @unittest.skipIf(runlevel(1), '仓库-自己的仓库列表')
    def test_admin_warehouse_list_owner(self):
        """
        仓库-自己的仓库列表
        :return:
        """
        response = self.api._admin_warehouse_list_owner()
        self.assertEqual(response.get('status'), 'OK')
        dbinfo = self.db.query_my_warehouse_info(userid=self.api.user.user_id)
        content = response.get('content')
        for i in range(len(content)):
            self.assertDictEqual(content[i], dbinfo[i])

    @unittest.skipIf(runlevel(1), '仓库-分页列表')
    def test_admin_warehouse_page(self):
        """
        仓库-分页列表
        :return:
        """
        dbinfo = random.choice(self.db.query_warehouse_detail())
        pn = None
        ps = None
        code = dbinfo.get('code')
        name = dbinfo.get('name')
        response = self.api._admin_warehouse_page(pn_=pn, ps_=ps, code_=code, name_=name)
        self.assertEqual(response.get('status'), 'OK')
        wareinfo = self.db.query_warehouse_info
        content = response.get('content').get('datas')
        for i in range(len(content)):
            self.assertDictEqual(content[i], wareinfo[i])
