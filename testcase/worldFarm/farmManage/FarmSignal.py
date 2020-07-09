#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2020 2020/2/20 11:58
__author__: wei.zhang
信号中继
"""
import time
from random import choice
from testcase.worldFarm import testCase,CattleMap


class CattleMapMain(testCase):

    fq = CattleMap()

    def test_mobile_cattle_bind_semaphore(self):
        """
        绑定信号中继
        :return:
        """
        device_eui = choice(self.fq.query_device_eui_id()).get('device_eui')
        farmid = choice(self.fq.query_default_farm(self.email)).get("farm_id")
        info = self.ka.mobile_cattle_bind_semaphore(farmId=farmid, deviceId=device_eui)
        self.assertEqual(info['status'], "OK")
        device = self.fq.query_bind_device_id(farmid=farmid, deviceid=device_eui)[0]
        self.assertEqual(device_eui, device.get('device_eui'))
        self.assertEqual(farmid, device.get('farm_id'))

    def test_mobile_cattle_map_farm_signal(self):
        """
        移动端-牲畜地图-农场信号
        :return:
        """
        farm = choice(self.fq.query_default_farm(self.email))
        register = self.ka.mobile_cattle_map_farm_signal(farmId=farm.get('farm_id'))
        self.assertEqual(register['status'], 'OK')
        self.assertEqual(type(register.get('content')), list)

    def test_mobile_cattle_map_add_or_update_name(self):
        """
        移动端-牲畜地图-添加或者修改农场信号名字【v1.2.6 可联调】 修改信号中继
        :return:
        """
        name = "接口测试%d" % int(time.time())
        devicedata = choice(self.fq.query_may_device_update(self.email))
        register = self.ka.mobile_cattle_map_add_or_update_name(farmId=devicedata.get('farm_id'),
                                                                number=devicedata.get('device_eui'), type="10030",
                                                                name=name)
        device = self.fq.query_device_remark(farmid=devicedata.get('farm_id'), deviceno=devicedata.get('device_eui'))[0]
        self.assertEqual(register['status'], 'OK')
        self.assertEqual(device.get("device_name"), name)

    def test_mobile_cattle_map_signal_relay_del(self):
        """
        移动端-牲畜地图-信号中继删除【v1.2.6 可联调】
        :return:
        """
        devicedata = choice(self.fq.query_may_device_update(self.email))
        register = self.ka.mobile_cattle_map_signal_relay_del(farmId=devicedata.get('farm_id'),
                                                              serialNo=devicedata.get('device_eui'))
        self.assertEqual(register['status'], 'OK')
        device = self.fq.query_bind_device_id(farmid=devicedata.get('farm_id'), deviceid=devicedata.get('device_eui'))
        self.assertEqual(device, None)

    def test_mobile_farm_signal_list(self):
        """
        移动端-农场信号中继-列表-农场信号【v1.2.8可联调】
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        register = self.ka.mobile_farm_signal_list(farmId=farmid)
        self.assertEqual(register.get('status'), 'OK')
        signal = self.fq.query_farm_device_bind_signal_relay(farmid=farmid)
        device_eui = self.tool.data_assemble('device_eui', signal)
        deviceId = self.tool.data_assemble('deviceId', register.get('content'))
        self.assertListEqual(device_eui, deviceId)

    def test_mobie_farm_signal_del(self):
        """
        移动端-农场信号中继-删除-农场信号【v1.2.8可联调】
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        device_eui = choice(self.fq.query_farm_device_bind_signal_relay(farmid=farmid)).get('device_eui')
        register = self.ka.mobile_farm_signal_del(farmId=farmid, deviceId=device_eui)
        self.assertEqual(register.get('status'), 'OK')
