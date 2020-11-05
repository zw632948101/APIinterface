from utils.log import log
import time
import random
import warnings
from interfaces.middleground.ProductAction import ProductAction
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.caseData.case_api import api_data
from testcase.middleground.sql.brandMP import mp_label
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest



@ddt
class inventory(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()

    # @data(*api_data().admin_inventory_add)
    # def test_admin_inventory_add(self,case):
    #     skuId_ = case['data']['skuId_']
    #     skuCode_ = case['data']['skuCode_']
    #     quantity_ = case['data']['quantity_']
    #     resp = self.api._admin_inventory_add(skuId_=skuId_, skuCode_=skuCode_, quantity_=quantity_)
    #     self.assertEqual(case['expected'],resp.get('status'))
    #
    @data(*api_data().admin_inventory_list)
    def test_admin_inventory_page_list(self,case):
        pn = case['data']['pn']
        ps = case['data']['ps']
        skuCode = case['data']['skuCode']
        skuName = case['data']['skuName']

        resp = self.api._admin_inventory_page_list(pn_=pn, ps_=ps, skuCode_=skuCode, skuName_=skuName)
        self.assertEqual(case['expected'],resp.get('status'))

    # @data(*api_data().admin_inventory_update)
    # def test_admin_inventory_update(self,case):
    #     skuCode_ = case['data']['skuCode']
    #     quantity_ = case['data']['quantity']
    #     resp = self.api._admin_inventory_update(skuCode_=skuCode_, quantity_=quantity_)
    #     self.assertEqual(case['expected'],resp.get('status'))

if __name__ == '__main__':
    unittest.main()