from utils.log import log
import time
import random
import warnings
from interfaces.wxshop.MallAction import MallAction
#from testcase.middleground.sql.brandMP import mp_label as
from testcase.shop.sql.webMP import mp_label
from testcase.shop.caseData.applet_data import applet_api
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest
import requests


# 先添加购物车--->获取购物车列表--->结算购物车
@ddt
class cartAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.id_list = None
        cls.token = None
        cls.shopping_id= None

    def setUp(self):
        """
        测试前数据准备
        :return:
        """
        self.api = MallAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')
    # 添加购物车
    @data(*applet_api().admin_web_cart_add)
    def test_web_cart_add(self,case):
        skuNo_ = case['data']['skuNo']
        shopId_ = case['data']['shopId']
        amount_ = case['data']['amount']
        res = self.api._web_cart_add(skuNo_=skuNo_,shopId_=shopId_,amount_=amount_)
        self.assertEqual(case['expect'],res.get('status'))
    # 获取购物车列表
    def test_web_cart_list(self):
#         url = "http://dev-gateway.worldfarm.com/wx-mall/web/cart/list"
#
#         header = {"Content-Type": "application/x-www-form-urlencoded",
#         "Accept": "application/json, text/plain, */*",
#         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4)"
#                       " AppleWebKit/537.36 (KHTML, like Gecko) "
#                       "Chrome/86.0.4240.111 Safari/537.36",
#         "_Device-Type_": "web",
#         "region": "online",
#         "Accept_Language": "zh",
#         "_Device-Id_":"cc4feebe419791332bbcff5e0fdf084a",
#         "_Token_": "eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJjYzRmZWViZTQxOTc5MTMzMmJiY2ZmNWUwZmRmMDg0YSIsImRldmljZUdyb3VwIjoiVVNFUiIsImlwIjoiMTkyLjE2OC44OS4xNzUiLCJpc3MiOiJaWVBfU1NPIiwidXNlciI6IntcImFjY291bnRUeXBlXCI6MjEsXCJhcHBJZFwiOlwiMTFcIixcImRldmljZVR5cGVcIjpcIkFORFJPSUQtVVNFUlwiLFwiaGVhZEltZ1wiOlwiaHR0cDovL3p5cC1mYXJtLTIub3NzLWFwLXNvdXRoZWFzdC0xLmFsaXl1bmNzLmNvbS9kYXRhL2ZjLXVzZXIvaGVhZEltZy8xNTkzNTgyNTM0ODAzLmpwZ1wiLFwiaWRcIjo2OTQsXCJuZXdcIjpmYWxzZSxcInBhc3N3b3JkXCI6XCI3Mzc1MzA0MWY3NzZiNjg0MjE0NmFlNTA0MTQ4NjBiMzdmMzY5Nzg2Njk4N2NiMGZcIixcInBob25lXCI6XCIxNTM4ODEyNjA3MlwiLFwic3RhdHVzXCI6MSxcInVzZXJOYW1lXCI6XCLlvKDkuInlkbXlkbXlkbVcIn0iLCJpYXQiOjE2MDQ3MTQxMDl9.l8Mf3c2JV8xPefzoorZi3qMk6Zphxpt5eSuH1ulMFz_3v15x5G0yVHDW_N6AjzkN2Ubac_f_YViu65yl7XI-lQ"
# }
        res = self.api._web_cart_list()
        self.assertEqual('OK',res.get('status'))
        # if res.get('status') == 'OK':
        #     resp = requests.post(url=url,headers = header)
        #     print("购物车列表: %s"%resp.json())

    #编辑购物车
    @data(*applet_api().admin_web_cart_edit_amount)
    def test_web_cart_edit_amount(self,case):
        id_ = case['data']['id']
        amount_ = case['data']['amount']
        res = self.api._web_cart_edit_amount(id_=id_,amount_=amount_)
        self.assertEqual(case['expect'],res.get('status'))
    # 购物车结算
    @data(*applet_api().admin_web_cart_balance)
    def test_web_cart_balance(self,case):
        id_ = case['data']['id']
        res = self.api._web_cart_balance(id_=id_)
        self.assertEqual(case['expect'],res.get('status'))

    # 直接购买
    @data(*applet_api().admin_web_cart_purchase)
    def test_web_cart_purchase(self,case):
        skuNo_ = case['data']['skuNo']
        shopId_ = case['data']['shopId']
        amount_ = case['data']['amount']
        res = self.api._web_cart_purchase(skuNo_=skuNo_,shopId_=shopId_,amount_=amount_)
        self.assertEqual('OK',res.get('status'))


if __name__ == '__main__':
    unittest.main()