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
from ddt import data, ddt
from testcase.middleground.WMS.common.Http import Request





@ddt
class warehouse_add(unittest.TestCase):

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

        self.url = read_config(Public_mkdir).get("test_url","url")

    # @data(*warehouse_data().admin_warehouse_add)
    # def test_warehouse_add(self,case):
    #     url = read_config(Public_mkdir).get("test_url","url") + case['url']
    #     data = json.dumps(case['data'])
    #
    #     response = Request('post',url=url,data=data,headers=self.headers,cookie=None)
    #     result = response.get_json()
    #
    #     self.assertEqual(case['expect'],result['status'])
    #     if result['status'] == 'OK':
    #         pass
    #         # 接口请求成功，做数据库断言
    #     else:
    #         pass
    # 详情-附加属性
    @data(*warehouse_data().admin_warehouse_detail)
    def test_admin_warehouse_additional_detail(self,case):
        url = self.url + '/admin/warehouse/additional-detail'
        data = case['data']
        resp = Request('post',
                       url=url,
                       data=data,
                       headers=self.headers,
                       cookie=None)
        self.assertEqual(case['expect'],resp.get_json()['status'])
        if resp.get_json()['status'] == 'OK':
            pass
            #print(resp.get_json())
    @data(*warehouse_data().admin_warehouse_additional_update)
    def test_admin_warehouse_additional_update(self,case):
        url = self.url + '/admin/warehouse/additional-update'
        data = case['data']

        resp = Request('post',
                       url=url,
                       data=data,
                       headers=self.headers,
                       cookie=None)
        self.assertEqual(case['expect'],resp.get_json()['status'])
        if resp.get_json()['status'] == 'OK':
            pass
    # 仓库列表
    @data(*warehouse_data().admin_warehouse_list)
    def test_admin_warehouse_list(self,case):
        url = self.url + '/admin/warehouse/list'
        data = case['data']
        resp = Request('post',
                       url=url,
                       data=data,
                       headers=self.headers,
                       cookie=None)
        self.assertEqual(case['expect'],resp.get_json()['status'])
        if resp.get_json()['status'] == 'OK':
            pass

    # 分页列表
    @data(*warehouse_data().admin_warehouse_page_list)
    def test_admin_warehouse_page_list(self,case):
        url = self.url + '/admin/warehouse/page-list'
        data = case['data']
        resp = Request('post',url=url,data=data,headers=self.headers,cookie=None)
        self.assertEqual(case['expect'],resp.get_json()['status'])

    # 推送至erp
    @data(*warehouse_data().admin_warehouse_push_to_erp)
    def test_admin_warehouse_push_to_erp(self,case):
        url = self.url + '/admin/warehouse/push-to-erp'
        data = case['data']
        resp = Request('post',
                       url=url,
                       data=data,
                       headers=self.headers,
                       cookie=None)
        self.assertEqual(case['expect'],resp.get_json()['status'])


if __name__ == '__main__':
    unittest.main()




