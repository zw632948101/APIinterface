#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log import log
from testcase.flowerChaser.sql.Bee import ConfigInformationSql, NectarSourceInformationSql, ContainerInformationSql
from testcase.flowerChaser.sql.OwnFarm import OwnFarmSql
from utils.fake.FakeLocation import FakeLocation
from faker import Faker
from random import choice
import random


class OwnFarmMain(unittest.TestCase):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    own_bee_farm = BeeAction()
    config_db = ConfigInformationSql()
    nectar_source_db = NectarSourceInformationSql()
    container_db = ContainerInformationSql()
    own_farm_db = OwnFarmSql()
    fl = FakeLocation()
    log.info("开始执行我的蜂场测试用例")
    fake = Faker(locale="zh_CN")
    own_bee_farm.set_user('19982917912')

    def test_mobile_nearby_bee_friend_list(self):
        """
        POST /mobile/nearby-bee-friend/page-list  V 2.3.1
        周边蜂友分页列
        :return:
        """
        lng = 104.042474
        lat = 30.544192
        response = self.own_bee_farm._mobile_nearby_bee_friend_list(lng_=lng, lat_=lat)
        own_farm_friend_sql = self.own_farm_db.query_nearby_friend(lat=lat, lng=lng)
        self.assertEqual(len(response['content']), len(own_farm_friend_sql))

    def test_mobile_nearby_bee_friend_associate(self):
        """
        POST /mobile/nearby-bee-friend/associate  V 2.3.1
        蜂友联想列表
        :return:
        """
        response = self.own_bee_farm._mobile_nearby_bee_friend_associate(pn_=1, ps_=50, searchKey_='蜂友')

    def test_mobile_bee_friend_follow_follow(self):
        """
        POST /mobile/bee-friend-follow/follow  V 2.3.0
        蜂友关注
        :return:
        """
        follow_friend_list = self.own_farm_db.query_follow_friend()
        follow_friend_info = choice(follow_friend_list)
        follow_friend_id = follow_friend_info.get('id')
        opt_type = random.randint(1, 2)
        self.own_bee_farm._mobile_bee_friend_follow_follow(followFriendId_=follow_friend_id,
                                                           optType_=opt_type)

    def test_mobile_apiary_overview(self):
        """
        POST /mobile/apiary/overview 我的蜂场信息预览
        :return:
        """
        province, city, county, address, lng, lat = self.fl.fake_location()
        self.own_bee_farm._mobile_apiary_overview(lat_=lat, lng_=lng)


