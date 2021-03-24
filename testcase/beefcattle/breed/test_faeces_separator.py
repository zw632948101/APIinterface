#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/23 10:41
# @Author: wei.zhang
# @File : test_faeces_separator.py
# @Software: PyCharm
import unittest
from interfaces.beefcattle.BreedAction import breedAction
from ..sql.breed import BullLibrary, CattleFence, FaecesSeparator
from utils.log import log
from faker import Faker
from random import choice, randint
from utils import timestamp, conversion
import json


class TestFaecesSeparator(unittest.TestCase):
    """
    粪便筛模块
    接口文档:http://dev-gateway.worldfarm.com/swagger-ui.html
    """
    breed = breedAction()
    log.info("养殖育肥服务-粪便筛模块")
    fake = Faker(locale="zh_CN")
    bull = BullLibrary()
    fence = CattleFence()
    faeces = FaecesSeparator()
    breed.set_user(mobile=15388126072)
    farmid = bull.query_cattle_farm_id(userid=breed.user.user_id)

    def test_admin_faeces_separator_add(self):
        """
        WEB-粪便筛-新建粪便筛
        :return:
        """
        farm_id = choice(self.farmid).get('id')
        fence_id = choice(self.fence.query_cattle_fence_list(farm_id=farm_id)).get('id')
        make_date = timestamp.get_timestamp()
        up_floor_ratio = randint(30, 40)
        middle_floor_ratio = randint(30, 40)
        down_floor_ratio = 100 - up_floor_ratio - middle_floor_ratio
        fence_remark = self.fake.text(200)
        resp = self.breed._admin_faecesSeparator_add(cattleFarmId_=farm_id, fenceId_=fence_id,
                                                     makeDate_=make_date,
                                                     upFloorRatio_=up_floor_ratio,
                                                     middleFloorRatio_=middle_floor_ratio,
                                                     downFloorRatio_=down_floor_ratio,
                                                     fenceRemark_=fence_remark)
        self.assertEqual(resp.get('status'), 'OK')
        faeces_list = self.faeces.query_faeces_separator_list_info(farm_id=farm_id,
                                                                   fence_id=fence_id,
                                                                   end_date=make_date,
                                                                   up_ratio=up_floor_ratio,
                                                                   middle_ratio=middle_floor_ratio,
                                                                   down_ratio=down_floor_ratio,
                                                                   editor_id=self.breed.user.user_id)
        self.assertEqual(len(faeces_list), 1)

    def test_admin_faeces_separator_batch_add(self):
        """
        WEB-粪便筛-新建粪便筛
        :return:
        """
        farm_id = choice(self.farmid).get('id')
        up_floor_ratio = randint(30, 40)
        middle_floor_ratio = randint(30, 40)
        down_floor_ratio = 100 - up_floor_ratio - middle_floor_ratio
        json_string = [{"cattleFarmId": farm_id,
                        "fenceId": choice(self.fence.query_cattle_fence_list(farm_id=farm_id)).get(
                            'id'),
                        "makeDate": timestamp.get_standardtime_timestamp(type=-1,
                                                                         day=randint(1, 30)),
                        "upFloorRatio": up_floor_ratio,
                        "middleFloorRatio": middle_floor_ratio,
                        "downFloorRatio": down_floor_ratio,
                        "fenceRemark": self.fake.text(200)} for i in range(10)]
        resp = self.breed._admin_faecesSeparator_batch_add(cattleFarmId_=farm_id,
                                                           jsonString_=json.dumps(json_string))
        self.assertEqual(resp.get('status'), 'OK')

    def test_admin_faeces_separator_edit(self):
        """
        WEB-粪便筛-编辑粪便筛
        :return:
        """
        farm_id = choice(self.farmid).get('id')
        fence_id = choice(self.fence.query_cattle_fence_list(farm_id=farm_id)).get('id')
        faeces = choice(self.faeces.query_faeces_separator_list_info(farm_id=farm_id))
        make_date = timestamp.get_timestamp()
        up_floor_ratio = randint(30, 40)
        middle_floor_ratio = randint(30, 40)
        down_floor_ratio = 100 - up_floor_ratio - middle_floor_ratio
        fence_remark = self.fake.text(200)
        resp = self.breed._admin_faecesSeparator_edit(fenceId_=fence_id, makeDate_=make_date,
                                                      upFloorRatio_=up_floor_ratio,
                                                      middleFloorRatio_=middle_floor_ratio,
                                                      downFloorRatio_=down_floor_ratio,
                                                      fenceRemark_=fence_remark,
                                                      id_=faeces.get('id'))
        self.assertEqual(resp.get('status'), 'OK')
        faeces_list = self.faeces.query_faeces_separator_list_info(farm_id=farm_id)
        faeces_list = conversion.del_dict_value_null(faeces_list)
        self.assertNotIn(faeces, faeces_list)

    def test_admin_faeces_separator_detail(self):
        """
        WEB-粪便筛-粪便筛详情
        :return:
        """
        farm_id = choice(self.farmid).get('id')
        faeces = choice(self.faeces.query_faeces_separator_list_info(farm_id=farm_id))
        resp = self.breed._admin_faecesSeparator_detail(id_=faeces.get('id'))
        self.assertEqual(resp.get('status'), 'OK')
        faeces = conversion.del_dict_value_null(faeces)
        self.assertDictEqual(faeces, resp.get('content'))

    def test_admin_faeces_separator_del(self):
        """
        WEB-粪便筛-删除粪便筛
        :return:
        """
        farm_id = choice(self.farmid).get('id')
        faeces = choice(self.faeces.query_faeces_separator_list_info(farm_id=farm_id))
        resp = self.breed._admin_faecesSeparator_del(id_=faeces.get('id'))
        self.assertEqual(resp.get('status'), 'OK')
        faeces_list = self.faeces.query_faeces_separator_list_info(farm_id=farm_id)
        self.assertNotIn(faeces, faeces_list)

    def test_admin_faeces_separator_list(self):
        """
        WEB-粪便筛-粪便筛列表
        :return:
        """
        farm_id = choice(self.farmid).get('id')
        fence_no = choice(self.fence.query_cattle_fence_list(farm_id=farm_id)).get('fence_no')
        # fence_no = '05-01'
        pn = 1
        ps = 20
        start_date = timestamp.get_standardtime_timestamp(type=-1, week=randint(8, 40))
        end_date = timestamp.get_standardtime_timestamp(day=1)
        resp = self.breed._admin_faecesSeparator_list(pn_=pn, ps_=ps, cattleFarmId_=farm_id,
                                                      fenceNo_=fence_no, startMakeDate_=start_date,
                                                      endMakeDate_=end_date)
        self.assertEqual(resp.get('status'), 'OK')
        faece_list = self.faeces.query_faeces_separator_list_info(farm_id=farm_id,
                                                                  fence_no=fence_no,
                                                                  start_date=start_date,
                                                                  end_date=end_date, ps=ps, pn=pn)
        content = resp.get('content')
        faeces_list = conversion.del_dict_value_null(faece_list)
        for c, f in zip(content.get('datas'), faeces_list):
            self.assertDictEqual(c, f)
