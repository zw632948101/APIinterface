#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2019/12/30 13:35
@Author: hengxin
"""


import unittest
import time
from interfaces.flowerChaser.BeeAction import BeeAction
from interfaces.flowerChaser.UserAction import UserAction
from utils.log.logger import logger
from testcase.flowerChaser.sql.Passport import PassportInfoSql
from testcase.flowerChaser.sql.Bee import ContainerInformationSql
from testcase.flowerChaser.sql.WorkRecord import WorkRecordSql
from utils.fake.FakeLocation import FakeLocation
from faker import Faker
import random


class KeepLogMain(unittest.TestCase):
    """
    接口文档: http://192.168.62.242:36054/swagger-ui.html
    """
    ua = UserAction()
    ba = BeeAction()
    email = '26632629@qq.com'
    ba.set_user(email, 123456)
    log = logger('WorkLogMain').logger
    log.info("开始执行工作日志接口测试用例")
    pis = PassportInfoSql()
    cis = ContainerInformationSql()
    wrs = WorkRecordSql()
    fake = Faker(locale="zh_CN")
    fl = FakeLocation()

    def test_mobile_add_keep_without_location(self):
        """
        POST /mobile/work-log/add-keep
        未定位尝试添加养蜂日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_keep(gatherHoneyRemark_='', gatherPollenRemark_='', detail_='{}')
        if json_response["status"] == "ERROR":
            self.assertIn(json_response["errorMsg"], ["详细地址不能为空", "省不能为空", "市不能为空",
                                                      "经度不能为空", "纬度不能为空"])
        else:
            self.assertTrue(False, "未定位尝试添加养蜂日志成功")

    def test_mobile_add_keep_with_wrong_lng_lat(self):
        """
        POST /mobile/work-log/add-keep
        非法经纬度
        :return:
        """
        containers = self.cis.sql_all_container()
        platform = random.choice(containers)["id"]
        json_response = self.ba._mobile_work_log_add_keep(province_='41', city_='4101', lng_=-180.1, lat_=-90.1,
                                                          address_='test',
                                                          gatherHoneyRemark_='', gatherPollenRemark_='',
                                                          detail_='''
                                                          [
                                                            {
                                                                "workType": 10020,
                                                                "groupType": 1002010,
                                                                "detailType": 100201001,
                                                                "platform": %d,
                                                                "remark": "备注信息"
                                                            }
                                                          ]''' % platform)
        if json_response["status"] == "ERROR":
            self.assertIn(json_response["errorMsg"], ["纬度超出范围(-90~+90)", "经度超出范围(-180~+180)"])
        else:
            self.assertTrue(False, "非法经纬度, 添加养蜂日志成功")

    def test_mobile_add_keep_with_wrong_region_id(self):
        """
        POST /mobile/work-log/add-keep
        省市ID不正确
        :return:
        """
        containers = self.cis.sql_all_container()
        platform = random.choice(containers)["id"]
        json_response = self.ba._mobile_work_log_add_keep(province_='0', city_='0', lng_='0', lat_='0',
                                                          address_='test',
                                                          gatherHoneyRemark_='', gatherPollenRemark_='',
                                                          detail_='''
                                                                    [
                                                                      {
                                                                          "workType": 10020,
                                                                          "groupType": 1002010,
                                                                          "detailType": 10020101,
                                                                          "platform": %d,
                                                                          "remark": "备注信息"
                                                                      }
                                                                    ]
                                                                 ''' % platform
                                                          )
        if json_response["status"] == "ERROR":
            self.assertIn(json_response["errorMsg"], ["省码不存在", "市码不存在"])
        else:
            self.assertTrue(False, "反解地址不正确, 添加养蜂日志成功")

    def test_mobile_add_keep_with_wrong_province_or_city(self):
        """
        POST /mobile/work-log/add-keep
        定位信息中的city和province为非数字类型
        :return:
        """
        json_response = self.ba._mobile_work_log_add_keep(province_='非数字', city_='非数字',
                                                          gatherHoneyRemark_='', gatherPollenRemark_='', detail_='{}')
        if json_response["status"] == "ERROR":
            self.assertTrue(json_response["errorMsg"].startswith("参数验证错误"))
        else:
            self.assertTrue(False, "city和province为非数字类型, 添加养蜂日志成功")

    def test_mobile_add_keep_with_no_detail(self):
        """
        POST /mobile/work-log/add-keep
        养蜂日志详情数据不能为空
        :return:
        """
        json_response = self.ba._mobile_work_log_add_keep(province_='41', city_='4101', lng_='104.067', lat_='30.535',
                                                          address_='四川省成都市',
                                                          gatherHoneyRemark_='', gatherPollenRemark_='', detail_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("养蜜日志详情数据不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "养蜜日志详情数据不能为空, 添加养蜂日志成功")

    def test_mobile_add_keep_with_wrong_detail_json(self):
        """
        POST /mobile/work-log/add-keep
        养蜂日志详情json格式错误
        :return:
        """
        detail_json = '{}'
        json_response = self.ba._mobile_work_log_add_keep(province_='41', city_='4101', lng_='104.067', lat_='30.535',
                                                          address_='四川省成都市', gatherHoneyRemark_='',
                                                          gatherPollenRemark_='', detail_=detail_json)
        if json_response["status"] == "ERROR":
            self.assertEqual("参数验证错误:%s" % detail_json, json_response["errorMsg"])
        else:
            self.assertTrue(False, "养蜜日志详情json无内容, 添加养蜂日志成功")

    def test_mobile_add_keep_with_wrong_work_type(self):
        """
        POST /mobile/work-log/add-keep
        养蜂日志工作类型错误
        :return:
        """
        json_response = self.ba._mobile_work_log_add_keep(province_='41', city_='4101', lng_='104.067', lat_='30.535',
                                                          address_='四川省成都市', gatherHoneyRemark_='',
                                                          gatherPollenRemark_='',
                                                          detail_='''
                                                          [
                                                            {
                                                                "workType": 10099,
                                                                "groupType": 1002020,
                                                                "detailType": 100202001,
                                                                "platform": 0,
                                                                "remark": "备注信息"
                                                            }
                                                          ]
                                                          '''
                                                          )
        if json_response["status"] == "ERROR":
            self.assertEqual("类型从属关系有误(10099->1002020)", json_response["errorMsg"])
        else:
            self.assertTrue(False, "养蜜日志工作类型错误, 添加养蜂日志成功")

    def test_mobile_add_keep_with_wrong_group_type(self):
        """
        POST /mobile/work-log/add-keep
        养蜂日志分组类型错误
        :return:
        """
        json_response = self.ba._mobile_work_log_add_keep(province_='41', city_='4101', lng_='104.067', lat_='30.535',
                                                          address_='四川省成都市', gatherHoneyRemark_='',
                                                          gatherPollenRemark_='',
                                                          detail_='''
                                                          [
                                                            {
                                                                "workType": 10010,
                                                                "groupType": 1001099,
                                                                "detailType": 100201010,
                                                                "platform": 0,
                                                                "remark": "备注信息"
                                                            }
                                                          ]
                                                          '''
                                                          )
        if json_response["status"] == "ERROR":
            self.assertEqual("蜂场情况类型(1001099)不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "养蜜日志分组类型错误, 添加养蜂日志成功")

    def test_mobile_add_keep_with_wrong_detail_type(self):
        """
        POST /mobile/work-log/add-keep
        养蜂日志详细类型错误
        :return:
        """
        json_response = self.ba._mobile_work_log_add_keep(province_='41', city_='4101', lng_='104.067', lat_='30.535',
                                                          address_='四川省成都市', gatherHoneyRemark_='',
                                                          gatherPollenRemark_='',
                                                          detail_='''
                                                          [
                                                            {
                                                                "workType": 10020,
                                                                "groupType": 1002010,
                                                                "detailType": 100201099,
                                                                "platform": 0,
                                                                "remark": "备注信息"
                                                            }
                                                          ]
                                                          '''
                                                          )
        if json_response["status"] == "ERROR":
            self.assertEqual("蜂场情况类型(100201099)不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "养蜂日志详细类型错误, 添加养蜂日志成功")

    def test_mobile_add_keep_with_mismatch_groupType_type(self):
        """
        POST /mobile/work-log/add-keep
        养蜂日志工作类型与分组类型不匹配
        :return:
        """
        containers = self.cis.sql_all_container()
        platform = random.choice(containers)["id"]
        json_response = self.ba._mobile_work_log_add_keep(province_='41', city_='4101', lng_='104.067', lat_='30.535',
                                                          address_='四川省成都市', gatherHoneyRemark_='',
                                                          gatherPollenRemark_='',
                                                          detail_='''
                                                          [
                                                            {
                                                                "workType": 10010,
                                                                "groupType": 1002010,
                                                                "detailType": 100201010,
                                                                "platform": %d,
                                                                "remark": "备注信息"
                                                            }
                                                          ]
                                                          ''' % platform
                                                          )
        if json_response["status"] == "ERROR":
            self.assertEqual("类型从属关系有误(10010->1002010)", json_response["errorMsg"])
        else:
            self.assertTrue(False, "养蜂日志工作类型与分组类型不匹配, 添加养蜂日志成功")

    def test_mobile_add_keep_with_mismatch_detailType_type(self):
        """
        POST /mobile/work-log/add-keep
        养蜂日志分组类型与详情类型不匹配
        :return:
        """
        containers = self.cis.sql_all_container()
        platform = random.choice(containers)["id"]
        json_response = self.ba._mobile_work_log_add_keep(province_='41', city_='4101', lng_='104.067', lat_='30.535',
                                                          address_='四川省成都市', gatherHoneyRemark_='',
                                                          gatherPollenRemark_='',
                                                          detail_='''
                                                          [
                                                            {
                                                                "workType": 10020,
                                                                "groupType": 1002010,
                                                                "detailType": 100301010,
                                                                "platform": %d,
                                                                "remark": "备注信息"
                                                            }
                                                          ]
                                                          ''' % platform
                                                          )
        if json_response["status"] == "ERROR":
            self.assertEqual("类型从属关系有误(1002010->100301010)", json_response["errorMsg"])
        else:
            self.assertTrue(False, "养蜂日志分组类型与详情类型不匹配, 添加养蜂日志成功")

    def test_mobile_add_keep_with_long_honey(self):
        """
        POST /mobile/work-log/add-keep
        养蜂日志添加进蜜情况超过200字
        :return:
        """
        long_text = '''
        最后学习是否是否情 况.安全成为只有能力.发生我们基本工具.浏览主要在线日本具有深圳如果.\n
        包括大家没有不过资源当然.文件今 天是一有关运行.\n朋友相关比较技术你的.学习部门市场能力虽然销售.感觉国家 一种到了经济选择学校.\n
        经验因为发展认为控制.北京不会继续必须经营.因为以下标准功能简介注册以下.相关推荐更多时候没有然后.\n
        部门操作阅读如此.开始完全同时认为有关项目.\n
        问题网站不同专业城市问题..
        '''
        json_response = self.ba._mobile_work_log_add_keep(province_='41', city_='4101', lng_='104.067', lat_='30.535',
                                                          address_='四川省成都市', gatherPollenRemark_='', detail_='{}',
                                                          gatherHoneyRemark_='%s' % long_text
                                                          )
        if json_response["status"] == "ERROR":
            self.assertEqual("蜜蜂进蜜情况不能超过200字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "养蜂日志添加进蜜情况超过200字, 添加养蜂日志成功")

    def test_mobile_add_keep_with_long_pollen(self):
        """
        POST /mobile/work-log/add-keep
        养蜂日志添加进粉情况超过200字
        :return:
        """
        long_text = '''
        最后学习是否是否情 况.安全成为只有能力.发生我们基本工具.浏览主要在线日本具有深圳如果.\n
        包括大家没有不过资源当然.文件今 天是一有关运行.\n朋友相关比较技术你的.学习部门市场能力虽然销售.感觉国家 一种到了经济选择学校.\n
        经验因为发展认为控制.北京不会继续必须经营.因为以下标准功能简介注册以下.相关推荐更多时候没有然后.\n
        部门操作阅读如此.开始完全同时认为有关项目.\n
        问题网站不同专业城市问题..
        '''
        json_response = self.ba._mobile_work_log_add_keep(province_='41', city_='4101', lng_='104.067', lat_='30.535',
                                                          address_='四川省成都市', gatherHoneyRemark_='', detail_='{}',
                                                          gatherPollenRemark_='%s' % long_text
                                                          )
        if json_response["status"] == "ERROR":
            self.assertEqual("蜜蜂进粉情况不能超过200字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "养蜂日志仅添加进蜜情况, 添加养蜂日志成功")

    def test_mobile_add_keep_with_wrong_platform(self):
        """
        POST /mobile/work-log/add-keep
        平台ID不存在
        :return:
        """
        json_response = self.ba._mobile_work_log_add_keep(province_='41', city_='4101', address_='四川省成都市',
                                                          lng_='104.067', lat_='30.535',
                                                          gatherHoneyRemark_='', gatherPollenRemark_='',
                                                          detail_='''
                                                          [
                                                            {
                                                                "workType": 10020,
                                                                "groupType": 1002020,
                                                                "detailType": 100202001,
                                                                "platform": 0,
                                                                "remark": "备注信息"
                                                            }
                                                          ]
                                                          '''
                                                          )
        if json_response["status"] == "ERROR":
            self.assertEqual("关联养蜂平台(ID:0)不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "平台ID不存在, 添加养蜂日志成功")

    def test_mobile_add_keep_with_repeated_platform_id(self):
        """
        POST /mobile/work-log/add-keep
        传入重复平台ID
        :return:
        """
        containers = self.cis.sql_all_container()
        platform = random.choice(containers)["id"]
        json_response = self.ba._mobile_work_log_add_keep(province_='41', city_='4101', address_='四川省成都市',
                                                          lng_='104.067', lat_='30.535',
                                                          gatherHoneyRemark_='', gatherPollenRemark_='',
                                                          detail_='''
                                                          [
                                                            {
                                                                "workType": 10010,
                                                                "groupType": 1001010,
                                                                "platform": "%s,%s",
                                                                "remark": "备注信息"
                                                            }
                                                          ]
                                                          ''' % (platform, platform)
                                                          )
        if json_response["status"] == "ERROR":
            self.assertEqual("关联平台重复或为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "传入重复平台ID, 添加养蜂日志成功")

    def test_mobile_add_keep_with_random_success(self):
        """
        POST /mobile/work-log/add-keep
        添加养蜂日志-共计5种, 转场/蜂场饲喂/病害防治/蜂群异常/其他, 遍历随机生成
        :return:
        """
        province_id, city_id, address, lng, lat = self.fl.fake_location()
        platform = self.cis.get_random_platform()
        random_types_list = self.wrs.get_random_type_for_keep_log()
        for t in random_types_list:
            if t[2]:
                detail_json = '''
                                [
                                    {
                                        "workType": %s,
                                        "groupType": %s,
                                        "detailType": %s,
                                        "platform": "%s",
                                        "remark": "备注信息"
                                    }
                                ]
                              ''' % (t[0], t[1], t[2], platform)
            else:
                detail_json = '''
                                                [
                                                    {
                                                        "workType": %s,
                                                        "groupType": %s,
                                                        "platform": "%s",
                                                        "remark": "备注信息"
                                                    }
                                                ]
                              ''' % (t[0], t[1], platform)
            json_response = self.ba._mobile_work_log_add_keep(province_=province_id, city_=city_id, address_=address,
                                                              lng_=lng, lat_=lat,
                                                              gatherHoneyRemark_='', gatherPollenRemark_='',
                                                              detail_=detail_json)
            if json_response["status"] == "OK":
                work_log = self.wrs.query_keep_log_by_email(self.email)[0]
                self.assertEqual(t[0], work_log["work_type"])
                self.assertEqual(t[1], work_log["group_type"])
                self.assertEqual(t[2], work_log["detail_type"])
                self.assertEqual(province_id, work_log["province"])
                self.assertEqual(city_id, work_log["city"])
                self.assertEqual(address, work_log["address"])
                self.assertEqual(lng, work_log["lng"])
                self.assertEqual(lat, work_log["lat"])
                self.assertEqual(platform, work_log["platform"])
                self.assertEqual('', work_log["gather_honey_remark"])
                self.assertEqual('', work_log["gather_pollen_remark"])
            else:
                self.assertTrue(False, "添加养蜂日志失败")

    def test_mobile_add_keep_with_multi_unusual(self):
        """
        POST /mobile/work-log/add-keep
        添加养蜂日志-共计5种, 转场/蜂场饲喂/病害防治/蜂群异常/其他, 遍历随机生成
        :return:
        """
        province_id, city_id, address, lng, lat = self.fl.fake_location()
        detail_json = '''
                        [
                            {
                                "workType": "10040",
                                "groupType": "1004010",
                                "platform": "%s",
                                "remark": "备注信息"
                            },
                            {
                                "workType": "10040",
                                "groupType": "1004020",
                                "platform": "%s",
                                "remark": "备注信息"
                            },
                            {
                                "workType": "10040",
                                "groupType": "1004030",
                                "platform": "%s",
                                "remark": "备注信息"
                            },
                            {
                                "workType": "10040",
                                "groupType": "1004040",
                                "platform": "%s",
                                "remark": "备注信息"
                            },
                            {
                                "workType": "10040",
                                "groupType": "1004050",
                                "platform": "%s",
                                "remark": "备注信息"
                            },
                            {
                                "workType": "10040",
                                "groupType": "1004060",
                                "platform": "%s",
                                "remark": "备注信息"
                            },
                            {
                                "workType": "10040",
                                "groupType": "1004070",
                                "platform": "%s",
                                "remark": "备注信息"
                            }
                        ]
                      ''' % (self.cis.get_random_platform(), self.cis.get_random_platform(),
                             self.cis.get_random_platform(), self.cis.get_random_platform(),
                             self.cis.get_random_platform(), self.cis.get_random_platform(),
                             self.cis.get_random_platform())
        json_response = self.ba._mobile_work_log_add_keep(province_=province_id, city_=city_id, address_=address,
                                                          lng_=lng, lat_=lat,
                                                          gatherHoneyRemark_='', gatherPollenRemark_='',
                                                          detail_=detail_json)
        if json_response["status"] == "OK":
            work_log = self.wrs.query_keep_log_by_email(self.email)[0]
            self.assertEqual("10040", work_log["work_type"])
            self.assertEqual("10040", work_log["group_type"][:5])
            self.assertEqual(None, work_log["detail_type"])
            self.assertEqual(province_id, work_log["province"])
            self.assertEqual(city_id, work_log["city"])
            self.assertEqual(address, work_log["address"])
            self.assertEqual(lng, work_log["lng"])
            self.assertEqual(lat, work_log["lat"])
            # self.assertEqual(platform, work_log["platform"])
            self.assertEqual('', work_log["gather_honey_remark"])
            self.assertEqual('', work_log["gather_pollen_remark"])
        else:
            self.assertTrue(False, "添加养蜂日志失败")

    def test_mobile_add_keep_with_honey_success(self):
        """
        POST /mobile/work-log/add-keep
        养蜂日志添加进蜜情况
        :return:
        """
        honey_remark = self.fake.text(max_nb_chars=200)
        province_id, city_id, address, lng, lat = self.fl.fake_location()
        json_response = self.ba._mobile_work_log_add_keep(province_=province_id, city_=city_id, lng_=lng, lat_=lat,
                                                          address_=address, gatherPollenRemark_='',
                                                          detail_='[]',
                                                          gatherHoneyRemark_='%s' % honey_remark
                                                          )
        if json_response["status"] == "OK":
            work_log = self.wrs.query_keep_log_by_email_without_extend(self.email)[0]
            self.assertEqual(None, work_log["work_type"])
            self.assertEqual(None, work_log["group_type"])
            self.assertEqual(None, work_log["detail_type"])
            self.assertEqual(province_id, work_log["province"])
            self.assertEqual(city_id, work_log["city"])
            self.assertEqual(address, work_log["address"])
            self.assertEqual(lng, work_log["lng"])
            self.assertEqual(lat, work_log["lat"])
            self.assertEqual(None, work_log["platform"])
            self.assertEqual(honey_remark, work_log["gather_honey_remark"])
            self.assertEqual('', work_log["gather_pollen_remark"])
        else:
            self.assertTrue(False, "养蜂日志添加进蜜情况, 添加失败")

    def test_mobile_add_keep_with_pollen_success(self):
        """
        POST /mobile/work-log/add-keep
        养蜂日志添加进粉情况
        :return:
        """
        pollen_remark = self.fake.text(max_nb_chars=200)
        province_id, city_id, address, lng, lat = self.fl.fake_location()
        json_response = self.ba._mobile_work_log_add_keep(province_=province_id, city_=city_id, lng_=lng, lat_=lat,
                                                          address_=address, gatherHoneyRemark_='',
                                                          detail_='[]',
                                                          gatherPollenRemark_='%s' % pollen_remark
                                                          )
        if json_response["status"] == "OK":
            work_log = self.wrs.query_keep_log_by_email_without_extend(self.email)[0]
            self.assertEqual(None, work_log["work_type"])
            self.assertEqual(None, work_log["group_type"])
            self.assertEqual(None, work_log["detail_type"])
            self.assertEqual(province_id, work_log["province"])
            self.assertEqual(2, work_log["type"])
            self.assertEqual(city_id, work_log["city"])
            self.assertEqual(address, work_log["address"])
            self.assertEqual(lng, work_log["lng"])
            self.assertEqual(lat, work_log["lat"])
            self.assertEqual(None, work_log["platform"])
            self.assertEqual('', work_log["gather_honey_remark"])
            self.assertEqual(pollen_remark, work_log["gather_pollen_remark"])
        else:
            self.assertTrue(False, "养蜂日志添加进粉情况, 添加失败")

    def test_mobile_edit_keep_without_log_id(self):
        """
        POST /mobile/work-log/edit-keep
        养蜂日志ID不正确
        :return:
        """
        json_response = self.ba._mobile_work_log_edit_keep(logId_='', gatherHoneyRemark_='',
                                                           detail_='[]', gatherPollenRemark_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("日志ID不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "养蜂日志ID不正确, 添加成功")

    def test_mobile_edit_keep_with_wrong_log_id(self):
        """
        POST /mobile/work-log/edit-keep
        养蜂日志ID不正确
        :return:
        """
        # 0和空都校验了, 但是其它类型的日志ID未做校验
        seek_log_id = self.wrs.query_seek_log_by_email(self.email)[0]["id"]
        json_response = self.ba._mobile_work_log_edit_keep(logId_=seek_log_id, gatherHoneyRemark_='',
                                                           detail_='[]', gatherPollenRemark_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("日志不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "养蜂日志ID不正确, 编辑成功")

    def test_mobile_edit_keep_without_detail(self):
        """
        POST /mobile/work-log/edit-keep
        养蜂日志详情为空
        :return:
        """
        # 0和空都校验了, 但是其它类型的日志ID未做校验
        keep_log_id = self.wrs.query_keep_log_by_email(self.email)[0]["id"]
        json_response = self.ba._mobile_work_log_edit_keep(logId_=keep_log_id, gatherHoneyRemark_='',
                                                           detail_='', gatherPollenRemark_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("养蜜日志详情数据不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "养蜂日志详情为空, 编辑成功")

    def test_mobile_edit_keep_with_nothing(self):
        """
        POST /mobile/work-log/edit-keep
        养蜂日志全部传空, 数据是否清空
        :return:
        """
        work_log = self.wrs.query_keep_log_by_email_without_extend(self.email)[0]
        keep_log_id = work_log["id"]
        json_response = self.ba._mobile_work_log_edit_keep(logId_=keep_log_id, gatherHoneyRemark_='',
                                                           detail_='[]', gatherPollenRemark_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("请至少填写一项工作内容", json_response["errorMsg"])
            edited_work_log = self.wrs.query_keep_log_by_email_without_extend(self.email)[0]
            self.assertEqual(edited_work_log["work_type"], work_log["work_type"])
            self.assertEqual(edited_work_log["group_type"], work_log["group_type"])
            self.assertEqual(edited_work_log["detail_type"], work_log["detail_type"])
            self.assertEqual(edited_work_log["province"], work_log["province"])
            self.assertEqual(2, work_log["type"])
            self.assertEqual(edited_work_log["city"], work_log["city"])
            self.assertEqual(edited_work_log["address"], work_log["address"])
            self.assertEqual(edited_work_log["lng"], work_log["lng"])
            self.assertEqual(edited_work_log["lat"], work_log["lat"])
            self.assertEqual(edited_work_log["platform"], work_log["platform"])
            self.assertEqual(edited_work_log["gather_honey_remark"], work_log["gather_honey_remark"])
            self.assertEqual(edited_work_log["gather_pollen_remark"], work_log["gather_pollen_remark"])
        else:
            self.assertTrue(False, "养蜂日志全部传空, 数据已清空")

    def test_mobile_edit_keep_success(self):
        """
        POST /mobile/work-log/edit-keep
        正确编辑养蜂日志
        :return:
        """
        work_log = self.wrs.query_keep_log_by_email(self.email)[0]
        keep_log_id = work_log["id"]
        platform = self.cis.get_random_platform()
        gather_honey_remark = self.fake.text()
        gather_pollen_remark = self.fake.text()
        random_types_list = self.wrs.get_random_type_for_keep_log()
        for t in random_types_list:
            if t[2]:
                detail_json = '''
                                        [
                                            {
                                                "workType": %s,
                                                "groupType": %s,
                                                "detailType": %s,
                                                "platform": "%s",
                                                "remark": "备注信息"
                                            }
                                        ]
                                      ''' % (t[0], t[1], t[2], platform)
            else:
                detail_json = '''
                                                        [
                                                            {
                                                                "workType": %s,
                                                                "groupType": %s,
                                                                "platform": "%s",
                                                                "remark": "备注信息"
                                                            }
                                                        ]
                                      ''' % (t[0], t[1], platform)
            json_response = self.ba._mobile_work_log_edit_keep(logId_=keep_log_id,
                                                               gatherHoneyRemark_=gather_honey_remark,
                                                               gatherPollenRemark_=gather_pollen_remark,
                                                               detail_=detail_json)
            if json_response["status"] == "OK":
                work_log = self.wrs.query_keep_log_by_email(self.email)[0]
                self.assertEqual(t[0], work_log["work_type"])
                self.assertEqual(t[1], work_log["group_type"])
                self.assertEqual(t[2], work_log["detail_type"])
                self.assertEqual(gather_honey_remark, work_log["gather_honey_remark"])
                self.assertEqual(gather_pollen_remark, work_log["gather_pollen_remark"])
                self.assertEqual(platform, work_log["platform"])
            else:
                self.assertTrue(False, "编辑养蜂日志失败")

    def test_mobile_detail_keep_with_wrong_id(self):
        """
        POST /mobile/work-log/detail-keep
        养蜂日志id错误, 查询日志详情
        :return:
        """
        work_log = self.wrs.query_seek_log_by_email(self.email)[0]
        seek_log_id = work_log["id"]
        json_response = self.ba._mobile_work_log_detail_keep(id_=seek_log_id)
        if json_response["status"] == "ERROR":
            self.assertEqual("日志不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "养蜂日志id错误, 查询日志详情成功")

    def test_mobile_detail_keep_without_id(self):
        """
        POST /mobile/work-log/detail-keep
        养蜂日志id为空, 查询日志详情
        :return:
        """
        json_response = self.ba._mobile_work_log_detail_keep(id_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("日志ID不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "养蜂日志id错误, 查询日志详情成功")

    def test_mobile_detail_keep_success(self):
        """
        POST /mobile/work-log/detail-keep
        正确养蜂日志ID, 查询日志详情
        :return:
        """
        work_log = self.wrs.query_keep_log_by_email(self.email)[0]
        keep_log_id = work_log["id"]
        json_response = self.ba._mobile_work_log_detail_keep(id_=keep_log_id)
        if json_response["status"] == "OK":
            json_data = json_response["content"]["situationList"][0]
            self.assertEqual(json_data["workType"], work_log["work_type"])
            self.assertEqual(json_data["detail"][0]["groupType"], work_log["group_type"])
            self.assertEqual(json_data["detail"][0].get("detailType", None), work_log["detail_type"])
            self.assertEqual(2, work_log["type"])
            self.assertEqual(json_response["content"]["address"], work_log["address"])
            self.assertEqual(json_response["content"]["creatorId"], work_log["tu.id"])
            self.assertEqual(json_response["content"]["creatorName"], work_log["username"])
            self.assertEqual(json_response["content"]["creatorHeadImg"], work_log["head_img"])
            create_time = time.strftime('%Y-%m-%d %H:%M:%S',
                                        time.localtime(float(json_response["content"]["createTime"]) / 1000.0))
            self.assertEqual(create_time, work_log["create_time"])
            self.assertEqual(json_data["detail"][0]["platform"], work_log["platform"])
            self.assertEqual(json_response["content"]["gatherHoneyRemark"], work_log["gather_honey_remark"])
            self.assertEqual(json_response["content"]["gatherPollenRemark"], work_log["gather_pollen_remark"])
        else:
            self.assertTrue(False, "正确养蜂日志ID, 查询日志失败")
