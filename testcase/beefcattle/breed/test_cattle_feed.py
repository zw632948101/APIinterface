#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/24 11:25
# @Author: wei.zhang
# @File : test_cattle_feed.py
# @Software: PyCharm
import json
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

    def test_admin_feed_add(self):
        """
        WEB-牛只饲养记录-新建牛只饲养记录
        :return:
        """
        farm_id = choice(self.farmid).get('id')
        fence_id = choice(
            self.cattle.query_cattle_fence_list(farm_id=farm_id, exist_filter=True)).get('id')
        feed_date = timestamp.get_timestamp()
        fodder_json = [{"warehouseCode": '50123', "fodderId": 'T0101010009', "dosage": '100'}]
        resp = self.breed._admin_feed_add(fenceId_=fence_id, cattleFarmId_=farm_id,
                                          feedDate_=feed_date, fodderJson_=json.dumps(fodder_json))
        self.assertEqual(resp.get('status'), 'OK')

    def test_admin_feed_list(self):
        """
        WEB-牛只饲养记录-牛只饲养记录列表
        :return:
        """
        farm_id = choice(self.farmid).get('id')
        fence = choice(self.cattle.query_cattle_fence_list(farm_id=farm_id, exist_filter=True))
        fence_no = fence.get('fenceNo')
        fence_no = None
        pn = None
        ps = None
        start_date = timestamp.get_standardtime_timestamp(type=-1, day=randint(1, 5),
                                                          formats="%Y-%m-%d")
        end_date = timestamp.get_standardtime_timestamp(day=randint(1, 5), formats="%Y-%m-%d")
        resp = self.breed._admin_feed_list(pn_=pn, ps_=ps, cattleFarmId_=farm_id, fenceNo_=fence_no,
                                           startFeedDate_=start_date, endFeedDate_=end_date)
        self.assertEqual(resp.get('status'), 'OK')
