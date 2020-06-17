#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2020/04/15
@Author: xiujuan chen
"""


import unittest
from actions.BeeAction import BeeAction
from tools.Config import Log
from faker import Faker
from sql.Bee import NectarSourceInformationSql, ConfigInformationSql, ContainerInformationSql, StaffSql
from testCase.FakeLocation import FakeLocation
import random
import json
import time,datetime
from tools.Tool import Tool


class RegisterLoginMain(unittest.TestCase):
    """
    接口文档: http://192.168.62.242:36054/swagger-ui.html
    """
    nectar_source = BeeAction()
    config_db = ConfigInformationSql()
    nectar_source_db = NectarSourceInformationSql()
    container_db = ContainerInformationSql()
    staff_db = StaffSql()
    fl = FakeLocation()
    mobile = '15200000003'
    log = Log('BeeInformationMain').logger
    log.info("开始执行内部蜂场管理模块测试用例")
    fake = Faker(locale="zh_CN")
    nectar_source.set_user(mobile)

    def test_admin_nectar_source_count(self):
        """
        POST /admin/nectar-source/count  V 2.2.1
        内部蜂场统计
        :return:
        """
        self.nectar_source._admin_nectar_source_count()

    def test_admin_nectar_source_add(self):
        """
        POST /admin/nectar-source/add  V 2.2.1
        新增内部蜂场
        :return:
        """
        name = self.fake.text(max_nb_chars=20)
        db_type = self.nectar_source_db.sql_random_nectar_source_type(random.randint(1, 5))
        type_list = Tool.data_assemble('typeCode', db_type)
        type_str = ",".join(type_list)
        base_type = random.randint(1, 3)
        province_id, city_id, district_id, address, lng, lat = self.fl.fake_location()
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
        response = self.nectar_source._admin_nectar_source_add(type_=type_list, name_=name, baseType_=base_type,
                                                               province_=province_id, city_=city_id, county_=district_id, address_=address, lng_=lng, lat_=lat,
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

    def test_admin_nectar_source_edit(self):
        """
        POST /admin/nectar-source/edit  V 2.2.1
        编辑内部蜂场
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
            response = self.nectar_source._admin_nectar_source_edit(type_=type_list, id_=nectar_source_id, name_=name, baseType_=base_type,
                                                                    province_=province_id, city_=city_id, county_=district_id, address_=address, lng_=lng, lat_=lat,
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
        else:
            self.assertTrue(False, "暂无蜂场")

    def test_admin_nectar_source_list(self):
        """
        POST /admin/nectar-source/list  V 2.2.1
        内部蜂场列表
        :return:
        """
        response = self.nectar_source._admin_nectar_source_list()
        self.assertEqual(response['status'], "OK")

    def test_admin_nectar_source_list_with_include_status(self):
        """
        内部蜂场列表-蜂场状态查询
        :return:
        """
        response = self.nectar_source._admin_nectar_source_list(includeStatus_=2)
        self.assertEqual(response['status'], "OK")

    def test_admin_nectar_source_list_with_include_area(self):
        """
        内部蜂场列表--蜂场地区查询
        :return:
        """
        response = self.nectar_source._admin_nectar_source_list(includeProvince_=510000, includeCity_=510100)
        self.assertEqual(response['status'], "OK")

    def test_admin_nectar_source_list_with_include_type(self):
        """
        内部蜂场列表--蜜源查询
        :return:
        """
        include_type = random.randint(1001, 1047)
        response = self.nectar_source._admin_nectar_source_list(includeType_=include_type)
        self.assertEqual(response['status'], "OK")

    def test_admin_nectar_source_list_with_flower_time(self):
        """
        内部蜂场列表--蜜源花期查询-输入全部时间
        :return:
        """
        response = self.nectar_source._admin_nectar_source_list(searchFlowerStart_=1577116800000,
                                                                 searchFlowerEnd_=1577203199000)
        self.assertEqual(response['status'], "OK")

    def test_mobile_nectar_source_list_with_vehicle_length(self):
        """
        内部蜂场列表--可通行车辆查询
        :return:
        """
        vehicle_length = random.randint(1001, 1018)
        response = self.nectar_source._admin_nectar_source_list(vehicleLength_=vehicle_length)
        self.assertEqual(response['status'], "OK")

    def test_mobile_nectar_source_list_with_is_enter(self):
        """
        内部蜂场列表--是否入驻查询
        :return:
        """
        response = self.nectar_source._admin_nectar_source_list(isEnter_=random.randint(1, 2))
        self.assertEqual(response['status'], "OK")

    def test_admin_excel_export_nectar_source(self):
        """
        GET /admin/excel-export/nectar-source  V 2.2.1
        内部蜂场导出
        :return:
        """
        include_status_dict = {1: '待入驻', 2: '已入驻'}
        include_status = random.choice(list(include_status_dict))
        ct_order_type_list = ['ASC', 'DESC']
        ct_order_type = ct_order_type_list[random.randint(0, (len(ct_order_type_list)-1))]
        response = self.nectar_source._admin_excel_export_nectar_source(excludeStatus_=None, includeStatus_=None,
                                                                        includeProvince_=None, includeCity_=None,
                                                                        includeType_=None, searchName_=None,
                                                                        searchFlowerStart_=None, searchFlowerEnd_=None,
                                                                        collectTimeStart_=None, collectTimeEnd_=None,
                                                                        collector_=None, vehicleLength_=None,
                                                                        ctOrderType_=None)
        f = open('内部蜂场信息导出_20200617.xlsx', 'wb+')
        f.write(response)
        f.close()

    def test_admin_nectar_source_detail(self):
        """
        POST /admin/nectar-source/detail  V 2.2.1
        内部蜂场详情
        :return:
        """
        nectar_source = self.nectar_source_db.sql_all_nectar_source()
        if nectar_source[0]["id"] is not None:
            num = random.randrange(0, len(nectar_source))
            nectar_source_id = nectar_source[num]["id"]
            response = self.nectar_source._admin_nectar_source_detail(id_=nectar_source_id)
            self.assertEqual(response['status'], "OK")
        else:
            self.assertTrue(False, "暂无蜂场")

    def test_admin_nectar_source_del(self):
        """
        POST /admin/nectar-source/del  V 1.0
        蜜源删除
        :return:
        """
        nectar_source = self.nectar_source_db.sql_nectar_source_id_by_status()
        if nectar_source[0]["id"] is not None:
            num = random.randrange(0, len(nectar_source))
            nectar_source_id = nectar_source[num]["id"]
            response = self.nectar_source._admin_nectar_source_del(id_=nectar_source_id)
            self.assertEqual("权限不足,请联系管理员", response['errorMsg'])
        else:
            self.assertTrue(False, "暂无待入驻蜜源地")

    def test_admin_nectar_source_leave(self):
        """
        运营后台-内部蜂场信息-平台和蜂场撤场 new 2.2.1
        撤场时间：大于等于最近一次入驻时间
        :return:
        """
        nectar_source = self.nectar_source_db.sql_all_nectar_source()
        if nectar_source[0]["id"] is not None:
            num = random.randrange(0, len(nectar_source))
            nectar_source_id = nectar_source[num]["id"]
            seetle_time_db = self.nectar_source_db.sql_nectar_source_last_seetle_time(nectar_source_id=nectar_source_id)
            if seetle_time_db:
                leave_time_start = seetle_time_db
                leave_time_end = int(time.time()*1000)
                leave_time = random.randint(leave_time_start, leave_time_end)
            else:
                start_date = datetime.datetime(year=2020, month=1, day=1)
                end_data = datetime.datetime(year=2020, month=12, day=30)
                leave_times = self.fake.date_time_between(start_date=start_date, end_date=end_data)
                leave_time = int(leave_times.timestamp() * 1000)
            response = self.nectar_source._admin_nectar_source_leave(nectarSourceId_=nectar_source_id, leaveTime_=leave_time)
            self.assertEqual(response['status'], "OK")
        else:
            self.assertTrue(False, "暂无内部蜂场")

    def test_admin_enter_enter_save(self):
        """
        平台和蜂箱入驻 new 2.2.1
        入驻时间：大于等于所选平台最近的一次入驻或撤场时间，小于等于当前时间
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
                hive_num = random.randint(1, 999999)
                response = self.nectar_source._admin_enter_enter_save(containerIds_=container,
                                                                      hiveNum_=hive_num,
                                                                      nectarSourceId_=nectar_source_id,
                                                                      enterTime_=1592064000000)
                self.assertEqual(response['status'], "OK")
            else:
                self.assertTrue(False, "暂无蜂场")
        else:
            self.assertTrue(False, "暂无养蜂平台")

    def test_admin_bee_friend_own_list(self):
        """
        自有养蜂人列表 new 2.2.1
        :return:
        """
        response = self.nectar_source._admin_bee_friend_own_list()
        self.assertEqual(response["status"], "OK")

    def test_admin_bee_friend_own_list_with_role(self):
        """
        自有养蜂人列表--用户角色查询 new 2.2.1
        :return:
        """
        role_code_list = ['1002', '1003']
        role_code = role_code_list[random.randint(0, (len(role_code_list) - 1))]
        response = self.nectar_source._admin_bee_friend_own_list(roleCode_=role_code)
        self.assertEqual(response["status"], "OK")

    def test_admin_bee_friend_own_list_with_location(self):
        """
        自有养蜂人列表--人员位置查询 new 2.2.1
        :return:
        """
        province_id, city_id, district_id, address, lng, lat = self.fl.fake_location()
        response = self.nectar_source._admin_bee_friend_own_list(province_=province_id, city_=city_id)
        if response["status"] == "OK":
           staff_db = self.staff_db.sql_bee_friend_own_count_by_area(province=province_id, city=city_id)
           if len(staff_db):
                self.assertEqual(response["content"]["tc"], len(staff_db))
           else:
                self.assertTrue(False, "数据库未查询出数据")
        else:
            self.assertTrue(False, "查询失败")

    def test_admin_bee_friend_own_count(self):
        """
        自有养蜂人数据统计--养蜂技师和养蜂总监总数
        :return:
        """
        response = self.nectar_source._admin_bee_friend_own_count()
        if response["status"] == "OK":
            staff_db = self.staff_db.sql_bee_friend_own_count()
            self.assertEqual(response["content"]["total"], len(staff_db))
        else:
            self.assertTrue(False, "自有养蜂人总数查询失败")
