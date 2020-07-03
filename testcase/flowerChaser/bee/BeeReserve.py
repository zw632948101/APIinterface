"""
@Time: 2020 2020/6/16
中蜂保护区管理
"""
import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.fake.FakeLocation import FakeLocation
from utils.log.logger import logger
from testcase.flowerChaser.sql.Bee import BeeReserveInformationSql
from faker import Faker
from utils.dataConversion.dataConversion import DataConversion
import random
import json


class BeeReserveMain(unittest.TestCase, FakeLocation, DataConversion):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    bee_reserve = BeeAction()
    br = BeeReserveInformationSql()
    fl = FakeLocation()
    log = logger('BeeReserveMain').logger
    fake = Faker(locale="zh_CN")
    bee_reserve.set_user('15200000003')

    def test_mobile_bee_reserve_add(self):
        """
        POST /mobile/bee-reserve/add 采集中蜂保护区
        v2.2.1 new
        :return:
        """
        reserve_name = self.fake.text(max_nb_chars=20)
        province, city, county, address, lng, lat = self.fl.fake_location()
        nectar_type = random.sample(range(1001, 1047), 3)
        vehicle_length = random.randint(1001, 1018)
        reserve_area = self.fake.random_int(min=1, max=99999999)
        altitude = 1654
        manager = self.fake.name()
        contact = self.fake.phone_number()
        remark = self.fake.text(max_nb_chars=200)
        attaches = [{"bizType": 1,
                     "url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252271444.jpg"},
                    {"bizType": 2,
                     "url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252272949.jpg"},
                    {"bizType": 3,
                     "url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252276148.jpg"},
                    {"bizType": 4,
                     "url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252276812.jpg"}]
        attaches = json.dumps(attaches, ensure_ascii=False)
        response = self.bee_reserve._mobile_bee_reserve_add(reserveName_=reserve_name, address_=address, lng_=lng,
                                                            lat_=lat,
                                                            province_=province, city_=city, county_=county,
                                                            addrProvince_=province,
                                                            addrCity_=city, addrCounty_=county,
                                                            nectarType_=nectar_type,
                                                            vehicleLength_=vehicle_length, reserveArea_=reserve_area,
                                                            altitude_=altitude,
                                                            manager_=manager, contact_=contact, remark_=remark,
                                                            attaches_=attaches)
        self.assertEqual("OK", response["status"])

    def test_mobile_bee_reserve_page_list(self):
        """
        POST /mobile/bee-reserve/page-list 分页列表
        v2.2.1 new
        :return:
        """
        response = self.bee_reserve._mobile_bee_reserve_page_list()
        self.assertEqual("OK", response["status"])

    def test_mobile_bee_reserve_edit(self):
        """
        POST /mobile/bee-reserve/edit 编辑中蜂保护区
        v2.2.1 new
        :return:
        """
        bee_reserve = self.br.sql_bee_reserve()
        if bee_reserve[0]["id"] is not None:
            num = random.randrange(0, len(bee_reserve))
            bee_reserve_id = bee_reserve[num]["id"]
            reserve_name = self.fake.text(max_nb_chars=20)
            province, city, county, address, lng, lat = self.fl.fake_location()
            nectar_type = random.sample(range(1001, 1047), 3)
            vehicle_length = random.randint(1001, 1018)
            reserve_area = self.fake.random_int(min=1, max=99999999)
            altitude = 1654
            manager = self.fake.name()
            contact = self.fake.phone_number()
            remark = self.fake.text(max_nb_chars=200)
            attaches = [{"bizType": 1,
                         "url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252271444.jpg"},
                        {"bizType": 2,
                         "url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252272949.jpg"},
                        {"bizType": 3,
                         "url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252276148.jpg"},
                        {"bizType": 4,
                         "url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252276812.jpg"}]
            attaches = json.dumps(attaches, ensure_ascii=False)
            response = self.bee_reserve._mobile_bee_reserve_edit(id_=bee_reserve_id, reserveName_=reserve_name,
                                                                 address_=address, lng_=lng, lat_=lat,
                                                                 province_=province, city_=city, county_=county,
                                                                 addrProvince_=province,
                                                                 addrCity_=city, addrCounty_=county,
                                                                 nectarType_=nectar_type,
                                                                 vehicleLength_=vehicle_length,
                                                                 reserveArea_=reserve_area,
                                                                 altitude_=altitude,
                                                                 manager_=manager, contact_=contact, remark_=remark,
                                                                 attaches_=attaches)
            self.assertEqual("OK", response["status"])
        else:
            self.assertTrue(False, "暂无中蜂保护区")

    def test_mobile_bee_reserve_detail(self):
        """
        POST /mobile/bee-reserve/detail 详情查看
        v2.2.1 new
        :return:
        """
        bee_reserve = self.br.sql_bee_reserve()
        if bee_reserve[0]["id"] is not None:
            num = random.randrange(0, len(bee_reserve))
            bee_reserve_id = bee_reserve[num]["id"]
            response = self.bee_reserve._mobile_bee_reserve_detail(id_=bee_reserve_id)
            self.assertEqual("OK", response["status"])
        else:
            self.assertTrue(False, "暂无中蜂保护区")

    def test_admin_bee_reserve_add(self):
        """
        POST /admin/bee-reserve/add 采集中蜂保护区
        v2.2.1 new
        :return:
        """
        reserve_name = self.fake.text(max_nb_chars=20)
        province, city, county, address, lng, lat = self.fl.fake_location()
        nectar_type = random.sample(range(1001, 1047), 3)
        vehicle_length = random.randint(1001, 1018)
        reserve_area = self.fake.random_int(min=1, max=99999999)
        manager = self.fake.name()
        contact = self.fake.phone_number()
        remark = self.fake.text(max_nb_chars=200)
        attaches = [{"bizType": 1,
                     "url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252271444.jpg"},
                    {"bizType": 2,
                     "url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252272949.jpg"},
                    {"bizType": 3,
                     "url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252276148.jpg"},
                    {"bizType": 4,
                     "url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252276812.jpg"}]
        attaches = json.dumps(attaches, ensure_ascii=False)
        response = self.bee_reserve._admin_bee_reserve_add(reserveName_=reserve_name, address_=address, lng_=lng,
                                                           lat_=lat,
                                                           province_=province, city_=city, county_=county,
                                                           addrProvince_=province,
                                                           addrCity_=city, addrCounty_=county,
                                                           nectarType_=nectar_type,
                                                           vehicleLength_=vehicle_length, reserveArea_=reserve_area,
                                                           altitude_=None,
                                                           manager_=manager, contact_=contact, remark_=remark,
                                                           attaches_=attaches)
        self.assertEqual("OK", response["status"])

    def test_admin_bee_reserve_edit(self):
        """
        POST /admin/bee-reserve/edit 编辑中蜂保护区
        v2.2.1 new
        :return:
        """
        bee_reserve = self.br.sql_bee_reserve()
        if bee_reserve[0]["id"] is not None:
            num = random.randrange(0, len(bee_reserve))
            bee_reserve_id = bee_reserve[num]["id"]
            reserve_name = self.fake.text(max_nb_chars=20)
            province, city, county, address, lng, lat = self.fl.fake_location()
            nectar_type = random.sample(range(1001, 1047), 3)
            vehicle_length = random.randint(1001, 1018)
            reserve_area = self.fake.random_int(min=1, max=99999999)
            altitude = 1654
            manager = self.fake.name()
            contact = self.fake.phone_number()
            remark = self.fake.text(max_nb_chars=200)
            attaches = [{"bizType": 1,
                         "url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252271444.jpg"},
                        {"bizType": 2,
                         "url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252272949.jpg"},
                        {"bizType": 3,
                         "url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252276148.jpg"},
                        {"bizType": 4,
                         "url": "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1589252276812.jpg"}]
            attaches = json.dumps(attaches, ensure_ascii=False)
            response = self.bee_reserve._admin_bee_reserve_edit(id_=bee_reserve_id, reserveName_=reserve_name,
                                                                address_=address, lng_=lng, lat_=lat,
                                                                province_=province, city_=city, county_=county,
                                                                addrProvince_=province,
                                                                addrCity_=city, addrCounty_=county,
                                                                nectarType_=nectar_type,
                                                                vehicleLength_=vehicle_length,
                                                                reserveArea_=reserve_area,
                                                                altitude_=altitude,
                                                                manager_=manager, contact_=contact, remark_=remark,
                                                                attaches_=attaches)
            self.assertEqual("OK", response["status"])
        else:
            self.assertTrue(False, "暂无中蜂保护区")

    def test_admin_bee_reserve_page_list(self):
        """
        POST /admin/bee-reserve/page-list 分页列表
        v2.2.1 new
        :return:
        """
        pn = None
        ps = None
        reserve_name = "保护区"
        nectar_type = random.sample(range(1001, 1047), 3)
        creator = ""
        gatherTimeStart = ""
        gatherTimeEnd = ""
        province = ""
        city = ""
        county = ""
        response = self.bee_reserve._admin_bee_reserve_page_list()
        self.assertEqual("OK", response["status"])

    def test_admin_bee_reserve_detail(self):
        """
        POST /admin/bee-reserve/detail 详情查看
        v2.2.1 new
        :return:
        """
        bee_reserve = self.br.sql_bee_reserve()
        if bee_reserve[0]["id"] is not None:
            num = random.randrange(0, len(bee_reserve))
            bee_reserve_id = bee_reserve[num]["id"]
            response = self.bee_reserve._admin_bee_reserve_detail(id_=bee_reserve_id)
            self.assertEqual("OK", response["status"])
        else:
            self.assertTrue(False, "暂无中蜂保护区")

    def test_admin_bee_reserve_del(self):
        """
        POST /admin/bee-reserve/del 数据删除
        v2.2.1 new
        :return:
        """
        bee_reserve = self.br.sql_bee_reserve()
        if bee_reserve[0]["id"] is not None:
            num = random.randrange(0, len(bee_reserve))
            bee_reserve_id = bee_reserve[num]["id"]
            response = self.bee_reserve._admin_bee_reserve_del(id_=bee_reserve_id)
            self.assertEqual("OK", response["status"])
        else:
            self.assertTrue(False, "暂无中蜂保护区")

    def test_admin_bee_reserve_statistics(self):
        """
        POST /admin/bee-reserve/statistics 列表头统计
        v2.2.1 new
        :return:
        """
        response = self.bee_reserve._admin_bee_reserve_statistics()
        bee_reserve_num = self.br.sql_bee_reserve_count()[0]["保护区总数"]
        self.assertEqual(bee_reserve_num, response["content"]["totalNum"])

    def test_admin_excel_export_reserve(self):
        """
        GET /admin/excel-export/reserve 中锋保护区列表导出
        v2.2.1 new
        :return:
        """
        response = self.bee_reserve._admin_excel_export_reserve()
        f = open('保护区信息导出_20200617.xlsx', 'wb+')
        f.write(response)
        f.close()
