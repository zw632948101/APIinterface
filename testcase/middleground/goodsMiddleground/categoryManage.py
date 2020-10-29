#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

from utils.log import log
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.goodsMP import MPcategory
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest


@ddt
class tagManage(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.db = MPcategory()
        self.faker = Faker('zh_CN')

    def test_admin_category_add(self):
        """
        商品类目-新建类别
        :return:
        """
        bizId = 1
        name = '测试商品分类%s' % timestamp.get_timestamp()
        isSale = 1
        remark = ''
        response = self.api._admin_category_add(bizId_=bizId, name_=name, isSale_=isSale, remark_=remark)
        self.assertEqual(response.get('status'), 'OK', response.get('errorMsg'))
