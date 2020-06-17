#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2020 2020/3/31 17:10
工作台-蜂友资料
"""
import json
import unittest
from actions.BeeAction import BeeAction
from testCase.FakeLocation import FakeLocation
from tools.Config import Log
from sql.Bee import VisitRecordSql
from faker import Faker
from random import choice
from tools.Tool import Tool
import datetime, time
import random
import json


class WorkbenchMain(unittest.TestCase, VisitRecordSql, FakeLocation, Tool):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    workbench = BeeAction()
    config_db = VisitRecordSql()
    vr = VisitRecordSql()
    fl = FakeLocation()
    user_id = 591
    mobile = (vr.query_contact_number_buy_user(user_id=user_id))[0].get('contact_number')
    log = Log('WorkbenchMain').logger
    fake = Faker(locale="zh_CN")
    # workbench.set_user('15200000033')
    workbench.set_user(mobile)

    def test_mobile_workbench_bee_friend_add(self):
        """
        V2.0 POST /mobile/workbench-bee-friend/add 新建蜂友资料和蜂群信息
        v2.2 修改 蜂友交易需求枚举值变更
        :return:
        """
        start_date = datetime.datetime(year=2019, month=1, day=1)
        end_data = datetime.datetime(year=2020, month=2, day=26)
        regular_source = random.randint(1001, 1047)
        intention = random.choice([0, 1, 2, 3])
        sale_num = None
        intention_price = None
        sale_time = sale_province = sale_city = sale_county = None
        if intention == 1:
            sale_num = self.fake.random_int(min=1, max=999999)
            intention_price = self.fake.random_int(min=1, max=99999999)
            propagation_time = self.fake.date_time_between(start_date=start_date, end_date=end_data)
            sale_time = int(propagation_time.timestamp() * 1000)
            sale_province, sale_city, sale_county, address4, lng4, lat4 = self.fl.fake_location()
        label_type = random.randint(1001, 1006)
        keeper_name = self.fake.name()
        contact_number = self.fake.phone_number()
        contact_number = '15200000000'
        gender = random.choice([1, 2])
        native_province, native_city, native_county, address1, lng1, lat1 = self.fl.fake_location()
        age = self.fake.random_int(min=1, max=99)
        seniority = self.fake.random_int(min=1, max=99)
        scale = random.choice([1, 2, 3, 4])
        province, city, county, address, lng, lat = self.fl.fake_location()
        hive_num = self.fake.random_int(min=1, max=999999)
        standard_num = self.fake.random_int(min=1, max=hive_num)
        small_num = hive_num - standard_num
        queen_num2 = self.fake.random_int(min=1, max=hive_num)
        queen_num1 = self.fake.random_int(min=1, max=hive_num)
        queen_num = self.fake.random_int(min=1, max=hive_num)
        eke_num = self.fake.random_int(min=1, max=hive_num)
        plat_num = self.fake.random_int(min=1, max=hive_num)
        baby_num = self.fake.random_int(min=1, max=999999)
        honey_num = self.fake.random_int(min=1, max=999999)
        propagation_time = self.fake.date_time_between(start_date=start_date, end_date=end_data)
        breed_time1 = int(propagation_time.timestamp() * 1000)
        breed_place1 = '成都市高新区天府大道'
        breed_time2 = int(propagation_time.timestamp() * 1000)
        breed_place2 = '成都市高新区天府大道'
        vehicle_length = random.randint(1001, 1018)
        expect_hive_num = self.fake.random_int(min=1, max=99999)
        pics = ["http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252271444.jpg",
                "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252272949.jpg",
                "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252276148.jpg",
                "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252276812.jpg"]
        remark = self.fake.text(max_nb_chars=200)
        nectar_type = random.randint(1001, 1047)
        nectar_province, nectar_city, nectar_county, address2, lng2, lat2 = self.fl.fake_location()
        next_nectar_source = [{"nectarType": nectar_type, "province": nectar_province, "city": nectar_city,
                              "county": nectar_county}]
        next_nectar_source = json.dumps(next_nectar_source)
        regular_province, regular_city, regular_county, address3, lng3, lat3 = self.fl.fake_location()
        regular_route = [{"province": regular_province, "city": regular_city, "county": regular_county}]
        regular_route = json.dumps(regular_route)
        study_from = random.choice([1, 2, 3, 4])
        heir = random.choice([1, 2, 3])
        yiel = self.fake.random_int(min=1, max=99999999)
        income = self.fake.random_int(min=1, max=99999999)*100
        cur_nectar_type = random.randint(1001, 1047)
        queen_type = random.choice([1, 2])
        response = self.workbench._mobile_workbench_bee_friend_add(labelType_=label_type, regularSource_=regular_source,
                                                                   intention_=intention, curNectarType_=cur_nectar_type,
                                                                   province_=province, city_=city, county_=county,
                                                                   address_=address, lng_=lng, lat_=lat,
                                                                   vehicleLength_=vehicle_length,
                                                                   expectHiveNum_=expect_hive_num, pics_=pics,
                                                                   scale_=scale, hiveNum_=hive_num, smallNum_=small_num,
                                                                   queenType_=queen_type, standardNum_=standard_num,
                                                                   queenNum2_=queen_num2, queenNum1_=queen_num1,
                                                                   queenNum_=queen_num, ekeNum_=eke_num,
                                                                   platNum_=plat_num, babyNum_=baby_num,
                                                                   honeyNum_=honey_num, remark_=remark,
                                                                   nextNectarSource_=next_nectar_source,
                                                                   contactNumber_=contact_number, keeperName_=keeper_name,
                                                                   age_=age, gender_=gender, nativeProvince_=native_province,
                                                                   nativeCounty_=native_county, nativeCity_=native_city,
                                                                   seniority_=seniority, regularRoute_=regular_route,
                                                                   studyFrom_=study_from, heir_=heir, yield_=yiel,
                                                                   income_=income, breedTime1_=breed_time1,
                                                                   breedPlace1_=breed_place1, breedTime2_=breed_time2,
                                                                   breedPlace2_=breed_place2, saleNum_=sale_num,
                                                                   intentionPrice_=intention_price, saleTime_=sale_time,
                                                                   saleProvince_=sale_province, saleCity_=sale_city,
                                                                   saleCounty_=sale_county)
        self.assertEqual("OK", response["status"])

    def test_mobile_workbench_bee_friend_detail(self):
        """
        v2.0  POST /mobile/workbench-bee-friend/detail 工作台蜂友详情
        :return:
        """
        bee_friend = self.config_db.sql_all_customer()
        if bee_friend[0]["id"] is not None:
            num = random.randrange(0, len(bee_friend))
            id = bee_friend[num]["id"]
            province, city, county, address, lng, lat = self.fl.fake_location()
            response = self.workbench._mobile_workbench_bee_friend_detail(id_=id, lng_=lng, lat_=lat)
            self.assertEqual("OK", response["status"])

    def test_mobile_workbench_bee_friend_edit(self):
        """
        v2.0  POST /mobile/workbench-bee-friend/edit 编辑蜂友资料
        v2.2 修改 蜂友交易需求枚举值变更
        :return:
        """
        start_date = datetime.datetime(year=2019, month=1, day=1)
        end_data = datetime.datetime(year=2020, month=2, day=26)
        bee_friend = self.config_db.sql_all_customer()
        if bee_friend[0]["id"] is not None:
            num = random.randrange(0, len(bee_friend))
            id = bee_friend[num]["id"]
            regular_source = random.randint(1001, 1047)
            label_type = random.randint(1001, 1006)
            keeper_name = self.fake.name()
            contact_number = self.fake.phone_number()
            gender = random.choice([1, 2])
            native_province, native_city, native_county, address1, lng1, lat1 = self.fl.fake_location()
            age = self.fake.random_int(min=1, max=99)
            seniority = self.fake.random_int(min=1, max=99)
            regular_province, regular_city, regular_county, address3, lng3, lat3 = self.fl.fake_location()
            regular_route = [{"province": regular_province, "city": regular_city, "county": regular_county}]
            regular_route = json.dumps(regular_route)
            study_from = random.choice([1, 2, 3, 4])
            heir = random.choice([1, 2, 3])
            yiel = self.fake.random_int(min=1, max=99999999)
            income = self.fake.random_int(min=1, max=99999999) * 100
            propagation_time = self.fake.date_time_between(start_date=start_date, end_date=end_data)
            breed_time1 = int(propagation_time.timestamp() * 1000)
            breed_place1 = '成都市高新区天府大道'
            breed_time2 = int(propagation_time.timestamp() * 1000)
            breed_place2 = '成都市高新区天府大道'
            intention = random.choice([0, 1, 2, 3])
            sale_num = None
            intention_price = None
            sale_time = sale_province = sale_city = sale_county = None
            if intention == 1:
                sale_num = self.fake.random_int(min=1, max=999999)
                intention_price = self.fake.random_int(min=1, max=99999999)
                propagation_time = self.fake.date_time_between(start_date=start_date, end_date=end_data)
                sale_time = int(propagation_time.timestamp() * 1000)
                sale_province, sale_city, sale_county, address4, lng4, lat4 = self.fl.fake_location()
            response = self.workbench._mobile_workbench_bee_friend_edit(regularSource_=regular_source,
                                                                        labelType_=label_type, intention_=intention,
                                                                        id_=id, keeperName_=keeper_name,
                                                                        contactNumber_=contact_number, gender_=gender,
                                                                        nativeProvince_=native_province,
                                                                        nativeCity_=native_city,
                                                                        nativeCounty_=native_county, age_=age,
                                                                        seniority_=seniority,
                                                                        regularRoute_=regular_route,
                                                                        studyFrom_=study_from, heir_=heir, yield_=yiel,
                                                                        income_=income, breedTime1_=breed_time1,
                                                                        breedPlace1_=breed_place1,
                                                                        breedTime2_=breed_time2,
                                                                        breedPlace2_=breed_place2, saleNum_=sale_num,
                                                                        intentionPrice_=intention_price,
                                                                        saleTime_=sale_time,
                                                                        saleProvince_=sale_province,
                                                                        saleCity_=sale_city,
                                                                        saleCounty_=sale_county)
            self.assertEqual("OK", response["status"])

    def test_mobile_workbench_bee_friend_mobile_check(self):
        """
        v2.0  POST /mobile/workbench-bee-friend/mobile-check 校验手机号重复性
        :return:
        """
        self.workbench._mobile_workbench_bee_friend_mobile_check(userId_=None, mobile_=19982917912)

    def test_mobile_workbench_bee_friend_page_list(self):
        """
        v2.0 POST /mobile/workbench-bee-friend/page-list 工作台蜂友分页列表
        :return:
        """
        response = self.workbench._mobile_workbench_bee_friend_page_list()
        self.assertEqual("OK", response["status"])

    def test_mobile_swarm_get_by_customer(self):
        """
        v2.0 POST POST /mobile/swarm/get-by-user 根据用户id获取蜂场信息
        v2.1 POST /mobile/swarm/get-by-friend 根据蜂友id获取蜂场列表
        :return:
        """
        customer_list = self.config_db.sql_all_customer()
        if customer_list[0]["id"] is not None:
            num = random.randrange(0, len(customer_list))
            friend_id = customer_list[num]["id"]
            response = self.workbench._mobile_swarm_get_by_friend(friendId_=105)
            self.assertEqual(response['status'], "OK")
        else:
            self.assertTrue(False, "暂无客户")

    def test_mobile_swarm_edit(self):
        """
        POST mobile/swarm/edit V 2.1.0 new
        编辑蜂场信息
        :return:
        """
        swarm_list = self.vr.query_swarm_detail()
        swarm_id = random.choice(swarm_list).get('id')
        curNectarType_list = self.vr.query_regular_source()
        curNectarType = random.choice(curNectarType_list).get('key')
        vehicleLength_list = self.vr.query_vehicle_length()
        vehicleLength = random.choice(list(vehicleLength_list)).get('key')
        expectHiveNum = 500
        img_list = ["http://a0.att.hudong.com/78/52/01200000123847134434529793168.jpg"]
        img = json.dumps(img_list, ensure_ascii=False)
        scale_dict = {1: '小于1500箱', 2: '150~200箱', 3: '200~300箱', 4: '大于300箱'}
        scale = random.choice(list(scale_dict))
        self.workbench._admin_swarm_edit(id_=swarm_id, curNectarType_=curNectarType, vehicleLength_=vehicleLength,
                                         expectHiveNum_=expectHiveNum, pics_=img, scale_=scale)

    def test_mobile_swarm_detail(self):
        """
        POST mobile/swarm/detail V 2.1.0 New
        蜂场详情
        :return:
        """
        swarm_list = self.vr.query_swarm_detail()
        swarm_id = random.choice(swarm_list).get('id')
        self.workbench._mobile_swarm_detail(id_=swarm_id)

    def test_mobile_workbench_bee_friend_add_check(self):
        """
        v2.1.0 new  POST /mobile/workbench-bee-friend/add-check 新增蜂友手机号校验
        """
        mobile = '15200000000'
        response = self.workbench._mobile_workbench_bee_friend_add_check(userId_=None, mobile_=mobile)
        self.assertEqual(response['status'], "OK")



















