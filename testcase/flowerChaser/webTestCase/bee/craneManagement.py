#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/8/28 16:07 
# @Author : wei.zhang
# @File : craneManagementSQL.py
# @Software: PyCharm


import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log import log
from faker import Faker
from testcase.flowerChaser.sql.craneManagementSQL import CraneManagementSQL
from utils.fake.FakeLocation import FakeLocation
import random
import json
import time, datetime
from utils.dataConversion.dataConversion import DataConversion as dc
from utils.Timestamp.TimestampTransform import TimestampTransform as tt


class CraneManagement(unittest.TestCase):
    """
    接口文档: http://192.168.62.242:36054/swagger-ui.html
    """
    ba = BeeAction()
    db = CraneManagementSQL()
    fl = FakeLocation()
    mobile = '15388126082'
    log.info("开始执行蜜源植物管理模块测试用例")
    fake = Faker(locale="zh_CN")
    ba.set_user(mobile)

    def test_admin_crane_overview(self):
        """
        航吊设备管理-航吊统计 V2.5
        """
        response = self.ba._admin_crane_overview()
        self.assertEqual(response["status"], "OK")
        count = self.db.query_crane_binding_count()
        content = response.get('content')
        self.assertDictEqual(content, count)

    def test_admin_crane_un_binding_list(self):
        """
        航吊设备管理-未绑定航吊集合 V2.5
        """
        response = self.ba._admin_crane_un_binding_list()
        self.assertEqual(response["status"], "OK")
        un_binding_list = self.db.query_crane_un_binding_list()
        serial_list = sorted(dc.data_assemble('serial_no', un_binding_list), reverse=True)
        self.assertListEqual(response.get('content'), serial_list)

    def test_admin_crane_gps_list(self):
        """
        航吊设备管理-GPS集合 V2.5
        """
        response = self.ba._admin_crane_gps_list()
        self.assertEqual(response["status"], "OK")

    def test_admin_crane_gateway_list(self):
        """
        航吊设备管理-网关集合 V2.5
        """
        response = self.ba._admin_crane_gateway_list()
        self.assertEqual(response["status"], "OK")

    def test_admin_crane_camera_list(self):
        """
        航吊设备管理-摄像头集合 V2.5
        """
        response = self.ba._admin_crane_camera_list()
        self.assertEqual(response["status"], "OK")

    def test_admin_crane_binding(self):
        """
        航吊设备管理-配置/绑定航吊 V2.5
        """
        un_binding_list = self.db.query_crane_un_binding_list()
        userinfo = random.choices(self.db.query_bee_fried_user_info(), k=5)
        gateway_list = self.db.query_age_gateway_on_all()
        gps_list = self.db.query_agr_gps_un_binding_all()
        deviceID = random.choice(un_binding_list).get('serial_no')
        hiveNum = random.randint(1, 99999)
        gatewayNo = random.choice(gateway_list).get('gateway_no') if gateway_list else None
        cameraNo = None
        gpsNo = random.choice(gps_list).get('device_eui') if gps_list else None
        if random.randint(1, 2) == 1 and gpsNo is not None:
            gatewayNo = None
        elif gatewayNo is not None:
            gpsNo = None
        # gatewayNo = None
        # gpsNo = '0201010000000089'
        # gatewayNo = '0201010000000089'
        user_dict = [{"serialNo": deviceID, "joinDate": tt().get_standardtime_timestamp(formats="%Y-%m-%d"),
                      "mobile": i.get('contact_number'), "realName": i.get('real_name') + "接口测试添加航吊"} for i in userinfo]
        # user_dict = [{"serialNo": deviceID, "joinDate": tt().get_standardtime_timestamp(formats="%Y-%m-%d"),
        #               "mobile": '15388126044', "realName": "接口测试添加航吊"}]
        response = self.ba._admin_crane_binding(serialNo_=deviceID, hiveNum_=hiveNum, gatewayNo_=gatewayNo,
                                                cameraNo_=cameraNo, gpsNo_=gpsNo, users_=json.dumps(user_dict))
        self.assertEqual(response["status"], "OK")

    def test_admin_crane_binding_list(self):
        """
        航吊设备管理-航吊详情-绑定用户列表 V2.5
        """
        serial = random.choice(self.db.query_crane_binding_serial()).get('serial_no')
        user_status = random.choice((0, 1))
        response = self.ba._admin_crane_binding_list(serialNo_=serial, status_=user_status)
        self.assertEqual(response["status"], "OK")
        bindinglist = self.db.query_crane_binding_user_list(serial_no=serial, binding_status=user_status)
        content = response.get("content")
        for i in range(len(content)):
            self.assertDictEqual(bindinglist, content)

    def test_admin_crane_detail(self):
        """
        航吊设备管理-航吊详情 V2.5
        """
        serial = random.choice(self.db.query_crane_binding_serial()).get('serial_no')
        response = self.ba._admin_crane_detail(serialNo_=serial)
        self.assertEqual(response["status"], "OK")

    def test_admin_crane_edit(self):
        """
        航吊设备管理-编辑航吊
        """
        un_binding_list = self.db.query_crane_binding_serial()
        gateway_list = self.db.query_age_gateway_on_all()
        gps_list = self.db.query_agr_gps_un_binding_all()
        deviceID = random.choice(un_binding_list).get('serial_no')
        deviceID = 'HD0100081'
        hiveNum = random.randint(1, 99999)
        gatewayNo = random.choice(gateway_list).get('gateway_no') if gateway_list else None
        cameraNo = None
        gpsNo = random.choice(gps_list).get('device_eui') if gps_list else None
        if random.randint(1, 2) == 1 and gpsNo is not None:
            gatewayNo = None
        elif gatewayNo is not None:
            gpsNo = None
        # gatewayNo = None
        # gpsNo = '0201010000000089'
        # gatewayNo = '0201010000000089'
        # user_dict = [{"serialNo": deviceID, "joinDate": tt().get_standardtime_timestamp(formats="%Y-%m-%d"),
        #               "mobile": '15388126044', "realName": "接口测试添加航吊"}]
        response = self.ba._admin_crane_edit(serialNo_=deviceID, hiveNum_=hiveNum, gatewayNo_=gatewayNo,
                                             cameraNo_=cameraNo, gpsNo_=gpsNo)
        self.assertEqual(response["status"], "OK")

    def test_admin_crane_binding_user(self):
        """
        航吊设备管理-添加蜂友 V2.5
        """
        un_binding_list = self.db.query_crane_binding_serial()
        deviceID = random.choice(un_binding_list).get('serial_no')
        # deviceID = 'HD0100075'
        userinfo = random.choice(self.db.query_bee_fried_user_info())
        mobile = userinfo.get('contact_number')
        # mobile = '18904419415'
        realName = userinfo.get('real_name') + "接口测试编辑航吊"
        joinDate = tt().get_standardtime_timestamp(type=-1, day=1, formats="%Y-%m-%d")
        response = self.ba._admin_crane_binding_user(serialNo_=deviceID, mobile_=mobile, realName_=realName,
                                                     joinDate_=joinDate)
        self.assertEqual(response["status"], "OK")

    def test_admin_crane_exit(self):
        """
        航吊设备管理-移除蜂友 V2.5
        """
        un_binding_list = self.db.query_crane_binding_serial()
        deviceID = random.choice(un_binding_list).get('serial_no')
        # deviceID = 'HD0100075'
        bindinginfo = self.db.query_bind_users_by_device(serial_no=deviceID)
        bindingid = random.choice(bindinginfo).get('id')
        # bindingid = 71
        quitReason =None
        response = self.ba._admin_crane_exit(serialNo_=deviceID, id_=bindingid, quitReason_=quitReason)
        self.assertEqual(response["status"], "OK")
