from utils.log import log
import time
import random
import warnings
from interfaces.middleground.ProductAction import ProductAction
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.brandMP import mp_label
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest


class inventory_data:
    inventory_add = [
        {"title":"新增库存","data":{"skuId_":"143","skuCode_":"T0101010001","quantity_":20000},"expected":"OK"},
        {"title":"新增库存","data":{"skuId_":"145","skuCode_":"T0101010002","quantity_":20000},"expected":"OK"},
        {"title":"库存为负","data":{"skuId_":"143","skuCode_":"T0101010001","quantity_":-10000},"expected":"ERROR"},
        {"title":"库存为空","data":{"skuId_":"143","skuCode_":"T0101010001","quantity_":None},"expected":"ERROR"},
        {"title":"ID为空","data":{"skuId_":None,"skuCode_":"T0101010001","quantity_":30000},"expected":"ERROR"},
        {"title":"code为空","data":{"skuId_":"143","skuCode_":None,"quantity_":30000},"expected":"ERROR"}
    ]
    inventory_update = [
        {"title":"修改库存","data":{"skuCode":"T0101010001","quantity":30000},"expected":"OK"},
        {"title":"修改库存-为负","data":{"skuCode":"T0101010001","quantity":-30000},"expected":"ERROR"},
        {"title":"修改库存-为空","data":{"skuCode":"T0101010001","quantity":None},"expected":"ERROR"}
    ]
    inventory_list = [
        {"title":"修改库存-为空","data":{"pn":"","ps":"","skuCode":"","skuName":""},"expected":"ERROR"},
        {}
    ]
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

    @data(*inventory_data().inventory_add)
    def test_admin_inventory_add(self,case):
        skuId_ = case['data']['skuId_']
        skuCode_ = case['data']['skuCode_']
        quantity_ = case['data']['quantity_']
        resp = self.api._admin_inventory_add(skuId_=skuId_, skuCode_=skuCode_, quantity_=quantity_)
        self.assertEqual(case['expected'],resp.get('status'))

    def test_admin_inventory_page_list(self):
        pass

    @data(*inventory_data().inventory_update)
    def test_admin_inventory_update(self,case):
        skuCode_ = case['data']['skuCode']
        quantity_ = case['data']['quantity']
        resp = self.api._admin_inventory_update(skuCode_=skuCode_, quantity_=quantity_)
        self.assertEqual(case['expected'],resp.get('status'))

if __name__ == '__main__':
    unittest.main()