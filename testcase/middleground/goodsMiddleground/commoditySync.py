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



# 商品档案同步

class commoditySync(unittest.TestCase):
    def setUp(self):
        """
        测试前数据准备
        :return:
        """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')


    # def test_admin_product_sync_push(self):
    #     skus_ = None
    #     subjectCode_ = None
    #     resp = self.api._admin_product_sync_erp_push(skus_=None,
    #                                                  subjectCode_=None)
    #
    def test_admin_product_sync_pageList(self):
        pn_ = 10
        ps_ = 1
        name_ = 'erp'
        skuName_ = None
        subjectId_  = 1
        skuCode_ = None
        status_ = 1
        resp = self.api._admin_product_sync_pageList(pn_= pn_,
                                                     ps_= ps_,
                                                     name_= name_,
                                                     skuName_= skuName_,
                                                     subjectId_= subjectId_,
                                                     skuCode_= skuCode_,
                                                     status_= status_)
        self.assertEqual('OK',resp.get('status'))
        print(resp.get('content'))

    # def test_admin_product_sync_sync(self):
    #     resp = self.api._admin_product_sync_sync(skuCodes_=None,
    #                                              type_=None)





if __name__ == '__main__':
    unittest.main()























