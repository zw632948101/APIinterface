#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Xiu juanchen'
__date__ = '2018/8/20'
集中测试  牲畜档案
"""
import unittest
import random
import time
from random import choice, sample
from testcase.worldFarm import testCase,CattleManage


class Main(testCase):

    fq = CattleManage()

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

    def test3011(self):
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

    def test_mobile_cattle_bind_semaphore_repetition(self):
        """
        绑定信号放大器(挂树母耳标)输入重复的设备ID
        :return:
        """
        device = choice(self.fq.query_may_device_update(self.email))
        info = self.ka.mobile_cattle_bind_semaphore(farmId=device.get('farm_id'),
                                                    deviceId=device.get('device_eui'))
        self.assertEqual(info['errorMsg'], "设备已绑定,请不要重复绑定")

    def test_v126_mobile_cattle_search_detail(self):
        """
        牲畜详情 update V 1.2.6
        :return:
        """
        cattle_list = self.fq.query_cattle_detail_buy_email(self.email)
        if len(cattle_list) > 0:
            cattle_id = cattle_list[0]["id"]
            register = self.ka.v126_mobile_cattle_search_detail(cattleId=cattle_id)
            cattle_detail_list = self.fq.query_cattle_detail_buy_cattle_id(cattle_id=cattle_id)
            birth_date = int(time.mktime(time.strptime(cattle_detail_list[0]["birth_date"],
                                                       "%Y-%m-%d %H:%M:%S")) * 1000)
            self.assertEqual(register["content"]["birthDate"], birth_date)
            self.assertEqual(register["content"]["cattleName"], cattle_detail_list[0]["cattle_name"])
        else:
            self.log.info("当前账号的默认农场下暂无牲畜！")

    def test_mobile_cattle_rebind(self):
        """
        解绑后再次绑定设备
        :return:
        """
        cattleid = choice(self.fq.query_all_farm_not_bind_cattle(self.email))
        deviceEui = choice(self.fq.query_device_eui_id()).get('device_eui')
        info = self.ka.mobile_cattle_rebind(id=cattleid.get('id'), deviceId=deviceEui)
        self.assertEqual(info["status"], "OK")
        cattleinfo = self.fq.query_cattle_detail_buy_cattle_id(cattle_id=cattleid.get('id'))[0]
        self.assertEqual(deviceEui, cattleinfo.get('device_id'))

    def test_mobile_cattle_rich_scan(self):
        """
        扫一扫
        :return:
        """
        deviceid = choice(self.fq.query_device_eui_id()).get('device_eui')
        info = self.ka.mobile_cattle_rich_scan(deviceEui=deviceid)
        self.assertEqual(info["status"], "OK")

    def test_mobile_cattle_unbind(self):
        """
        解绑设备

        :return:
        """
        cfrd = choice(self.fq.query_default_farm_cattle_info_list(self.email))
        register = self.ka.mobile_cattle_unbind(farmId=cfrd.get('farm_id'), cattleId=cfrd.get('id'),
                                                deviceId=[cfrd.get('device_id')])
        cfrd = self.fq.query_cattle_farm_region_id(cattleid=cfrd.get('id'))[0]
        self.assertEqual(register['status'], 'OK')
        self.assertEqual(cfrd.get('device_id'), None)

    def test_mobile_cattle_change_fence(self):
        """
        更换围栏
        1.2.4更改
        V1.2.5 更改
        :return:
        """
        # 获取当前农场的围栏信息
        farm_region_id = self.fq.query_farm_id_and_region_id(self.email)
        farm_fegion = random.choices(farm_region_id)[0]

        # 获取当前农场的全部牲畜，并随机取其中10条牲畜的ID
        weaning_detail = self.fq.query_cattle_farm_region_id()
        cattleIds = self.tool.data_assemble('id', weaning_detail, 10)

        register = self.ka.mobile_cattle_change_fence(cattleIds=cattleIds,
                                                      farmId=farm_fegion.get('farm_id'),
                                                      regionId=farm_fegion.get('region_id'))
        self.assertEqual(register['status'], 'OK')

    def cattle_add_bind_info(self):
        """
        新增编辑牲畜数据处理
        :return:
        """
        # 获取config配置表数据
        cattle_typr_dict = self.dispose_cattle_data()
        cattle_type = choice(cattle_typr_dict.get('10004'))
        varietyId = choice(cattle_typr_dict.get('10003'))
        blood = choice(cattle_typr_dict.get('10011'))
        farm_info = choice(self.fq.query_only_default_farm_id(self.email))
        farmId = farm_info.get('farm_id')
        regionId = farm_info.get('region_id')
        sourceType = choice([{'key': 1, 'value': '采购'}, {'key': 2, 'value': '.生产'}, {'key': 3, 'value': '其他'}])

        # blood = choice([{'key': 1, 'value': '纯血'}, {'key': 2, 'value': '混血'}, {'key': 3, 'value': '纯种'}])
        level = choice(cattle_typr_dict.get('10012'))
        level = 1004

        isHorn = choice([{'key': 0, 'value': '否'}, {'key': 1, 'value': '是'}])

        bodyColor = choice([{'key': 1, 'value': '黄色'}, {'key': 2, 'value': '.褐色'}, {'key': 3, 'value': '草白色'},
                            {'key': 4, 'value': '黑白花色'}, {'key': 5, 'value': '黄白花色'}])
        now_birthDate = int(time.time())
        # birthDate = now_birthDate - (15 * 24 * 60 * 60)*1000
        birthDate = now_birthDate - (15 * 24 * 60 * 60) * 1000
        # birthDate = random.randint(1288333211, now_birthDate) * 1000
        cow_list_sql = self.fq.query_cow_cattle_id_list(email=self.email)
        if len(cow_list_sql) > 0:
            cattle = choice(cow_list_sql)
            mid = cattle.get("id")
            mname = cattle.get("cattle_name")
        else:
            mid = mname = None
        bull_list_sql = self.fq.query_all_bull_id_buy_email(email=self.email)
        if len(bull_list_sql) > 0:
            bull_cattle = choice(bull_list_sql)
            pid = bull_cattle.get("id")
            pname = bull_cattle.get("cattle_name")
        else:
            pid = pname = None
        # 判断来源是否为购买，如果是购买就填充数据，生产全部置为None
        if sourceType.get('key') == 1:
            supplier = '测试供应商'
            supplierPic = nvdNo = '12345678'
            sourceRemark = '这是一个测试来源'
            buyTime = str(now_birthDate)
            buyPrice = random.randint(2000, 9999)
            buyWeight = random.randint(200, 2000)
        else:
            supplier = supplierPic = nvdNo = sourceRemark = buyTime = buyPrice = buyWeight = None
        # device_id_sql = self.fq.query_device_eui_id()
        # if len(device_id_sql) != 0:
        #     device_id = device_id_sql[0]["device_eui"]
        #     if len(device_id) < 6:
        #         device_id = None
        # else:
        #     device_id = None
        device_id = None
        return cattle_type, blood, level, varietyId, farmId, regionId, sourceType, isHorn, bodyColor, now_birthDate, birthDate, mid, mname, pid, pname, supplier, supplierPic, nvdNo, sourceRemark, buyTime, buyWeight, device_id

    def test_v126_mobile_cattle_add_bind(self):
        """
        移动端-牲畜档案-新增绑定牲畜 v1.2.4
        V1.2.6修改
        :return:
        """
        cattle_type, blood, level, varietyId, farmId, regionId, sourceType, isHorn, bodyColor, now_birthDate, birthDate, mid, mname, pid, pname, supplier, supplierPic, nvdNo, sourceRemark, buyTime, buyWeight, device_id = self.cattle_add_bind_info()
        remark = '这是一个接口测试'
        info = self.ka.v126_mobile_cattle_add_bind(farmId=farmId, regionId=regionId,
                                                   type=cattle_type.get('key'),
                                                   blood=blood.get('key'), level=level,
                                                   varietyId=varietyId.get('key'), birthDate=birthDate,
                                                   cattleName=now_birthDate, sourceType=sourceType.get('key'),
                                                   nlis=now_birthDate, pid=pid, mid=mid, pname=pname,
                                                   mname=mname, supplier=supplier, supplierPic=supplierPic,
                                                   nvdNo=nvdNo, bodyColor=bodyColor.get('key'),
                                                   isHorn=isHorn.get('key'), remark=remark, imgs=None,
                                                   deviceId=device_id,
                                                   visionNum=int(now_birthDate), sourceRemark=sourceRemark,
                                                   buyTime=buyTime, buyWeight=buyWeight)
        if info.get("status") == "ERROR":
            self.log.info(info.get("errorMsg"))
            return
        cattleinfo = self.fq.query_new_cattle_info(farmid=farmId, regionid=regionId, cattlename=now_birthDate,
                                                   nlis=now_birthDate)
        self.assertEqual(info.get('status'), 'OK')
        self.assertEqual(info['content']["id"], cattleinfo.get('id'))
        self.assertEqual(cattleinfo.get('variety_id'), varietyId.get('key'))
        self.assertEqual(cattleinfo.get('blood'), str(blood.get('key')))
        self.assertEqual(cattleinfo.get('level'), str(level))
        self.assertEqual(cattleinfo.get('vision_num'), str(int(now_birthDate)))
        self.assertEqual(cattleinfo.get('source_type'), sourceType.get('key'))
        self.assertEqual(cattleinfo.get('source_remark'), sourceRemark)
        self.assertEqual(cattleinfo.get('buy_weight'), buyWeight)
        self.assertEqual(cattleinfo.get('supplier'), supplier)
        self.assertEqual(cattleinfo.get('supplier_pic'), supplierPic)
        self.assertEqual(cattleinfo.get('nvd_no'), nvdNo)
        self.assertEqual(cattleinfo.get('body_color'), bodyColor.get('key'))
        self.assertEqual(cattleinfo.get('is_horn'), isHorn.get('key'))
        self.assertEqual(cattleinfo.get('remark'), remark)

    def test_v126_mobile_cattle_update(self):
        """
        移动端-牲畜档案-编辑牲畜 v1.2.4
        V1.2.6 修改
        :return:
        """

        cattle_type, blood, level, varietyId, farmId, regionId, sourceType, isHorn, bodyColor, now_birthDate, birthDate, mid, mname, pid, pname, supplier, supplierPic, nvdNo, sourceRemark, buyTime, buyWeight, device_id = self.cattle_add_bind_info()
        remark = '这是一个接口测试'
        sql_cattle_id = self.fq.query_all_bull_id_buy_email(email=self.email)
        cattleid = choice(sql_cattle_id).get('id')
        info = self.ka.v126_mobile_cattle_update(id=cattleid, farmId=farmId, regionId=regionId,
                                                 type=cattle_type.get('key'), varietyId=varietyId.get('key'),
                                                 blood=blood.get('key'), level=level,
                                                 birthDate=birthDate, cattleName=now_birthDate,
                                                 sourceType=sourceType.get('key'), nlis=now_birthDate, pid=pid,
                                                 mid=mid, pname=pname, mname=mname,
                                                 supplier=supplier, supplierPic=supplierPic,
                                                 nvdNo=nvdNo, bodyColor=bodyColor.get('key'),
                                                 isHorn=isHorn.get('key'), remark=remark, imgs=None,
                                                 visionNum=int(now_birthDate), sourceRemark=sourceRemark,
                                                 buyTime=buyTime, buyWeight=buyWeight)
        if info.get("status") == "ERROR":
            self.log.info(info.get("errorMsg"))
            return
        cattleinfo = self.fq.query_cattle_detail_buy_cattle_id(cattleid)[0]
        self.assertEqual(info.get('status'), 'OK')
        self.assertEqual(cattleinfo["variety_id"], varietyId.get('key'))
        self.assertEqual(cattleinfo['blood'], str(blood.get('key')))
        self.assertEqual(cattleinfo['level'], str(level))
        self.assertEqual(cattleinfo.get('vision_num'), str(int(now_birthDate)))
        self.assertEqual(cattleinfo.get('source_type'), sourceType.get('key'))
        self.assertEqual(cattleinfo.get('source_remark'), sourceRemark)
        self.assertEqual(cattleinfo.get('buy_weight'), buyWeight)
        self.assertEqual(cattleinfo.get('supplier'), supplier)
        self.assertEqual(cattleinfo.get('supplier_pic'), supplierPic)
        self.assertEqual(cattleinfo.get('nvd_no'), nvdNo)
        self.assertEqual(cattleinfo.get('body_color'), bodyColor.get('key'))
        self.assertEqual(cattleinfo.get('is_horn'), isHorn.get('key'))
        self.assertEqual(cattleinfo.get('remark'), remark)

    def test_v126_mobile_cattle_search_get_blood_relation(self):
        """
        根据牲畜id查询血缘关系  V1.2.6
        :return:
        """
        cattle_list = self.fq.query_relationship_buy_email(email=self.email)
        cattle_id = cattle_list[0]['id']
        register = self.ka.v126_mobile_cattle_search_get_blood_relation(cattleId=cattle_id)
        m_id = cattle_list[0]['m_id']
        p_id = cattle_list[0]['p_id']
        if m_id is not None:
            m_info = self.fq.query_cattle_detail_buy_cattle_id(m_id)
            gm_info = self.fq.query_cattle_detail_buy_cattle_id(cattle_id=m_id)
            gm_id = gm_info[0]['m_id']
        if p_id is not None:
            p_info = self.fq.query_cattle_detail_buy_cattle_id(p_id)
            gp_info = self.fq.query_cattle_detail_buy_cattle_id(cattle_id=p_id)
            gp_id = gm_info[0]['p_id']
        if len(register['content']['ma']) != 0:
            self.assertEqual(register['content']['ma']['cattleName'], m_info[0]['cattle_name'])
            self.assertEqual(register['content']['ma']['id'], m_id)
            self.assertEqual(register['content']['ma']['nlis'], m_info[0]['nlis'])
            if len(register['content']['ma']['ma']) != 0:
                self.assertEqual(register['content']['ma']['ma']['id'], gm_id)
                self.assertEqual(register['content']['ma']['ma']['cattleName'], gm_info[0]['cattle_name'])
                self.assertEqual(register['content']['ma']['ma']['nlis'], gm_info[0]['nlis'])
        if len(register['content']['pa']) != 0:
            self.assertEqual(register['content']['pa']['cattleName'], p_info[0]['cattle_name'])
            self.assertEqual(register['content']['pa']['id'], p_id)
            self.assertEqual(register['content']['pa']['nlis'], p_info[0]['nlis'])
            if len(register['content']['pa']['pa']) != 0:
                self.assertEqual(register['content']['pa']['pa']['id'], gp_id)
                self.assertEqual(register['content']['pa']['pa']['cattleName'], gp_info[0]['cattle_name'])
                self.assertEqual(register['content']['pa']['pa']['nlis'], gp_info[0]['nlis'])

    def test_mobile_cattle_update_blood(self):
        """
        修改血缘关系  V1.2.6
        :return:
        """
        cattle_list = self.fq.query_relationship_buy_email(email=self.email)
        if not cattle_list:
            self.log.info("该账户下没有牲畜有血缘关系")
            return
        cattle_id = cattle_list[0]['id']
        bull_list = self.fq.query_bull_id_buy_email(email=self.email)

        p_id = None if not bull_list else choice(bull_list).get('id')
        cow_list = self.fq.query_cow_id_buy_email_unbreeding_num(email=self.email)
        m_id = cow_list[0]['id']
        p_name = None
        m_name = None
        self.ka.mobile_cattle_update_blood(cattleId=cattle_id, pid=p_id, mid=m_id,
                                           pname=p_name, mname=m_name)
        cattle_info = self.fq.query_cattle_detail_buy_cattle_id(cattle_id=cattle_id)
        self.assertEqual(p_id, cattle_info[0]['p_id'])
        self.assertEqual(m_id, cattle_info[0]['m_id'])
        self.assertEqual(p_name, cattle_info[0]['p_name'])
        self.assertEqual(m_name, cattle_info[0]['m_name'])

    def test_mobile_cattle_detail_by_device(self):
        """
        移动端-牲畜档案-根据设备编号获取牲畜详情 v1.2.4
        V1.2.5 修改
        :return:
        """
        device_id = choice(self.fq.query_default_farm_cattle_info_list(self.email)).get('device_id')
        info = self.ka.mobile_cattle_search_detail_by_device(device_id)
        self.assertEqual(info["status"], "OK")

    def test_v126_mobile_cattle_detail_by_device(self):
        """
        移动端-牲畜档案-根据设备编号获取牲畜详情 V1.2.6
        :return:
        """
        device_id = choice(self.fq.query_default_farm_cattle_info_list(self.email)).get('device_id')
        info = self.ka.v126_mobile_cattle_search_detail_by_device(device_id)
        self.assertEqual(info["status"], "OK")

    def test_mobile_cattle_search_list(self):
        """
        移动端-牲畜档案-牲畜档案列表 v1.2.4
        :return:
        """
        configdict = self.dispose_cattle_data()
        typelist = self.tool.data_assemble('key', configdict.get('10004'),
                                           random.randint(0, len(configdict.get('10004'))))
        variety_id = self.tool.data_assemble('key', configdict.get('10003'),
                                             random.randint(0, len(configdict.get('10003'))))
        sexId = self.tool.data_assemble('key', configdict.get('10002'),
                                        random.randint(0, len(configdict.get('10002'))))
        level = self.tool.data_assemble('key', configdict.get('10012'),
                                        random.randint(0, len(configdict.get('10012'))))
        stage = [{"10": "待断奶"}, {"20": "发育期"}, {"30": "待交配"}, {"31": "空怀"}, {"32": "流产"}, {"33": "已产犊待交配"},
                 {"40": "已交配"}, {"50": "已怀孕"}, {"60": "已产犊"}]
        stage = sample(stage, random.randint(0, len(stage)))
        stage = [i.keys() for i in stage] if stage else None
        Bind = choice([0, 1, (0, 1), None])  # 是否绑定设备(0.否、1.是)
        farmid = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        regionlist = self.fq.query_farm_region_list(farmid, isNeedFilter=1, isNeedNoPaddock=1)
        regionid = self.tool.data_assemble('region_id', regionlist, random.randint(0, len(regionlist)))
        regionid = [-1 if i == None else i for i in regionid] if regionid else None
        info = self.ka.mobile_cattle_search_list(regionId=regionid, type=typelist, varietyId=variety_id,
                                                 sexId=sexId, farmId=farmid, level=level, stage=stage,
                                                 orderType="CREATE_DESC", isBindDevice=Bind)
        self.assertEqual(info["status"], "OK")
        if info.get('content'):
            cattledata = self.fq.query_farm_all_cattle_list(farmid=farmid, regionid=regionid, varietyid=variety_id,
                                                            type_=typelist, sex=sexId, level=level, stage=stage,
                                                            bind=Bind)
            content = info.get('content')
            for i in range(len(content)):
                self.assertEqual(content[i].get('bodyColor'), cattledata[i].get('body_color'))
                self.assertEqual(content[i].get('cattleName'), cattledata[i].get('cattle_name'))
                self.assertEqual(content[i].get('isHorn'), cattledata[i].get('is_horn'))
                self.assertEqual(content[i].get('nlis'), cattledata[i].get('nlis'))
                self.assertEqual(content[i].get('regionId'), cattledata[i].get('region_id'))
                self.assertEqual(content[i].get('remark'), cattledata[i].get('remark'))
                self.assertEqual(content[i].get('sex'), cattledata[i].get('sex'))
                self.assertEqual(content[i].get('sourceType'), cattledata[i].get('source_type'))
                self.assertEqual(content[i].get('type'), cattledata[i].get('type'))
                self.assertEqual(content[i].get('varietyId'), cattledata[i].get('variety_id'))
                self.assertEqual(content[i].get('visionNum'), cattledata[i].get('vision_num'))

    def test_mobile_farm_user_detail(self):
        """
        移动端-农场成员-人员详情 v1.2.4
        :return:
        """
        farmuserinfo = self.fq.query_user_create_farm_all_user_id(self.email)
        if not farmuserinfo:
            self.log.info("当前账户：%s 创建的农场没有添加人员" % self.email)
            return
        farmuser = choice(farmuserinfo)
        farm_id = farmuser.get('farm_id')
        user_id = farmuser.get('user_id')
        info = self.ka.mobile_farm_user_detail(farm_id, user_id)
        self.assertEqual(info["status"], "OK")

    def test_mobile_farm_user_list_by_farm(self):
        """
        移动端-农场成员-获取指定农场的成员列表 v1.2.4
        :return:
        """
        farm_id = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        info = self.ka.mobile_farm_user_list_by_farm(farm_id)
        self.assertEqual(info["status"], "OK")

    def test_mobile_farm_user_list_by_user(self):
        """
        移动端-农场成员-获取当前用户所在农场的所有成员列表 v1.2.4
        :return:
        """
        info = self.ka.mobile_farm_user_list_by_user()
        self.assertEqual(info["status"], "OK")

    def test_mobile_farm_detail(self):
        """
        移动端-农场管理-农场详情
        :return:
        """
        farm_id = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        info = self.ka.mobile_farm_detail(farm_id)
        self.assertEqual(info["status"], "OK")

    def test_mobile_cattle_whether_plan(self):
        """
        移动端-牲畜档案-根据牲畜Id查询是否有放牧计划【v1.2.5 】
        :return:
        """
        cattle_list = self.fq.query_default_farm_cattle_info_list(self.email)
        cattleids = self.tool.data_assemble('id', cattle_list, random.randint(1, len(cattle_list)))
        self.ka.mobile_cattle_search_whether_plan(cattleIds=cattleids)


if __name__ == '__main__':
    m = Main()
    unittest.main()
