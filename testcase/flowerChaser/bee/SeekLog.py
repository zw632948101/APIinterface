#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2020/1/2 10:22
@Author: hengxin
"""


import unittest
import random
import time
from interfaces.flowerChaser.BeeAction import BeeAction
from interfaces.flowerChaser.UserAction import UserAction
from utils.log.logger import logger
from testcase.flowerChaser.sql.Passport import PassportInfoSql
from testcase.flowerChaser.sql.Bee import ContainerInformationSql
from testcase.flowerChaser.sql.WorkRecord import WorkRecordSql
from utils.fake.FakeLocation import FakeLocation
from faker import Faker


class SeekLogMain(unittest.TestCase):
    """
    接口文档: http://192.168.62.242:36054/swagger-ui.html
    """
    ua = userAction()
    ba = BeeAction()
    email = '26632629@qq.com'
    ba.set_user(email, 123456)
    log = logger('SeekLogMain').logger
    log.info("开始执行寻蜜日志接口测试用例")
    pis = PassportInfoSql()
    cis = ContainerInformationSql()
    wrs = WorkRecordSql()
    fake = Faker(locale="zh_CN")
    fl = FakeLocation()

    def test_mobile_add_seek_without_province(self):
        """
        POST /mobile/work-log/add-seek
        省ID为空尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='', city_='4101', address_='测试地址', lng_='103', lat_='40', remark_='remark',
            isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员')
        if json_response["status"] == "ERROR":
            self.assertEqual("省不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "省ID为空, 添加寻蜜日志成功")

    def test_mobile_add_seek_without_city(self):
        """
        POST /mobile/work-log/add-seek
        市ID为空尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='', address_='测试地址', lng_='103', lat_='40', remark_='remark',
            isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员')
        if json_response["status"] == "ERROR":
            self.assertEqual("市不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "市ID为空, 添加寻蜜日志成功")

    def test_mobile_add_seek_without_address(self):
        """
        POST /mobile/work-log/add-seek
        详细地址为空, 尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='', lng_='103', lat_='40', remark_='remark',
            isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员')
        if json_response["status"] == "ERROR":
            self.assertEqual("详细地址不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "详细地址为空, 添加寻蜜日志成功")

    def test_mobile_add_seek_without_lng(self):
        """
        POST /mobile/work-log/add-seek
        经度为空, 尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='测试地址', lng_='', lat_='40', remark_='remark',
            isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员')
        if json_response["status"] == "ERROR":
            self.assertEqual("经度不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "经度为空, 添加寻蜜日志成功")

    def test_mobile_add_seek_illegal_lng(self):
        """
        POST /mobile/work-log/add-seek
        经度超出范围, 尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='测试地址', lng_='180.1', lat_='40', remark_='remark',
            isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员')
        if json_response["status"] == "ERROR":
            self.assertEqual("经度超出范围(-180~+180)", json_response["errorMsg"])
        else:
            self.assertTrue(False, "经度超出范围, 添加寻蜜日志成功")

    def test_mobile_add_seek_without_lat(self):
        """
        POST /mobile/work-log/add-seek
        纬度为空, 尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='测试地址', lng_='103', lat_='', remark_='remark',
            isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员')
        if json_response["status"] == "ERROR":
            self.assertEqual("纬度不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "纬度为空, 添加寻蜜日志成功")

    def test_mobile_add_seek_illegal_lat(self):
        """
        POST /mobile/work-log/add-seek
        纬度超出范围, 尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='测试地址', lng_='180', lat_='-90.1', remark_='remark',
            isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员')
        if json_response["status"] == "ERROR":
            self.assertEqual("纬度超出范围(-90~+90)", json_response["errorMsg"])
        else:
            self.assertTrue(False, "纬度超出范围, 添加寻蜜日志成功")

    def test_mobile_add_seek_with_illegal_province(self):
        """
        POST /mobile/work-log/add-seek
        省ID不正确
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='0', city_='4101', address_='测试地址', lng_='104', lat_='30', remark_='remark',
            isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员')
        if json_response["status"] == "ERROR":
            self.assertEqual("省码不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "省ID不正确, 添加寻蜜日志成功")

    def test_mobile_add_seek_with_illegal_city(self):
        """
        POST /mobile/work-log/add-seek
        市ID不正确
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='0', address_='测试地址', lng_='104', lat_='30', remark_='remark',
            isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员')
        if json_response["status"] == "ERROR":
            self.assertEqual("市码不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "市ID不正确, 添加寻蜜日志成功")

    def test_mobile_add_seek_with_wrong_province_or_city(self):
        """
        POST /mobile/work-log/add-seek
        定位信息中的city和province为非数字类型
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='test', city_='test', address_='测试地址', lng_='104', lat_='30', remark_='remark',
            isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员'
        )
        if json_response["status"] == "ERROR":
            self.assertTrue(json_response["errorMsg"].startswith("参数验证错误"))
        else:
            self.assertTrue(False, "city和province为非数字类型, 添加寻蜜日志成功")

    def test_mobile_add_seek_without_is_fit(self):
        """
        POST /mobile/work-log/add-seek
        是否有合适蜜源地为空, 尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='4101', city_='41', address_='测试地址', lng_='104', lat_='30', remark_='remark',
            isFit_='', route_='自动化测试寻蜜路线', worker_='在岗人员'
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("是否有合适蜜源地不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "是否有合适蜜源地为空, 添加寻蜜日志成功")

    def test_mobile_add_seek_with_illegal_fit(self):
        """
        POST /mobile/work-log/add-seek
        是否有合适蜜源地枚举非法, 尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='4101', city_='41', address_='测试地址', lng_='104', lat_='30', remark_='remark',
            isFit_='2', route_='自动化测试寻蜜路线', worker_='在岗人员'
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("0.否,1.是", json_response["errorMsg"])
        else:
            self.assertTrue(False, "是否有合适蜜源地枚举非法, 添加寻蜜日志成功")

    def test_mobile_add_seek_without_remark(self):
        """
        POST /mobile/work-log/add-seek
        详细情况备注为空, 尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='4101', city_='41', address_='测试地址', lng_='104', lat_='30', remark_='',
            isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员'
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("详细情况备注不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "详细情况备注为空, 添加寻蜜日志成功")

    def test_mobile_add_seek_with_long_remark(self):
        """
        POST /mobile/work-log/add-seek
        详细情况备注超过200字, 尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='4101', city_='41', address_='测试地址', lng_='104', lat_='30', remark_='''
            最后学习是否是否情 况.安全成为只有能力.发生我们基本工具.浏览主要在线日本具有深圳如果.\n
        包括大家没有不过资源当然.文件今 天是一有关运行.\n朋友相关比较技术你的.学习部门市场能力虽然销售.感觉国家 一种到了经济选择学校.\n
        经验因为发展认为控制.北京不会继续必须经营.因为以下标准功能简介注册以下.相关推荐更多时候没有然后.\n
        部门操作阅读如此.开始完全同时认为有关项目.\n
        问题网站不同专业城市问题..
            ''',
            isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员'
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("详细情况备注不能超过200字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "详细情况备注超过200字, 添加寻蜜日志成功")

    def test_mobile_add_seek_without_route(self):
        """
        POST /mobile/work-log/add-seek
        寻蜜路线为空, 尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='4101', city_='41', address_='测试地址', lng_='104', lat_='30', remark_='remark',
            isFit_='0', route_='', worker_='worker'
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("寻蜜路线不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "寻蜜路线为空, 添加寻蜜日志成功")

    def test_mobile_add_seek_with_long_route(self):
        """
        POST /mobile/work-log/add-seek
        寻蜜路线超长, 尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='4101', city_='41', address_='测试地址', lng_='104', lat_='30', remark_='remark',
            isFit_='0', worker_='worker', route_='''
            最后学习是否是否情 况.安全成为只有能力.发生我们基本工具.浏览主要在线日本具有深圳如果.\n
        包括大家没有不过资源当然.文件今 天是一有关运行.\n朋友相关比较技术你的.学习部门市场能力虽然销售.感觉国家 一种到了经济选择学校.\n
        经验因为发展认为控制.北京不会继续必须经营.因为以下标准功能简介注册以下.相关推荐更多时候没有然后.\n
        部门操作阅读如此.开始完全同时认为有关项目.\n
        问题网站不同专业城市问题..
            '''
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("寻蜜路线不能超过200字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "寻蜜路线超长, 添加寻蜜日志成功")

    def test_mobile_add_seek_without_worker(self):
        """
        POST /mobile/work-log/add-seek
        在岗人员为空, 尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='4101', city_='41', address_='测试地址', lng_='104', lat_='30', remark_='remark',
            isFit_='0', route_='自动化测试寻蜜路线', worker_=None
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("在岗人员不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "在岗人员为空, 添加寻蜜日志成功")

    def test_mobile_add_seek_with_long_worker(self):
        """
        POST /mobile/work-log/add-seek
        在岗人员超过200字, 尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='4101', city_='41', address_='测试地址', lng_='104', lat_='30', remark_='remark',
            isFit_='0', route_='自动化测试寻蜜路线', worker_='''
            最后学习是否是否情 况.安全成为只有能力.发生我们基本工具.浏览主要在线日本具有深圳如果.\n
        包括大家没有不过资源当然.文件今 天是一有关运行.\n朋友相关比较技术你的.学习部门市场能力虽然销售.感觉国家 一种到了经济选择学校.\n
        经验因为发展认为控制.北京不会继续必须经营.因为以下标准功能简介注册以下.相关推荐更多时候没有然后.\n
        部门操作阅读如此.开始完全同时认为有关项目.\n
        问题网站不同专业城市问题..
        '''
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("在岗人员不能超过200字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "在岗人员超过200字, 添加寻蜜日志成功")

    def test_mobile_add_seek_with_long_flower_remark(self):
        """
        POST /mobile/work-log/add-seek
        花源情况超过200字, 尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='4101', city_='41', address_='测试地址', lng_='104', lat_='30', remark_='remark',
            isFit_='0', route_='自动化测试寻蜜路线', worker_='worker', flowerRemark_='''
            最后学习是否是否情 况.安全成为只有能力.发生我们基本工具.浏览主要在线日本具有深圳如果.\n
        包括大家没有不过资源当然.文件今 天是一有关运行.\n朋友相关比较技术你的.学习部门市场能力虽然销售.感觉国家 一种到了经济选择学校.\n
        经验因为发展认为控制.北京不会继续必须经营.因为以下标准功能简介注册以下.相关推荐更多时候没有然后.\n
        部门操作阅读如此.开始完全同时认为有关项目.\n
        问题网站不同专业城市问题..
        '''
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("花源情况不能超过200字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "花源情况超过200字, 添加寻蜜日志成功")

    def test_mobile_add_seek_with_long_env(self):
        """
        POST /mobile/work-log/add-seek
        周边环境情况超过200字, 尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='4101', city_='41', address_='测试地址', lng_='104', lat_='30', remark_='remark',
            isFit_='0', route_='自动化测试寻蜜路线', worker_='worker', flowerRemark_='', env_='''
            最后学习是否是否情 况.安全成为只有能力.发生我们基本工具.浏览主要在线日本具有深圳如果.\n
        包括大家没有不过资源当然.文件今 天是一有关运行.\n朋友相关比较技术你的.学习部门市场能力虽然销售.感觉国家 一种到了经济选择学校.\n
        经验因为发展认为控制.北京不会继续必须经营.因为以下标准功能简介注册以下.相关推荐更多时候没有然后.\n
        部门操作阅读如此.开始完全同时认为有关项目.\n
        问题网站不同专业城市问题..
        '''
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("周边环境情况不能超过200字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "周边环境情况超过200字, 添加寻蜜日志成功")

    def test_mobile_add_seek_without_picture(self):
        """
        POST /mobile/work-log/add-seek
        现场照片为空尝试添加寻蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_seek(pics_='', province_='41', city_='4101', address_='测试地址',
                                                          lng_='103', lat_='40', remark_='remark',
                                                          isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员')
        if json_response["status"] == "ERROR":
            self.assertEqual("现场照片不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "现场照片为空, 添加寻蜜日志成功")

    def test_mobile_add_seek_with_repeated_picture(self):
        """
        POST /mobile/work-log/add-seek
        多张现场照片重复, 尝试添加寻蜜日志
        :return:
        """
        pic_url = "https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"
        pics = '["%s", "%s"]' % (pic_url, pic_url)
        json_response = self.ba._mobile_work_log_add_seek(pics_=pics, province_='41', city_='4101', address_='测试地址',
                                                          lng_='103', lat_='40', remark_='remark',
                                                          isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员')
        if json_response["status"] == "ERROR":
            self.assertEqual("图片URL重复或为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "多张现场照片重复, 添加寻蜜日志成功")

    def test_mobile_add_seek_with_more_picture(self):
        """
        POST /mobile/work-log/add-seek
        现场照片超过三张, 尝试添加寻蜜日志
        :return:
        """
        pic_url = self.cis.get_random_img_list(4)
        json_response = self.ba._mobile_work_log_add_seek(pics_=pic_url, province_='41', city_='4101', address_='测试地址',
                                                          lng_='103', lat_='40', remark_='remark',
                                                          isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员')
        if json_response["status"] == "ERROR":
            self.assertEqual("图片最多三张", json_response["errorMsg"])
        else:
            self.assertTrue(False, "现场照片超过三张, 添加寻蜜日志成功")

    def test_mobile_add_seek_with_more_flower_remark(self):
        """
        POST /mobile/work-log/add-seek
        花源情况超过200字, 尝试添加寻蜜日志
        :return:
        """
        flower_remark = '''
        最后学习是否是否情 况.安全成为只有能力.发生我们基本工具.浏览主要在线日本具有深圳如果.\n
        包括大家没有不过资源当然.文件今 天是一有关运行.\n朋友相关比较技术你的.学习部门市场能力虽然销售.感觉国家 一种到了经济选择学校.\n
        经验因为发展认为控制.北京不会继续必须经营.因为以下标准功能简介注册以下.相关推荐更多时候没有然后.\n
        部门操作阅读如此.开始完全同时认为有关项目.\n
        问题网站不同专业城市问题..
        '''
        pic_url = self.cis.get_random_img_list(4)
        json_response = self.ba._mobile_work_log_add_seek(pics_=pic_url, province_='41', city_='4101',
                                                          address_='测试地址', lng_='103', lat_='40', remark_='remark',
                                                          flowerRemark_=flower_remark,
                                                          isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员')
        if json_response["status"] == "ERROR":
            self.assertEqual("花源情况不能超过200字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "花源情况超过200字, 添加寻蜜日志成功")

    def test_mobile_add_seek_with_more_env(self):
        """
        POST /mobile/work-log/add-seek
        周边环境情况超过200字, 尝试添加寻蜜日志
        :return:
        """
        env = '''
        最后学习是否是否情 况.安全成为只有能力.发生我们基本工具.浏览主要在线日本具有深圳如果.\n
        包括大家没有不过资源当然.文件今 天是一有关运行.\n朋友相关比较技术你的.学习部门市场能力虽然销售.感觉国家 一种到了经济选择学校.\n
        经验因为发展认为控制.北京不会继续必须经营.因为以下标准功能简介注册以下.相关推荐更多时候没有然后.\n
        部门操作阅读如此.开始完全同时认为有关项目.\n
        问题网站不同专业城市问题..
        '''
        pic_url = self.cis.get_random_img_list(4)
        json_response = self.ba._mobile_work_log_add_seek(pics_=pic_url, province_='41', city_='4101', address_='地址',
                                                          lng_='103', lat_='40', remark_='remark', env_=env,
                                                          isFit_='0', route_='自动化测试寻蜜路线', worker_='在岗人员')
        if json_response["status"] == "ERROR":
            self.assertEqual("周边环境情况不能超过200字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "周边环境情况超过200字, 添加寻蜜日志成功")

    def test_mobile_add_seek_success(self):
        """
        POST /mobile/work-log/add-seek
        添加寻蜜日志成功
        :return:
        """
        province_id, city_id, address, lng, lat = self.fl.fake_location()
        remark = self.fake.text()
        route = self.fake.text()
        worker = self.fake.text()
        env = self.fake.text()
        flower_remark = self.fake.text()
        pic_url = self.cis.get_random_img_list(3)
        is_fit = random.choice([0, 1])
        json_response = self.ba._mobile_work_log_add_seek(pics_=pic_url, province_=province_id, city_=city_id,
                                                          address_=address, flowerRemark_=flower_remark,
                                                          lng_=lng, lat_=lat, remark_=remark, env_=env,
                                                          isFit_=is_fit, route_=route, worker_=worker)
        if json_response["status"] == "OK":
            work_log = self.wrs.query_seek_log_by_email(self.email)[0]
            self.assertEqual(province_id, work_log["province"])
            self.assertEqual(city_id, work_log["city"])
            self.assertEqual(address, work_log["address"])
            self.assertEqual(lng, work_log["lng"])
            self.assertEqual(lat, work_log["lat"])
            self.assertEqual(1, work_log["type"])
            self.assertEqual(is_fit, work_log["is_fit"])
            self.assertEqual(remark, work_log["remark"])
            self.assertEqual(route, work_log["route"])
            self.assertEqual(worker, work_log["worker"])
            self.assertEqual(env, work_log["env"])
            self.assertEqual(pic_url, work_log["pics"])
            self.assertEqual(flower_remark, work_log["flower_remark"])
        else:
            self.assertTrue(False, "添加寻蜜日志失败")

    def test_mobile_edit_seek_without_log_id(self):
        """
        POST /mobile/work-log/edit-seek
        寻蜜日志ID不正确
        :return:
        """
        json_response = self.ba._mobile_work_log_edit_seek(logId_='', pics_='pics', flowerRemark_="flower_remark",
                                                           remark_="remark", env_="env",
                                                           isFit_="0", route_="route", worker_="worker")
        if json_response["status"] == "ERROR":
            self.assertEqual("日志ID不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "寻蜜日志ID不正确, 添加成功")

    def test_mobile_edit_seek_with_wrong_log_id(self):
        """
        POST /mobile/work-log/edit-seek
        寻蜜日志ID不正确
        :return:
        """
        json_response = self.ba._mobile_work_log_edit_seek(logId_=0, pics_='["pics"]', flowerRemark_="flower_remark",
                                                           remark_="remark", env_="env",
                                                           isFit_="0", route_="route", worker_="worker")
        if json_response["status"] == "ERROR":
            self.assertEqual("日志不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "寻蜜日志ID不正确, 编辑成功")

    def test_mobile_edit_seek_without_remark(self):
        """
        POST /mobile/work-log/edit-seek
        寻蜜日志详情为空
        :return:
        """
        seek_log_id = self.wrs.query_seek_log_by_email(self.email)[0]["id"]
        json_response = self.ba._mobile_work_log_edit_seek(logId_=seek_log_id, pics_='pics', flowerRemark_="",
                                                           remark_="", env_="",
                                                           isFit_="0", route_="route", worker_="worker")
        if json_response["status"] == "ERROR":
            self.assertEqual("详细情况备注不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "寻蜜日志详情为空, 编辑成功")

    def test_mobile_edit_seek_without_picture(self):
        """
        POST /mobile/work-log/edit-seek
        现场照片为空, 编辑寻蜜日志成功
        :return:
        """
        work_log = self.wrs.query_seek_log_by_email(self.email)[0]
        seek_log_id = work_log["id"]
        json_response = self.ba._mobile_work_log_edit_seek(logId_=seek_log_id, pics_='', flowerRemark_="",
                                                           remark_="remark", env_="",
                                                           isFit_="0", route_="route", worker_="worker")
        if json_response["status"] == "ERROR":
            self.assertEqual("现场照片不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "现场照片为空, 编辑寻蜜日志成功")

    def test_mobile_edit_seek_with_more_picture(self):
        """
        POST /mobile/work-log/edit-seek
        现场照片超过3张, 编辑寻蜜日志成功
        :return:
        """
        work_log = self.wrs.query_seek_log_by_email(self.email)[0]
        seek_log_id = work_log["id"]
        pics = self.cis.get_random_img_list(4)
        json_response = self.ba._mobile_work_log_edit_seek(logId_=seek_log_id, pics_=pics, flowerRemark_="",
                                                           remark_="remark", env_="",
                                                           isFit_="0", route_="route", worker_="worker")
        if json_response["status"] == "ERROR":
            self.assertEqual("图片最多三张", json_response["errorMsg"])
        else:
            self.assertTrue(False, "现场照片超过3张, 编辑寻蜜日志成功")

    def test_mobile_edit_seek_with_illegal_fit(self):
        """
        POST /mobile/work-log/edit-seek
        错误的是否有合适蜜源枚举
        :return:
        """
        work_log = self.wrs.query_seek_log_by_email(self.email)[0]
        seek_log_id = work_log["id"]
        json_response = self.ba._mobile_work_log_edit_seek(logId_=seek_log_id, pics_="pics", flowerRemark_="",
                                                           remark_="remark", env_="",
                                                           isFit_=2, route_="route", worker_="worker")
        if json_response["status"] == "ERROR":
            self.assertEqual("0.否,1.是", json_response["errorMsg"])
        else:
            self.assertTrue(False, "错误的是否有合适蜜源枚举, 编辑寻蜜日志成功")

    def test_mobile_detail_seek_without_route(self):
        """
        POST /mobile/work-log/edit-seek
        寻蜜路线为空, 编辑寻蜜日志成功
        :return:
        """
        work_log = self.wrs.query_seek_log_by_email(self.email)[0]
        seek_log_id = work_log["id"]
        json_response = self.ba._mobile_work_log_edit_seek(logId_=seek_log_id, pics_="pics", flowerRemark_="",
                                                           remark_="remark", env_="",
                                                           isFit_=0, route_="", worker_="worker")
        if json_response["status"] == "ERROR":
            self.assertEqual("寻蜜路线不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "寻蜜路线为空, 编辑寻蜜日志成功")

    def test_mobile_detail_seek_without_worker(self):
        """
        POST /mobile/work-log/edit-seek
        在岗人员为空, 编辑寻蜜日志成功
        :return:
        """
        work_log = self.wrs.query_seek_log_by_email(self.email)[0]
        seek_log_id = work_log["id"]
        json_response = self.ba._mobile_work_log_edit_seek(logId_=seek_log_id, pics_="pics", flowerRemark_="",
                                                           remark_="remark", env_="",
                                                           isFit_=0, route_="寻蜜路线", worker_=None)
        if json_response["status"] == "ERROR":
            self.assertEqual("在岗人员不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "在岗人员为空, 编辑寻蜜日志成功")

    def test_mobile_detail_seek_without_id(self):
        """
        POST /mobile/work-log/detail-seek
        日志ID为空, 查询日志详情
        :return:
        """
        json_response = self.ba._mobile_work_log_detail_seek(id_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("日志ID不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "日志ID为空, 查询日志详情成功")

    def test_mobile_detail_seek_with_wrong_id(self):
        """
        POST /mobile/work-log/detail-seek
        日志ID为空, 查询日志详情
        :return:
        """
        work_log = self.wrs.query_keep_log_by_email(self.email)[0]
        keep_log_id = work_log["id"]
        json_response = self.ba._mobile_work_log_detail_seek(id_=keep_log_id)
        if json_response["status"] == "ERROR":
            self.assertEqual("日志不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "日志ID为空, 查询日志详情成功")

    def test_mobile_detail_seek_success(self):
        """
        POST /mobile/work-log/detail-seek
        正确寻蜜日志ID, 查询日志详情
        :return:
        """
        work_log = self.wrs.query_seek_log_by_email(self.email)[0]
        seek_log_id = work_log["id"]
        json_response = self.ba._mobile_work_log_detail_seek(id_=seek_log_id)
        if json_response["status"] == "OK":
            json_data = json_response["content"]
            self.assertEqual(json_data["address"], work_log["address"])
            self.assertEqual(json_data["isFit"], work_log["is_fit"])
            self.assertEqual(json_data["remark"], work_log["remark"])
            self.assertEqual(json_data["route"], work_log["route"])
            self.assertEqual(json_data["worker"], work_log["worker"])
            self.assertEqual(json_data["flowerRemark"], work_log["flower_remark"])
            self.assertEqual(json_data["env"], work_log["env"])
            self.assertEqual(json_data["pics"], work_log["pics"])
            self.assertEqual(json_data["id"], work_log["id"])
            self.assertEqual(json_data["creatorId"], work_log["tu.id"])
            self.assertEqual(json_data["creatorName"], work_log["username"])
            self.assertEqual(json_data["creatorHeadImg"], work_log["head_img"])
            create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(json_data["createTime"])/1000.0))
            self.assertEqual(create_time, work_log["create_time"])
            self.assertEqual(1, work_log["type"])
        else:
            self.assertTrue(False, "正确寻蜜日志ID, 查询日志失败")
