#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log import log
from testcase.flowerChaser.sql.Bee import BeeClueSql
from utils.fake.FakeLocation import FakeLocation
import random
import json
from faker import Faker
import re
from utils.dataConversion.dataConversion import DataConversion


class WeatherMain(unittest.TestCase, DataConversion):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    ba = BeeAction()
    ba_db = BeeClueSql()
    log.info("开始执行天气管理接口测试用例")
    fake = Faker(locale="zh_CN")
    fl = FakeLocation()
    ba.set_user('19982917912')

    def test_mobile_user_nectar_source_update(self):
        """
        POST /mobile/user-nectar-source/update
        添加用户常去地点
        :return:
        """
        nectarSource_st = []
        for i in range(random.randint(0, 5)):
            province_id, city_id, district_id, address, lng, lat = self.fl.fake_location()
            a = {'province': province_id, 'city': int(city_id), 'county': district_id, 'address': address, 'lng': lng,
                 'lat': lat}
            nectarSource_st.append(a)
        nectarSource = json.dumps(nectarSource_st)
        self.ba._mobile_user_nectar_source_update(nectarSources_=nectarSource)

    def test_mobile_user_nectar_source_list(self):
        """
        POST /mobile/user-nectar-source/list
        用户常去地点列表
        :return:
        """
        # self.ba.set_user('19988776654')
        resp = self.ba._mobile_user_nectar_source_list()
        self.assertEqual(resp.get('status'), 'OK')
        content = resp.get('content')
        sourcelist = self.ba_db.query_user_nectar_soure_list(userid=self.ba.user.user_id)
        for i in range(len(content)):
            self.assertDictEqual(content[i], sourcelist[i])

    def test_mobile_hot_nectar_source_list(self):
        """
        POST /mobile/hot-nectar-source/list
        热门蜜源地列表 ----2.0枚举值：高州市、灵山县、桂平市、兴义市、罗平县、文山县、泸西县、富源县、绵阳市
        :return:
        """
        self.ba.set_user('19988776654')
        json_response = self.ba._mobile_hot_nectar_source_list()
        hot_nectar_source = ['高州市', '灵山县', '桂平市', '兴义市', '罗平县', '文山市', '泸西县', '富源县', '绵阳市']
        if json_response["status"] == "OK":
            if len(hot_nectar_source) == len(json_response):
                for i in range(len(hot_nectar_source)):
                    if json_response["content"][i]["countyName"]:
                        self.assertEqual(hot_nectar_source[i], json_response["content"][i]["countyName"])
                    else:
                        self.assertEqual(hot_nectar_source[i], json_response["content"][i]["cityName"])
            else:
                self.assertTrue(False, "热门蜜源地列表数据与枚举值数量不符")
        else:
            self.assertTrue(False, "热门蜜源地查询失败")

    def test_mobile_weather_home(self):
        """
        POST mobile/weather/home
        用户天气首页
        :return:
        """
        self.ba._mobile_weather_home()

    def test_region_common_search(self):
        """
        地区搜索 - new 2.0
        :return:
        """
        address = self.fake.address()
        searchlist = re.split('省|市|区|县|镇|乡|村|街|路', address)
        searchContent = random.choice(searchlist[1: -1])
        resp = self.ba._region_common_search(searchContent_=searchContent)
        self.assertEqual(resp.get('status'), 'OK')
        # data_search = self.ba_db.query_city_and_county_name_list(searchContent=searchContent)

    def test_mobile_weather_detail(self):
        """
        POST mobile/weather/detail
        天气详情
        :return:
        """
        self.ba._mobile_weather_detail(province_='410000', city_='410300', county_='410325')

    def test_mobile_user_nectar_source_count(self):
        """
        POST /mobile/user-nectar-source/count
        用户常驻蜜源地数量---首页判断有无城市进行跳转
        :return:
        """
        self.ba._mobile_user_nectar_source_count()


        data_search = self.ba_db.query_city_and_county_name_list(searchContent=searchContent)
        data_search = self.del_dict_value_null(data_search)
        content = resp.get('content')
        for i in range(len(content)):
            self.assertEqual(content[i], data_search[i])
