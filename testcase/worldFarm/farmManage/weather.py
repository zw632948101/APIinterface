#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Wei'
__date__ = '2019/ / '
   天气模块
"""

from testcase.worldFarm import testCase, FarmQuery


class Weather(testCase):
    fq = FarmQuery()

    def __init__(self, methodName='runTest'):
        super(Weather, self).__init__(methodName=methodName)
        self.ka.set_user(mobile=self.email, password=self.password)

    def test_mobile_weather_detail(self):
        """
        移动端-天气 - 首页-天气详情 V1.2.5
        :return:
        """
        farmId = self.fq.query_default_farm(self.email)[0].get('farm_id')
        register = self.ka._mobile_weather_detail(farmId=farmId)
        self.assertEqual(register['status'], "OK")

    def test_mobile_weather_home_rain(self):
        """
        移动端-天气 - 首页-天气(当日降雨量、本月降雨量)
        :return:
        """
        farmId = self.fq.query_default_farm(self.email)[0].get('farm_id')
        register = self.ka._mobile_weather_home_rain(farmId=farmId)
        self.assertEqual(register['status'], "OK")
