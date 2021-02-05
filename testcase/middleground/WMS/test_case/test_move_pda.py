from utils.log import log
import time
import json
import random
import warnings
from testcase.middleground.WMS.common.Pash import Header_mkdir
from testcase.middleground.WMS.common.Pash import Public_mkdir
from testcase.middleground.WMS.common.Http import Request
from testcase.middleground.WMS.prepare.login import login
from testcase.middleground.WMS.common.config import read_config
from interfaces.middleground.Wms_apiAction import wms_apiAction
from utils.userInfo.GetUserInfo import SessionTool
from testcase.middleground.sql.sku_inventoryMP import mp_label
from testcase.middleground.WMS.datas.whs_warehousing_notice_data import warehousing_notice_data
from testcase.middleground.WMS.datas.whs_in_order_data import whs_in_order
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest


class move_pda(unittest.TestCase):
    def setUp(self):
        """
        测试前数据准备
        :return:
        """
        self.api = wms_apiAction()
        self.api.set_user(mobile=15198034727)
        self.db = mp_label()
        self.faker = Faker('zh_CN')


    # 确认入库
    # def test_mobile_receipt_pda_product_submit(self):
    #     resp = self.api._mobile_receipt_pda_product_submit(code_='RK0220210203000002',
    #                                                        productInfo_=json.dumps(
    #                                                                     [
    #
    #                                                                         {
    #                                                                             "productCode":"T0101010006",
    #                                                                             "actualQuantity":"5",
    #                                                                             "receiptTracings":
    #                                                                                                 [{"tracingCode":"JX010012011","weight":"90"},
    #                                                                                                  {"tracingCode":"JX010012022","weight":"90"},
    #                                                                                                  {"tracingCode":"JX010012033","weight":"90"},
    #                                                                                                  {"tracingCode":"JX010012044","weight":"90"},
    #                                                                                                  {"tracingCode":"JX010012055","weight":"90"}
    #                                                                                                  ]
    #                                                                          },
    #
    #
    #                                                                      ]),
    #                                                        qualityResult_=None,
    #                                                        receiptQualityInfo_=None)
    #     self.assertEqual('OK',resp.get('status'))
    # 确认拣货出库
    def test_admin_move_pda_pick_submit(self):
        invoiceCode_ = "CK1320210203000032" #出库单号
        code_ = "JH1320210203000033"  #拣货单号
        productJson_ = json.dumps([
                                    {
                                        "id":18,
                                        "productCode":"T0101010006",
                                        "actualQuantity":1,
                                        "weight":1,
                                        "sourceList":
                                                    [
                                                        {"productCode":"T0101010006",
                                                         "tracingCode":"JX010012011",
                                                         "quantity":1,
                                                         "purchaseWeight":1,
                                                         "weight":1}
                                                    ]
                                    }
                                ])

        resp = self.api._mobile_move_pda_pick_submit(invoiceCode_= invoiceCode_,
                                                     code_=code_,
                                                     productJson_=productJson_)
        self.assertEqual('OK',resp.get('status'))



if __name__ == '__main__':
    unittest.main()
