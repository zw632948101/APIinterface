#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/22 15:09
# @Author: wei.zhang
# @File : test_cowshed.py
# @Software: PyCharm
import unittest
from interfaces.beefcattle.BreedAction import breedAction
from utils.fake.FakeLocation import FakeLocation
from ..sql.breed import BullLibrary, CowshedSql
from utils.log import log
from faker import Faker
from random import choice, randint
from utils import timestamp,conversion


class TestCowshed(unittest.TestCase):
    """
    牛舍
    接口文档:http://dev-gateway.worldfarm.com/swagger-ui.html
    """
    breed = breedAction()
    log.info("养殖育肥服务-公牛库模块测试")
    fake = Faker(locale="zh_CN")
    loaction = FakeLocation()
    bull = BullLibrary()
    cowshed = CowshedSql()
    breed.set_user(mobile=15388126072)
    farmid = bull.query_cattle_farm_id(userid=660)

    def test_admin_cowshed_newCowshedNo(self):
        """
        WEB-牛舍-新建牛舍获取牛舍编号
        :return:
        """
        resp = self.breed._admin_cowshed_newCowshedNo(cattleFarmId_='1002')
        self.assertEqual(resp.get('status'), 'OK')

    def test_admin_cowshed_add(self):
        """
        WEB-牛舍-新增牛舍
        :return:
        """
        cowshedName = choice(self.bull.query_cattle_config_variety()).get('name') + '牛舍2'
        cattleFarmId = choice(self.farmid).get('id')
        cowNo_info = self.breed._admin_cowshed_newCowshedNo(cattleFarmId_=cattleFarmId)
        cowshedNo = cowNo_info.get('content')
        area = randint(999, 999999)
        epcNo = 'NC' + str(timestamp.get_timestamp())
        remark = self.fake.text(30)
        resp = self.breed._admin_cowshed_add(cowshedName_=cowshedName, cowshedNo_=cowshedNo,
                                             cattleFarmId_=cattleFarmId, area_=area, epcNo_=epcNo,
                                             remark_=remark)
        self.assertEqual(resp.get('status'), 'OK')
        cowsheds = self.cowshed.query_cowshed_list_info(farm_id=cattleFarmId, cowshed_no=cowshedNo,
                                                        cowshed_name=cowshedName, epc_no=epcNo)
        self.assertEqual(len(cowsheds), 1)

    def test_admin_cowshed_edit(self):
        """
        WEB-牛舍-编辑牛舍
        :return:
        """
        cowshed_name = choice(self.bull.query_cattle_config_variety()).get('name') + '牛舍1'
        farm_id = choice(self.farmid).get('id')
        cowshed = choice(self.cowshed.query_cowshed_list_info(farm_id=farm_id))
        area = randint(999, 999999)
        epcNo = 'NC' + str(timestamp.get_timestamp())
        remark = self.fake.text(30)
        resp = self.breed._admin_cowshed_edit(id_=cowshed.get('id'), cowshedName_=cowshed_name,
                                              area_=area, epcNo_=epcNo, remark_=remark)
        self.assertEqual(resp.get('status'), 'OK')
        cowsheds = self.cowshed.query_cowshed_list_info(farm_id=farm_id)
        self.assertNotIn(cowshed, cowsheds)

    def test_admin_cowshed_detail(self):
        """
        WEB-牛舍-牛舍列表
        :return:
        """
        farm_id = choice(self.farmid).get('id')
        cowshed = choice(self.cowshed.query_cowshed_list_info(farm_id=farm_id))
        resp = self.breed._admin_cowshed_detail(id_=cowshed.get('id'))
        self.assertEqual(resp.get('status'), 'OK')
        content = resp.get('content')
        self.assertDictEqual(cowshed, content)

    def test_admin_cowshed_del(self):
        """
        WEB-牛舍-牛舍列表
        :return:
        """
        farm_id = choice(self.farmid).get('id')
        cowshed = choice(self.cowshed.query_cowshed_list_info(farm_id=farm_id))
        resp = self.breed._admin_cowshed_del(id_=cowshed.get('id'))
        self.assertEqual(resp.get('status'), 'OK')
        cowsheds = self.cowshed.query_cowshed_list_info(farm_id=farm_id)
        self.assertNotIn(cowshed, cowsheds)

    def test_admin_cowshed_list(self):
        """
        WEB-牛舍-牛舍列表
        :return:
        """
        farm_id = choice(self.farmid).get('id')
        cowshed_name = None
        cowshed_no = None
        pn = 1
        ps = 20
        resp = self.breed._admin_cowshed_list(pn_=pn, ps_=ps, cattleFarmId_=farm_id,
                                              cowshedName_=cowshed_name, cowshedNo_=cowshed_no)
        self.assertEqual(resp.get('status'), 'OK')
        cowsheds = self.cowshed.query_cowshed_list_info(farm_id=farm_id, cowshed_name=cowshed_name,
                                                        cowshed_no=cowshed_no, pn=pn, ps=ps)
        cowsheds = conversion.del_dict_value_null(cowsheds)
        content = resp.get('content')
        for con, cow in zip(content.get('datas'), cowsheds):
            self.assertDictEqual(con, cow)
