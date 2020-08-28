#! /usr/bin/env python3
# -*- coding: UTF-8 -*-


import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log import log
from faker import Faker
from testcase.flowerChaser.sql.Bee import NectarSourcePointSql, NectarSourceInformationSql
from utils.fake.FakeLocation import FakeLocation
import random
import json
from utils.dataConversion.dataConversion import DataConversion as dc

class NectarSourcePointMain(unittest.TestCase):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    nectar_source_point = BeeAction()
    nectar_source_db = NectarSourceInformationSql()
    nectar_source_point_db = NectarSourcePointSql()
    fl = FakeLocation()
    log.info("开始执行蜜源点管理测试用例")
    fake = Faker(locale="zh_CN")
    nectar_source_point.set_user('15200000003')

    def random_month(self):
        """
        随机生成月份
        :return:
        """
        one_number = random.randint(0, 1)
        two_number = None
        if one_number == 0:
            two_number = random.randint(1, 9)
        else:
            two_number = random.randint(0, 2)
        three_number = random.randint(1, 12)
        three_number_str = None
        if three_number < 10:
            three_number_str = "0" + str(three_number)
        else:
            three_number_str = str(three_number)
        random_month = str(one_number) + str(two_number) + three_number_str
        return random_month

    def random_code(self):
        """
        随机生成蜜源类型code
        :return:
        """
        db_type = self.nectar_source_db.sql_nectar_source_type()
        random_num = random.randint(0, len(db_type))
        plant_code = db_type[random_num]["code"]
        return plant_code

    def test_admin_nectar_source_point_add(self):
        """
        POST /admin/nectar-source-point/add 新增蜜源点
        v2.3.0新增
        :return:
        """
        province, city, county, address, lng, lat = self.fl.fake_location()
        plant_code = self.random_code()
        flowering_start_date = self.random_month()
        nectar_flow = self.random_month()
        nectar_source_area = self.fake.pyfloat(left_digits=random.randint(1, 8), right_digits=2, positive=True)
        apiary_density = self.fake.random_int(min=1, max=6)
        entry_date = self.random_month()
        departure_date = self.random_month()
        purpose = random.randint(1, 4)
        db_type = self.nectar_source_db.sql_random_nectar_source_type(random.randint(1, 5))
        type_list = dc.data_assemble('code', db_type)
        type_lists = []
        for i in range(len(type_list)):
            type_lists.append(str(type_list[i]))
        second_plant_code = ",".join(type_lists)
        pesticide_condition = self.fake.text(max_nb_chars=50)
        main_intensively = self.fake.text(max_nb_chars=50)
        remark = self.fake.text(max_nb_chars=200)
        province_n, city_n, county_n, address_n, lng_n, lat_n = self.fl.fake_location()
        province_s, city_s, county_s, address_s, lng_s, lat_s = self.fl.fake_location()
        nectar_source_flow_inputs = [{"province": province_n, "city": city_n, "county": county_n,
                                      "plantCode": self.random_code(), "infoType": 1},
                                     {"province": province_s, "city": city_s, "county": county_s,
                                      "plantCode": self.random_code(), "infoType": 2}]
        nectar_source_flow_inputs = json.dumps(nectar_source_flow_inputs, ensure_ascii=False)
        url = "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"
        nectar_source_point_attach_inputs = [{"url": url, "remark": self.fake.text(max_nb_chars=200)}]
        nectar_source_point_attach_inputs = json.dumps(nectar_source_point_attach_inputs, ensure_ascii=False)
        response = self.nectar_source_point._admin_nectar_source_point_add(province_=province, city_=city,
                                                                           county_=county, lng_=lng, lat_=lat,
                                                                           plantCode_=plant_code,
                                                                           floweringStartDate_=flowering_start_date,
                                                                           nectarFlow_=nectar_flow,
                                                                           nectarSourceArea_=nectar_source_area,
                                                                           apiaryDensity_=apiary_density,
                                                                           entryDate_=entry_date,
                                                                           departureDate_=departure_date,
                                                                           purpose_=purpose,
                                                                           secondPlantCode_=second_plant_code,
                                                                           pesticideCondition_=pesticide_condition,
                                                                           mainIntensively_=main_intensively,
                                                                           remark_=remark,
                                                                           nectarSourcePointAttachInputs_=nectar_source_point_attach_inputs,
                                                                           nectarSourceFlowInputs_=nectar_source_flow_inputs)
        self.assertEqual("OK", response['status'])

    def test_admin_nectar_source_point_edit(self):
        """
        POST /admin/nectar-source-point/add 编辑蜜源点
        v2.3.0新增
        :return:
        """
        nectar_source_point = self.nectar_source_point_db.query_nectar_source_point()
        if nectar_source_point[0]["id"] is not None:
            num = random.randrange(0, len(nectar_source_point))
            id = nectar_source_point[num]["id"]
            province, city, county, address, lng, lat = self.fl.fake_location()
            plant_code = self.random_code()
            flowering_start_date = self.random_month()
            nectar_flow = self.random_month()
            nectar_source_area = self.fake.pyfloat(left_digits=random.randint(1, 8), right_digits=2, positive=True)
            apiary_density = self.fake.random_int(min=1, max=6)
            entry_date = self.random_month()
            departure_date = self.random_month()
            purpose = random.randint(1, 4)
            db_type = self.nectar_source_db.sql_random_nectar_source_type(random.randint(1, 5))
            type_list = dc.data_assemble('code', db_type)
            type_lists = []
            for i in range(len(type_list)):
                type_lists.append(str(type_list[i]))
            second_plant_code = ",".join(type_lists)
            pesticide_condition = self.fake.text(max_nb_chars=50)
            main_intensively = self.fake.text(max_nb_chars=50)
            remark = self.fake.text(max_nb_chars=200)
            province_n, city_n, county_n, address_n, lng_n, lat_n = self.fl.fake_location()
            province_s, city_s, county_s, address_s, lng_s, lat_s = self.fl.fake_location()
            nectar_source_flow_inputs = [{"province": province_n, "city": city_n, "county": county_n,
                                          "plantCode": self.random_code(), "infoType": 1},
                                         {"province": province_s, "city": city_s, "county": county_s,
                                          "plantCode": self.random_code(), "infoType": 2}]
            nectar_source_flow_inputs = json.dumps(nectar_source_flow_inputs, ensure_ascii=False)
            url = "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1592186565033.jpg"
            nectar_source_point_attach_inputs = [{"url": url, "remark": self.fake.text(max_nb_chars=200)}]
            nectar_source_point_attach_inputs = json.dumps(nectar_source_point_attach_inputs, ensure_ascii=False)
            response = self.nectar_source_point._admin_nectar_source_point_edit(id_=id,
                                                                                province_=province, city_=city,
                                                                                county_=county, lng_=lng, lat_=lat,
                                                                                plantCode_=plant_code,
                                                                                floweringStartDate_=flowering_start_date,
                                                                                nectarFlow_=nectar_flow,
                                                                                nectarSourceArea_=nectar_source_area,
                                                                                apiaryDensity_=apiary_density,
                                                                                entryDate_=entry_date,
                                                                                departureDate_=departure_date,
                                                                                purpose_=purpose,
                                                                                secondPlantCode_=second_plant_code,
                                                                                pesticideCondition_=pesticide_condition,
                                                                                mainIntensively_=main_intensively,
                                                                                remark_=remark,
                                                                                nectarSourcePointAttachInputs_=nectar_source_point_attach_inputs,
                                                                                nectarSourceFlowInputs_=nectar_source_flow_inputs)
            self.assertEqual("OK", response['status'])
        else:
            self.assertTrue(False, "暂无蜜源点")

    def test_admin_nectar_source_point_del(self):
        """
        POST /admin/nectar-source-point/del 蜜源点删除
        v2.3.0新增
        :return:
        """
        nectar_source_point = self.nectar_source_point_db.query_nectar_source_point()
        if nectar_source_point[0]["id"] is not None:
            num = random.randrange(0, len(nectar_source_point))
            id = nectar_source_point[num]["id"]
            response = self.nectar_source_point._admin_nectar_source_point_del(id_=id)
            self.assertEqual("OK", response['status'])
        else:
            self.assertTrue(False, "暂无蜜源点")

    def test_admin_nectar_source_point_attach_del(self):
        """
        POST /admin/nectar-source-point/attach/del 蜜源点附件删除
        v2.3.0新增
        :return:
        """
        nectar_source_point_attach = self.nectar_source_point_db.query_nectar_source_point_attach()
        if nectar_source_point_attach[0]["id"] is not None:
            num = random.randrange(0, len(nectar_source_point_attach))
            id = nectar_source_point_attach[num]["id"]
            point_id = nectar_source_point_attach[num]["point_id"]
            attach = self.nectar_source_point_db.query_nectar_source_point_attach_by_point_id(point_id)
            response = self.nectar_source_point._admin_nectar_source_point_del(id_=id)
            if len(attach) == 1:
                self.assertEqual("只有一张图片不允许删除", response['errorMsg'])
            else:
                self.assertEqual("OK", response['status'])


    def test_admin_nectar_source_point_attach_list(self):
        """
        POST /admin/nectar-source-point/attach/list 蜜源点附件列表
        v2.3.0新增
        :return:
        """
        nectar_source_point = self.nectar_source_point_db.query_nectar_source_point()
        if nectar_source_point[0]["id"] is not None:
            num = random.randrange(0, len(nectar_source_point))
            id = nectar_source_point[num]["id"]
            response = self.nectar_source_point._admin_nectar_source_point_attach_list(id_=id)
            self.assertEqual("OK", response['status'])
        else:
            self.assertTrue(False, "暂无蜜源点")

    def test_admin_nectar_source_point_detail(self):
        """
        POST /admin/nectar-source-point/detail 蜜源点详情
        v2.3.0新增
        :return:
        """
        nectar_source_point = self.nectar_source_point_db.query_nectar_source_point()
        if nectar_source_point[0]["id"] is not None:
            num = random.randrange(0, len(nectar_source_point))
            id = nectar_source_point[num]["id"]
            response = self.nectar_source_point._admin_nectar_source_point_detail(id_=id)
            self.assertEqual("OK", response['status'])
        else:
            self.assertTrue(False, "暂无蜜源点")

    def test_admin_nectar_source_point_list(self):
        """
        POST /admin/nectar-source-point/list 蜜源点列表
        v2.3.0新增
        :return:
        """
        response = self.nectar_source_point._admin_nectar_source_point_list()
        self.assertEqual("OK", response['status'])


