#! /usr/bin/env python3
# -*- coding: UTF-8 -*-


from unittest import TestCase
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log import log
from testcase.flowerChaser.sql.Bee import BeeSettleInRecordSql
import random
import json
from faker import Faker
import datetime
import requests


class BeeSettleInRecord(TestCase):
    api = BeeAction()
    sql = BeeSettleInRecordSql()
    log.info("开始执行蜜蜂入驻记录接口测试用例")
    fake = Faker(locale="zh_CN")
    api.set_user('15388126080')

    def test_mobile_purchase_enter_save(self):
        """
        mobile/purchase-enter/save
        新增入驻记录
        """
        json_response = self.api._mobile_purchase_enter_save(
            customerId_=1,
            contractNo_='1583113248',
            settledNum_=1,
            nectarSourceId_=123,
            technicianId_=391,
            chiefInspectorId_=431,
            enterTime_=int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)
        )

    def test_mobile_fc_user_technician_list(self):
        """
        mobile/fc-user/technician-list
        技师列表
        :return:
        """
        json_response = self.api._mobile_fc_user_technician_list()

    def test_mobile_fc_user_inspector_list(self):
        """
        mobile/fc-user/inspector-list
        总监列表
        :return:
        """
        json_response = self.api._mobile_fc_user_inspector_list()

    def test_mobile_purchase_purchase_option_list(self):
        """
        mobile/purchase/purchase-option-list
        获取可选择的合同列表
        :return:
        """
        json_response = self.api._mobile_purchase_purchase_option_list(customerId_=1)

    def test_mobile_nectar_source_list(self):
        """
        mobile/nectar-source/list
        可入驻蜜源地列表(无定位)
        :return:
        """
        json_response = self.api._mobile_nectar_source_list(
            excludeStatus_=None,
            includeStatus_=None,
            includeProvince_=None,
            includeCity_=None,
            includeType_=None,
            pn_=1,
            ps_=300,
            searchName_=None,
            searchFlowerStart_=None,
            searchFlowerEnd_=None
        )

    def test_mobile_nectar_source_distance_list(self):
        """
        mobile/nectar-source/distance-list
        获取可选择的合同列表
        :return:
        """
        json_response = self.api._mobile_nectar_source_distance_list(
                                                                    lat_=22.49559,
                                                                    lng_=113.91218
        )

    def test_mobile_purchase_enter_detail(self):
        """
        mobile/purchase-enter/detail
        入驻记录详情
        :return:
        """
        json_response = self.api._mobile_purchase_enter_detail(id_=4)

    def test_mobile_purchase_enter_list(self):
        """
        mobile/purchase-enter/list
        入驻记录列表
        :return:
        """
        json_response = self.api._mobile_purchase_enter_list(pn_=1, ps_=500)

    def test_mobile_customer_valuable_list(self):
        """
        mobile/customer/valuable-list
        入驻时选择可出售人
        :return:
        """
        json_response = self.api._mobile_customer_valuable_list(contactNumber_='123')
