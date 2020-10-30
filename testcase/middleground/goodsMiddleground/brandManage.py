"""
! /usr/bin/env python3
-*- coding: UTF-8 -*-
@Time:2020/10/29 9:30
@Author: he.chao
@File : brandManage.py
@Software: PyCharm
@modular:品牌管理
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
excelpath = os.path.join(os.path.join(filepath, "caseData"), "caseData_brand.xlsx")  # 获取excel的测试用例数据文件路径
brandAdd_data = excelRead(excelpath, "brandAdd")
brandPageList_data = excelRead(excelpath, "brandPageList")


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

    @unittest.skipIf(runlevel(1), '主流程执行用例，设置等级为2时跳过该用例')
    def test_admin_brand_add(self):
        """
        添加品牌
        :return:
        """
        name = self.faker.text(10)
        logo = self.faker.text(20)
        resp = self.api._admin_brand_add(name_=name,logo_=logo)
        self.assertEqual(resp.get('status'), 'OK', resp.get('errorMsg'))
        db_info = self.db.query_mp_brand_info()
        self.assertEqual(db_info[0].get("name"), name)
        self.assertEqual(db_info[0].get("logo"), logo)
        self.assertEqual(db_info[0].get("status"), 0)   #断言创建的品牌状态是启动

    @data(*brandAdd_data)
    @unittest.skipIf(runlevel(3), '主流程执行用例，设置等级为4时跳过该用例')
    def test_admin_brand_add_check(self, caseData):
        """
        添加品牌校验字段
        :return:
        """
        self.name = self.faker.text(10)
        self.logo = self.faker.text(20)
        case_title = caseData["case_title"]
        case_data = eval(changData(caseData["case_data"], self))
        case_expect = eval(changData(caseData["case_expect"], self))
        name = case_data["name"]
        logo = case_data["logo"]
        resp = self.api._admin_brand_add(name_=name, logo_=logo)
        try:
            self.assertEqual(resp.get('status'), 'OK', resp.get('errorMsg'))
            db_info = self.db.query_mp_brand_info()
            self.assertEqual(db_info[0].get("name"), case_expect["name"])
            self.assertEqual(db_info[0].get("logo"), case_expect["logo"])
            self.assertEqual(db_info[0].get("status"), 0)  # 断言创建的品牌状态是启动
        except:
            self.assertEqual(case_expect.get("errorCode"), resp.get("errorCode"), "{0}断言失败:{1}"
                             .format(case_title, resp.get('errorMsg')))
            self.assertEqual(case_expect.get("status"), resp.get("status"), "{0}断言失败{1}:"
                             .format(case_title, resp.get('errorMsg')))
    @unittest.skipIf(runlevel(1), '主流程执行用例，设置等级为2时跳过该用例')
    def test_admin_brand_list_all(self):
        """
        所有品牌列表
        :return:
        """
        resp = self.api._admin_brand_list_all()
        db_info = self.db.query_mp_brand_info(all=1)
        self.assertEqual("OK", resp["status"],"status状态断言失败")
        self.assertEqual(len(resp["content"]), len(db_info),"回传品牌数量与db数量不一致")

    @unittest.skipIf(runlevel(1), '主流程执行用例，设置等级为2时跳过该用例')
    def test_admin_brand_list_enable(self):
        """
        生效品牌列表
        :return:
        """
        resp = self.api._admin_brand_list_enable()
        db_info = self.db.query_mp_brand_info(enable=1)
        self.assertEqual("OK", resp["status"], "status状态断言失败")
        self.assertEqual(len(resp["content"]), len(db_info), "回传品牌数量与db数量不一致")
        for i in resp["content"]:
            if i["status"] != 1:
                raise AssertionError("品牌信息状态非禁用")

    @unittest.skipIf(runlevel(1), '主流程执行用例，设置等级为2时跳过该用例')
    def test_admin_brand_page_list(self):
        pn = 1
        ps = 5
        resp = self.api._admin_brand_page_list(pn_=pn,ps_=ps)
        self.assertEqual("OK", resp.get("status"), "状态断言失败")
        self.assertEqual(pn, jsonpath(resp, "$..pn")[0], "页数字段断言失败")
        self.assertEqual(ps, jsonpath(resp, "$..ps")[0], "页面信息数量字段断言失败")
        db_info = self.db.query_mp_brand_info(pn=pn, ps=ps)
        self.assertEqual(len(jsonpath(resp, "$..datas", )[0]), len(db_info), "接口返回与db数据数量效验失败")

    @data(*brandPageList_data)
    @unittest.skipIf(runlevel(3), '主流程执行用例，设置等级为4时跳过该用例')
    def test_admin_brand_page_list_check(self,caseData):
        self.pn = 1
        self.ps = random.randint(1, 100)
        case_title = caseData["case_title"]
        case_data = eval(changData(caseData["case_data"], self))
        case_except = eval(changData(caseData["case_expect"], self))
        pn = case_data["pn"]
        ps = case_data["ps"]
        resp = self.api._admin_brand_page_list(pn_=pn, ps_=ps)
        try:
            self.assertEqual("OK", resp.get("status"), "状态断言失败")
            self.assertEqual(case_except["pn"], jsonpath(resp, "$..pn")[0], "页数字段断言失败")
            self.assertEqual(case_except["ps"], jsonpath(resp, "$..ps")[0], "每页显示数量字段断言失败")
            db_info = self.db.query_mp_brand_info(pn=pn, ps=ps)
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
