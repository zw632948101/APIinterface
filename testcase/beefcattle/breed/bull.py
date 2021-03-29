#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/20 14:14
# @Author: wei.zhang
# @File : bull.py
# @Software: PyCharm

import unittest
from interfaces.beefcattle.BreedAction import breedAction
from utils.fake.FakeLocation import FakeLocation
from ..sql.breed import BullLibrary
from utils.log import log
from faker import Faker
from random import choice, randint
from utils import timestamp


class BullLibraryCase(unittest.TestCase):
    """
    本地公牛库模块
    接口文档:http://dev-gateway.worldfarm.com/swagger-ui.html
    """
    breed = breedAction()
    log.info("养殖育肥服务-公牛库模块测试")
    fake = Faker(locale="zh_CN")
    loaction = FakeLocation()
    bull = BullLibrary()
    breed.set_user(mobile=15388126072)
    farmid = bull.query_cattle_farm_id(userid=660)

    def test_admin_bull_add(self):
        """
        WEB-公牛库-添加公牛
        :return:
        """
        cattleNo = 'GN' + str(timestamp.get_timestamp())
        # cattleNo = 'GN1616396115000'
        cattleFarmId = choice(self.farmid).get('id')
        frozenSemenNo = 'DJ' + str(timestamp.get_timestamp())
        variety = choice(self.bull.query_cattle_config_variety()).get('code')
        fatherNo = 'F' + str(timestamp.get_timestamp())
        motherNo = 'M' + str(timestamp.get_timestamp())
        sexControlStatus = choice([0, 1])
        remark = self.fake.text(20)
        resp = self.breed._admin_bull_add(cattleNo_=cattleNo, cattleFarmId_=cattleFarmId,
                                          frozenSemenNo_=frozenSemenNo, variety_=variety,
                                          fatherNo_=fatherNo, motherNo_=motherNo, remark_=remark,
                                          sexControlStatus_=sexControlStatus)
        self.assertEqual(resp.get('status'), 'OK')
        bullinfo = self.bull.query_bull_info_list(cattle_no=cattleNo, farmid=cattleFarmId)
        self.assertEqual(len(bullinfo), 1)

    def test_admin_bull_newBullNo(self):
        """
        新建公牛获取公牛编号
        :return:
        """
        farmid = choice(self.farmid).get('id')
        resp = self.breed._admin_bull_newBullNo(cattleFarmId_=farmid)
        self.assertEqual(resp.get('status'), 'OK')

    def test_admin_bull_list(self):
        """
        WEB-公牛库-公牛列表
        :return:
        """
        farmid = choice(self.farmid).get('id')
        pn = 1
        ps = 20
        variety = choice(self.bull.query_cattle_config_variety()).get('code')
        frozenSemen = None
        cattleNo = None
        resp = self.breed._admin_bull_list(cattleFarmId_=farmid, variety_=variety,
                                           frozenSemenNo_=frozenSemen, cattleNo_=cattleNo, ps_=ps,
                                           pn_=pn)
        self.assertEqual(resp.get('status'), 'OK')
        bullListinfo = self.bull.query_bull_info_list(cattle_no=cattleNo, farmid=farmid,
                                                      frozen_no=frozenSemen, variety=variety, ps=ps,
                                                      pn=pn)
        content = resp.get('content')
        self.assertEqual(len(content.get('datas')), len(bullListinfo))
        for datas, bullinfo in zip(content.get('datas'), bullListinfo):
            self.assertDictEqual(datas, bullinfo)

    def test_admin_bull_edit(self):
        """
        WEB-公牛库-编辑
        :return:
        """
        farmid = choice(self.farmid).get('id')
        bullinfo = choice(self.bull.query_bull_info_list(farmid=farmid))
        cattleNo = 'GN' + str(timestamp.get_timestamp())
        frozenSemenNo = 'DJ' + str(timestamp.get_timestamp()) + '123456'
        variety = choice(self.bull.query_cattle_config_variety()).get('code')
        fatherNo = 'F' + str(timestamp.get_timestamp())
        motherNo = 'M' + str(timestamp.get_timestamp())
        sexControlStatus = choice([0, 1])
        remark = self.fake.text(20)
        resp = self.breed._admin_bull_edit(id_=bullinfo.get('id'), frozenSemenNo_=frozenSemenNo,
                                           variety_=variety, fatherNo_=fatherNo, motherNo_=motherNo,
                                           sexControlStatus_=sexControlStatus, remark_=remark,
                                           cattleNo_=cattleNo)
        self.assertEqual(resp.get('status'), 'OK')
        bulllist = self.bull.query_bull_info_list(frozen_no=frozenSemenNo, farmid=farmid,
                                                  variety=variety, cattle_no=cattleNo)
        self.assertNotIn(bullinfo, bulllist)

    def test_admin_bull_detail(self):
        """
        WEB-公牛库-公牛详情
        :return:
        """
        farmid = choice(self.farmid).get('id')
        bullinfo = choice(self.bull.query_bull_info_list(farmid=farmid))
        resp = self.breed._admin_bull_detail(id_=bullinfo.get('id'))
        self.assertEqual(resp.get('status'), 'OK')

    def test_admin_bull_del(self):
        """
        WEB-公牛库-删除公牛
        :return:
        """
        farmid = choice(self.farmid).get('id')
        bullinfo = choice(self.bull.query_bull_info_list(farmid=farmid))
        resp = self.breed._admin_bull_del(id_=bullinfo.get('id'))
        self.assertEqual(resp.get('status'), 'OK')
