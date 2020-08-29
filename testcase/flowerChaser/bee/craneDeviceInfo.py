#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/8/29 14:51 
# @Author : wei.zhang
# @File : craneDeviceInfo.py
# @Software: PyCharm

import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log import log
from testcase.flowerChaser.sql.craneManagementSQL import CraneManagementSQL
from utils.dataConversion.dataConversion import DataConversion as dc


class CraneDevice(unittest.TestCase):
    """
    接口文档: http://qa-gateway.worldfarm.com/swagger-ui.html#/
    """
    ba = BeeAction()
    db = CraneManagementSQL()
    mobile = '13666666666'
    log.info("开始执行设备信息模块测试用例")
    ba.set_user(mobile)

    def test_mobile_crane_binding_list(self):
        """
        航吊设备管理-设备信息-已绑定航吊列表
        """
        response = self.ba._mobile_crane_binding_list()
        self.assertEqual(response.get('status'), 'OK')
        seriallist = self.db.query_user_id_serial_on_list(userid=self.ba.user.user_id)
        seriallist = dc.data_assemble('serial_no', seriallist)
        self.assertListEqual(response.get('content'), seriallist)

    def test_mobile_crane_list(self):
        """
        航吊设备管理-设备信息-航吊集合
        """
        response = self.ba._mobile_crane_list()
        self.assertEqual(response.get('status'), 'OK')