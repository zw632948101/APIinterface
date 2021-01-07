from utils.log import log
import time
import random
import warnings
from interfaces.middleground.Wms_apiAction import wms_apiAction

from testcase.middleground.sql.sku_inventoryMP import mp_label
from testcase.middleground.WMS.datas.whs_in_order_data import whs_in_order
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest

@ddt
class warehouse_order(unittest.TestCase):
    def setUp(self):
        """
        测试前数据准备
        :return:
        """
        self.api = wms_apiAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')

    def test_admin_whs_receipt_count(self):
        try:
            resp = self.api._admin_whs_receipt_count()
        except Exception as e:
            raise e
        if resp.get('status') == 'ERROR':
            print("获取订单总数: 接口报错！")
        self.assertEqual('OK', resp.get('status'))

    @data(*whs_in_order().admin_whs_receipt_detail)
    def test_admin_whs_receipt_detail(self,case):
        code_ = case['data']['code_']
        resp = self.api._admin_whs_receipt_detail(code_=code_)
        if resp.get('status') == 'ERROR':
            print("响应结果-FAIL: {0}".format(resp))
        else:
            print("测试结果-PASS: {0}".format(resp.get('content')))
        self.assertEqual(case['expect'],resp.get('status'))

    @data(*whs_in_order().admin_whs_receipt_page_list)
    def test_admin_whs_receipt_page_list(self,case):
        pn_ = case['data']['pn']
        ps_ = case['data']['ps']
        code_ = case['data']['code']
        status_ = case['data']['status']
        type_ = case['data']['type']
        warehouseCode_ = case['data']['warehouseCode']
        creatorId_ = case['data']['creatorId']
        resp = self.api._admin_whs_receipt_page_list(pn_=pn_,
                                                     ps_=ps_,
                                                     code_=code_,
                                                     status_=status_,
                                                     type_=type_,
                                                     warehouseCode_=warehouseCode_,
                                                     creatorId_=creatorId_)
        if resp.get('status') == 'ERROR':
            print("响应结果-FAIL: {0}".format(resp))
        else:
            print("测试结果-PASS: {0}".format(resp.get('content')))
        self.assertEqual(case['expect'],resp.get('status'))
    @data(*whs_in_order().admin_whs_receipt_page_list)
    def test_admin_whs_receipt_tracing_page_list(self,case):
        pn_ = case['data']['pn']
        ps_ = case['data']['pn']
        orderCode_ = case['data']['orderCode']
        productCode_ = case['data']['productCode']
        tracingCode_ = case['data']['tracingCode']
        resp = self.api._admin_whs_receipt_tracing_page_list(pn_=pn_,
                                                             ps_=ps_,
                                                             orderCode_=orderCode_,
                                                             productCode_=productCode_,
                                                             tracingCode_=tracingCode_)

        if resp.get('status') == 'ERROR':
            print("响应结果-FAIL: {0}".format(resp))
        else:
            print("测试结果-PASS: {0}".format(resp.get('content')))
        self.assertEqual(case['expect'],resp.get('status'))
if __name__ == '__main__':
        unittest.main()


