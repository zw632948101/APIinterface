from utils.log import log
import time
import json
import random
import warnings
from interfaces.middleground.Wms_apiAction import wms_apiAction
from utils.userInfo.GetUserInfo import SessionTool
from testcase.middleground.sql.sku_inventoryMP import mp_label
from testcase.middleground.WMS.datas.whs_warehousing_notice_data import warehousing_notice_data
from testcase.middleground.WMS.datas.whs_in_order_data import whs_in_order
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest


@ddt
class warehousing_notice(unittest.TestCase):
    def setUp(self):
        """
        测试前数据准备
        :return:
        """
        self.api = wms_apiAction()
        self.api.set_user(mobile=15198034727)
        self.db = mp_label()
        self.faker = Faker('zh_CN')
    # 查询ERP单据
    def test_admin_erp_uncleared_order_purchase_list(self):
        companyCode_ = 100002 # QA环境时传 2；DEV环境时传 100002

        resp = self.api._admin_erp_uncleared_order_purchase_list(companyCode_=companyCode_)
        self.assertEqual('OK',resp.get('status'))

        for case in resp.get('content'):
            print(case)

    # 新增入库通知单
    @data(*warehousing_notice_data().admin_receipt_notice_add)
    def test_admin_receipt_notice_add(self,case):
        relevanceCode_ = case['data']['relevanceCode']
        source_ = case['data']['source']
        type_ = case['data']['type']
        warehouseCode_ = case['data']['warehouseCode']
        purchasingCompany_ = case['data']['purchasingCompany']
        possessor_ = case['data']['possessor']
        supplier_ = case['data']['supplier']
        remark_ = case['data']['remark']
        erpType_ = case['data']['erpType']
        productInfo_ = json.dumps(case['data']['productInfo'])
        resp = self.api._admin_receipt_notice_add(relevanceCode_=relevanceCode_,
                                                  source_=source_,
                                                  type_=type_,
                                                  warehouseCode_=warehouseCode_,
                                                  purchasingCompany_=purchasingCompany_,
                                                  possessor_=possessor_,
                                                  supplier_=supplier_,
                                                  remark_=remark_,
                                                  erpType_=erpType_,
                                                  productInfo_=productInfo_)
        self.assertEqual(case['expect'],resp.get('status'))
    # 取消入库通知单
    @data(*warehousing_notice_data().admin_receipt_notice_cancel)
    def test_admin_receipt_notice_cancel(self,case):
        code_ = case['data']['code_']
        resp = self.api._admin_receipt_notice_cancel(code_=code_)
        self.assertEqual(case['expect'],resp.get('status'))
    # 确认入库通知单
    # def test_admin_receipt_notice_confirm(self):
    #     code_ = None
    #     resp = self.api._admin_receipt_notice_confirm(code_=None)


if __name__ == '__main__':
    unittest.main()
    #list = [{'productCode': 'T0101020013','planQuantity': 980, 'price': 10.0,'taxRate': 0.0,'taxRateCode': 'J1','erpLine': 0,'noticeTracings':[{'tracingCode': 'T0101010009','purchaseWeight': 1,'tareWeight':1}]}]

