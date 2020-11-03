from utils.log import log
import time
import random
import warnings
from interfaces.middleground.ProductAction import ProductAction
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.shopMP import mp_label
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest

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

class shop_data:
    shop_add = [
        {"title":"新增店铺",
         "data":
             {"name": Random().create_name(),"remark":"本店专门营销什么什么商品，假一罚十信誉保证。本店的服务宗旨是用心服务，以诚待人!"}
            ,"expected":"OK"},
        {"title":"店铺名超过20字符",
            "data":{"name":"本店所有的商品照片为专业摄影师拍摄后期精心修制及色彩调整","remark":"本店专门营销什么什么商品，假一罚十信誉保证。"}
            ,"expected":"ERROR"},
        {"title":"店铺说明超过20字符",
         "data":{"name":Random().create_name(),"remark":"本店所有的商品照片为专业摄影师拍摄，后期精心修制及色彩调整，尽量与实际商品保持一致，但由于拍摄时用光、角度、显示器色彩偏差、个人对颜色的认知等方面的差异，导致实物可能会与照片存在一些色差，最终颜色以实际商品为准。请在购买前与我们客服充分沟通后做出慎重选择。色差问题将不被我们认可当退换货的理由!"}
            ,"expected":"ERROR"},
        {"title":"店铺名称为空",
         "data":{"name":None,"remark":"本店专门营销什么什么商品，假一罚十信誉保证。本店的服务宗旨是用心服务，以诚待人!"}
            ,"expected":"ERROR"},
        {"title":"店铺说明为空",
         "data":{"name":Random().create_name(),"remark":None}
            ,"expected":"ERROR"}
    ]
    shop_edit = [
        {"title": "修改店铺信息",
         "data":
             {"name": Random().create_name(), "remark": "一间芝麻大的小铺 八仙过海各抒己见","isDelete_":0}
            , "expected": "OK"},
        {"title": "修改名字＞20",
         "data":
             {"name": "五月终可开张经营百分热情双倍才行千挑万选献上宝贝", "remark": "一间芝麻大的小铺 八仙过海各抒己见哈哈","isDelete_":0}
            , "expected": "ERROR"},
        {"title": "名字为空",
         "data":
             {"name": None, "remark": "一间芝麻大的小铺 八仙过海各抒己见","isDelete_":0}
            , "expected": "ERROR"},
        {"title": "说明为空",
         "data":
             {"name": Random().create_name(), "remark": None,"isDelete_":0}
            , "expected": "ERROR"}

    ]
    shop_delete = [{"title":"删除店铺","data":{"isDelete_":1},"expected":"OK"},
                   {"title":"删除店铺","data":{"isDelete_":0},"expected":"ERROR"}
                   ]

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
    @data(*shop_data().shop_add)
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
    @data(*shop_data().shop_edit)
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
    @data(*shop_data().shop_delete)
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
