#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from actions.BeeAction import BeeAction
from tools.Config import Log
from sql.Bee import ConfigInformationSql, NectarSourceInformationSql, ContainerInformationSql
from testCase.FakeLocation import FakeLocation
import random
import json
from faker import Faker
import datetime, time
import re
from tools.Tool import Tool

class NectarSourceMain(unittest.TestCase):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    nectar_source = BeeAction()
    config_db = ConfigInformationSql()
    nectar_source_db = NectarSourceInformationSql()
    container_db = ContainerInformationSql()
    fl = FakeLocation()
    log = Log('FarmInformationMain').logger
    log.info("开始执行追花族蜂场管理测试用例")
    fake = Faker(locale="zh_CN")
    nectar_source.set_user('19988776600')

    def test_mobile_nectar_source_add(self):
        """
        POST /mobile/nectar-source/add 新建自有蜂场
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        db_type = self.nectar_source_db.sql_random_nectar_source_type(random.randint(1, 5))
        type_list = Tool.data_assemble('typeCode', db_type)
        type_str = ",".join(type_list)
        base_type = random.randint(1, 3)
        province_id, city_id, district_id, address, lng, lat = self.fl.fake_location()
        altitude = random.randint(100, 1000)
        start_date = datetime.datetime(year=2020, month=1, day=1)
        end_data = datetime.datetime(year=2020, month=6, day=15)
        bloom_start = self.fake.date_time_between(start_date=start_date, end_date=end_data)
        bloom_starts = int(bloom_start.timestamp() * 1000)
        bloom_end = self.fake.date_time_between(start_date=bloom_start, end_date=end_data)
        bloom_ends = int(bloom_end.timestamp() * 1000)
        flower_start = self.fake.date_time_between(start_date=bloom_start, end_date=bloom_end)
        flower_starts = int(flower_start.timestamp() * 1000)
        flower_end = self.fake.date_time_between(start_date=flower_start, end_date=bloom_end)
        flower_ends = int(flower_end.timestamp() * 1000)
        contacts = self.fake.name()
        contact_number = self.fake.phone_number()
        site_area = self.fake.random_int(min=1, max=99999999)
        nectar_source_area = self.fake.random_int(min=1, max=99999999)
        expect_ive_num = random.randint(1, 99999)
        price = self.fake.random_int(min=1, max=999999)*100
        vehicle_length = random.randint(1001, 1018)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(type_=type_list, name_=name, baseType_=base_type,
                                                                province_=province_id, city_=city_id,  county_=district_id, address_=address, lng_=lng, lat_=lat,
                                                                altitude_=altitude,
                                                                flowerStart_=flower_starts,
                                                                flowerEnd_=flower_ends, bloomStart_=bloom_starts,
                                                                bloomEnd_=bloom_ends,
                                                                contacts_=contacts, contactNumber_=contact_number,
                                                                siteArea_=site_area,
                                                                nectarSourceArea_=nectar_source_area,
                                                                expectHiveNum_=expect_ive_num,
                                                                price_=price,
                                                                vehicleLength_=vehicle_length,
                                                                remark_=remark,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                waterPic_=water_pic)
        if response["status"] == "OK":
            nectar_sources = self.nectar_source_db.sql_all_nectar_source()[0]
            nectar_source_detail = nectar_sources
            self.assertEqual(name, nectar_source_detail["name"])
            self.assertEqual(type_str, nectar_source_detail["type"])
            self.assertEqual(base_type, nectar_source_detail["base_type"])
            self.assertEqual(int(province_id), nectar_source_detail["province"])
            self.assertEqual(int(city_id), nectar_source_detail["city"])
            self.assertEqual(lng, nectar_source_detail["lng"])
            self.assertEqual(lat, nectar_source_detail["lat"])
            self.assertEqual(address, nectar_source_detail["address"])
            self.assertEqual(altitude, nectar_source_detail["altitude"])
            flower_start_time = time.localtime(flower_starts / 1000)
            flower_start_time_stamp = time.strftime("%Y-%m-%d", flower_start_time)
            self.assertEqual(flower_start_time_stamp, nectar_source_detail["flower_start"])
            flower_end_time = time.localtime(flower_ends / 1000)
            flower_end_time_stamp = time.strftime("%Y-%m-%d", flower_end_time)
            self.assertEqual(flower_end_time_stamp, nectar_source_detail["flower_end"])
            bloom_start_time = time.localtime(bloom_starts / 1000)
            bloom_start_time_stamp = time.strftime("%Y-%m-%d", bloom_start_time)
            self.assertEqual(bloom_start_time_stamp, nectar_source_detail["bloom_start"])
            bloom_end_time = time.localtime(bloom_ends / 1000)
            bloom_end_time_stamp = time.strftime("%Y-%m-%d", bloom_end_time)
            self.assertEqual(bloom_end_time_stamp, nectar_source_detail["bloom_end"])
            self.assertEqual(contacts, nectar_source_detail["contacts"])
            self.assertEqual(contact_number, nectar_source_detail["contact_number"])
            self.assertEqual(site_area, int(nectar_source_detail["site_area"]))
            self.assertEqual(nectar_source_area, int(nectar_source_detail["nectar_source_area"]))
            self.assertEqual(str(vehicle_length), nectar_source_detail["vehicle_length"])
            self.assertEqual(price, int(nectar_source_detail["price"]))
            self.assertEqual(remark, nectar_source_detail["remark"])
        else:
            self.assertTrue(False, "内部蜂场添加失败")

    def test_mobile_nectar_source_add_without_name(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 蜜源名称为空
        :return:
        """
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=None, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("蜜源名称不能为空", response['errorMsg'])

    def test_mobile_nectar_source_add_with_long_name(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 蜜源名称超过20字
        :return:
        """
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_='123456789012345678900', type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("蜜源名称不能超过20字", response['errorMsg'])

    def test_mobile_nectar_source_add_without_type(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 蜜源类型为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=None, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("蜜源品种不能为空", response['errorMsg'])

    def test_mobile_nectar_source_add_with_wrong_type_id(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 蜜源类型错误
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1000, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("蜜源类型不存在", response['errorMsg'])

    def test_mobile_nectar_source_add_without_province_id(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 省份为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=None,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("省不能为空", response['errorMsg'])

    def test_mobile_nectar_source_add_without_city_id(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 城市为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=None, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("市不能为空", response['errorMsg'])

    def test_mobile_nectar_source_add_with_wrong_lng(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 错误的lng
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1000, province_=65,
                                                                city_=6502, lng_=-190, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("经度超出范围(-180~+180)", response['errorMsg'])

    def test_mobile_nectar_source_add_with_wrong_province_id(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 错误的region_id
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=0,
                                                                city_=0, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("省码不存在", response['errorMsg'])

    def test_mobile_nectar_source_add_with_wrong_lat(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 错误的lat
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1000, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=-95,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("纬度超出范围(-90~+90)", response['errorMsg'])

    def test_mobile_nectar_source_add_without_address(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 蜜源地址为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_=None,
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("详细地址不能为空", response['errorMsg'])

    def test_mobile_nectar_source_add_without_flower_start(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 盛花时间开始时间为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=None,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("盛花期起始时间不能为空", response['errorMsg'])

    def test_mobile_nectar_source_add_without_flower_end(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 盛花结束时间为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=None, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("盛花期结束时间不能为空", response['errorMsg'])

    def test_mobile_nectar_source_add_without_bloom_start(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 开始时间开始时间为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=None,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("开花期结束时间不能为空", response['errorMsg'])

    def test_mobile_nectar_source_add_without_bloom_end(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 开花时间结束时间为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=None,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=1321530)
        self.assertEqual("开花期结束时间不能为空", response['errorMsg'])

    def test_mobile_nectar_source_add_with_wrong_flower_time(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 盛花时间不包含在开花时间内
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1577808000000,
                                                                flowerEnd_=1577894400000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("开花时间段需包含盛花时间段", response['errorMsg'])

    def test_mobile_nectar_source_add_without_contacts(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 联系人为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_=None, contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("联系人不能为空", response['errorMsg'])

    def test_mobile_nectar_source_add_with_long_contacts(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 超长联系人名称
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕12345678901234567890',
                                                                contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("联系人不能超过20字", response['errorMsg'])

    def test_mobile_nectar_source_add_without_contact_number(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 联系电话为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=None,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("联系电话不能为空", response['errorMsg'])

    def test_mobile_nectar_source_add_with_long_contact_number(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 联系电话格式错误
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=892168933332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("联系电话格式不正确", response['errorMsg'])

    def test_mobile_nectar_source_add_without_site_area(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 场地面积为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=None,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("场地面积不能为空", response['errorMsg'])

    def test_mobile_nectar_source_add_with_long_site_area(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 超长场地面积
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=493857332266400000,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("场地面积最多8位整数+两位小数", response['errorMsg'])

    def test_mobile_nectar_source_add_without_nectar_source_area(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 蜜源面积为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=None,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("蜜源面积不能为空", response['errorMsg'])

    def test_mobile_nectar_source_add_with_long_nectar_source_area(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 蜜源面积超长
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=3816758633944200000,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("蜜源面积最多8位整数+两位小数", response['errorMsg'])

    def test_mobile_nectar_source_add_without_vehicle_length(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 可通行车辆最大长度(类型)为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=None,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("可通行车辆最大长度(类型)不能为空", response['errorMsg'])

    def test_mobile_nectar_source_add_with_wrong_vehicle_length(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 可通行车辆最大长度(类型)为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1000,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("车辆类型不存在", response['errorMsg'])

    def test_mobile_nectar_source_add_with_long_am_num(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 意蜂场数量超长
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=1001, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("蜂场数量范围1~999整数", response['errorMsg'])

    def test_mobile_nectar_source_add_with_long_ac_num(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 中蜂场数量超长
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=1001, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("蜂场数量范围1~999整数", response['errorMsg'])

    def test_mobile_nectar_source_add_with_long_remark(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 备注超长
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=251)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("蜜源信息备注不能超过200字", response['errorMsg'])

    def test_mobile_nectar_source_add_without_water_pic(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 水源照片为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("OK", response['status'])

    def test_mobile_nectar_source_add_without_road_pic(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 道路图片为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic,
                                                                price_=132153)
        self.assertEqual("道路照片不能为空", response['errorMsg'])

    def test_mobile_nectar_source_add_without_site_pic(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 远景照片为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=132153)
        self.assertEqual("远景照片不能为空", response['errorMsg'])

    def test_mobile_nectar_source_add_with_wrong_price(self):
        """
        POST /mobile/nectar-source/add 新建蜜源- 蜜源价格超过最大值
        :return:
        """
        price = 100000000
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001, province_=65,
                                                                city_=6502, lng_=97.92522696494416, lat_=29.92445012687,
                                                                address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                flowerStart_=1572457560000,
                                                                flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                bloomEnd_=1576602314000,
                                                                contacts_='江海燕', contactNumber_=18921689332,
                                                                siteArea_=49385733226640,
                                                                nectarSourceArea_=38167586339442,
                                                                vehicleLength_=1003,
                                                                amNum_=5, acNum_=443, remark_=remark,
                                                                waterPic_=water_pic,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                price_=price)
        self.assertEqual("蜂场价格最多6位整数+两位小数", response['errorMsg'])

    def test_mobile_nectar_source_del(self):
        """
        POST /mobile/nectar-source/del 蜜源删除
        :return:
        """
        nectar_source = self.nectar_source_db.sql_nectar_source_id_by_status()
        if nectar_source[0]["id"] is not None:
            num = random.randrange(0, len(nectar_source))
            nectar_source_id = nectar_source[num]["id"]
            response = self.nectar_source._mobile_nectar_source_del(id_=nectar_source_id)
            self.assertEqual("没有操作权限", response['errorMsg'])
        else:
            self.assertTrue(False, "暂无待入驻蜜源地")

    def test_mobile_nectar_source_del_with_wrong_status_nectar_source_id(self):
        """
        POST /mobile/nectar-source/del 蜜源删除--删除不存在的自有蜂场
        :return:
        """
        response = self.nectar_source._mobile_nectar_source_del(id_=0)
        self.assertEqual("没有操作权限", response['errorMsg'])

    def test_mobile_nectar_source_del_with_wrong_nectar_source_id(self):
        """
        POST /mobile/nectar-source/del 蜜源删除--删除已入驻状态的自有蜂场
        :return:
        """
        response = self.nectar_source._mobile_nectar_source_del(id_=15)
        self.assertEqual("没有操作权限", response['errorMsg'])

    def test_mobile_nectar_source_detail(self):
        """
        POST /mobile/nectar-source/detail 自有蜂场详情
        :return:
        """
        nectar_source = self.nectar_source_db.sql_all_nectar_source()
        if nectar_source[0]["id"] is not None:
            num = random.randrange(0, len(nectar_source))
            nectar_source_id = nectar_source[num]["id"]
            response = self.nectar_source._mobile_nectar_source_detail(id_=nectar_source_id)
            self.assertEqual(response['status'], "OK")
        else:
            self.assertTrue(False, "暂无蜂场")

    def test_mobile_nectar_source_detail_with_wrong_nectar_source_id(self):
        """
        POST /mobile/nectar-source/detail 蜜源详情--查看不存在自有蜂场详情
        :return:
        """

        response = self.nectar_source._mobile_nectar_source_detail(id_=0)
        self.assertEqual("蜂场不存在", response['errorMsg'])

    def test_mobile_nectar_source_edit(self):
        """
        POST /mobile/nectar-source/edit 编辑蜜源
        :return:
        """
        nectar_source = self.nectar_source_db.sql_all_nectar_source()
        if nectar_source[0]["id"] is not None:
            num = random.randrange(0, len(nectar_source))
            nectar_source_id = nectar_source[num]["id"]
            name = self.fake.text(max_nb_chars=20)
            db_type = self.nectar_source_db.sql_random_nectar_source_type(random.randint(1, 5))
            type_list = Tool.data_assemble('typeCode', db_type)
            type_str = ",".join(type_list)
            base_type = random.randint(1, 3)
            province_id, city_id, district_id, address, lng, lat = self.fl.fake_location()
            altitude = random.randint(100, 1000)
            start_date = datetime.datetime(year=2020, month=1, day=1)
            end_data = datetime.datetime(year=2020, month=6, day=15)
            bloom_start = self.fake.date_time_between(start_date=start_date, end_date=end_data)
            bloom_starts = int(bloom_start.timestamp() * 1000)
            bloom_end = self.fake.date_time_between(start_date=bloom_start, end_date=end_data)
            bloom_ends = int(bloom_end.timestamp() * 1000)
            flower_start = self.fake.date_time_between(start_date=bloom_start, end_date=bloom_end)
            flower_starts = int(flower_start.timestamp() * 1000)
            flower_end = self.fake.date_time_between(start_date=flower_start, end_date=bloom_end)
            flower_ends = int(flower_end.timestamp() * 1000)
            contacts = self.fake.name()
            contact_number = self.fake.phone_number()
            site_area = self.fake.random_int(min=1, max=99999999)
            nectar_source_area = self.fake.random_int(min=1, max=99999999)
            expect_ive_num = random.randint(1, 99999)
            price = self.fake.random_int(min=1, max=999999) * 100
            vehicle_length = random.randint(1001, 1018)
            remark = self.fake.text(max_nb_chars=200)
            prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
            prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
            tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
            tent_pic = json.dumps(tent_pic, ensure_ascii=False)
            site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
            site_pic = json.dumps(site_pic, ensure_ascii=False)
            road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
            road_pic = json.dumps(road_pic, ensure_ascii=False)
            water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
            water_pic = json.dumps(water_pic, ensure_ascii=False)
            response = self.nectar_source._mobile_nectar_source_edit(type_=type_list, id_=nectar_source_id, name_=name, baseType_=base_type,
                                                                     province_=province_id, city_=city_id, county_=district_id, address_=address, lng_=lng, lat_=lat,
                                                                     altitude_=altitude,
                                                                     flowerStart_=flower_starts,
                                                                     flowerEnd_=flower_ends, bloomStart_=bloom_starts,
                                                                     bloomEnd_=bloom_ends,
                                                                     contacts_=contacts, contactNumber_=contact_number,
                                                                     siteArea_=site_area,
                                                                     nectarSourceArea_=nectar_source_area,
                                                                     expectHiveNum_=expect_ive_num,
                                                                     price_=price,
                                                                     vehicleLength_=vehicle_length,
                                                                     remark_=remark,
                                                                     prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                     waterPic_=water_pic)
            if response["status"] == "OK":
                nectar_sources = self.nectar_source_db.sql_nectar_source_by_id(nectar_source_id)
                nectar_source_detail = nectar_sources[0]
                self.assertEqual(name, nectar_source_detail["name"])
                self.assertEqual(type_str, nectar_source_detail["type"])
                self.assertEqual(base_type, nectar_source_detail["base_type"])
                self.assertEqual(int(province_id), nectar_source_detail["province"])
                self.assertEqual(int(city_id), nectar_source_detail["city"])
                self.assertEqual(int(district_id), nectar_source_detail["county"])
                self.assertEqual(lng, nectar_source_detail["lng"])
                self.assertEqual(lat, nectar_source_detail["lat"])
                self.assertEqual(address, nectar_source_detail["address"])
                self.assertEqual(altitude, nectar_source_detail["altitude"])
                flower_start_time = time.localtime(flower_starts / 1000)
                flower_start_time_stamp = time.strftime("%Y-%m-%d", flower_start_time)
                self.assertEqual(flower_start_time_stamp, nectar_source_detail["flower_start"])
                flower_end_time = time.localtime(flower_ends / 1000)
                flower_end_time_stamp = time.strftime("%Y-%m-%d", flower_end_time)
                self.assertEqual(flower_end_time_stamp, nectar_source_detail["flower_end"])
                bloom_start_time = time.localtime(bloom_starts / 1000)
                bloom_start_time_stamp = time.strftime("%Y-%m-%d", bloom_start_time)
                self.assertEqual(bloom_start_time_stamp, nectar_source_detail["bloom_start"])
                bloom_end_time = time.localtime(bloom_ends / 1000)
                bloom_end_time_stamp = time.strftime("%Y-%m-%d", bloom_end_time)
                self.assertEqual(bloom_end_time_stamp, nectar_source_detail["bloom_end"])
                self.assertEqual(contacts, nectar_source_detail["contacts"])
                self.assertEqual(contact_number, nectar_source_detail["contact_number"])
                self.assertEqual(site_area, int(nectar_source_detail["site_area"]))
                self.assertEqual(nectar_source_area, int(nectar_source_detail["nectar_source_area"]))
                self.assertEqual(str(vehicle_length), nectar_source_detail["vehicle_length"])
                self.assertEqual(price, int(nectar_source_detail["price"]))
                self.assertEqual(remark, nectar_source_detail["remark"])
            else:
                self.assertTrue(False, "蜂场修改失败")
            # self.assertEqual(response['status'], "OK")
        else:
            self.assertTrue(False, "暂无蜂场")

    def test_mobile_nectar_source_edit_without_name(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 蜜源名称为空
        :return:
        """
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=None, id_=5, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 waterPic_=water_pic,
                                                                 price_=132153)
        self.assertEqual("蜜源名称不能为空", response['errorMsg'])

    def test_mobile_nectar_source_edit_with_long_name(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 蜜源名称超过20字
        :return:
        """
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_='123456789012345678900', type_=1001,
                                                                 province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 id_=5,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 waterPic_=water_pic,price_=132153)
        self.assertEqual("蜜源名称不能超过20字", response['errorMsg'])

    def test_mobile_nectar_source_edit_without_type(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 蜜源类型为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=None, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic, id_=5,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic, price_=132153)
        self.assertEqual("蜜源品种不能为空", response['errorMsg'])

    def test_mobile_nectar_source_edit_with_wrong_type_id(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 蜜源类型错误
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1000, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003, id_=5,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153)
        self.assertEqual("蜜源类型不存在", response['errorMsg'])

    def test_mobile_nectar_source_edit_without_province_id(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 省份为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=None,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003, id_=5,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153)
        self.assertEqual("省不能为空", response['errorMsg'])

    def test_mobile_nectar_source_edit_without_city_id(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 城市为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=None, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003, id_=5,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153)
        self.assertEqual("市不能为空", response['errorMsg'])

    def test_mobile_nectar_source_edit_with_wrong_lng(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 错误的lng
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1000, province_=65,
                                                                 city_=6502, lng_=-190, lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003, id_=5,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153)
        self.assertEqual("经度超出范围(-180~+180)", response['errorMsg'])

    def test_mobile_nectar_source_edit_with_wrong_province_id(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 错误的region_id
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=0,
                                                                 city_=0, lng_=97.92522696494416, lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003, id_=5,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153)
        self.assertEqual("省码不存在", response['errorMsg'])

    def test_mobile_nectar_source_edit_with_wrong_lat(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 错误的lat
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1000, province_=65,
                                                                 city_=6502, lng_=97.92522696494416, lat_=-95,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003, id_=5,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153)
        self.assertEqual("纬度超出范围(-90~+90)", response['errorMsg'])

    def test_mobile_nectar_source_edit_without_address(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 蜜源地址为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_=None,
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640, id_=5,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153)
        self.assertEqual("详细地址不能为空", response['errorMsg'])

    def test_mobile_nectar_source_edit_without_flower_start(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 盛花时间开始时间为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=None,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003, id_=5,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153)
        self.assertEqual("盛花期起始时间不能为空", response['errorMsg'])

    def test_mobile_nectar_source_edit_without_flower_end(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 盛花结束时间为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=None, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003, id_=5,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153)
        self.assertEqual("盛花期结束时间不能为空", response['errorMsg'])

    def test_mobile_nectar_source_edit_without_bloom_start(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 开始时间开始时间为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=None,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003, id_=5,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153)
        self.assertEqual("开花期结束时间不能为空", response['errorMsg'])

    def test_mobile_nectar_source_edit_without_bloom_end(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 开花时间结束时间为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=None, id_=5,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153)
        self.assertEqual("开花期结束时间不能为空", response['errorMsg'])

    def test_mobile_nectar_source_edit_with_wrong_flower_time(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 盛花时间不包含在开花时间内
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416, lat_=29.9244501268,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1577808000000,
                                                                 flowerEnd_=1577894400000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003, id_=5,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153)
        self.assertEqual("开花时间段需包含盛花时间段", response['errorMsg'])

    def test_mobile_nectar_source_edit_without_contacts(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 联系人为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416, lat_=29.9244501268,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_=None, contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic, id_=5,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153)
        self.assertEqual("联系人不能为空", response['errorMsg'])

    def test_mobile_nectar_source_edit_with_long_contacts(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 超长联系人名称
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416, lat_=29.9244501268,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕12345678901234567890',
                                                                 contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic, id_=5,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153)
        self.assertEqual("联系人不能超过20字", response['errorMsg'])

    def test_mobile_nectar_source_edit_without_contact_number(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 联系电话为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=None,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153, id_=5)
        self.assertEqual("联系电话不能为空", response['errorMsg'])

    def test_mobile_nectar_source_edit_with_long_contact_number(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 联系电话格式错误
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=892168933332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153, id_=5)
        self.assertEqual("联系电话格式不正确", response['errorMsg'])

    def test_mobile_nectar_source_edit_without_site_area(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 场地面积为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=None,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153, id_=5)
        self.assertEqual("场地面积不能为空", response['errorMsg'])

    def test_mobile_nectar_source_edit_with_long_site_area(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 超长场地面积
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=493857332266400000,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153, id_=5)
        self.assertEqual("场地面积不超过15位正整数", response['errorMsg'])

    def test_mobile_nectar_source_edit_without_nectar_source_area(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 蜜源面积为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=None,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153, id_=5)
        self.assertEqual("蜜源面积不能为空", response['errorMsg'])

    def test_mobile_nectar_source_edit_with_long_nectar_source_area(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 蜜源面积超长
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=3816758633944200000,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153, id_=5)
        self.assertEqual("蜜源面积不超过15位正整数", response['errorMsg'])

    def test_mobile_nectar_source_edit_without_vehicle_length(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 可通行车辆最大长度(类型)为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=None,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153, id_=5)
        self.assertEqual("可通行车辆最大长度(类型)不能为空", response['errorMsg'])

    def test_mobile_nectar_source_edit_with_wrong_vehicle_length(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 可通行车辆最大长度(类型)为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1000,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153, id_=5)
        self.assertEqual("车辆类型不存在", response['errorMsg'])

    def test_mobile_nectar_source_edit_with_long_am_num(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 意蜂场数量超长
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=1001, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153, id_=5)
        self.assertEqual("蜂场数量范围1~999整数", response['errorMsg'])

    def test_mobile_nectar_source_edit_with_long_ac_num(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 中蜂场数量超长
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=1001, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153, id_=5)
        self.assertEqual("蜂场数量范围1~999整数", response['errorMsg'])

    def test_mobile_nectar_source_edit_with_long_remark(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 备注超长
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = "啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦" \
                 "啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦" \
                 "啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦" \
                 "啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦"
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153, id_=5)
        self.assertEqual("蜜源信息备注不能超过200字", response['errorMsg'])

    def test_mobile_nectar_source_edit_without_water_pic(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 水源照片为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=None,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153, id_=5)
        self.assertEqual("OK", response['status'])

    def test_mobile_nectar_source_edit_without_road_pic(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 道路图片为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153, id_=5)
        self.assertEqual("道路照片不能为空", response['errorMsg'])

    def test_mobile_nectar_source_edit_without_site_pic(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 场地照片为空
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=132153, id_=5)
        self.assertEqual("场地照片不能为空", response['errorMsg'])

    def test_mobile_nectar_source_edit_with_wrong_price(self):
        """
        POST /mobile/nectar-source/add 编辑蜜源- 蜜源价格超过最大值
        :return:
        """
        price = 100000000
        name = self.fake.text(max_nb_chars=20)
        remark = self.fake.text(max_nb_chars=200)
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        water_pic = ["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1577330419920.jpg"]
        water_pic = json.dumps(water_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_edit(name_=name, type_=1001, province_=65,
                                                                 city_=6502, lng_=97.92522696494416,
                                                                 lat_=29.92445012687,
                                                                 address_='西藏自治区昌都市左贡县仁果乡加永瑞剌',
                                                                 flowerStart_=1572457560000,
                                                                 flowerEnd_=1574536749000, bloomStart_=1563660242000,
                                                                 bloomEnd_=1576602314000,
                                                                 contacts_='江海燕', contactNumber_=18921689332,
                                                                 siteArea_=49385733226640,
                                                                 nectarSourceArea_=38167586339442,
                                                                 vehicleLength_=1003,
                                                                 amNum_=5, acNum_=443, remark_=remark,
                                                                 waterPic_=water_pic,
                                                                 prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                 price_=price, id_=5)
        self.assertEqual("蜜源价格不超过8位正整数", response['errorMsg'])

    def test_mobile_nectar_source_list(self):
        """
        POST /mobile/nectar-source/list 自有蜂场列表
        :return:
        """
        response = self.nectar_source._mobile_nectar_source_list()
        self.assertEqual(response['status'], "OK")

    def test_mobile_nectar_source_list_with_include_status(self):
        """
        POST /mobile/nectar-source/list 蜜源列表-蜜源状态查询
        :return:
        """
        response = self.nectar_source._mobile_nectar_source_list(includeStatus_=[1, 2])
        self.assertEqual(response['status'], "OK")

    def test_mobile_nectar_source_list_include_area(self):
        """
        POST /mobile/nectar-source/list 蜜源列表-蜜源地区查询
        :return:
        """
        response = self.nectar_source._mobile_nectar_source_list(includeCity_=450700)
        self.assertEqual(response['status'], "OK")

    def test_mobile_nectar_source_list_with_include_type(self):
        """
        POST /mobile/nectar-source/list 蜜源列表-蜜源类型查询
        :return:
        """
        response = self.nectar_source._mobile_nectar_source_list(includeType_=[1001, 1046])
        self.assertEqual(response['status'], "OK")

    def test_mobile_nectar_source_list_with_flower_start(self):
        """
        POST /mobile/nectar-source/list 蜜源列表--蜜源花期查询-只输入盛花开始时间
        :return:
        """
        response = self.nectar_source._mobile_nectar_source_list(searchFlowerStart_=1574524800000)
        self.assertEqual(response['status'], "OK")

    def test_mobile_nectar_source_list_with_flower_end(self):
        """
        POST /mobile/nectar-source/list 蜜源列表--蜜源花期查询-只输入盛花结束时间
        :return:
        """
        response = self.nectar_source._mobile_nectar_source_list(searchFlowerEnd_=1574524800000)
        self.assertEqual(response['status'], "OK")

    def test_mobile_nectar_source_list_with_flower_time(self):
        """
        POST /mobile/nectar-source/list 蜜源列表--蜜源花期查询-输入全部时间
        :return:
        """
        response = self.nectar_source._mobile_nectar_source_list(searchFlowerStart_=1577116800000,
                                                                 searchFlowerEnd_=1577203199000)
        self.assertEqual(response['status'], "OK")

    def test_mobile_enter_enter_check(self):
        """
        POST /mobile/enter/enter-check 平台入驻前校验
        :return:
        """
        container_list = self.container_db.sql_container_by_status()
        if container_list[0]["id"] is not None:
            random_container = random.sample(container_list, 3)
            random_container_id = [x["id"] for x in random_container]
            random_serial_no = [y["serial_no"] for y in random_container]
            # container_ids = []
            # serial_nos = []
            # for i in range(3):
            #     num = random.randrange(0, len(container_list))
            #     container_id = container_list[num]["id"]
            #     serial_no = container_list[num]["serial_no"]
            #     container_ids.append(container_id)
            #     serial_nos.append(serial_no)
            # container = list(set(container_ids))
            # serial_no = list(set(serial_nos))
            nectar_source = self.nectar_source_db.sql_all_nectar_source()
            if nectar_source[0]["id"] is not None:
                num = random.randrange(0, len(nectar_source))
                nectar_source_id = nectar_source[num]["id"]
                response = self.nectar_source._mobile_enter_enter_check(containerIds_=random_container_id,
                                                                        nectarSourceId_=nectar_source_id)
                if response['status'] == "ERROR":
                    self.assertEqual(response['status'], "ERROR")
                    response_serial_nos = re.sub("[^a-zA-Z0-9]", "、", response['errorMsg']).split("、")
                    response_serial_no = list(filter(None, response_serial_nos))
                    for i in response_serial_no:
                        if i not in random_serial_no:
                            self.assertTrue(False, "检验错误")
                    # self.assertEqual(response['errorMsg'], "【分层式平台】%s、【分层式平台】%s、【分层式平台】%s已在其他蜜源地入驻中,请再次确认是否入驻新蜜源地"
                    #                  % (random_serial_no[0], random_serial_no[1], random_serial_no[2]))
        else:
            self.assertTrue(False, "暂无养蜂平台")

    def test_mobile_enter_enter_check_with_del_container_id(self):
        """
        POST /mobile/enter/enter-check 平台入驻前校验--传入已删除的养蜂平台ID
        :return:
        """

        response = self.nectar_source._mobile_enter_enter_check(containerIds_=16,
                                                                nectarSourceId_=25)
        self.assertEqual("所选平台中部分已被删除,请重新选择", response['errorMsg'])

    def test_mobile_enter_enter_check_with_wrong_container_id(self):
        """
        POST /mobile/enter/enter-check 平台入驻前校验--传入不存在的养蜂平台ID
        :return:
        """

        response = self.nectar_source._mobile_enter_enter_check(containerIds_=0,
                                                                nectarSourceId_=25)
        self.assertEqual("所选平台中部分已被删除,请重新选择", response['errorMsg'])

    def test_mobile_enter_enter_check_with_wrong_nectar_source_id(self):
        """
        POST /mobile/enter/enter-check 平台入驻前校验--传入不存在的蜜源地ID
        :return:
        """

        response = self.nectar_source._mobile_enter_enter_check(containerIds_=2,
                                                                nectarSourceId_=0)
        self.assertEqual("蜜源不存在", response['errorMsg'])

    def test_mobile_enter_enter_save(self):
        """
        POST /mobile/enter/enter-save 平台入驻
        :return:
        """
        container_list = self.container_db.sql_all_container()
        if container_list[0]["id"] is not None:
            container_ids = []
            for i in range(3):
                num = random.randrange(0, len(container_list))
                container_id = container_list[num]["id"]
                container_ids.append(container_id)
            container = list(set(container_ids))
            nectar_source = self.nectar_source_db.sql_all_nectar_source()
            if nectar_source[0]["id"] is not None:
                num = random.randrange(0, len(nectar_source))
                nectar_source_id = nectar_source[num]["id"]
                # start_date = datetime.datetime(year=2020, month=1, day=1)
                # end_data = datetime.datetime(year=2020, month=6, day=15)
                # enter_time = self.fake.date_time_between(start_date=start_date, end_date=end_data)
                # enter_times = int(enter_time.timestamp() * 1000)
                # entertime：大于入驻平台最近的一次入驻或撤场时间，小于等于当前时间
                hive_num = random.randint(1, 999999)
                response = self.nectar_source._mobile_enter_enter_save(containerIds_=container,
                                                                       hiveNum_=hive_num,
                                                                       nectarSourceId_=213,
                                                                       enterTime_=1591977600000)
                self.assertEqual(response['status'], "OK")
            else:
                self.assertTrue(False, "暂无蜂场")
        else:
            self.assertTrue(False, "暂无养蜂平台")

    def test_mobile_enter_enter_save_with_wrong_nectar_source_id(self):
        """
        POST /mobile/enter/enter-save 平台入驻--错误的蜜源地ID
        :return:
        """
        response = self.nectar_source._mobile_enter_enter_save(containerIds_=2,
                                                               nectarSourceId_=0,
                                                               enterTime_=1576602314000)
        self.assertEqual("蜜源不存在", response['errorMsg'])

    def test_mobile_enter_enter_save_with_wrong_container_id(self):
        """
        POST /mobile/enter/enter-save 平台入驻--错误的养蜂平台ID
        :return:
        """
        response = self.nectar_source._mobile_enter_enter_save(containerIds_=0,
                                                               nectarSourceId_=6,
                                                               enterTime_=1576602314000)
        self.assertEqual("所选平台中部分已被删除,请重新选择", response['errorMsg'])

    def test_mobile_enter_enter_save_with_wrong_enter_time(self):
        """
        POST /mobile/enter/enter-save 平台入驻--大于当前时间的时间戳
        :return:
        """
        response = self.nectar_source._mobile_enter_enter_save(containerIds_=2,
                                                               nectarSourceId_=6,
                                                               enterTime_=1585843200000)
        self.assertEqual("入驻时间不能晚于当前时间", response['errorMsg'])

    def test_mobile_nectar_source_leave(self):
        """
        POST /mobile/nectar-source/leave 平台和蜂箱撤场
        :return:
        """
        nectar_source = self.nectar_source_db.sql_all_nectar_source()
        if nectar_source[0]["id"] is not None:
            num = random.randrange(0, len(nectar_source))
            nectar_source_id = nectar_source[num]["id"]
            seetle_time_db = self.nectar_source_db.sql_nectar_source_last_seetle_time(nectar_source_id=nectar_source_id)
            if seetle_time_db:
                leave_time_start = seetle_time_db
                leave_time_end = int(time.time() * 1000)
                leave_time = random.randint(leave_time_start, leave_time_end)
            else:
                start_date = datetime.datetime(year=2020, month=1, day=1)
                end_data = datetime.datetime(year=2020, month=12, day=30)
                leave_times = self.fake.date_time_between(start_date=start_date, end_date=end_data)
                leave_time = int(leave_times.timestamp() * 1000)
            response = self.nectar_source._mobile_nectar_source_leave(nectarSourceId_=nectar_source_id, leaveTime_=leave_time)
            self.assertEqual(response['status'], "OK")
        else:
            self.assertTrue(False, "暂无内部蜂场")

    def test_mobile_nectar_source_add_with_required(self):
        """
        POST /mobile/nectar-source/add 新建自有蜂场- 只填写必填项
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        province_id, city_id, district_id, address, lng, lat = self.fl.fake_location()
        prospect_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186431321.jpg"]
        prospect_pic = json.dumps(prospect_pic, ensure_ascii=False)
        tent_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186460148.jpg"]
        tent_pic = json.dumps(tent_pic, ensure_ascii=False)
        site_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186528062.jpg"]
        site_pic = json.dumps(site_pic, ensure_ascii=False)
        road_pic = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"]
        road_pic = json.dumps(road_pic, ensure_ascii=False)
        response = self.nectar_source._mobile_nectar_source_add(name_=name, type_=1001,  baseType_=None, province_=province_id,
                                                                city_=city_id, lng_=lng, lat_=lat, county_=district_id,
                                                                address_=address, altitude_=None,
                                                                flowerStart_=None, flowerEnd_=None,
                                                                bloomStart_=None, bloomEnd_=None,
                                                                contacts_=None, contactNumber_=None,
                                                                siteArea_=None,
                                                                nectarSourceArea_=None,
                                                                expectHiveNum_=999,
                                                                vehicleLength_=1003,
                                                                remark_=None,
                                                                prospectPic_=prospect_pic, tentPic_=tent_pic, sitePic_=site_pic, roadPic_=road_pic,
                                                                waterPic_=None)
        self.assertEqual("OK", response['status'])
