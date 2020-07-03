"""
@Time: 2020 2020/6/16
员工轨迹
"""
import json
import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.fake.FakeLocation import FakeLocation
from testcase.flowerChaser.sql.Bee import StaffSql
from utils.log import log
from faker import Faker
from random import choice
from utils.dataConversion.dataConversion import DataConversion
import datetime, time
import random
import json


class StaffTrailMain(unittest.TestCase, FakeLocation, DataConversion):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    staff_trail = BeeAction()
    fl = FakeLocation()
    ss = StaffSql()
    fake = Faker(locale="zh_CN")
    staff_trail.set_user('15200000003')

    def test_mobile_fc_user_update_location(self):
        """
        POST /mobile/fc-user/update-location 更新当前登录用户位置
        v2.2.1 update
        :return:
        """
        province, city, county, address, lng, lat = self.fl.fake_location()
        response = self.staff_trail._mobile_fc_user_update_location(province_=province, city_=city, county_=county,
                                                                    address_=address, lng_=lng, lat_=lat)
        self.assertEqual("OK", response["status"])

    def test_admin_staff_trail_staff_count(self):
        """
        POST /admin/staff-trail/staff-count 定位员工数量统计
        v2.2.1 new
        :return:
        """
        response = self.staff_trail._admin_staff_trail_staff_count()
        staff_nums = self.ss.sql_staff_number()
        staff_num = len(staff_nums)
        self.assertEqual(staff_num, response["content"]["total"])

    def test_admin_staff_trail_latest_list(self):
        """
        POST /admin/staff-trail/latest-list 员工最近定位-分页列表
        v2.2.1 new
        :return:
        """
        response = self.staff_trail._admin_staff_trail_latest_list()
        self.assertEqual("OK", response["status"])

    def test_admin_staff_trail_detail_list(self):
        """
        POST /admin/staff-trail/detail-list 指定员工定位列表
        v2.2.1 new
        :return:
        """
        user_id = 610
        response = self.staff_trail._admin_staff_trail_detail_list(userId_=user_id)
        self.assertEqual("OK", response["status"])

