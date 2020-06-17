#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from actions.BeeAction import BeeAction
from tools.Config import Log
from sql.Shunt import ShuntingRecordsSql
from testCase.FakeLocation import FakeLocation
import random
import json
from faker import Faker
import datetime, time
import re

class NectarSourceMain(unittest.TestCase):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    shunt_manage = BeeAction()
    shunt_record_db = ShuntingRecordsSql()
    fl = FakeLocation()
    log = Log('FarmInformationMain').logger
    log.info("开始执行调车管理测试用例")
    fake = Faker(locale="zh_CN")
    shunt_manage.set_user('19988776600')

    def test_admin_shunt_statistics(self):
        """
        运营后台-调车管理-调车记录统计  new 2.2.1
        :return:
        """
        response = self.shunt_manage._admin_shunt_statistics()
        if response["status"] == "OK":
            shunt_records_status1 = self.shunt_record_db.sql_all_shunt_records_by_status(1)[0]["COUNT(*)"]
            shunt_records_status2 = self.shunt_record_db.sql_all_shunt_records_by_status(2)[0]["COUNT(*)"]
            shunt_records_status3 = self.shunt_record_db.sql_all_shunt_records_by_status(3)[0]["COUNT(*)"]
            shunt_records_status4 = self.shunt_record_db.sql_all_shunt_records_by_status(4)[0]["COUNT(*)"]
            self.assertEqual(response["content"][0]["num"], shunt_records_status1)
            self.assertEqual(response["content"][1]["num"], shunt_records_status2)
            self.assertEqual(response["content"][2]["num"], shunt_records_status3)
            self.assertEqual(response["content"][3]["num"], shunt_records_status4)
        else:
            self.assertTrue(False, "调车记录总数查询失败")

    def test_admin_shunt_page_list(self):
        """
        POST fc-bee/admin/shunt/page-list 调车记录列表
        :return:
        """
        response = self.shunt_manage._admin_shunt_page_list()
        self.assertEqual(response['status'], "OK")

    def test_admin_shunt_page_list_by_usetime(self):
        """
        根据用车时间查询调车记录
        :return:
        """
        start_date = datetime.datetime(year=2020, month=1, day=1)
        end_data = datetime.datetime(year=2020, month=6, day=15)
        use_start = self.fake.date_time_between(start_date=start_date, end_date=end_data)
        use_starts = int(use_start.timestamp() * 1000)
        use_end = self.fake.date_time_between(start_date=start_date, end_date=end_data)
        use_ends = int(use_end.timestamp() * 1000)
        response = self.shunt_manage._admin_shunt_page_list(issuer_=None, shuntStatus_=None,
                                                            startCreateTime_=None, endCreateTime_=None,
                                                            startUseTime_=use_starts, endUseTime_=use_ends)
        if response["status"] == "OK":
            shunt_records = self.shunt_record_db.sql_all_shunt_records_by_usetime(use_start, use_end)
            if len(shunt_records):
                self.assertEqual(response["content"]["tc"], len(shunt_records))
            else:
                self.assertTrue(False, "数据库无查询结果")
        else:
            self.assertTrue(False, "查询失败")

    def test_admin_shunt_page_list_by_createime(self):
        """
        根据发布日期查询调车记录
        :return:
        """
        start_date = datetime.datetime(year=2020, month=1, day=1)
        end_data = datetime.datetime(year=2020, month=6, day=15)
        create_start = self.fake.date_time_between(start_date=start_date, end_date=end_data)
        create_starts = int(create_start.timestamp() * 1000)
        create_end = self.fake.date_time_between(start_date=start_date, end_date=end_data)
        create_ends = int(create_end.timestamp() * 1000)
        response = self.shunt_manage._admin_shunt_page_list(issuer_=None, shuntStatus_=None,
                                                            startCreateTime_=create_starts, endCreateTime_=create_ends,
                                                            startUseTime_=None, endUseTime_=None)
        if response["status"] == "OK":
            shunt_records = self.shunt_record_db.sql_all_shunt_records_by_createtime(create_start, create_end)
            if len(shunt_records):
                self.assertEqual(response["content"]["tc"], len(shunt_records))
            else:
                self.assertTrue(False, "数据库无查询结果")
        else:
            self.assertTrue(False, "查询失败")

    def test_admin_shunt_page_list_by_issuer(self):
        """
        调车记录--发布人姓名或手机号查询
        :return:
        """
        phone = random.randint(180, 199)
        response = self.shunt_manage._admin_shunt_page_list(issuer_=str(phone))
        if response["status"] == "OK":
            shunt_records = self.shunt_record_db.sql_shunt_page_list_by_issuer(phone)
            if shunt_records:
                self.assertEqual(response["content"]["tc"], len(shunt_records))
            else:
                self.assertTrue(False, "数据库无查询结果")
        else:
            self.assertTrue(False, "查询失败")


