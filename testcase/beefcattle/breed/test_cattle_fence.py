#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/22 15:20
# @Author: wei.zhang
# @File : test_cattle_fence.py
# @Software: PyCharm
import unittest
from interfaces.beefcattle.BreedAction import breedAction
from utils.fake.FakeLocation import FakeLocation
from ..sql.breed import BullLibrary, CowshedSql,CattleFence
from utils.log import log
from faker import Faker
from random import choice, randint
from utils import timestamp


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
        cowshedid = choice(self.cow.query_cowshed_list_info(farmid=farmid)).get('id')
        fence_info = self.breed._admin_cattleFence_newFenceNo(cattleFarmId_=farmid,
                                                              cowshedId_=cowshedid)
        fenceNo = fence_info.get('content')
        fenceName = self.fake.name()
        type_ = choice(['1001', '1002'])
        area = None
        epcNo = None
        remark = None
        resp = self.breed._admin_cattleFence_add(fenceNo_=fenceNo, fenceName_=fenceName,
                                                 cowshedId_=cowshedid, cattleFarmId_=farmid,
                                                 type_=type_, area_=area, epcNo_=epcNo,
                                                 remark_=remark)
        self.assertEqual(resp.get('status'), 'OK')
