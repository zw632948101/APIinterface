#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/22 16:37
# @Author: wei.zhang
# @File : test_penn_state_separator.py
# @Software: PyCharm
import unittest
from interfaces.beefcattle.BreedAction import breedAction
from ..sql.breed import BullLibrary, CattleFence, PennStateSeparator
from utils.log import log
from faker import Faker
from random import choice, randint
from utils import timestamp,conversion
import json


class TestPennStateSeparator(unittest.TestCase):
    """
    滨州筛模块
    接口文档:http://dev-gateway.worldfarm.com/swagger-ui.html
    """
    breed = breedAction()
    log.info("养殖育肥服务-滨州筛模块")
    fake = Faker(locale="zh_CN")
    bull = BullLibrary()
    fence = CattleFence()
    penn = PennStateSeparator()
    breed.set_user(mobile=15388126072)
    farmid = bull.query_cattle_farm_id(userid=breed.user.user_id)

    def test_admin_penn_state_separator_add(self):
        """
        WEB-滨州筛-添加滨州筛
        :return:
        """
        cattleFarmId = choice(self.farmid).get('id')
        fenceId = choice(self.fence.query_cattle_fence_list(farm_id=cattleFarmId)).get('id')
        # fenceId = None
        makeDate = timestamp.get_timestamp()
        # makeDate = None
        dryMatterRatio = randint(1, 100)
        waterRatio = 100 - dryMatterRatio
        firstFloorRatio = randint(20, 30)
        secondFloorRatio = randint(20, 40)
        threeFloorRatio = randint(20, 40)
        fourFloorRatio = 100 - firstFloorRatio - secondFloorRatio - threeFloorRatio
        fenceRemark = self.fake.text(200)
        resp = self.breed._admin_pennStateSeparator_add(cattleFarmId_=cattleFarmId,
                                                        fenceId_=fenceId, makeDate_=makeDate,
                                                        dryMatterRatio_=dryMatterRatio,
                                                        waterRatio_=waterRatio,
                                                        firstFloorRatio_=firstFloorRatio,
                                                        secondFloorRatio_=secondFloorRatio,
                                                        threeFloorRatio_=threeFloorRatio,
                                                        fourFloorRatio_=fourFloorRatio,
                                                        fenceRemark_=fenceRemark)
        self.assertEqual(resp.get('status'), 'OK')

    def test_admin_penn_state_separator_batch_add(self):
        """
        WEB-滨州筛-批量添加滨州筛
        :return:
        """
        cattleFarmId = choice(self.farmid).get('id')
        makeDate = timestamp.get_timestamp()
        dryMatterRatio = randint(1, 100)
        waterRatio = 100 - dryMatterRatio
        firstFloorRatio = randint(20, 30)
        secondFloorRatio = randint(20, 40)
        threeFloorRatio = randint(20, 40)
        fourFloorRatio = 100 - firstFloorRatio - secondFloorRatio - threeFloorRatio
        fenceRemark = self.fake.text(200)
        jsonString = [{"cattleFarmId_": cattleFarmId,
                       "fenceId_": choice(
                           self.fence.query_cattle_fence_list(farm_id=cattleFarmId)).get('id'),
                       "makeDate_": makeDate,
                       "dryMatterRatio_": dryMatterRatio,
                       "waterRatio_": waterRatio,
                       "firstFloorRatio_": firstFloorRatio,
                       "secondFloorRatio_": secondFloorRatio,
                       "threeFloorRatio_": threeFloorRatio,
                       "fourFloorRatio_": fourFloorRatio,
                       "fenceRemark_": fenceRemark} for i in range(10)]
        resp = self.breed._admin_pennStateSeparator_batch_add(cattleFarmId_=cattleFarmId,
                                                              jsonString_=json.dumps(jsonString))
        self.assertEqual(resp.get('status'), 'OK')

    def test_admin_penn_state_separator_list(self):
        """
        WEB-滨州筛-滨州筛列表
        :return:
        """
        pn = 1
        ps = 20
        cattleFarmId = choice(self.farmid).get('id')
        # fenceNo = choice(self.fence.query_cattle_fence_list(farmid=cattleFarmId)).get('fence_no')
        fenceNo = None
        startMakeDate = timestamp.get_standardtime_timestamp(type=-1, week=4)
        endMakeDate = timestamp.get_standardtime_timestamp(day=1)
        resp = self.breed._admin_pennStateSeparator_list(pn_=pn, ps_=ps, cattleFarmId_=cattleFarmId,
                                                         fenceNo_=fenceNo,
                                                         startMakeDate_=startMakeDate,
                                                         endMakeDate_=endMakeDate)
        self.assertEqual(resp.get('status'), 'OK')
        penn = self.penn.query_penn_state_separator_list(farm_id=cattleFarmId, fence_no=fenceNo,
                                                         start_date=startMakeDate,
                                                         end_date=endMakeDate, ps=ps, pn=pn)

        content = resp.get('content')
        penn = conversion.del_dict_value_null(penn)
        for d, p in zip(content.get('datas'), penn):
            self.assertDictEqual(d, p)

    def test_admin_penn_state_separator_detail(self):
        """
        WEB-滨州筛-滨州筛详情
        :return:
        """
        farm_id = choice(self.farmid).get('id')
        penn = choice(self.penn.query_penn_state_separator_list(farm_id=farm_id))
        resp = self.breed._admin_pennStateSeparator_detail(id_=penn.get('id'))
        self.assertEqual(resp.get('status'), 'OK')
        content = resp.get('content')
        penn = conversion.del_dict_value_null(penn)
        self.assertDictEqual(penn, content)

    def test_admin_penn_state_separator_edit(self):
        """
        WEB-滨州筛-滨州筛编辑
        :return:
        """
        farm_id = choice(self.farmid).get('id')
        penn = choice(self.penn.query_penn_state_separator_list(farm_id=farm_id))
        fenceId = choice(self.fence.query_cattle_fence_list(farm_id=farm_id)).get('id')
        # fenceId = None
        makeDate = timestamp.get_timestamp()
        # makeDate = None
        dryMatterRatio = randint(1, 100)
        waterRatio = 100 - dryMatterRatio
        # waterRatio = None
        firstFloorRatio = randint(20, 30)
        secondFloorRatio = randint(20, 40)
        threeFloorRatio = randint(20, 40)
        fourFloorRatio = 100 - firstFloorRatio - secondFloorRatio - threeFloorRatio
        # fourFloorRatio = None
        fenceRemark = self.fake.text(200)
        resp = self.breed._admin_pennStateSeparator_edit(id_=penn.get('id'), fenceId_=fenceId,
                                                         makeDate_=makeDate,
                                                         dryMatterRatio_=dryMatterRatio,
                                                         waterRatio_=waterRatio,
                                                         firstFloorRatio_=firstFloorRatio,
                                                         secondFloorRatio_=secondFloorRatio,
                                                         threeFloorRatio_=threeFloorRatio,
                                                         fourFloorRatio_=fourFloorRatio,
                                                         fenceRemark_=fenceRemark)
        self.assertEqual(resp.get('status'), 'OK')
        plist = self.penn.query_penn_state_separator_list(farm_id=farm_id)
        self.assertNotIn(penn, plist)

    def test_admin_penn_state_separator_del(self):
        """
        WEB-滨州筛-滨州筛编辑
        :return:
        """
        farm_id = choice(self.farmid).get('id')
        penn = choice(self.penn.query_penn_state_separator_list(farm_id=farm_id))
        resp = self.breed._admin_pennStateSeparator_del(id_=penn.get('id'))
        self.assertEqual(resp.get('status'), 'OK')
        plist = self.penn.query_penn_state_separator_list(farm_id=farm_id)
        self.assertNotIn(penn, plist)
