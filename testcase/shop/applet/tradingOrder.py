#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/11/3 15:51
# @Author: wei.zhang
# @File : tradingOrder.py
# @Software: PyCharm
from utils.log import log
import time
import random
import warnings
from interfaces.wxshop.MallAction import MallAction
#from testcase.middleground.sql.brandMP import mp_label as
from testcase.shop.sql.webMP import mp_label
from testcase.shop.caseData.applet_data import applet_api,submit_order
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest
import requests
import json
import random


class Centext:
    cartId = ''
    orderNo = ''


@ddt
class trading_order(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 数据库订单数-->接口请求前查出的
        cls.order_expect = len(mp_label().git_web_order())

    def setUp(self):
        """
        测试前数据准备
        :return:
        """
        self.api = MallAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')

    # 新增购物车
    @data(*applet_api().admin_web_cart_add)
    def test_1_web_cart_add(self, case):
        skuNo_ = mp_label().gti_web_cart_add2(True)[0]['code']
        shopId_ = mp_label().gti_web_cart_add2(False)[0]['id']
        amount_ = case['data']['amount']

        res = self.api._web_cart_add(skuNo_=skuNo_, shopId_=shopId_, amount_=amount_)
        self.assertEqual(case['expect'], res.get('status'))

    # 获取购物车列表
    def test_2_web_cart_list(self):
        res = self.api._web_cart_list()
        self.assertEqual('OK', res.get('status'))
        if res.get('status') == 'OK':
            result = res.get('content')[0]['cartList']
            # 获取到的购物车di 存起来
            setattr(Centext, 'cartId', random.choice(result)['cartId'])
    # 下单
    @data(*submit_order().web_order_submit_order)
    def test_3_admin_web_order_submit_order(self,case):
        shopId_ = 1 # 店铺id
        product_ = str([{"cartId":getattr(Centext,"cartId"),"skuNo":"10801010004","skuNum":1}]) # 商品信息
        addressId_ = 24 # 收货地址
        freight_ = 0 # 运费
        deliveryType_ = 1 # 运送方式
        productPrice_ = 1 # 商品总金额
        buyerMemo_ = "随便" # 买家备注
        res = self.api._web_order_submit_order(shopId_=shopId_, product_=product_,
                                           addressId_=addressId_, freight_=freight_,
                                           deliveryType_=deliveryType_, productPrice_=productPrice_,
                                           buyerMemo_=buyerMemo_)
        self.assertEqual(case['expect'], res.get('status'))
        # 数据库实际订单数-->接口请求之后查出的
        actual = len(mp_label().git_web_order())
        if res.get('status') == 'OK':
            # 参数依赖-->下单接口OK，orderNo参数值存起来，后续接口调用
            orderNo=res.get('content')['orderNo']
            setattr(Centext,'orderNo',orderNo)
            # 数据断言-->下单接口OK，数据库订单列表数据+1
            self.assertEqual(self.order_expect+1,actual)
        else:
            self.assertEqual(self.order_expect,actual)

    # 查看订单详情
    def test_4_admin_web_order_detail(self):
        res = self.api._web_order_detail(orderNo_=getattr(Centext,'orderNo'))
        self.assertEqual('OK',res.get('status'))
        if res.get('status') == 'OK':
            print("订单详情: %s"%res.get('content'))

    # 取消订单
    @data(*submit_order().web_order_close)
    def test_5_admin_web_order_close(self,case):
        pn_ = case['data']['pn']
        ps_ = case['data']['ps']
        orderNo_ = getattr(Centext,'orderNo') # 订单号
        reason_ = case['data']['reason'] # 关闭原因
        resp = self.api._web_order_close(pn_=pn_,ps_=ps_,orderNo_=orderNo_,reason_=reason_)
        self.assertEqual(case['expect'],resp.get('status'))
        # 如果取消成功，订单状态为"已取消"
        order_status = None
        for i in mp_label().git_web_order_close(orderNo_):
            order_status = i['order_status']
        if resp.get('status') == 'OK':
            self.assertEqual(100,order_status) # 取消订单成功，订单装order_status状态应为100
        else:
            self.assertEqual(10,order_status)  # 取消订单失败，订单装order_status状态应为10

if __name__ == '__main__':
    unittest.main()
