#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2020/04/15
@Author: xiujuan chen
"""


import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log.logger import logger
from faker import Faker
from testcase.flowerChaser.sql.Bee  import NectarSourceInformationSql
from sql.Passport import PassportInfoSql
from utils.fake.FakeLocation import FakeLocation
from testcase.flowerChaser.sql.Bee  import VisitRecordSql
import json
import random
import datetime


class RegisterLoginMain(unittest.TestCase):
    """
    接口文档: http://192.168.62.242:36054/swagger-ui.html
    """
    ba = BeeAction()
    ns = NectarSourceInformationSql()
    ps = PassportInfoSql()
    vr = VisitRecordSql()
    user_id = 591
    mobile = (vr.query_contact_number_buy_user(user_id=user_id))[0].get('contact_number')
    fl = FakeLocation()
    # mobile = '19982917912'
    log = logger('BeeInformationMain').logger
    log.info("开始执行蜂友管理模块测试用例")
    fake = Faker(locale="zh_CN")
    ba.set_user(mobile)

    def test_admin_bee_friend_add(self):
        """
        POST /admin/bee-friend/add  V 1.0
        V 2.2 Update
        新建蜂友资料和蜂群信息
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
        income = self.fake.random_int(min=1, max=99999999) * 100
        cur_nectar_type = random.randint(1001, 1047)
        queen_type = random.choice([1, 2])
        response = self.ba._admin_bee_friend_add(labelType_=label_type, regularSource_=regular_source,
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
                                                 contactNumber_=contact_number,
                                                 keeperName_=keeper_name,
                                                 age_=age, gender_=gender,
                                                 nativeProvince_=native_province,
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

    def test_admin_bee_friend_edit(self):
        """
        POST /admin/bee-friend/edit  V 2.2 Update
        编辑蜂友资料
        :return:
        """
        friend_info = self.vr.query_friend_info_by_user_id(user_id=self.user_id)
        friend_id = friend_info[0]['id']
        label_type = random.randint(1001, 1006)
        province_list = self.ns.sql_region(level=0)  # level 0.省,  1.市,  2.区
        province = (random.sample(province_list, 1))[0]['id']
        city_list = self.ns.sql_region(level=1)
        city = (random.sample(city_list, 1))[0]['id']
        address = '接口测试编辑蜜源详细地址'
        lng = '116.092952'
        lat = '40.073798'
        img_list = ["http://a0.att.hudong.com/78/52/01200000123847134434529793168.jpg"]
        img = json.dumps(img_list, ensure_ascii=False)
        age = 22
        gender_dict = {1: "男", 2: "女"}
        gender = random.choice(list(gender_dict))
        seniority = 22
        str_start = str(random.choice(['135', '136', 138]))
        str_end = ''.join(random.sample('0123456789', 8))
        contact_number = str_start + str_end
        keeper_name = '陈秀娟'
        regular_source = None
        response = self.ba._admin_bee_friend_edit(regularSource_=regular_source, labelType_=label_type, intention_=None,
                                                  id_=friend_id,
                                                  keeperName_=keeper_name, contactNumber_=contact_number, gender_=gender,
                                                  nativeProvince_=None, nativeCity_=None, nativeCounty_=None, age_=age,
                                                  seniority_=seniority, regularRoute_=None, studyFrom_=None, heir_=None,
                                                  yield_=None, income_=None, breedTime1_=None, breedPlace1_=None,
                                                  breedTime2_=None, breedPlace2_=None, saleNum_=None,
                                                  intentionPrice_=None, saleTime_=None,
                                                  saleProvince_=None, saleCity_=None, saleCounty_=None)
        sql_friend = self.vr.query_friend_info_by_user_id(user_id=self.user_id)
        if response['status'] == 'OK':
            self.assertEqual(sql_friend[0]['regular_source'], regular_source)
            self.assertEqual(int(sql_friend[0]['label_type']), label_type)
            self.assertEqual(sql_friend[0]['keeper_name'], keeper_name)
            self.assertEqual(sql_friend[0]['contact_number'], contact_number)
            self.assertEqual(sql_friend[0]['gender'], gender)
            self.assertEqual(sql_friend[0]['seniority'], seniority)
            self.assertEqual(sql_friend[0]['age'], age)
        else:
            self.log.info('运行错误提示，请查看日志')

    def test_admin_swarm_edit(self):
        """
        POST admin/swarm/edit V 2.1.0 new
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
        self.ba._admin_swarm_edit(id_=swarm_id, curNectarType_=curNectarType, vehicleLength_=vehicleLength,
                                  expectHiveNum_=expectHiveNum, pics_=img, scale_=scale)

    def test_admin_bee_friend_detail(self):
        """
        POST /admin/bee-friend/detail  V 2.1.0 Update
        蜂友详情
        :return:
        """
        user_info_list = self.ps.query_user_info()
        friend_id = random.choice(user_info_list).get('id')
        self.ba._admin_bee_friend_detail(id_=friend_id, lng_=None, lat_=None)

    def test_admin_swarm_detail(self):
        """
        POST admin/swarm/detail V 2.1.0 New
        蜂场详情
        :return:
        """
        swarm_list = self.vr.query_swarm_detail()
        swarm_id = random.choice(swarm_list).get('id')
        self.ba._admin_swarm_detail(id_=swarm_id)

    def test_admin_swarm_get_by_friend(self):
        """
        POST admin/swarm/get-by-friend V 2.1.0 New
        根据蜂友id获取蜂场列表
        :return:
        """
        friend_info = self.vr.query_friend_info_by_user_id(self.user_id)
        friend_id = (random.choice(friend_info)).get('id')
        self.ba._admin_swarm_get_by_friend(friendId_=friend_id)

    def test_admin_bee_friend_count(self):
        """
        POST /admin/bee-friend/count  V 1.0
        蜂友统计
        :return:
        """
        self.ba._admin_bee_friend_count()

    def test_admin_bee_friend_mobile_check(self):
        """
        POST /admin/bee-friend/mobile-check  V 1.0
        校验手机号重复性
        :return:
        """
        user_info_list = self.ps.query_user_info_by_phone(phone=self.mobile)
        user_id = user_info_list[0]['id']
        self.ba._admin_bee_friend_mobile_check(userId_=user_id, mobile_='19982917912')

    def test_admin_bee_friend_page_list(self):
        """
        POST /admin/bee-friend/page-list  V 2.0.1 Update
        蜂友分页列表
        :return:
        """
        vehicle_length_list = self.vr.query_vehicle_length()
        vehicle_length = (random.choice(list(vehicle_length_list))).get('key')
        curNectarType_list = self.vr.query_regular_source()
        curNectarType = (random.choice(list(curNectarType_list))).get('key')
        business_labels = random.randint(1001, 1006)
        response = self.ba._admin_bee_friend_page_list(businessLabels_=1002, pn_=1,
                                                       registed_=1, showStaff_=1)

    def test_admin_contract_page_list(self):
        """
        POST /admin/contract/page-list  V 1.0
        合同分页列表
        :return:
        """
        user_info_list = self.ps.query_user_info_by_phone(phone=self.mobile)
        user_id = user_info_list[0]['id']
        self.ba._admin_contract_page_list(pn_=1, ps_=10, userId_=user_id)

    def test_admin_shunt_list(self):
        """
        POST /admin/shunt/list  V 1.0
        调车列表
        :return:
        """
        user_info_list = self.ps.query_user_info_by_phone(phone=self.mobile)
        user_id = user_info_list[0]['id']
        self.ba._admin_shunt_list(pn_=1, ps_=10, userId_=user_id)

    def test_admin_excel_export_bee_friend(self):
        """
        GET /admin/excel-export/bee-friend  V1.0
        蜂友列表导出
        :return:
        """
        response = self.ba._admin_excel_export_bee_friend()
        f = open('蜂友信息导出_20200321.xlxs', 'wb+')
        f.write(response)
        f.close()

    def test_admin_workbench_bee_friend_add_check(self):
        """
        v2.1.0 new  POST /admin/workbench-bee-friend/add-check 新增蜂友手机号校验
        """
        mobile = '15200000000'
        response = self.ba._admin_bee_friend_add_check(userId_=None, mobile_=mobile)
        self.assertEqual(response['status'], "OK")

    def test_admin_swarm_page_list(self):
        """
        v2.2.0 new  POST /admin/swarm/page-list 蜂场分页列表
        :return:
        """
        response = self.ba._admin_swarm_page_list()
        self.assertEqual(response['status'], "OK")

    def test_admin_swarm_count(self):
        """
        v2.2.0 new  POST /admin/swarm/count 蜂场统计
        :return:
        """
        response = self.ba._admin_swarm_count()
        self.assertEqual(response['status'], "OK")



