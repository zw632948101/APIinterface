#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__: wei.zhang
 @FILE     : CollectionStatistics.py
 @Time     : 2020/5/12 14:38
 @Software : PyCharm
 蜂友采集统计
"""

import unittest
import random
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log.logger import logger
from faker import Faker
from testcase.flowerChaser.sql.Bee import CollectionStatisticsSQL, VisitRecordSql
from testcase.flowerChaser.sql.Passport import PassportInfoSql
from utils.Timestamp.TimestampTransform import TimestampTransform as tt


class CollectionStatistics(unittest.TestCase, tt):
    """
    接口文档: http://192.168.62.242:36054/swagger-ui.html
    """
    ba = BeeAction()
    ns = CollectionStatisticsSQL()
    ps = PassportInfoSql()
    vr = VisitRecordSql()
    mobile = '15388126080'
    log = logger('CollectionStatistics').logger
    log.info("开始执行蜂友采集统计")
    fake = Faker(locale="zh_CN")
    ba.set_user(mobile)

    def test_admin_bee_friend_collection_list(self):
        """
        运营后台-蜂友采集统计-蜂友采集统计列表 new V2.1.0
        """
        collectionTiem = self.get_standardtime_timestamp(type=1, formats="%Y-%m-%d")
        response = self.ba._admin_bee_friend_collection_list(countTime_=collectionTiem)
        self.assertEqual(response.get('status'), "OK")

    def test_admin_promoter_statistics_list(self):
        """
        运营后台-蜂友采集统计-线下推广人员统计列表 new V2.1.0
        """
        collectionTiem = self.get_standardtime_timestamp(type=1, formats="%Y-%m-%d")
        response = self.ba._admin_promoter_statistics_list(countTime_=collectionTiem)
        self.assertEqual(response.get('status'), "OK")

    def test_admin_bee_friend_statistics_total(self):
        """
        运营后台-蜂友统计-蜂友统计 new 2.1.0
        """
        response = self.ba._admin_bee_friend_statistics_total()
        self.assertEqual(response.get('status'), "OK")

    def test_admin_bee_friend_statistics_source(self):
        """
        运营后台-蜂友统计-蜂友来源统计数据 new 2.1.0
        """
        startDate = self.get_standardtime_timestamp(type=0, day=random.randint(1, 30), formats="%Y-%m-%d")
        endDate = self.get_standardtime_timestamp(type=1, formats="%Y-%m-%d")
        response = self.ba._admin_bee_friend_statistics_source(startDate_=startDate, endDate_=endDate)
        self.assertEqual(response.get('status'), "OK")

    def test_admin_bee_friend_statistics_collection_phone(self):
        """
        运营后台-蜂友统计-蜂友采集电话统计数据 new 2.1.0
        """
        startDate = self.get_standardtime_timestamp(type=0, day=random.randint(1, 30), formats="%Y-%m-%d")
        endDate = self.get_standardtime_timestamp(type=1, formats="%Y-%m-%d")
        response = self.ba._admin_bee_friend_statistics_collection_phone(startDate_=startDate, endDate_=endDate)
        self.assertEqual(response.get('status'), "OK")

    def test_admin_index_swarm_data(self):
        """
        运营后台-首页-蜂场分布-蜂场信息 new 2.1.0
        """
        response = self.ba._admin_index_swarm_data(swarmId_=33)
        self.assertEqual(response.get('status'), "OK")

    def test_admin_index_swarm_count(self):
        """
        运营后台-首页-蜂场分布-数据统计 new 2.1.0
        """
        response = self.ba._admin_index_swarm_count()
        self.assertEqual(response.get('status'), "OK")

    def test_admin_index_position_data(self):
        """
        运营后台-首页-蜂场分布-定位数据 new 2.1.0
        """
        dataTypes = random.choice([1, 2, '1,2'])
        startDate = self.get_standardtime_timestamp(type=0, day=random.randint(1, 30), formats="%Y-%m-%d")
        endDate = self.get_standardtime_timestamp(type=1, formats="%Y-%m-%d")
        response = self.ba._admin_index_position_data(dataTypes_=dataTypes, stDate_=startDate, edDate_=endDate,
                                                      vehicle_=None, stHiveNum_=None, edHiveNum_=None)
        self.assertEqual(response.get('status'), "OK")
