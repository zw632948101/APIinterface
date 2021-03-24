#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/22 15:39
# @Author: wei.zhang
# @File : test_cattle.py
# @Software: PyCharm
import unittest
from interfaces.beefcattle.BreedAction import breedAction
from utils.fake.FakeLocation import FakeLocation
from ..sql.breed import BullLibrary, CattleFence
from utils.log import log
from faker import Faker
from random import choice, randint
from utils import timestamp, conversion


class TestCattle(unittest.TestCase):
    """
    牛舍
    接口文档:http://dev-gateway.worldfarm.com/swagger-ui.html
    """
    breed = breedAction()
    log.info("养殖育肥服务-公牛库模块测试")
    fake = Faker(locale="zh_CN")
    loaction = FakeLocation()
    bull = BullLibrary()
    cattle = CattleFence()
    breed.set_user(mobile=15388126072)
    farmid = bull.query_cattle_farm_id(userid=breed.user.user_id)

    def test_admin_cattle_add(self):
        """
        WEB-牛只信息-添加牛只信息
        :return:
        """
        farmid = choice(self.farmid).get('id')
        cattleEarTagNo_ = 'EB' + str(timestamp.get_timestamp())
        cattleFenceId_ = choice(self.cattle.query_cattle_fence_list(farm_id=farmid)).get('id')
        variety_ = None
        gender_ = choice(['1001', '1002', '1003'])
        birthday_ = timestamp.get_standardtime_timestamp(type=-1, week=randint(8, 90))
        entryDate_ = timestamp.get_timestamp()
        currentChildTime_ = None
        birthWeight_ = None
        feedType_ = None
        fatherNo_ = None
        motherNo_ = None
        rfidCode_ = None
        nucleusGroupStatus_ = None
        insureNo_ = None
        purchaseOrderNo_ = None
        skuCode_ = 'T160802'
        usedNo_ = 'EB' + str(timestamp.get_timestamp())
        pics_ = None
        resp = self.breed._admin_cattle_add(cattleEarTagNo_=cattleEarTagNo_,
                                            cattleFenceId_=cattleFenceId_, variety_=variety_,
                                            gender_=gender_, birthday_=birthday_,
                                            entryDate_=entryDate_,
                                            currentChildTime_=currentChildTime_,
                                            birthWeight_=birthWeight_, feedType_=feedType_,
                                            fatherNo_=fatherNo_, motherNo_=motherNo_,
                                            rfidCode_=rfidCode_,
                                            nucleusGroupStatus_=nucleusGroupStatus_,
                                            insureNo_=insureNo_, purchaseOrderNo_=purchaseOrderNo_,
                                            skuCode_=skuCode_, usedNo_=usedNo_, pics_=pics_)
        self.assertEqual(resp.get('status'), 'OK')
