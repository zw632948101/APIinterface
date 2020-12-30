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
    @classmethod
    def setUpClass(cls):
        cls.skuNo_ = random.choice(mp_label().gti_web_cart_add2(True))['code']
        cls.shopId_ = random.choice(mp_label().gti_web_cart_add2(False))['id']
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
    @data(*applet_api().admin_web_cart_add)
    def test_1_web_cart_add(self,case):
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
            setattr(Centext,'cartId', random.choice(result)['cartId'])


    # 编辑购物车
    cart_edit_amount = [{'data':{"amount":"7"},'expect':'OK'},
                            {'data':{"amount":None},'expect':'ERROR'}
                            ]
    @data(*cart_edit_amount)
    def test_3_web_cart_edit_amount(self,case):
        id_ = getattr(Centext ,'cartId')
        amount_ = case['data']['amount']
        resp = self.api._web_cart_edit_amount(id_=id_,amount_=amount_)
        self.assertEqual(case['expect'],resp.get('status'))

    # 购物车结算
    def test_4_web_cart_balance(self):
        id_ = getattr(Centext,'cartId')
        resp = self.api._web_cart_balance(id_=id_)
        self.assertEqual('OK',resp.get('status'))
        #print("结算id： %s"%id_)
    # 再次购买
    @data(*applet_api().admin_web_cart_buy_again)
    def test_5_web_cart_buy_again(self,case):
        product_ = str(case['data']['product'])
        shopId_ = case['data']['shopId']
        resp = self.api._web_cart_buy_again(product_=product_, shopId_=shopId_)
        self.assertEqual(case['expect'],resp.get('status'))
        if resp.get('status') == 'OK':
            result = self.api._web_cart_list()
            res = result.get('content')[0]['cartList']
            # print("再次购买，生成的购物车id",res)
            setattr(Centext, 'cartId', res[0]['cartId'])
        else:
            pass
    # 删除购物车
    def test_6_web_cart_del(self):
        resp = self.api._web_cart_del(id_=getattr(Centext, 'cartId'))
        self.assertEqual('OK',resp.get('status'))







    # # 确认下单
    # @data(*submit_order().web_order_submit_order)
    # def test_3_admin_web_order_submit_order(self,datas):
    #     shopId_ = datas['data']['shopId']
    #     product_ = str([{"cartId":getattr(Centext,'cartId'),"skuNo":mp_label().gti_web_cart_add2(True)[0]['code'],"skuNum":"3"}])
    #     addressId_ = datas['data']['addressId']
    #     freight_ = datas['data']['freight']
    #     deliveryType_ = datas['data']['deliveryType']
    #     productPrice_ = datas['data']['productPrice']
    #     buyerMemo_ = datas['data']['buyerMemo']
    #     res = self.api._web_order_submit_order(shopId_=shopId_, product_=product_,
    #                                            addressId_=addressId_, freight_=freight_,
    #                                            deliveryType_=deliveryType_, productPrice_=productPrice_,
    #                                            buyerMemo_=buyerMemo_)
    #     self.assertEqual(datas['expect'], res.get('status'))
    #     if res.get('status') == 'OK':
    #         orderNo=res.get('content')['orderNo']# 订单号存起来
    #         setattr(Centext,'orderNo',orderNo)
    #         # 断言-->订单新增成功，订单详情应该与下单时信息匹配，则PASS
    #
    # # 查看订单详情
    # def test_4_admin_web_order_detail(self):
    #
    #     res = self.api._web_order_detail(orderNo_=getattr(Centext,'orderNo'))
    #     self.assertEqual('OK',res.get('status'))

if __name__ == '__main__':
    unittest.main()
