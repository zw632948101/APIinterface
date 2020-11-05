from utils.log import log
import time
import random
import warnings
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.brandMP import mp_label
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest


class releaseManage(unittest.TestCase):
    def setUp(self):
        """
                测试前数据准备
                :return:
                """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')


    #
    # def test_admin_release_opt_release(self):
    #     resp = self.api._admin_release_opt_release(releaseId_=1)
    #     self.assertEqual('OK',resp.get('status'))

    # def test_admin_release_opt_on_off_shelve(self):
    #     resp = self.api._admin_release_opt_on_off_shelve(releaseId_=1, status_=1)
    #     self.assertEqual('OK',resp.get('status'))

    def test_admin_release_opt_page_opt_list(self):
        pn = 1
        ps = 2
        channeld = 1
        labelid = 1
        labelName = ''
        skuName = ''
        resp = self.api._admin_release_opt_page_opt_list(pn_=pn,ps_=ps,channelId_=channeld,labelId_=labelid,labelName_=labelName,skuName_=skuName)
        self.assertEqual('OK',resp.get('status'))
if __name__ == '__main__':
    unittest.main()