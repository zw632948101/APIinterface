#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2020 2020/2/28 16:37
__author__: wei.zhang
客户管理，新增编辑客户资料，编辑蜂农资料
2020/03/30 工作台
"""

import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.fake.FakeLocation import FakeLocation
from utils.log import log
from testcase.flowerChaser.sql.Bee import ClinteleSql
from testcase.flowerChaser.sql.Bee import VisitRecordSql
from faker import Faker
from random import choice
from utils.dataConversion.dataConversion import DataConversion
import datetime, time
import random


class CommentrMain(unittest.TestCase, ClinteleSql, FakeLocation, DataConversion):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    comment = BeeAction()
    config_db_v = VisitRecordSql()
    fake = Faker(locale="zh_CN")
    comment.set_user('yaxin.guan@worldfarm.com', '123456')

    def test_mobile_bee_friend_add(self):
        """
        移动端-客户资料-新建客户资料和蜂群信息
        1.2.1 修改 新增蜂农
        :return:
        """
        start_date = datetime.datetime(year=2019, month=1, day=1)
        end_data = datetime.datetime(year=2020, month=2, day=26)
        province_id, city_id, county, address, lng, lat = self.fake_location()  # 省市区详细地址，经纬度 必填
        keeperName = self.fake.name()  # 姓名-必填
        contactNumber = self.fake.phone_number()  # 联系电话 必填
        saleIntention = choice([1, 2, 3])  # 卖蜂意向必填
        saleNum = self.fake.random_int(min=1, max=999999)  # 可出售数量 非必填
        nativeCounty = county  # 户籍地址 非必填
        age = self.fake.random_int(min=20, max=70)  # 年龄
        seniority = self.fake.random_int(min=1, max=99)  # 养蜂年限
        regularRoute = '成都，重庆，贵阳'  # 常跑路线
        scale = choice([1, 2, 3, 4])  # 养殖规模 必填
        willingness = choice([1, 2, 3])  # 入职意愿 必填
        colony = choice([1, 2, 3])  # 蜂群群式 必填
        mite = choice([1, 2, 3, 4])  # 蜂螨必填
        chalkbrood = choice([1, 2, 3, 4])  # 白垩病必填
        poisoning = choice([1, 2, 3, 4])  # 中毒 必填
        hiveNum = self.fake.random_int(min=1, max=99999)  # 蜂箱总数必填
        standardNum = self.fake.random_int(min=1, max=99999)  # 标箱总数
        smallNum = self.fake.random_int(min=1, max=99999)  # 小箱数
        babySpleenNum = self.fake.random_int(min=1, max=99999)  # 子脾平均数
        honeySpleenNum = self.fake.random_int(min=1, max=99999)  # 蜜脾平均数
        doubleKingsNum = self.fake.random_int(min=1, max=99999)  # 双王箱数
        singleKingNum = self.fake.random_int(min=1, max=99999)  # 单王箱数
        nectar = choice([1, 2, 3])  # 储蜜情况
        pollen = choice([1, 2, 3])  # 储粉情况
        recentNectarSource = '成都市高新区天府大道'  # 最近采集蜜源地
        recentGatherTime = self.fake.date_time_between(start_date=start_date, end_date=end_data)  # 最近采集时间
        recentGatherTime = int(recentGatherTime.timestamp() * 1000)
        recentMiteTime = self.fake.date_time_between(start_date=start_date, end_date=end_data)  # 最近治螨时间
        recentMiteTime = int(recentMiteTime.timestamp() * 1000)
        miteTreatType = choice([1, 2, 3, 4])  # 最近治螨形式
        queenType = choice([1, 2])  # 蜂王类型
        propagationTime = self.fake.date_time_between(start_date=start_date, end_date=end_data)  # 春繁时间
        propagationTime = int(propagationTime.timestamp() * 1000)
        propagationPlace = '成都市高新区天府大道'  # 春繁地点
        brokenSonTime = self.fake.date_time_between(start_date=start_date, end_date=end_data)  # 断子时间
        brokenSonTime = int(brokenSonTime.timestamp() * 1000)
        inifo = self.comment._mobile_bee_friend_add(keeperName_=keeperName, contactNumber_=contactNumber,
                                                    province_=province_id, city_=city_id, county_=county,
                                                    address_=address, lng_=lng, lat_=lat, saleIntention_=saleIntention,
                                                    saleNum_=saleNum, nativeProvince_=province_id, nativeCity_=city_id,
                                                    nativeCounty_=nativeCounty, age_=age, seniority_=seniority,
                                                    regularRoute_=regularRoute, scale_=scale,
                                                    willingness_=willingness, colony_=colony, mite_=mite,
                                                    chalkbrood_=chalkbrood, poisoning_=poisoning, hiveNum_=hiveNum,
                                                    standardNum_=standardNum, smallNum_=smallNum,
                                                    babySpleenNum_=babySpleenNum, honeySpleenNum_=honeySpleenNum,
                                                    doubleKingsNum_=doubleKingsNum, singleKingNum_=singleKingNum,
                                                    nectar_=nectar, pollen_=pollen,
                                                    recentNectarSource_=recentNectarSource,
                                                    recentGatherTime_=recentGatherTime, recentMiteTime_=recentMiteTime,
                                                    miteTreatType_=miteTreatType, queenType_=queenType,
                                                    propagationTime_=propagationTime,
                                                    propagationPlace_=propagationPlace,
                                                    brokenSonTime_=brokenSonTime)
        self.assertEqual(inifo.get("status"), 'OK')
        customer = self.query_customer_and_swarm_info(phone=contactNumber)
        self.assertEqual(province_id, customer.get('province'))
        self.assertEqual(city_id, str(customer.get('city')))
        self.assertEqual(county, customer.get('county'))
        self.assertEqual(address, customer.get('address'))
        self.assertEqual(keeperName, customer.get('keeper_name'))
        self.assertEqual(contactNumber, customer.get('contact_number'))
        self.assertEqual(age, customer.get('age'))
        self.assertEqual(saleNum, customer.get('sale_num'))
        self.assertEqual(nativeCounty, customer.get('native_county'))
        self.assertEqual(province_id, customer.get('native_province'))
        self.assertEqual(city_id, str(customer.get('native_city')))
        self.assertEqual(seniority, customer.get('seniority'))
        self.assertEqual(regularRoute, customer.get('regular_route'))
        self.assertEqual(scale, customer.get('scale'))
        self.assertEqual(willingness, customer.get('willingness'))
        self.assertEqual(colony, customer.get('colony'))
        self.assertEqual(mite, customer.get('mite'))
        self.assertEqual(chalkbrood, customer.get('chalkbrood'))
        self.assertEqual(poisoning, customer.get('poisoning'))
        self.assertEqual(hiveNum, customer.get('hive_num'))
        self.assertEqual(standardNum, customer.get('standard_num'))
        self.assertEqual(smallNum, customer.get('small_num'))
        self.assertEqual(babySpleenNum, customer.get('baby_spleen_num'))
        self.assertEqual(honeySpleenNum, customer.get('honey_spleen_num'))
        self.assertEqual(doubleKingsNum, customer.get('double_kings_num'))
        self.assertEqual(singleKingNum, customer.get('single_king_num'))
        self.assertEqual(nectar, customer.get('nectar'))
        self.assertEqual(pollen, customer.get('pollen'))
        self.assertEqual(recentNectarSource, customer.get('recent_nectar_source'))
        self.assertEqual(miteTreatType, customer.get('mite_treat_type'))
        self.assertEqual(queenType, customer.get('queen_type'))
        self.assertEqual(propagationPlace, customer.get('propagation_place'))

        recentGatherTime = time.strftime("%Y-%m-%d", time.localtime(recentGatherTime / 1000))
        self.assertEqual(recentGatherTime, customer.get('recent_gather_time'))

        recentMiteTime = time.strftime("%Y-%m-%d", time.localtime(recentMiteTime / 1000))
        self.assertEqual(recentMiteTime, customer.get('recent_mite_time'))

        propagationTime = time.strftime("%Y-%m-%d", time.localtime(propagationTime / 1000))
        self.assertEqual(propagationTime, customer.get('propagation_time'))

        brokenSonTime = time.strftime("%Y-%m-%d", time.localtime(brokenSonTime / 1000))
        self.assertEqual(brokenSonTime, customer.get('broken_son_time'))

    def test_mobile_customer_add_bee_cule(self):
        """
        移动端-客户资料-以卖蜂线索手机号新建客户资料和蜂群信息
        1.2.1 修改 新增蜂农
        :return:
        """
        start_date = datetime.datetime(year=2019, month=1, day=1)
        end_data = datetime.datetime(year=2020, month=2, day=26)
        clueinfo = self.query_all_bee_clue_info()
        if clueinfo:
            clue = choice(clueinfo)
        else:
            log("当前系统中暂无卖蜂线索")
            return
        province_id, city_id, county, address, lng, lat = self.fake_location()
        keeperName = self.fake.name()
        contactNumber = clue.get('contact_number')
        saleIntention = choice([1, 2, 3])
        saleNum = self.fake.random_int(min=1, max=99999)
        nativeCounty = county
        age = self.fake.random_int(min=20, max=70)
        seniority = self.fake.random_int(min=1, max=99)
        regularRoute = '成都，重庆，贵阳'
        scale = choice([1, 2, 3, 4])
        willingness = choice([1, 2, 3])
        colony = choice([1, 2, 3])
        mite = choice([1, 2, 3, 4])
        chalkbrood = choice([1, 2, 3, 4])
        poisoning = choice([1, 2, 3, 4])
        hiveNum = self.fake.random_int(min=1, max=99999)
        standardNum = self.fake.random_int(min=1, max=99999)
        smallNum = self.fake.random_int(min=1, max=99999)
        babySpleenNum = self.fake.random_int(min=1, max=99999)
        honeySpleenNum = self.fake.random_int(min=1, max=99999)
        doubleKingsNum = self.fake.random_int(min=1, max=99999)
        singleKingNum = self.fake.random_int(min=1, max=99999)
        nectar = choice([1, 2, 3])
        pollen = choice([1, 2, 3])
        recentNectarSource = '成都市高新区天府大道'
        recentGatherTime = self.fake.date_time_between(start_date=start_date, end_date=end_data)
        recentGatherTime = int(recentGatherTime.timestamp() * 1000)
        recentMiteTime = self.fake.date_time_between(start_date=start_date, end_date=end_data)
        recentMiteTime = int(recentMiteTime.timestamp() * 1000)
        miteTreatType = choice([1, 2, 3, 4])
        queenType = choice([1, 2])
        propagationTime = self.fake.date_time_between(start_date=start_date, end_date=end_data)
        propagationTime = int(propagationTime.timestamp() * 1000)
        propagationPlace = '成都市高新区天府大道'
        brokenSonTime = self.fake.date_time_between(start_date=start_date, end_date=end_data)
        brokenSonTime = int(brokenSonTime.timestamp() * 1000)
        inifo = self.comment._mobile_bee_friend_add(keeperName_=keeperName, contactNumber_=contactNumber,
                                                    province_=province_id, city_=city_id, county_=county,
                                                    address_=address, lng_=lng, lat_=lat, saleIntention_=saleIntention,
                                                    saleNum_=saleNum, nativeProvince_=province_id, nativeCity_=city_id,
                                                    nativeCounty_=nativeCounty, age_=age, seniority_=seniority,
                                                    regularRoute_=regularRoute, scale_=scale,
                                                    willingness_=willingness, colony_=colony, mite_=mite,
                                                    chalkbrood_=chalkbrood, poisoning_=poisoning, hiveNum_=hiveNum,
                                                    standardNum_=standardNum, smallNum_=smallNum,
                                                    babySpleenNum_=babySpleenNum, honeySpleenNum_=honeySpleenNum,
                                                    doubleKingsNum_=doubleKingsNum, singleKingNum_=singleKingNum,
                                                    nectar_=nectar, pollen_=pollen,
                                                    recentNectarSource_=recentNectarSource,
                                                    recentGatherTime_=recentGatherTime, recentMiteTime_=recentMiteTime,
                                                    miteTreatType_=miteTreatType, queenType_=queenType,
                                                    propagationTime_=propagationTime,
                                                    propagationPlace_=propagationPlace,
                                                    brokenSonTime_=brokenSonTime)
        self.assertEqual(inifo.get("status"), 'OK')
        clue_isdelete = self.query_all_bee_clue_by_phone(phone=contactNumber).get('status')
        customer = self.query_customer_and_swarm_info(phone=contactNumber)
        self.assertEqual(clue_isdelete, 2)
        self.assertEqual(province_id, customer.get('province'))
        self.assertEqual(city_id, str(customer.get('city')))
        self.assertEqual(county, customer.get('county'))
        self.assertEqual(address, customer.get('address'))
        self.assertEqual(keeperName, customer.get('keeper_name'))
        self.assertEqual(contactNumber, customer.get('contact_number'))
        self.assertEqual(age, customer.get('age'))
        self.assertEqual(saleNum, customer.get('sale_num'))
        self.assertEqual(nativeCounty, customer.get('native_county'))
        self.assertEqual(province_id, customer.get('native_province'))
        self.assertEqual(city_id, str(customer.get('native_city')))
        self.assertEqual(seniority, customer.get('seniority'))
        self.assertEqual(regularRoute, customer.get('regular_route'))
        self.assertEqual(scale, customer.get('scale'))
        self.assertEqual(willingness, customer.get('willingness'))
        self.assertEqual(colony, customer.get('colony'))
        self.assertEqual(mite, customer.get('mite'))
        self.assertEqual(chalkbrood, customer.get('chalkbrood'))
        self.assertEqual(poisoning, customer.get('poisoning'))
        self.assertEqual(hiveNum, customer.get('hive_num'))
        self.assertEqual(standardNum, customer.get('standard_num'))
        self.assertEqual(smallNum, customer.get('small_num'))
        self.assertEqual(babySpleenNum, customer.get('baby_spleen_num'))
        self.assertEqual(honeySpleenNum, customer.get('honey_spleen_num'))
        self.assertEqual(doubleKingsNum, customer.get('double_kings_num'))
        self.assertEqual(singleKingNum, customer.get('single_king_num'))
        self.assertEqual(nectar, customer.get('nectar'))
        self.assertEqual(pollen, customer.get('pollen'))
        self.assertEqual(recentNectarSource, customer.get('recent_nectar_source'))
        self.assertEqual(miteTreatType, customer.get('mite_treat_type'))
        self.assertEqual(queenType, customer.get('queen_type'))
        self.assertEqual(propagationPlace, customer.get('propagation_place'))

        recentGatherTime = time.strftime("%Y-%m-%d", time.localtime(recentGatherTime / 1000))
        self.assertEqual(recentGatherTime, customer.get('recent_gather_time'))

        recentMiteTime = time.strftime("%Y-%m-%d", time.localtime(recentMiteTime / 1000))
        self.assertEqual(recentMiteTime, customer.get('recent_mite_time'))

        propagationTime = time.strftime("%Y-%m-%d", time.localtime(propagationTime / 1000))
        self.assertEqual(propagationTime, customer.get('propagation_time'))

        brokenSonTime = time.strftime("%Y-%m-%d", time.localtime(brokenSonTime / 1000))
        self.assertEqual(brokenSonTime, customer.get('broken_son_time'))

    def test_mobile_customer_edit(self):
        """
        移动端-客户资料-编辑客户资料
        1.2.1 修改 编辑蜂农资料
        :return:
        """
        contact_number = self.query_bee_friend_According_to_the_condition()
        customerid = ''
        if contact_number:
            customerid = choice(contact_number).get('id')
        else:
            log("系统中没有客户资料")

        province_id, city_id, county, address, lng, lat = self.fake_location()
        keeperName = self.fake.name()
        contactNumber = self.fake.phone_number()
        saleIntention = choice([1, 2, 3])
        saleNum = self.fake.random_int(min=1, max=99999)
        nativeCounty = county
        age = self.fake.random_int(min=20, max=70)
        seniority = self.fake.random_int(min=1, max=99)
        regularRoute = '成都，重庆，贵阳'
        scale = choice([1, 2, 3, 4])
        willingness = choice([1, 2, 3])
        info = self.comment._mobile_bee_friend_edit(keeperName_=keeperName, contactNumber_=contactNumber,
                                                    province_=province_id, city_=city_id, county_=county,
                                                    address_=address, lng_=lng, lat_=lat, saleIntention_=saleIntention,
                                                    saleNum_=saleNum, nativeProvince_=province_id, nativeCity_=city_id,
                                                    nativeCounty_=nativeCounty, age_=age, seniority_=seniority,
                                                    regularRoute_=regularRoute, scale_=scale,
                                                    willingness_=willingness, id_=customerid)
        self.assertEqual(info.get("status"), 'OK')
        customer = self.query_customer_and_swarm_info(phone=contactNumber)
        self.assertEqual(province_id, customer.get('province'))
        self.assertEqual(city_id, str(customer.get('city')))
        self.assertEqual(county, customer.get('county'))
        self.assertEqual(address, customer.get('address'))
        self.assertEqual(keeperName, customer.get('keeper_name'))
        self.assertEqual(contactNumber, customer.get('contact_number'))
        self.assertEqual(age, customer.get('age'))
        self.assertEqual(saleNum, customer.get('sale_num'))
        self.assertEqual(nativeCounty, customer.get('native_county'))
        self.assertEqual(province_id, customer.get('native_province'))
        self.assertEqual(city_id, str(customer.get('native_city')))
        self.assertEqual(seniority, customer.get('seniority'))
        self.assertEqual(regularRoute, customer.get('regular_route'))
        self.assertEqual(scale, customer.get('scale'))
        self.assertEqual(willingness, customer.get('willingness'))

    def test_mobile_customer_page_list(self):
        """
        移动端-客户资料-客户分页列表
        1.2.1 修改
        :return:
        """
        pn = 0
        ps = 20
        province_id, city_id, county, address, lng, lat = self.fake_location()

        contact_number = self.query_constomer_all_info()
        if contact_number:
            contactNumber = choice(contact_number).get('contact_number')
        else:
            contactNumber = None
        contactNumber = choice([None, contactNumber])
        cooperationIntentions = choice([None, 1, 2, (1, 2)])
        searchType = choice([1, 2])
        distanceType = choice([1, 2, 3, 4])
        if searchType == 1:
            distanceType = lng = lat = None

        else:
            province_id = city_id = county = None

        if contactNumber:
            province_id = city_id = county = lng = lat = searchType = distanceType = None
        contactNumber = None
        province_id = None
        city_id = None
        county = None
        lng = 101.01521129195828
        lat = 36.30153230942763
        searchType = 2
        distanceType = 3
        info = self.comment._mobile_bee_friend_page_list(pn_=pn, ps_=ps, contactNumber_=contactNumber,
                                                         cooperationIntentions_=cooperationIntentions,
                                                         searchType_=searchType, province_=province_id, city_=city_id,
                                                         county_=county, lng_=lng, lat_=lat, distanceType_=distanceType)
        self.assertEqual(info.get("status"), 'OK')
        customerdata = self.query_bee_friend_According_to_the_condition(pn=pn, ps=ps, phone=contactNumber,
                                                                        province_id=province_id, city_id=city_id,
                                                                        county=county, lng=lng, lat=lat,
                                                                        cooperationIntentions=cooperationIntentions,
                                                                        searchType=searchType,
                                                                        distanceType=distanceType)
        if info['content'].get('datas'):
            customerdata = self.del_dict_value_null(customerdata)
            customerapidata = info['content'].get('datas')
            customerapidata = self.del_dict_value_null(customerapidata)
            self.assertListEqual(customerapidata, customerdata)
            for i in range(len(customerapidata)):
                self.assertDictEqual(customerdata[i], customerapidata[i])

    def test_mobile_swarm_edit(self):
        """
        移动端-蜂群信息-蜂群信息编辑
        :return:
        """
        swarminfo = self.query_swarm_all_info()
        if swarminfo:
            sid = 15
        else:
            log("当前系统无蜂群信息")
            return
        start_date = datetime.datetime(year=2019, month=1, day=1)
        end_data = datetime.datetime(year=2020, month=2, day=26)
        colony = choice([1, 2, 3])
        mite = choice([1, 2, 3, 4])
        chalkbrood = choice([1, 2, 3, 4])
        poisoning = choice([1, 2, 3, 4])
        hiveNum = self.fake.random_int(min=1, max=99999)
        standardNum = self.fake.random_int(min=1, max=99999)
        smallNum = self.fake.random_int(min=1, max=99999)
        babySpleenNum = self.fake.random_int(min=1, max=99999)
        honeySpleenNum = self.fake.random_int(min=1, max=99999)
        doubleKingsNum = self.fake.random_int(min=1, max=99999)
        singleKingNum = self.fake.random_int(min=1, max=99999)
        nectar = choice([1, 2, 3])
        pollen = choice([1, 2, 3])
        recentNectarSource = '成都市高新区天府大道'
        recentGatherTime = self.fake.date_time_between(start_date=start_date, end_date=end_data)
        recentGatherTime = int(recentGatherTime.timestamp() * 1000)
        recentMiteTime = self.fake.date_time_between(start_date=start_date, end_date=end_data)
        recentMiteTime = int(recentMiteTime.timestamp() * 1000)
        miteTreatType = choice([1, 2, 3, 4])
        queenType = choice([1, 2])
        propagationTime = self.fake.date_time_between(start_date=start_date, end_date=end_data)
        propagationTime = int(propagationTime.timestamp() * 1000)
        propagationPlace = '成都市高新区天府大道'
        brokenSonTime = self.fake.date_time_between(start_date=start_date, end_date=end_data)
        brokenSonTime = int(brokenSonTime.timestamp() * 1000)
        info = self.comment._mobile_swarm_edit(id_=sid, colony_=colony, mite_=mite,
                                               chalkbrood_=chalkbrood, poisoning_=poisoning, hiveNum_=hiveNum,
                                               standardNum_=standardNum, smallNum_=smallNum,
                                               babySpleenNum_=babySpleenNum, honeySpleenNum_=honeySpleenNum,
                                               doubleKingsNum_=doubleKingsNum, singleKingNum_=singleKingNum,
                                               nectar_=nectar, pollen_=pollen,
                                               recentNectarSource_=recentNectarSource,
                                               recentGatherTime_=recentGatherTime, recentMiteTime_=recentMiteTime,
                                               miteTreatType_=miteTreatType, queenType_=queenType,
                                               propagationTime_=propagationTime, propagationPlace_=propagationPlace,
                                               brokenSonTime_=brokenSonTime)
        self.assertEqual(info.get("status"), 'OK')
        customer = self.query_swarm_all_info(sid=sid)
        self.assertEqual(colony, customer.get('colony'))
        self.assertEqual(mite, customer.get('mite'))
        self.assertEqual(chalkbrood, customer.get('chalkbrood'))
        self.assertEqual(poisoning, customer.get('poisoning'))
        self.assertEqual(hiveNum, customer.get('hive_num'))
        self.assertEqual(standardNum, customer.get('standard_num'))
        self.assertEqual(smallNum, customer.get('small_num'))
        self.assertEqual(babySpleenNum, customer.get('baby_spleen_num'))
        self.assertEqual(honeySpleenNum, customer.get('honey_spleen_num'))
        self.assertEqual(doubleKingsNum, customer.get('double_kings_num'))
        self.assertEqual(singleKingNum, customer.get('single_king_num'))
        self.assertEqual(nectar, customer.get('nectar'))
        self.assertEqual(pollen, customer.get('pollen'))
        self.assertEqual(recentNectarSource, customer.get('recent_nectar_source'))
        self.assertEqual(miteTreatType, customer.get('mite_treat_type'))
        self.assertEqual(queenType, customer.get('queen_type'))
        self.assertEqual(propagationPlace, customer.get('propagation_place'))

        recentGatherTime = time.strftime("%Y-%m-%d", time.localtime(recentGatherTime / 1000))
        self.assertEqual(recentGatherTime, customer.get('recent_gather_time'))

        recentMiteTime = time.strftime("%Y-%m-%d", time.localtime(recentMiteTime / 1000))
        self.assertEqual(recentMiteTime, customer.get('recent_mite_time'))

        propagationTime = time.strftime("%Y-%m-%d", time.localtime(propagationTime / 1000))
        self.assertEqual(propagationTime, customer.get('propagation_time'))

        brokenSonTime = time.strftime("%Y-%m-%d", time.localtime(brokenSonTime / 1000))
        self.assertEqual(brokenSonTime, customer.get('broken_son_time'))

    def test_mobile_bee_friend_detail(self):
        """
        POST /mobile/bee-friend/detail  蜂友详情  v1.2.1
        :return:
        """
        customer_list = self.config_db_v.sql_all_customer()
        if customer_list[0]["id"] is not None:
            num = random.randrange(0, len(customer_list))
            customer_id = customer_list[num]["id"]
            response = self.comment._mobile_bee_friend_detail(id_=customer_id)
            if response['status'] == "OK":
                bee_friend = self.config_db_v.sql_bee_friend_by_id(customer_id)[0]
                self.assertEqual(response['content']['address'], bee_friend['address'])
                self.assertEqual(response['content']['age'], bee_friend['age'])
                self.assertEqual(response['content']['city'], bee_friend['city'])
                self.assertEqual(response['content']['contactNumber'], bee_friend['contact_number'])
                self.assertEqual(response['content']['contactTime'], bee_friend['contact_time'])
                self.assertEqual(response['content']['county'], bee_friend['county'])
                self.assertEqual(response['content']['keeperName'], bee_friend['keeper_name'])
                self.assertEqual(response['content']['lat'], bee_friend['lat'])
                self.assertEqual(response['content']['lng'], bee_friend['lng'])
                self.assertEqual(response['content']['nativeCity'], bee_friend['native_city'])
                self.assertEqual(response['content']['nativeCounty'], bee_friend['native_county'])
                self.assertEqual(response['content']['nativeProvince'], bee_friend['native_province'])
                self.assertEqual(response['content']['province'], bee_friend['province'])
                self.assertEqual(response['content']['regularRoute'], bee_friend['regular_route'])
                self.assertEqual(response['content']['saleIntention'], bee_friend['sale_intention'])
                self.assertEqual(response['content']['saleNum'], bee_friend['sale_num'])
                self.assertEqual(response['content']['seniority'], bee_friend['seniority'])
                self.assertEqual(response['content']['willingness'], bee_friend['willingness'])
        else:
            self.assertTrue(False, "暂无客户")

    def test_mobile_bee_friend_add_contact_time(self):
        """
        POST /mobile/bee-friend/add-contact-time 增加联系次数 v1.2.1
        :return:
        """
        customer_list = self.config_db_v.sql_all_customer()
        if customer_list[0]["id"] is not None:
            num = random.randrange(0, len(customer_list))
            customer_id = customer_list[num]["id"]
            bee_friend = self.config_db_v.sql_bee_friend_by_id(customer_id)[0]
            contact_time_one = bee_friend["contact_time"]
            response = self.comment._mobile_bee_friend_add_contact_time(id_=customer_id)
            if response['status'] == "OK":
                bee_friend = self.config_db_v.sql_bee_friend_by_id(customer_id)[0]
                contact_time_two = bee_friend["contact_time"]
                contact_time_ones = contact_time_one+1
                self.assertEqual(contact_time_two, contact_time_ones)
        else:
            self.assertTrue(False, "暂无客户")

    def test_mobile_swarm_detail(self):
        """
        POST /mobile/swarm/detail 获取蜂群信息
        """
        swarm_list = self.config_db_v.sql_all_swarm_info()
        if swarm_list[0]["id"] is not None:
            num = random.randrange(0, len(swarm_list))
            cswarm_id = swarm_list[num]["id"]
            response = self.comment._mobile_swarm_detail(id_=cswarm_id)
            self.assertEqual(response['status'], "OK")
        else:
            self.assertTrue(False, "暂无客户")

    def test_mobile_swarm_get_by_customer(self):
        """
        POST /mobile/swarm/get-by-customer 根据客户id获取蜂群信息
        :return:
        """
        customer_list = self.config_db.sql_all_customer()
        if customer_list[0]["id"] is not None:
            num = random.randrange(0, len(customer_list))
            customer_id = customer_list[num]["id"]
            response = self.comment._mobile_swarm_get_by_customer(id_=customer_id)
            self.assertEqual(response['status'], "OK")
        else:
            self.assertTrue(False, "暂无客户")
