#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import unittest
import json
import random
from interfaces.middleground.Wms_apiAction import wms_apiAction
from testcase.middleground.sql.shopMP import mpShopSql
from ddt import data, ddt
from utils import runlevel
from faker import Faker
import unittest



# 获取ERP采购单->创建入库通知单->确认入库通知单



class wms(unittest.TestCase):
    # 获取ERP采购单
    def setUp(self) -> None:
        """
                测试前数据准备
                :return:
                """
        self.api = wms_apiAction()
        self.api.set_user(mobile=15198034727, account_type='web-mp')
        self.db = mpShopSql()
        self.faker = Faker('zh_CN')

    @classmethod
    def setUpClass(cls):
        cls.erp_list = []


    # 获取ERP采购单
    def test_admin_erp_uncleared_order_purchase_list(self):
        companyCode_ = 100002
        resp = self.api._admin_erp_uncleared_order_purchase_list(companyCode_=companyCode_)
        self.assertEqual('OK',resp.get('status'))
        # 储存ERP采购单code
        relevanceCode = []
        if resp.get('status') == 'OK':
            for order_list in resp.get('content'):
                relevanceCode.append(order_list['relevanceCode'])
                self.erp_list.append(order_list['relevanceCode'])
        print(relevanceCode)
    # 创建入库通知单

    # def test_admin_receipt_notice_add(self):
    #     relevanceCode_ = 105
    #     source_ = "ERP"
    #     type_ = "RK02"
    #     warehouseCode_ = 40122
    #     company_ = 100002
    #     supplier_ = "S05000001"
    #     supplierName_ = "成都大农科技供应商test"
    #     remark_ = None
    #     erpType_ = 22
    #     productInfo_ = json.dumps([{"productCode":"T0102010002","planQuantity":2,"price":24,"taxRate":0,"taxRateCode":"J0","erpLine":"0","erpItemType":"N"}])
    #     resp = self.api._admin_receipt_notice_add(
    #                                               relevanceCode_=relevanceCode_,
    #                                               source_=source_,
    #                                               type_=type_,
    #                                               warehouseCode_=warehouseCode_,
    #                                               company_=company_,
    #                                               supplier_=supplier_,
    #                                               supplierName_=supplierName_,
    #                                               remark_=remark_,
    #                                               erpType_=erpType_,
    #                                               productInfo_=productInfo_
    #                                               )
    #     self.assertEqual('OK',resp.get('status'))

    def test_mobile_receipt_pda_product_submit(self):


        resp = self.api._mobile_receipt_pda_product_submit(code_='RK0220210205000012',
                                                       productInfo_=json.dumps(
                                                                    [

                                                                        {
                                                                            "productCode":"T0101010007",
                                                                            "actualQuantity":"101",
                                                                            # "receiptTracings":
                                                                            #                     [{"tracingCode":"JX010000015","weight":"90"}
                                                                            #
                                                                            #                      ]
                                                                         },


                                                                     ]),
                                                       qualityResult_=None,
                                                       receiptQualityInfo_=None)
        self.assertEqual('OK',resp.get('status'))

if __name__ == '__main__':
    unittest.main()