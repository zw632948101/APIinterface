#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2020/1/4 14:32
@Author: hengxin
"""


import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from interfaces.flowerChaser.UserAction import UserAction
from utils.log import log
from testcase.flowerChaser.sql.Passport import PassportInfoSql
from testcase.flowerChaser.sql.Bee import ContainerInformationSql
from testcase.flowerChaser.sql.Bee import NectarSourceInformationSql
from testcase.flowerChaser.sql.WorkRecord import WorkRecordSql
from utils.fake.FakeLocation import FakeLocation
from faker import Faker


class LogListMain(unittest.TestCase):
    """
    接口文档: http://192.168.62.242:36054/swagger-ui.html
    """
    ua = UserAction()
    ba = BeeAction()
    email = 'yaxin.guan@worldfarm.com'
    ba.set_user(email, 123456)
    log.info("开始执行摇蜜日志接口测试用例")
    pis = PassportInfoSql()
    cis = ContainerInformationSql()
    nsi = NectarSourceInformationSql()
    wrs = WorkRecordSql()
    fake = Faker(locale="zh_CN")
    fl = FakeLocation()

    def test_work_log_page_list(self):
        """
        我的日志和全部日志标志为空, 查询日志列表
        :return:
        """
        json_response = self.ba._mobile_work_log_page_list(ps_='', pn_='', onlySelf_='')
        if json_response["status"] == "ERROR":
            self.assertTrue(json_response["errorMsg"].startswith("参数验证错误"))
        else:
            self.assertTrue(False, "我的日志和全部日志标志为空, 查询日志列表成功")

    def test_work_log_page_list_with_authority(self):
        """
        管理员查询所有日志
        :return:
        """
        self.ba.set_user("26632629@qq.com", "123456")
        json_response = self.ba._mobile_work_log_page_list(ps_='100', pn_='1', onlySelf_=False)
        if json_response["status"] == "OK":
            my_log = self.wrs.query_all_log_by_email(self.email)
            # self.assertEqual([], json_response["content"]["datas"])
        else:
            self.assertTrue(False, "非管理员查询全部日志成功")

    def test_work_log_page_list_without_authority(self):
        """
        非管理员查询全部日志
        :return:
        """
        self.ba.set_user("heng.xin@gmail.com.au", "123456")
        json_response = self.ba._mobile_work_log_page_list(ps_='', pn_='', onlySelf_=False)
        if json_response["status"] == "ERROR":
            self.assertEqual("因权限问题无法查看所有日志", json_response["errorMsg"])
        else:
            self.assertTrue(False, "非管理员查询全部日志成功")

    def test_work_log_page_list_mine(self):
        """
        管理员查询我的日志
        :return:
        """
        self.ba.set_user("26632629@qq.com", "123456")
        json_response = self.ba._mobile_work_log_page_list(ps_='', pn_='', onlySelf_=True)
        if json_response["status"] == "OK":
            json_data = json_response["content"]["datas"]
            my_log = self.wrs.query_all_log_by_email(self.email)
            for i in range(len(my_log)):
                self.assertEqual(json_data[i]["address"], my_log[i]["address"])
                self.assertEqual(json_data[i]["creatorHeadImg"], my_log[i]["head_img"])
                self.assertEqual(json_data[i]["creatorId"], my_log[i]["creator_id"])
                self.assertEqual(json_data[i]["creatorName"], my_log[i]["username"])
                self.assertEqual(json_data[i]["id"], my_log[i]["id"])
                self.assertEqual(json_data[i]["type"], my_log[i]["type"])
        else:
            self.assertTrue(False, "非管理员查询全部日志成功")

    def test_ezviz_get_token(self):
        """
        获取萤石云TOKEN
        :return:
        """
        json_response = self.ba._mobile_container_get_token()
        if json_response["status"] == "OK":
            token = "at.4vsqet7o8gbj38899apx6fgs8kj3ukxv-1hqbtct1bt-1d1btou-njdbubrqu"
            self.assertEqual(token, json_response["content"])
        else:
            self.assertTrue(False, "获取萤石云TOKEN失败")
