"""
! /usr/bin/env python3
-*- coding: UTF-8 -*-
@Time:2020/10/29 9:30
@Author: he.chao
@File : sectionManage.py
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
from jsonpath import jsonpath

filepath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
excelpath = os.path.join(os.path.join(filepath, "caseData"), "caseData_section.xlsx")  # 获取excel的测试用例数据文件路径
sectionAdd_data = excelRead(excelpath, "sectionAdd")
sectionPageList_data = excelRead(excelpath, "sectionPageList")


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

    @data(sectionAdd_data[0])
    @unittest.skipIf(runlevel(1), '主流程执行用例，设置等级为2时跳过该用例')
    def test_admin_section_add(self, caseData):
        """
        添加号段
        :return:
        """
        self.prefix = self.faker.random_letter()
        self.num = random.randint(1, 100)
        case_data = eval(changData(caseData["case_data"], self))  # 替换excel用例中请求参数#号的内容
        case_except = eval(changData(caseData["case_expect"], self))  # 替换excel用例中预期结果参数#号的内容
        resp = self.api._admin_section_add(prefix_=case_data["prefix"], bizId_=case_data["bizId"],
                                           num_=case_data["num"])
        self.assertEqual(resp.get('status'), 'OK', resp.get('errorMsg'))
        db_info = self.db.query_mp_section_info(lastOne=1)
        db_num = db_info[0].get("end_serial") - db_info[0].get("start_serial") + 1  # 根据db中截止编码和起始编码计算分配数量
        self.assertEqual(db_info[0].get("prefix"), case_except["prefix"])
        self.assertEqual(db_info[0].get("biz_id"), case_except["bizId"])
        self.assertEqual(db_num, case_except["num"])

    @data(*sectionAdd_data[1:])
    @unittest.skipIf(runlevel(3), '主流程执行用例，设置等级为4时跳过该用例')
    def test_admin_section_add_check(self, caseData):
        """
        添加号段校验字段
        :return:
        """
        self.prefix = self.faker.random_letter()
        self.bizId = 1
        self.num = random.randint(1, 100)
        case_title = caseData["case_title"]
        case_data = eval(changData(caseData["case_data"], self))  # 替换excel用例中请求参数#号的内容
        case_except = eval(changData(caseData["case_expect"], self))  # 替换excel用例中预期结果参数#号的内容
        resp = self.api._admin_section_add(prefix_=case_data["prefix"], bizId_=case_data["bizId"],
                                           num_=case_data["num"])
        try:
            self.assertEqual(resp.get('status'), 'OK', resp.get('errorMsg'))
            db_info = self.db.query_mp_section_info(lastOne=1)
            db_num = db_info[0].get("end_serial") - db_info[0].get("start_serial") + 1  # 根据db中截止编码和起始编码计算分配数量
            self.assertEqual(str(case_except["prefix"]), db_info[0].get("prefix"), "前缀断言失败：{}"
                             .format(resp.get('errorMsg')))
            self.assertEqual(case_except["bizId"], db_info[0].get("biz_id"), "所属业务断言失败：{}"
                             .format(resp.get('errorMsg')))
            self.assertEqual(case_except["num"], db_num, "分配号段断言失败：{}".format(resp.get('errorMsg')))
        except:
            self.assertEqual(case_except.get("errorCode"), resp.get("errorCode"), "{0}断言失败:{1}"
                             .format(case_title, resp.get('errorMsg')))
            self.assertEqual(case_except.get("status"), resp.get("status"), "{0}断言失败{1}:"
                             .format(case_title, resp.get('errorMsg')))

    @unittest.skipIf(runlevel(1), '主流程执行用例，设置等级为2时跳过该用例')
    def test_admin_section_list_all(self):
        """
        所有号段列表
        :return:
        """
        resp = self.api._admin_section_list_all()
        self.assertEqual("OK", resp.get("status"), "status状态断言失败")
        db_info = self.db.query_mp_section_info(all=1)
        self.assertEqual(len(resp.get("content")), len(db_info), "回传号段数量与db数量不一致")

    @data(sectionPageList_data[0])
    @unittest.skipIf(runlevel(1), '主流程执行用例，设置等级为2时跳过该用例')
    def test_admin_section_page_list(self, caseData):
        """
        分页号段列表
        :return:
        """
        pn = eval(caseData["case_data"])["pn"]
        ps = eval(caseData["case_data"])["ps"]
        resp = self.api._admin_section_page_list(pn_=pn, ps_=ps)
        self.assertEqual("OK", resp.get("status"), "状态断言失败")
        self.assertEqual(pn, jsonpath(resp, "$..pn")[0], "页数字段断言失败")
        self.assertEqual(ps, jsonpath(resp, "$..ps")[0], "页面信息数量字段断言失败")
        db_info = self.db.query_mp_section_info(pn=pn, ps=ps)
        self.assertEqual(len(jsonpath(resp, "$..datas", )[0]), len(db_info), "接口返回与db数据数量效验失败")

    @data(*sectionPageList_data[1:])
    @unittest.skipIf(runlevel(3), '主流程执行用例，设置等级为4时跳过该用例')
    def test_admin_section_page_list_check(self, caseData):
        """
        分页号段列表效验字段
        :return:
        """
        self.pn = 1
        self.ps = random.randint(1, 100)
        case_title = caseData["case_title"]
        case_data = eval(changData(caseData["case_data"], self))
        case_except = eval(changData(caseData["case_expect"], self))
        pn = case_data["pn"]
        ps = case_data["ps"]
        resp = self.api._admin_section_page_list(pn_=pn, ps_=ps)
        try:
            self.assertEqual("OK", resp.get("status"), "状态断言失败")
            self.assertEqual(case_except["pn"], jsonpath(resp, "$..pn")[0], "页数字段断言失败")
            self.assertEqual(case_except["ps"], jsonpath(resp, "$..ps")[0], "每页显示数量字段断言失败")
            db_info = self.db.query_mp_section_info(pn=pn, ps=ps)
            self.assertEqual(len(jsonpath(resp, "$..datas", )[0]), len(db_info), "接口返回与db数据数量效验失败")
        except:
            self.assertEqual(case_except.get("errorCode"), resp.get("errorCode"), "{0}断言失败:{1}"
                             .format(case_title, resp.get('errorMsg')))
            self.assertEqual(case_except.get("status"), resp.get("status"), "{0}断言失败{1}:"
                             .format(case_title, resp.get('errorMsg')))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
