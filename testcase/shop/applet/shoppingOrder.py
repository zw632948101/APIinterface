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
class shopping_order(unittest.TestCase):


    def setUp(self):
        """
        测试前数据准备
        :return:
        """
        self.api = MallAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')

    #新增购物车
    def test_1_web_cart_add(self):
        skuNo_ = "Z0101010003"
        shopId_ = 1
        amount_ = 14
        res = self.api._web_cart_add(skuNo_=skuNo_, shopId_=shopId_, amount_=amount_)
        self.assertEqual('OK', res.get('status'))
    # 获取购物车列表
    def test_2_web_cart_list(self):
        res = self.api._web_cart_list()
        self.assertEqual('OK', res.get('status'))
        if res.get('status') == 'OK':
            result = res.get('content')[0]['cartList']
            # 获取到的购物车di 存起来
            setattr(Centext,'cartId', random.choice(result)['cartId'])

    # 确认下单
    @data(*submit_order().web_order_submit_order)
    def test_3_admin_web_order_submit_order(self,case):
        shopId_ = case['data']['shopId']
        product_ = str([{"cartId":getattr(Centext,'cartId'),"skuNo":"Z0101010003","skuNum":"3"}])
        addressId_ = case['data']['addressId']
        freight_ = case['data']['freight']
        deliveryType_ = case['data']['deliveryType']
        productPrice_ = case['data']['productPrice']
        buyerMemo_ = case['data']['buyerMemo']
        res = self.api._web_order_submit_order(shopId_=shopId_, product_=product_,
                                               addressId_=addressId_, freight_=freight_,
                                               deliveryType_=deliveryType_, productPrice_=productPrice_,
                                               buyerMemo_=buyerMemo_)
        self.assertEqual(case['expect'], res.get('status'))
        if res.get('status') == 'OK':
            orderNo=res.get('content')['orderNo']# 订单号存起来
            setattr(Centext,'orderNo',orderNo)
            # 断言-->订单新增成功，订单详情应该与下单时信息匹配，则PASS

    # 查看订单详情
    def test_4_admin_web_order_detail(self):

        res = self.api._web_order_detail(orderNo_=getattr(Centext,'orderNo'))
        self.assertEqual('OK',res.get('status'))

if __name__ == '__main__':
    unittest.main()
