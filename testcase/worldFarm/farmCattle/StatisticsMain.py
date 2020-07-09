#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Wei'
__date__ = '2019/8/15'
移动端统计面板
"""
import random
from random import choice
from testcase.worldFarm import testCase, Statistics


class StatisticsMain(testCase):
    fq = Statistics()

    # def test_mobile_statistics_count(self):
    #     """
    #     移动端-统计-牲畜数量,种类数量,异常数量统计 v1.2.3
    #     :return:
    #     """
    #     register = self.ko.mobile_statistics_count(farmId=678)
    #     self.assertEqual(register['status'], 'OK')

    def test_mobile_statistics_stat_abnormal_list(self):
        """
        移动端-统计-活动异常牲畜或外部闯入牲畜-列表 v1.2.3
        移动端-统计-未上传定位牲畜或走出农场牲畜-列表 v1.2.5 修改
        :return:
        """
        farminfo = self.fq.query_default_farm(self.email)[0]
        positionStatus = choice([3, 5])
        register = self.ka.mobile_statistics_stat_abnormal_list(farmId=farminfo.get('farm_id'),
                                                                positionStatus=positionStatus)
        self.assertEqual(register['status'], 'OK')
        abnormallist = self.fq.query_statistics_cattle_intrude(farm_id=farminfo.get('farm_id'),
                                                               positionStatus=4 if positionStatus == 5 else None)
        content = register['content']
        self.assertEqual(len(abnormallist), len(content))
        for i in range(len(content)):
            if abnormallist[i].get('birth_date'):
                birth_date = self.tt.str_time_timestamp(abnormallist[i].get('birth_date'))
            else:
                birth_date = abnormallist[i].get('birth_date')
            self.assertEqual(birth_date, content[i].get('birthDate'))
            self.assertEqual(abnormallist[i].get('device_eui'), content[i].get('eui'))
            self.assertEqual(abnormallist[i].get('device_type'), content[i].get('deviceType'))
            self.assertEqual(abnormallist[i].get('cattle_name'), content[i].get('cattleName'))
            self.assertEqual(abnormallist[i].get('farm_id'), content[i].get('farmId'))
            self.assertEqual(abnormallist[i].get('lat'), content[i].get('lat'))
            self.assertEqual(abnormallist[i].get('lng'), content[i].get('lng'))
            self.assertEqual(abnormallist[i].get('position_farm_id'), content[i].get('positionFarmId'))
            self.assertEqual(abnormallist[i].get('position_region_id'), content[i].get('positionRegionId'))
            self.assertEqual(abnormallist[i].get('region_id'), content[i].get('regionId'))
            self.assertEqual(abnormallist[i].get('sex'), content[i].get('sexName'))
            self.assertEqual(abnormallist[i].get('label_id'), content[i].get('typeName'))
            self.assertEqual(abnormallist[i].get('variety_id'), content[i].get('varietyName'))

    def test_mobile_statistics_stat_abnormal_map(self):
        """
        移动端-统计-活动异常牲畜或外部闯入牲畜-地图 v1.2.3
        移动端-统计-未上传定位牲畜或走出农场牲畜-地图【v1.2.5】
        :return:
        """
        farminfo = self.fq.query_default_farm(self.email)[0]
        positionStatus = ([3, 5])
        register = self.ka.mobile_statistics_stat_abnormal_map(farmId=farminfo.get('farm_id'),
                                                               positionStatus=positionStatus)
        self.assertEqual(register['status'], 'OK')
        content = register['content']
        cattleinfo = self.fq.query_statistics_cattle_intrude(farm_id=farminfo.get('farm_id'), devicetype=3,
                                                             positionStatus=4 if positionStatus == 5 else None)
        self.assertEqual(len(content), len(cattleinfo))
        self.assertListEqual(
            sorted(self.tool.data_assemble(key="device_eui", parameters_ld=cattleinfo, num=len(cattleinfo))),
            sorted(self.tool.data_assemble(key="eui", parameters_ld=content, num=len(content))))

        self.assertListEqual(
            sorted(self.tool.data_assemble(key="lat", parameters_ld=cattleinfo, num=len(cattleinfo))),
            sorted(self.tool.data_assemble(key="lat", parameters_ld=content, num=len(content))))

        self.assertListEqual(
            sorted(self.tool.data_assemble(key="lng", parameters_ld=cattleinfo, num=len(cattleinfo))),
            sorted(self.tool.data_assemble(key="lng", parameters_ld=content, num=len(content))))

    def test_mobile_statistics_stat_abnormal_near(self):
        """
        移动端-统计-活动异常牲畜或外部闯入牲畜-附近 v1.2.3
        移动端-统计-未上传定位牲畜或走出农场牲畜-附近【v1.2.5】
        :return:
        """
        farminfo = self.fq.query_default_farm(self.email)[0]
        positionStatus = choice([3, 5])
        abnormallist = self.fq.query_statistics_cattle_intrude(farm_id=farminfo.get('farm_id'),
                                                               positionStatus=4 if positionStatus == 5 else None,
                                                               devicetype=2)
        if abnormallist is None:
            self.log.info("农场内没有活动异常的牲畜")
            return
        deviceEui = choice(abnormallist).get('device_eui')
        register = self.ka.mobile_statistics_stat_abnormal_near(farmId=farminfo.get('farm_id'),
                                                                positionStatus=positionStatus,
                                                                deviceEui=deviceEui)

        self.assertEqual(register['status'], 'OK')
        content = register.get('content')
        abnormal = self.fq.query_statistics_cattle_intrude(farm_id=farminfo.get('farm_id'),
                                                           positionStatus=4 if positionStatus == 5 else None,
                                                           devicetype=2, deviceeui=deviceEui)
        self.assertEqual(len(content), len(abnormal))
        self.assertListEqual(
            sorted(self.tool.data_assemble(key="device_eui", parameters_ld=abnormal, num=len(abnormal))),
            sorted(self.tool.data_assemble(key="eui", parameters_ld=content, num=len(content))))

        self.assertListEqual(
            sorted(self.tool.data_assemble(key="lat", parameters_ld=abnormal, num=len(abnormal))),
            sorted(self.tool.data_assemble(key="lat", parameters_ld=content, num=len(content))))

        self.assertListEqual(
            sorted(self.tool.data_assemble(key="lng", parameters_ld=abnormal, num=len(abnormal))),
            sorted(self.tool.data_assemble(key="lng", parameters_ld=content, num=len(content))))
        self.assertListEqual(
            sorted(self.tool.data_assemble(key="cattle_name", parameters_ld=abnormal, num=len(abnormal))),
            sorted(self.tool.data_assemble(key="cattleName", parameters_ld=content, num=len(content))))
        self.assertListEqual(
            sorted(self.tool.data_assemble(key="variety_id", parameters_ld=abnormal, num=len(abnormal))),
            sorted(self.tool.data_assemble(key="varietyName", parameters_ld=content, num=len(content))))
        self.assertListEqual(
            sorted(self.tool.data_assemble(key="sex", parameters_ld=abnormal, num=len(abnormal))),
            sorted(self.tool.data_assemble(key="sexName", parameters_ld=content, num=len(content))))
        self.assertListEqual(
            sorted(self.tool.data_assemble(key="label_id", parameters_ld=abnormal, num=len(abnormal))),
            sorted(self.tool.data_assemble(key="typeName", parameters_ld=content, num=len(content))))

    def test_mobile_statistics_home_cattle_count(self):
        """
        移动端-统计-首页-牲畜统计 v1.2.4
        :return:
        """
        farminfo = self.fq.query_default_farm(self.email)[0]
        register = self.ka.mobile_statistics_home_cattle_count(farminfo.get('farm_id'))
        data = self.fq.query_cattle_list_statistics_number(farminfo.get('farm_id'))
        abnormal = self.fq.qyery_statistics_abnormal(farminfo.get('farm_id'))
        data = dict(data, **abnormal)
        self.assertEqual(register["status"], "OK")
        stageCount = register['content']['stageCount']
        typeCount = register['content']['typeCount']
        positionCount = register['content']['positionCount']
        statistics = stageCount + typeCount + positionCount
        self.assertEqual(register['content'].get('taggedCount'), int(data.get('taggedCount')))
        self.assertEqual(register['content'].get('totalCount'), int(data.get('cattle_num')))
        for info_d in statistics:
            self.assertEqual(info_d.get('count'), int(data.get(info_d.get('typeDesc'))))

    def test_mobile_statistics_group_detail(self):
        """
        移动端-牲畜档案 - 分组详情【v1.2.5】
        :return:
        """
        cattle_stage = cattle_type = None
        farminfo = self.fq.query_default_farm(self.email)[0]
        if random.randint(0, 1):
            cattle_stage = choice(['10', '30,31,32,33', '40', '50'])
        else:
            cattle_type = choice(['1001', '1002', '1003,1005,1007', '1004,1006,1008', '1007,1008'])

        info = self.ka.mobile_statistics_group_detail(farmId=farminfo.get('farm_id'), type=cattle_type,
                                                      stage=cattle_stage)
        self.assertEqual(info["status"], "OK")
        statistics_group = self.fq.query_statistics_group_detail(farminfo.get('farm_id'), cattle_type, cattle_stage)
        self.assertEqual(info['content'].get('all'), int(statistics_group.get('cattle_num')))
        self.assertEqual(info['content'].get('tagged'), int(statistics_group.get('tagged_num')))
        self.assertEqual(info['content'].get('untagged'), int(statistics_group.get('untagged_num')))

    def test_mobile_statistics_group_location(self):
        """
        移动端-牲畜档案-分组牲畜位置【v1.2.5】
        :return:
        """
        cattle_stage = cattle_type = None
        farminfo = self.fq.query_default_farm(self.email)[0]
        if random.randint(0, 1):
            cattle_stage = choice(['10', '30,31,32,33', '40', '50'])
        else:
            cattle_type = choice(['1001', '1002', '1003,1005', '1004,1006'])
        info = self.ka.mobile_statistics_group_location(farmId=farminfo.get('farm_id'), type=cattle_type,
                                                        stage=cattle_stage)
        self.assertEqual(info["status"], "OK")
        content = info.get('content')
        cattlemap = self.fq.query_farm_cattle_location_map_info(farmid=farminfo.get('farm_id'), type=cattle_type,
                                                                stage=cattle_stage)
        if content:
            self.assertEqual(len(content), len(cattlemap))

            self.assertListEqual(
                sorted(self.tool.data_assemble(key="cattleName", parameters_ld=cattlemap, num=len(cattlemap))),
                sorted(self.tool.data_assemble(key="cattleName", parameters_ld=content, num=len(content))))

            self.assertListEqual(
                sorted(self.tool.data_assemble(key="cattleId", parameters_ld=cattlemap, num=len(cattlemap))),
                sorted(self.tool.data_assemble(key="cattleId", parameters_ld=content, num=len(content))))

            self.assertListEqual(
                sorted(self.tool.data_assemble(key="eui", parameters_ld=cattlemap, num=len(cattlemap))),
                sorted(self.tool.data_assemble(key="eui", parameters_ld=content, num=len(content))))

            self.assertListEqual(
                sorted(self.tool.data_assemble(key="lat", parameters_ld=cattlemap, num=len(cattlemap))),
                sorted(self.tool.data_assemble(key="lat", parameters_ld=content, num=len(content))))
            self.assertListEqual(
                sorted(self.tool.data_assemble(key="lng", parameters_ld=cattlemap, num=len(cattlemap))),
                sorted(self.tool.data_assemble(key="lng", parameters_ld=content, num=len(content))))

            self.assertListEqual(
                sorted(self.tool.data_assemble(key="type", parameters_ld=cattlemap, num=len(cattlemap))),
                sorted(self.tool.data_assemble(key="type", parameters_ld=content, num=len(content))))
            self.assertListEqual(
                sorted(self.tool.data_assemble(key="typeName", parameters_ld=cattlemap, num=len(cattlemap))),
                sorted(self.tool.data_assemble(key="typeName", parameters_ld=content, num=len(content))))
            self.assertListEqual(
                sorted(self.tool.data_assemble(key="varietyId", parameters_ld=cattlemap, num=len(cattlemap))),
                sorted(self.tool.data_assemble(key="varietyId", parameters_ld=content, num=len(content))))
            self.assertListEqual(
                sorted(self.tool.data_assemble(key="varietyName", parameters_ld=cattlemap, num=len(cattlemap))),
                sorted(self.tool.data_assemble(key="varietyName", parameters_ld=content, num=len(content))))

    def test_mobile_statistics_cattle_home(self):
        """
        移动端-统计-牲畜管理首页【v1.2.6 可联调】
        :return:
        """
        famrid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        info = self.ka.mobile_statistics_cattle_home(farmId=famrid)
        self.assertEqual(info["status"], "OK")


if __name__ == '__main__':
    s = StatisticsMain()
