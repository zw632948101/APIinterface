from utils.log import log
from interfaces.wxshop.MallAction import MallAction
from testcase.shop.sql.appletWX import wx_applet_evaluate
from testcase.shop.caseData.applet_data import submit_order
from testcase.shop.sql.webMP import mp_label
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest
import inspect
import json

# 小程序商品收藏
@ddt
class attach_upload(unittest.TestCase):
    def setUp(self):
        """
                测试前数据准备
                :return:
                """
        self.api = MallAction()
        self.api.set_user(mobile=15388126072)
        self.db = wx_applet_evaluate()
        self.faker = Faker('zh_CN')
    # 加入收藏
    @data(*submit_order().web_favorite_add)
    def test_web_favorite_add(self,case):
        skuNo_ = case['data']['skuNo']
        shopId_ = case['data']['shopId']
        resp = self.api._web_favorite_add(skuNo_=skuNo_, shopId_=shopId_)
        self.assertEqual(case['expect'],resp.get('status'))

    # 收藏列表
    def test_web_favorite_list(self):
        resp = self.api._web_favorite_list(pn_=1, ps_=10)
        self.assertEqual('OK',resp.get('status'))
    # 取消收藏
    @data(*submit_order().web_favorite_add)
    def test_web_favorite_cancel(self,case):
        skuNo_ = case['data']['skuNo']
        shopId_ = case['data']['shopId']
        resp = self.api._web_favorite_cancel(skuNo_=skuNo_, shopId_=shopId_)
        self.assertEqual(case['expect'],resp.get('status'))


if __name__ == '__main__':
    unittest.main()
