#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/11/3 15:50
# @Author: wei.zhang
# @File : shoppingCart.py
# @Software: PyCharm
"""
小程序购物车模块接口测试用例
"""

from utils.log import log
from interfaces.wxshop.MallAction import MallAction
from testcase.shop.sql.appletWX import wx_applet_shoppingCart
from utils import runlevel, timestamp, conversion
from ddt import data, unpack, ddt
from faker import Faker
import unittest, random
import inspect


class CartData(object):
    def __init__(self):
        super(CartData, self).__init__()

    def inspect_name(self, data_dict, **kwargs):
        import copy
        add_data = []
        for k in kwargs.keys():
            for i in kwargs.get(k):
                cp_dict = copy.deepcopy(data_dict)
                cp_dict[k] = i
                add_data.append(cp_dict)
        return add_data

    def add_cart_data(self):
        """
        添加购物车测试数据
        :return:
        """
        skucode = ['T0101020001', 'T01010100001x', None, 1, '#']
        shopid = [1, -1, 0, 99, None, '#']
        amount = [1, 0, -1, 1000000, None, '#']
        adddict = {'skucode': 'T0101010001', 'shopid': '1', 'amount': 1}
        return self.inspect_name(data_dict=adddict, skucode=skucode, shopid=shopid, amount=amount)

    def edit_cart_data(self):
        """
        编辑购物车商品测试数据
        :return:
        """
        cartid = [4, 3, None, '#']
        amount = [1, 0, -1, 1000000, None, '#']
        adddict = {'cartid': '4', 'amount': 1}
        return self.inspect_name(data_dict=adddict, cartid=cartid, amount=amount)

    def del_cart_data(self):
        """
        删除购物车商品测试数据
        :return:
        """
        return [1, 4, None, '#']


@ddt
class Cart(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = MallAction()
        self.api.set_user(mobile=15388126072)
        self.db = wx_applet_shoppingCart()
        self.faker = Faker('zh_CN')

    @unittest.skipIf(runlevel(1), "小程序-购物车-添加购物车")
    def test_web_cart_add(self):
        """
        小程序-购物车-添加购物车
        :return:
        """
        dbinfo = random.choice(self.db.query_shop_all_sku())
        skuNo = dbinfo.get('code')
        shopId = dbinfo.get('id')
        amount = 1
        cartnum = self.db.query_add_cart_goods_num(userid=self.api.user.user_id, shopid=shopId, code=skuNo)
        if cartnum:
            cartnum = cartnum.get('amount')
        else:
            cartnum = 0
        response = self.api._web_cart_add(skuNo_=skuNo, shopId_=shopId, amount_=amount)
        self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))
        addnum = self.db.query_add_cart_goods_num(userid=self.api.user.user_id, shopid=shopId, code=skuNo)
        self.assertGreater(addnum.get('amount'), cartnum)

    @data(*CartData().add_cart_data())
    @unittest.skipIf(runlevel(3), "小程序-购物车-添加购物车")
    def test_web_cart_add_chcke(self, cartdict):
        """
        小程序-购物车-添加购物车
        :return:
        """
        skuNo = cartdict.get('skucode')
        shopId = cartdict.get('shopid')
        amount = cartdict.get('amount')
        cartnum = self.db.query_add_cart_goods_num(userid=self.api.user.user_id, shopid=shopId, code=skuNo)
        if cartnum:
            cartnum = cartnum.get('amount')
        else:
            cartnum = 0
        response = self.api._web_cart_add(skuNo_=skuNo, shopId_=shopId, amount_=amount)
        if response.get('status') == "OK":
            self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))
            addnum = self.db.query_add_cart_goods_num(userid=self.api.user.user_id, shopid=shopId, code=skuNo)
            self.assertGreater(addnum.get('amount'), cartnum)
        else:
            if response.get('errorCode') == "11010302":
                self.assertEqual(response.get('errorMsg'), '商品不存在，请检查商品信息', response.get('errorMsg'))
            elif shopId == '#' or amount == '#':
                self.assertIn('参数验证错误', response.get('errorMsg'))
            elif amount < 1:
                self.assertEqual(response.get('errorMsg'), '数量最小为1', response.get('errorMsg'))
            elif skuNo is None:
                self.assertEqual(response.get('errorMsg'), '商品编码不能为空', response.get('errorMsg'))
            elif shopId is None:
                self.assertEqual(response.get('errorMsg'), '店铺Id不能为空', response.get('errorMsg'))
            elif response.get('errorCode') == "11010003":
                self.assertEqual(response.get('errorMsg'), '店铺Id输入不正确', response.get('errorMsg'))
            elif response.get('errorCode') == "11010201":
                self.assertEqual(response.get('errorMsg'), '店铺不存在', response.get('errorMsg'))
            elif response.get('errorCode') == "11010305":
                self.assertEqual(response.get('errorMsg'), '追花族-蜂蜜-椴树蜜-500ml库存不足', response.get('errorMsg'))

    @unittest.skipIf(runlevel(2), "小程序-购物车 - 购物车列表")
    def test_web_cart_list(self):
        """
        小程序-购物车 - 购物车列表
        """
        response = self.api._web_cart_list()
        self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))
        productlist = self.db.query_cart_list_product(userid=self.api.user.user_id)
        shopidlist = conversion.data_assemble(key='shopId', parameters_ld=productlist)
        shopinfo = self.db.query_cart_list_shopinfo(shopid=shopidlist)
        cartinfo = []
        for shopi in shopinfo:
            carti = {"cartList": [], "shopInfo": shopi}
            for product in productlist:
                if product.get('shopId') == shopi.get('id'):
                    carti['cartList'].append(product)
            cartinfo.append(carti)
        content = sorted(response.get('content'))
        self.assertEqual(len(content), len(cartinfo))
        cartinfo = sorted(cartinfo)
        for i in range(len(content)):
            self.assertDictEqual(cartinfo[i], content[i])

    @unittest.skipIf(runlevel(1), "小程序-购物车 - 编辑购物车商品数量")
    def test_web_cart_edit_amount(self):
        """
        小程序-购物车 - 编辑购物车商品数量
        :return:
        """
        productlist = self.db.query_cart_list_product(userid=self.api.user.user_id)
        cartid = random.choice(productlist).get('cartId')
        amount = 10
        response = self.api._web_cart_edit_amount(id_=cartid, amount_=amount)
        self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))

    @data(*CartData().edit_cart_data())
    @unittest.skipIf(runlevel(3), "小程序-购物车 - 编辑购物车商品数量")
    def test_web_cart_edit_amount_check(self, cartdict):
        """
        小程序-购物车 - 编辑购物车商品数量
        :return:
        """
        cartid = cartdict.get('cartid')
        amount = cartdict.get('amount')
        response = self.api._web_cart_edit_amount(id_=cartid, amount_=amount)
        if response.get('status') == 'OK':
            self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))
        else:
            self.assertEqual(response.get('status'), 'ERROR')
            if response.get('errorCode') == '11010154':
                self.assertEqual(response.get('errorMsg'), '购物车操作权限不足')
            elif amount == '#' or cartid == '#':
                self.assertIn('参数验证错误', response.get('errorMsg'))
            elif amount is None:
                self.assertEqual(response.get('errorMsg'), '数量不能为空')
            elif amount < 1:
                self.assertEqual(response.get('errorMsg'), '数量最小为1')
            elif response.get('errorCode') == '11010003':
                self.assertEqual(response.get('errorMsg'), '购物车Id不能为空')
            elif response.get('errorCode') == '11010305':
                self.assertEqual(response.get('errorMsg'), '追花族-蜂蜜-椴树蜜-500ml库存不足')

    @unittest.skipIf(runlevel(3), "小程序-购物车 - 删除购物车商品")
    def test_web_cart_del(self):
        """
        小程序-购物车 - 删除购物车商品
        :return:
        """
        productlist = self.db.query_cart_list_product(userid=self.api.user.user_id)
        cartid = random.choice(productlist).get('cartId')
        response = self.api._web_cart_del(id_=cartid)
        self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))

    @data(*CartData().del_cart_data())
    @unittest.skipIf(runlevel(3), "小程序-购物车 - 删除购物车商品")
    def test_web_cart_del_check(self, cartid):
        """
        小程序-购物车 - 删除购物车商品
        :return:
        """
        response = self.api._web_cart_del(id_=cartid)
        if response.get('status') == 'OK':
            self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))
        else:
            self.assertEqual(response.get('status'), 'ERROR')
            if response.get('errorCode') == '11010151':
                self.assertEqual(response.get('errorMsg'), '购物车ID输入不合法')
            elif response.get('errorCode') == '11010003':
                self.assertEqual(response.get('errorMsg'), '购物车ID不能为空')
            elif response.get('errorCode') == '11010154':
                self.assertEqual(response.get('errorMsg'), '购物车操作权限不足')

    @unittest.skipIf(runlevel(1), "小程序-购物车 - 购物车结算")
    def test_web_cart_balance(self):
        """
        小程序-购物车 - 购物车结算
        :return:
        """
        productlist = self.db.query_cart_list_product(userid=self.api.user.user_id)
        cartid = random.choice(productlist).get('cartId')
        response = self.api._web_cart_balance(id_=cartid)
        self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))

    @data(*CartData().del_cart_data())
    @unittest.skipIf(runlevel(1), "小程序-购物车 - 购物车结算")
    def test_web_cart_balance_check(self, cartid):
        """
        小程序-购物车 - 购物车结算
        :return:
        """
        response = self.api._web_cart_balance(id_=cartid)
        self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))
