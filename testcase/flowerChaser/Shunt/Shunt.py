#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log.logger import logger
from testcase.flowerChaser.sql.Bee  import ContainerInformationSql, PurchaseSql
import random
from faker import Faker
import time, datetime
import json


class ContainerMain(unittest.TestCase):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    container = BeeAction()
    container_db = ContainerInformationSql()
    purchase_db = PurchaseSql()
    log = logger('ContainerMain').logger
    log.info("开始执行调车接口测试用例")
    fake = Faker(locale="zh_CN")
    container.set_user('yaxin.guan@worldfarm.com', '123456')

    def test_mobile_shunt_add(self):
        """
        POST _mobile_shunt_add
        调车信息发布 new 2.0
        :return:
        """
        self.container._mobile_shunt_add()
