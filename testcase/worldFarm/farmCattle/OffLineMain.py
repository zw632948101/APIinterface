#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Wei'
__date__ = '2019/ 08/ 16'
离线数据接口
"""
import json
import random

from testcase.worldFarm import testCase


class OffLineMain(testCase):


    def test_mobile_offline_search_condition_cattle(self):
        """
        离线筛选条件-获取牲畜离线筛选条件
        :return:
        """
        register = self.oa.mobile_offline_search_condition_cattle()
        self.assertEqual(register['status'], 'OK')

    def test_mobile_offline_search_condition_cattle_position(self):
        """
        离线筛选条件-获取牲畜设备定位离线筛选条件
        :return:
        """

        register = self.oa.mobile_offline_search_condition_cattle_position()
        self.assertEqual(register['status'], 'OK')

    def test_mobile_offline_upload_data(self):
        """
        离线上传-上传离线数据
        :return:
        """
        bizId = ''
        for i in range(len('f3f368499cb240bc9769cf666c714621')):
            bizId += str(random.randint(0, 9)) if random.randint(1, 2) == 1 else chr(random.randint(ord('a'), ord('f')))
        geo_list = [{"bizId": "D155DA2C69384F26B204E9C54BC11F80",
                     "bizType": "landmark",
                     "optType": "add",
                     "requestParam": "{\"solidIcon\":\"https://dnkj-world-farm-prd.oss-ap-southeast-1.aliyuncs.com/data/world-koala/farm/static/icon/iocn2019061400000005.png\",\"type2Name\":\"谷仓\",\"type1\":\"10030\",\"locations\":{\"lat \":-27.672931864320821,\"lng \":150.70435590644173},\"id\":\"-191524242\",\"buildPrice\":0,\"currencyType\":\"USD\",\"shapeType\":1,\"length\":0,\"farmId\":\"621\",\"type2\":\"10080\",\"currencyTypeDesc\":\"美元\",\"createTime\":0,\"landmarkId\":\"-191524242\",\"currencyTypeSymbol\":\"$\",\"name\":\"尴尬1\",\"buildDate\":\"2019/07/13\"}"
                     }]
        geo_json = json.dumps(geo_list)
        register = self.oa.mobile_offline_upload_data(jsonParam=geo_json)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_offline_version_check(self):
        """
        离线数据版本检查-检查是否有新数据更新
        :return:
        """
        geo_list = '[{"type":"cattle","version":"10"}]'
        geo_json = json.dumps(json.loads(geo_list))
        register = self.oa.mobile_offline_version_check(jsonParam=geo_json)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_offline_camera(self):
        """
        离线数据-获取摄像头离线数据【无离线版本号、不支持分页，默认返回全量】
        :return:
        """
        register = self.oa.mobile_offline_camera(page=0)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_offline_cattle(self):
        """
        离线数据-获取牲畜离线数据
        :return:
        """
        register = self.oa.mobile_offline_cattle(page=0)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_offline_cattle_position(self):
        """
        离线数据-获取牲畜定位离线数据【无离线版本号、不支持分页，默认返回全量】
        :return:
        """
        register = self.oa.mobile_offline_cattle_position(page=0)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_offline_farm(self):
        """
        离线数据-获取农场离线数据
        :return:
        """
        register = self.oa.mobile_offline_farm(page=1)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_offline_farm_region(self):
        """
        离线数据-获取围栏离线数据
        :return:
        """
        register = self.oa.mobile_offline_farm_region(page=0)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_offline_farm_signal(self):
        """
        离线数据-获取农场信号离线数据【无离线版本号、不支持分页，默认返回全量】
        :return:
        """
        register = self.oa.mobile_offline_farm_signal(page=0)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_offline_farm_user(self):
        """
        离线数据-获取用户离线数据
        :return:
        """
        register = self.oa.mobile_offline_farm_user(page=0)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_offline_landmark(self):
        """
        离线数据-获取地标离线数据【不支持分页，默认返回全量】
        :return:
        """
        register = self.oa.mobile_offline_landmark(page=0)
        self.assertEqual(register['status'], 'OK')


if __name__ == '__main__':
    om = OffLineMain()
