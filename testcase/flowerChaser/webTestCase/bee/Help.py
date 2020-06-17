#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2020/04/16
@Author: xiujuan chen
"""


import unittest
from actions.BeeAction import BeeAction
from testCase.FakeLocation import FakeLocation
from sql.Bee import HelpSql
from tools.Config import Log
from faker import Faker
from sql.Passport import PassportInfoSql
import random


class RegisterLoginMain(unittest.TestCase):
    """
    接口文档: http://192.168.62.242:36054/swagger-ui.html
    """
    ba = BeeAction()
    ps = PassportInfoSql()
    fl = FakeLocation()
    help_db = HelpSql()
    mobile = '19982917912'
    log = Log('BeeInformationMain').logger
    log.info("开始执行蜂友互助模块测试用例")
    fake = Faker(locale="zh_CN")
    ba.set_user(mobile)

    def test_admin_help_comment_del(self):
        """
        POST /admin/help-comment/del  V 1.0
        评论删除
        :return:
        """
        help_info = self.help_db.sql_help_comment_by_user_id(user_id=515)
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_comment_id = help_info[num]["id"]
            self.ba._admin_help_comment_del(helpCommentId_=help_comment_id)

    def test_admin_help_comment_list(self):
        """
        POST /admin/help-comment/list  V 1.0
        评论列表
        :return:
        """
        help_info = self.help_db.sql_help_info()
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_info_id = help_info[num]["id"]
            response = self.ba._admin_help_comment_list(helpInfoId_=help_info_id)
            self.assertEqual("OK", response["status"])

    def test_admin_help_info_close(self):
        """
        POST /admin/help-info/close  V 1.0
        互助信息关闭
        :return:
        """
        help_info = self.help_db.sql_help_info_by_user_id()
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_info_id = help_info[num]["id"]
            response = self.ba._admin_help_info_close(helpInfoId_=help_info_id)
            self.assertEqual("OK", response["status"])

    def test_admin_help_info_del(self):
        """
        v2.0 POST /admin/help-info/del 互助信息删除
        :return:
        """
        help_info = self.help_db.sql_help_info_by_user_id()
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_info_id = help_info[num]["id"]
            response = self.ba._admin_help_info_del(helpInfoId_=help_info_id, reasonType_=4)
            self.assertEqual("OK", response["status"])

    def test_admin_help_info_detail(self):
        """
        POST /admin/help-info/detail  V 1.0
        互助信息详情
        :return:
        """
        help_info = self.help_db.sql_help_info()
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_info_id = help_info[num]["id"]
            province, city, county, address, lng, lat = self.fl.fake_location()
            response = self.ba._admin_help_info_detail(lng_=lng, lat_=lat, helpInfoId_=help_info_id, readStatus_=None)
            self.assertEqual("OK", response["status"])

    def test_admin_help_info_list(self):
        """
        POST /admin/help-info/list 互助信息-列表
        :return:
        """
        response = self.ba._admin_help_info_list(pn_=1, ps_=100)
        self.assertEqual("OK", response["status"])

    def test_admin_help_info_total(self):
        """
        POST /admin/help-info/total  V 1.0
        互助信息-总数
        :return:
        """
        self.ba._admin_help_info_total(pn_=None, ps_=None, type_=None, province_=None, city_=None, county_=None,
                                       queryDistance_=None, locationLng_=None, locationLat_=None)

    def test_admin_help_operate_log_list(self):
        """
        POST /admin/help-operate-log/list
        操作日志
        :return:
        """
        help_info = self.help_db.sql_help_info_by_user_id()
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_info_id = help_info[num]["id"]
            self.ba._admin_help_operate_log_list(helpInfoId_=help_info_id)

