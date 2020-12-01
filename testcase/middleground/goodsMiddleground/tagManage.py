#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/10/27 17:31
# @Author: wei.zhang
# @File : tagManage.py
# @Software: PyCharm
"""
标签管理 测试用例
"""

from utils.log import log
import time
import random
import warnings
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.goodsMP import mp_label
from testcase.middleground.caseData.case_api import api_data
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest


class tagMdata(object):
    def __init__(self):
        super(tagMdata, self).__init__()
        self.faker = Faker('zh_CN')

    def add_label_data(self):
        """
        添加标签数据
        :return:
        """
        ldata = [None, self.faker.text(21), self.faker.text(20), self.faker.text(20), self.faker.text(20)]
        ltype = [1, 1, '1', None, self.faker.text(10)]
        label_data = [list(i) for i in zip(ldata, ltype)]
        return label_data


@ddt
class tagManage(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')


    @unittest.skipIf(runlevel(1), '主流程执行用例，设置等级为2时跳过该用例')
    def test_admin_label_add(self):
        """
        添加标签
        :return:
        """

        name = '测试标签' + str(timestamp.get_timestamp())
        _type = 1
        resp = self.api._admin_label_add(name_=name, type_=_type)
        self.assertEqual(resp.get('status'), 'OK', resp.get('errorMsg'))
        info = self.db.query_mp_label_info(label_name=name, label_type=_type)
        self.assertEqual(str(info[0].get('creator_id')), self.api.user.user_id)

    @data(*tagMdata().add_label_data())
    @unpack
    @unittest.skipIf(runlevel(3), '主流程执行用例，设置等级为4时跳过该用例')
    def test_admin_label_add_check(self, name, _type):
        """
        添加标签校验字段
        :return:
        """
        resp = self.api._admin_label_add(name_=name, type_=_type)
        if resp.get('status') == 'OK':
            self.assertEqual(resp.get('status'), 'OK', resp.get('errorMsg'))
            info = self.db.query_mp_label_info(label_name=name, label_type=_type)
            self.assertEqual(str(info[0].get('creator_id')), self.api.user.user_id)
        else:
            self.assertEqual(resp.get('status'), 'ERROR', resp.get('errorMsg'))
            if name is None:
                self.assertEqual(resp.get('errorMsg'), '名称不能为空')
            elif len(name) > 20:
                self.assertEqual(resp.get('errorMsg'), '名称不超过20字')
            elif _type is None:
                self.assertEqual(resp.get('errorMsg'), '类型不能为空')
            elif _type is str and len(_type) > 2:
                self.assertIn('参数验证错误', resp.get('errorMsg'))



    @data(*api_data().admin_label_add_data)
    def test_admin_label_add(self,case):
        """
                添加标签
                :return:
                """
        name_ = case['data']['name']
        _type = case['data']['type']
        resp = self.api._admin_label_add(name_= name_, type_=_type)
        self.assertEqual(case['expected'],resp.get('status'))
        info = self.db.query_mp_label_info(label_name=name_, label_type=_type)
        if  resp.get('status') == 'OK':
            self.assertEqual(str(info[0].get('creator_id')), self.api.user.user_id)
        else:
            print("")

    @unittest.skipIf(runlevel(2), "跑主流程时，跳过该用例")
    def test_get_label_list_all(self):
        """
                所有标签获取
                :return:
                """
        resp = self.api._admin_label_list_all()
        # 断言 接口响应是否通过
        self.assertEqual(resp.get('status'), 'OK', resp.get('errorMsg'))
        # 断言通过接口拿出来的数据，与实际数据库中数据，是否条数一致
        self.assertEqual(len(self.db.git_label_list()),len(resp["content"]))

    @data(*api_data().admin_label_change_status_data)
    def test_admin_label_change_status(self,case):
        """
        启用禁用标签
        :param case:
        :return:
        """

        id_ = int(case['data']["id_"])
        status_ = int(case['data']["status_"])
        print(id_ ,status_)
        resp = self.api._admin_label_change_status(id_=id_,status_=status_)

        self.assertEqual(resp.get('status'),'OK',resp.get('errorMsg'))
        self.assertEqual(self.db.git_admin_label_change_status()[0]['status'],int(case['data']['status_']))

    @unittest.skipIf(runlevel(2), "跑主流程时，跳过该用例")
    def test_admin_label_page_list(self):
        '''
        分页查询
        :return:
        '''
        resp = self.api._admin_label_page_list(pn_=1,ps_=5)
        self.assertEqual(resp.get('status'),'OK',resp.get('errorMsg'))
        self.assertEqual(len(self.db.git_admin_label_page_list()),len(resp['content']['datas']))
        self.assertEqual(self.db.git_admin_label_page_list()[0]['name'],resp['content']['datas'][0]['name'])

    @unittest.skipIf(runlevel(2), "跑主流程时，跳过该用例")
    @data(*api_data().admin_label_list_by_type)
    def test_admin_label_list_by_type(self,case):
        '''

        按类型查询列表
        :return:
        '''
        type_ = case['data']['type']
        status_ = case['data']['type']

        resp = self.api._admin_label_list_by_type(type_=type_,status_=status_)
        self.assertEqual(case['expected'],resp.get('status'))

        # 如果通过接口查询出结果，再去数据库查询
        if resp.get('status') == 'OK':
            self.assertEqual(len(self.db.git_admin_label_list_by_type(type_,status_)),len(resp['content']))
        else:
            print("")
if __name__ == '__main__':
   unittest.main()
