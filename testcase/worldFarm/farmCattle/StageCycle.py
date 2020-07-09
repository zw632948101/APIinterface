#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Xiujuan Chen'
__date__ = '2019/11/04'
集中测试  牲畜生理周期
"""
import json
import random
import time
from random import choice
from testcase.worldFarm import testCase,CattleManage


class Main(testCase):

    fq = CattleManage()

    def test_mobile_cattle_weaning_add(self):
        """
        新增断奶记录 1.2.4增加
        1.2.6 更改
        :return:
        """
        farm = self.fq.query_default_farm(self.email)
        farmid = choice(farm).get('farm_id')
        regionid = choice(farm).get('region_id')
        weaningdata = self.fq.query_no_weaning_cattle(farmid=farmid)
        if not weaningdata:
            self.log.info("系统中无幼年牲畜")
            return
        cattleids = self.tool.data_assemble('id', weaningdata, random.randint(1, len(weaningdata)))
        weaningDate = int(time.time()) * 1000
        weaningWeight = random.randint(300, 1500)
        info = self.ka.mobile_cattle_weaning_add(cattleIds=cattleids, weaningDate=weaningDate,
                                                 weaningWeight=weaningWeight, regionId=regionid, farmId=farmid)
        self.assertEqual(info['status'], 'OK')
        if len(cattleids) > 1:
            weaninginfo = self.fq.query_cattle_weaning_info(tuple(cattleids))
        else:
            weaninginfo = self.fq.query_cattle_weaning_info(cattleids[0])
        for cattle in weaninginfo:
            weaning_date_table = self.tt.str_time_timestamp(cattle.get('weaning_date'))
            self.assertEqual(weaningDate, weaning_date_table)
            self.assertEqual(cattle.get('weaning_weight'), weaningWeight)

    def test_mobile_cattle_weaning_detail(self):
        """
        查询断奶记录V 1.2.5
        :return:
        """
        weaning_detail = self.fq.query_weaning_detail()
        register = self.ka.mobile_cattle_weaning_detail(cattleWeaningId=weaning_detail.get('id'))
        self.assertEqual(register['status'], 'OK')
        # 判断查询断奶记录体重
        self.assertEqual(weaning_detail.get('weaning_weight'), register['content']['weaningWeight'])
        # 判读查询断奶记录时间
        weaning_date = self.tt.str_time_timestamp(weaning_detail.get('weaning_date'))
        self.assertEqual(weaning_date, register['content']['weaningDate'])

    def test_mobile_cattle_weaning_update(self):
        """
        编辑断奶记录
        :return:
        """
        weaning_detail = self.fq.query_weaning_detail()
        now = int(time.time()) * 1000
        weaning_weight = 200
        self.ka.mobile_cattle_weaning_update(id=weaning_detail.get('id'), weaningDate=now,
                                             weaningWeight=weaning_weight)
        weaning_detail_sql = self.fq.query_weaning_detail_buy_id(weaning_id=weaning_detail.get('id'))
        weaning_date_sql = int(time.mktime(time.strptime(weaning_detail_sql[0]['weaning_date'],
                                                         "%Y-%m-%d %H:%M:%S")) * 1000)
        self.assertEqual(now, weaning_date_sql)
        self.assertEqual(weaning_weight, weaning_detail_sql[0]["weaning_weight"])

    def test_mobile_cattle_breeding_list(self):
        """
        交配列表 V 1.2.6
        :return:
        """
        breeding_info = self.fq.query_new_cattle_breeding_date_buy_email(self.email)
        cattle_id = breeding_info[0]['cattle_id']
        register = self.ka.mobile_cattle_breeding_list(cattleId=cattle_id)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_cattle_breeding_add(self):
        """
        新增交配记录V 1.2.5
        :return:
        """
        end_date = self.tt.get_standardtime_timestamp(week=4, formats="%Y-%m-%d")
        start_date = self.tt.get_standardtime_timestamp(formats="%Y-%m-%d")
        remark = "接口测试新增交配记录备注"

        cow_id_list = self.fq.query_no_breeding_cow_id_buy_email(email=self.email)

        if not cow_id_list:
            self.log.info("当前账号下的农场暂无待交配成年母牛,请先核对")
            return
        cowIds = choice([self.tool.data_assemble('id', cow_id_list, 1),
                         self.tool.data_assemble('id', cow_id_list, random.randint(1, len(cow_id_list)))])

        breedingType = choice([10, 20, 30])
        isRegionSame = 1 if len(cowIds) == 1 else 0

        bullIds = None
        if len(cowIds) == 1 and breedingType == 10:
            bull_id_list = self.fq.query_bull_id_buy_email(email=self.email)
            bullIds = self.tool.data_assemble('id', bull_id_list, 3) if bull_id_list else None
        letter_list = [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)]
        num = ''.join(self.tool.data_assemble(parameters_ld=letter_list, num=8)) if breedingType != 10 else None
        register = self.ka.mobile_cattle_breeding_add(cattleIds=cowIds, bullIds=bullIds, startDate=start_date,
                                                      endDate=end_date, breedingType=breedingType,
                                                      remark=remark, isRegionSame=isRegionSame, num=num)

        self.assertEqual(register.get('status'), 'OK')
        if len(cowIds) > 1:
            cowids_info = self.fq.query_breeding_date_buy_cattle_id(tuple(cowIds), btype=breedingType,
                                                                    sdate=self.tt.timestamp_formatting(
                                                                        start_date / 1000,
                                                                        '%Y-%m-%d'))
        else:
            cowids_info = self.fq.query_breeding_date_buy_cattle_id(cowIds[0], btype=breedingType,
                                                                    sdate=self.tt.timestamp_formatting(
                                                                        start_date / 1000,
                                                                        '%Y-%m-%d'))
        for cattle in cowids_info:
            self.assertEqual(self.tt.str_time_timestamp(cattle.get('start_date')), start_date)
            self.assertEqual(self.tt.str_time_timestamp(cattle.get('end_date')), end_date)
            self.assertEqual(cattle.get('breeding_type'), breedingType)
            self.assertEqual(cattle.get('remark'), remark)
            # 单头牛增加交配记录，断言公牛列表
            if bullIds:
                bullid = self.self.tool.data_assemble('bull_id', cowids_info, len(cowids_info))
                self.assertListEqual(list(map(int, bullid[0].split(','))), bullIds)

    def test_mobile_cattle_breeding_add_num(self):
        """
        新增交配记录V 1.2.5
        V1.2.6 update  交配方式为：人工授精、胚胎移植
        :return:
        """
        end_date = self.tt.get_standardtime_timestamp(week=4, formats="%Y-%m-%d")
        start_date = self.tt.get_standardtime_timestamp(formats="%Y-%m-%d")
        remark = "接口测试新增交配记录备注"
        cow_id_list = self.fq.query_no_breeding_cow_id_buy_email(email=self.email)

        if not cow_id_list:
            self.log.info("当前账号下的农场暂无成年母牛,请先核对")
            return
        cowIds = self.tool.data_assemble('id', cow_id_list, 1)
        breedingType = choice([20, 30])
        letter_list = [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)]
        num = ''.join(self.tool.data_assemble(parameters_ld=letter_list, num=8)) if breedingType != 10 else None
        isRegionSame = 1 if len(cowIds) == 1 else 0
        register = self.ka.mobile_cattle_breeding_add(cattleIds=cowIds, startDate=start_date,
                                                      endDate=end_date, breedingType=breedingType, num=num,
                                                      remark=remark, isRegionSame=isRegionSame)

        self.assertEqual(register.get('status'), 'OK')
        if len(cowIds) > 1:
            cowids_info = self.fq.query_breeding_date_buy_cattle_id(tuple(cowIds), breedingType,
                                                                    self.tt.timestamp_formatting(
                                                                        start_date / 1000,
                                                                        '%Y-%m-%d'))
        else:
            cowids_info = self.fq.query_breeding_date_buy_cattle_id(cowIds[0], breedingType,
                                                                    self.tt.timestamp_formatting(
                                                                        start_date / 1000,
                                                                        '%Y-%m-%d'))

        for cattle in cowids_info:
            self.assertEqual(self.tt.str_time_timestamp(cattle.get('start_date')), start_date)
            self.assertEqual(self.tt.str_time_timestamp(cattle.get('end_date')), end_date)
            self.assertEqual(cattle.get('breeding_type'), breedingType)
            self.assertEqual(cattle.get('remark'), remark)
            self.assertEqual(cattle.get('num'), num)

    def test_mobile_cattle_breeding_update(self):
        """
        修改交配记录  V 1.2.6  交配方式为：自然交配
        :return:
        """
        end_date = self.tt.get_standardtime_timestamp(week=4, formats="%Y-%m-%d")
        start_date = self.tt.get_standardtime_timestamp(formats="%Y-%m-%d")
        remark = "接口测试编辑交配记录备注"
        breeding_id = self.fq.query_new_cattle_breeding_date_buy_email(self.email)

        if not breeding_id:
            self.log.info("当前账号下的农场暂无成年母牛,请先核对")
            return
        breeding_id = choice(breeding_id).get('id')

        breedingType = 10
        isRegionSame = choice([0, 1])

        bull_id_list = self.fq.query_bull_id_buy_email(email=self.email)
        bullIds = self.tool.data_assemble('id', bull_id_list, 3) if bull_id_list else None

        register = self.ka.mobile_cattle_breeding_update(bullIds=bullIds, id=breeding_id, startDate=start_date,
                                                         endDate=end_date, breedingType=breedingType,
                                                         remark=remark, isRegionSame=isRegionSame)

        self.assertEqual(register.get('status'), 'OK')
        cowids_info = self.fq.query_cattle_breeding_id_info(breeding_id)

        for cattle in cowids_info:
            self.assertEqual(self.tt.str_time_timestamp(cattle.get('start_date')), start_date)
            self.assertEqual(self.tt.str_time_timestamp(cattle.get('end_date')), end_date)
            self.assertEqual(cattle.get('breeding_type'), breedingType)
            self.assertEqual(cattle.get('remark'), remark)
            # 单头牛增加交配记录，断言公牛列表
            if bullIds:
                bullid = self.tool.data_assemble('bull_id', cowids_info, len(cowids_info))
                self.assertListEqual(list(map(int, bullid[0].split(','))), bullIds)

    def test_mobile_cattle_breeding_update_num(self):
        """
        修改交配记录V 1.2.5
        V1.2.6 update  交配方式为：人工授精、胚胎移植
        :return:
        """
        end_date = self.tt.get_standardtime_timestamp(week=4, formats="%Y-%m-%d")
        start_date = self.tt.get_standardtime_timestamp(formats="%Y-%m-%d")
        remark = "接口测试编辑交配记录备注 人工授精、胚胎移植"
        breeding_id = self.fq.query_new_cattle_breeding_date_buy_email(self.email)

        if not breeding_id:
            self.log.info("当前账号下的农场暂无成年母牛,请先核对")
            return
        breeding_id = choice(breeding_id).get('id')
        breedingType = choice([20, 30])
        isRegionSame = 0
        bullIds = None
        letter_list = [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)]
        num = ''.join(self.tool.data_assemble(parameters_ld=letter_list, num=8))

        register = self.ka.mobile_cattle_breeding_update(bullIds=bullIds, id=breeding_id, startDate=start_date,
                                                         endDate=end_date, breedingType=breedingType,
                                                         remark=remark, isRegionSame=isRegionSame, num=num)

        self.assertEqual(register.get('status'), 'OK')
        cowids_info = self.fq.query_cattle_breeding_id_info(breeding_id)

        for cattle in cowids_info:
            self.assertEqual(self.tt.str_time_timestamp(cattle.get('start_date')), start_date)
            self.assertEqual(self.tt.str_time_timestamp(cattle.get('end_date')), end_date)
            self.assertEqual(cattle.get('breeding_type'), breedingType)
            self.assertEqual(cattle.get('remark'), remark)
            self.assertEqual(cattle.get('num'), num)

    def test_mobile_cattle_breeding_detail(self):
        """
        交配记录详情 V 1.2.6
        :return:
        """
        breeding_id = (self.fq.query_new_cattle_breeding_date_buy_email(self.email))[0]['id']
        register = self.ka.mobile_cattle_breeding_detail(id=breeding_id)
        breeding_detail = self.fq.query_breeding_detail_buy_id(breeding_id)
        if register['status'] == 'OK':
            self.assertEqual(register['content']['id'], breeding_detail[0]['id'])
            end_date = self.tt.str_time_timestamp(str(breeding_detail[0]['end_date']), "%Y-%m-%d %H:%M:%S")
            start_date = self.tt.str_time_timestamp(str(breeding_detail[0]['start_date']), "%Y-%m-%d %H:%M:%S")
            predict_calving_date = self.tt.str_time_timestamp(str(breeding_detail[0]['predict_calving_date']),
                                                              "%Y-%m-%d %H:%M:%S")
            self.assertEqual(register['content']['startDate'], start_date)
            self.assertEqual(register['content']['endDate'], end_date)
            self.assertEqual(register['content']['breedingType'], breeding_detail[0]['breeding_type'])
            if 'num' in register['content'].keys():
                self.assertEqual(register['content']['num'], breeding_detail[0]['num'])
            if 'bullIds' in register['content'].keys():
                self.assertEqual(register['content']['num'], breeding_detail[0]['bull_ids'])
            if breeding_detail[0]['id'] == 20:
                self.assertEqual(register['content']['breedingTypeDesc'], '人工授精')
            if breeding_detail[0]['id'] == 30:
                self.assertEqual(register['content']['breedingTypeDesc'], '胚胎移植')
            self.assertEqual(register['content']['predictCalvingDate'], predict_calving_date)
            self.assertEqual(register['content']['remark'], breeding_detail[0]['remark'])

    def test_mobile_cattle_preg_add(self):
        """
        新增怀孕记录 V1.2.5 修改
        V 1.2.6 update
        """
        cow_id_list = self.fq.query_cow_cattle_id_list(self.email)
        if not cow_id_list:
            self.log.info("当前账号下的牲畜没有成年母牛或者种母牛!")
            return
        start_date = self.tt.get_standardtime_timestamp(formats="%Y-%m-%d")
        check_result = choice([20, 30])
        remark = '接口测试新增怀孕记录备注'
        images = [{"url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012058085.png",
                   "sortNo": 1}]
        attachment = json.dumps(images)

        Typedict = {"10": "外部观察", "20": "直肠检查", "30": "阴道检查", "40": "其他"}
        checktype = choice(list(Typedict.keys()))
        cow_id = choice(
            [self.tool.data_assemble('id', cow_id_list, 1),
             self.tool.data_assemble('id', cow_id_list, random.randint(1, len(cow_id_list)))])

        cattle = choice(self.fq.query_default_farm(self.email))
        farmId = cattle.get('farm_id')
        regionId = cattle.get('region_id')

        cattleBreedingId = None
        if len(cow_id) == 1:
            breeding = self.fq.query_breeding_date_buy_cattle_id(cow_id[0])
            cattleBreedingId = breeding[0].get('id') if breeding else None

        response = self.ka.mobile_cattle_preg_add(cattleIds=cow_id, checkDate=start_date,
                                                  checkResult=check_result, checkType=checktype,
                                                  remark=remark, farmId=farmId, regionId=regionId,
                                                  cattleBreedingId=cattleBreedingId)
        self.assertEqual(response.get('status'), 'OK')
        if len(cow_id) > 1:
            cowids_info = self.fq.query_cattle_preg_date_info(tuple(cow_id), checktype,
                                                              self.tt.timestamp_formatting(start_date / 1000,
                                                                                           '%Y-%m-%d'),
                                                              check_result)
        else:
            cowids_info = self.fq.query_cattle_preg_date_info(cow_id[0], checktype,
                                                              self.tt.timestamp_formatting(start_date / 1000,
                                                                                           '%Y-%m-%d'),
                                                              check_result)
        for cattle in cowids_info:
            self.assertEqual(self.tt.str_time_timestamp(cattle.get('check_date')), start_date)
            self.assertEqual(cattle.get('check_result'), check_result)
            self.assertEqual(cattle.get('remark'), remark)

    def test_mobile_cattle_preg_detail(self):
        """
        牲畜怀孕记录详情
        :return:
        """
        preg_info = self.fq.query_preg_date_buy_email(self.email)
        preg_id = preg_info[0]['id']
        register = self.ka.mobile_cattle_preg_detail(id=preg_id)
        preg_info_sql = self.fq.query_preg_info_buy_id(preg_id=preg_id)
        check_date = int(time.mktime(time.strptime(preg_info_sql[0]["check_date"],
                                                   "%Y-%m-%d %H:%M:%S")) * 1000)
        self.assertEqual(register['content']['checkDate'], check_date)
        check_result = register['content']['checkResult']
        self.assertEqual(register['content']['checkResult'], check_result)
        if check_result == 10:
            self.assertEqual(register['content']['checkResultDesc'], '待确定')
        if check_result == 20:
            self.assertEqual(register['content']['checkResultDesc'], '空怀')
        if check_result == 30:
            self.assertEqual(register['content']['checkResultDesc'], '怀孕')
        check_type = register['content']['checkType']
        if check_type == 10:
            self.assertEqual(register['content']['checkTypeDesc'], '外部观察')
        if check_type == 20:
            self.assertEqual(register['content']['checkTypeDesc'], '直肠检查')
        if check_type == 30:
            self.assertEqual(register['content']['checkTypeDesc'], '阴道检查')
        if check_type == 40:
            self.assertEqual(register['content']['checkTypeDesc'], '其他')
        self.assertEqual(register['content'].get('remark'), preg_info_sql[0].get('remark'))

    def test_mobile_cattle_preg_update(self):
        """
        修改怀孕记录 V1.2.5 修改
        V 1.2.6 update
        """
        preg_list = self.fq.query_preg_date_buy_email(self.email)
        if not preg_list:
            self.log.info("当前账号的默认农场下，没有牲畜含有怀孕记录!")
            return
        start_date = self.tt.get_standardtime_timestamp(formats="%Y-%m-%d")
        check_result = choice([20, 30])
        remark = '接口测试编辑怀孕记录备注'
        Typedict = {"10": "外部观察", "20": "直肠检查", "30": "阴道检查", "40": "其他"}
        checktype = choice(list(Typedict.keys()))
        cow_id = (self.tool.data_assemble('cattle_id', preg_list, 1))[0]
        cowids_info = self.fq.query_cattle_preg_date_info(cow_id)
        preg_id = cowids_info[0]['id']
        # 判断牲畜是否有交配记录，有交配记录，怀孕记录关联最新的交配记录，无交配记录，怀孕记录不关联交配记录
        newest_breeding_info = self.fq.query_breeding_date_buy_cattle_id(cattle_id=cowids_info[0]['cattle_id'])

        if newest_breeding_info:

            self.ka.mobile_cattle_preg_update(id=preg_id, cattleBreedingId=None,
                                              checkDate=start_date,
                                              checkResult=check_result, checkType=checktype,
                                              remark=remark)
        else:
            breeding_id = newest_breeding_info[0]['id']
            self.ka.mobile_cattle_preg_update(id=preg_id, cattleBreedingId=breeding_id,
                                              checkDate=start_date,
                                              checkResult=check_result, checkType=checktype,
                                              remark=remark)

        cattle = (self.fq.query_preg_info_buy_id(preg_id=preg_id))[0]
        self.assertEqual(self.tt.str_time_timestamp(cattle.get('check_date')), start_date)
        self.assertEqual(cattle.get('check_result'), check_result)
        self.assertEqual(cattle.get('remark'), remark)

    def test_mobile_cattle_calving_add(self):
        """
        新增产犊记录V 1.2.5
        V 1.2.6 update
        :return:
        """
        cow_cattle = self.fq.query_cow_cattle_id_list(email=self.email)
        calving_date = round(int(time.time()) * 1000)
        calving_result = 10
        calving_count = random.randint(1, 2) if calving_result == 10 else None
        calvingSex = choice([10, 20]) if calving_count == 1 else choice([10, 20, 30])
        calvingSex = calvingSex if calving_result == 10 else None
        if cow_cattle:
            cattle_id = choice(cow_cattle).get('id')
            newest_breeding_info = self.fq.query_breeding_date_buy_cattle_id(cattle_id=cattle_id)
            cattle_breeding_id = None
            if newest_breeding_info:
                cattle_breeding_id = choice(newest_breeding_info).get('id')
            self.ka.mobile_cattle_calving_add(cattleId=cattle_id, cattleBreedingId=cattle_breeding_id,
                                              calvingResult=calving_result, calvingSex=calvingSex,
                                              calvingDate=calving_date, calvingCount=calving_count)
            calving_detail = self.fq.query_calving_info_buy_cattle_id(cattle_id=cattle_id)
            calving_date_sql = int(time.mktime(time.strptime(calving_detail[0]["calving_date"],
                                                             "%Y-%m-%d %H:%M:%S")) * 1000)
            self.assertEqual(cattle_breeding_id, calving_detail[0]["cattle_breeding_id"])
            self.assertEqual(calving_result, calving_detail[0]["calving_result"])
            self.assertEqual(calving_date, calving_date_sql)
            self.assertEqual(calving_count, calving_detail[0]['calving_count'])
        else:
            self.log.info('当前账号下的牲畜没有成年母牛或者种母牛!')

    def test_mobile_cattle_calving_update(self):
        """
        修改产犊记录 V 1.2.6
        :return:
        """
        cow_cattle = self.fq.query_cow_cattle_id_list(email=self.email)
        cattle_id = cow_cattle[0]['id']
        calving_detail = self.fq.query_calving_info_buy_cattle_id(cattle_id=cattle_id)
        calving_id = calving_detail[0]['id']
        newest_breeding_info = self.fq.query_breeding_date_buy_cattle_id(cattle_id=cattle_id)
        calving_result = 10
        calving_date = round(int(time.time()) * 1000)
        remark = '修改产犊记录备注'
        if len(newest_breeding_info) == 0:
            self.ka.mobile_cattle_calving_update(id=calving_id, cattleBreedingId=None,
                                                 calvingResult=calving_result, calvingDate=calving_date,
                                                 remark=remark)
            calving_detail = self.fq.query_calving_info_buy_cattle_id(cattle_id=cattle_id)
            calving_date_sql = int(time.mktime(time.strptime(calving_detail[0]["calving_date"],
                                                             "%Y-%m-%d %H:%M:%S")) * 1000)
            self.assertEqual(calving_result, calving_detail[0]["calving_result"])
            self.assertEqual(calving_date, calving_date_sql)
            self.assertEqual(remark, calving_detail[0]['remark'])
        if len(newest_breeding_info) != 0:
            cattle_breeding_id = newest_breeding_info[0]['id']
            self.ka.mobile_cattle_calving_update(id=calving_id, cattleBreedingId=cattle_breeding_id,
                                                 calvingResult=calving_result, calvingDate=calving_date,
                                                 remark=remark)
            calving_detail = self.fq.query_calving_info_buy_cattle_id(cattle_id=cattle_id)
            self.assertEqual(cattle_breeding_id, calving_detail[0]["cattle_breeding_id"])

            calving_date_sql = int(time.mktime(time.strptime(calving_detail[0]["calving_date"],
                                                             "%Y-%m-%d %H:%M:%S")) * 1000)
            self.assertEqual(calving_result, calving_detail[0]["calving_result"])
            self.assertEqual(calving_date, calving_date_sql)
            self.assertEqual(remark, calving_detail[0]['remark'])

    def test_mobile_cattle_calving_detail(self):
        """
        产犊记录详情 V 1.2.6
        :return:
        """
        cow_cattle = self.fq.query_cow_cattle_id_list(email=self.email)
        cattle_id = cow_cattle[0]['id']
        calving_detail = self.fq.query_calving_info_buy_cattle_id(cattle_id=cattle_id)
        calving_id = calving_detail[0]['id']
        register = self.ka.mobile_cattle_calving_detail(id=calving_id)
        calving_detail = self.fq.query_calving_info_buy_cattle_id(cattle_id=cattle_id)
        self.assertEqual(register['content']['calvingCount'], calving_detail[0]['calving_count'])
        calving_date = int(time.mktime(time.strptime(calving_detail[0]['calving_date'], "%Y-%m-%d %H:%M:%S")) * 1000)
        self.assertEqual(register['content']['calvingDate'], calving_date)
        self.assertEqual(register['content']['calvingResult'], calving_detail[0]['calving_result'])
        if register['content']['calvingResult'] == 10:
            self.assertEqual(register['content']['calvingResultDesc'], '产犊')
        if register['content']['calvingResult'] == 20:
            self.assertEqual(register['content']['calvingResultDesc'], '流产')
        self.assertEqual(register['content']['id'], calving_detail[0]['id'])
        self.assertEqual(register['content']['remark'], calving_detail[0]['remark'])

    def test_mobile_cattle_calving_get_offspring(self):
        """
        获取牲畜后代列表V 1.2.5
        V 1.2.6 update
        :return:
        """
        # 查询含有后代的牲畜id
        relationship_list = self.fq.query_relationship_buy_email(self.email)

        cattle_list = self.tool.data_assemble('p_id', relationship_list, len(relationship_list)) + \
                      self.tool.data_assemble('m_id', relationship_list, len(relationship_list))
        cattle_id = choice(cattle_list)
        # check = self.fq.query_cattle_detail_buy_cattle_id(cattle_id=cattle_id)

        register = self.ka.mobile_cattle_calving_get_offspring(cattleId=cattle_id)
        if len(register["content"]) > 0:
            offspring_detail = self.fq.query_offspring_info_buy_cattle_id(cattle_id)
            for i in range(len(offspring_detail)):
                self.assertEqual(register["content"][i].get("id"), offspring_detail[i].get("id"))
                self.assertEqual(register["content"][i].get("cattleName"), offspring_detail[i].get("cattle_name"))
                self.assertEqual(register["content"][i].get("type"), offspring_detail[i].get("type"))
                self.assertEqual(register["content"][i].get("typeName"), offspring_detail[i].get("value"))
                self.assertEqual(register["content"][i].get("varietyId"), offspring_detail[i].get("variety_id"))

    def test_mobile_cattle_calving_del_offspring(self):
        """
        删除牲畜后代 V 1.2.5
        V 1.2.6 update
        :return:
        """
        relationship_list = self.fq.query_relationship_buy_email(self.email)
        if len(relationship_list) > 0:
            # 随机获取农场具有血缘关系的牲畜id
            cattle_id = (self.tool.data_assemble('id', relationship_list, 1))[0]
            cattle_detail = self.fq.query_cattle_detail_buy_cattle_id(cattle_id=cattle_id)
            if 'p_id' in cattle_detail[0].keys():
                p_id = cattle_detail[0]['p_id']
                self.ka.mobile_cattle_calving_del_offspring(calfId=cattle_id, cattleId=p_id)
                cattle_detail_list = self.fq.query_cattle_detail_buy_cattle_id(cattle_id=cattle_id)
                self.assertEqual(None, cattle_detail_list[0]['p_id'])
            if 'm_id' in cattle_detail[0].keys():
                m_id = cattle_detail[0]["m_id"]
                self.ka.mobile_cattle_calving_del_offspring(calfId=cattle_id, cattleId=m_id)
                cattle_detail_list = self.fq.query_cattle_detail_buy_cattle_id(cattle_id=cattle_id)
                self.assertEqual(None, cattle_detail_list[0]['m_id'])
        else:
            self.log.info("默认农场下暂无牲畜具有血缘关系")

    def test_mobile_cattle_search_get_offspring(self):
        """
        根据牲畜Id查询后代牲畜列表 V 1.2.6
        :return:
        """
        relationship_list = self.fq.query_relationship_buy_email(self.email)
        if len(relationship_list) > 0:
            # 随机获取农场具有血缘关系的牲畜id
            cattle_id = (self.tool.data_assemble('id', relationship_list, 1))[0]
            cattle_detail = self.fq.query_cattle_detail_buy_cattle_id(cattle_id=cattle_id)
            if 'p_id' in cattle_detail[0].keys():
                p_id = cattle_detail[0]['p_id']
                self.ka.mobile_cattle_search_get_offspring(cattleId=p_id)
                cattle_detail_list = self.fq.query_cattle_detail_buy_cattle_id(cattle_id=cattle_id)
                self.assertEqual(p_id, cattle_detail_list[0]['p_id'])
            if 'm_id' in cattle_detail[0].keys():
                m_id = cattle_detail[0]["m_id"]
                self.ka.mobile_cattle_search_get_offspring(cattleId=m_id)
                cattle_detail_list = self.fq.query_cattle_detail_buy_cattle_id(cattle_id=cattle_id)
                self.assertEqual(m_id, cattle_detail_list[0]['m_id'])

    def test_mobile_cattle_stage_cycle_list(self):
        """
        获取牲畜生理阶段周期记录卡片列表V 1.2.5
        V 1.2.6 update
        :return:
        """
        cattle_detail_list = self.fq.query_breeding_cow_id_buy_email(self.email)
        cattle_id_list = self.tool.data_assemble("id", cattle_detail_list, 1)
        cattle_id = cattle_id_list[0]
        self.ka.mobile_cattle_stage_cycle_list(cattleId=cattle_id)

    def test_mobile_cattle_stage_cycle_del(self):
        """
        删除牲畜生理阶段周期记录卡片
        :return:
        """
        cattle_detail_list = self.fq.query_breeding_cow_id_buy_email(self.email)
        if len(cattle_detail_list) > 0:
            cattle_id = cattle_detail_list[0]["id"]
            cycle_info_list = self.fq.query_cattle_all_cycle(cattle_id=cattle_id, is_delete=0)
            cycle_id = cycle_info_list[0]['id']
            self.ka.mobile_cattle_stage_cycle_del(id=cycle_id)
            cycle_info_list = self.fq.query_cattle_all_cycle(cattle_id=cattle_id, is_delete=1)
            # self.assertEqual(1, cycle_info_list[0]["is_delete"])
        else:
            self.log.info("当前默认农场下，生理周期阶段的牲畜没有历史记录卡片！")

    # def test_mobile_cattle_stage_cycle_detail(self):
    #     """
    #     获取牲畜生理阶段周期记录卡片详情V 1.2.5
    #     :return:
    #     """
    #     stage_status = 31
    #     cattle_detail_list = self.fq.query_stage_cycle(self.email, stage_status=stage_status)
    #     cattle_id_list = self.tool.data_assemble("id", cattle_detail_list, 1)
    #     cycle_id = cattle_id_list[0]
    #     self.koalaAction.mobile_cattle_stage_cycle_detail(id=cycle_id)

    def test_mobile_cattle_stage_cycle_update(self):
        """
        修改牲畜生理阶段周期记录卡片V 1.2.5
        :return:
        """
        bull_id_list = self.fq.query_bull_id_buy_email(email=self.email)
        bullIds = self.tool.data_assemble('id', bull_id_list, 3)
        stage_status = 40
        # 查询对应状态下的生理周期记录信息
        cattle_detail_list = self.fq.query_stage_cycle(self.email, stage_status=stage_status)
        cycle_id = cattle_detail_list[0]["id"]
        cattle_id = cattle_detail_list[0]["cattle_id"]
        breeding_list = self.fq.query_breeding_date_buy_cattle_id(cattle_id=cattle_id)
        breeding_id = breeding_list[0]["id"]
        start_date = self.tt.get_standardtime_timestamp(formats="%Y-%m-%d")
        end_date = self.tt.get_standardtime_timestamp(week=4, formats="%Y-%m-%d")
        breeding_remark = "修改牲畜生理阶段周期记录表备注"
        is_region_same = 0
        self.ka.mobile_cattle_stage_cycle_update(bullIds=bullIds, id=cycle_id, breedingId=breeding_id,
                                                 breedingStartDate=start_date, breedingEndDate=end_date,
                                                 breedingRemark=breeding_remark, isRegionSame=is_region_same,
                                                 pregId=None, pregCheckDate=None, pregCheckResult=None,
                                                 calvingId=None, calvingResult=None, calvingDate=None,
                                                 calvingCalfId=None)

    # def test_mobile_cattle_stage_cycle_updateHistory(self):
    #     """
    #     修改牲畜生理阶段周期历史记录卡片V 1.2.5
    #     :return:
    #     """
    #     bull_id_list = self.fq.query_bull_id_buy_email(email=self.email)
    #     bullIds = self.tool.data_assemble('id', bull_id_list, 3)
    #     stage_status = 31
    #     cattle_detail_list = self.fq.query_stage_cycle(self.email, stage_status=stage_status)
    #     if len(cattle_detail_list) > 0:
    #         cycle_id = cattle_detail_list[0]["id"]
    #         now_date = datetime.date.today()
    #         future_date = now_date + datetime.timedelta(weeks=4)
    #         end_date = self.tt.str_time_timestamp(str(future_date), "%Y-%m-%d")
    #         start_date = self.tt.str_time_timestamp(str(now_date), "%Y-%m-%d")
    #         breeding_remark = "修改牲畜生理阶段周期记录表备注"
    #         preg_check_date = self.tt.str_time_timestamp(str(now_date), "%Y-%m-%d")
    #         calving_date = self.tt.str_time_timestamp(str(now_date), "%Y-%m-%d")
    #         is_region_same = 0
    #         self.koalaAction.mobile_cattle_stage_cycle_updateHistory(bullIds=bullIds, id=cycle_id,
    #                                                                  breedingStartDate=start_date,
    #                                                                  breedingEndDate=end_date,
    #                                                                  breedingRemark=breeding_remark,
    #                                                                  pregCheckDate=preg_check_date,
    #                                                                  calvingDate=None,
    #                                                                  isRegionSame=is_region_same)
    #     else:
    #         self.log.info("当前默认农场下，生理周期阶段的牲畜没有历史记录卡片！")


if __name__ == '__main__':
    m = Main()
