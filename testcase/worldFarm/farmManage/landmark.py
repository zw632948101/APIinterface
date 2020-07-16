#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Wei'
__date__ = '2019/ / '
  地标模块
"""

import json
from random import choice, randint
from testcase.worldFarm import testCase, FarmManage


class LandmarkMain(testCase):
    fq = FarmManage()

    def __init__(self, methodName='runTest'):
        super(LandmarkMain, self).__init__(methodName=methodName)
        self.ka.set_user(mobile=self.email, password=self.password)

    def test_mobile_farm_search_condition(self):
        """
        移动端-农场管理-农场围栏/区域/地标筛选条件/分享内容列表
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        register = self.ka._mobile_farm_search_condition(farmId=farmid)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_landmark_add(self):
        """
        移动端-农场地标-新增地标
        :return:
        """
        farminfo = choice(self.fq.query_default_farm(self.email))
        farmid = farminfo.get('farm_id')
        location = json.loads(farminfo.get('region_locations'))
        remark = name = "接口测试添加地标"
        type1 = choice(self.category)
        type2 = list(choice(self.kinds.get(list(type1.keys())[0])).values())[0]
        type1 = list(type1.values())[0]
        buildDate = self.tt.get_standardtime_timestamp()
        buildPrice = randint(5000, 50000)
        if type2 in ['10220', '10160', '10170']:
            locations = self.cc.linetype_land(location, type2)
        else:
            locations = self.cc.dot_land(location)
        specs = waterCapacity = None
        if type2 in ['10180', '10240', '10200']:
            specs = '接口测试添加水资源地标%s' % self.tt.get_standardtime_timestamp()
            waterCapacity = randint(100, 999999)
        register = self.ka._mobile_landmark_add(farmId=farmid, regionId=None, type1=type1, type2=type2,
                                                name=name, buildDate=buildDate, buildPrice=buildPrice, remark=remark,
                                                imageList=None, locations=locations, specs=specs,
                                                waterCapacity=waterCapacity)
        self.assertEqual(register['status'], "OK")
        landmarkId = register['content']['landmarkId']
        landmarkinfo = self.fq.query_farm_landmark_id(landmarkId)
        self.assertEqual(locations, landmarkinfo.get('locations'))
        self.assertEqual(name, landmarkinfo.get('landmark_name'))
        self.assertEqual(type2, landmarkinfo.get('type2'))
        self.assertEqual(type1, landmarkinfo.get('type1'))
        self.assertEqual(remark, landmarkinfo.get('remark'))
        self.assertEqual(specs, landmarkinfo.get('specs'))
        self.assertEqual(waterCapacity, landmarkinfo.get('water_capacity'))

    def test_mobile_landmark_list(self):
        """
        移动端-农场地标-筛选地标列表
        :return:
        """
        farm = choice(self.fq.query_farm_and_region(self.email))
        register = self.ka._mobile_landmark_list(farmId=farm.get('farm_id'), types=None)
        self.assertEqual(register['status'], "OK")

    def test_mobile_landmark_del(self):
        """
        移动端-农场地标-删除地标
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        landmarkId = choice(self.fq.query_landmark_info_farmid(farmid)).get('id')
        # landmarkId = 1844
        register = self.ka._mobile_landmark_del(landmarkId=landmarkId)
        self.assertEqual(register['status'], "OK")
        landmarkinfo = self.fq.query_farm_landmark_id(landmarkId)
        self.assertEqual(1, landmarkinfo.get('is_delete'))

    def test_mobile_landmark_detail(self):
        """
        移动端-农场地标-地标详情
        1.2.5 修改
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        landmarkid = choice(self.fq.query_landmark_info_farmid(farmid)).get('id')
        register = self.ka._mobile_landmark_detail(landmarkId=landmarkid)
        self.assertEqual(register['status'], "OK")
        landmark = self.fq.query_farm_landmark_id(landmarkid)
        self.assertEqual(register['content'].get('locations'), landmark.get('locations'))
        self.assertEqual(register['content'].get('name'), landmark.get('landmark_name'))
        self.assertEqual(register['content'].get('type1'), landmark.get('type1'))
        self.assertEqual(register['content'].get('type2'), landmark.get('type2'))
        self.assertEqual(register['content'].get('currencyType'), landmark.get('currency_type'))
        self.assertEqual(register['content'].get('farmId'), landmark.get('farm_id'))
        self.assertEqual(register['content'].get('farmName'), landmark.get('farm_name'))
        self.assertEqual(register['content'].get('length'), landmark.get('length'))
        self.assertEqual(register['content'].get('locations'), landmark.get('locations'))
        self.assertEqual(register['content'].get('remark'), landmark.get('remark'))
        self.assertEqual(register['content'].get('specs'), landmark.get('specs'))
        self.assertEqual(register['content'].get('waterCapacity'), landmark.get('water_capacity'))

    def test_mobile_landmark_type_count(self):
        """
        移动端-农场地标-获取地标分类统计
        :return:
        """
        farminfo = choice(self.fq.query_default_farm(self.email))
        farmid = farminfo.get('farm_id')
        regionid = farminfo.get('region_id')
        register = self.ka._mobile_landmark_type_count(farmId=farmid, regionId=regionid)
        self.assertEqual(register['status'], "OK")

    def test_mobile_landmark_update(self):
        """
        移动端-农场地标-编辑坐标
        :return:
        """
        farminfo = choice(self.fq.query_default_farm(self.email))
        farmid = farminfo.get('farm_id')
        location = json.loads(farminfo.get('region_locations'))
        remark = name = "接口测试编辑水资源地标"

        landmarkinfo = choice(self.fq.query_landmark_info_farmid(farmid))

        landmarkid = landmarkinfo.get('id')
        type2 = landmarkinfo.get('type2')
        type1 = landmarkinfo.get('type1')
        buildDate = self.tt.get_standardtime_timestamp()
        buildPrice = randint(5000, 50000)

        if type2 in ['10220', '10160', '10170']:
            locations = self.cc.linetype_land(location, type2)
        else:
            locations = self.cc.dot_land(location)
        specs = waterCapacity = None
        if type2 in ['10180', '10240', '10200']:
            specs = '接口测试编辑水资源地标%s' % self.tt.get_standardtime_timestamp()
            waterCapacity = randint(100, 999999)

        register = self.ka._mobile_landmark_update(farmId=farmid, regionId=None, type1=type1, type2=type2,
                                                   name=name, buildDate=buildDate, buildPrice=buildPrice, remark=remark,
                                                   imageList=None, locations=locations, specs=specs,
                                                   waterCapacity=waterCapacity, landmarkId=landmarkid)
        self.assertEqual(register['status'], "OK")
        landmarkinfo = self.fq.query_farm_landmark_id(landmarkid)
        self.assertEqual(locations, landmarkinfo.get('locations'))
        self.assertEqual(name, landmarkinfo.get('landmark_name'))
        self.assertEqual(type2, landmarkinfo.get('type2'))
        self.assertEqual(type1, landmarkinfo.get('type1'))
        self.assertEqual(remark, landmarkinfo.get('remark'))
        self.assertEqual(specs, landmarkinfo.get('specs'))
        self.assertEqual(waterCapacity, landmarkinfo.get('water_capacity'))

    def test_mobile_water_resource_home_list(self):
        """
        移动端-水资源-水资源管理首页【v1.2.7 可对字段】
        返回字段错误
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        register = self.ka._mobile_water_resource_home_list(farmId=farmid)
        self.assertEqual(register['status'], "OK")
        waterResourceGroup1Outputs = register['content']['waterResourceGroup1Outputs']
        waterResourceGroup2Outputs = register['content']['waterResourceGroup2Outputs']
        if waterResourceGroup1Outputs:
            waterResourceGroup1Outputs.append(waterResourceGroup2Outputs[0])
            waterinfo = self.fq.query_farm_home_water_resource(farmid)
            waterinfo = self.tool.del_dict_value_null(waterinfo)
            for i in range(len(waterResourceGroup1Outputs)):
                self.assertDictEqual(waterinfo[i], waterResourceGroup1Outputs[i])

    def test_mobile_water_resource_list(self):
        """
        移动端-水资源-水资源列表【v1.2.7 可对字段】
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        water_type = list(choice(self.kinds.get('水资源')).values())[0]
        register = self.ka._mobile_water_resource_list(farmId=farmid, type=water_type)
        self.assertEqual(register['status'], "OK")
        content = register.get('content')
        datas = content.get('datas')
        if datas:
            # 查询水资源图片
            water_info_list = self.fq.query_landmark_list_info_transit_farmid(farmid, water_type)
            landmarkpng = self.fq.query_landmark_png_info(farm_id=farmid)
            for water in water_info_list:
                imageList = []
                for png in landmarkpng:
                    if water.get('id') == png.get('id'):
                        png.pop('id')
                        imageList.append(png)
                water['imageList'] = imageList
            water_info = self.tool.del_dict_value_null(water_info_list)
            self.log.info(water_info)
            self.assertListEqual(water_info, datas)


if __name__ == '__main__':
    l = LandmarkMain()
