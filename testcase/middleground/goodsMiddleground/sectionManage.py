import unittest
from utils.log import log
from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.goodsMP import mp_label
from utils import runlevel, timestamp
from ddt import data, unpack, ddt
from faker import Faker
import unittest
class TestSectionManage(unittest.TestCase):
    def setUp(self):
        """
                测试前数据准备
                :return:
                """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')
    def tearDown(self):
        pass
    def test_admin_section_add(self):
        self.api._admin_section_add()

if __name__ == '__main__':
    unittest.main()