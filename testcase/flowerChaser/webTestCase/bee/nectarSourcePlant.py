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
    mobile = '15200000003'
    log.info("开始执行蜜源植物管理模块测试用例")
    fake = Faker(locale="zh_CN")
    ba.set_user(mobile)

    def test_admin_nectar_source_plant_add(self):
        """
        添加蜜源植物

        """
        plantName = '油菜'
        type_ = random.choice([1, 2])  # 蜜源类型（1主要蜜源2辅助蜜源）
        variety = '接口測試品种'
        slice_ = '接口测试蜜源植物别名'
        region = '接口测试蜜源植物主要分布区域（成都）'
        area = random.randint(1000, 9999999)
        floweringDescription = '接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述接口测试蜜源植物花期描述'
        nectarFlowCondition = '接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件接口测试蜜源植物留蜜条件'
        powderType = random.choice([1, 2, 3])  # 蜜粉情况(1蜜粉丰富2蜜少粉多3蜜多粉少)
        minHoneyYield = random.randint(100, 999)  # 最小产蜜量/群(公斤)
        maxHoneyYield = random.randint(minHoneyYield, 999)  # 最大产蜜量/群(公斤)
        codeIcon = "https://dnkj-world-farm-prd.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/nectar-source-type/1576581418905.png"
        mapIcon = "https://dnkj-world-farm-prd.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/nectar-source-type/1576581418905.png"
        remark = '接口测试蜜源植物添加'
        response = self.ba._admin_nectar_source_plant_add(plantName_=plantName, type_=type_, variety_=variety,
                                                          alias_=slice_, region_=region,
                                                          area_=area, floweringDescription_=floweringDescription,
                                                          nectarFlowCondition_=nectarFlowCondition,
                                                          powderType_=powderType, minHoneyYield_=minHoneyYield,
                                                          maxHoneyYield_=maxHoneyYield,
                                                          codeIcon_=codeIcon, mapIcon_=mapIcon, remark_=remark)
        self.assertEqual(response["status"], "OK")

    def test_admin_nectar_source_plant_detail(self):
        """
        蜜源植物详情 V2.3.0
        """
        plant_dict = dc.del_dict_value_null(random.choice(self.db.query_nectar_source_plant_all()))
        plant_id = plant_dict.get('id')
        response = self.ba._admin_nectar_source_plant_detail(id_=plant_id)
        log.info(response.get('content'))
        self.assertEqual(response["status"], "OK")
        self.assertDictEqual(response.get('content'), plant_dict)
