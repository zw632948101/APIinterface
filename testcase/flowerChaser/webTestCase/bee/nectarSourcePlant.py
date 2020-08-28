#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log import log
from faker import Faker
from testcase.flowerChaser.sql.Bee import NectarSourcePlant
from utils.fake.FakeLocation import FakeLocation
import random
import json
import time, datetime
from utils.dataConversion.dataConversion import DataConversion as dc


class RegisterLoginMain(unittest.TestCase):
    """
    接口文档: http://192.168.62.242:36054/swagger-ui.html
    """
    ba = BeeAction()
    db = NectarSourcePlant()
    fl = FakeLocation()
    mobile = '15388126082'
    log.info("开始执行蜜源植物管理模块测试用例")
    fake = Faker(locale="zh_CN")
    ba.set_user(mobile)

    def test_admin_nectar_source_plant_add(self):
        """
        添加蜜源植物

        """
        plantName = int(time.time())
        type_ = random.choice([1, 2])  # 蜜源类型（1主要蜜源2辅助蜜源）
        variety = '接口測試品种'
        slice_ = '接口测试蜜源植物别名'
        region = '接口测试蜜源植物主要分布区域（成都）'
        area = random.randint(1000, 9999999)
        features = ['接口测试1', '接口测试2']
        floweringDescription = '接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述'
        nectarFlowCondition = '接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件'
        powderType = random.choice([1, 2, 3])  # 蜜粉情况(1蜜粉丰富2蜜少粉多3蜜多粉少)
        minHoneyYield = random.randint(100, 999)  # 最小产蜜量/群(公斤)
        maxHoneyYield = random.randint(minHoneyYield, 999)  # 最大产蜜量/群(公斤)
        codeIcon = "https://dnkj-world-farm-prd.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/nectar-source-type/1576581418905.png"
        mapIcon = "https://dnkj-world-farm-prd.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/nectar-source-type/1576581418905.png"
        remark = '接口测试蜜源植物添加'
        pics = [{
            "url": "https://dnkj-world-farm-prd.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/nectar-source-type/1576581418905.png",
            "tag": "接口测试标签", "rmark": "接口测试备注"}]
        response = self.ba._admin_nectar_source_plant_add(plantName_=plantName, type_=type_, variety_=variety,
                                                          alias_=slice_, region_=region,
                                                          area_=area, floweringDescription_=floweringDescription,
                                                          nectarFlowCondition_=nectarFlowCondition,
                                                          powderType_=powderType, minHoneyYield_=minHoneyYield,
                                                          maxHoneyYield_=maxHoneyYield,
                                                          codeIcon_=codeIcon, mapIcon_=mapIcon, remark_=remark,
                                                          features_=features, pics_=json.dumps(pics))
        self.assertEqual(response["status"], "OK")
        infolist = self.db.query_nectar_source_plant_info(plantName=plantName)
        self.assertEqual(len(infolist), 1)

    def test_admin_nectar_source_plant_detail(self):
        """
        蜜源植物详情 V2.3.0
        """
        plant_dict = dc.del_dict_value_null(random.choice(self.db.query_nectar_source_plant_all()))
        plant_id = plant_dict.get('id')
        response = self.ba._admin_nectar_source_plant_detail(id_=plant_id)
        log.info(response.get('content'))
        self.assertEqual(response["status"], "OK")
        self.db.query_nectar_source_plant_attach(plantCode=plant_dict.get('code'))
        self.assertDictEqual(response.get('content'), plant_dict)

    def test_admin_nectar_source_plant_edit(self):
        """
        编辑蜜源植物 V2.5.0
        """
        # plant_dict = dc.del_dict_value_null(random.choice(self.db.query_nectar_source_plant_all()))
        plant_id = 112
        plantName = int(time.time())
        type_ = random.choice([1, 2])  # 蜜源类型（1主要蜜源2辅助蜜源）
        variety = '接口測試品种'
        slice_ = '接口测试蜜源植物别名'
        region = '接口测试蜜源植物主要分布区域（成都）'
        area = random.randint(1000, 9999999)
        features = ['接口测试1', '接口测试2']
        floweringDescription = '接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述'
        nectarFlowCondition = '接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件'
        powderType = random.choice([1, 2, 3])  # 蜜粉情况(1蜜粉丰富2蜜少粉多3蜜多粉少)
        minHoneyYield = random.randint(100, 999)  # 最小产蜜量/群(公斤)
        maxHoneyYield = random.randint(minHoneyYield, 999)  # 最大产蜜量/群(公斤)
        codeIcon = "https://dnkj-world-farm-prd.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/nectar-source-type/1576581418905.png"
        mapIcon = "https://dnkj-world-farm-prd.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/nectar-source-type/1576581418905.png"
        remark = '接口测试蜜源植物添加'
        pics = [{
            "url": "https://dnkj-world-farm-prd.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/nectar-source-type/1576581418905.png",
            "tag": "接口测试标签", "rmark": "接口测试备注"}]
        response = self.ba._admin_nectar_source_plant_edit(plantName_=plantName, type_=type_, variety_=variety,
                                                           alias_=slice_, region_=region,
                                                           area_=area, floweringDescription_=floweringDescription,
                                                           nectarFlowCondition_=nectarFlowCondition,
                                                           powderType_=powderType, minHoneyYield_=minHoneyYield,
                                                           maxHoneyYield_=maxHoneyYield, id_=plant_id,
                                                           codeIcon_=codeIcon, mapIcon_=mapIcon, remark_=remark,
                                                           features_=features, pics_=json.dumps(pics))
        self.assertEqual(response["status"], "OK")
        infolist = self.db.query_nectar_source_plant_info(plantName=plantName)
        self.assertEqual(len(infolist), 1)

    def test_admin_nectar_source_plant_list(self):
        """
        蜜源植物-列表 V2.5
        """
        pn = 1
        ps = 10
        type_ = random.choice([None, 1, 2])
        powderType = random.choice([None, 1, 2, 3])
        name = None
        sortType = random.choice([1, 2, 3, 4])
        flowering = None
        response = self.ba._admin_nectar_source_plant_list(pn_=pn, ps_=ps, type_=type_, powderType_=powderType,
                                                           name_=name,
                                                           sortType_=sortType, flowering_=flowering)
        self.assertEqual(response["status"], "OK")

    def test_admin_nectar_source_plant_count(self):
        """
        蜜源植物统计 V2.5

        """
        response = self.ba._admin_nectar_source_plant_count()
        self.assertEqual(response["status"], "OK")
        plant_count = self.db.query_nectar_source_plant_count()
        content = response.get('content')
        self.assertDictEqual(plant_count, content)

    def test_admin_nectar_source_point_add(self):
        """

        """