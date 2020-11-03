"""
! /usr/bin/env python3
-*- coding: UTF-8 -*-
@Time:2020/10/29 9:30
@Author: he.chao
@File : attrManage.py
@Software: PyCharm
@modular:属性管理
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
excelpath = os.path.join(os.path.join(filepath, "caseData"), "caseData_attr.xlsx")  # 获取excel的测试用例数据文件路径
attrAdd_data = excelRead(excelpath, "attrAdd")
attrPageList_data = excelRead(excelpath, "attrPageList")


@ddt
class TestAttrManage(unittest.TestCase):
    def setUp(self):
        """
        测试前数据准备
        :return:
        """
        self.api = ProductAction()
        self.api.set_user(mobile=15388126072)
        self.db = mp_label()
        self.faker = Faker('zh_CN')

    # @unittest.skipIf(runlevel(1), '主流程执行用例，设置等级为2时跳过该用例')
    # def test_admin_attr_add(self):
    #     attrName = self.faker.text(10)
    #     isSale = random.randint(0, 1)
    #     resp = self.api._admin_attr_add(attrName_=attrName, isSale_=isSale)
    #     self.assertEqual("OK",resp["status"],"状态status断言失败")
    #     db_info = self.db.query_mp_attr_info()
    #     self.assertEqual(attrName,jsonpath(db_info,"$..name")[0],"属性名字attrName断言失败")
    #     self.assertEqual(isSale, jsonpath(db_info,"$..is_sale")[0],"是否销售状态isSale断言失败")

    # @data(*attrAdd_data)
    # @unittest.skipIf(runlevel(3), '主流程执行用例，设置等级为4时跳过该用例')
    # def test_admin_attr_add_check(self, caseData):
    #     self.isSale = random.randint(0, 1)
    #     self.attrName = self.faker.pystr(min_chars=5, max_chars=10)
    #     case_title = caseData["case_title"]
    #     case_data = eval(changData(caseData["case_data"], self))
    #     case_expect = eval(changData(caseData["case_expect"], self))
    #     attrName = case_data["attrName"]
    #     isSale = case_data["isSale"]
    #     resp = self.api._admin_attr_add(attrName_=attrName, isSale_=isSale)
    #
    #     try:
    #         self.assertEqual('OK', resp["status"], "状态断言失败")
    #         db_info = self.db.query_mp_attr_info(attrName=attrName, isSale=isSale)
    #         self.assertEqual(attrName, jsonpath(db_info, "$..name")[0], "属性名字段断言失败")
    #         self.assertEqual(isSale, jsonpath(db_info, "$..is_sale")[0], "是否销售属性字段断言失败")
    #     except:
    #         self.assertEqual(case_expect.get("errorCode"), resp.get("errorCode"), "{0}断言失败:{1}"
    #                          .format(case_title, resp.get('errorMsg')))
    #         self.assertEqual(case_expect.get("status"), resp.get("status"), "{0}断言失败{1}:"
    #                          .format(case_title, resp.get('errorMsg')))
    #
    # @unittest.skipIf(runlevel(1), '主流程执行用例，设置等级为2时跳过该用例')
    # def test_admin_attr_list_all(self):
    #     self.api._admin_attr_list_all()
    #     """
    #     所有属性列表
    #     :return:
    #     """
    #     resp = self.api._admin_attr_list_all()
    #     self.assertEqual("OK", resp.get("status"), "status状态断言失败")
    #     db_info = self.db.query_mp_attr_info(all=1)
    #     self.assertEqual(len(resp.get("content")), len(db_info), "回传号段数量与db数量不一致")

    @unittest.skipIf(runlevel(1), '主流程执行用例，设置等级为2时跳过该用例')
    def test_admin_attr_page_list(self):
        """
        分页属性列表
        :return:
        """
        pn = 1
        ps = 5
        db_info = self.db.query_mp_attr_info(lastOne=1)
        attrName = jsonpath(db_info, "$..name")[0]
        isSale = jsonpath(db_info, "$..status")[0]
        resp = self.api._admin_attr_page_list(pn_=pn, ps_=ps, attrName_=attrName, isSale_=isSale)
        print(attrName,resp)
        self.assertEqual("OK", resp["status"], "状态status断言失败")
        self.assertEqual(pn, jsonpath(resp, "$..pn")[0], "pn断言失败")
        self.assertEqual(ps, jsonpath(resp, "$..ps")[0], "ps断言失败")
        self.assertEqual(attrName, jsonpath(resp, "$..name")[0], "ps断言失败")
        self.assertEqual(isSale, jsonpath(resp["content"], "$..isSale")[0], "ps断言失败")

    # @data(*attrPageList_data)
    # @unittest.skipIf(runlevel(3), '主流程执行用例，设置等级为4时跳过该用例')
    # def test_admin_attr_page_list_check(self, caseData):
    #     """
    #     分页属性列表效验字段
    #     :return:
    #     """
    #     self.pn = 1
    #     self.ps = random.randint(1, 100)
    #     db_info = self.db.query_mp_attr_info(all=1)
    #     random_index = random.randint(0, len(db_info) - 1)
    #     random_attr = db_info[random_index]
    #     print(random_attr)
    #     self.attrName = random_attr["name"]
    #     self.isSale = random_attr["is_sale"]
    #     case_title = caseData["case_title"]
    #     case_data = eval(changData(caseData["case_data"], self))
    #     case_expect = eval(changData(caseData["case_expect"], self))
    #     pn = case_data["pn"]
    #     ps = case_data["ps"]
    #     attrName = case_data["attrName"]
    #     isSale = case_data["isSale"]
    #     resp = self.api._admin_attr_page_list(pn_=pn, ps_=ps, attrName_=attrName, isSale_=isSale)
    #     print(resp)
    #     print(attrName, jsonpath(resp, "$..name")[0])
    #     try:
    #         self.assertEqual("OK", resp["status"], "状态断言失败")
    #         self.assertEqual(case_expect["pn"], jsonpath(resp, "$..pn")[0], "页数字段断言失败")
    #         self.assertEqual(case_expect["ps"], jsonpath(resp, "$..ps")[0], "每页显示数量字段断言失败")
    #         self.assertEqual(attrName, jsonpath(resp, "$..name")[0], "属性名字字段断言失败")
    #         self.assertEqual(isSale, jsonpath(resp, "$..isSale")[0], "是否销售属性字段断言失败")
    #         db_info = self.db.query_mp_attr_info(attrName=attrName, isSale=isSale)
    #
    #         print(db_info)
    #         self.assertEqual(len(jsonpath(resp, "$..datas", )[0]), len(db_info), "接口返回与db数据数量效验失败")
    #     except:
    #         self.assertEqual(case_expect.get("errorCode"), resp.get("errorCode"), "{0}断言失败:{1}"
    #                          .format(case_title, resp.get('errorMsg')))
    #         self.assertEqual(case_expect.get("status"), resp.get("status"), "{0}断言失败{1}:"
    #                          .format(case_title, resp.get('errorMsg')))
    #
    # def tearDown(self):
    #     pass


if __name__ == '__main__':
    unittest.main()
