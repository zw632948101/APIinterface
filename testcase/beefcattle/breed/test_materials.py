#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/24 10:54
# @Author: wei.zhang
# @File : test_materials.py
# @Software: PyCharm
import unittest
from interfaces.beefcattle.BreedAction import breedAction
from utils.log import log


class TestMaterials(unittest.TestCase):
    """
    物资管理
    接口文档:http://dev-gateway.worldfarm.com/swagger-ui.html
    """
    breed = breedAction()
    log.info("养殖育肥服务-物资管理")
    breed.set_user(mobile=15388126072)

    def test_admin_materials_warhouse_list(self):
        """
         WEB-物资管理-仓库列表
        :return:
        """
        company_code = '100004'
        resp = self.breed._admin_materials_warehouse_list(companyCode_=company_code)
        self.assertEqual(resp.get('status'), 'OK')

    def test_admin_materials_inventory_list(self):
        """
        WEB-物资管理-物资列表
        :return:
        """
        pn = None
        ps = None
        warehouse_code = '50123'
        product_code = None
        product_name = None
        resp = self.breed._admin_materials_inventory_list(pn_=pn, ps_=ps,
                                                          warehouseCode_=warehouse_code,
                                                          productCode_=product_code,
                                                          productName_=product_name)
        self.assertEqual(resp.get('status'), 'OK')

    def test_admin_materials_inventory_detail(self):
        """
        WEB-物资管理-物资详情
        :return:
        """
        warehouse_code = '70088'
        product_code = 'T1608010001'
        resp = self.breed._admin_materials_inventory_detail(warehouseCode_=warehouse_code,
                                                            productCode_=product_code)
        self.assertEqual(resp.get('status'), 'OK')
