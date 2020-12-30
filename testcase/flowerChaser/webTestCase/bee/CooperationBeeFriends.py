#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/7/16 11:24 
# @Author : wei.zhang
# @File : CooperationBeeFriends.py
# @Software: PyCharm
import json
import unittest
import random
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log import log
from faker import Faker
from utils import DataConversion
from testcase.flowerChaser.sql.CooperationBeeFriendsSql import CooperationBeeFriendsSql


class CollectionStatistics(unittest.TestCase, DataConversion):
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
        content = lambda x: self.ba._admin_platform_bee_friend_total(status_=x)
        content_normal = content(1)
        content_quit = content(2)
        self.assertEqual(content_normal.get('status'), 'OK')
        self.assertEqual(content_quit.get('status'), 'OK')
        total = self.db.query_bee_friend_total()
        self.assertEqual(content_normal.get('content'), total.get('content_normal'))
        self.assertEqual(content_quit.get('content'), total.get('content_quit'))

    def test_admin_platform_bee_friend_list(self):
        """
        已入驻平台蜂友列表 & 已移除平台蜂友列表 V2.3.1
        """
        dataassemble = lambda dt: self.del_dict_value_null(dt=dt)
        b_status = random.choice([1, 2])
        response = self.ba._admin_platform_bee_friend_list(status_=b_status, pn_=1, ps_=20)
        self.assertEqual(response.get('status'), "OK")
        content = sorted(response.get('content').get('test_case'), key=lambda x: x['userId'])
        friend = dataassemble(self.db.query_common_bee_friend(b_status=b_status))
        friend = sorted(friend, key=lambda x: x['userId'])
        for i in range(len(friend)):
            location_r = dataassemble(self.db.query_location_region(userid=friend[i].get('userId')))
            native_r = dataassemble(self.db.query_native_region(userid=friend[i].get('userId')))
            friend[i]['locationRegion'] = location_r if location_r else {}
            friend[i]['nativeRegion'] = native_r if native_r else {}
            friend[i]['contactNumber'] = friend[i]['contactNumber'][0:3] + '****' + friend[i]['contactNumber'][-4:]
        for i in range(len(content)):
            self.assertDictEqual(content[i], friend[i])

    def test_admin_platform_bee_friend_list_search(self):
        """
        已入驻平台蜂友列表&已移除平台蜂友列表 (筛选)V2.3.1
        """
        dataassemble = lambda dt: self.del_dict_value_null(dt=dt)
        b_status = random.choice([1, 2])
        userinfo = dataassemble(self.db.query_all_platform_bee_friend(b_status))
        userinfo = random.choice(list(userinfo.values()))
        response = self.ba._admin_platform_bee_friend_list(status_=b_status, pn_=1, ps_=20, search_=userinfo)
        self.assertEqual(response.get('status'), "OK")
        content = sorted(response.get('content').get('test_case'), key=lambda x: x['userId'])
        friend = dataassemble(self.db.query_common_bee_friend(b_status=b_status, b_search=userinfo))
        friend = sorted(friend, key=lambda x: x['userId'])
        for i in range(len(friend)):
            location_r = dataassemble(self.db.query_location_region(userid=friend[i].get('userId')))
            native_r = dataassemble(self.db.query_native_region(userid=friend[i].get('userId')))
            friend[i]['locationRegion'] = location_r if location_r else {}
            friend[i]['nativeRegion'] = native_r if native_r else {}
            friend[i]['contactNumber'] = friend[i]['contactNumber'][0:3] + '****' + friend[i]['contactNumber'][-4:]
        for i in range(len(content)):
            self.assertDictEqual(content[i], friend[i])

    def test_admin_platform_bee_friend_detail(self):
        """
        运营后台-平台蜂友-详情
        """
        dataassemble = lambda dt: self.del_dict_value_null(dt=dt)
        b_status = random.choice([1, 2])
        userinfo = self.db.query_all_platform_bee_friend(b_status)
        userid = userinfo.get('user_id')
        userid = 486
        response = self.ba._admin_platform_bee_friend_detail(userId_=userid)
        self.assertEqual(response.get('status'), "OK")
        platform = dataassemble(self.db.query_one_platform_bee_friend(userid=userid))
        beeContainers = dataassemble(self.db.query_bee_container_list_devices_all(userid=userid))
        apiaryDetail = dataassemble(self.db.query_my_bee_field_info(userid=userid))
        if apiaryDetail.get('products'):
            apiaryDetail['products'] = apiaryDetail['products'].split(',')
        platform['apiaryDetail'] = apiaryDetail
        platform['beeContainers'] = beeContainers
        self.assertDictEqual(response.get('content'), platform)

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

    def test_admin_platform_bee_container_add_repetition(self):
        """
        新增平台蜂友 V2.3.1
        航吊摄像头编号不能重复
        """
        cameralist_ = self.db.query_bee_container_camera_list()
        gatway_list = self.data_assemble('gatewayNo', self.db.query_bee_container_gateway_list())
        cameralist = lambda str_key, number: self.data_assemble(str_key, cameralist_, number)

        containerInfo = [{'gatewayNo': i, 'cameraNo': random.choices(cameralist, k=cameralist('serialNo', 2))}
                         for i in gatway_list]
        containerInfo = json.dumps(containerInfo)
        mobilePhone = self.db.query_bee_container_add_repetition()
        moblie = random.choice(mobilePhone).get('contact_number')

        response = self.ba._admin_platform_bee_container_add(mobilePhone_=moblie, containerInfo_=containerInfo,
                                                             realName_='张云明')
        self.assertEqual(response.get('status'), "ERROR")
        self.assertEqual(response.get('errorMsg'), "航吊摄像头编号不能重复")

    def test_admin_platform_bee_container_add(self):
        """
        新增平台蜂友 V2.3.1
        """
        cameralist_ = self.db.query_bee_container_camera_list()
        gatway_list = self.data_assemble('gatewayNo', self.db.query_bee_container_gateway_list(), 4)
        cameralist = lambda str_key, number: self.data_assemble(str_key, cameralist_, number)
        containerInfo_list = [
            {'gatewayNo': i,
             'cameraNo': cameralist('serialNo', 2)}
            for i in gatway_list]
        containerInfo = json.dumps(containerInfo_list)
        mobilePhone = self.db.query_bee_container_add_mobile()
        mobilePhone = random.choice(self.del_dict_value_null(mobilePhone))
        Phone = mobilePhone.get('phone')
        username = mobilePhone.get('username')
        username = 'wangjue'
        Phone = 18612345678
        response = self.ba._admin_platform_bee_container_add(mobilePhone_=Phone, containerInfo_=containerInfo,
                                                             realName_=username)
        self.assertEqual(response.get('status'), "OK")
        userid = self.db.query_user_id(mobilePhone)[0].get('id')
        devices = self.db.query_bee_container_add_devices(userid, len(containerInfo))
        for i in range(len(devices)):
            devices[i]['cameraNo'] = devices[i]['cameraNo'].split(',')
            self.assertDictEqual(containerInfo_list[i], devices[i])

    def test_admin_platform_bee_container_list(self):
        """
        航吊列表 V2.3.1
        """
        mobilePhone = self.db.query_bee_container_add_repetition()
        userid = random.choice(mobilePhone).get('user_id')
        response = self.ba._admin_platform_bee_container_list(userId_=userid)
        self.assertEqual(response.get('status'), "OK")
        content = response.get('content')
        deviceslist = self.db.query_bee_container_list_devices_all(userid=userid)
        for i in range(len(content)):
            self.assertDictEqual(content[i], deviceslist[i])

    def test_admin_platform_bee_container_remove(self):
        """
        航吊移除 V2.3.1
        移除全部航吊
        """
        mobilePhone = self.db.query_bee_container_add_repetition()
        userid = random.choice(mobilePhone).get('user_id')
        deviceslist = self.db.query_bee_container_list_devices_all(userid=userid)
        beeContainerIds = self.data_assemble('id', deviceslist)
        response = self.ba._admin_platform_bee_container_remove(beeContainerIds_=beeContainerIds,
                                                                reason_='接口测试移除航吊：%s' % beeContainerIds)
        self.assertEqual(response.get('status'), "OK")
        quit_list = self.db.query_remov_devices_list(beeContainerIds)
        for i in quit_list:
            self.assertEqual(i.get('quit_reason'), '接口测试移除航吊：%s' % beeContainerIds)
            self.assertEqual(i.get('status'), 1)

    def test_admin_platform_bee_container_remove_one(self):
        """
        航吊移除 V2.3.1
        每次只删除一个
        """
        mobilePhone = self.db.query_bee_container_add_repetition()
        userid = random.choice(mobilePhone).get('user_id')
        deviceslist = self.db.query_bee_container_list_devices_all(userid=userid)
        beeContainerIds = random.choices(self.data_assemble('id', deviceslist))
        response = self.ba._admin_platform_bee_container_remove(beeContainerIds_=beeContainerIds,
                                                                reason_='接口测试移除航吊：%s' % beeContainerIds)
        self.assertEqual(response.get('status'), "OK")
        quit_list = self.db.query_remov_devices_list(beeContainerIds)
        for i in quit_list:
            self.assertEqual(i.get('quit_reason'), '接口测试移除航吊：%s' % beeContainerIds)
            self.assertEqual(i.get('status'), 1)

    def test_admin_platform_bee_container_user_record(self):
        """
        用户入驻记录 V2.3.1
        """
        mobilePhone = self.db.query_bee_container_add_repetition(-1)
        userid = random.choice(mobilePhone).get('user_id')
        # userid = 428
        response = self.ba._admin_platform_bee_container_user_record(userId_=userid)
        self.assertEqual(response.get('status'), "OK")

        removebcs = self.db.query_bee_container_user_record(userid=userid, u_status=1)
        usebcs = self.db.query_bee_container_user_record(userid=userid, u_status=0)
        usebcs = self.del_dict_value_null(usebcs)
        removebeeCS = response.get('content').get('removeBeeContainers')
        beecs = response.get('content').get('useBeeContainers')
        for i in range(len(removebeeCS)):
            self.assertDictEqual(removebcs[i], removebeeCS[i])
        for i in range(len(beecs)):
            self.assertDictEqual(beecs[i], usebcs[i])
