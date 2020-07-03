#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log.logger import logger
from testcase.flowerChaser.sql.Bee import BeeClueSql
from utils.fake.FakeLocation import FakeLocation
import random
from faker import Faker


class BeeClueMain(unittest.TestCase):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    beeclue = BeeAction()
    beeclue_db = BeeClueSql()
    log = logger('BeeClueMain').logger
    log.info("开始执行卖蜂线索管理接口测试用例")
    fake = Faker(locale="zh_CN")
    fl = FakeLocation()
    beeclue.set_user('yaxin.guan@worldfarm.com', '123456')

    def test_mobile_bee_clue_add(self):
        """
        接口地址：POST /mobile/bee-clue/add  添加卖蜂线索
        :return:
        """
        keeper_name = self.fake.name()
        contact_number = self.fake.phone_number()
        province_id, city_id, district_id, address, lng, lat = self.fl.fake_location()
        sale_num = self.fake.random_number(digits=6)
        spleen_num = self.fake.random_number(digits=6)
        intention_price = random.choice([-1, self.fake.random_number(digits=6) * 100])
        response = self.beeclue._mobile_bee_clue_add(keeperName_=keeper_name,
                                                     contactNumber_=contact_number,
                                                     province_=province_id,
                                                     city_=city_id,
                                                     county_=district_id,
                                                     address_=address,
                                                     lng_=lng,
                                                     lat_=lat,
                                                     saleNum_=sale_num,
                                                     spleenNum_=spleen_num,
                                                     intentionPrice_=intention_price)
        if response["status"] == "OK":
            clue = self.beeclue_db.sql_all_bee_clue()
            self.assertEqual(keeper_name, clue["keeper_name"])
            self.assertEqual(contact_number, clue["contact_number"])
            self.assertEqual(int(province_id), clue["province"])
            self.assertEqual(int(city_id), clue["city"])
            self.assertEqual(district_id, clue["county"])
            self.assertEqual(address, clue["address"])
            self.assertEqual(lng, clue["lng"])
            self.assertEqual(lat, clue["lat"])
            self.assertEqual(sale_num, clue["sale_num"])
            self.assertEqual(spleen_num, clue["spleen_num"])
            self.assertEqual(intention_price, clue["intention_price"])
        else:
            self.assertTrue(False, "卖蜂线索添加失败")

    def test_mobile_bee_clue_add_without_mobile(self):
        """
        接口地址：POST /mobile/bee-clue/add  添加卖蜂线索---不输入必填项联系电话
        :return:
        """
        response = self.beeclue._mobile_bee_clue_add(keeperName_="王良",
                                                     contactNumber_=None,
                                                     province_=22,
                                                     city_=22204,
                                                     county_=220407,
                                                     address_="河南省平顶山市叶县常村镇李九思村",
                                                     lng_=113.12762505432899,
                                                     lat_=33.485066502274464,
                                                     saleNum_=random.randint(0, 999999),
                                                     spleenNum_=random.randint(0, 999999),
                                                     intentionPrice_=random.randint(-1, 999999))
        self.assertEqual(response["errorMsg"], "联系电话不能为空")

    def test_mobile_bee_clue_add_with_error_mobile(self):
        """
        接口地址：POST /mobile/bee-clue/add  添加卖蜂线索---输入错误的联系电话
        :return:
        """
        response = self.beeclue._mobile_bee_clue_add(keeperName_="王良",
                                                     contactNumber_="25519546825",
                                                     province_=22,
                                                     city_=22204,
                                                     county_=220407,
                                                     address_="河南省平顶山市叶县常村镇李九思村",
                                                     lng_=113.12762505432899,
                                                     lat_=33.485066502274464,
                                                     saleNum_=random.randint(0, 999999),
                                                     spleenNum_=random.randint(0, 999999),
                                                     intentionPrice_=random.randint(-1, 999999))
        self.assertEqual("联系电话格式不正确", response["errorMsg"])

    def test_mobile_bee_clue_list(self):
        """
        接口地址：POST /mobile/bee-clue/list 卖蜂线索列表
        :return:
        """
        response = self.beeclue._mobile_bee_clue_list(pn_=1,
                                                      ps_=20,
                                                      mobile_=None)
        clue = self.beeclue_db.sql_bee_clue_order_by_contact()
        if response["status"] == "OK":
            if len(clue) == response["content"]["tc"]:
                for i in range(len(clue)):
                    if clue[i]["keeper_name"]:
                        self.assertEqual(response["content"]["datas"][i]["keeperName"], clue[i]["keeper_name"])
                    self.assertEqual(response["content"]["datas"][i]["contactNumber"], clue[i]["contact_number"])
                    if clue[i]["province"]:
                        self.assertEqual(response["content"]["datas"][i]["province"], clue[i]["province"])
                    if clue[i]["city"]:
                        self.assertEqual(response["content"]["datas"][i]["city"], clue[i]["city"])
                    if clue[i]["county"]:
                        self.assertEqual(response["content"]["datas"][i]["county"], clue[i]["county"])
                    if clue[i]["address"]:
                        self.assertEqual(response["content"]["datas"][i]["address"], clue[i]["address"])
                    if clue[i]["lng"]:
                        self.assertEqual(response["content"]["datas"][i]["lng"], clue[i]["lng"])
                    if clue[i]["lat"]:
                        self.assertEqual(response["content"]["datas"][i]["lat"], clue[i]["lat"])
                    if clue[i]["sale_num"]:
                        self.assertEqual(response["content"]["datas"][i]["saleNum"], clue[i]["sale_num"])
                    if clue[i]["spleen_num"]:
                        self.assertEqual(response["content"]["datas"][i]["spleenNum"], clue[i]["spleen_num"])
                    if clue[i]["intention_price"]:
                        self.assertEqual(response["content"]["datas"][i]["intentionPrice"], clue[i]["intention_price"])
            else:
                raise AssertionError("数据库未查询出数据")
        else:
            self.assertTrue(False, "卖蜂线索查询失败")

    def test_mobile_bee_clue_list_by_mobile(self):
        """
        接口地址：POST /mobile/bee-clue/list 卖蜂线索列表--手机号查询
        :return:
        """
        mobile = self.fake.phone_number()
        response = self.beeclue._mobile_bee_clue_list(pn_=1,
                                                      ps_=20,
                                                      mobile_=mobile)
        clue = self.beeclue_db.sql_bee_clue_by_mobile(mobile)
        if response["status"] == "OK":
            if len(clue) > 0:
                if clue[0]["keeper_name"]:
                    self.assertEqual(response["content"]["datas"]["keeperName"], clue[0]["keeper_name"])
                self.assertEqual(response["content"]["datas"]["contactNumber"], clue[0]["contact_number"])
                if clue[0]["province"]:
                    self.assertEqual(response["content"]["datas"]["province"], clue[0]["province"])
                if clue[0]["city"]:
                    self.assertEqual(response["content"]["datas"]["city"], clue[0]["city"])
                if clue[0]["county"]:
                    self.assertEqual(response["content"]["datas"]["county"], clue[0]["county"])
                if clue[0]["address"]:
                    self.assertEqual(response["content"]["datas"]["address"], clue[0]["address"])
                if clue[0]["lng"]:
                    self.assertEqual(response["content"]["datas"]["lng"], clue[0]["lng"])
                if clue[0]["lat"]:
                    self.assertEqual(response["content"]["datas"]["lat"], clue[0]["lat"])
                if clue[0]["sale_num"]:
                    self.assertEqual(response["content"]["datas"]["saleNum"], clue[0]["sale_num"])
                if clue[0]["spleen_num"]:
                    self.assertEqual(response["content"]["datas"]["spleenNum"], clue[0]["spleen_num"])
                if clue[0]["intention_price"]:
                    self.assertEqual(response["content"]["datas"]["intentionPrice"], clue[0]["intention_price"])
            else:
                self.assertEqual([], response["content"]["datas"])
        else:
            self.assertTrue(False, "卖蜂线索查询失败")

    def test_mobile_bee_clue_edit(self):
        """
        POST /mobile/bee-clue/edit 编辑卖蜂线索
        :return:
        """
        clue_list = self.beeclue._mobile_bee_clue_list()['content']['datas']
        contact_number = self.fake.phone_number()
        province_id, city_id, district_id, address, lng, lat = self.fl.fake_location()
        sale_num = self.fake.random_number(digits=6)
        spleen_num = self.fake.random_number(digits=6)
        intention_price = random.choice([-1, self.fake.random_number(digits=6) * 100])
        if len(clue_list) is not None:
            num = random.randrange(0, len(clue_list))
            clue_id = clue_list[num]["id"]
            response = self.beeclue._mobile_bee_clue_edit(id_=clue_id,
                                                          contactNumber_=contact_number,
                                                          province_=province_id,
                                                          city_=city_id,
                                                          county_=district_id,
                                                          address_=address,
                                                          lng_=lng,
                                                          lat_=lat,
                                                          saleNum_=sale_num,
                                                          spleenNum_=spleen_num,
                                                          intentionPrice_=intention_price)
            self.assertEqual(response["status"], "OK")

    def test_mobile_bee_clue_detail(self):
        """
        接口地址：POST /mobile/bee-clue/detail  卖蜂线索详情
        :return:
        """
        clue_list = self.beeclue._mobile_bee_clue_list()['content']['datas']
        if len(clue_list) is not None:
            num = random.randrange(0, len(clue_list))
            clue_id = clue_list[num]["id"]
            response = self.beeclue._mobile_bee_clue_detail(id_=clue_id)
            clue = self.beeclue_db.sql_bee_clue_detail(id=clue_id)
            if response["status"] == "OK":
                if len(clue) > 0:
                    if clue[0]["keeper_name"]:
                        self.assertEqual(response["content"]["keeperName"], clue[0]["keeper_name"])
                    self.assertEqual(response["content"]["contactNumber"], clue[0]["contact_number"])
                    if clue[0]["province"]:
                        self.assertEqual(response["content"]["province"], clue[0]["province"])
                    if clue[0]["city"]:
                        self.assertEqual(response["content"]["city"], clue[0]["city"])
                    if clue[0]["county"]:
                        self.assertEqual(response["content"]["county"], clue[0]["county"])
                    if clue[0]["address"]:
                        self.assertEqual(response["content"]["address"], clue[0]["address"])
                    if clue[0]["lng"]:
                        self.assertEqual(response["content"]["lng"], clue[0]["lng"])
                    if clue[0]["lat"]:
                        self.assertEqual(response["content"]["lat"], clue[0]["lat"])
                    if clue[0]["sale_num"]:
                        self.assertEqual(response["content"]["saleNum"], clue[0]["sale_num"])
                    if clue[0]["spleen_num"]:
                        self.assertEqual(response["content"]["spleenNum"], clue[0]["spleen_num"])
                    if clue[0]["intention_price"]:
                        self.assertEqual(response["content"]["intentionPrice"], clue[0]["intention_price"])
                else:
                    raise AssertionError("数据库未查询出数据")
            else:
                self.assertTrue(False, "卖蜂线索不存在")

    def test_mobile_bee_clue_add_contact_time(self):
        """
        接口地址： POST /mobile/bee-clue/add-contact-time 增加联系次数
        :return:
        """
        self.beeclue._mobile_bee_clue_add_contact_time(id_=9)

    def test_mobile_bee_clue_del(self):
        """
        接口地址：POST /mobile/bee-clue/del 删除卖蜂线索
        :return:
        """
        clue_list = self.beeclue._mobile_bee_clue_list()['content']['datas']
        if len(clue_list) is not None:
            num = random.randrange(0, len(clue_list))
            clue_id = clue_list[num]["id"]
            response = self.beeclue._mobile_bee_clue_del(id_=clue_id)
            if response["status"] == "OK":
                clue = self.beeclue_db.sql_bee_clue_is_delete(id=clue_id)
                self.assertEqual(clue[0]["is_delete"], 1)
            else:
                self.assertTrue(False, "卖蜂线索删除失败")
