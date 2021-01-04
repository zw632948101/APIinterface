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
from utils import runlevel, dataDispose, timestamp, FakeLocation
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
        return dataDispose().inspect_name(data_dict=dic, code=code, name=name,
                                          supplierTypeId=supplierTypeId,
                                          adderss=adderss, contacts=contacts, phone=phone,
                                          business=business)


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
        province, city, county, address, lng, lat = FakeLocation().fake_location()
        SupplierInput = {
            "address": address,
            "business": self.faker.text(200),
            "city": city,
            "contacts": self.faker.name(),
            "county": county,
            "lat": lat,
            "lng": lng,
            "name": self.faker.company(),
            "phone": self.faker.phone_number(),
            "province": province,
            "remark": self.faker.text(200),
            "sku": [
                {
                    "skuCode": "T0101010005",
                    "unitPrice": 1
                }
            ],
            "supplierExtInput": {
                "bankAccount": self.faker.credit_card_number(),
                "businessEndDate": timestamp.str_time_timestamp("2021-05-21", formats="%Y-%m-%d"),
                "businessStartDate": timestamp.str_time_timestamp("2019-05-21", formats="%Y-%m-%d"),
                "companyType": {
                    "dictCode": "company",
                    "dictKey": "1"
                },
                "corporation": self.faker.name(),
                "establishDate": timestamp.str_time_timestamp("2018-05-21", formats="%Y-%m-%d"),
                "invoice": 1,
                "qualifyMaterials": [
                    {
                        "effectiveDate": 1008662713,
                        "expirationDate": 1608278713,
                        "imageUrls": "https://dnkj-mp-asset-prod.oss-cn-beijing.aliyuncs.com/data/dev/mp-asset/1604562219313.jpg",
                        "qualifyName": "公司营业执照"
                    }
                ],
                "realName": self.faker.name(),
                "registBankName": "中国银行",
                "registMoney": self.faker.numerify(),
                "returnAddress": self.faker.address(),
                "socialCode": self.faker.credit_card_number(),
                "taxRate": {
                    "dictCode": "tax-rate",
                    "dictKey": "13"
                }
            },
            "supplierType": {
                "dictCode": "supplier",
                "dictKey": "105"
            }
        }
        resp = self.api._admin_supplier_add(input_=SupplierInput)
        if resp.get('status') == 'OK':
            self.assertEqual(resp.get('status'), 'OK')
        else:
            errorCode = ['11050151', '11050003']
            errorMsg = ['供应商代码重复', '供应商代码不能为空', '供应商代码超过限制长度(10)', '联系人超过限制长度(16)', '供应商名称不能为空',
                        '供应商地址不能为空', '联系人不能为空', '联系电话不能为空', '主营业务不能为空', '供应商类型id不能为空',
                        '供应商代码超过限制长度(10)']
            self.assertEqual(resp.get('status'), 'ERROR')
            self.assertIn(resp.get('errorCode'), errorCode)
            self.assertIn(resp.get('errorMsg'), errorMsg)

    @unittest.skipIf(runlevel(1), '供应商-编辑')
    def test_admin_supplier_edit(self):
        """
        供应商-编辑
        :return:
        """
        dbinfo = random.choice(self.db.query_asset_supplier())
        province, city, county, address, lng, lat = FakeLocation().fake_location()
        SupplierInput = {
            "address": address,
            "business": self.faker.text(200),
            "city": city,
            "id": dbinfo.get('id'),
            "contacts": self.faker.name(),
            "county": county,
            "lat": lat,
            "lng": lng,
            "name": self.faker.company(),
            "phone": self.faker.phone_number(),
            "province": province,
            "remark": self.faker.text(200),
            "sku": [
                {
                    "skuCode": "T0101010005",
                    "unitPrice": 1
                }
            ],
            "supplierExtInput": {
                "bankAccount": self.faker.credit_card_number(),
                "businessEndDate": timestamp.str_time_timestamp("2021-05-21", formats="%Y-%m-%d"),
                "businessStartDate": timestamp.str_time_timestamp("2019-05-21", formats="%Y-%m-%d"),
                "companyType": {
                    "dictCode": "company",
                    "dictKey": "1"
                },
                "corporation": self.faker.name(),
                "establishDate": timestamp.str_time_timestamp("2018-05-21", formats="%Y-%m-%d"),
                "invoice": 1,
                "qualifyMaterials": [
                    {
                        "effectiveDate": 1008662713,
                        "expirationDate": 1608278713,
                        "imageUrls": "https://dnkj-mp-asset-prod.oss-cn-beijing.aliyuncs.com/data/dev/mp-asset/1604562219313.jpg",
                        "qualifyName": "公司营业执照"
                    }
                ],
                "realName": self.faker.name(),
                "registBankName": "中国银行",
                "registMoney": self.faker.numerify(),
                "returnAddress": self.faker.address(),
                "socialCode": self.faker.credit_card_number(),
                "taxRate": {
                    "dictCode": "tax-rate",
                    "dictKey": "1"
                }
            },
            "supplierType": {
                "dictCode": "supplier",
                "dictKey": "104"
            }
        }
        resp = self.api._admin_supplier_edit(input_=SupplierInput)
        if resp.get('status') == 'OK':
            self.assertEqual(resp.get('status'), 'OK')
        else:
            errorCode = ['11050151', '11050003']
            errorMsg = ['供应商代码重复', '供应商代码不能为空', '供应商代码超过限制长度(10)', '联系人超过限制长度(16)', '供应商名称不能为空',
                        '供应商地址不能为空', '联系人不能为空', '联系电话不能为空', '主营业务不能为空', '供应商类型id不能为空',
                        '供应商代码超过限制长度(10)']
            self.assertEqual(resp.get('status'), 'ERROR')
            self.assertIn(resp.get('errorCode'), errorCode)
            self.assertIn(resp.get('errorMsg'), errorMsg)

    def test_admin_supplier_page(self):
        """
        供应商接口
        :return:
        """
        datas = {"ps": 10, "pn": 1, "supplierType": {"dictCode": "supplier", "dictKey": "104"}}
        self.api._admin_supplier_page(input_=datas)

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
                                            address_=adderss, contacts_=contacts, phone_=phone,
                                            business_=business)
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
