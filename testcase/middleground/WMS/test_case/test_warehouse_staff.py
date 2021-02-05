#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from utils.log import log
import time
import json
import random
import warnings
import unittest
from interfaces.middleground.Wms_apiAction import wms_apiAction
from testcase.middleground.WMS.common.Mysql import mp_label
from utils.userInfo.GetUserInfo import SessionTool
from testcase.middleground.sql.sku_inventoryMP import mp_label
from testcase.middleground.WMS.datas.whs_warehousing_notice_data import warehousing_notice_data
from testcase.middleground.WMS.datas.whs_in_order_data import whs_in_order
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker




# 获取仓库列表-绑定员工-解绑员工-列表
class warehouse_staff(unittest.TestCase):


    warehouse = []

    def setUp(self):
        """
        测试前数据准备
        :return:
        """
        self.api = wms_apiAction()
        self.api.set_user(mobile=15198034727)
        self.db = mp_label()
        self.faker = Faker('zh_CN')

    # 获取仓库列表，绑定员工
    def test_admin_warehouse_list(self):
        resp = self.api._admin_warehouse_list(status_=1,
                                              code_=None,
                                              shopCode_=None)
        self.assertEqual('OK',resp.get('status'))
        for warehuse in resp.get('content'):
            self.warehouse.append(warehuse['id'])

        userIds_ = 18593,18599
        resp = self.api._admin_warehouse_employee_add(userIds_=userIds_,
                                                      warehouseId_=self.warehouse[0])
        self.assertEqual('OK',resp.get('status'))


    def test_admin_warehouse_employee_dell(self):
        resp = self.api._admin_warehouse_employee_del(warehouseEmployeeId_=45)
        self.assertEqual('OK',resp.get('status'))

    def test_admin_warehouse_employee_list(self):
        resp = self.api._admin_warehouse_employee_list(id_=45)
        self.assertEqual('OK',resp.get('status'))



if __name__ == '__main__':
    unittest.main()































