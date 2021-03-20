import unittest
import requests
import json
from testcase.middleground.WMS.common.loginHeader import assembleHeader
from interfaces.middleground.Wms_apiAction import wms_apiAction
from testcase.middleground.sql.shopMP import mpShopSql
from testcase.middleground.WMS.datas.warehouse_data import warehouse_data
from ddt import data, ddt
from testcase.middleground.WMS.common.Mysql import mp_label
from utils import runlevel
from faker import Faker


class orderflow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        #获取一次100001公司下，ERP关联单据
        cls.headers = assembleHeader(url="/world-passport/admin/sso/sms-login").add_header()
        cls.url = "http://qa-gateway.worldfarm.com/mp-wms/admin/erp/uncleared/order/purchase-list"
        cls.data = {"companyCode": "100001"}
        cls.resp = requests.post(url=cls.url,
                                data=cls.data,
                                headers=cls.headers)
        cls.result = cls.resp.json()['content'][0]
        print(cls.result)
        pass


    def setUp(self) -> None:
        """
            测试前数据准备
            :return:
        """
        self.api = wms_apiAction()
        self.api.set_user(mobile=15198034727, account_type='web-mp')
        self.db = mpShopSql()
        self.faker = Faker('zh_CN')

    def tearDown(self) -> None:
        pass
    def test_admin_erp_uncleared_order_purchase_list(self):
        resp = self.api._admin_erp_uncleared_order_purchase_list(companyCode_=100001)
        print(resp.get('content')[0])

    def test_admin_receipt_notice_add(self):
        # 通过ERP关联单号接口获取
        relevanceCode_ = 72
        supplier_ = 'MS-4550'
        supplierName_ = '苗叔1'
        erpType_ = 22
        productInfo_ = json.dumps(self.result['purchaseProducts'])

        resp = self.api._admin_receipt_notice_add(relevanceCode_=relevanceCode_,
                                                  source_="ERP",
                                                  type_="RK02",
                                                  warehouseCode_=30020,
                                                  company_=100001,
                                                  supplier_=supplier_,
                                                  supplierName_=supplierName_,
                                                  initiator_=18593,
                                                  remark_="测试",
                                                  erpType_=None,
                                                  erpDocNum_=None,
                                                  productInfo_=productInfo_)

        self.assertEqual('OK',resp.get('status'))
        print(resp.get('content'))

if __name__ == '__main__':
    unittest.main()