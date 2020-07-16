#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2020 2020/2/10 15:00
__author__: wei.zhang
饲养记录
"""
import json
from random import choice
from testcase.worldFarm import testCase, CattleManage


class CattleDrugMain(testCase):
    fq = CattleManage()

    def __init__(self, methodName='runTest'):
        super(CattleDrugMain, self).__init__(methodName=methodName)
        self.ka.set_user(mobile=self.email, password=self.password)

    def test_mobile_farm_raise_add(self):
        """
        移动端-饲养记录-添加-饲养记录【v1.2.8可联调】
        :return:
        """
        farminfo = choice(self.fq.query_default_farm(self.email))
        farmid = farminfo.get('farm_id')
        regionid = farminfo.get('region_id')
        feedingDate = self.tt.get_timestamp()
        reamrk = "添加饲养记录备注%s" % (feedingDate / 1000)
        detailList = '[{"feedType": "1", "type": "天然牧草1","feedingAmount": 50.0},{"feedType": "2", "type": "天然牧草2","feedingAmount": 50.0},{"feedType": "3", "type": "天然牧草3","feedingAmount": 50.0},{"feedType": "4", "type": "天然牧草4","feedingAmount": 50.0},{"feedType": "5", "type": "天然牧草5","feedingAmount": 50.0},{"feedType": "6", "type": "天然牧草6","feedingAmount": 50.0},{"feedType": "7", "type": "天然牧草7","feedingAmount": 50.0},{"feedType": "1", "type": "天然牧草8","feedingAmount": 50.0},{"feedType": "2", "type": "天然牧草9","feedingAmount": 50.0},{"feedType": "3", "type": "天然牧草10","feedingAmount": 50.0},{"feedType": "4", "type": "天然牧草11","feedingAmount": 50.0},{"feedType": "5", "type": "天然牧草12","feedingAmount": 50.0},{"feedType": "6", "type": "天然牧草13","feedingAmount": 50.0},{"feedType": "7", "type": "天然牧草14","feedingAmount": 50.0},{"feedType": "1", "type": "天然牧草15","feedingAmount": 50.0},{"feedType": "2", "type": "天然牧草16","feedingAmount": 50.0},{"feedType": "3", "type": "天然牧草17","feedingAmount": 50.0},{"feedType": "4", "type": "天然牧草18","feedingAmount": 50.0},{"feedType": "5", "type": "天然牧草19","feedingAmount": 50.0},{"feedType": "6", "type": "天然牧草20","feedingAmount": 50.0},{"feedType": "7", "type": "天然牧草21","feedingAmount": 50.0}]'
        info = self.ka._mobile_farm_raise_add(farmId=farmid, regionId=regionid, feedingDate=feedingDate, remark=reamrk,
                                              detailList=detailList)
        self.assertEqual(info.get('status'), 'OK')

        raiseinfo = self.fq.query_farm_raise_feeding_date(feedingDate=feedingDate / 1000)
        raisedetail = self.fq.query_farm_raise_detail(raiseid=raiseinfo.get('id'))
        raiselist = json.loads(detailList)
        self.assertEqual(farmid, raiseinfo.get('farm_id'))
        self.assertEqual(regionid, raiseinfo.get('region_id'))
        self.assertEqual(feedingDate / 1000, raiseinfo.get('feeding_date'))
        self.assertListEqual(raisedetail, raiselist)

    def test_mobile_farm_raise_detail(self):
        """
        移动端-饲养记录-详情-饲养记录【v1.2.8可联调】
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        raiseinfo = choice(self.fq.query_farm_raise_id(farmid=farmid))
        raiseid = raiseinfo.get('id')
        info = self.ka._mobile_farm_raise_detail(raiseId=raiseid)
        self.assertEqual(info.get('status'), 'OK')
        content = info.get('content')
        self.assertEqual(self.tt.str_time_timestamp(raiseinfo.get('create_time')), content.get('createTime'))
        self.assertEqual(self.tt.str_time_timestamp(raiseinfo.get('feeding_date')), content.get('feedingDate'))
        self.assertEqual(raiseinfo.get('farm_id'), content.get('farmId'))
        self.assertEqual(raiseinfo.get('region_id'), content.get('regionId'))
        self.assertEqual(raiseinfo.get('remark'), content.get('remark'))
        raisedetail = self.fq.query_farm_raise_detail(raiseid=raiseid, feedTypeDesc=1)
        self.assertListEqual(content.get('farmRaiseDetailOutputs'), raisedetail)

    def test_mobile_farm_raise_edit(self):
        """
        移动端-饲养记录-编辑-饲养记录【v1.2.8可联调】
        :return:
        """
        farminfo = choice(self.fq.query_default_farm(self.email))
        farmid = farminfo.get('farm_id')
        regionid = farminfo.get('region_id')
        raiseid = choice(self.fq.query_farm_raise_id(farmid=farmid)).get('id')
        feedingDate = self.tt.get_timestamp()
        reamrk = "添加饲养记录备注%s" % (feedingDate / 1000)
        detailList = '[{"feedType": "1", "type": "天然牧草1","feedingAmount": 50.0},{"feedType": "2", "type": "天然牧草2","feedingAmount": 50.0},{"feedType": "3", "type": "天然牧草3","feedingAmount": 50.0},{"feedType": "4", "type": "天然牧草4","feedingAmount": 50.0},{"feedType": "5", "type": "天然牧草5","feedingAmount": 50.0},{"feedType": "6", "type": "天然牧草6","feedingAmount": 50.0},{"feedType": "7", "type": "天然牧草7","feedingAmount": 50.0},{"feedType": "1", "type": "天然牧草8","feedingAmount": 50.0},{"feedType": "2", "type": "天然牧草9","feedingAmount": 50.0},{"feedType": "3", "type": "天然牧草10","feedingAmount": 50.0},{"feedType": "4", "type": "天然牧草11","feedingAmount": 50.0},{"feedType": "5", "type": "天然牧草12","feedingAmount": 50.0},{"feedType": "6", "type": "天然牧草13","feedingAmount": 50.0},{"feedType": "7", "type": "天然牧草14","feedingAmount": 50.0},{"feedType": "1", "type": "天然牧草15","feedingAmount": 50.0},{"feedType": "2", "type": "天然牧草16","feedingAmount": 50.0},{"feedType": "3", "type": "天然牧草17","feedingAmount": 50.0},{"feedType": "4", "type": "天然牧草18","feedingAmount": 50.0},{"feedType": "5", "type": "天然牧草19","feedingAmount": 50.0},{"feedType": "6", "type": "天然牧草20","feedingAmount": 50.0},{"feedType": "7", "type": "天然牧草21","feedingAmount": 50.0}]'
        info = self.ka._mobile_farm_raise_edit(farmId=farmid, regionId=regionid, feedingDate=feedingDate, remark=reamrk,
                                               detailList=detailList, id=raiseid)
        self.assertEqual(info.get('status'), 'OK')

        raiseinfo = self.fq.query_farm_raise_feeding_date(feedingDate=feedingDate / 1000)
        raisedetail = self.fq.query_farm_raise_detail(raiseid=raiseinfo.get('id'))
        raiselist = json.loads(detailList)
        self.assertEqual(farmid, raiseinfo.get('farm_id'))
        self.assertEqual(regionid, raiseinfo.get('region_id'))
        self.assertEqual(feedingDate / 1000, raiseinfo.get('feeding_date'))
        self.assertListEqual(raisedetail, raiselist)

    def test_mobile_farm_raise_list(self):
        """
        移动端-饲养记录-列表-饲养记录【v1.2.8可联调】
        :return:
        """
        farminfo = self.fq.query_default_farm(self.email)
        farmid = farminfo[0].get('farm_id')
        regionid = self.tool.data_assemble('region_id', farminfo)
        info = self.ka._mobile_farm_raise_list(regionIds=regionid, farmId=farmid)
        self.assertEqual(info.get('status'), 'OK')
        raiseinfo = self.fq.query_farm_raise_id(farmid=farmid, limit=20)
        content = info.get('content')
        self.assertEqual(len(content.get('datas')), len(raiseinfo))
        datas = content.get('datas')
        for i in range(len(raiseinfo)):
            self.assertEqual(datas[i].get('createTime'), self.tt.str_time_timestamp(raiseinfo[i].get('create_time')))
            self.assertEqual(datas[i].get('feedingDate'), self.tt.str_time_timestamp(raiseinfo[i].get('feeding_date')))
            self.assertEqual(datas[i].get('id'), raiseinfo[i].get('id'))
            self.assertEqual(datas[i].get('regionId'), raiseinfo[i].get('region_id'))
            self.assertEqual(datas[i].get('remark'), raiseinfo[i].get('remark'))
            raisedeail = self.fq.query_farm_raise_detail(raiseid=raiseinfo[i].get('id'), feedTypeDesc=1)
            farmRaise = datas[i].get('farmRaiseDetailOutputs')
            self.assertListEqual(raisedeail, farmRaise)

    def test_mobile_farm_raise_del(self):
        """
        移动端-饲养记录-删除-饲养记录【v1.2.8可联调】
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        raiseid = choice(self.fq.query_farm_raise_id(farmid=farmid)).get('id')
        info = self.ka._mobile_farm_raise_del(raiseId=raiseid)
        self.assertEqual(info.get('status'), 'OK')
        isdel = self.fq.query_farm_raise(raiseid=raiseid)
        self.assertEqual(isdel.get('is_delete'), 1)
