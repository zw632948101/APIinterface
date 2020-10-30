from utils.log import log
import time
import random
import warnings
from interfaces.middleground.ProductAction import ProductAction
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.brandMP import mp_label
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


class Random:
    # 随机名字
    def create_name(self):
        xs = ["yexin_",
                   "Tom_",
                   "Mary_",
                   "Crazy_",
                   "Python_",
                   "Java_",
                    "PHP",
                    "javascpit",
                    "CSS",
                    "html",
                    "XLMX",
                    "sql",
                    "Ruby",
                    "Go",
                    "Swift"
                   ]
        mz = ["默然",
                   "旅人",
                   "多余",
                   "云中",
                   "残雪",
                   "末世",
                   "桑榆",
                   "扉匣",
                   ]
        sj = time.strftime('%S', time.localtime(time.time())) # 获取当前时间秒

        name = random.choice(xs) + random.choice(mz) + sj
        return name

class brand_data:
    admin_biz_add = [

        {"title":"业务新增","data":{"ruleName_":Random().create_name()},"expect":"OK"},
        {"title":"业务新增-为空","data":{"ruleName_":None},"expect":"ERROR"},
        {"title":"业务新增-为int","data":{"ruleName_":8888},"expect":"ERROR"},
        {"title":"业务新增-长度>20","data":{"ruleName_":"具有某种特征的人典型属于苹果手机山东新增本地确诊病例1例类型的具特征的"},"expect":"ERROR"},
        # {"title":"业务新增-符号","data":{"ruleName_":'******'},"expect":"ERROR"},
        {"title":"业务新增-空格","data":{"ruleName_":"      "},"expect":"ERROR"}
    ]


    admin_biz_change_status = [
            {"title":"业务启用","data":{"id":1,"status":1},"expect":"OK"},
            {"title":"业务禁用","data": {"id":1,"status":2},"expect":"OK"},
            {"title": "业务ID为空", "data": {"id": None, "status":""}, "expect": "ERROR"},
            {"title": "业务status为空", "data": {"id":'', "status": None}, "expect": "ERROR"}


                               ]

    admin_biz_list_enable = [

        {"title": "业务分页", "data": {"pn": 1, "ps": 20}, "expect": "OK"},
        {"title": "业务分页-异常值", "data": {"pn": '搞笑', "ps": '小品'}, "expect": "ERROR"}

    ]
    admin_biz_page_list = []




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


    # @data(*brand_data().admin_biz_add)
    # def test_admin_biz_add(self,case):
    #
    #     ruleName = case['data']['ruleName_']
    #     print(ruleName)
    #     resp = self.api._admin_biz_add(ruleName_= ruleName)
    #     self.assertEqual(case['expect'],resp.get('status'))
    #     if resp.get('status') == 'OK':
    #         # 新增成功，数据库中查出来的名字，跟传入接口的名字相同，PASS
    #         self.assertEqual(self.db.git_admin_biz_add(ruleName)[0]['name'],ruleName)
    #         self.assertTrue(self.db.git_admin_biz_add(ruleName))
    #     else:
    #         pass

    # @data(*brand_data().admin_biz_change_status)
    # def test_admin_biz_change_status(self,case):
    #     id = case['data']['id']
    #     status = case['data']['status']
    #     resp = self.api._admin_biz_change_status(id_=id,status_=status)
    #     self.assertEqual(case['expect'], resp.get('status'))
    #     if resp.get('status') == 'OK':
    #         self.assertEqual(self.db.git_admin_biz_change_status(id,status)[0]['id'],id)
    #         self.assertEqual(self.db.git_admin_biz_change_status(id,status)[0]['status'],status)

    # def test_admin_biz_list_all(self):
    #     resp = self.api._admin_biz_list_all()
    #     self.assertEqual('OK',resp.get('status'))
    #     if resp.get('status') == 'OK':
    #         self.assertEqual(len(self.db.git_admin_biz_list_all()),len(resp['content']))
    #
    # def test_admin_biz_list_enable(self):
    #     resp = self.api._admin_biz_list_enable()
    #     self.assertEqual('OK', resp.get('status'))

    # @data(*brand_data().admin_biz_list_enable)
    # def test_admin_biz_page_list(self,case):
    #     pn = case['data']['pn']
    #     ps = case['data']['ps']
    #     resp = self.api._admin_biz_page_list(pn_=pn,ps_=ps)
    #     self.assertEqual(case['expect'],resp.get('status'))


    def test_admin_brand_change_status(self):
        pass

    def test_admin_brand_edit(self):
        pass
if __name__ == '__main__':
    unittest.main()
