#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2019/7/13'
"""

import unittest
import json
import datetime, time

from tools.Config import Config

from tools.Session import UserSession
from actions.PassportAction import PassportAction
from actions.KoalaAction import KoalaAction
from actions.UserAction import UserAction
from testcase.worldFarm.sql.SmokeMainQuery import SmokeMainQuery
from actions.FakePosition import Transitions
from random import uniform
from random import randint, choice


class Main(unittest.TestCase):

    category = [{'围栏': '10010'}, {'区域': '10020'}, {'房屋及建筑': '10030'}, {'水资源': '10040'}, {'道路': '10050'}]
    kinds = {'房屋及建筑': [{'房屋': '10060'}, {'干草棚': '10070'}, {'谷仓': '10080'}, {'棚子': '10090'},
                       {'操作栏': '10100'}, {'门': '10110'}, {'信号塔': '10120'}, {'太阳能电站': '10130'}],
             '水资源': [{'水井': '10140'}, {'水坝': '10150'}, {'管道': '10160'}, {'水渠': '10170'},
                     {'饮水槽': '10180'}, {'风车': '10190'}, {'水箱': '10200'}, {'水泵': '10210'}, {'蓄水池': '10240'}],
             '道路': [{'道路': '10220'}]}
    leafNodes = {
        "branchNode": False,
        "leafNodes": [
        ],
        "location": {
            "lat": -27.61998178738515,
            "lng": 150.6437266043214
        }
    }

    geo_list = []

    # 登录
    # 农场创建
    # 围栏添加
    # 地标添加
    # 牲畜添加
    # 绑定设备(子母耳标) # 6位, 16位
    # 热力图 / 轨迹
    # 找牛触发(正常 / 启用 / 生效)
    # 母耳标点击跳转
    # 消息(出栏, 混栏, 异常)
    # 跳转
    # 消息红点

    def setUp(self) -> None:
        self.email = Config('config').data['account'].get('username')
        ENV = Config('config').data['run']
        user = UserSession()
        # mgr_user = MgrSession('root', 'agrrobot_2019', ENV)
        # self.mgr = MgrAction(mgr_user, ENV)
        self.fq = SmokeMainQuery()
        self.pa = PassportAction(user)
        self.ua = UserAction(user)
        self.ko = KoalaAction(user)
        self.fp = Transitions(ENV)

    def tearDown(self) -> None:
        pass

    def random_rectangle(self, lat=None, lng=None):
        """
        随机经纬度产生矩形
        :return:
        """
        if lat == None and lng == None:
            rand_lat = round(uniform(-89.545000, 89.545000), 6)
            rand_lng = round(uniform(-179.545000, 179.545000), 6)
        else:
            rand_lat = lat
            rand_lng = lng
        self.log.info('中心点: %s' % [rand_lng, rand_lat])
        geo_list = []
        for i in (0.045500, 0.022700):
            if i == 0.045500:
                distance = i
            elif i == 0.022700:
                distance = i
                y1 = json.dumps({"lng": (rand_lng + 0), "lat": (rand_lat + distance)})
                y2 = json.dumps({"lng": (rand_lng + 0), "lat": (rand_lat - distance)})

            p0 = json.dumps({"lng": (rand_lng + distance), "lat": (rand_lat + distance)})
            p1 = json.dumps({"lng": (rand_lng + distance), "lat": (rand_lat - distance)})
            p2 = json.dumps({"lng": (rand_lng - distance), "lat": (rand_lat - distance)})
            p3 = json.dumps({"lng": (rand_lng - distance), "lat": (rand_lat + distance)})
            if distance == 0.045500:
                geo_str = '[ %s, %s, %s, %s, %s ]' % (p0, p1, p2, p3, p0)
            else:
                geo_str = '[ %s, %s, %s, %s, %s ]' % (p0, p1, y2, y1, p0)
                geo_str1 = '[ %s, %s, %s, %s, %s ]' % (y1, y2, p2, p3, y1)
                locations1 = json.loads(geo_str1)
                if locations1:
                    for loc in locations:
                        geo_list.append([loc['lng'], loc['lat']])
                    self.log.info('坐标集: %s' % geo_list)
                    # 农场产权边界坐标集存于 类成员变量geo_list[0]
                    self.geo_list.append(geo_str1)
            locations = json.loads(geo_str)
            for loc in locations:
                geo_list.append([loc['lng'], loc['lat']])
            self.log.info('坐标集: %s' % geo_list)
            # 农场产权边界坐标集存于 类成员变量geo_list[0]
            self.geo_list.append(geo_str)

        # distance = 0.022700
        # p0 = json.dumps({"lng": (rand_lng + distance), "lat": (rand_lat + distance)})
        # p1 = json.dumps({"lng": (rand_lng + distance), "lat": (rand_lat - distance)})
        # p2 = json.dumps({"lng": (rand_lng - distance), "lat": (rand_lat - distance)})
        # p3 = json.dumps({"lng": (rand_lng - distance), "lat": (rand_lat + distance)})
        # geo_str = '[ %s, %s, %s, %s, %s ]' % (p0, p1, p2, p3, p0)
        # locations = json.loads(geo_str)
        # geo_list = []
        # for loc in locations:
        #     geo_list.append([loc['lng'], loc['lat']])
        # self.log.info('坐标集: %s' % geo_list)
        # # 农场围栏边界坐标集存于 类成员变量geo_list[1]
        # self.geo_list.append(geo_str)

    def random_circuit(self, kind):
        """
        计算线型地标坐标
        :param kind:
        :return:
        """
        farm_region = self.fq.query_farm_region_locations(self.email)
        lng, lat = self.fp.__dispose_data__(json.loads(farm_region.get('locations')))
        centre_lng = (lng[1] - lng[0]) / 2 + lng[0]
        centre_lat = (lat[1] - lat[0]) / 2 + lat[0]
        distance = 0.002500
        if kind == '10160':
            p = [{"lng": (centre_lng + distance * i), "lat": (centre_lat + distance * i)} for i in
                 range(1, 3)]

            p_bl = [{"lng": (p[1].get('lng') + distance * (i / 2)), "lat": (p[1].get('lat') + distance * i)} for i in
                    range(1, 4)]
            p_ul = [{"lng": (p[1].get('lng') + distance * (i / 2)), "lat": (p[1].get('lat') - distance * i)} for i in
                    range(1, 4)]
        if kind == '10170':
            p = [{"lng": (centre_lng - distance * i), "lat": (centre_lat - distance * i)} for i in
                 range(1, 3)]

            p_bl = [{"lng": (p[1].get('lng') - distance * (i / 2)), "lat": (p[1].get('lat') + distance * i)} for i in
                    range(1, 4)]
            p_ul = [{"lng": (p[1].get('lng') - distance * (i / 2)), "lat": (p[1].get('lat') - distance * i)} for i in
                    range(1, 4)]

        if kind == '10220':
            p = [{"lng": (centre_lng), "lat": (centre_lat - distance * i)} for i in
                 range(1, 3)]

            p_bl = [{"lng": (p[1].get('lng') - distance * (i / 2)), "lat": (p[1].get('lat') - distance * i)} for i in
                    range(1, 4)]
            p_ul = [{"lng": (p[1].get('lng') + distance * (i / 2)), "lat": (p[1].get('lat') - distance * i)} for i in
                    range(1, 4)]

        leafNodes = self.assemble_circuit_location(p, p_bl, p_ul)
        return leafNodes

    def assemble_circuit_location(self, one_circuit, bifurcate_circuit1, bifurcate_circuit2):
        """
        组合线型地标坐标集
        :param one_circuit:
        :param bifurcate_circuit1:
        :param bifurcate_circuit2:
        :return:
        """
        leafNodes_b = self.leafNodes.copy()
        leafNodes_u = self.leafNodes.copy()
        leafNodes = {}
        pl = [i for i in range(3)]
        pl.sort(reverse=True)
        for i in pl:
            leafNodes_p_bl = self.leafNodes.copy()
            leafNodes_p_ul = self.leafNodes.copy()
            if i == 2:
                leafNodes_p_bl['branchNode'] = True
            leafNodes_p_bl['location'] = bifurcate_circuit1[i]
            leafNodes_p_ul['location'] = bifurcate_circuit2[i]
            if i < 2:
                leafNodes_p_bl['leafNodes'] = leafNodes_b
                leafNodes_p_ul['leafNodes'] = leafNodes_u
            leafNodes_b = leafNodes_p_bl
            leafNodes_u = leafNodes_p_ul

        for i in pl:
            if i < pl[0]:
                leafNodes1 = self.leafNodes.copy()
                leafNodes1['location'] = one_circuit[i]
                if i == 1:
                    leafNodes1['leafNodes'] = [leafNodes_p_bl, leafNodes_p_ul]
                if i == 0:
                    leafNodes1['leafNodes'] = leafNodes
                leafNodes = leafNodes1
        leafNodes = json.dumps(leafNodes)
        self.log.info(leafNodes)
        return leafNodes

    def random_mark_point(self):
        """
        生成矩形农场内随机经纬度
        :param geo_json_list:
        :return:
        """
        lng_list = []
        lat_list = []
        if self.geo_list == []:
            farm_info = self.fq.query_default_farm(self.email)[0]
            self.geo_list.append(farm_info.get('locations'))
        for loc in json.loads(self.geo_list[0]):
            lng_list.append(loc['lng'])
            lat_list.append(loc['lat'])
        self.log.info('lng最小值%f' % min(lng_list))
        self.log.info('lat最小值%f' % min(lat_list))
        return {"lng": uniform(min(lng_list), max(lng_list)), "lat": uniform(min(lat_list), max(lat_list))}

    def add_farm(self, lat=None, lng=None):
        """
        mobile添加农场
        :return:
        """
        self.random_rectangle(lat, lng)
        geo_json = '[{"locations":' + self.geo_list[0] + '}]'
        register = self.ko.mobile_farm_add(name="Dev新测试农场", postcodeId=7,
                                           address="Townsville Airport", lng=146.75082826811467,
                                           lat=-19.250204509949924,
                                           currencyType="CNY",
                                           farmRightAddList=geo_json)
        self.assertEqual(register['status'], "OK")

    def del_farm(self):
        """
        删除农场
        :return:
        """
        user_info = self.fq.query_user_info_by_email(self.email)
        farm_info = self.fq.query_farm_info_by_uid(user_info['id'])
        info = self.ko.mobile_farm_del(farmId=farm_info["id"])
        self.assertEqual(info['status'], "OK")

    def add_region(self):
        """
        添加农场围栏
        :return:
        """
        user_info = self.fq.query_user_info_by_email(self.email)
        farm_info = self.fq.query_farm_info_by_uid(user_info['id'])
        info = self.ko.mobile_farm_region_add(farmId=farm_info["id"], regionType="10010", name="鑫围栏",
                                              perimeter="0.01", area="0.01", colorType="2",
                                              locations=self.geo_list[1],
                                              soilType="3", soilPh="3", remark="鑫围栏备注")
        self.assertEqual(info['status'], "OK")

    def add_forest(self):
        """
        添加农场林区
        :return:
        """
        user_info = self.fq.query_user_info_by_email(self.email)
        farm_info = self.fq.query_farm_info_by_uid(user_info['id'])
        info = self.ko.mobile_farm_region_add(farmId=farm_info["id"], regionType="10020", name="鑫林区",
                                              perimeter="0.01", area="0.01", colorType="2",
                                              locations=self.geo_list[2],
                                              soilType="3", soilPh="3", remark="鑫林区备注")
        self.assertEqual(info['status'], "OK")

    def region_list(self):
        """
        筛选围栏/区域
        :return:
        """
        user_info = self.fq.query_user_info_by_email(self.email)
        farm_info = self.fq.query_farm_info_by_uid(user_info['id'])
        # isNeedFilter: 1: 过滤没有牲畜的围栏; 其它: 不过滤
        info = self.ko.mobile_farm_region_list(farmId=farm_info["id"], types="10010", isNeedFilter=0)
        self.assertEqual(info['status'], "OK")
        return info['content']

    def region_info(self):
        """
        围栏/区域详情
        :return:
        """
        if self.region_list() == []:
            region_id = self.region_list()[0]["id"]
            info = self.ko.mobile_farm_region_get(regionId=region_id)
            self.assertEqual(info['status'], "OK")

    def del_region(self):
        """
        删除围栏/区域
        :return:
        """
        region_ids = self.region_list()
        for region_id in region_ids:
            register = self.ko.mobile_farm_region_del(regionId=region_id)
            self.assertEqual(register['status'], "OK")

    def farm_info(self):
        user_info = self.fq.query_user_info_by_email(self.email)
        farm_info = self.fq.query_farm_info_by_uid(user_info['id'])
        info = self.ko.mobile_farm_detail(farmId=farm_info["id"])
        self.assertEqual(info['content']['farmName'], farm_info["name"])
        self.assertEqual(info['content']['farmId'], farm_info["id"])
        self.assertEqual(info['content']['currencyType'], farm_info["currency_type"])
        self.assertEqual(info['content']['rightArea'], farm_info["right_area"])

    def add_random_landmark(self):
        """
        新增随机地标(除去围栏林区)
        :return:
        """
        rand_category = self.category[randint(2, len(self.category) - 1)]
        for k in rand_category:
            self.log.info("将添加 %s 大类" % k)
            rand_cate = rand_category[k]
            rand_kind = self.kinds[k][randint(0, len(self.kinds[k]) - 1)]
            for r in rand_kind:
                self.log.info("将添加 %s 小类" % r)
                kind = rand_kind[r]
                user_info = self.fq.query_user_info_by_email(self.email)
                farm_info = self.fq.query_farm_info_by_uid(user_info['id'])
                region_id = self.region_list()[0]["id"]
                info = self.ko.mobile_landmark_add(farmId=farm_info["id"], regionId=region_id, type1=rand_cate,
                                                   type2=kind, name="自动化%s" % r, buildDate=None, buildPrice=None,
                                                   remark=None, length=None, imageList=None,
                                                   locations=json.dumps(self.random_mark_point()))
                self.assertEqual(info['status'], "OK")

    def add_all_landmark(self):
        """
        新增随机地标(除去围栏林区)
        :return:
        """
        farm_info = self.fq.query_default_farm(self.email)[0]
        # region_id = self.region_list()[0]["id"]
        for cate_index in range(2, len(self.category)):
            for cate_key in self.category[cate_index]:
                self.log.info("将添加 %s 大类" % cate_key)
                cate_id = self.category[cate_index][cate_key]
                self.log.info("将添加 大类编号 type1: %s" % cate_id)
                for kind_dict in self.kinds[cate_key]:
                    for k in kind_dict:
                        self.log.info("将添加 %s 小类" % k)
                        self.log.info("将添加 小类编号 type2: %s" % kind_dict[k])
                        locations = json.dumps(self.random_mark_point())
                        length = None
                        buildDate = time.strftime("%Y-%m-%d", time.localtime())
                        buildPrice = randint(900000, 99999999)
                        if kind_dict[k] in ('10220', '10170', '10160'):
                            locations = self.random_circuit(kind_dict[k])
                            length = 9865.98
                        info = self.ko.mobile_landmark_add(farmId=farm_info["farm_id"], regionId=None, type1=cate_id,
                                                           type2=kind_dict[k], name="自动化%s" % k,
                                                           buildDate=buildDate, buildPrice=buildPrice,
                                                           remark="这是测试%s" % k, length=length, imageList=None,
                                                           locations=locations)
                        self.assertEqual(info['status'], "OK")

    def landmark_list(self):
        """
        筛选地标列表
        :return:
        """
        user_info = self.fq.query_user_info_by_email(self.email)
        farm_info = self.fq.query_farm_info_by_uid(user_info['id'])
        info = self.ko.mobile_landmark_list(farmId=farm_info["id"], types=None)
        self.assertEqual(info['status'], "OK")
        return info['content']

    def del_latest_landmark(self):
        """
        删除最新的地标
        :return:
        """
        landmark_ids = self.landmark_list()
        for landmark_id in landmark_ids:
            info = self.ko.mobile_landmark_del(landmarkId=landmark_id)
            self.assertEqual(info['status'], "OK")

    def del_all_landmark(self):
        """
        删除所有地标
        :return:
        """
        landmarks = self.landmark_list()
        for landmark in landmarks:
            info = self.ko.mobile_landmark_del(landmarkId=landmark["id"])
            self.assertEqual(info['status'], "OK")

    def dispose_cattle_data(self):
        """
        处理查询牲畜类型的数据,返回字典
        :return:
        """
        cattle_data = self.fq.query_cattle_config()
        cattle_dict = {}
        for cattle_type in cattle_data:
            code = cattle_type.get('code')
            if cattle_dict == {}:
                cattle_dict[code] = []
            elif cattle_type.get('code') not in cattle_dict.keys():
                cattle_dict[code] = []
            del cattle_type['code']
            cattle_dict[code].append(cattle_type)
        return cattle_dict

    def device_add(self, startDevEui=None, endDevEui=None):
        """
        添加设备(可批量添加)
        当不传值时,自动查询10个可绑定的设备返回,如果查询结果不足10个,调用接口添加补齐10个,再重新查询一遍
        当有传参时,根据传参添加设备编号,并查询查询10个可绑定的设备返回
        :return:
        """
        if startDevEui is None:
            productModelId = choice([3, 5])
            device_euilist = self.fq.query_device_eui()
            if len(device_euilist) < 10:
                if productModelId == 5:
                    device_eui = self.fq.query_device_eui_one(comparison='<')
                    startDevEui = int(device_eui.get('device_eui')) + 1
                    endDevEui = int(device_eui.get('device_eui')) + 10 - len(device_euilist)
                if productModelId == 3:
                    device_eui = self.fq.query_device_eui_one(comparison='>')
                    startDevEui = int(device_eui.get('device_eui')) + 1
                    endDevEui = int(device_eui.get('device_eui')) + 10 - len(device_euilist)

                self.mgr.admin_device_add(startDevEui=startDevEui, endDevEui=endDevEui, productModelId=productModelId,
                                          platFormId=1, remark=None)
                device_euilist = self.fq.query_device_eui()
        else:
            productModelId = 3 if len(startDevEui) > 8 else 5
            self.mgr.admin_device_add(startDevEui=startDevEui, endDevEui=endDevEui, productModelId=productModelId,
                                      platFormId=1, remark=None)
            device_euilist = self.fq.query_device_eui()
        return device_euilist

    def __new_cattle_add_bind__(self, farmId, regionId, earTagId, deviceId):
        """
        添加牲畜并绑定,
        :param farmId: 农场ID
        :param regionId: 围栏ID
        :param earTagId: 牲畜姓名
        :param deviceId: 设备ID
        :return:
        """
        cattle_typr_dict = self.dispose_cattle_data()
        cattle_type = choice(cattle_typr_dict.get('10004'))
        varietyId = choice(cattle_typr_dict.get('10003'))
        labelId = choice(cattle_typr_dict.get('10004'))

        sourceType = choice([{'key': 1, 'value': '采购'}, {'key': 2, 'value': '.生产'}, {'key': 3, 'value': '其他'}])

        isHorn = choice([{'key': 0, 'value': '否'}, {'key': 1, 'value': '.是'}])

        bodyColor = choice([{'key': 1, 'value': '黄色'}, {'key': 2, 'value': '.褐色'}, {'key': 3, 'value': '草白色'},
                            {'key': 4, 'value': '黑白花色'}, {'key': 5, 'value': '黄白花色'}])
        # year = datetime.datetime.now().year
        # month = datetime.datetime.now().month
        # day = datetime.datetime.now().day
        # birthDate = str(year) + '-' + str(month) + '-' + str(day)
        now_birthDate = int(time.time())
        # birthDate = now_birthDate - (15 * 24 * 60 * 60)*1000
        birthDate = now_birthDate - (15 * 24 * 60 * 60) * 1000
        self.log.info(
            "farmId=%s, regionId=%s, type=%s,varietyId=%s, labelId=%s, birthDate=None,earTagId=%s, "
            "sourceType=%s, gnlis=None, pnlis=None,mnlis=None, supplier=None, supplierPic=None, nvdNo=None,"
            "bodyColor=%s, isHorn=%s, remark=None, imgs=None,deviceId=deviceId" % (
                farmId, regionId, cattle_type.get('value'), sourceType.get('value'), labelId.get('value'),
                earTagId, sourceType.get('value'), bodyColor.get('value'), isHorn.get('value')))
        self.log.info('新增绑定牲畜')
        self.ko.mobile_cattle_add_bind(farmId=farmId, regionId=regionId, type=cattle_type.get('key'),
                                       varietyId=varietyId.get('key'), birthDate=birthDate,
                                       cattleName=now_birthDate, sourceType=sourceType.get('key'), nlis=now_birthDate,
                                       pid=None,
                                       mid=None, supplier=None, supplierPic=None, nvdNo=None,
                                       bodyColor=bodyColor.get('key'), isHorn=isHorn.get('key'), remark=None, imgs=None,
                                       deviceId=deviceId, visionNum=int(now_birthDate / 10000))

    def new_cattle_add_bind(self):
        """
        查询数据库当天新增且未绑定的设备
        通过邮箱查询用户已加入的农场和围栏
        遍历所有的设备ID,随机插入用户已的某一个农场
        :return:
        """
        global device_dict
        device_dict = self.device_add()
        farm_lit = self.fq.query_farm_and_region(self.email)
        if device_dict == () or farm_lit == ():
            self.log.info("device_dict或farm_lit为空")
            return
        for i in device_dict:
            farm_dict = choice(farm_lit)
            self.log.info("开始在\"%s\"农场的\"%s\"围栏添加并绑定牲畜" % (farm_dict.get('farm_name'), farm_dict.get('region_name')))
            self.__new_cattle_add_bind__(farmId=farm_dict.get('farm_id'), regionId=farm_dict.get('region_id'),
                                         earTagId=i.get('device_eui'), deviceId=i.get('device_eui'))

    def cattle_list(self):
        """
        获取牲畜档案列表
        :return:
        """
        farm_list = self.fq.query_farm_and_region(self.email)
        for i in farm_list:
            farmId = i.get('farm_id')
            self.log.info("--------------------获取牲畜档案列表--------------------")
            self.ko.mobile_cattle_list(regionId=None, type=None, varietyId=None, labelId=None, pn=10, ps=10,
                                       farmId=farmId, orderType='CREATE_DESC', isBindDevice=None, searchName=None)

    def cattle_detail(self):
        """
        查看牲畜详情
        :return:
        """
        cattleId_dict = self.fq.query_cattle_id(self.email)
        for i in cattleId_dict:
            cattleId = i.get('id')
            self.log.info("--------------------查看牲畜详情--------------------")
            self.ko.mobile_cattle_detail(cattleId=cattleId)

    def cattle_update(self):
        """
        编辑牲畜
        :return:
        """
        cattle_typr_dict = self.dispose_cattle_data()
        cattle_type = choice(cattle_typr_dict.get('10002'))
        varietyId = choice(cattle_typr_dict.get('10003'))
        labelId = choice(cattle_typr_dict.get('10004'))

        sourceType = choice([{'key': 1, 'value': '采购'}, {'key': 2, 'value': '生产'}, {'key': 3, 'value': '其他'}])

        isHorn = choice([{'key': 0, 'value': '否'}, {'key': 1, 'value': '是'}])

        bodyColor = choice([{'key': 1, 'value': '黄色'}, {'key': 2, 'value': '褐色'}, {'key': 3, 'value': '草白色'},
                            {'key': 4, 'value': '黑白花色'}, {'key': 5, 'value': '黄白花色'}])

        year = datetime.datetime.now().year
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        birthDate = str(year) + '-' + str(month) + '-' + str(day)
        cattleId_dict = self.fq.query_cattle_id(self.email)
        farm_dict = self.fq.query_farm_and_region(self.email)

        for i in cattleId_dict:
            cattleId = i.get('id')
            farmId = choice(farm_dict)
            earTagId = str(i)
            self.log.info("--------------------编辑牲畜--------------------")
            self.ko.mobile_cattle_update(id=cattleId, farmId=farmId.get('farm_id'), regionId=farmId.get('region_id'),
                                         type=cattle_type.get('key'), varietyId=varietyId.get('key'),
                                         labelId=labelId.get('key'), birthDate=birthDate, earTagId=earTagId,
                                         sourceType=sourceType.get('key'), gnlis=None, pnlis=None, mnlis=None,
                                         supplier=None, supplierPic=None, nvdNo=None, bodyColor=bodyColor.get('key'),
                                         isHorn=isHorn.get('key'), remark=None, imgs=None)

    def cattle_unbind(self):
        """
        解绑牲畜
        :return:
        """
        cattleId_dict = self.fq.query_cattle_bind_id(self.email)
        for i in cattleId_dict:
            farmId = i.get('farm_id')
            cattleId = i.get('id')
            deviceId = i.get('device_id')
            self.log.info("--------------------解绑牲畜--------------------")
            self.ko.mobile_cattle_unbind(farmId=farmId, cattleId=cattleId, deviceId=deviceId)

    def cattle_del(self):
        """
        删除用户所有牲畜
        :return:
        """
        cattleId_dict = self.fq.query_cattle_id(self.email)
        for i in cattleId_dict:
            cattleId = i.get('id')
            self.log.info("--------------------删除用户所有牲畜--------------------")
            self.ko.mobile_cattle_del(cattleId=cattleId)

    def mobile_user_invite_search(self):
        """
        搜索站内成员
        :return:
        """
        join_farm_dict = self.ko.mobile_farm_user_list_by_user()
        join_farm_list = join_farm_dict.get('content')
        if join_farm_list == [] or join_farm_list is None:
            self.log.info("用户未加入农场")
            return
        if join_farm_list != []:
            farm_id = join_farm_list[0].get('farmId')
            self.ko.mobile_user_invite_search(farmId=farm_id, account='xiujuan.chen@worldfarm.com')

    def mobile_user_invite_inner_invite(self):
        """
        发送站内邀请（此处被邀请ID为固定的用户id）
        :return:
        """
        join_farm_dict = self.ko.mobile_farm_user_list_by_user()
        join_farm_list = join_farm_dict.get('content')
        if join_farm_list == [] or join_farm_list is None:
            self.log.info("用户未加入农场")
            return
        if join_farm_list != []:
            farm_id = join_farm_list[0].get('farmId')
            userId = '83'
            self.log.info('--------------------发送站内邀请,邀请用户邮箱为“xiujuan.chen@worldfarm.com”--------------------')
            self.ko.mobile_user_invite_inner_invite(farmId=farm_id, inviteeId=83)

    def mobile_user_invite_list(self):
        """
        已邀请列表（当前农场的已邀请列表）
        :return:
        """
        join_farm_dict = self.ko.mobile_farm_user_list_by_user()
        join_farm_list = join_farm_dict.get('content')
        if join_farm_list == [] or join_farm_list is None:
            self.log.info("用户未加入农场")
            return
        if join_farm_list != []:
            farm_id = join_farm_list[0].get('farmId')
            self.log.info('--------------------发送站内邀请--------------------')
            self.ko.mobile_user_invite_list(farmId=farm_id)

    def mobile_user_invite_inner_invite_info(self):
        """
        站内邀请信息（当前农场的已邀请信息）
        :return:
        """
        join_farm_dict = self.ko.mobile_farm_user_list_by_user()
        join_farm_list = join_farm_dict.get('content')
        user_info = self.fq.query_user_info_by_email(self.email)
        user_id = user_info.get('id')
        if join_farm_list == [] or join_farm_list is None:
            self.log.info("用户未加入农场")
            return
        if join_farm_list != []:
            farm_id = join_farm_list[0].get('farmId')
            inviteId = self.fq.query_invite_info(farm_id=farm_id, creator_id=user_id)
            for i in inviteId:
                self.log.info('--------------------查看站内邀请信息--------------------')
                self.ko.mobile_user_invite_inner_invite_info(inviteId=i.get('id'))

    def mobile_user_invite_inner_accept(self):
        """
        接收站内邀请
        :return:
        """
        join_farm_dict = self.ko.mobile_farm_user_list_by_user()
        join_farm_list = join_farm_dict.get('content')
        user_info = self.fq.query_user_info_by_email(self.email)
        user_id = user_info.get('id')
        if join_farm_list == [] or join_farm_list is None:
            self.log.info("用户未加入农场")
            return
        if join_farm_list != []:
            farm_id = join_farm_list[0].get('farmId')
            inviteId = self.fq.query_invite_info(farm_id=farm_id, creator_id=user_id)
            self.email = 'xiujuan.chen@worldfarm.com'

            user = UserSession()
            for i in inviteId:
                self.log.info('--------------------接收站内邀请--------------------')
                self.ko.mobile_user_invite_inner_accept(inviteId=i.get('id'))

    def mobile_farm_user_list_by_user(self):
        """
        获取当前用户所在农场的成员列表
        :return:
        """
        self.log.info('--------------------获取当前用户所在农场的成员列表--------------------')
        self.ko.mobile_farm_user_list_by_user()

    def mobile_farm_user_list_by_farm(self):
        """
        获取指定农场的成员列表(此处获取用户所在农场id正序第一个农场)
        :return:
        """
        join_farm_dict = self.ko.mobile_farm_user_list_by_user()
        join_farm_list = join_farm_dict.get('content')
        if join_farm_list == [] or join_farm_list is None:
            self.log.info("用户未加入农场")
            return
        if join_farm_list != []:
            self.log.info('--------------------获取用户所在农场id正序第一个农场--------------------')
            farm_id = join_farm_list[0].get('farmId')
            self.log.info('--------------------通过农场id查询农场成员列表--------------------')
            self.ko.mobile_farm_user_list_by_farm(farmId=farm_id)
            return

    def mobile_farm_user_roles(self):
        """
        获取可分配的角色列表(此处获取用户所在农场id正序第一个农场)
        :return:
        """
        join_farm_dict = self.ko.mobile_farm_user_list_by_user()
        join_farm_list = join_farm_dict.get('content')
        if join_farm_list == [] or join_farm_list is None:
            self.log.info("用户未加入农场")
            return
        if join_farm_list != []:
            self.log.info('--------------------获取用户所在农场id正序第一个农场--------------------')
            farm_id = join_farm_list[0].get('farmId')
            self.log.info('--------------------通过农场id查询可分配的角色列表--------------------')
            self.ko.mobile_farm_user_roles(farmId=farm_id)
            return

    def mobile_user_role_set_role(self):
        """
        设置成员角色(当前账号为农场主，所在农场id正序第一个农场，设置普通人员为管理员)
        :return:
        """
        join_farm_dict = self.ko.mobile_farm_user_list_by_user()
        join_farm_list = join_farm_dict.get('content')
        if join_farm_list == [] or join_farm_list is None:
            self.log.info("用户未加入农场")
            return
        if join_farm_list != []:
            farm_id = join_farm_list[0].get('farmId')
            userId_list = self.fq.query_role_info_buy_farm_id(farm_id=farm_id)
            if userId_list == ():
                self.log.info('--------------------当前农场无普通人员--------------------')
                for i in userId_list:
                    self.log.info('--------------------设置当前农场普通人员用户为管理人员用户--------------------')
                    self.ko.mobile_user_role_set_role(farmId=farm_id, userId=i.get('user_id'), roleId=2)

    def mobile_farm_user_detail(self):
        """
        人员详情(此处获取用户所在农场id正序第一个农场的成员详情)
        :return:
        """
        join_farm_dict = self.ko.mobile_farm_user_list_by_user()
        join_farm_list = join_farm_dict.get('content')
        if join_farm_list == [] or join_farm_list is None:
            self.log.info("用户未加入农场")
            return
        if join_farm_list != []:
            farm_id = join_farm_list[0].get('farmId')
            userId_list = self.fq.query_role_id_buy_farm_id(farm_id=farm_id)
            for i in userId_list:
                self.log.info('--------------------查看当前农场成员信息详情--------------------')
                self.ko.mobile_farm_user_detail(farmId=farm_id, userId=i.get('user_id'))

    def mobile_farm_user_remove(self):
        """
        移除人员(此处移除用户所在农场id正序第一个农场非农场主成员)
        :return:
        """
        join_farm_dict = self.ko.mobile_farm_user_list_by_user()
        join_farm_list = join_farm_dict.get('content')
        if join_farm_list == [] or join_farm_list is None:
            self.log.info("用户未加入农场")
            return
        if join_farm_list != []:
            farm_id = join_farm_list[0].get('farmId')
            userId_list = self.fq.query_role_not_farmer_id_buy_farm_id(farm_id=farm_id)
            for i in userId_list:
                self.log.info('--------------------移除当前农场非农场主身份的农场成员--------------------')
                self.ko.mobile_farm_user_remove(farmId=farm_id, userId=i.get('user_id'))

    # def test_smoke_test(self):
        # 此处由于农场随机范围, 不能随意调换执行顺序
        # self.add_farm(lat=30.688446297643623, lng=104.17468451946894)
        # self.add_region()
        # self.add_forest()
        # self.farm_info()
        # self.region_list()
        # self.region_info()
        # self.add_all_landmark()
        # self.device_add()
        # self.new_cattle_add_bind()
        # self.cattle_list()
        # self.cattle_detail()
        # self.cattle_update()
        # self.cattle_unbind()
        # self.cattle_del()
        # self.add_random_landmark()
        # self.landmark_list()
        # self.del_latest_landmark()
        # self.del_all_landmark()
        # self.del_region()
        # self.del_farm()
        # self.mobile_user_invite_search()
        # self.mobile_user_invite_inner_invite()
        # self.mobile_user_invite_list()
        # self.mobile_user_invite_inner_invite_info()
        # self.mobile_user_invite_inner_accept()
        # self.mobile_farm_user_list_by_user()
        # self.mobile_farm_user_list_by_farm()
        # self.mobile_farm_user_roles()
        # self.mobile_user_role_set_role()
        # self.mobile_farm_user_detail()
        # self.mobile_farm_user_remove()


if __name__ == '__main__':
    m = Main()
