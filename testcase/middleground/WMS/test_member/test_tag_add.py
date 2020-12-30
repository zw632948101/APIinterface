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
from testcase.middleground.WMS.case_data.member_data import member_data


@ddt
class member_tag(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = r"/world-passport/admin/sso/sms-login"
        cls.login = login(url=cls.url).test_login()
        cls.headers = {
            "_Device-Id_": read_config(Header_mkdir).get("header", "_device-id_"),
            "_Token_": read_config(Header_mkdir).get("header", "_token_"),
            "region": "online"
        }
    # 会员标签新增
    @data(*member_data().tag_add)
    def test_tag_add(self,case):
        url = read_config(Public_mkdir).get("test_url","member_url") + "/admin/tag/add"
        data = case['data']
        try:
            resp = Request('post',url=url,
                                 data=data,
                                 headers=self.headers,
                                 cookie=None)
        except Exception as e:
            raise e
        result = resp.get_json()
        self.assertEqual(case['expect'],result['status'])




if __name__ == '__main__':
    unittest.main()


