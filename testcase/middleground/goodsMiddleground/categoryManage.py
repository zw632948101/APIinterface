#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
商品类目
"""
import random

from utils.log import log
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.goodsMP import MPcategory
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest
import inspect


class categoryData(object):
    """
    商品类目测试数据
    """

    def __init__(self):
        super(categoryData, self).__init__()
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

    def category_add_data(self):
        import copy
        ret = lambda var: [vn for vn, v in inspect.currentframe().f_back.f_locals.items() if v is var]
        category_dict = {"bizId": 1, 'pcode': 'T01', 'name': '', "isSale": 1, "remark": self.faker.text(20)}
        bizId = [1, -1, 0, '#', None]
        pcode = ['01', '\#', 1, 'T01', None]
        name = ['测试商品%s' % timestamp.get_timestamp(), self.faker.text(21), None]
        isSale = [0, 1, -1, 2, None, '#']
        remark = [self.faker.text(200), self.faker.text(201), None]
        add_data = []
        for klist in [bizId, pcode, name, isSale, remark]:
            lname = ret(klist)[1]
            for k in klist:
                cp_dict = copy.deepcopy(category_dict)
                cp_dict['name'] = '测试标签%s%s' % (timestamp.get_timestamp(), random.randint(10, 99))
                cp_dict[lname] = k
                add_data.append(cp_dict)
        return add_data

    def category_edit_data(self):
        category_dict = {'code': 'T02', "isSale": 1, "remark": self.faker.text(20)}
        code = ['01', '\#', 1, 'T01', None]
        isSale = [0, 1, -1, 2, None, '#']
        remark = [self.faker.text(200), self.faker.text(201), None]
        return self.inspect_name(data_dict=category_dict, code=code, isSale=isSale, remark=remark)

    def category_status_data(self):
        category_dict = {'id': '71', "status": 1}
        id = ['71', '\#', 1, 'T01', None]
        status = [0, 1, -1, 2, None, '#']
        return self.inspect_name(data_dict=category_dict, id=id, status=status)


@ddt
class categoryManage(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.db = MPcategory()
        self.faker = Faker('zh_CN')

    @unittest.skipIf(runlevel(1), '主流程用例，新建类别')
    def test_admin_category_add(self):
        """
        商品类目-新建类别
        :return:
        """
        bizId = 1
        name = "测试类别%s" % timestamp.get_timestamp()
        isSale = 1
        remark = self.faker.text(200)
        pcode = None
        response = self.api._admin_category_add(bizId_=bizId, pcode_=pcode, name_=name, isSale_=isSale, remark_=remark)
        self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))
        dbinfo = self.db.query_category_add_info(bizid=bizId, name=name, isSale=isSale, remark=remark, pcode=pcode)
        self.assertEqual(len(dbinfo), 1)
        self.assertEqual(self.api.user.user_id, str(dbinfo[0].get('creator_id')))

    @data(*categoryData().category_add_data())
    @unittest.skipIf(runlevel(3), '非主流程用例，新建类别')
    def test_admin_category_add_check(self, adddict):
        """
        商品类目-新建类别
        :return:
        """
        log.info(adddict)
        bizId = adddict.get('bizId')
        name = adddict.get('name')
        isSale = adddict.get('isSale')
        remark = adddict.get('remark')
        pcode = adddict.get('pcode')
        response = self.api._admin_category_add(bizId_=bizId, pcode_=pcode, name_=name, isSale_=isSale, remark_=remark)
        if response.get('status') == 'OK':
            self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))
            dbinfo = self.db.query_category_add_info(bizid=bizId, name=name, isSale=isSale, remark=remark, pcode=pcode)
            self.assertEqual(len(dbinfo), 1)
            self.assertEqual(self.api.user.user_id, str(dbinfo[0].get('creator_id')))
        else:
            self.assertEqual(response.get('status'), 'ERROR')
            if response.get('errorCode') == '11020101':
                self.assertEqual(response.get('errorMsg'), '业务类型不存在!')
            elif name is None:
                self.assertEqual(response.get('errorMsg'), '名称不能为空')
            elif len(name) > 20:
                self.assertEqual(response.get('errorMsg'), '名称不超过20字')
            elif response.get('errorCode') == '11020003':
                self.assertEqual(response.get('errorMsg'), '所属业务不能为空')
            elif response.get('errorCode') == '11020105':
                self.assertEqual(response.get('errorMsg'), '商品类目不存在')

    @unittest.skipIf(runlevel(1), '主流程，商品类目列表分页')
    def test_admin_category_page_list(self):
        """
        商品类目-分页列表
        :return:
        """
        pn = 1
        ps = 20
        response = self.api._admin_category_page_list(pn_=pn, ps_=ps)
        self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))
        dbinfo = self.db.query_category_page_list(pn=pn, ps=ps)
        dbinfo = conversion.del_dict_value_null(dbinfo)
        content = response.get('content')
        self.assertEqual(len(dbinfo), len(content.get('datas')))
        for dbi, datai in list(zip(dbinfo, content.get('datas'))):
            self.assertDictEqual(dbi, datai)

    @unittest.skipIf(runlevel(1), '编辑商品类目主流程')
    def test_admin_category_edit(self):
        """
        编辑商品类目
        :return:
        """
        dbinfo = self.db.query_category_page_list()[0]
        code = dbinfo.get('code')
        remark = self.faker.text(200)
        isSale = 0
        response = self.api._admin_category_edit(code_=code, remark_=remark, isSale_=isSale)
        self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))
        dbinfo = self.db.query_category_edit_info(isSale=isSale, code=code)
        self.assertEqual(len(dbinfo), 1)
        self.assertEqual(self.api.user.user_id, str(dbinfo[0].get('creator_id')))

    @data(*categoryData().category_edit_data())
    @unittest.skipIf(runlevel(3), '编辑商品类目主流程')
    def test_admin_category_edit_check(self, editdict):
        """
        编辑商品类目
        :return:
        """
        code = editdict.get('code')
        remark = editdict.get('remark')
        isSale = editdict.get('isSale')
        response = self.api._admin_category_edit(code_=code, remark_=remark, isSale_=isSale)
        if response.get('status') == 'OK':
            self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))
            dbinfo = self.db.query_category_edit_info(isSale=isSale, code=code)
            self.assertEqual(len(dbinfo), 1)
            self.assertEqual(self.api.user.user_id, str(dbinfo[0].get('editor_id')))
        else:
            self.assertEqual(response.get('status'), 'ERROR')
            if code == None:
                self.assertEqual(response.get('errorMsg'), '编码不能为空')
            else:
                self.assertEqual(response.get('errorMsg'), '数据不存在')

    @unittest.skipIf(runlevel(1), '主流程用例，商品类目  启用/禁用')
    def test_admin_category_change_status(self):
        """
        商品类目  启用/禁用
        :return:
        """
        dbinfo = self.db.query_category_page_list()[0]
        id_ = dbinfo.get('id')
        status = 1 if dbinfo.get('status') == 2 else 2
        response = self.api._admin_category_change_status(id_=id_, status_=status)
        self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))
        dbinfo = self.db.query_category_status_info(id_=id_)
        self.assertEqual(len(dbinfo), 1)
        self.assertEqual(self.api.user.user_id, str(dbinfo[0].get('creator_id')))

    @data(*categoryData().category_status_data())
    @unittest.skipIf(runlevel(2), '主流程用例，商品类目  启用/禁用')
    def test_admin_category_change_status_check(self, statusdict):
        """
        商品类目  启用/禁用
        :return:
        """
        id_ = statusdict.get('id')
        status = statusdict.get('status')
        response = self.api._admin_category_change_status(id_=id_, status_=status)
        if response.get('status') == 'OK':
            self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))
            dbinfo = self.db.query_category_status_info(id_=id_)
            self.assertEqual(len(dbinfo), 1)
            self.assertEqual(self.api.user.user_id, str(dbinfo[0].get('creator_id')))
        else:
            if response.get('errorCode') == '11020116':
                self.assertEqual(response.get('errorMsg'), '数据已更新,请刷新页面')
            if response.get('errorCode') == '11020115':
                self.assertEqual(response.get('errorMsg'), '数据不存在')
            if response.get('errorCode') == '11020003':
                self.assertEqual(response.get('errorMsg'), '状态不能为空')
