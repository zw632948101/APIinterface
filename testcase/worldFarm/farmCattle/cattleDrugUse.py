#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2020 2020/2/10 13:54
__author__: wei.zhang
牲畜药物记录
"""
import random
from random import choice
from testcase.worldFarm import testCase, CattleManage


class CattleDrugMain(testCase):
    fq = CattleManage()

    def test_mobile_cattle_drug_use_add(self):
        """
        移动端-药物记录-添加-药物记录【v1.2.8可联调】
        :return:
        """
        farmid = self.fq.query_default_farm(self.email)[0].get('farm_id')
        cattleinfo = self.fq.query_livestock_by_farm_id(farmid)
        cattleid = self.tool.data_assemble('id', cattleinfo, random.randint(1, len(cattleinfo) / 2))
        # 药物类型：{"1": "疾病"}, {"2": "疫苗"}, {"3": "超排"}, {"4", "驱虫"}, {"5": "其他"}
        drugType = choice([1, 2, 3, 4, 5])
        useDate = self.tt.get_timestamp()
        drugName = "药物名称%s" % int(useDate / 1000)
        usageDose = random.randint(1, 9999)
        remark = "接口测试添加药物记录备注%s" % useDate
        info = self.ka.mobile_cattle_drug_use_add(cattleIds=cattleid, type=drugType, useDate=useDate,
                                                  drugName=drugName, usageDose=usageDose, remark=remark)
        self.assertEqual(info.get('status'), 'OK')
        druginfo = self.fq.query_cattle_drug_use_info(cattleIds=cattleid, usedate=useDate)
        cattleids = self.tool.data_assemble('cattle_id', druginfo)
        drug = choice(druginfo)
        self.assertListEqual(cattleids, sorted(cattleid))
        self.assertEqual(drugName, drug.get('drug_name'))
        self.assertEqual(useDate, self.tt.str_time_timestamp(drug.get('use_date')))
        self.assertEqual(usageDose, drug.get('usage_dose'))
        self.assertEqual(remark, drug.get('remark'))

    def test_mobile_cattle_drug_use_del(self):
        """
        移动端-药物记录-删除-药物记录【v1.2.8可联调】
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        drugUseId = choice(self.fq.query_default_farn_cattle_drug(farmid)).get('id')
        info = self.ka.mobile_cattle_drug_use_del(drugUseId=drugUseId)
        self.assertEqual(info.get('status'), 'OK')

    def test_mobile_cattle_drug_use_detail(self):
        """
        移动端-药物记录-详情-药物记录【v1.2.8可联调】
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        druginfo = choice(self.fq.query_default_farn_cattle_drug(farmid))
        drugUseId = druginfo.get('id')
        info = self.ka.mobile_cattle_drug_use_detail(drugUseId=drugUseId)
        self.assertEqual(info.get('status'), 'OK')
        content = info.get('content')
        self.assertEqual(content.get('cattleId'), druginfo.get('cattle_id'))
        self.assertEqual(content.get('id'), drugUseId)
        self.assertEqual(content.get('drugName'), druginfo.get('drug_name'))
        self.assertEqual(content.get('remark'), druginfo.get('remark'))
        self.assertEqual(content.get('type'), druginfo.get('type'))
        self.assertEqual(content.get('usageDose'), druginfo.get('usage_dose'))

    def test_mobile_cattle_drug_use_edit(self):
        """
        移动端-药物记录-添加-药物记录【v1.2.8可联调】
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        druginfo = choice(self.fq.query_default_farn_cattle_drug(farmid))
        drugUseId = druginfo.get('id')
        # 药物类型：{"1": "疾病"}, {"2": "疫苗"}, {"3": "超排"}, {"4", "驱虫"}, {"5": "其他"}
        drugType = choice([1, 2, 3, 4, 5])
        useDate = self.tt.get_timestamp()
        drugName = "药物名称%s" % int(useDate / 1000)
        usageDose = random.randint(1, 9999)
        remark = "接口测试添加药物记录备注%s" % useDate
        info = self.ka.mobile_cattle_drug_use_edit(id=drugUseId, type=drugType, useDate=useDate,
                                                   drugName=drugName, usageDose=usageDose, remark=remark)
        self.assertEqual(info.get('status'), 'OK')
        drug = self.fq.query_cattle_drug_use_info(druginfo.get('cattle_id'), useDate)[0]
        self.assertEqual(drugName, drug.get('drug_name'))
        self.assertEqual(useDate, self.tt.str_time_timestamp(drug.get('use_date')))
        self.assertEqual(usageDose, drug.get('usage_dose'))
        self.assertEqual(remark, drug.get('remark'))


if __name__ == '__main__':
    cdm = CattleDrugMain()
