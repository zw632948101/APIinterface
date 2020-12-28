from utils.log import log
import time
import json
import random
import warnings
import requests
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.sku_inventoryMP import mp_label
from testcase.middleground.caseData.sku_push_data import push_sku
from testcase.middleground.WMS.prepare.login import login
from testcase.middleground.WMS.common.config import read_config
from testcase.middleground.WMS.common.Pash import Header_mkdir
from testcase.middleground.caseData.case_data import middleground_data
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest

'''新增商品-->查看新增的商品详情-->获取商品列表-->将商品同步到ERP或WMS'''



@ddt
class product(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 提前查出库中sku总数
        global sku_expect,sku_list
        sku_expect = mp_label().git_sku_add(2)[0]['count(*)']
        sku_list = []
    def setUp(self):
        """
        测试前数据准备
        :return:
        """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')

    # 新增商品sku
    @data(*push_sku().sku_add)
    def test_01_admin_sku_add(self,case):
        resp = self.api._admin_sku_add( name_=case['data']['name_'],
                                        alias_=case['data']['alias_'],
                                        class1_=case['data']['class1_'],
                                        class2_=case['data']['class2_'],
                                        class3_=case['data']['class3_'],
                                        brandId_=case['data']['brandId_'],
                                        basicCost_=case['data']['basicCost_'],
                                        minimumPrice_=case['data']['minimumPrice_'],
                                        marketPrice_=case['data']['marketPrice_'],
                                        validity_=case['data']['validity_'],
                                        validityUnit_=case['data']['validityUnit_'],
                                        netWeight_=case['data']['netWeight_'],
                                        grossWeight_=case['data']['grossWeight_'],
                                        airTransport_=case['data']['airTransport_'],
                                        basicAttr_=json.dumps(case['data']['basicAttr_']),
                                        saleAttr_=json.dumps(case['data']['saleAttr_']),
                                        length_=case['data']['length_'],
                                        width_=case['data']['width_'],
                                        height_=case['data']['height_'],
                                        volume_=case['data']['volume_'],
                                        barCode_=case['data']['barCode_'],
                                        batchMnt_=case['data']['batchMnt_'],
                                        hasSourceCode_=case['data']['hasSourceCode_'],
                                        needWeigh_=case['data']['needWeigh_'],
                                        inventoryUnit_=case['data']['inventoryUnit_'],
                                        purchaseUnit_=case['data']['purchaseUnit_'],
                                        salesUnit_=case['data']['salesUnit_'],
                                        salesUnitQuantity_=case['data']['salesUnitQuantity_'],
                                        purchaseUnitQuantity_=case['data']['purchaseUnitQuantity_'],
                                        purchaseTaxId_=case['data']['purchaseTaxId_'],
                                        salesTaxId_=case['data']['salesTaxId_'],
                                        salesTaxId2_=case['data']['salesTaxId2_'],
                                        accessoryCost_=case['data']['accessoryCost_'],
                                        productType_=case['data']['productType_'],
                                        skuRelatedStr_=case['data']['skuRelatedStr_'])
        self.assertEqual('OK',resp.get('status'))
        #商品新增成功，数据库t_sku表数据增加
        actual = mp_label().git_sku_add(2)[0]['count(*)']
        if resp.get('status') == 'OK':
            self.assertEqual(sku_expect + 1, actual)
        else:
            self.assertNotEqual(sku_expect + 1, actual)
    # 获取商品详情
    def test_admin_sku_detail(self):
        skuCode_ = mp_label().git_sku_add(1)[0]['code']
        self.api._admin_sku_detail(skuCode_=skuCode_)
    # # 编辑商品
    # def test_admin_sku_edit(self):
    #     self.api._admin_sku_edit(code_=None,
    #                              name_=None,
    #                              alias_=None,
    #                              brandId_=None,
    #                              basicCost_=None,
    #                              minimumPrice_=None,
    #                              marketPrice_=None,
    #                              validity_=None,
    #                              validityUnit_=None,
    #                              netWeight_=None,
    #                              grossWeight_=None,
    #                              baseUnit_=None,
    #                              isSale_=None,
    #                              airTransport_=None,
    #                              basicAttr_=None,
    #                              saleAttr_=None,
    #                              length_=None,
    #                              width_=None,
    #                              height_=None,
    #                              volume_=None,
    #                              barCode_=None,
    #                              batchMnt_=None,
    #                              needWeigh_=None,
    #                              inventoryUnit_=None,
    #                              purchaseUnit_=None,
    #                              salesUnit_=None,
    #                              salesUnitQuantity_=None,
    #                              purchaseUnitQuantity_=None,
    #                              relatedSkuCode_=None,
    #                              purchaseTaxId_=None,
    #                              salesTaxId_=None,
    #                              salesTaxId2_=None,
    #                              accessoryCost_=None,
    #                              productType_=None,
    #                              skuRelatedStr_=None)
    # # 商品分页列表
    # def test_admin_sku_page_list(self):
    #     self.api._admin_sku_page_list(pn_=None, ps_=None, skuCode_=None, name_=None)

    # 同步sku到ERP

    # 获取商品列表
    # 获取商品列表，存入商品sku
    def test_04_admin_sku_page_list(self):
        pn_ = 1
        ps_ = 10
        skuCode_ = None
        name_ = None
        resp = self.api._admin_sku_page_list(pn_=pn_,
                                             ps_=ps_,
                                             skuCode_=skuCode_,
                                             name_=name_)
        self.assertEqual('OK',resp.get('status'))
        # 存入商品编码，后面push接口要用
        if resp.get('status') == 'OK':
            for sku in resp.get('content')['datas']:
                sku_list.append(sku['code'])
        else:
            pass
    # 同步商品到ERP
    def test_admin_product_push(self):
        skus_ = sku_list
        subjectCode_ = 1
        resp = self.api._admin_product_sync_erp_push(skus_=json.dumps(skus_),
                                                     subjectCode_=subjectCode_)
        self.assertEqual('OK',resp.get('status'))

    # 同步商品到WMS或ERP
    def test_admin_product_sync(self):
        skuCodes_ = sku_list
        type_ = 2
        resp = self.api._admin_product_sync_sync(skuCodes_=skuCodes_, type_=type_)
        print(resp.get('content'))
        self.assertEqual('OK',resp.get('status'))


if __name__ == '__main__':
    unittest.main()
