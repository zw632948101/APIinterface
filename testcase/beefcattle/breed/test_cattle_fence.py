#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/22 15:20
# @Author: wei.zhang
# @File : test_cattle_fence.py
# @Software: PyCharm
import unittest
from interfaces.beefcattle.BreedAction import breedAction
from utils.fake.FakeLocation import FakeLocation
from ..sql.breed import BullLibrary, CowshedSql, CattleFence
from utils.log import log
from faker import Faker
from random import choice, randint
from utils import timestamp, conversion


class TestCattleFence(unittest.TestCase):
    """
    牛栏
    接口文档:http://dev-gateway.worldfarm.com/swagger-ui.html
    """
    breed = breedAction()
    log.info("养殖育肥服务-公牛库模块测试")
    fake = Faker(locale="zh_CN")
    loaction = FakeLocation()
    bull = BullLibrary()
    cow = CowshedSql()
    cattle = CattleFence()
    breed.set_user(mobile=15388126072)
    farmid = bull.query_cattle_farm_id(userid=breed.user.user_id)

    def test_admin_cattle_fence_add(self):
        """
        WEB-牛栏-新建牛栏
        :return:
        """
        farmid = choice(self.farmid).get('id')
        cowshedid = choice(self.cow.query_cowshed_list_info(farm_id=farmid)).get('id')
        fence_info = self.breed._admin_cattleFence_newFenceNo(cattleFarmId_=farmid,
                                                              cowshedId_=cowshedid)
        fenceNo = fence_info.get('content')
        fenceName = self.fake.name() + '的牛舍'
        # fenceName = None
        type_ = choice(['1001', '1002'])
        # type_ = None
        area = randint(999, 999999)
        # area = 'None'
        epcNo = 'NL' + str(timestamp.get_timestamp())
        remark = self.fake.text(30)
        resp = self.breed._admin_cattleFence_add(fenceNo_=fenceNo, fenceName_=fenceName,
                                                 cowshedId_=cowshedid, cattleFarmId_=farmid,
                                                 type_=type_, area_=area, epcNo_=epcNo,
                                                 remark_=remark)
        self.assertEqual(resp.get('status'), 'OK')
        fences = self.cattle.query_cattle_fence_list(farm_id=farmid, fence_no=fenceNo,
                                                     fence_name=fenceName, cowshed_id=cowshedid,
                                                     type_=type_, area=area, epc_no=epcNo,
                                                     remark=remark)
        self.assertEqual(len(fences), 1)

    def test_admin_cattle_fence_edit(self):
        """
        WEB-牛栏-编辑牛栏
        :return:
        """
        farmid = choice(self.farmid).get('id')
        fence = choice(self.cattle.query_cattle_fence_list(farm_id=farmid))
        fenceName = self.fake.name() + '的牛栏'
        # fenceName = '牛栏1'
        type_ = choice(['1001', '1002'])
        # type_ = None
        area = randint(999, 999999)
        epcNo = 'NL' + str(timestamp.get_timestamp())
        remark = self.fake.text(30)
        resp = self.breed._admin_cattleFence_edit(fenceName_=fenceName, type_=type_, area_=area,
                                                  epcNo_=epcNo, remark_=remark, id_=fence.get('id'))
        self.assertEqual(resp.get('status'), 'OK')
        fences = self.cattle.query_cattle_fence_list(farm_id=farmid, fence_name=fenceName,
                                                     type_=type_, area=area, epc_no=epcNo,
                                                     remark=remark)
        self.assertNotIn(fence, fences)

    def test_admin_cattle_fence_detail(self):
        """
        WEB-牛栏-牛栏详情
        :return:
        """
        farmid = choice(self.farmid).get('id')
        fence = choice(self.cattle.query_cattle_fence_list(farm_id=farmid))
        resp = self.breed._admin_cattleFence_detail(id_=fence.get('id'))
        self.assertEqual(resp.get('status'), 'OK')
        self.assertDictEqual(resp.get('content'), fence)

    def test_admin_cattle_fence_del(self):
        """
        WEB-牛栏-牛栏详情
        :return:
        """
        farmid = choice(self.farmid).get('id')
        fence = choice(self.cattle.query_cattle_fence_list(farm_id=farmid))
        resp = self.breed._admin_cattleFence_del(id_=fence.get('id'))
        self.assertEqual(resp.get('status'), 'OK')
        fences = self.cattle.query_cattle_fence_list(farm_id=farmid)
        self.assertNotIn(fence, fences)

    def test_admin_cattle_fence_list(self):
        """
        WEB-牛栏-牛栏列表
        :return:
        """
        farm_id = choice(self.farmid).get('id')
        fence_name = None
        fence_no = None
        cowshed_id = None
        pn = 1
        ps = 20
        cattle_exist_filter = None
        resp = self.breed._admin_cattleFence_list(cattleFarmId_=farm_id, fenceNo_=fence_no,
                                                  fenceName_=fence_name, cowshedId_=cowshed_id,
                                                  pn_=pn, ps_=ps,
                                                  cattleExistFilter_=cattle_exist_filter)
        self.assertEqual(resp.get('status'), 'OK')
        fences = self.cattle.query_cattle_fence_list(farm_id=farm_id, pn=pn, ps=ps,
                                                     exist_filter=cattle_exist_filter,
                                                     fence_no=fence_no, fence_name=fence_name,
                                                     cowshed_id=cowshed_id)
        fences = conversion.del_dict_value_null(fences)
        content = resp.get('content')
        for c, f in zip(content.get('datas'), fences):
            self.assertDictEqual(c, f)
