#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2020 2020/4/01 15:40
蜂友互助
"""

import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.fake.FakeLocation import FakeLocation
from utils.log import log
from testcase.flowerChaser.sql.Bee import VisitRecordSql, HelpSql
from faker import Faker
from utils.dataConversion.dataConversion import DataConversion

import random


class HelpMain(unittest.TestCase, VisitRecordSql, FakeLocation, DataConversion, HelpSql):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    help = BeeAction()
    config_db = VisitRecordSql()
    help_db = HelpSql()
    fl = FakeLocation()
    fake = Faker(locale="zh_CN")
    help.set_user("19999999990")

    def test_mobile_help_info_add(self):
        """
        v2.0 POST /mobile/help-info/add 互助信息新增
        :return:
        """
        type = random.randint(1001, 1006)
        content = self.fake.text(max_nb_chars=50)
        province, city, county, address, lng, lat = self.fl.fake_location()
        images = "[{url:'http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1590128533511.jpg'," \
                 "name:'1.jpg'}," \
                 "{url:'http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1590128552868.jpg'," \
                 "name:'2.jpeg'}," \
                 "{url:'http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1590116956739.jpg'," \
                 "name:'3.jpeg'}]"
        response = self.help._mobile_help_info_add(type_=type, content_=content, province_=province, city_=city,
                                                   county_=county, address_=address, lng_=lng, lat_=lat, images_=images)
        self.assertEqual("OK", response["status"])

    def test_mobile_help_info_update(self):
        """
        v2.0  POST /mobile/help-info/update 互助信息修改
        :return:
        """
        help_info = self.help_db.sql_help_info_by_user_id()
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_info_id = help_info[num]["id"]
            type = random.randint(1001, 1006)
            content = self.fake.text(max_nb_chars=50)
            province, city, county, address, lng, lat = self.fl.fake_location()
            images = "[{url:'http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1585735338203.jpeg'," \
                     "name:'1.jpeg'}]"
            response = self.help._mobile_help_info_update(type_=type, content_=content, province_=province, city_=city,
                                                          county_=county, address_=address, lng_=lng, lat_=lat,
                                                          images_=images, helpInfoId_=help_info_id)
            self.assertEqual("OK", response["status"])

    def test_mobile_help_info_detail(self):
        """
        v2.0 POST /mobile/help-info/detail 互助信息详情
        :return:
        """
        help_info = self.help_db.sql_help_info()
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_info_id = help_info[num]["id"]
            province, city, county, address, lng, lat = self.fl.fake_location()
            response = self.help._mobile_help_info_detail(lng_=lng, lat_=lat, helpInfoId_=help_info_id)
            self.assertEqual("OK", response["status"])

    def test_mobile_help_info_del(self):
        """
        v2.0 POST /mobile/help-info/del 互助信息删除
        :return:
        """
        help_info = self.help_db.sql_help_info_by_user_id()
        help_info = self.help_db.sql_help_info_by_user_id(user_id=513)
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_info_id = help_info[num]["id"]
            response = self.help._mobile_help_info_del(helpInfoId_=help_info_id)
            self.assertEqual("OK", response["status"])

    def test_mobile_help_info_close(self):
        """
        v2.0 POST /mobile/help-info/close 互助信息关闭
        :return:
        """
        help_info = self.help_db.sql_help_info_by_user_id()
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_info_id = help_info[num]["id"]
            response = self.help._mobile_help_info_close(helpInfoId_=6293)
            self.assertEqual("OK", response["status"])

    def test_mobile_help_info_list(self):
        """
        v2.0 POST /mobile/help-info/list 互助信息列表(公开)
        :return:
        """
        response = self.help._mobile_help_info_list(pn_=1, ps_=100)
        self.assertEqual("OK", response["status"])

    def test_mobile_help_info_attention_list(self):
        """
        v2.0 POST /mobile/help-info/attention-list 互助信息相关列表
        :return:
        """
        response = self.help._mobile_help_info_attention_list(pn_=1, ps_=100)
        self.assertEqual("OK", response["status"])

    def test_mobile_help_info_self_list(self):
        """
        v2.0 POST /mobile/help-info/self-list 互助信息自己列表
        :return:
        """
        response = self.help._mobile_help_info_self_list(pn_=1, ps_=100)
        self.assertEqual("OK", response["status"])


    def test_mobile_help_comment_comment(self):
        """
        v2.0 POST /mobile/help-comment/comment 评论/回复
        :return:
        """
        help_info = self.help_db.sql_help_info()
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_info_id = help_info[num]["id"]
            content = self.fake.text(max_nb_chars=50)
            response = self.help._mobile_help_comment_comment(helpInfoId_=6292, helpCommentId_=330, content_=content)
            self.assertEqual("OK", response["status"])

    def test_mobile_help_comment_list(self):
        """
        v2.0 POST /mobile/help-comment/list 评论列表
        :return:
        """
        help_info = self.help_db.sql_help_info()
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_info_id = help_info[num]["id"]
            response = self.help._mobile_help_comment_list(helpInfoId_=help_info_id)
            self.assertEqual("OK", response["status"])

    def test_mobile_help_comment_unread_count(self):
        """
        v2.0 POST /mobile/help-comment/unread-count 评论/回复未读统计
        :return:
        """
        response = self.help._mobile_help_comment_unread_count()
        self.assertEqual("OK", response["status"])

    def test_mobile_help_comment_del(self):
        """
        v2.0 POST /mobile/help-comment/del 评论删除
        :return:
        """
        help_info = self.help_db.sql_help_comment_by_user_id(user_id=515)
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_comment_id = help_info[num]["id"]
            response = self.help._mobile_help_comment_del(helpCommentId_=help_comment_id)
            self.assertEqual("OK", response["status"])

    def test_mobile_help_comment_detail(self):
        """
        v2.0 POST /mobile/help-comment/detail 评论详情
        :return:
        """
        help_info = self.help_db.sql_help_comment()
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_comment_id = help_info[num]["id"]
            response = self.help._mobile_help_comment_detail(helpCommentId_=help_comment_id)
            self.assertEqual("OK", response["status"])

    def test_mobile_share_help_info(self):
        """
        v2.0 POST /mobile/share/help-info 互助信息分享
        :return:
        """
        help_info = self.help_db.sql_help_info()
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_info_id = help_info[num]["id"]
            response = self.help._mobile_share_help_info(helpInfoId_=help_info_id)
            self.assertEqual("OK", response["status"])

    def test_web_help_info_detail(self):
        """
        v2.0 POST POST /web/help-info/detail 互助信息详情
        :return:
        """
        help_info = self.help_db.sql_help_info()
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_info_id = help_info[num]["id"]
            province, city, county, address, lng, lat = self.fl.fake_location()
            response = self.help._web_help_info_detail(lng_=lng, lat_=lat, helpInfoId_=help_info_id)
            self.assertEqual("OK", response["status"])

    def test_web_help_comment_list(self):
        """
        v2.0 POST /web/help-comment/list 评论列表
        :return:
        """
        help_info = self.help_db.sql_help_info()
        if help_info[0]["id"] is not None:
            num = random.randrange(0, len(help_info))
            help_info_id = help_info[num]["id"]
            response = self.help._web_help_comment_list(helpInfoId_=help_info_id)
            self.assertEqual("OK", response["status"])












