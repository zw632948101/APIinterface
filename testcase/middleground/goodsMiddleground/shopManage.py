from utils.log import log
import time
import random
import warnings
from interfaces.middleground.ProductAction import ProductAction
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.caseData.case_api import api_data
from testcase.middleground.sql.shopMP import mp_label
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest



@ddt
class shopManage(unittest.TestCase):
    # 事先查出，最新店铺删除状态
    @classmethod
    def setUpClass(cls):
        global expect
        expect = mp_label().git_admin_shop_add()[0]['is_delete']
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')


    #新增店铺
    @data(*api_data().admin_shop_add)
    def test_admin_shop_add(self,case):
        name = case['data']['name']
        remark = case['data']['remark']
        resp = self.api._admin_shop_add(name_=name,remark_=remark)
        # print(case['data'])
        # print("这是响应实体: %s"%resp)
        self.assertEqual(case['expected'],resp.get('status'))
        # 新增成功，校验参数写入数据库
        if resp.get('status') == 'OK':
            self.assertEqual(self.db.git_admin_shop_add()[0]['name'],name)
            self.assertEqual(self.db.git_admin_shop_add()[0]['remark'],remark)

    #修改最新的店铺基本信息
    @data(*api_data().admin_shop_edit)
    def test_admin_shop_edit(self,case):
        _id= self.db.git_admin_shop_add()[0]['id']
        name = case['data']['name']
        remark = case['data']['remark']
        resp = self.api._admin_shop_edit(id_=_id,name_=name,remark_=remark)
        print(_id,case['data'])
        self.assertEqual(case['expected'],resp.get('status'))
        if resp.get('status') == 'OK':
            self.assertEqual(self.db.git_admin_shop_add()[0]['name'],name)
            self.assertEqual(self.db.git_admin_shop_add()[0]['remark'],remark)

    # #删除最新的店铺
    @data(*api_data().admin_shop_delete)
    def test_admin_shop_fdelete(self,case):
        _id = mp_label().git_admin_shop_add()[0]['id']
        isDelete_ = case['data']['isDelete_']
        actual = mp_label().git_admin_shop_add()[0]['is_delete']

        resp = self.api._admin_shop_delete(id_=_id, isDelete_=isDelete_)
        self.assertEqual(case['expected'],resp.get('status'))

        if resp.get('status') == 'OK':
            self.assertNotEqual(expect,actual)  # 先前的删除状态，和调用删除接口后的状态，不等则PASS
        else:
            pass


    @unittest.skipIf(runlevel(2),"跑主流程时，跳过该用例")
    def test_admin_shop_get(self):
        resp = self.api._admin_shop_get()
        self.assertEqual('OK',resp.get('status'))

    @unittest.skipIf(runlevel(2), "跑主流程时，跳过该用例")
    def test_admin_shop_list_all(self):
        resp = self.api._admin_shop_list_all()
        self.assertEqual('OK', resp.get('status'))
if __name__ == '__main__':
    unittest.main()
