#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Wei'
__date__ = '2019/7/13'
"""

import json
import time

from random import choice
from testcase.worldFarm import testCase,CattleMap


class CattleMapMain(testCase):

    fq = CattleMap()

    def test_mobile_cattle_set_frequency_clever(self):
        """
        移动端-设备频率-设置回传频率(快速找牛)
        V1.2.5 修改
        :return:
        """
        deviceEui = choice(self.fq.query_default_farm_cattle_info_list(self.email, '1,2'))
        register = self.ka.mobile_cattle_set_frequency_clever(farmId=deviceEui.get('farm_id'),
                                                              deviceEui=deviceEui.get('device_id'))
        self.assertEqual(register['status'], 'OK')

    def test_mobile_cattle_set_frequency_clever_batch(self):
        """
        移动端-设备频率-批量设置回传频率(快速找牛)
        :return:
        """
        deviceEui = choice(self.fq.query_default_farm_cattle_info_list(self.email, '1,2'))
        register = self.ka.mobile_cattle_set_frequency_clever_batch(farmId=deviceEui.get('farm_id'),
                                                                    deviceEuis=[deviceEui.get('device_id')])
        self.assertEqual(register['status'], 'OK')

    def test_mobile_cattle_frequency_num(self):
        """
        移动端-设备频率-临时频率数量
        V1.2.5 修改
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        register = self.ka.mobile_cattle_frequency_num(farmId=farmid)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_cattle_frequency_list(self):
        """
        移动端-设备频率-临时频率设备列表
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        register = self.ka.mobile_cattle_frequency_list(farmId=farmid, status=choice([0, 1, 2, None]))
        self.assertEqual(register['status'], 'OK')

    def test_mobile_cattle_close_frequency(self):
        """
        移动端-设备频率-关闭临时频率(关闭快速找牛：农场所有设备、单个设备)
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        register = self.ka.mobile_cattle_close_frequency(farmId=farmid, deviceEui=None)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_cattle_map_trace(self):
        """
        异常设备轨迹 1.2.2 农场内 lora设备
        查看轨迹1.2.3 修改
        查看轨迹1.2.6修改
        :return:
        """
        device = choice(self.fq.query_cattle_trace(group=1))
        register = self.ka.mobile_cattle_map_trace(farmId=device.get('farm_id'), deviceEui=device.get('device_eui'))
        if register.get('status') == "ERROR":
            self.log.info(register.get("errorMsg"))
            return
        self.assertEqual(register['status'], 'OK')

    def test_mobile_cattle_map_cattle_card(self):
        """
        牲畜卡片详情-lora耳标
        1.2.4 修改
        :return:
        """
        farminfo = self.fq.query_default_farm(self.email)[0]
        cattleinfo = self.fq.query_cattle_info(farminfo.get('farm_id'))[0]
        register = self.ka.mobile_cattle_map_cattle_card(farmId=cattleinfo.get('farm_id'),
                                                         deviceEui=cattleinfo.get('device_id'))

        self.assertEqual(register['status'], 'OK')
        # 判断农场ID
        self.assertEqual(cattleinfo.get('farm_id'), register['content']['farmId'])
        # 判断牲畜ID
        self.assertEqual(cattleinfo.get('id'), register['content']['cattleId'])
        # 判断牲畜出生日期
        # self.assertEqual(self.tt.str_time_timestamp(cattleinfo.get('birth_date')), register['content']['birthDate'])

    def test_mobile_cattle_map_bluetooth_near_cattle_list(self):
        """
        移动端-牲畜地图-蓝牙附近牲畜列表
        :return:
        """
        farminfo = self.fq.query_default_farm(self.email)[0]
        cattleinfo = self.fq.query_cattle_info(farminfo.get('farm_id'))
        deviceEuis = self.tool.data_assemble('device_id', cattleinfo, 10)
        register = self.ka.mobile_cattle_map_bluetooth_near_cattle_list(deviceEuis=deviceEuis)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_cattle_map_frequency_trace(self):
        """
        移动端-牲畜地图-开启临时频率后的轨迹
        :return:
        """
        register = self.ka.mobile_cattle_map_frequency_trace(farmId='547', deviceEui='11020203f0000029')
        self.assertEqual(register['status'], 'OK')

    def test_mobile_cattle_map_heat_map(self):
        """
        移动端-牲畜地图-热力图
        :return:
        """
        endTime = int(time.time() * 1000)
        startTime = endTime - 5 * 24 * 60 * 60 * 1000
        farmId = choice(self.fq.query_default_farm(self.email))
        register = self.ka.mobile_cattle_map_heat_map(farmId=farmId.get('farm_id'), positionTimeEnd=endTime,
                                                      positionTimeStart=startTime)
        self.assertEqual(register['status'], 'OK')
        if register:
            return
        heat = register['content']['positionList']
        endtime = self.tt.timestamp_formatting(endTime)
        starttime = self.tt.timestamp_formatting(startTime)
        dbheat = self.fq.query_farm_map_heat(farmid=farmId.get('farm_id'),
                                             endtime=endtime, starttime=starttime)
        heat_num = self.fq.query_farm_map_heat(farmid=farmId.get('farm_id'),
                                               endtime=endtime, starttime=starttime)
        self.assertEqual(register['content']['cattleNum'], len(heat_num))
        self.assertEqual(register['content']['positionTimeEnd'], endTime)
        self.assertEqual(register['content']['positionTimeStart'], startTime)
        for i in range(len(heat)):
            self.assertEqual(heat[i].get('lat'), dbheat[i].get('lat'))
            self.assertEqual(heat[i].get('lng'), dbheat[i].get('lng'))

    def test_mobile_c8attle_map_near_cattle_list(self):
        """
        移动端-牲畜地图-地图首页附近牲畜列表-1.2.3
        1.2.4 修改
        1.2.5 复用
        :return:
        """
        cattlelist = self.fq.query_near_cattle_list()

        register = self.ka.mobile_cattle_map_near_cattle_list(farmId=cattlelist[0].get('farm_id'),
                                                              deviceEui=cattlelist[0].get('device_id'), deviceType=2)
        self.assertEqual(register['status'], 'OK')
        for reg in register['content']:
            for cattle in cattlelist:
                if reg.get('eui') == cattle.get('device_id'):
                    # 判断牲畜名称
                    self.assertEqual(cattle.get('cattle_name'), reg['cattleName'])
                    # 判断牲畜出生日期
                    # self.assertEqual(cattle.get('birth_date'), reg['birthDate'])
                    # 判断牲畜种族
                    self.assertEqual(cattle.get('variety_id'), reg['varietyName'])
                    # 判断牲畜性别
                    # self.assertEqual(cattle.get('type'), reg['typeName'])

    def test_mobile_cattle_map_position_list(self):
        """
        移动端-牲畜地图-地图牲畜定位列表
        1.2.4 修改
        :return:
        """
        # register = self.ko.mobile_cattle_map_position_list(farmId='607', fenceId='174', positionType=0) 1.2.3
        regionlist = self.fq.query_region_cattle_list()
        register = self.ka.mobile_cattle_map_position_list(farmId=regionlist[0].get('farm_id'))
        self.assertEqual(register['status'], 'OK')

    def test_mobile_cattle_map_position_type_num(self):
        """
        移动端-牲畜地图-设备定位类型数量
        :return:
        """
        farm = choice(self.fq.query_default_farm(self.email))
        register = self.ka.mobile_cattle_map_position_type_num(farmId=farm.get('farm_id'),
                                                               fenceId=farm.get('region_id'))
        self.assertEqual(register['status'], "OK")

    def test_mobile_cattle_map_region_cattle_list(self):
        """
        移动端-牲畜地图-获取围栏内牲畜列表以及定位信息-1.2.3
        1.2.4 修改
        1.2.5 修改
        :return:
        """
        farm = choice(self.fq.query_default_farm(self.email))
        activeStatus = choice([1, 2, '1,2', None])
        deviceType = choice([3, 1, '1,3', None])
        bindStatus = choice([0, 1, '1,0', None])
        register = self.ka.mobile_cattle_map_region_cattle_list(activeStatus=activeStatus, deviceType=deviceType,
                                                                bindStatus=bindStatus, farmId=farm.get('farm_id'),
                                                                regionId=farm.get('region_id'), searchName=None,
                                                                searchNameOrVisionNum=None)
        self.assertEqual(register['status'], 'OK')
        bindStatus = 1 if deviceType and activeStatus else bindStatus
        cattle = self.fq.query_farm_region_cattle_info_list(farmid=farm.get('farm_id'),
                                                            regionid=farm.get('region_id'),
                                                            activeStatus=activeStatus, isBindDevice=bindStatus,
                                                            device_type=deviceType)
        content = register.get('content')

        if content:
            self.assertEqual(len(content), len(cattle))
            # for key in content[0].keys():
            #     self.assertListEqual(sorted(self.tool.data_assemble(key, content, len(content))),
            #                          sorted(self.tool.data_assemble(key, cattle, len(cattle))))

    def test_mobile_cattle_map_trace1(self):
        """
        移动端-牲畜地图-查询设备轨迹
        1.2.4 修改
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        deviceid = choice(self.fq.query_cattle_is_position(farmid=farmid)).get('device_eui')
        # deviceid ='0101020000001532'

        register = self.ka.mobile_cattle_map_trace(farmId=farmid,
                                                   deviceEui=deviceid)
        self.assertEqual(register['status'], 'OK')
        cattletrace = self.fq.query_cattle_histry_position(deviceid)
        cattletrace = self.tool.del_dict_value_null(cattletrace)
        content = register['content'].get('devicePositionResponseList')
        for i in range(len(content)):
            self.assertDictEqual(cattletrace[i], content[i])

    def test_common_calculate(self):
        """
        公共接口-面积/周长计算
        :return:
        """
        coordinate = '[{"lat":-25.018867511643137,"lng":147.58022623210945},{"lat":-25.340169074383184,"lng":147.62126079584834},{"lat":-25.3127543352156,"lng":147.93348030279174},{"lat":-24.988146260871247,"lng":147.89601396196292},{"lat":-25.018867511643137,"lng":147.58022623210945}]'
        coordinate_josn = json.dumps(json.loads(coordinate))
        register = self.ka.common_calculate(coordinate=coordinate_josn)
        self.assertEqual(register['status'], 'OK')

    def test_config_common_get_all_enum_list(self):
        """
        公共接口-获取所有枚举字典列表
        :return:
        """
        register = self.ka.config_common_get_all_enum_list()
        self.assertEqual(register['status'], 'OK')

    def test_config_common_get_config_list(self):
        """
        公共接口-字典配置-获取字典配置列表【model调整】
        :return:
        """
        register = self.ka.config_common_get_config_list(codes=None)
        self.assertEqual(register['status'], 'OK')

    def test_config_common_get_post_code_list(self):
        """
        公共接口-字典配置-后模糊查询邮编列表
        :return:
        """
        register = self.ka.config_common_get_post_code_list(code='')
        self.assertEqual(register['status'], 'OK')

    def test_mobile_farm_right_list(self):
        """
        获取指定农场的边界列表
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get("farm_id")
        register = self.ka.mobile_farm_right_list(farmId=farmid)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_farm_contacts_add(self):
        """
        添加联系信息
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get("farm_id")
        register = self.ka.mobile_farm_contacts_add(farmId=farmid, type=1, name="wei.zhang", region=None,
                                                    phone='15388126072', email=None)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_farm_contacts_change_farmer(self):
        """
        变更农场主
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get("farm_id")
        register = self.ka.mobile_farm_contacts_change_farmer(farmId=farmid, farmerId=188)
        self.assertEqual(register['status'], 'ERROR')
        self.assertEqual(register['errorMsg'], '没有操作权限')

    def test_mobile_farm_contacts_list(self):
        """
        获取农场联系人列表
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get("farm_id")
        register = self.ka.mobile_farm_contacts_list(farmId=farmid)

        self.assertEqual(register['status'], 'OK')

    def test_mobile_farm_contacts_farmer(self):
        """
        获取农场主信息
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get("farm_id")
        register = self.ka.mobile_farm_contacts_farmer(farmId=farmid)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_farm_contacts_update(self):
        """
        获取农场主信息
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get("farm_id")
        register = self.ka.mobile_farm_contacts_list(farmId=farmid)
        self.assertEqual(register['status'], 'OK')
        if register['content']['contactListOutput']:
            contactsid = register['content']['contactListOutput'][0]['contacts'][0]['id']
            self.ka.mobile_farm_contacts_update(id=contactsid, name='baron.zhang', region=None,
                                                phone='15388126073', email='632948101@qq.com')

    def test_mobile_farm_contacts_del(self):
        """
        获取农场主信息
        :return:
        """
        farmid = choice(self.fq.query_default_farm(self.email)).get("farm_id")
        register = self.ka.mobile_farm_contacts_list(farmId=farmid)
        contactsid = register['content']['contactListOutput'][0]['contacts'][0]['id']

        register = self.ka.mobile_farm_contacts_del(contactId=contactsid)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_share_add(self):
        """
        新增地图分享内容
        :return:
        """
        register = self.ka.mobile_share_add(farmId=621, content={
            "landmarkType": "10060,10130,10110,10240,10080,10120,10170,10180,10220"})
        self.assertEqual(register['status'], 'OK')

    def test_mobile_camera_add_or_update_name(self):
        """
        移动端-摄像头-添加或者修改摄像头名字
        :return:
        """
        register = self.ka.mobile_camera_add_or_update_name(farmId=547, number='D75520582',
                                                            name='接口测试%s' % int(time.time()))
        self.assertEqual(register['status'], 'OK')

    def test_mobile_camera_list(self):
        """
        移动端-摄像头-摄像头列表
        :return:
        """
        register = self.ka.mobile_camera_list(farmId=547)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_camera_get_token(self):
        """
        移动端-摄像头-摄像头列表
        :return:
        """
        register = self.ka.mobile_camera_get_token(appKey='WAIRBL')
        self.assertEqual(register['status'], 'OK')

    def test_mobile_app_version_upload_app(self):
        """
        上传安装包
        :return:
        """
        file = 'E://FTP//test.apk'
        register = self.ko.mobile_app_version_upload_app(file=file)
        self.assertEqual(register['status'], 'OK')


if __name__ == '__main__':
    m = CattleMapMain()
