#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.fake.FakeLocation import FakeLocation
from utils.log.logger import logger
from testcase.flowerChaser.sql.Bee import ContainerInformationSql, ShuntSql
import random
from faker import Faker
import time, datetime
import json
from utils.Timestamp.TimestampTransform import TimestampTransform as tt
from utils.dataConversion.dataConversion import DataConversion as tl


class ContainerMain(unittest.TestCase, tt, FakeLocation, tl):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    container = BeeAction()
    container_db = ContainerInformationSql()
    shunt_db = ShuntSql()
    log = logger('ContainerMain').logger
    fake = Faker(locale="zh_CN")
    container.set_user('19982917912')

    def setUp(self) -> None:
        self.log.info("开始执行调车接口测试用例")

    def tearDown(self) -> None:
        self.log.info("结束执行调车接口测试用例")

    def test_mobile_shunt_add(self):
        """
        POST _mobile_shunt_add
        调车信息发布 new 2.2.1
        :return:
        """

        def str_split(s: str):
            num = s[s.find('县'):-1]
            if not num:
                num = s[s.find('区'):-1]
            return num

        truck_list = ["1.8", "2.7", "3.8", "4.2", "5", "6.2", "6.8", "7.7", "8.2", "8.7", "9.6", "11.7",
                      "12.5", "13", "13.7", "15", "16", "17.5"]
        truckTL = ["1", "2", "12", "3"]
        cargo_T = {"蜜蜂": "1", "蜂箱": "2", "蜂蜜": "3", "空桶": "4", "空托盘": "5", "空木箱": "6", "杂件": "7"}
        load_province_id, load_city_id, load_district_id, load_address, load_lng, load_lat = self.fake_location()
        unload_province_id, unload_city_id, unload_district_id, unload_address, unload_lng, unload_lat = self.fake_location()
        loadadder = {
            "addressType": '1',
            "province": load_province_id,
            "city": load_city_id,
            "county": load_district_id,
            "lat": load_lat,
            "lng": load_lng,
            "address": load_address,
            "locationName": str_split(load_address)
        }  # 装货地址
        unloadadder = {
            "addressType": '2',
            "province": unload_province_id,
            "city": unload_city_id,
            "county": unload_district_id,
            "lat": unload_lat,
            "lng": unload_lng,
            "address": unload_address,
            "locationName": str_split(unload_address)
        }  # 卸货地址
        loadingType = random.choice([1, 2, 3])  # 装卸方式
        loadAddressId = None  # 装货地址id(地址薄选择)
        unloadAddressId = None  # 卸货地址id(地址薄选择)
        useTime = self.get_standardtime_timestamp(day=random.randint(0, 5),
                                                  hour=random.randint(1, 23),
                                                  formats="%Y-%m-%d %H")  # 用车时间

        cargoName = random.choice(["蜂蜜", "蜜蜂", "蜂箱", "空桶", "空木箱", "空托盘", "杂件"])  # 货物名称
        cargoType = cargo_T.get(cargoName)  # 货物类型
        amount = random.randint(1, 2000)  # 数量
        minWeight = random.randint(1, 500)  # 重量最小值
        maxWeight = int(minWeight * 1.2)  # 重量最大值
        minCapacity = random.randint(1, 500)  # 体积最小值
        maxCapacity = int(minCapacity * 1.2)  # 体积最小值
        useType = random.randint(0, 1)  # 用车类型
        truckLengthList = ','.join(random.sample(truck_list, 3))  # 车长
        truckTypeList = ','.join(random.sample(truckTL, 3))  # 车型
        mileage = random.randint(1000, 999999999)
        isFindPickBees = None if loadingType != 10 else random.choice(['true', 'false'])  # 找人挑蜂
        remark = "添加调车发货接口测试"  # 备注
        shuntAddressInputs = json.dumps([loadadder, unloadadder])  # 装卸货地址

        response = self.container._mobile_shunt_add(loadingType_=loadingType, loadAddressId_=loadAddressId,
                                                    unloadAddressId_=unloadAddressId, useTime_=useTime,
                                                    cargoType_=cargoType,
                                                    cargoName_=cargoName, amount_=amount, minWeight_=minWeight,
                                                    maxWeight_=maxWeight, minCapacity_=minCapacity,
                                                    maxCapacity_=maxCapacity,
                                                    useType_=useType, truckLengthList_=truckLengthList,
                                                    truckTypeList_=truckTypeList,  mileage_=mileage, isFindPickBees_=isFindPickBees,
                                                    remark_=remark,
                                                    shuntAddressInputs_=shuntAddressInputs)
        self.assertEqual(response.get('status'), 'OK')

    def test_mobile_shunt_list(self):
        """
        调车历史-列表 new 2.0
        :return:
        """
        pn = 1
        ps = 20
        resp = self.container._mobile_shunt_list(pn_=pn, ps_=ps)
        self.assertEqual(resp.get('status'), 'OK')
        userid = self.container.user.user_id
        shunt_list = self.shunt_db.query_shunt_list_info(userid=userid)
        shunt_info_id = 1
        shunt_a = ''
        shunt_info_list = []
        for shunt_info in shunt_list:
            shunt, shunt_address = self.dict_chunk(shunt_info, 25)
            shunt_address.update({'id': shunt_address.pop('address_id')})
            shunt_address = self.del_dict_value_null(shunt_address)
            if shunt_info_id != shunt.get('id'):
                shunt_a = self.del_dict_value_null(shunt)
                if shunt_address.get('addressType') == 1:
                    shunt_a['loadAddressOutput'] = shunt_address
                else:
                    shunt_a['unloadAddressOutput'] = shunt_address
                shunt_info_id = shunt.get('id')
            else:
                if shunt_address.get('addressType') == 1:
                    shunt_a['loadAddressOutput'] = shunt_address
                else:
                    shunt_a['unloadAddressOutput'] = shunt_address
                shunt_info_list.append(shunt_a)
        content = resp.get('content')
        datas = content.get('datas')
        for i in range(len(datas)):
            self.assertDictEqual(datas[i], shunt_info_list[i])

    def test__mobile_shunt_detail(self):
        """
        POST /mobile/shunt/detail
        调车详情 new 2.0
        :return:
        """
        shunt_status = random.choice([1, 2, 3])
        userid = self.container.user.user_id
        shunt_id_list = self.shunt_db.sql_shunt_buy_status(shunt_status=shunt_status, user_id=userid)
        if len(shunt_id_list) == 0:
            self.log.info("未获取到调车记录ID")
        else:
            shunt_id = shunt_id_list[0].get('id')
            self.container._mobile_shunt_detail(shuntId_=shunt_id)

    def test_mobile_shunt_confirm(self):
        """
        POST /mobile/shunt/confirm
        调车历史-确认调车 new 2.0
        :return:
        """
        shunt_status = 1
        userid = self.container.user.user_id
        shunt_id_list = self.shunt_db.sql_shunt_buy_status(shunt_status=shunt_status, user_id=userid)
        if len(shunt_id_list) == 0:
            self.log.info("未获取到状态为调车中的调车记录ID")
        else:
            shunt_id = shunt_id_list[0].get('id')
            driver_name = "接口测试司机姓名" + self.fake.name()
            phone_head = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151",
                          "152", "153", "155", "156", "157", "158", "159", "186", "187", "188"]
            plate_number = "川A 12345"
            phone = random.choice(phone_head) + "".join(random.choice("0123456789") for i in range(8))
            self.container._mobile_shunt_confirm(id_=shunt_id, driverName_=driver_name,
                                                 driverTelephone_=phone, plateNumber_=plate_number)
            db_info = self.shunt_db.sql_shunt_buy_id(shunt_id=shunt_id)
            self.assertEqual(db_info[0]['shunt_status'], 2)

    def test_mobile_shunt_arrive(self):
        """
        POST /mobile/shunt/arrive
        调车历史-确认到达 new 2.0
        :return:
        """
        shunt_status = 2
        userid = self.container.user.user_id
        shunt_id_list = self.shunt_db.sql_shunt_buy_status(shunt_status=shunt_status, user_id=userid)
        if len(shunt_id_list) == 0:
            self.log.info("未获取到状态为已调车的调车记录ID")
        else:
            shunt_id = shunt_id_list[0].get('id')
            now_time = int((time.time()) * 1000)
            self.container._mobile_shunt_arrive(shuntId_=shunt_id, arriveTime_=now_time)
            db_data = self.shunt_db.sql_shunt_buy_id(shunt_id=shunt_id)
            self.assertEqual(db_data[0]['shunt_status'], 4)

    def test_mobile_shunt_cancel(self):
        """
        POST /mobile/shunt/cancel
        调车历史-取消调车 new 2.0
        :return:
        """
        shunt_status = random.choice([1, 2])
        userid = self.container.user.user_id
        shunt_id_list = self.shunt_db.sql_shunt_buy_status(shunt_status=shunt_status, user_id=userid)
        if len(shunt_id_list) == 0:
            self.log.info("未获取到状态为调车中/已调车的调车记录ID")
        else:
            shunt_id = shunt_id_list[0].get('id')
            cancel_type = random.choice([1, 2, 3, 99])
            self.container._mobile_shunt_cancel(shuntId_=shunt_id, cancelType_=cancel_type)
            db_data = self.shunt_db.sql_shunt_buy_id(shunt_id=shunt_id)
            self.assertEqual(db_data[0]['shunt_status'], 3)

    def test_mobile_shunt_address_list(self):
        """
        调车发布-地址簿 new 2.0
        /mobile/shunt-address/list
        :return:
        """
        addressType = random.randint(1, 2)
        resp = self.container._mobile_shunt_address_list(addressType_=addressType)
        self.assertEqual(resp.get('status'), 'OK')
        userid = self.container.user.user_id
        addresslist = self.shunt_db.query_chunt_address_info_list(addressType=addressType, userid=userid)
        content = resp.get('content')
        for i in range(len(content)):
            self.assertDictEqual(content[i], addresslist[i])

    def test_mobile_shunt_driver_list(self):
        """
        调车详情-已联系司机列表 new 2.0
        post    /mobile/shunt/driver-list
        :return:
        """

        shunt_status = 1
        userid = self.container.user.user_id
        shunt_id_list = self.shunt_db.sql_shunt_buy_status(shunt_status=shunt_status, user_id=userid)
        shuntId = random.choice(shunt_id_list).get('id')
        resp = self.container._mobile_shunt_driver_list(shuntId_=shuntId)
        self.assertEqual(resp.get('status'), 'OK')

    def test_mobile_shunt_nearby_list(self):
        """
        附近挑蜂列表 new 2.0

        :return:
        """
        # province_id, city_id, district_id, address, lng, lat = self.fake_location()
        self.container._mobile_shunt_nearby_list(lng_=104.06895697699653, lat_=30.53841552734375)
