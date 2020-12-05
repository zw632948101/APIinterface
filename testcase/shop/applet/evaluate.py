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
from testcase.shop.sql.webMP import mp_label
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest
import inspect
import json


@ddt
class add_evaluate(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 查出可评价订单
        cls.orderNo = mp_label().git_web_order_evaluate('蜂友708528')[0]['order_no']
        # 接口请求前，查一次评价审核状态
        global expect
        cls.expect = mp_label().git_web_order_product_evaluate()[0]['status']
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
    def test_add_evaluate(self,case):
        orderNo_ = self.orderNo
        serviceScore_ = case['data']['serviceScore']
        logisticsScore_ = case['data']['logisticsScore']
        productEvaluateJson_ = json.dumps(case['data']['productEvaluateJson'])
        resp = self.api._web_evaluate_add( orderNo_=orderNo_,
                                              serviceScore_=serviceScore_,
                                              logisticsScore_=logisticsScore_,
                                              productEvaluateJson_=productEvaluateJson_,
                                            )
        self.assertEqual(case['expect'],resp.get('status'))
        print("传入的订单号: ",orderNo_)
        if resp.get('status') == 'OK':
            # 评论成功，订单状态应为60
            self.assertEqual(mp_label().git_web_order_status(True,self.orderNo)[0]['order_status'] , 60)
        else:
            pass
    # 审核评价
    @data(*submit_order().web_mobile_evaluate_order_audit)
    def test_admin_evaluate_audit(self,case):
        evaluateNo = mp_label().git_web_order_product_evaluate()[0]['evaluate_no']
        status = case['data']['status']
        resp = self.api._admin_evaluate_audit(evaluateNo_=evaluateNo,
                                              status_=status)
        self.assertEqual(case['expect'],resp.get('status'))
    def test_admin_evaluate_list(self):
        pn_ = 1
        ps_ = 10
        contentStatus_ = 2
        resp = self.api._admin_evaluate_list(pn_=pn_, ps_=ps_, contentStatus_=contentStatus_)
        self.assertEqual('OK',resp.get('status'))

    # 回复评价
    @data(*submit_order().web_mobile_evaluate_order_reply)
    def test_admin_evaluate_reply(self,case):
        evaluateNo_ = '4020120410530693018096'
        comment_ = case['data']['comment']
        replyEvaluateNo_ = None
        resp = self.api._admin_evaluate_reply(evaluateNo_=evaluateNo_, comment_=comment_, replyEvaluateNo_=None)
        self.assertEqual('OK',resp.get('status'))


    # 最后还原已评价的订单状态为50，便于下次测试订单评价
    @classmethod
    def tearDownClass(cls):
        mp_label().git_web_order_status(False,order_no=cls.orderNo)

if __name__ == '__main__':
    unittest.main()
