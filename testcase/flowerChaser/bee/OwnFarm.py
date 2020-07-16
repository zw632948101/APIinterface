#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log import log
from testcase.flowerChaser.sql.Bee import ConfigInformationSql, NectarSourceInformationSql, ContainerInformationSql
from utils.fake.FakeLocation import FakeLocation
from faker import Faker

class OwnFarmMain(unittest.TestCase):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    own_bee_farm = BeeAction()
    config_db = ConfigInformationSql()
    nectar_source_db = NectarSourceInformationSql()
    container_db = ContainerInformationSql()
    fl = FakeLocation()
    log.info("开始执行我的蜂场测试用例")
    fake = Faker(locale="zh_CN")
    own_bee_farm.set_user('19988776600')

    def test_mobile_apiary_overview(self):
        """

        :return:
        """
