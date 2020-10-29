"""
! /usr/bin/env python3
-*- coding: UTF-8 -*-
@Time:2020/10/29 9:30
@Author: he.chao
@File : setionManage.py
@Software: PyCharm
@modular:号段管理
"""

from interfaces.middleground.ProductAction import ProductAction
from testcase.middleground.sql.goodsMP import mp_label
from utils import runlevel
from ddt import data, ddt
from faker import Faker
import unittest
import random
import os
from utils.excelRead import excelRead
from utils.changData import changData

filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
excelpath = os.path.join(os.path.join(filepath, "caseData"), "caseData_sectionAdd.xlsx")  # 获取excel的测试用例数据文件路径
value = excelRead(excelpath, "sectionAdd")


@ddt
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

    @data(value[0])
    @unittest.skipIf(runlevel(1), '主流程执行用例，设置等级为2时跳过该用例')
    def test_admin_section_add(self, caseData):
        """
        添加号段
        :return:
        """
        self.prefix = self.faker.random_letter()
        self.bizId = 1
        self.num = random.randint(1, 100)
        case_data = eval(changData(caseData["case_data"], self))  # 替换excel用例中请求参数#号的内容
        case_except = eval(changData(caseData["case_expect"], self))  # 替换excel用例中预期结果参数#号的内容
        resp = self.api._admin_section_add(prefix_=case_data["prefix"], bizId_=case_data["bizId"],
                                           num_=case_data["num"])
        self.assertEqual(resp.get('status'), 'OK', resp.get('errorMsg'))
        db_info = self.db.query_mp_section_info()
        db_num = db_info[0].get("end_serial") - db_info[0].get("start_serial") + 1  # 根据db中截止编码和起始编码计算分配数量
        self.assertEqual(db_info[0].get("prefix"), case_except["prefix"])
        self.assertEqual(db_info[0].get("biz_id"), case_except["bizId"])
        self.assertEqual(db_num, case_except["num"])

    @data(*value[1:])
    @unittest.skipIf(runlevel(3), '主流程执行用例，设置等级为4时跳过该用例')
    def test_admin_section_add_check(self, caseData):
        """
        添加号段校验字段
        :return:
        """
        self.prefix = self.faker.random_letter()
        self.bizId = 1
        self.num = random.randint(1, 100)
        caseTitle = caseData["case_title"]
        case_data = eval(changData(caseData["case_data"], self))  # 替换excel用例中请求参数#号的内容
        case_except = eval(changData(caseData["case_expect"], self))  # 替换excel用例中预期结果参数#号的内容
        resp = self.api._admin_section_add(prefix_=case_data["prefix"], bizId_=case_data["bizId"],
                                           num_=case_data["num"])
        try:
            self.assertEqual(resp.get('status'), 'OK', resp.get('errorMsg'))
            db_info = self.db.query_mp_section_info()
            db_num = db_info[0].get("end_serial") - db_info[0].get("start_serial") + 1  # 根据db中截止编码和起始编码计算分配数量
            self.assertEqual(str(case_except["prefix"]), db_info[0].get("prefix"), "前缀断言失败：{0},1{1},2{2}"
                             .format(resp.get('errorMsg')))
            self.assertEqual(case_except["bizId"], db_info[0].get("biz_id"), "所属业务断言失败：{}"
                             .format(resp.get('errorMsg')))
            self.assertEqual(case_except["num"], db_num, "分配号段断言失败：{}".format(resp.get('errorMsg')))
        except:
            self.assertEqual(case_except.get("errorCode"), resp.get("errorCode"), "{0}断言失败:{1}".format(caseTitle))
            self.assertEqual(case_except.get("status"), resp.get("status"), "{0}断言失败{1}:".format(caseTitle))

    def test_admin_section_list_all(self):
        """
        添加号段
        :return:
        """
        resp = self.api._admin_section_list_all()
        self.assertEqual("OK", resp.get("status"), "status状态断言失败")

        len(resp)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
