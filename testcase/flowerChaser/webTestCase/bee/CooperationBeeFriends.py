#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/7/16 11:24 
# @Author : wei.zhang
# @File : CooperationBeeFriends.py
# @Software: PyCharm

import unittest
import random
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log import log
from faker import Faker
from utils.Timestamp.TimestampTransform import TimestampTransform as tt
from testcase.flowerChaser.sql.CooperationBeeFriendsSql import CooperationBeeFriendsSql


class CollectionStatistics(unittest.TestCase, tt):
    """
    接口文档: http://192.168.62.242:36054/swagger-ui.html
    """
    ba = BeeAction()
    mobile = '19982917912'
    log.info("开始执行合作蜂友")
    fake = Faker(locale="zh_CN")
    db = CooperationBeeFriendsSql()
    ba.set_user(mobile)

    def test_admin_platform_bee_friend_total(self):
        """
        平台蜂友统计总数 V2.3.1
        """
        self.ba._admin_platform_bee_friend_total(status_=1)

    def test_admin_platform_bee_container_gateway_list(self):
        """
        获取网关列表 V2.3.1
        """
        response = self.ba._admin_platform_bee_container_gateway_list()
        self.assertEqual(response.get('status'), "OK")
        content = response.get('content')
        gatway_list = self.db.query_bee_container_gateway_list()
        for i in range(len(content)):
            self.assertDictEqual(gatway_list[i], content[i])

    def test_admin_platform_bee_container_camera_list(self):
        """
        获取摄像头列表 V2.3.1
        """
        response = self.ba._admin_platform_bee_container_camera_list()
        self.assertEqual(response.get('status'), "OK")
        content = sorted(response.get('content'), key=lambda x: x['channelName'])
        cameralist = self.db.query_bee_container_camera_list()
        self.assertListEqual(content, cameralist)
        # for i in range(len(content)):
        #     self.assertDictEqual(cameralist[i], content[i])

    def test_admin_platform_bee_container_add(self):
        """
        新增平台蜂友 V2.3.1
        """
        self.ba._admin_platform_bee_container_add(mobilePhone_=19988776600,
                                                  containerInfo_="[{gatewayNo:'0201030000000042',cameraNo:['E27814543']}]")
