#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/11/9 10:40
# @Author: wei.zhang
# @File : product.py
# @Software: PyCharm
"""
资产产品用例
"""
import json

from interfaces.middleground.AssetAction import assetAction
from testcase.middleground.sql.asstMpSQL import productSQL
from utils import runlevel, dataDispose, conversion
from ddt import data, ddt
from faker import Faker
import unittest
import random


class productData(object):
    def __init__(self):
        super(productData, self).__init__()
        self.faker = Faker('zh_CN')

    def inspect_name(self, data_dict, **kwargs):
        import copy
        add_data = []
        for k in kwargs.keys():
            for i in kwargs.get(k):
                cp_dict = copy.deepcopy(data_dict)
                cp_dict[k] = i
                add_data.append(cp_dict)
        return add_data

    def product_add_data(self):
        """
        添加资产产品类型数据
        :return:
        """
        typeId = [1, 4, 0, -1, None, '#']
        code = ['QJX-%s' % random.randint(1, 999999), 'QJX-123456789101112141315', None, '#%^', 123]
        name = [self.faker.name(), '浅继箱', self.faker.text(20), None, '#$%', 123]
        unit = ['个', self.faker.text(20), self.faker.text(20), None, '@$$', 123]
        desc = [self.faker.text(50), self.faker.text(51), None, 123]
        attrName = [self.faker.text(20), self.faker.text(50), None, 123]
        attrs_dict = {'attrName': '数量', 'unit': '个', 'type': '2'}
        add_dict = {'typeId': 2, 'code': random.randint, 'name': self.faker.name,
                    'unit': '个', 'desc': self.faker.text(20),
                    'attrs': {'attrName': '数量', 'unit': '个', 'type': '2'}}
        attrs = self.inspect_name(data_dict=attrs_dict, unit=unit, type=typeId, attrName=attrName)
        attrs.append(None)
        attrs.append(123)
        return self.inspect_name(data_dict=add_dict, typeId=typeId, code=code, name=name, unit=unit,
                                 desc=desc, attrs=attrs)

    def get_attr_data(self):
        """
        资产属性
        :return:
        """
        return [0, 18, None, '#']

    def get_list_page_data(self):
        """
        资产产品-分页列表测试数据
        :return:
        """
        pn = [1, None]
        ps = [1, 15, None]
        typeId = [0, 1, None, '-1', '#']
        code = ['QJX_18636', 'Q', 1, None, '#']
        name = ['王', 'dfs', 12, None, '#']
        pagedata = {'pn': None, 'ps': None, 'typeId': None, 'code': None, 'name': None}
        pdata = dataDispose().recursion_dispose_data_dict(dic=pagedata, pn=pn, ps=ps, typeId=typeId,
                                                          code=code, name=name)
        return pdata

    def detail_data(self):
        """
        资产产品详情请求传参字段
        :return:
        """
        return [0, -1, None, '#']


@ddt
class codeBase(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = assetAction()
        self.api.set_user(mobile=15388126072)
        self.db = productSQL()
        self.faker = Faker('zh_CN')

    @unittest.skipIf(runlevel(1), '资产产品-新建')
    def test_admin_product_add(self):
        """
        资产产品-新建 涉及ERP同步
        :return:
        """
        productT = random.choice(self.db.query_product_type_id())
        typeId = productT.get('id')  # 产品类型id
        code = str(productT.get('prefix')) + str(random.randint(1, 9999))  # 代码库编码
        name = '世界农场设备' + str(random.randint(1, 9999))  # 资产名称
        unit = '台'  # 单位
        desc = self.faker.text(50)  # 资产说明
        attrs = json.dumps([{'attrName': '数量', 'unit': '台', 'type': '1'}])  # 资产属性集合
        response = self.api._admin_product_add(typeId_=typeId, code_=code, name_=name, unit_=unit,
                                               desc_=desc, attrs_=attrs)
        if response.get('status') == 'OK':
            self.assertEqual(response.get('status'), 'OK')
            dbinfo = self.db.query_prodcut_parameter_info(code=code, name=name, unit=unit,
                                                          typeid=typeId)
            self.assertEqual(len(dbinfo), 1)
        else:
            codelist = ['11050055', '11050065', '11050001', '11050003', '11050052', '10020020']
            errorMsg = ['该类资产不存在', '产品类型id不能为空', '资产名称不能为空', '资产名称重复,不能重复添加', '资产代码重复,不能重复添加',
                        '单位不能为空', '编码必须是字母或字母+数字',
                        "Your account is logged on on another device, and you are forced to go offline."]
            self.assertIn(response.get('errorCode'), codelist)
            self.assertIn(response.get('errorMsg'), errorMsg)

    @data(*productData().product_add_data())
    @unittest.skipIf(runlevel(3), '资产产品-新建')
    def test_admin_product_add_check(self, adict):
        """
        资产产品-新建
        :return:
        """
        typeId = adict.get('typeId')
        code = adict.get('code') if isinstance(adict.get('code'),
                                               str) else 'QJX_%s' % random.randint(1, 99999)
        name = adict.get('name') if isinstance(adict.get('name'), str) else self.faker.name()
        unit = adict.get('unit')
        desc = adict.get('desc')
        attrs = json.dumps([adict.get('attrs')])
        response = self.api._admin_product_add(typeId_=typeId, code_=code, name_=name, unit_=unit,
                                               desc_=desc, attrs_=attrs)
        if response.get('status') == 'OK':
            self.assertEqual(response.get('status'), 'OK')
        else:
            codelist = ['11050055', '11050065', '11050001', '11050003', '11050052', '10020020']
            errorMsg = ['该类资产不存在', '产品类型id不能为空', '资产名称不能为空', '资产名称重复,不能重复添加', '资产代码重复,不能重复添加',
                        '单位不能为空', '编码必须是字母或字母+数字',
                        "Your account is logged on on another device, and you are forced to go offline."]
            self.assertIn(response.get('errorCode'), codelist)
            self.assertIn(response.get('errorMsg'), errorMsg)

    @unittest.skipIf(runlevel(1), '资产产品-获取资产属性')
    def test_admin_product_get_product_attr(self):
        """
        资产产品-获取资产属性
        :return:
        """
        dbinfo = random.choice(self.db.query_product_info())
        id = dbinfo.get('id')
        response = self.api._admin_product_get_product_attr(id_=id)
        self.assertEqual(response.get('status'), 'OK')
        typeinfo = self.db.query_product_type_info(pid=id)
        content = response.get('content')
        self.assertEqual(len(typeinfo), len(content))
        for i in range(len(content)):
            self.assertDictEqual(typeinfo[i], content[i])

    @data(*productData().get_attr_data())
    @unittest.skipIf(runlevel(3), '资产产品-获取资产属性')
    def test_admin_product_get_product_attr_check(self, id):
        """
        资产产品-获取资产属性
        :return:
        """
        response = self.api._admin_product_get_product_attr(id_=id)
        if response.get('status') == 'OK':
            self.assertEqual(response.get('status'), 'OK')
            typeinfo = self.db.query_product_type_info(pid=id)
            content = response.get('content')
            self.assertEqual(len(typeinfo), len(content))
            for i in range(len(content)):
                self.assertDictEqual(typeinfo[i], content[i])
        else:
            self.assertEqual(response.get('status'), 'ERROR')
            if response.get('errorCode') == '11050052':
                self.assertEqual(response.get('errorMsg'), '该类资产不存在')
            elif response.get('errorCode') == '11050001':
                self.assertEqual(response.get('errorMsg'), '系统繁忙，请稍后再试')

    @unittest.skipIf(runlevel(1), '资产产品-分页列表')
    def test_admin_product_list_page(self):
        """
        资产产品-分页列表
        :return:
        """
        pn = None
        ps = None
        typeId = None
        code = None
        name = None
        response = self.api._admin_product_list_page(pn_=pn, ps_=ps, typeId_=typeId, code_=code,
                                                     name_=name)
        self.assertEqual(response.get('status'), 'OK')
        dbinfo = self.db.query_product_list_page(pn=pn, ps=ps, name=name, typeid=typeId, code=code)
        for i in range(len(dbinfo)):
            typeinfo = self.db.query_product_type_info(pid=dbinfo[i].get('id'))
            typeinfo = conversion.del_dict_value_null(list(typeinfo))
            dbinfo[i]['attrs'] = typeinfo
        datas = response.get('content').get('datas')
        self.assertEqual(len(datas), len(dbinfo))
        for i in range(len(datas)):
            self.assertDictEqual(datas[i], dbinfo[i])

    @data(*productData().get_list_page_data())
    @unittest.skipIf(runlevel(3), '资产产品-分页列表')
    def test_admin_product_list_page_check(self, dic):
        """
        资产产品-分页列表
        :return:
        """
        pn = dic.get('pn')
        ps = dic.get('ps')
        typeId = dic.get('typeId')
        code = dic.get('code')
        name = dic.get('name')
        response = self.api._admin_product_list_page(pn_=pn, ps_=ps, typeId_=typeId, code_=code,
                                                     name_=name)
        if response.get('status') == 'OK':
            self.assertEqual(response.get('status'), 'OK')
            dbinfo = self.db.query_product_list_page(pn=pn, ps=ps, name=name, typeid=typeId,
                                                     code=code)
            for i in range(len(dbinfo)):
                typeinfo = self.db.query_product_type_info(pid=dbinfo[i].get('id'))
                typeinfo = conversion.del_dict_value_null(list(typeinfo))
                dbinfo[i]['attrs'] = list(typeinfo)
            datas = response.get('content').get('datas')
            self.assertEqual(len(datas), len(dbinfo))
            for i in range(len(datas)):
                self.assertDictEqual(datas[i], dbinfo[i])
        else:
            self.assertEqual(response.get('status'), 'ERROR')
            if response.get('errorCode') == '11050003':
                self.assertIn('参数验证错误', response.get('errorMsg'))
            else:
                self.assertIn('参数验证错误', response.get('errorMsg'))

    @unittest.skipIf(runlevel(1), '资产产品-详情')
    def test_admin_product_detail(self):
        """
        资产产品-详情
        :return:
        """
        dbinfo = random.choice(self.db.query_product_info())
        prid = dbinfo.get('id')
        response = self.api._admin_product_detail(id_=prid)
        self.assertEqual(response.get('status'), 'OK')
        dbinfo = self.db.query_product_list_page(productid=prid)
        for i in range(len(dbinfo)):
            typeinfo = self.db.query_product_type_info(pid=dbinfo[i].get('id'))
            typeinfo = conversion.del_dict_value_null(list(typeinfo))
            dbinfo[i]['attrs'] = typeinfo
        content = response.get('content')
        for i in range(len(content)):
            self.assertDictEqual(content[i], dbinfo[i])

    @unittest.skipIf(runlevel(3), '资产产品-详情')
    @data(*productData().detail_data())
    def test_admin_product_detail_check(self, prid):
        """
        资产产品-详情
        :return:
        """
        response = self.api._admin_product_detail(id_=prid)
        if response.get('status') == 'OK':
            self.assertEqual(response.get('status'), 'OK')
            dbinfo = self.db.query_product_list_page(productid=prid)
            for i in range(len(dbinfo)):
                typeinfo = self.db.query_product_type_info(pid=dbinfo[i].get('id'))
                typeinfo = conversion.del_dict_value_null(list(typeinfo))
                dbinfo[i]['attrs'] = typeinfo
            content = response.get('content')
            for i in range(len(content)):
                self.assertDictEqual(content[i], dbinfo[i])
        else:
            self.assertEqual(response.get('status'), 'ERROR')
            if response.get('errorCode') == '11050052':
                self.assertEqual(response.get('errorMsg'), "该类资产不存在")
            else:
                self.assertEqual(response.get('errorMsg'), "系统繁忙，请稍后再试")

    @unittest.skipIf(runlevel(6), '资产-使用轨迹分页列表')
    def test_admin_product_type_list(self):
        """
        资产-使用轨迹分页列表-不在使用
        :return:
        """
        response = self.api._admin_product_type_list()
        self.assertEqual(response.get('status'), 'OK')

    @unittest.skipIf(runlevel(1), '资产产品-产品列表下拉框')
    def test_admin_product_list(self):
        """
        资产产品-产品列表下拉框
        :return:
        """
        response = self.api._admin_product_list()
        self.assertEqual(response.get('status'), 'OK')
        dbinfo = self.db.query_admin_product_list()
        content = response.get('content')
        for i in range(len((content))):
            self.assertDictEqual(dbinfo[i], content[i])

    @unittest.skipIf(runlevel(1), '资产产品-编辑')
    def test_admin_product_edit(self):
        """
        资产产品-编辑 涉及ERP同步
        :return:
        """
        pid_info = random.choice(self.db.query_product_info())
        pid = pid_info.get('id')
        productT = random.choice(self.db.query_product_type_id())
        typeId = productT.get('id')  # 产品类型id
        code = str(productT.get('prefix')) + str(random.randint(1, 9999))  # 代码库编码
        name = '世界农场设备' + str(random.randint(1, 9999))  # 资产名称
        unit = '台'  # 单位
        desc = self.faker.text(50)  # 资产说明
        attrs = json.dumps([{'attrName': '数量', 'unit': '台', 'type': '1'}])  # 资产属性集合
        response = self.api._admin_product_edit(id_=pid, typeId_=typeId, code_=code, name_=name,
                                                unit_=unit, desc_=desc, attrs_=attrs)
        if response.get('status') == 'OK':
            self.assertEqual(response.get('status'), 'OK')
            dbinfo = self.db.query_prodcut_parameter_info(code=code, name=name, unit=unit,
                                                          typeid=typeId)
            self.assertEqual(len(dbinfo), 1)
        else:
            codelist = ['11050055', '11050065', '11050001', '11050003', '11050052', '10020020']
            errorMsg = ['该类资产不存在', '产品类型id不能为空', '资产名称不能为空', '资产名称重复,不能重复添加', '资产代码重复,不能重复添加',
                        '单位不能为空', '编码必须是字母或字母+数字',
                        "Your account is logged on on another device, and you are forced to go offline."]
            self.assertIn(response.get('errorCode'), codelist)
            self.assertIn(response.get('errorMsg'), errorMsg)
