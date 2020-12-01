from utils.log import log
import time
import random
import warnings
from interfaces.middleground.ProductAction import ProductAction
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.brandMP import mp_label
from testcase.middleground.caseData.case_api import api_data
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest






class tagMdata(object):
    def __init__(self):
        super(tagMdata, self).__init__()
        self.faker = Faker('zh_CN')

    def add_label_data(self):
        """
        添加标签数据
        :return:
        """
        ldata = [None, self.faker.text(21), self.faker.text(20), self.faker.text(20), self.faker.text(20)]
        ltype = [1, 1, '1', None, self.faker.text(10)]
        label_data = [list(i) for i in zip(ldata, ltype)]
        return label_data




@ddt
class brandManage(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')

        # 启用/禁用品牌，接口所需参数(提前查出最新品牌ID)
        # 修改品牌也用这个Id
        self._id = self.db.git_admin_brand_add()[0]['id']



    @data(*api_data().admin_biz_add)
    def test_admin_biz_add(self,case):

        ruleName = case['data']['ruleName_']
        print(ruleName)
        resp = self.api._admin_biz_add(ruleName_= ruleName)
        self.assertEqual(case['expect'],resp.get('status'))
        if resp.get('status') == 'OK':
            # 新增成功，数据库中查出来的名字，跟传入接口的名字相同，PASS
            self.assertEqual(self.db.git_admin_biz_add(ruleName)[0]['name'],ruleName)
            self.assertTrue(self.db.git_admin_biz_add(ruleName))
        else:
            pass

    @data(*api_data().admin_biz_change_status)
    def test_admin_biz_change_status(self,case):
        id = case['data']['id']
        status = case['data']['status']
        resp = self.api._admin_biz_change_status(id_=id,status_=status)
        self.assertEqual(case['expect'], resp.get('status'))
        if resp.get('status') == 'OK':
            self.assertEqual(self.db.git_admin_biz_change_status(id,status)[0]['id'],id)
            self.assertEqual(self.db.git_admin_biz_change_status(id,status)[0]['status'],status)

    @unittest.skipIf(runlevel(2), "跑主流程时，跳过该用例")
    def test_admin_biz_list_all(self):
        resp = self.api._admin_biz_list_all()
        self.assertEqual('OK',resp.get('status'))
        if resp.get('status') == 'OK':
            self.assertEqual(len(self.db.git_admin_biz_list_all()),len(resp['content']))

    @unittest.skipIf(runlevel(2), "跑主流程时，跳过该用例")
    def test_admin_biz_list_enable(self):
        resp = self.api._admin_biz_list_enable()
        self.assertEqual('OK', resp.get('status'))

    @unittest.skipIf(runlevel(2), "跑主流程时，跳过该用例")
    @data(*api_data().admin_biz_list_enable)
    def test_admin_biz_page_list(self,case):
        pn = case['data']['pn']
        ps = case['data']['ps']
        resp = self.api._admin_biz_page_list(pn_=pn,ps_=ps)
        self.assertEqual(case['expect'],resp.get('status'))

    #新增品牌
    @data(*api_data().admin_brand_add)
    def test_admin_brand_add(self,case):
        name = case['data']['name']
        logo = case['data']['logo']
        resp = self.api._admin_brand_add(name_=name,logo_=logo)
        self.assertEqual(case['expect'],resp.get('status'))




    @data(*api_data().admin_brand_status)
    def test_admin_brand_change_status(self,case):
        status = case['data']['status']
        resp = self.api._admin_brand_change_status(id_=self._id,status_=status)
        self.assertEqual(case['expect'],resp.get('status'))
        if resp.get('status') == 'OK':
            self.assertEqual(status,self.db.git_admin_brand_add()[0]['status'])

    @data(*api_data().admin_brand_edit)
    def test_admin_brand_edit(self,case):
        name = case['data']['name']
        resp = self.api._admin_brand_edit(id_=self._id,name_=name)
        self.assertEqual(case['expect'],resp.get('status'))
if __name__ == '__main__':
    unittest.main()
