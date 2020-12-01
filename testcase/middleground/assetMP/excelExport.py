#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/11/11 15:45
# @Author: wei.zhang
# @File : excelExport.py
# @Software: PyCharm

import json
from interfaces.middleground.AssetAction import assetAction
from testcase.middleground.sql.asstMpSQL import excelExportSQL
from utils import runlevel, dataDispose, timestamp
from ddt import data, ddt
from faker import Faker
import unittest
import random


@ddt
class excelExport(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = assetAction()
        self.api.set_user(mobile=15388126072)
        self.db = excelExportSQL()
        self.faker = Faker('zh_CN')

    def test_admin_excel_export_code(self):
        batchid = 14
        value = '1'
        resp = self.api._admin_excel_export_code(batchId_=batchid,value_=value)
        with open('资产编码导出_'+timestamp.get_standardtime_by_offset(formats="%Y%m%d")+'.xlsx','wb') as f:
            f.write(resp)


