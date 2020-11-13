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

data_list = [{
                "name": 'jj',
                "alias": 'gg',
                "class1": "F14",
                "class2": "F1402",
                "class3": "F140201",
                "brandId": "1",
                "basicCost": 1,
                "minimumPrice": 1,
                "marketPrice": 1,
                "validity": -365,
                "validityUnit": "MONTH",
                "netWeight": "50",
                "grossWeight": "50",
                "weightUnit": "kg",
                "baseUnit": -1,
                "isSale": "1",
                "basicAttr": "",
                "saleAttr": ""
            }]
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
    #
    # @data(*data_list)
    # def test_admin_section_add(self,case):
    #     ruleName_ = case['ruleName']
    #
    #     resp = self.api._admin_sku_add()
    #     self.assertEqual('OK',resp.get('status'))

    @data(*data_list)
    def test_admin_sku_add(self,case):
        name = case['name']
        alias = case['alias']
        class1 = case['class1']
        class2 = case['class2']
        class3 = case['class3']
        brandId = case['brandId']
        basicCost = case['basicCost']
        minimumPrice = case['minimumPrice']
        marketPrice = case['marketPrice']
        validity = case['validity']
        validityUnit = case['validityUnit']
        netWeight = case['netWeight']
        grossWeight = case['grossWeight']
        weightUnit = case['weightUnit']
        baseUnit = case['baseUnit']
        isSale = case['isSale']
        basicAttr = case['basicAttr']
        saleAttr = case['saleAttr']

        resp = self.api._admin_sku_add(name_=name,alias_=alias,class1_=class1,class2_=class2,class3_=class3,
                                       brandId_=brandId,basicCost_=basicCost,minimumPrice_=minimumPrice,
                                       marketPrice_=marketPrice,validity_=validity,validityUnit_=validityUnit,
                                       netWeight_=netWeight,grossWeight_=grossWeight,weightUnit_=weightUnit,
                                       baseUnit_=baseUnit,isSale_=isSale,basicAttr_=basicAttr,saleAttr_=saleAttr)

        self.assertEqual('OK',resp.get('status'))


if __name__ == '__main__':
    unittest.main()
