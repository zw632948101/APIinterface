#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/11/10 18:10
# @Author: wei.zhang
# @File : supplier.py
# @Software: PyCharm
"""
供应商
"""
import json
from interfaces.middleground.AssetAction import assetAction
from testcase.middleground.sql.asstMpSQL import supplierSQL
from utils import runlevel, dataDispose, timestamp
from ddt import data, ddt
from faker import Faker
import unittest
import random


class supplierData(object):
    def __init__(self):
        super(supplierData, self).__init__()
        self.faker = Faker('zh_CN')

    def supplier_add_data(self):
        """
        添加供应商数据
        :return:
        """
        code = ['DNJT-%s' % random.randint(1, 9999), '#', None]
        name = ['大农集团', 12, None, '#']
        supplierTypeId = [1, -1, 0, '#', None]
        adderss = ['四川省成都市高新区软件园A区', None]
        contacts = ['张三', None, self.faker.text(17)]
        phone = ['+86 15388126072', None, 15388126072, self.faker.text(17)]
        business = [self.faker.text(100), None]
        dic = {'code': 'DNJT-6918', 'name': '大农集团', 'supplierTypeId': 1,
               'address': '四川省成都市高新区软件园A区', 'contacts': '张三',
               'phone': '+86 15388126072', 'business': 'None'}
        return dataDispose().inspect_name(data_dict=dic, code=code, name=name, supplierTypeId=supplierTypeId,
                                          adderss=adderss, contacts=contacts, phone=phone, business=business)


@ddt
class supplier(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = assetAction()
        self.api.set_user(mobile=15388126072)
        self.db = supplierSQL()
        self.faker = Faker('zh_CN')

    @unittest.skipIf(runlevel(1), '供应商-新建')
    def test_admin_supplier_add(self):
        """
        供应商-新建
        :return:
        """
        code = 'MS-%s' % random.randint(1, 9999)
        name = '苗叔'
        supplierTypeId = 6
        adderss = '四川省成都市高新区软件园A区'
        contacts = self.faker.name()
        phone = '15388126072'
        business = self.faker.text(200)
        resp = self.api._admin_supplier_add(code_=code, name_=name, supplierTypeId_=supplierTypeId,
                                            address_=adderss, contacts_=contacts, phone_=phone, business_=business)
        if resp.get('status') == 'OK':
            self.assertEqual(resp.get('status'), 'OK')
        else:
            self.assertEqual(resp.get('status'), 'ERROR')
            if resp.get('errorCode') == '11050151':
                self.assertEqual(resp.get('errorMsg'), '供应商代码重复')
            elif code is None:
                self.assertEqual(resp.get('errorMsg'), '供应商代码不能为空')
            elif len(code) > 10:
                self.assertEqual(resp.get('errorMsg'), '供应商代码超过限制长度(10)')
            elif len(name) > 16:
                self.assertEqual(resp.get('errorMsg'), '联系人超过限制长度(16)')
            elif name is None:
                self.assertEqual(resp.get('errorMsg'), '供应商名称不能为空')
            elif adderss is None:
                self.assertEqual(resp.get('errorMsg'), '供应商地址不能为空')
            elif contacts is None:
                self.assertEqual(resp.get('errorMsg'), '联系人不能为空')
            elif phone is None:
                self.assertEqual(resp.get('errorMsg'), '联系电话不能为空')
            elif business is None:
                self.assertEqual(resp.get('errorMsg'), '主营业务不能为空')
            elif supplierTypeId is None:
                self.assertEqual(resp.get('errorMsg'), '供应商类型id不能为空')
            elif resp.get('errorCode') == '11050003':
                self.assertIn('参数验证错误', resp.get('errorMsg'))
            else:
                self.assertEqual(resp.get('errorMsg'), '供应商代码超过限制长度(10)')

    @data(*supplierData().supplier_add_data())
    @unittest.skipIf(runlevel(1), '供应商-新建')
    def test_admin_supplier_add_check(self, dic):
        """
        供应商-新建
        :return:
        """
        code = dic.get('code')
        name = dic.get('name')
        supplierTypeId = dic.get('supplierTypeId')
        adderss = dic.get('adderss')
        contacts = dic.get('contacts')
        phone = dic.get('phone')
        business = dic.get('business')
        resp = self.api._admin_supplier_add(code_=code, name_=name, supplierTypeId_=supplierTypeId,
                                            address_=adderss, contacts_=contacts, phone_=phone, business_=business)
        if resp.get('status') == 'OK':
            self.assertEqual(resp.get('status'), 'OK')
        else:
            self.assertEqual(resp.get('status'), 'ERROR')
            if resp.get('errorCode') == '11050151':
                self.assertEqual(resp.get('errorMsg'), '供应商代码重复')
            elif name is None:
                self.assertEqual(resp.get('errorMsg'), '供应商名称不能为空')
            elif supplierTypeId is None:
                self.assertEqual(resp.get('errorMsg'), '供应商类型id不能为空')
            elif adderss is None:
                self.assertEqual(resp.get('errorMsg'), '供应商地址不能为空')
            elif code is None:
                self.assertEqual(resp.get('errorMsg'), '供应商代码不能为空')
            elif len(code) > 10:
                self.assertEqual(resp.get('errorMsg'), '供应商代码超过限制长度(10)')
            elif len(name) > 16:
                self.assertEqual(resp.get('errorMsg'), '联系人超过限制长度(16)')
            elif contacts is None:
                self.assertEqual(resp.get('errorMsg'), '联系人不能为空')
            elif phone is None:
                self.assertEqual(resp.get('errorMsg'), '联系电话不能为空')
            elif business is None:
                self.assertEqual(resp.get('errorMsg'), '主营业务不能为空')

            elif resp.get('errorCode') == '11050003':
                self.assertIn('参数验证错误', resp.get('errorMsg'))
            else:
                self.assertEqual(resp.get('errorMsg'), '供应商代码超过限制长度(10)')
