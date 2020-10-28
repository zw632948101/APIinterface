#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/10/27 17:31
# @Author: wei.zhang
# @File : tagManage.py
# @Software: PyCharm

from utils.log import log
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.goodsMP import mp_label
from utils import runlevel,timestamp
import unittest


class tagManage(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()

    @unittest.skipIf(runlevel(1), '主流程执行用例，设置等级为2时跳过该用例')
    def test_admin_label_add(self):
        """
        添加标签
        :return:
        """
        name = '测试标签'+str(timestamp.get_timestamp())
        _type = 1
        resp = self.api._admin_label_add(name_=name, type_=_type)
        self.assertEqual(resp.get('status'), 'OK', resp.get('errorMsg'))
        info = self.db.query_mp_label_info(label_name=name, label_type=_type)
        self.assertEqual(str(info[0].get('creator_id')), self.api.user.user_id)
