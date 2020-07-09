#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Wei'
__date__ = '2019/ / '

围栏/林区管理
"""
import time
from random import choice, sample
from testcase.worldFarm import testCase,PaddockManage


class RegionManage(testCase):

    fq = PaddockManage()

    def __init__(self, methodName='runTest'):
        super(RegionManage, self).__init__(methodName=methodName)
        self.ka.set_user(mobile=self.email, password=self.password)

    def test_api_farm_region_add(self):
        """
        添加农场围栏或者林區
        :return:
        """
        farminfo = self.fq.query_default_farm(self.email)[0]
        regionType = '10020'
        name = "dev测试围栏"
        perimeter = "28410.38"
        area = "3.347943"
        colorType = choice(list(range(1, 5)))
        soilType = choice(list(range(1, 3)))
        soilPh = choice(list(range(1, 6)))
        pastureType = ",".join(map(str, sample(list(range(1001, 1012)), 3)))
        locations = '[{"lng": 104.03994443737503, "lat": 30.80169307208601}, {"lng": 104.03994443737503, "lat": 30.75629307208601}, {"lng": 104.01724443737503, "lat": 30.75629307208601}, {"lng": 104.01724443737503, "lat": 30.80169307208601}, {"lng": 104.03994443737503, "lat": 30.80169307208601}]'
        register = self.ka._mobile_farm_region_add(farmId=farminfo.get('farm_id'), regionType=regionType, name=name,
                                                  perimeter=perimeter, area=area, colorType=colorType,
                                                  locations=locations, soilType=soilType, soilPh=soilPh,
                                                  pastureType=pastureType, remark=name)
        self.assertEqual(register['status'], "OK")
        regioninfo = self.fq.query_new_region(self.email)
        self.assertEqual(regioninfo.get('name'), name)
        self.assertEqual(regioninfo.get('remark'), name)
        self.assertEqual(regioninfo.get('soil_ph'), soilPh)
        self.assertEqual(regioninfo.get('soil_type'), str(soilType))
        self.assertEqual(regioninfo.get('color_type'), colorType)
        self.assertEqual(regioninfo.get('pasture_type'), pastureType)
        self.assertEqual(regioninfo.get('region_type'), regionType)

    def test_mobile_farm_region_update(self):
        """
        编辑围栏区域
        :return:
        """
        regioninfo = self.fq.query_new_region(self.email)
        name = "DEV測試养牛大户"
        perimeter = "28410.38"
        area = "3.35"
        colorType = choice(list(range(1, 5)))
        soilType = choice(list(range(1, 3)))
        soilPh = choice(list(range(1, 6)))
        pastureType = ",".join(map(str, sample(list(range(1001, 1012)), 3)))
        locations = '[{"lng": 104.03994443737503, "lat": 30.80169307208601}, {"lng": 104.03994443737503, "lat": 30.75629307208601}, {"lng": 104.01724443737503, "lat": 30.75629307208601}, {"lng": 104.01724443737503, "lat": 30.80169307208601}, {"lng": 104.03994443737503, "lat": 30.80169307208601}]'
        register = self.ka._mobile_farm_region_update(id=regioninfo.get('id'), name=name, perimeter=perimeter,
                                                     area=area, colorType=colorType, locations=locations,
                                                     soilType=soilType, soilPh=soilPh, remark=name,
                                                     pastureType=pastureType)
        self.assertEqual(register['status'], "OK")
        regioninfo = self.fq.query_del_region_data_info(regioninfo.get('id'))
        self.assertEqual(regioninfo.get('name'), name)
        self.assertEqual(regioninfo.get('remark'), name)
        self.assertEqual(regioninfo.get('soil_ph'), soilPh)
        self.assertEqual(regioninfo.get('soil_type'), str(soilType))
        self.assertEqual(regioninfo.get('color_type'), colorType)
        self.assertEqual(regioninfo.get('pasture_type'), pastureType)

    def test_mobile_rarm_region_list(self):
        """
        删除围栏
        :return:
        """
        regionId = self.fq.query_new_region(self.email)
        register = self.ka._mobile_farm_region_del(regionId=regionId.get('id'))
        self.assertEqual(register['status'], "OK")
        regioninfo = self.fq.query_del_region_data_info(regionId.get('id'))
        self.assertEqual(regioninfo.get('is_delete'), 1)

    def test_mobile_farm_region_list(self):
        """
        筛选围栏
        :return:
        """
        regionId = choice(self.fq.query_farm_and_region(self.email))
        types = '10020'
        isNeedFilter = 1
        isNeedStoreNum = None
        isNeedNoPaddock = 1
        register = self.ka._mobile_farm_region_list(farmId=547, types=types,
                                                   isNeedFilter=isNeedFilter, isNeedStoreNum=isNeedStoreNum,
                                                   isNeedNoPaddock=isNeedNoPaddock)
        self.assertEqual(register['status'], "OK")
        dbregion = self.fq.query_farm_region_list(farmid=547, types=types,
                                                  isNeedFilter=isNeedFilter,
                                                  isNeedNoPaddock=isNeedNoPaddock)
        register = register['content']
        for i in range(len(register)):
            apiregion = register[i]
            dbr = dbregion[i]
            if i == len(register) - 1 and isNeedNoPaddock == 1:
                self.assertEqual(apiregion.get('name'), dbr.get('name'))
                self.assertEqual(apiregion.get('storedNum'), dbr.get('storedNum'))
                continue
            if isNeedStoreNum == 1:
                self.assertEqual(apiregion.get('storedNum'), dbr.get('storedNum'))
            self.assertEqual(apiregion.get('area'), dbr.get('area'))
            self.assertEqual(apiregion.get('id'), dbr.get('region_id'))
            self.assertEqual(apiregion.get('locations'), dbr.get('locations'))
            self.assertEqual(apiregion.get('name'), dbr.get('name'))
            if apiregion.get('pastureType'):
                self.assertEqual(apiregion.get('pastureType'), dbr.get('pasture_type'))
            self.assertEqual(apiregion.get('perimeter'), dbr.get('perimeter'))
            self.assertEqual(apiregion.get('regionType'), dbr.get('region_type'))
            self.assertEqual(apiregion.get('remark'), dbr.get('remark'))
            self.assertEqual(apiregion.get('soilPh'), dbr.get('soil_ph'))
            self.assertEqual(apiregion.get('soilType'), dbr.get('soil_type'))

    def test_mobile_farm_region_paddock_list(self):
        """
        移动端-围栏/区域-围栏/区域列表(带放牧计划)【v1.2.6 可联调】
        :return:
        """
        farminfo = self.fq.query_default_farm(self.email)[0]
        register = self.ka._mobile_farm_region_paddock_list(farmId=farminfo.get('farm_id'))
        self.assertEqual(register['status'], "OK")
        register = register.get('content')
        task = self.fq.query_farm_task_region_data(farminfo.get('farm_id'))
        for i in range(len(register)):
            self.assertEqual(register[i].get('id'), task[i].get('id'))
            self.assertEqual(register[i].get('name'), task[i].get('name'))
            self.assertEqual(register[i].get('perimeter'), task[i].get('perimeter'))
            self.assertEqual(register[i].get('area'), task[i].get('area'))
            self.assertEqual(register[i].get('regionType'), task[i].get('region_type'))
            self.assertEqual(register[i].get('soilType'), task[i].get('soil_type'))
            self.assertEqual(register[i].get('soilPh'), task[i].get('soil_ph'))
            self.assertEqual(register[i].get('remark'), task[i].get('remark'))
            self.assertEqual(register[i].get('pastureType'), task[i].get('pasture_type'))
            self.assertEqual(register[i].get('locations'), task[i].get('locations'))
            if register[i].get('storedNum'):
                self.assertEqual(register[i].get('storedNum'), task[i].get('region_count'))
            grazePlan = register[i].get('grazePlan')
            if grazePlan:
                self.assertEqual(grazePlan.get('id'), task[i].get('tfgp_id'))
                self.assertEqual(grazePlan.get('planType'), task[i].get('plan_type'))
                self.assertEqual(grazePlan.get('planStartTime'),
                                 self.tt.str_time_timestamp(task[i].get('plan_start_time')))
                self.assertEqual(grazePlan.get('currentQuality'), task[i].get('current_quality'))
                self.assertEqual(grazePlan.get('endQuality'), task[i].get('end_quality'))
                self.assertEqual(grazePlan.get('growRate'), task[i].get('grow_rate'))
                self.assertEqual(grazePlan.get('consumeRate'), task[i].get('consume_rate'))
                self.assertEqual(grazePlan.get('expectDate'), task[i].get('expect_date'))
                self.assertEqual(grazePlan.get('actualDays'), int(task[i].get('calculate_day')))
                self.assertEqual(grazePlan.get('grazingCapacity'), int(task[i].get('grazing_capacity')))
                self.assertEqual(grazePlan.get('nextFieldDays'), task[i].get('date_line'), 2)

    def test_mobile_farm_region_get(self):
        """
        移动端-围栏/区域 - 围栏/区域详情【v1.2.7 可对字段】
        :return:
        """
        regionId = self.fq.query_new_region(self.email)
        register = self.ka._mobile_farm_region_get(regionId=regionId.get('id'))
        self.assertEqual(register['status'], "OK")
        regioninfo = self.fq.query_del_region_data_info(regionId.get('id'))
        cattle_statistics = self.fq.query_region_cattle_statistics(regionId.get('id'))
        self.assertEqual(regioninfo.get('name'), register['content'].get('name'))
        self.assertEqual(regioninfo.get('remark'), register['content'].get('remark'))
        self.assertEqual(regioninfo.get('soil_ph'), register['content'].get('soilPh'))
        self.assertEqual(regioninfo.get('soil_type'), register['content'].get('soilType'))
        self.assertEqual(regioninfo.get('color_type'), register['content'].get('colorType'))
        self.assertEqual(regioninfo.get('pasture_type'), register['content'].get('pastureType'))
        self.assertEqual(regioninfo.get('grass_state'), register['content'].get('grassState'))
        self.assertEqual(regioninfo.get('paddock_state'), register['content'].get('paddockState'))
        self.assertEqual(cattle_statistics.get('围栏牲畜总数'), register['content'].get('storedNum'))
        for statistics in register['content'].get('cattleTypeCountOutputs'):
            self.assertEqual(statistics.get('count'), cattle_statistics.get(statistics.get('typeDesc')))

    def test_mobile_farm_region_set_state(self):
        """
        移动端-围栏/区域-设置围栏状态【v1.2.7 可对字段】
        :return:
        """
        region_id = choice(self.fq.query_default_farm(self.email)).get('region_id')
        paddockState = choice([10, 20])
        grassState = choice([10, 20])
        remark = "接口测试，设置围栏状态"
        register = self.ka._mobile_farm_region_set_state(id=region_id, paddockState=paddockState, grassState=grassState,
                                                        remark=remark)
        self.assertEqual(register['status'], "OK")
        time.sleep(3)
        regioninfo = self.fq.query_del_region_data_info(region_id)
        self.assertEqual(regioninfo.get('remark'), remark)
        self.assertEqual(regioninfo.get('paddock_state'), paddockState)
        self.assertEqual(regioninfo.get('grass_state'), grassState)


if __name__ == '__main__':
    r = RegionManage()
