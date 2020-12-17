#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import unittest
import json
import random
from testcase.middleground.WMS.prepare.login import login
from testcase.middleground.WMS.common.Pash import Header_mkdir # 存放header值得配置文件
from testcase.middleground.WMS.common.Pash import Public_mkdir
from testcase.middleground.WMS.common.config import read_config
from testcase.middleground.WMS.common.Mysql import mp_label
from testcase.middleground.WMS.datas.warehouse_data import warehouse_data
from ddt import data, ddt
from testcase.middleground.WMS.common.Http import Request

class Centext:
    serialNo_code = ''
@ddt
class warehouse_monitor(unittest.TestCase):
    # 测试准备--登录
    def setUp(self):
        '''
                测试准备，先登录,准备header (header里的key一定要写成 _Device-Id_ 和 _Token_  )
                '''
        self.url = r"/world-passport/admin/sso/sms-login"
        self.login = login(self.url).test_login()
        self.headers = {
            "_Device-Id_": read_config(Header_mkdir).get("header", "_device-id_"),
            "_Token_": read_config(Header_mkdir).get("header", "_token_"),
            "region": "online"
        }

    # 获取摄像头编号接口
    def test_01_monitor_list(self):
        url = read_config(Public_mkdir).get("test_url","url") + "/admin/warehouse/monitor/camera-list"
        response = Request('post',url=url,data=None,headers=self.headers,cookie=None)
        result = response.get_json()
        # 收集摄像头编号
        serialNo_list = []
        if result['status'] == 'OK':
            for serialNo in result['content']:
                serialNo_list.append(serialNo['serialNo'])
        else:
            print("获取摄像头编号报错: %s"%result)
        setattr(Centext,"serialNo_code",random.choice(serialNo_list))

    #绑定仓库
    def test_02_monitor_bind(self):
        url = read_config(Public_mkdir).get("test_url","url") + "/admin/warehouse/monitor/bind"
        data = {"cameraCodes":getattr(Centext,"serialNo_code"),"warehouseId":"1"}

        response = Request('post',url=url,data=data,headers=self.headers,cookie=None)
        result = response.get_json()
        if result['status'] == 'OK':
            print("绑定成功")


    # 解绑摄像头跟仓库的关联
    def test_03_monitor_unbind(self):
        url = read_config(Public_mkdir).get("test_url","url") + "/admin/warehouse/monitor/unbind"
        data = {"id":mp_label().git_warehouse_monitor(1)[0]['id']}
        response = Request('post',url=url,data=data,headers=self.headers,cookie=None)
        result = response.get_json()
        self.assertEqual('OK',result['status'])



if __name__ == '__main__':
    unittest.main()
