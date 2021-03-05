from utils.log import log
import time
import random
import warnings
from interfaces.middleground.ProductAction import ProductAction

from testcase.middleground.sql.sku_inventoryMP import mp_label
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
        ldata = [None, self.faker.text(21), self.faker.text(20), self.faker.text(20),
                 self.faker.text(20)]
        ltype = [1, 1, '1', None, self.faker.text(10)]
        label_data = [list(i) for i in zip(ldata, ltype)]
        return label_data


@ddt
class skuManage(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')

    @data(*api_data().admin_sku_add)
    def test_admin_sku_add(self, case):
        name = case['data']['name']
        alias = case['data']['alias']
        class1 = case['data']['class1']
        class2 = case['data']['class2']
        class3 = case['data']['class3']
        brandId = case['data']['brandId']
        basicCost = case['data']['basicCost']
        minimumPrice = case['data']['minimumPrice']
        marketPrice = case['data']['marketPrice']
        validity = case['data']['validity']
        validityUnit = case['data']['validityUnit']
        netWeight = case['data']['netWeight']
        grossWeight = case['data']['grossWeight']
        weightUnit = case['data']['weightUnit']
        baseUnit = case['data']['baseUnit']
        isSale = case['data']['isSale']
        basicAttr = case['data']['basicAttr']
        saleAttr = case['data']['saleAttr']

        resp = self.api._admin_sku_add(name_=name, alias_=alias, class1_=class1, class2_=class2,
                                       class3_=class3,
                                       brandId_=brandId, basicCost_=basicCost,
                                       minimumPrice_=minimumPrice,
                                       marketPrice_=marketPrice, validity_=validity,
                                       validityUnit_=validityUnit,
                                       netWeight_=netWeight, grossWeight_=grossWeight,
                                       weightUnit_=weightUnit,
                                       baseUnit_=baseUnit, isSale_=isSale, basicAttr_=basicAttr,
                                       saleAttr_=saleAttr)

        self.assertEqual(case['expect'], resp.get('status'))
        if resp.get('status') == 'OK':
            self.assertEqual(mp_label().git_sku_add(1)[0]['name'], name)

    def test_admin_sku_list_zh_charge(self):
        """
        商品sku-追花定金策略商品列表
        :return:
        """
        class1 = 'T01'
        class2 = 'T0105'
        class3 = 'T010501'
        province = None
        city = None
        county = None
        resp = self.api._admin_sku_list_zh_charge(class1_=class1, class2_=class2, class3_=class3,
                                                  province_=province, city_=city, county_=county)
        self.assertEqual(resp.get('status'), 'OK')

    def test_admin_sku_list_zh_charge(self):
        """
        商品sku-追花定金策略商品列表
        :return:
        """
        class1 = 'T01'
        class2 = 'T0105'
        class3 = 'T010501'
        province = None
        city = None
        county = None
        resp = self.api._admin_sku_list_zh_charge(class1_=class1, class2_=class2, class3_=class3,
                                                  province_=province, city_=city, county_=county)
        self.assertEqual(resp.get('status'), 'OK')

    # @unittest.skipIf(runlevel(2), "跑主流程时，跳过该用例")
    # @data(*api_data().admin_sku_page_list)
    # def test_admin_sku_page_list(self,case):
    #     pn = case['data']['pn']
    #     ps = case['data']['ps']
    #     skuCode = case['data']['skuCode']
    #     name = case['data']['name']
    #     resp = self.api._admin_sku_page_list(pn_=pn, ps_=ps, skuCode_=skuCode, name_=name)

    # def test_admin_sku_detail(self):
    #     resp = self.api._admin_sku_detail(skuCode_="F1402010006")
    #     self.assertEqual('OK',resp.get('status'))
    #     print("这是响应实体: %s"%resp)
    #     print(resp.get('header'))


if __name__ == '__main__':
    unittest.main()
