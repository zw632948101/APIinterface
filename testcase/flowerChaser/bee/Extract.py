#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log.logger import logger
from testcase.flowerChaser.sql.Bee import ExtractInformationSql, NectarSourceInformationSql, ContainerInformationSql
import random
import json
from faker import Faker
import datetime, time
from datetime import datetime
import requests


class ExtractMain(unittest.TestCase):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    extract = BeeAction()
    extract_db = ExtractInformationSql()
    nectar_source_db = NectarSourceInformationSql()
    container_db = ContainerInformationSql()
    log = logger('ContainerMain').logger
    log.info("开始执行摇蜜管理接口测试用例")
    fake = Faker(locale="zh_CN")
    extract.set_user('19988776600')

    def test_mobile_bee_keeper_list(self):
        """
        POST /mobile/bee-keeper/list 养蜂师傅列表
        :return:
        """
        response = self.extract._mobile_extract_operator_list()
        self.assertEqual(response['status'], "OK")
        return response["content"]

    def test_mobile_extract_operator(self):
        """
        POST /mobile/extract/operator 摇蜜记录操作人列表
        :return:
        """
        response = self.extract._mobile_extract_operator_list()
        self.assertEqual(response['status'], "OK")
        return response["content"]

    def test_mobile_extract_add(self):
        """
        POST /mobile/extract/add 新建摇蜜记录
        :return:
        """
        nectar_source = self.nectar_source_db.sql_nectar_source_id_by_status_id()
        # containers = []
        detail_list = []
        if nectar_source[0]["id"] is not None:
            num = random.randrange(0, len(nectar_source))
            # nectar_source_id = nectar_source[num]["id"]
            nectar_source_id = 213
            # container_list = self.container_db.sql_container_by_nectar_source_id(nectar_source_id)
            # for i in range(3):
            #     num = random.randrange(0, len(container_list))
            #     container_id = container_list[num]["id"]
            #     containers.append(container_id)
            # container = list(set(containers))
            # for j in range(len(container)):
            #     container_ids = {"containerId": container[j], "hiveNum": self.fake.random_int(min=1, max=999)}
            #     detail_list.append(container_ids)
            # detail = json.dumps(detail_list, ensure_ascii=False)
            weight = self.fake.pyfloat(left_digits=6, right_digits=2, positive=True)
            # start_dates = container_list[0]["enter_time"]
            start_date = datetime.strptime(self.fake.date(), '%Y-%m-%d')
            end_data = datetime.now()
            enter_time = self.fake.date_time_between(start_date=start_date, end_date=end_data)
            gather_time = int(enter_time.timestamp() * 1000)
            operator_list = self.test_mobile_extract_operator()
            operator = operator_list[random.randint(1, 10)]["operatorId"]
            nectar_source_type = random.randint(1001, 1046)
            unit = random.randint(1, 3)
            response = self.extract._mobile_extract_add(nectarSourceId_=nectar_source_id,
                                                        nectarSourceType_=nectar_source_type,
                                                        gatherTime_=gather_time,
                                                        weight_=weight,
                                                        operatorId_=operator,
                                                        unit_=unit)
            if response["status"] == "OK":
                extract_records = self.extract_db.sql_all_extract_record()
                extract_record_detail = extract_records[0]
                self.assertEqual(nectar_source_id, extract_record_detail["nectar_source_id"])
                gather_time_time = time.localtime(gather_time / 1000)
                gather_time_stamp = time.strftime("%Y-%m-%d", gather_time_time)
                self.assertEqual(gather_time_stamp, extract_record_detail["gather_time"])
                if unit == 1:
                    self.assertEqual(weight, extract_record_detail["forklift_barrel"])
                elif unit == 2:
                    self.assertEqual(weight, extract_record_detail["weight"])
                elif unit == 3:
                    self.assertEqual(weight, extract_record_detail["normal_barrel"])
                self.assertEqual(str(operator), extract_record_detail["operator_id"])
                self.assertEqual(str(nectar_source_type), extract_record_detail["nectar_source_type"])
            else:
                self.assertTrue(False, "摇蜜记录添加失败")
        else:
            self.assertTrue(False, "暂无已入驻蜜源地")

    def test_mobile_extract_add_without_nectar_source_id(self):
        """
        POST /mobile/extract/add 新建摇蜜记录 - 蜜源地ID为空
        :return:
        """
        detail = json.dumps([{"containerId": 9, "hiveNum": 288}, {"containerId": 10, "hiveNum": 922}],
                            ensure_ascii=False)
        response = self.extract._mobile_extract_add(nectarSourceId_=None, gatherTime_=1568706985000,
                                                    weight_=675, operator_='张丽娟', unit_=random.randint(1, 3),
                                                    nectarSourceType_=1027)
        self.assertEqual("蜜源id不能为空", response['errorMsg'])

    def test_mobile_extract_add_with_wrong_nectar_source_id(self):
        """
        POST /mobile/extract/add 新建摇蜜记录 - 输入不存在的蜜源地ID
        :return:
        """
        detail = json.dumps([{"containerId": 9, "hiveNum": 288}, {"containerId": 10, "hiveNum": 922}],
                            ensure_ascii=False)
        response = self.extract._mobile_extract_add(nectarSourceId_=0, gatherTime_=1568706985000,
                                                    weight_=675, operator_='张丽娟', unit_=random.randint(1, 3),
                                                    nectarSourceType_=1027)
        self.assertEqual("蜜源不存在", response['errorMsg'])

    # def test_mobile_extract_add_nectar_source_id_mismatch_container_id(self):
    #     """
    #     POST /mobile/extract/add 新建摇蜜记录 - 输入的蜜源ID与养蜂平台ID不匹配
    #     :return:
    #     """
    #     detail = json.dumps([{"containerId": 9, "hiveNum": 288}, {"containerId": 10, "hiveNum": 922}],
    #                         ensure_ascii=False)
    #     response = self.extract._mobile_extract_add(nectarSourceId_=13, gatherTime_=1568706985000,
    #                                                 weight_=675, operator_='张丽娟',  unit_=random.randint(1, 3),
    #                                                 nectarSourceType_=1027)
    #     self.assertEqual("被摇蜜平台(ID:9)未入驻该蜜源地", response['errorMsg'])

    # def test_mobile_extract_add_without_container_id(self):
    #     """
    #     POST /mobile/extract/add 新建摇蜜记录 - 未输入养蜂平台ID
    #     :return:
    #     """
    #     detail = json.dumps([{"containerId": None, "hiveNum": 288}, {"containerId": 10, "hiveNum": 922}],
    #                         ensure_ascii=False)
    #     response = self.extract._mobile_extract_add(nectarSourceId_=8, gatherTime_=1568706985000,
    #                                                 weight_=675, operator_='张丽娟',  unit_=random.randint(1, 3),
    #                                                 nectarSourceType_=1027)
    #     self.assertEqual("被摇蜜平台(ID:null)不存在", response['errorMsg'])

    # def test_mobile_extract_add_without_hive_num(self):
    #     """
    #     POST /mobile/extract/add 新建摇蜜记录 -未输入蜂箱数量
    #     :return:
    #     """
    #     response = self.extract._mobile_extract_add(nectarSourceId_=8, gatherTime_=1568706985000,
    #                                                 weight_=675, operator_='张丽娟',  unit_=random.randint(1, 3),
    #                                                 nectarSourceType_=1027)
    #     self.assertEqual("被摇蜜蜂箱数不能为0", response['errorMsg'])

    def test_mobile_extract_add_with_wrong_type(self):
        """
        POST /mobile/extract/add 新建摇蜜记录 -输入不存在的蜜源品种
        :return:
        """
        detail = json.dumps([{"containerId": 9, "hiveNum": 322}, {"containerId": 10, "hiveNum": 922}],
                            ensure_ascii=False)
        response = self.extract._mobile_extract_add(nectarSourceId_=8, gatherTime_=1568706985000,
                                                    weight_=675, operator_='张丽娟',  unit_=random.randint(1, 3),
                                                    nectarSourceType_=1207)
        self.assertEqual("蜜源类型不存在", response['errorMsg'])

    def test_mobile_extract_detail(self):
        """
        POST /mobile/extract/detail 摇蜜记录详情
        :return:
        """
        extract_record = self.extract_db.sql_all_extract_record()
        if extract_record[0]["id"] is not None:
            num = random.randrange(0, len(extract_record))
            extract_record_id = extract_record[num]["id"]
            response = self.extract._mobile_extract_detail(extract_record_id)
            self.assertEqual(response['status'], "OK")
        else:
            self.assertTrue(False, "暂无摇蜜记录")

    def test_mobile_extract_edit(self):
        """
        POST /mobile/extract/edit 编辑摇蜜记录
        :return:
        """
        extract_records = self.extract_db.sql_all_extract_record()
        if extract_records[0]["id"] is not None:
            num = random.randrange(0, len(extract_records))
            extract_record_id = extract_records[num]["id"]
            weight = self.fake.pyfloat(left_digits=3, right_digits=2, positive=True)
            operator_list = self.test_mobile_extract_operator()
            operator = operator_list[random.randint(1, 10)]
            extract_record_detail = self.extract_db.sql_extract_record_detail_by_extract_record_id(extract_record_id)
            detail = []
            for i in range(len(extract_record_detail)):
                container_ids = {"containerId": extract_record_detail[i]["container_id"],
                                 "hiveNum": self.fake.random_int(min=1, max=999)}
                detail.append(container_ids)
            extract_record = self.extract_db.sql_extract_record_by_extract_record_id(extract_record_id)
            gather_times = extract_record[0]["gather_time"]
            # enter_time = extract_record_detail[0]["enter_time"]
            time = datetime.strptime(gather_times, '%Y-%m-%d')
            gather_time = int(time.timestamp() * 1000)
            response = self.extract._mobile_extract_edit(id_=extract_record_id, weight_=weight, operator_=operator,
                                                         unit_=random.randint(1, 3), gatherTime_=gather_time)
            self.assertEqual(response['status'], "OK")
        else:
            self.assertTrue(False, "暂无摇蜜记录")

    def test_mobile_extract_edit_with_gather_time(self):
        """
        POST /mobile/extract/edit 编辑摇蜜记录-更改摇蜜时间
        :return:
        """
        response = self.extract._mobile_extract_edit(id_=12, weight_=79.82, operator_="蜂友10001",
                                                     unit_=3,
                                                     gatherTime_=1192636800000)
        self.assertEqual(response['status'], "OK")

    def test_mobile_extract_edit_with_wrong_gather_time(self):
        """
        POST /mobile/extract/edit 编辑摇蜜记录-跨月更改摇蜜时间
        :return:
        """
        response = self.extract._mobile_extract_edit(id_=12, weight_=79.82, operator_="蜂友10001",
                                                     unit_=3,
                                                     gatherTime_=1192636800000)
        self.assertEqual("摇蜜时间不能跨月编辑", response['errorMsg'])

    def test_mobile_extract_list(self):
        """
        POST /mobile/extract/list 摇蜜记录列表
        :return:
        """
        response = self.extract._mobile_extract_list()
        self.assertEqual(response['status'], "OK")
