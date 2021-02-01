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


        self.url = r"/world-passport/admin/sso/sms-login"
        self.login = login(self.url).test_login()
        self.headers = {
            "_Device-Id_": read_config(Header_mkdir).get("header", "_device-id_"),
            "_Token_": read_config(Header_mkdir).get("header", "_token_"),
            "region": "online"
        }

        self.url = read_config(Public_mkdir).get("test_url","url")
    #确认入库
    # def test_mobile_receipt_pda_product_submit(self):
    #     resp = self.api._mobile_receipt_pda_product_submit(code_='RK202101180012',
    #                                                        productInfo_=json.dumps(
    #                                                            [{
    #                                                                "productCode": "T0103010009",
    #                                                                "actualQuantity": "1"
    #                                                            },
    #                                                                {
    #                                                                    "productCode": "T0103020012",
    #                                                                    "actualQuantity": "1"
    #                                                                },
    #                                                                {
    #                                                                    "productCode": "T0102010025",
    #                                                                    "actualQuantity": "1"
    #                                                                },
    #                                                                {
    #                                                                    "productCode": "T0102010026",
    #                                                                    "actualQuantity": "1"
    #                                                                },
    #                                                                {
    #                                                                    "productCode": "T0103010016",
    #                                                                    "actualQuantity": "1"
    #                                                                },
    #                                                                {
    #                                                                    "productCode": "T0103010017",
    #                                                                    "actualQuantity": "1"
    #                                                                },
    #
    #                                                                {
    #                                                                    "productCode": "T0103010011",
    #                                                                    "actualQuantity": "1",
    #                                                                    "receiptTracings": [{
    #                                                                        "tracingCode": "JX010001120",
    #                                                                        "weight": "100"
    #                                                                    }]
    #                                                                },
    #                                                                {
    #                                                                    "productCode": "T0102010024",
    #                                                                    "actualQuantity": "1",
    #                                                                    "receiptTracings": [{
    #                                                                        "tracingCode": "JX010001130",
    #                                                                        "weight": "100"
    #                                                                    }]
    #                                                                },
    #                                                                {
    #                                                                    "productCode": "T0103010015",
    #                                                                    "actualQuantity": "1",
    #                                                                    "receiptTracings": [{
    #                                                                        "tracingCode": "JX010001140",
    #                                                                        "weight": "100"
    #                                                                    }]
    #                                                                },
    #                                                                {
    #                                                                    "productCode": "T0102010027",
    #                                                                    "actualQuantity": "1",
    #                                                                    "receiptTracings": [{
    #                                                                        "tracingCode": "JX010001150",
    #                                                                        "weight": "100"
    #                                                                    }]
    #                                                                },
    #                                                                {
    #                                                                    "productCode": "T0101020021",
    #                                                                    "actualQuantity": "1",
    #                                                                    "receiptTracings": [{
    #                                                                        "tracingCode": "JX010001160",
    #                                                                        "weight": "100"
    #                                                                    }]
    #                                                                },
    #                                                                {
    #                                                                    "productCode": "T0103010018",
    #                                                                    "actualQuantity": "1",
    #                                                                    "receiptTracings": [{
    #                                                                        "tracingCode": "JX010001170",
    #                                                                        "weight": "100"
    #                                                                    }]
    #                                                                }
    #                                                            ]
    #                                                        ),
    #                                                         qualityResult_=None,
    #                                                        receiptQualityInfo_=None)
    #     print(resp.get('content'))
    #
    # def test_admin_move_pda_pick_submit(self):
    #     invoiceCode_ = "CK202101150155" #出库单号    #     code_ = "JH202101150156"  #拣货单号
    #     productJson_ = json.dumps([{"id":43,
    #                                 "productCode":"T0103010019",
    #                                 "actualQuantity":1,
    #                                 "weight":1,
    # #                                 # 商品创建时有 朔源码，就要下面的数组，没有就不要
    #                                 "sourceList":[{"productCode":"JX010001910",
    #                                                "tracingCode":"JX010001911",
    #                                                "quantity":1,
    #                                                "purchaseWeight":1,
    #                                                "weight":1},
    #                                               {"productCode":"T0103010002",
    #                                                "tracingCode":"JX010006902",
    #                                                "quantity":1,
    #                                                "purchaseWeight":1,
    #                                                "weight":1},
    #                                               {"productCode":"T0103010003",
    #                                                "tracingCode":"JX010007903",
    #                                                "quantity":1,
    #                                                "purchaseWeight":1,
    #                                                "weight":1},
    #                                               {"productCode":"T0103010004",
    #                                                "tracingCode":"JX010008904",
    #                                                "quantity":1,
    #                                                "purchaseWeight":1,
    #                                                "weight":1},
                                                  # {"productCode":"T0103010011",
                                                  #  "tracingCode":"JX010009950",
                                                  #  "quantity":1,
                                                  #  "purchaseWeight":100,
        # #                                           #  "weight":100}
        #                                         ]
        #                         }])
        #
        # resp = self.api._mobile_move_pda_pick_submit(invoiceCode_= invoiceCode_, code_=code_, productJson_=productJson_)
        # print(resp.get('content'))
        #




if __name__ == '__main__':
    unittest.main()
