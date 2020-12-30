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

@ddt
class warehouse_monitor_raname(unittest.TestCase):
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
    @data(*warehouse_data().admin_wraehouse_rename)
    def test_admin_warehouse_monitor_raname(self,case):
        url = read_config(Public_mkdir).get("test_url","url") + "/admin/warehouse/monitor/rename"
        data = {"id":mp_label().git_warehouse_monitor_is_delete()[0]['id'],"name":case['data']['name']}

        response = Request('post',
                           url=url,
                           data=data,
                           headers=self.headers,
                           cookie=None)
        result = response.get_json()
        self.assertEqual(case['expect'],result['status'])

        if result['status'] == 'OK':
            # 修复接口成功，数据库中的名字，跟接口传递的名字一致
            actual = mp_label().git_warehouse_monitor_is_delete()[0]['name']
            self.assertEqual(data['name'],actual)
        else:

            actual = mp_label().git_warehouse_monitor_is_delete()[0]['name']
            self.assertNotEqual(data['name'],actual)
    @data(*warehouse_data().admin_warehouse_monitor_list)
    def test_admin_warehouse_monitor_list(self,case):
        url = read_config(Public_mkdir).get("test_url","url") + "/admin/warehouse/monitor/list"
        data = case['data']
        resphonse = Request('post',
                            url=url,
                            data=data,
                            headers=self.headers,
                            cookie=None)
        result = resphonse.get_json()
        self.assertEqual(case['expect'],result['status'])
        if result['status'] == 'ERROR':
            print(result['errorMsg'])

if __name__ == '__main__':
    unittest.main()