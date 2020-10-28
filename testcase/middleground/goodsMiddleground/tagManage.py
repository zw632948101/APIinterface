#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/10/27 17:31
# @Author: wei.zhang
# @File : tagManage.py
# @Software: PyCharm

from utils.log import log
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.goodsMP import mp_label
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
        log.info(label_data)
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
