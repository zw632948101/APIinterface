#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log.logger import logger
from testcase.flowerChaser.sql.Bee import ContainerInformationSql
import random
import json
from faker import Faker
import datetime, time
import requests


class ContainerMain(unittest.TestCase):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    container = BeeAction()
    container_db = ContainerInformationSql()
    log = logger('ContainerMain').logger
    log.info("开始执行平台管理接口测试用例")
    fake = Faker(locale="zh_CN")
    container.set_user('yaxin.guan@worldfarm.com', '123456')

    def test_mobile_container_gateway_list(self):
        """
        POST /mobile/container/gateway-list 网关列表
        :return:
        """
        response = self.container._mobile_container_gateway_list()
        return response["content"]

    def test_mobile_container_camera_list(self):
        """
        POST /mobile/container/camera-list 摄像头列表
        :return:
        """
        response = self.container._mobile_container_camera_list()
        return response["content"]

    def test_mobile_container_add(self):
        """
        POST /mobile/container/add 新建平台
        :return:
        """
        gateway_no_list = self.test_mobile_container_gateway_list()
        camera_list = self.test_mobile_container_camera_list()
        gateway_no = None
        camera_json = None
        json_list = []
        if len(gateway_no_list) is not None:
            num = random.randrange(0, len(gateway_no_list))
            gateway_no = gateway_no_list[num]["gatewayNo"]
        if len(camera_list) is not None:
            for i in range(3):
                num = random.randrange(0, len(camera_list))
                camera_no = camera_list[num]['serialNo']
                json_list.append(camera_no)
        camera = list(set(json_list))
        # camera_json = json.dumps(camera, ensure_ascii=False)
        serial_no = self.fake.password(length=10, special_chars=False, lower_case=False)
        hive_num = self.fake.random_int(min=1, max=999)
        start_date = datetime.datetime(year=2019, month=1, day=1)
        end_data = datetime.datetime(year=2019, month=12, day=26)
        receive_time = self.fake.date_time_between(start_date=start_date, end_date=end_data)
        receive_times = int(receive_time.timestamp() * 1000)
        receiver = self.fake.name()
        contact_number = self.fake.phone_number()
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_add(serialNo_=serial_no, gatewayNo_=gateway_no,
                                                        cameraNo_=camera,
                                                        hiveNum_=hive_num,
                                                        receiveTime_=receive_times, receiver_=receiver,
                                                        contactNumber_=contact_number,
                                                        picUrl_=pic_url, remark_=remark)
        if response["status"] == "OK":
            containers = self.container_db.sql_all_container()
            container_detail = containers[0]
            self.assertEqual(serial_no, container_detail["serial_no"])
            self.assertEqual(gateway_no, container_detail["gateway_no"])
            self.assertEqual(hive_num, container_detail["hive_num"])
            receive_time_time = time.localtime(receive_times / 1000)
            receive_time_stamp = time.strftime("%Y-%m-%d", receive_time_time)
            self.assertEqual(receive_time_stamp, container_detail["receive_time"])
            self.assertEqual(receiver, container_detail["receiver"])
            self.assertEqual(contact_number, container_detail["contact_number"])
            self.assertEqual(pic_url, container_detail["pic_url"])
            self.assertEqual(remark, container_detail["remark"])
        else:
            self.assertTrue(False, "养蜂平台添加失败")

    def test_mobile_container_add_with_same_serial_no(self):
        """
        POST /mobile/container/add 新建平台--输入数据库已存在的平台ID
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_add(serialNo_='4E3NQ2WW3A', gatewayNo_='0201010000000084',
                                                        cameraNo_='J60520790', hiveNum_=451, receiveTime_=1576393693000,
                                                        receiver_='曹莉', contactNumber_=14768632113,
                                                        picUrl_=pic_url, remark_=remark)
        self.assertEqual("平台ID已存在", response['errorMsg'])

    def test_mobile_container_add_without_serial_no(self):
        """
        POST /mobile/container/add 新建平台--平台ID为空
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_add(serialNo_=None, gatewayNo_='0201010000000084',
                                                        cameraNo_='J60520790', hiveNum_=451, receiveTime_=1576393693000,
                                                        receiver_='曹莉', contactNumber_=14768632113,
                                                        picUrl_=pic_url, remark_=remark)
        self.assertEqual("平台编号不能为空", response['errorMsg'])

    def test_mobile_container_add_without_hive_num(self):
        """
        POST /mobile/container/add 新建平台--蜂箱数量为空
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_add(serialNo_='K3CUH52NG0', gatewayNo_='0201010000000084',
                                                        cameraNo_='J60520790', hiveNum_=None,
                                                        receiveTime_=1576393693000,
                                                        receiver_='曹莉', contactNumber_=14768632113,
                                                        picUrl_=pic_url, remark_=remark)
        self.assertEqual("蜂箱数量不能为空", response['errorMsg'])

    def test_mobile_container_add_with_long_hive_num(self):
        """
        POST /mobile/container/add 新建平台--输入超长的蜂箱数量
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_add(serialNo_='K3CUH52NG9', gatewayNo_='0201010000000084',
                                                        cameraNo_='J60520790', hiveNum_=0, receiveTime_=1576393693000,
                                                        receiver_='曹莉', contactNumber_=14768632113,
                                                        picUrl_=pic_url, remark_=remark)
        self.assertEqual("蜂箱数量范围1~999整数", response['errorMsg'])

    def test_mobile_container_add_without_receive_time(self):
        """
        POST /mobile/container/add 新建平台--接收时间为空
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_add(serialNo_='K3CUH52NG81', gatewayNo_='0201010000000084',
                                                        cameraNo_='J60520790', hiveNum_=451, receiveTime_=None,
                                                        receiver_='曹莉', contactNumber_=14768632113,
                                                        picUrl_=pic_url, remark_=remark)
        self.assertEqual("接收时间不能为空", response['errorMsg'])

    def test_mobile_container_add_without_receiver(self):
        """
        POST /mobile/container/add 新建平台--接收人为空
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_add(serialNo_='K3CUH52NG81', gatewayNo_='0201010000000084',
                                                        cameraNo_='J60520790', hiveNum_=451, receiveTime_=1576393693000,
                                                        receiver_=None, contactNumber_=14768632113,
                                                        picUrl_=pic_url, remark_=remark)
        self.assertEqual("接收人不能为空", response['errorMsg'])

    def test_mobile_container_add_without_contact_number(self):
        """
        POST /mobile/container/add 新建平台--联系电话为空
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_add(serialNo_='K3CUH52NG81', gatewayNo_='0201010000000084',
                                                        cameraNo_='J60520790', hiveNum_=451, receiveTime_=1576393693000,
                                                        receiver_='曹莉', contactNumber_=None,
                                                        picUrl_=pic_url, remark_=remark)
        self.assertEqual("联系电话不能为空", response['errorMsg'])

    def test_mobile_container_add_with_wrong_contact_number(self):
        """
        POST /mobile/container/add 新建平台--输入错误的联系电话格式
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_add(serialNo_='K3CUH52NG81', gatewayNo_='0201010000000084',
                                                        cameraNo_='J60520790', hiveNum_=451, receiveTime_=1576393693000,
                                                        receiver_='曹莉', contactNumber_=24768632113,
                                                        picUrl_=pic_url, remark_=remark)
        self.assertEqual("联系电话格式不正确", response['errorMsg'])

    def test_mobile_container_add_without_pic_url(self):
        """
        POST /mobile/container/add 新建平台--平台照片为空
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_add(serialNo_='K3CUH52NG81', gatewayNo_='0201010000000084',
                                                        cameraNo_='J60520790', hiveNum_=451, receiveTime_=1576393693000,
                                                        receiver_='曹莉', contactNumber_=14768632113,
                                                        picUrl_=None, remark_=remark)
        self.assertEqual("平台照片不能为空", response['errorMsg'])

    def test_mobile_container_add_with_wrong_gateway_no(self):
        """
        POST /mobile/container/add 新建平台--错误的网关编码
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_add(serialNo_='K3CUH52NG81', gatewayNo_='0201010000000111111',
                                                        cameraNo_='J60520790', hiveNum_=451, receiveTime_=1576393693000,
                                                        receiver_='曹莉', contactNumber_=14768632113,
                                                        picUrl_=pic_url, remark_=remark)
        self.assertEqual("网关(GatewayNo:0201010000000111111)不存在", response['errorMsg'])

    def test_mobile_container_add_with_wrong_camera_no(self):
        """
        POST /mobile/container/add 新建平台--错误的摄像头编码
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_add(serialNo_='K3CUH52NG81', gatewayNo_='0201010000000084',
                                                        cameraNo_='333444444', hiveNum_=451, receiveTime_=1576393693000,
                                                        receiver_='曹莉', contactNumber_=14768632113,
                                                        picUrl_=pic_url, remark_=remark)
        self.assertEqual("摄像头(Serialno:333444444)不存在", response['errorMsg'])

    def test_mobile_container_del(self):
        """
        POST /mobile/container/del 平台删除
        :return:
        """
        container_list = self.container_db.sql_container_id_by_status()
        if container_list[0]["id"] is not None:
            num = random.randrange(0, len(container_list))
            container_id = container_list[num]["id"]
            response = self.container._mobile_container_del(id_=container_id)
            self.assertEqual(response['status'], "OK")
        else:
            self.assertTrue(False, "暂无待投放养蜂平台")

    def test_mobile_container_del_without_container_id(self):
        """
        POST /mobile/container/del 平台删除- 平台ID为空
        :return:
        """
        response = self.container._mobile_container_del(id_=None)
        self.assertEqual("平台ID不能为空", response['errorMsg'])

    def test_mobile_container_del_with_wrong_status(self):
        """
        POST /mobile/container/del 平台删除--删除状态为已投放或者已摇蜜的养蜂平台
        :return:
        """
        response = self.container._mobile_container_del(id_=3)
        self.assertEqual("养蜂平台已投入使用,不能删除", response['errorMsg'])

    def test_mobile_container_detail(self):
        """
        POST /mobile/container/detail 平台详情
        :return:
        """
        container_list = self.container_db.sql_all_container()
        if container_list[0]["id"] is not None:
            num = random.randrange(0, len(container_list))
            container_id = container_list[num]["id"]
            response = self.container._mobile_container_detail(id_=container_id)
            self.assertEqual(response['status'], "OK")
        else:
            self.assertTrue(False, "暂无养蜂平台")

    def test_mobile_container_detail_without_container_id(self):
        """
        POST /mobile/container/detail 平台详情-查看不存在或者已经删除的养蜂平台
        :return:
        """
        response = self.container._mobile_container_detail(id_=2)
        self.assertEqual("养蜂平台不存在", response['errorMsg'])

    def test_mobile_container_edit(self):
        """
        POST /mobile/container/edit 编辑平台
        :return:
        """
        container_list = self.container_db.sql_all_container()
        if container_list[0]["id"] is not None:
            num = random.randrange(0, len(container_list))
            container_id = container_list[num]["id"]
            gateway_no_list = self.test_mobile_container_gateway_list()
            camera_list = self.test_mobile_container_camera_list()
            gateway_no = None
            camera_json = None
            json_list = []
            if len(gateway_no_list) is not None:
                num = random.randrange(0, len(gateway_no_list))
                gateway_no = gateway_no_list[num]["gatewayNo"]
            if len(camera_list) is not None:
                for i in range(3):
                    num = random.randrange(0, len(camera_list))
                    camera_no = camera_list[num]['serialNo']
                    json_list.append(camera_no)
            camera = list(set(json_list))
            serial_no = self.fake.password(length=10, special_chars=False, lower_case=False)
            hive_num = self.fake.random_int(min=1, max=999)
            start_date = datetime.datetime(year=2019, month=1, day=1)
            end_data = datetime.datetime(year=2019, month=12, day=26)
            receive_time = self.fake.date_time_between(start_date=start_date, end_date=end_data)
            receive_times = int(receive_time.timestamp() * 1000)
            receiver = self.fake.name()
            contact_number = self.fake.phone_number()
            pic_url = json.dumps(
                ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
                ensure_ascii=False)
            remark = self.fake.text(max_nb_chars=200)
            response = self.container._mobile_container_edit(serialNo_=serial_no, gatewayNo_=gateway_no,
                                                             cameraNo_=camera, hiveNum_=hive_num,
                                                             receiveTime_=receive_times, receiver_=receiver,
                                                             contactNumber_=contact_number,
                                                             picUrl_=pic_url, remark_=remark, id_=container_id)
            if response["status"] == "OK":
                containers = self.container_db.sql_container_by_id(container_id)
                container_detail = containers[0]
                self.assertEqual(serial_no, container_detail["serial_no"])
                self.assertEqual(gateway_no, container_detail["gateway_no"])
                self.assertEqual(hive_num, container_detail["hive_num"])
                receive_time_time = time.localtime(receive_times / 1000)
                receive_time_stamp = time.strftime("%Y-%m-%d", receive_time_time)
                self.assertEqual(receive_time_stamp, container_detail["receive_time"])
                self.assertEqual(receiver, container_detail["receiver"])
                self.assertEqual(contact_number, container_detail["contact_number"])
                self.assertEqual(pic_url, container_detail["pic_url"])
                self.assertEqual(remark, container_detail["remark"])
            else:
                self.assertTrue(False, "养蜂平台修改失败")

    def test_mobile_container_edit_with_same_serial_no(self):
        """
        POST /mobile/container/edit 编辑平台--输入数据库已存在的平台ID
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_edit(serialNo_='4E3NQ2WW3A', gatewayNo_='0201010000000084',
                                                         cameraNo_='J60520790', hiveNum_=451,
                                                         receiveTime_=1576393693000,
                                                         receiver_='曹莉', contactNumber_=14768632113,
                                                         picUrl_=pic_url, remark_=remark, id_=1)
        self.assertEqual("平台ID已存在", response['errorMsg'])

    def test_mobile_container_edit_without_serial_no(self):
        """
        POST /mobile/container/edit 编辑平台--平台ID为空
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_edit(serialNo_=None, gatewayNo_='0201010000000084',
                                                         cameraNo_='J60520790', hiveNum_=451,
                                                         receiveTime_=1576393693000,
                                                         receiver_='曹莉', contactNumber_=14768632113,
                                                         picUrl_=pic_url, remark_=remark, id_=1)
        self.assertEqual("平台编号不能为空", response['errorMsg'])

    def test_mobile_container_edit_without_hive_num(self):
        """
        POST /mobile/container/edit 编辑平台--蜂箱数量为空
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_edit(serialNo_='K3CUH52NG0', gatewayNo_='0201010000000084',
                                                         cameraNo_='J60520790', hiveNum_=None,
                                                         receiveTime_=1576393693000,
                                                         receiver_='曹莉', contactNumber_=14768632113,
                                                         picUrl_=pic_url, remark_=remark, id_=1)
        self.assertEqual("蜂箱数量不能为空", response['errorMsg'])

    def test_mobile_container_edit_with_long_hive_num(self):
        """
        POST /mobile/container/edit 编辑平台--输入超长的蜂箱数量
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_edit(serialNo_='K3CUH52NG9', gatewayNo_='0201010000000084',
                                                         cameraNo_='J60520790', hiveNum_=0,
                                                         receiveTime_=1576393693000,
                                                         receiver_='曹莉', contactNumber_=14768632113,
                                                         picUrl_=pic_url, remark_=remark, id_=1)
        self.assertEqual("蜂箱数量范围1~999整数", response['errorMsg'])

    def test_mobile_container_edit_without_receive_time(self):
        """
        POST /mobile/container/edit 编辑平台--接收时间为空
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_edit(serialNo_='K3CUH52NG81', gatewayNo_='0201010000000084',
                                                         cameraNo_='J60520790', hiveNum_=451, receiveTime_=None,
                                                         receiver_='曹莉', contactNumber_=14768632113,
                                                         picUrl_=pic_url, remark_=remark, id_=1)
        self.assertEqual("接收时间不能为空", response['errorMsg'])

    def test_mobile_container_edit_without_receiver(self):
        """
        POST /mobile/container/edit 编辑平台--接收人为空
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_edit(serialNo_='K3CUH52NG81', gatewayNo_='0201010000000084',
                                                         cameraNo_='J60520790', hiveNum_=451,
                                                         receiveTime_=1576393693000,
                                                         receiver_=None, contactNumber_=14768632113,
                                                         picUrl_=pic_url, remark_=remark, id_=1)
        self.assertEqual("接收人不能为空", response['errorMsg'])

    def test_mobile_container_edit_without_contact_number(self):
        """
        POST /mobile/container/edit 编辑平台--联系电话为空
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_edit(serialNo_='K3CUH52NG81', gatewayNo_='0201010000000084',
                                                         cameraNo_='J60520790', hiveNum_=451,
                                                         receiveTime_=1576393693000,
                                                         receiver_='曹莉', contactNumber_=None,
                                                         picUrl_=pic_url, remark_=remark, id_=1)
        self.assertEqual("联系电话不能为空", response['errorMsg'])

    def test_mobile_container_edit_with_wrong_contact_number(self):
        """
        POST /mobile/container/edit 编辑平台--输入错误的联系电话格式
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_edit(serialNo_='K3CUH52NG81', gatewayNo_='0201010000000084',
                                                         cameraNo_='J60520790', hiveNum_=451,
                                                         receiveTime_=1576393693000,
                                                         receiver_='曹莉', contactNumber_=24768632113,
                                                         picUrl_=pic_url, remark_=remark, id_=1)
        self.assertEqual("联系电话格式不正确", response['errorMsg'])

    def test_mobile_container_edit_without_pic_url(self):
        """
        POST /mobile/container/edit 编辑平台--平台照片为空
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_edit(serialNo_='K3CUH52NG81', gatewayNo_='0201010000000084',
                                                         cameraNo_='J60520790', hiveNum_=451,
                                                         receiveTime_=1576393693000,
                                                         receiver_='曹莉', contactNumber_=14768632113,
                                                         picUrl_=None, remark_=remark, id_=1)
        self.assertEqual("平台照片不能为空", response['errorMsg'])

    def test_mobile_container_edit_with_wrong_gateway_no(self):
        """
        POST /mobile/container/edit 编辑平台--错误的网关编码
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_edit(serialNo_='K3CUH52NG81', gatewayNo_='0201010000000111111',
                                                         cameraNo_='J60520790', hiveNum_=451,
                                                         receiveTime_=1576393693000,
                                                         receiver_='曹莉', contactNumber_=14768632113,
                                                         picUrl_=pic_url, remark_=remark, id_=1)
        self.assertEqual("网关(GatewayNo:0201010000000111111)不存在", response['errorMsg'])

    def test_mobile_container_edit_with_wrong_camera_no(self):
        """
        POST /mobile/container/edit 编辑平台--错误的摄像头编码
        :return:
        """
        pic_url = json.dumps(
            ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1578897317144.jpg"],
            ensure_ascii=False)
        remark = self.fake.text(max_nb_chars=200)
        response = self.container._mobile_container_edit(serialNo_='K3CUH52NG81', gatewayNo_='0201010000000084',
                                                         cameraNo_='333444444', hiveNum_=451,
                                                         receiveTime_=1576393693000,
                                                         receiver_='曹莉', contactNumber_=14768632113,
                                                         picUrl_=pic_url, remark_=remark, id_=1)
        self.assertEqual("摄像头(Serialno:333444444)不存在", response['errorMsg'])

    def test_mobile_container_list(self):
        """
        POST /mobile/container/list 平台不分页列表
        :return:
        """
        response = self.container._mobile_container_list()
        self.assertEqual(response['status'], "OK")

    def test_mobile_container_page_list(self):
        """
        POST /mobile/container/page-list 平台分页列表
        :return:
        """
        response = self.container._mobile_container_page_list()
        self.assertEqual(response['status'], "OK")

    def test_mobile_container_ready_count(self):
        """
        POST /mobile/container/ready-count 待投放平台数量
        :return:
        """
        response = self.container._mobile_container_ready_count()
        self.assertEqual(response['status'], "OK")

    def test_mobile_container_camera_check(self):
        """
        POST /mobile/container/camera-check 摄像头选择前校验【可联调】
        :return:
        """
        serial_nos = ['J60520791', 'J60520790']
        container_id = None
        response = self.container._mobile_container_camera_check(serialNos_=serial_nos, containerId_=container_id)
        self.assertEqual("摄像头J60520791、J60520790已在其他养蜂平台使用中，请再次确认是否使用，选择使用后，其他平台则无法再使用",
                         response['errorMsg'])

    def test_mobile_container_gateway_check(self):
        """
        POST /mobile/container/gateway-check 网关选择前校验【可联调】
        :return:
        """
        serial_nos = '0201010000000084'
        container_id = None
        response = self.container._mobile_container_gateway_check(gatewayNo_=serial_nos, containerId_=container_id)
        self.assertEqual("网关0201010000000084已在其他养蜂平台使用中，请再次确认是否使用，选择使用后，其他平台则无法再使用",
                         response['errorMsg'], )
