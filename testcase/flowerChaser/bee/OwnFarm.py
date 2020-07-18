#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log import log
from utils.fake.FakeLocation import FakeLocation
from faker import Faker
import random


class OwnFarmMain(unittest.TestCase):
    """
    接口文档:http://dev-gateway.worldfarm.com/fc-bee/swagger-ui.html#!
    """
    apiary = BeeAction()
    fl = FakeLocation()
    log.info("开始执行我的蜂场测试用例")
    fake = Faker(locale="zh_CN")
    apiary.set_user('15200000003')

    def test_mobile_apiary_edit(self):
        """
        POST /mobile/apiary/edit 蜂场编辑
        v2.3.1 新增
        :return:
        """
        products = random.randint(1, 3)
        major_nectar = random.randint(1001, 1054)
        remark = self.fake.text(max_nb_chars=200)
        swarm_num = random.randint(1, 999999)
        integrated_num = random.randint(1, 999999)
        queen_bee_type = random.randint(1, 3)
        queen_bee_species = random.randint(1, 11)
        response = self.apiary._mobile_apiary_edit(products_=products, majorNectar_=major_nectar, remark_=remark,
                                                   swarmNum_=swarm_num, integratedNum_=integrated_num,
                                                   queenBeeSpecies_=queen_bee_species, queenBeeType_=queen_bee_type,id_='')
        self.assertEqual("OK", response["status"])

    def test_mobile_apiary_detail(self):
        """
        POST /mobile/apiary/detail 蜂场详情
        v2.3.1 新增
        :return:
        """
        response = self.apiary._mobile_apiary_detail()
        self.assertEqual("OK", response["status"])