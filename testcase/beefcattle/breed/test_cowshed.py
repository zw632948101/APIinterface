#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/22 15:09
# @Author: wei.zhang
# @File : test_cowshed.py
# @Software: PyCharm
import unittest
from interfaces.beefcattle.BreedAction import breedAction
from utils.fake.FakeLocation import FakeLocation
from ..sql.breed import BullLibrary
from utils.log import log
from faker import Faker
from random import choice, randint
from utils import timestamp


class TestCowshed(unittest.TestCase):
    """
    牛舍
    接口文档:http://dev-gateway.worldfarm.com/swagger-ui.html
    """
    breed = breedAction()
    log.info("养殖育肥服务-公牛库模块测试")
    fake = Faker(locale="zh_CN")
    loaction = FakeLocation()
    bull = BullLibrary()
    breed.set_user(mobile=15388126072)
    farmid = bull.query_cattle_farm_id(userid=breed.user.user_id)

    def test_admin_cowshed_add(self):
        """
        新增牛舍
        :return:
        """
        cowshedName = choice(self.bull.query_cattle_config_variety()).get('name') + '牛舍'
        cattleFarmId = choice(self.farmid).get('id')
        cowNo_info = self.breed._admin_cowshed_newCowshedNo(cattleFarmId_=cattleFarmId)
        cowshedNo = cowNo_info.get('content')
        area = None
        epcNo = None
        remark = None
        resp = self.breed._admin_cowshed_add(cowshedName_=cowshedName, cowshedNo_=cowshedNo,
                                             cattleFarmId_=cattleFarmId, area_=area, epcNo_=epcNo,
                                             remark_=remark)
        self.assertEqual(resp.get('status'), 'OK')
