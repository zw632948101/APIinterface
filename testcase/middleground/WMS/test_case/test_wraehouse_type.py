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

class wraehouse_type(unittest.TestCase):
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
    def test_admin_warehouse_type_count(self):
        url = read_config(Public_mkdir).get("test_url","url") + "/admin/warehouse/type/count"
        data = None
        resphonse = Request('post',url=url,data=data,headers=self.headers,cookie=None)


    def test_admin_warehouse_type_list(self):
        pass


    def test_admin_warehouse_type_page_list(self):
        pass





























