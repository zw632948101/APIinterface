#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Wei'
__date__ = '2019/ / '
农场物资
"""
import random
from testcase.worldFarm import testCase,FarmManage


class SuppliesMain(testCase):

    fq = FarmManage()

    def test_mobile_farm_supplies_add(self):
        """
        移动端-农场物资-添加农场物资【v1.2.6 可联调】
        :return:
        """
        farm_id_list = self.fq.query_default_farm(email=self.email)
        farm_id = farm_id_list[0]['farm_id']
        suppliesType = random.choice(['10', '20', '30', '40'])
        supplies = {'10': ['犁', '耙', '镰刀', '收割机', '播种机', '灌溉机'], '20': ['土豆种植技术', '南瓜种植技术', '肉牛养殖'],
                    '30': ["杀虫剂", "杀螨剂", "杀鼠剂", "杀线虫剂", "杀软体动物剂"], '40': ['汽车', '沙滩车', '山地车']}
        suppliesName = random.choice(supplies.get(suppliesType))
        specs = {'10': ['台', '把'], '20': ['本'], '30': ['袋', '箱', '瓶'], '40': ['台']}
        specs = random.choice(specs.get(suppliesType))
        resource = random.choice(['购买', '赠送'])
        price = random.randint(10, 99999)
        stock = random.randint(1, 10)
        unit = specs
        acqDate = self.tt.get_standardtime_timestamp(type=0, day=random.randint(1, 100))
        expDate = self.tt.get_standardtime_timestamp(day=random.randint(1, 100))
        remark = "接口测试任务描述8"
        imgs = 'https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1713274956,427129811&fm=26&gp=0.jpg'
        register = self.ka.mobile_farm_supplies_add(farmId=farm_id, suppliesType=suppliesType,
                                                    suppliesName=suppliesName,
                                                    specs=specs, resource=resource, price=price, stock=stock, unit=unit,
                                                    acqDate=acqDate, expDate=expDate, remark=remark, imgs=imgs)
        self.assertEqual(register['status'], "OK")
        supplies = self.fq.query_farm_supplies_add_info(farmid=farm_id)
        self.assertEqual(int(suppliesType), supplies.get('supplies_type'))
        self.assertEqual(suppliesName, supplies.get('supplies_name'))
        self.assertEqual(specs, supplies.get('specs'))
        self.assertEqual(resource, supplies.get('resource'))
        self.assertEqual(price, supplies.get('price'))
        self.assertEqual(remark, supplies.get('remark'))

    def test_mobile_farm_supplies_count(self):
        """
        移动端-农场物资-农场详情-物资数量统计【v1.2.6 可联调】
        :return:
        """
        farm_id = random.choice(self.fq.query_default_farm(email=self.email)).get('farm_id')
        register = self.ka.mobile_farm_supplies_count(farmId=farm_id)
        self.assertEqual(register['status'], "OK")
        supplies_num = self.fq.query_farm_supplies_add_info_count(farm_id)
        self.assertEqual(register['content'], supplies_num.get('supplies_num'))

    def test_mobile_farm_supplies_detail(self):
        """
        移动端-农场物资-农场物资详情【v1.2.6 可联调】
        :return:
        """
        farm_id = random.choice(self.fq.query_default_farm(email=self.email)).get('farm_id')
        supplies = self.fq.query_farm_supplies_add_info(farmid=farm_id)
        register = self.ka.mobile_farm_supplies_detail(suppliesId=supplies.get('id'))

        self.assertEqual(register['status'], "OK")
        register = register.get('content')
        self.assertEqual(register.get('suppliesType'), supplies.get('supplies_type'))
        self.assertEqual(register.get('suppliesName'), supplies.get('supplies_name'))
        self.assertEqual(register.get('specs'), supplies.get('specs'))
        self.assertEqual(register.get('resource'), supplies.get('resource'))
        self.assertEqual(register.get('price'), supplies.get('price'))
        self.assertEqual(register.get('remark'), supplies.get('remark'))

    def test_mobile_farm_supplies_list(self):
        """
        移动端-农场物资-农场物资详情【v1.2.6 可联调】
        :return:
        """
        farm_id = random.choice(self.fq.query_default_farm(email=self.email)).get('farm_id')
        suppliesType = random.choice(['10', '20', '30', '40'])
        register = self.ka.mobile_farm_supplies_list(farmId=farm_id, suppliesType=suppliesType)
        self.assertEqual(register['status'], "OK")
        supplies_list = self.fq.query_farm_supplies_info_list(farm_id, suppliesType)
        register = register.get('content')
        datas = register.get('datas')
        self.assertEqual(register.get('tc'), len(supplies_list))
        for i in range(len(datas)):
            self.assertEqual(datas[i].get('id'), supplies_list[i].get('id'))

    def test_mobile_farm_supplies_update(self):
        """
        移动端-农场物资-添加农场物资【v1.2.6 可联调】
        :return:
        """
        farm_id = random.choice(self.fq.query_default_farm(email=self.email)).get('farm_id')

        supplies = self.fq.query_farm_supplies_add_info(farm_id)
        suppliesType = str(supplies.get('supplies_type'))
        suppliesid = supplies.get('id')
        supplies = {'10': ['犁', '耙', '镰刀', '收割机', '播种机', '灌溉机'], '20': ['土豆种植技术', '南瓜种植技术', '肉牛养殖'],
                    '30': ["杀虫剂", "杀螨剂", "杀鼠剂", "杀线虫剂", "杀软体动物剂"], '40': ['汽车', '沙滩车', '山地车']}
        suppliesName = random.choice(supplies.get(suppliesType))
        specs = {'10': ['台', '把'], '20': ['本'], '30': ['袋', '箱', '瓶'], '40': ['台']}
        specs = random.choice(specs.get(suppliesType))
        resource = random.choice(['购买', '赠送'])
        price = random.randint(10, 99999)
        stock = random.randint(1, 10)
        unit = specs
        acqDate = self.tt.get_standardtime_timestamp(type=0, day=random.randint(1, 100))
        expDate = self.tt.get_standardtime_timestamp(day=random.randint(1, 100))
        remark = "接口测试任务描述-编辑"
        imgs = 'https://dss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=1713274956,427129811&fm=26&gp=0.jpg'

        register = self.ka.mobile_farm_supplies_update(id=suppliesid, farmId=farm_id, suppliesType=suppliesType,
                                                       suppliesName=suppliesName,
                                                       specs=specs, resource=resource, price=price, stock=stock,
                                                       unit=unit,
                                                       acqDate=acqDate, expDate=expDate, remark=remark, imgs=imgs)
        self.assertEqual(register['status'], "OK")
        supplies = self.fq.query_farm_supplies_info(suppliesid)
        self.assertEqual(int(suppliesType), supplies.get('supplies_type'))
        self.assertEqual(suppliesName, supplies.get('supplies_name'))
        self.assertEqual(specs, supplies.get('specs'))
        self.assertEqual(resource, supplies.get('resource'))
        self.assertEqual(price, supplies.get('price'))
        self.assertEqual(remark, supplies.get('remark'))

    def test_mobile_farm_supplies_del(self):
        """
        移动端-农场物资-农场物资删除【v1.2.6 可联调】
        :return:
        """
        farm_id = random.choice(self.fq.query_default_farm(email=self.email)).get('farm_id')
        supplies = self.fq.query_farm_supplies_add_info(farmid=farm_id)
        register = self.ka.mobile_farm_supplies_del(suppliesId=supplies.get('id'))
        self.assertEqual(register['status'], "OK")
        supplies_info = self.fq.query_farm_supplies_info(supplies.get('id'))
        self.assertEqual(supplies_info.get('is_delete'), 1)
