#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log.logger import logger
from testcase.flowerChaser.sql.Bee  import StatisticsSql
import random
import json
from faker import Faker
import datetime
import requests


class NectarSourceMain(unittest.TestCase):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    statistics = BeeAction()
    statistics_db = StatisticsSql()
    log = logger('FarmInformationMain').logger
    log.info("开始执行统计接口测试用例")
    fake = Faker(locale="zh_CN")
    statistics.set_user('15388126072')

    def setUp(self) -> None:
        self.statics_generate()

    def tearDown(self) -> None:
        pass

    def statics_generate(self):
        """
        调用内部API手动刷新数据统计
        :return:
        """
        json_response = self.statistics._api_statistics_generate()
        if json_response["status"] == "OK":
            self.log.info("实时数据刷新成功")
        else:
            self.assertTrue(False, "实时数据刷新失败")

    def test_mobile_statistics_nectar_source(self):
        """
        POST /mobile/statistics/nectar-source 蜜源省分布
        :return:
        """
        json_response = self.statistics._mobile_statistics_nectar_source()
        source_from_db = self.statistics_db.sql_statistics_nectar_source()
        source_by_province = source_from_db[0]
        source_by_province.append(source_from_db[1][0])
        if json_response["status"] == "OK":
            sources_response = json_response["content"]["dataList"]
            for source_db in source_by_province:
                for source_res in sources_response:
                    if source_db["article"] == source_res["article"]:
                        self.assertEqual(str(source_db.get("province", 0)), str(source_res.get("province", 0)))
                        self.assertEqual(int(source_db["readyNum"]), source_res["readyNum"])
                        self.assertEqual(int(source_db["workingNum"]), source_res["workingNum"])
                        self.assertEqual(int(source_db["completedNum"]), source_res["completedNum"])
                        self.assertEqual(int(source_db["total"]), source_res["total"])
        else:
            self.assertTrue(False, "蜜源省分布接口报错")

    def test_mobile_statistics_nectar_source_type(self):
        """
        POST /mobile/statistics/nectar-source-type 蜜源类型饼图
        :return:
        """
        json_response = self.statistics._mobile_statistics_nectar_source_type()
        source_type_from_db = self.statistics_db.sql_statistics_nectar_source_type()
        if json_response["status"] == "OK":
            sources_response = json_response["content"]["typeCountList"]
            for source_db in source_type_from_db:
                for source_res in sources_response:
                    if source_db["typeName"] == source_res["typeName"]:
                        self.assertEqual(source_db["typeCode"], source_res["typeCode"])
                        self.assertEqual(source_db["typeNum"], source_res["typeNum"])
        else:
            self.assertTrue(False, "蜜源类型饼图接口报错")

    def test_mobile_statistics_nectar_type(self):
        """
        POST /mobile/statistics/nectar-type 蜂蜜类型
        :return:
        """
        json_response = self.statistics._mobile_statistics_nectar_type()
        honey_weight_from_db = self.statistics_db.sql_statistics_nectar_type()
        if json_response["status"] == "OK":
            honey_weight_from_response = json_response["content"]["typeCountList"]
            for source_db in honey_weight_from_db:
                for source_res in honey_weight_from_response:
                    if source_db["typeName"] == source_res["typeName"]:
                        self.assertEqual(source_db["typeCode"], source_res["typeCode"])
                        self.assertEqual(source_db["typeWeight"], source_res["typeWeight"])
        else:
            self.assertTrue(False, "蜂蜜类型接口报错")

    def test_mobile_statistics_container(self):
        """
        POST /mobile/statistics/container 平台数量
        :return:
        """
        start_time = 1578128155078
        json_response = self.statistics._mobile_statistics_container()
        if json_response["status"] == "OK":
            container_month_report = self.statistics_db.query_count_of_container(start_time / 1000)
            for source_db in container_month_report:
                for source_res in json_response["content"]["data"]:
                    if source_db["label"] == source_res["label"]:
                        self.assertEqual([int(x) for x in source_db["value"].split(',')], source_res["value"])
        else:
            self.assertTrue(False, "平台数量接口报错")

    def test_mobile_statistics_hive(self):
        """
        POST /mobile/statistics/hive 蜂箱数量
        :return:
        """
        start_time = 1578128155078
        json_response = self.statistics._mobile_statistics_hive()
        if json_response["status"] == "OK":
            hive_month_report = self.statistics_db.query_count_of_hive(start_time / 1000)
            for source_db in hive_month_report:
                for source_res in json_response["content"]["dataList"]:
                    if source_db["monthNo"] == source_res["monthNo"]:
                        self.assertEqual(source_db["hiveNum"], source_res["hiveNum"])
        else:
            self.assertTrue(False, "蜂箱数量接口报错")

    def test_mobile_statistics_nectar(self):
        """
        POST /mobile/statistics/nectar 蜂蜜数量
        :return:
        """
        start_time = 1578128155078
        json_response = self.statistics._mobile_statistics_nectar()
        if json_response["status"] == "OK":
            honey_month_report = self.statistics_db.query_count_of_honey(start_time /1000)
            res_data_list = json_response["content"]["dataList"]
            res_data_list.pop()
            for source_db in honey_month_report:
                for source_res in res_data_list:
                    if source_db["monthNo"] == source_res["monthNo"]:
                        self.assertEqual(source_db["hiveNum"], source_res["hiveNum"])
                        self.assertEqual(source_db["containerNum"], source_res["containerNum"])
                        self.assertEqual(source_db["nectarWeight"], source_res["nectarWeight"])
                        self.assertEqual(source_db["avg"], source_res["avg"])
        else:
            self.assertTrue(False, "蜂蜜数量接口报错")
