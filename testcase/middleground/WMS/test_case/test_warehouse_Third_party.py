#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import unittest
import json
from testcase.middleground.WMS.prepare.login import login
from testcase.middleground.WMS.common.Pash import Header_mkdir # 存放header值得配置文件
from testcase.middleground.WMS.common.Pash import Public_mkdir
from testcase.middleground.WMS.common.config import read_config
from testcase.middleground.WMS.datas.warehouse_data import warehouse_data
from testcase.middleground.WMS.common.Mysql import mp_label
from interfaces.middleground.Wms_apiAction import wms_apiAction
from ddt import data, ddt
from testcase.middleground.WMS.common.Http import Request

@ddt
class wraehouse_third_party(unittest.TestCase):
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
        self.url = read_config(Public_mkdir).get("test_url", "url")
    @data(*warehouse_data().admin_wraehouse_employee_add)
    def test_admin_warehouse_employee_add(self,case):
        url = self.url + '/admin/warehouse/employee/add'
        data = case['data']
        try:
            resp = Request('post',
                           url=url,
                           data=data,
                           headers=self.headers,
                           cookie=None)
        except Exception as e:
            raise e
        self.assertEqual(case['expect'],resp.get_json()['status'])
        if resp.get_json()['status'] == 'OK':
            pass

    @data(*warehouse_data().admin_wraehouse_employee_del)
    def test_admin_warehouse_employee_del(self,case):
        url = self.url + '/admin/warehouse/employee/del'
        data = case['data']
        try:
            resp = Request('post',
                           url=url,
                           data=data,
                           headers=self.headers,
                           cookie=None)
        except Exception as e:
            raise e
        self.assertEqual(case['expect'],resp.get_json()['status'])
    @data(*warehouse_data().admin_wraehouse_employee_list)
    def test_admin_warehouse_employee_list(self,case):
        url = self.url + '/admin/warehouse/employee/list'
        data = case['data']
        try:
            resp = Request('post',
                           url=url,
                           data=data,
                           headers=self.headers,
                           cookie=None)
        except Exception as e:
            raise e
        self.assertEqual(case['expect'],resp.get_json()['status'])

if __name__ == '__main__':
    unittest.main()