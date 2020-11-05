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


class cartAdd(unittest.TestCase):
    def setUp(self):
        """
                测试前数据准备
                :return:
                """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')

    def test_web_cart_add(self):
        pass