#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/11/3 15:54
# @Author: wei.zhang
# @File : evaluate.py
# @Software: PyCharm

from utils.log import log
from interfaces.wxshop.MallAction import MallAction
from testcase.shop.sql.appletWX import wx_applet_evaluate
from testcase.shop.caseData.applet_data import submit_order
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest
import inspect


@ddt
class add_evaluate(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = MallAction()
        self.api.set_user(mobile=15388126072)
        self.db = wx_applet_evaluate()
        self.faker = Faker('zh_CN')

    @data(*submit_order().web_mobile_evaluate_order_add)
    def test_add_evaluate(self):
        self.api._mobile_evaluate_order_add_( orderNo_=None,
                                              comment_=None,
                                              totalScore_=None,
                                              serviceScore_=None,
                                              logisticsScore_=None,
                                              productScore_=None)




