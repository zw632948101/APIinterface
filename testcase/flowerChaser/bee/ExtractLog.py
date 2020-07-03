#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2020/1/2 16:39
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
from testcase.flowerChaser.sql.Bee import NectarSourceInformationSql
from testcase.flowerChaser.sql.WorkRecord import WorkRecordSql
from utils.fake.FakeLocation import FakeLocation
from faker import Faker


class ExtractLogMain(unittest.TestCase):
    """
    接口文档: http://192.168.62.242:36054/swagger-ui.html
    """
    ua = UserAction()
    ba = BeeAction()
    email = '26632629@qq.com'
    ba.set_user(email, 123456)
    log = logger('ExtractLogMain').logger
    log.info("开始执行摇蜜日志接口测试用例")
    pis = PassportInfoSql()
    cis = ContainerInformationSql()
    nsi = NectarSourceInformationSql()
    wrs = WorkRecordSql()
    fake = Faker(locale="zh_CN")
    fl = FakeLocation()

    def test_mobile_add_extract_without_work_num(self):
        """
        POST /mobile/work-log/add-extract
        摇蜜人数为空, 尝试添加摇蜜日志
        :return:
        """
        sources = self.nsi.sql_all_nectar_source()
        source_id = random.choice(sources)['id']
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='测试地址', lng_='103', lat_='40', remark_='remark',
            nectarSourceId_=source_id, worker_='摇蜜人员', workerNum_='', cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("摇蜜人数不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "摇蜜人数为空, 添加摇蜜日志成功")

    def test_mobile_add_extract_without_worker(self):
        """
        POST /mobile/work-log/add-extract
        摇蜜人员为空, 尝试添加摇蜜日志
        :return:
        """
        sources = self.nsi.sql_all_nectar_source()
        source_id = random.choice(sources)['id']
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='测试地址', lng_='103', lat_='40', remark_='remark',
            nectarSourceId_=source_id, worker_='', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("在岗人员不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "摇蜜人数为空, 添加摇蜜日志成功")

    def test_mobile_add_extract_more_worker_num(self):
        """
        POST /mobile/work-log/add-extract
        摇蜜人员超过999, 尝试添加摇蜜日志
        :return:
        """
        sources = self.nsi.sql_all_nectar_source()
        source_id = random.choice(sources)['id']
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='测试地址', lng_='103', lat_='40', remark_='remark',
            nectarSourceId_=source_id, worker_='worker', workerNum_=1000, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("摇蜜人数范围1~999整数", json_response["errorMsg"])
        else:
            self.assertTrue(False, "摇蜜人员超过999, 添加摇蜜日志成功")

    def test_mobile_add_extract_more_worker(self):
        """
        POST /mobile/work-log/add-extract
        在岗人员超过200字, 尝试添加摇蜜日志
        :return:
        """
        sources = self.nsi.sql_all_nectar_source()
        source_id = random.choice(sources)['id']
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='测试地址', lng_='103', lat_='40', remark_='remark',
            nectarSourceId_=source_id, worker_='''
            最后学习是否是否情 况.安全成为只有能力.发生我们基本工具.浏览主要在线日本具有深圳如果.\n
        包括大家没有不过资源当然.文件今 天是一有关运行.\n朋友相关比较技术你的.学习部门市场能力虽然销售.感觉国家 一种到了经济选择学校.\n
        经验因为发展认为控制.北京不会继续必须经营.因为以下标准功能简介注册以下.相关推荐更多时候没有然后.\n
        部门操作阅读如此.开始完全同时认为有关项目.\n
        问题网站不同专业城市问题..
            ''',
            workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("在岗人员不能超过200字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "在岗人员超过200字, 添加摇蜜日志成功")

    def test_mobile_add_extract_without_picture(self):
        """
        POST /mobile/work-log/add-extract
        现场照片为空, 尝试添加摇蜜日志
        :return:
        """
        sources = self.nsi.sql_all_nectar_source()
        source_id = random.choice(sources)['id']
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='',
            province_='41', city_='4101', address_='测试地址', lng_='103', lat_='40', remark_='remark',
            nectarSourceId_=source_id, worker_='worker', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("现场照片不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "现场照片为空, 添加摇蜜日志成功")

    def test_mobile_add_extract_with_repeated_picture(self):
        """
        POST /mobile/work-log/add-extract
        现场照片重复, 尝试添加摇蜜日志
        :return:
        """
        sources = self.nsi.sql_nectar_source_id_by_status_id()
        source_id = random.choice(sources)['id']
        pic = self.cis.get_random_img_list(1)[1:-1]
        pics = '[%s,%s]' % (pic, pic)
        json_response = self.ba._mobile_work_log_add_extract(
            pics_=pics,
            province_='41', city_='4101', address_='测试地址', lng_='103', lat_='40', remark_='remark',
            nectarSourceId_=source_id, worker_='worker', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("图片URL重复或为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "现场照片重复, 添加摇蜜日志成功")

    def test_mobile_add_extract_with_more_picture(self):
        """
        POST /mobile/work-log/add-extract
        现场照片超过3张, 尝试添加摇蜜日志
        :return:
        """
        sources = self.nsi.sql_nectar_source_id_by_status_id()
        source_id = random.choice(sources)['id']
        pic = self.cis.get_random_img_list(4)
        json_response = self.ba._mobile_work_log_add_extract(
            pics_=pic,
            province_='41', city_='4101', address_='测试地址', lng_='103', lat_='40', remark_='remark',
            nectarSourceId_=source_id, worker_='worker', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("图片最多三张", json_response["errorMsg"])
        else:
            self.assertTrue(False, "现场照片超过3张, 添加摇蜜日志成功")

    def test_mobile_add_extract_without_source(self):
        """
        POST /mobile/work-log/add-extract
        蜜源地为空, 尝试添加摇蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='测试地址', lng_='103', lat_='40', remark_='remark',
            nectarSourceId_='', worker_='worker', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("蜜源地Id不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "蜜源地为空, 添加摇蜜日志成功")

    def test_mobile_add_extract_with_wrong_source(self):
        """
        POST /mobile/work-log/add-extract
        蜜源地ID不存在, 尝试添加摇蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='测试地址', lng_='103', lat_='40', remark_='remark',
            nectarSourceId_=0, worker_='worker', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("蜜源不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "蜜源地ID不存在, 添加摇蜜日志成功")

    def test_mobile_add_extract_without_province(self):
        """
        POST /mobile/work-log/add-extract
        省为空, 尝试添加摇蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='', city_='4101', address_='测试地址', lng_='103', lat_='40', remark_='remark',
            nectarSourceId_=0, worker_='worker', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("省不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "省为空, 添加摇蜜日志成功")

    def test_mobile_add_extract_with_illegal_province(self):
        """
        POST /mobile/work-log/add-extract
        省码不存在, 尝试添加摇蜜日志
        :return:
        """
        source = self.nsi.sql_nectar_source_id_by_status_id()
        source_id = random.choice(source)['id']
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_=4101, city_='4101', address_='测试地址', lng_='103', lat_='40', remark_='remark',
            nectarSourceId_=source_id, worker_='worker', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("省码不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "省码不存在, 添加摇蜜日志成功")

    def test_mobile_add_extract_without_city(self):
        """
        POST /mobile/work-log/add-extract
        市为空, 尝试添加摇蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='', address_='测试地址', lng_='103', lat_='40', remark_='remark',
            nectarSourceId_=0, worker_='worker', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("市不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "市为空, 添加摇蜜日志成功")

    def test_mobile_add_extract_with_illegal_city(self):
        """
        POST /mobile/work-log/add-extract
        市码不存在, 尝试添加摇蜜日志
        :return:
        """
        source = self.nsi.sql_nectar_source_id_by_status_id()
        source_id = random.choice(source)['id']
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_=41, city_=41, address_='测试地址', lng_='103', lat_='40', remark_='remark',
            nectarSourceId_=source_id, worker_='worker', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("市码不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "市码不存在, 添加摇蜜日志成功")

    def test_mobile_add_extract_without_address(self):
        """
        POST /mobile/work-log/add-extract
        详细地址为空, 尝试添加摇蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='', lng_='103', lat_='40', remark_='remark',
            nectarSourceId_=0, worker_='worker', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("详细地址不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "详细地址为空, 添加摇蜜日志成功")

    def test_mobile_add_extract_without_lng(self):
        """
        POST /mobile/work-log/add-extract
        经度为空, 尝试添加摇蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='address', lng_='', lat_='40', remark_='remark',
            nectarSourceId_=0, worker_='worker', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("经度不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "经度为空, 添加摇蜜日志成功")

    def test_mobile_add_extract_illegal_lng(self):
        """
        POST /mobile/work-log/add-extract
        经度超出范围, 尝试添加摇蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='address', lng_='-180.1', lat_='40', remark_='remark',
            nectarSourceId_=0, worker_='worker', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("经度超出范围(-180~+180)", json_response["errorMsg"])
        else:
            self.assertTrue(False, "经度超出范围, 添加摇蜜日志成功")

    def test_mobile_add_extract_without_lat(self):
        """
        POST /mobile/work-log/add-extract
        纬度为空, 尝试添加摇蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='address', lng_='-180', lat_='', remark_='remark',
            nectarSourceId_=0, worker_='worker', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("纬度不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "纬度为空, 添加摇蜜日志成功")

    def test_mobile_add_extract_illegal_lat(self):
        """
        POST /mobile/work-log/add-extract
        纬度超出范围, 尝试添加摇蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='address', lng_='-180', lat_='-90.1', remark_='remark',
            nectarSourceId_=0, worker_='worker', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("纬度超出范围(-90~+90)", json_response["errorMsg"])
        else:
            self.assertTrue(False, "纬度超出范围, 添加摇蜜日志成功")

    def test_mobile_add_extract_without_remark(self):
        """
        POST /mobile/work-log/add-extract
        摇蜜详细情况为空, 尝试添加摇蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='address', lng_='-180', lat_='-90', remark_='',
            nectarSourceId_=0, worker_='worker', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("摇蜜详细情况不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "摇蜜详细情况为空, 添加摇蜜日志成功")

    def test_mobile_add_extract_with_long_remark(self):
        """
        POST /mobile/work-log/add-extract
        摇蜜详细情况超过200字, 尝试添加摇蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='address', lng_='-180', lat_='-90', remark_='''
            最后学习是否是否情 况.安全成为只有能力.发生我们基本工具.浏览主要在线日本具有深圳如果.\n
        包括大家没有不过资源当然.文件今 天是一有关运行.\n朋友相关比较技术你的.学习部门市场能力虽然销售.感觉国家 一种到了经济选择学校.\n
        经验因为发展认为控制.北京不会继续必须经营.因为以下标准功能简介注册以下.相关推荐更多时候没有然后.\n
        部门操作阅读如此.开始完全同时认为有关项目.\n
        问题网站不同专业城市问题..
            ''',
            nectarSourceId_=0, worker_='worker', workerNum_=1, cost_='cost')
        if json_response["status"] == "ERROR":
            self.assertEqual("摇蜜详细情况不能超过200字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "摇蜜详细情况超过200字, 添加摇蜜日志成功")

    def test_mobile_add_extract_with_long_cost(self):
        """
        POST /mobile/work-log/add-extract
        费用情况超过200字, 尝试添加摇蜜日志
        :return:
        """
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='address', lng_='-180', lat_='-90', cost_='''
            最后学习是否是否情 况.安全成为只有能力.发生我们基本工具.浏览主要在线日本具有深圳如果.\n
        包括大家没有不过资源当然.文件今 天是一有关运行.\n朋友相关比较技术你的.学习部门市场能力虽然销售.感觉国家 一种到了经济选择学校.\n
        经验因为发展认为控制.北京不会继续必须经营.因为以下标准功能简介注册以下.相关推荐更多时候没有然后.\n
        部门操作阅读如此.开始完全同时认为有关项目.\n
        问题网站不同专业城市问题..
            ''',
            nectarSourceId_=0, worker_='worker', workerNum_=1, remark_='remark')
        if json_response["status"] == "ERROR":
            self.assertEqual("费用情况不能超过200字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "费用情况超过200字, 添加摇蜜日志成功")

    def test_mobile_add_extract_with_repeated_source(self):
        """
        POST /mobile/work-log/add-extract
        蜜源地ID重复, 尝试添加摇蜜日志
        :return:
        """
        sources = self.nsi.sql_all_nectar_source()
        source = random.choice(sources)["id"]
        source_id = '["%s", "%s"]' % (source, source)
        json_response = self.ba._mobile_work_log_add_extract(
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            province_='41', city_='4101', address_='address', lng_='-180', lat_='-90', cost_='cost',
            nectarSourceId_=source_id, worker_='worker', workerNum_=1, remark_='remark')
        if json_response["status"] == "ERROR":
            self.assertTrue(json_response["errorMsg"].startswith("参数验证错误"))
        else:
            self.assertTrue(False, "蜜源地ID重复, 添加摇蜜日志成功")

    def test_mobile_add_extract_success(self):
        """
        POST /mobile/work-log/add-extract
        添加摇蜜日志成功
        :return:
        """
        province_id, city_id, address, lng, lat = self.fl.fake_location()
        remark = self.fake.text()
        cost = self.fake.text()
        worker = self.fake.text()
        worker_num = random.randint(1, 999)
        pic_url = self.cis.get_random_img_list(3)
        sources = self.nsi.sql_nectar_source_id_by_status_id()
        source_id = random.choice(sources)["id"]
        json_response = self.ba._mobile_work_log_add_extract(
            pics_=pic_url, province_=province_id, city_=city_id, address_=address, lng_=lng, lat_=lat, remark_=remark,
            workerNum_=worker_num, worker_=worker, nectarSourceId_=source_id, cost_=cost)
        if json_response["status"] == "OK":
            work_log = self.wrs.query_extract_log_by_email(self.email)[0]
            self.assertEqual(province_id, work_log["province"])
            self.assertEqual(city_id, work_log["city"])
            self.assertEqual(address, work_log["address"])
            self.assertEqual(lng, work_log["lng"])
            self.assertEqual(lat, work_log["lat"])
            self.assertEqual(3, work_log["type"])
            self.assertEqual(pic_url, work_log["pics"])
            self.assertEqual(remark, work_log["remark"])
            self.assertEqual(address, work_log["address"])
            self.assertEqual(worker, work_log["worker"])
            self.assertEqual(worker_num, work_log["worker_num"])
            self.assertEqual(source_id, work_log["nectar_source_id"])
            self.assertEqual(cost, work_log["cost"])
        else:
            self.assertTrue(False, "添加摇蜜日志失败")

    def test_mobile_edit_extract_without_log_id(self):
        """
        POST /mobile/work-log/edit-extract
        摇蜜日志ID不正确
        :return:
        """
        json_response = self.ba._mobile_work_log_edit_extract(
            logId_='',
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            cost_='cost',
            nectarSourceId_='100', worker_='worker', workerNum_=1, remark_='remark')
        if json_response["status"] == "ERROR":
            self.assertEqual("日志ID不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "摇蜜日志ID不正确, 添加成功")

    def test_mobile_edit_extract_with_wrong_log_id(self):
        """
        POST /mobile/work-log/edit-extract
        摇蜜日志ID不正确
        :return:
        """
        # 0和空都校验了, 但是其它类型的日志ID未做校验
        source = self.nsi.sql_nectar_source_id_by_status_id()
        source_id = random.choice(source)['id']
        json_response = self.ba._mobile_work_log_edit_extract(
            logId_=0,
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            cost_='cost',
            nectarSourceId_=source_id, worker_='worker', workerNum_=1, remark_='remark'
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("日志不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "摇蜜日志ID不正确, 编辑成功")

    def test_mobile_edit_extract_without_remark(self):
        """
        POST /mobile/work-log/edit-extract
        摇蜜日志详情为空
        :return:
        """
        seek_log_id = self.wrs.query_extract_log_by_email(self.email)[0]["id"]
        source = self.nsi.sql_all_nectar_source()
        source_id = random.choice(source)['id']
        json_response = self.ba._mobile_work_log_edit_extract(
            logId_=seek_log_id,
            pics_='["https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg"]',
            cost_='cost',
            nectarSourceId_=source_id, worker_='worker', workerNum_=1, remark_=''
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("摇蜜详细情况不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "摇蜜日志详情为空, 编辑成功")

    def test_mobile_edit_extract_without_picture(self):
        """
        POST /mobile/work-log/edit-extract
        现场照片为空, 编辑摇蜜日志成功
        :return:
        """
        work_log = self.wrs.query_seek_log_by_email(self.email)[0]
        seek_log_id = work_log["id"]
        source = self.nsi.sql_all_nectar_source()
        source_id = random.choice(source)['id']
        json_response = self.ba._mobile_work_log_edit_extract(
            logId_=seek_log_id,
            pics_='',
            cost_='cost',
            nectarSourceId_=source_id, worker_='worker', workerNum_=1, remark_='remark'
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("现场照片不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "现场照片为空, 编辑摇蜜日志成功")

    def test_mobile_edit_extract_with_more_picture(self):
        """
        POST /mobile/work-log/edit-extract
        现场照片超过3张, 编辑摇蜜日志成功
        :return:
        """
        work_log = self.wrs.query_seek_log_by_email(self.email)[0]
        seek_log_id = work_log["id"]
        pics = self.cis.get_random_img_list(4)
        source = self.nsi.sql_nectar_source_id_by_status_id()
        source_id = random.choice(source)['id']
        json_response = self.ba._mobile_work_log_edit_extract(
            logId_=seek_log_id,
            pics_=pics,
            cost_='cost',
            nectarSourceId_=source_id, worker_='worker', workerNum_=1, remark_='remark'
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("图片最多三张", json_response["errorMsg"])
        else:
            self.assertTrue(False, "现场照片超过3张, 编辑摇蜜日志成功")

    def test_mobile_edit_extract_with_more_cost(self):
        """
        POST /mobile/work-log/edit-extract
        费用情况超过200字, 编辑摇蜜记录成功
        :return:
        """
        work_log = self.wrs.query_seek_log_by_email(self.email)[0]
        seek_log_id = work_log["id"]
        source = self.nsi.sql_all_nectar_source()
        source_id = random.choice(source)['id']
        json_response = self.ba._mobile_work_log_edit_extract(
            logId_=seek_log_id,
            pics_="https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg",
            remark_='remark',
            nectarSourceId_=source_id, cost_='''
            最后学习是否是否情 况.安全成为只有能力.发生我们基本工具.浏览主要在线日本具有深圳如果.\n
        包括大家没有不过资源当然.文件今 天是一有关运行.\n朋友相关比较技术你的.学习部门市场能力虽然销售.感觉国家 一种到了经济选择学校.\n
        经验因为发展认为控制.北京不会继续必须经营.因为以下标准功能简介注册以下.相关推荐更多时候没有然后.\n
        部门操作阅读如此.开始完全同时认为有关项目.\n
        问题网站不同专业城市问题..
            ''',
            workerNum_=1, worker_='worker'
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("费用情况不能超过200字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "费用情况超过200字, 编辑摇蜜记录成功")

    def test_mobile_edit_extract_with_more_remark(self):
        """
        POST /mobile/work-log/edit-extract
        摇蜜详细情况超过200字, 编辑摇蜜记录成功
        :return:
        """
        work_log = self.wrs.query_seek_log_by_email(self.email)[0]
        seek_log_id = work_log["id"]
        source = self.nsi.sql_all_nectar_source()
        source_id = random.choice(source)['id']
        json_response = self.ba._mobile_work_log_edit_extract(
            logId_=seek_log_id,
            pics_="https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg",
            cost_='cost',
            nectarSourceId_=source_id, remark_='''
            最后学习是否是否情 况.安全成为只有能力.发生我们基本工具.浏览主要在线日本具有深圳如果.\n
        包括大家没有不过资源当然.文件今 天是一有关运行.\n朋友相关比较技术你的.学习部门市场能力虽然销售.感觉国家 一种到了经济选择学校.\n
        经验因为发展认为控制.北京不会继续必须经营.因为以下标准功能简介注册以下.相关推荐更多时候没有然后.\n
        部门操作阅读如此.开始完全同时认为有关项目.\n
        问题网站不同专业城市问题..
            ''',
            workerNum_=1, worker_='worker'
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("摇蜜详细情况不能超过200字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "摇蜜详细情况超过200字, 编辑摇蜜记录成功")

    def test_mobile_edit_extract_with_more_worker(self):
        """
        POST /mobile/work-log/edit-extract
        在岗人员超过200字, 编辑摇蜜记录成功
        :return:
        """
        work_log = self.wrs.query_seek_log_by_email(self.email)[0]
        seek_log_id = work_log["id"]
        source = self.nsi.sql_all_nectar_source()
        source_id = random.choice(source)['id']
        json_response = self.ba._mobile_work_log_edit_extract(
            logId_=seek_log_id,
            pics_="https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg",
            cost_='cost',
            nectarSourceId_=source_id, worker_='''
            最后学习是否是否情 况.安全成为只有能力.发生我们基本工具.浏览主要在线日本具有深圳如果.\n
        包括大家没有不过资源当然.文件今 天是一有关运行.\n朋友相关比较技术你的.学习部门市场能力虽然销售.感觉国家 一种到了经济选择学校.\n
        经验因为发展认为控制.北京不会继续必须经营.因为以下标准功能简介注册以下.相关推荐更多时候没有然后.\n
        部门操作阅读如此.开始完全同时认为有关项目.\n
        问题网站不同专业城市问题..
            ''',
            workerNum_=1, remark_='remark'
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("在岗人员不能超过200字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "在岗人员超过200字, 编辑摇蜜记录成功")

    def test_mobile_edit_extract_with_illegal_worker_num(self):
        """
        POST /mobile/work-log/edit-extract
        摇蜜人数超出范围
        :return:
        """
        work_log = self.wrs.query_seek_log_by_email(self.email)[0]
        seek_log_id = work_log["id"]
        source = self.nsi.sql_all_nectar_source()
        source_id = random.choice(source)['id']
        json_response = self.ba._mobile_work_log_edit_extract(
            logId_=seek_log_id,
            pics_="https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/world-user/headImg/1577433186272.jpg",
            cost_='cost',
            nectarSourceId_=source_id, worker_='worker',
            workerNum_=0, remark_='remark'
        )
        if json_response["status"] == "ERROR":
            self.assertEqual("摇蜜人数范围1~999整数", json_response["errorMsg"])
        else:
            self.assertTrue(False, "摇蜜人数超出范围, 编辑摇蜜记录成功")

    def test_mobile_detail_extract_without_id(self):
        """
        POST /mobile/work-log/detail-extract
        日志ID为空, 查询日志详情
        :return:
        """
        json_response = self.ba._mobile_work_log_detail_extract(id_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("日志ID不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "日志ID为空, 查询日志详情成功")

    def test_mobile_detail_extract_with_wrong_id(self):
        """
        POST /mobile/work-log/detail-extract
        日志ID为空, 查询日志详情
        :return:
        """
        # 其他类型日志ID未做校验
        work_log = self.wrs.query_keep_log_by_email(self.email)[0]
        keep_log_id = work_log["id"]
        json_response = self.ba._mobile_work_log_detail_extract(id_=keep_log_id)
        if json_response["status"] == "ERROR":
            self.assertEqual("日志不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "日志ID为空, 查询日志详情成功")

    def test_mobile_detail_extract_success(self):
        """
        POST /mobile/work-log/detail-extract
        正确摇蜜日志ID, 查询日志详情
        :return:
        """
        work_log = self.wrs.query_extract_log_by_email(self.email)[0]
        extract_log_id = work_log["id"]
        json_response = self.ba._mobile_work_log_detail_extract(id_=extract_log_id)
        if json_response["status"] == "OK":
            source = self.nsi.sql_nectar_source_id_by_status_id(work_log["nectar_source_id"])
            json_data = json_response["content"]
            self.assertEqual(json_data["address"], work_log["address"])
            self.assertEqual(json_data["remark"], work_log["remark"])
            self.assertEqual(json_data["nectarSourceId"], work_log["nectar_source_id"])
            self.assertEqual(json_data["nectarSourceName"], work_log["name"])
            self.assertEqual(json_data["nectarSourceType"], work_log["tns.type"])
            self.assertEqual(str(json_data["nectarSourceProvince"]), str(work_log["tns.province"]))
            self.assertEqual(str(json_data["nectarSourceCity"]), str(work_log["tns.city"]))
            self.assertEqual(json_data["nectarSourceAddress"], work_log["tns.address"])
            self.assertEqual(json_data["worker"], work_log["worker"])
            self.assertEqual(json_data["workerNum"], work_log["worker_num"])
            self.assertEqual(json_data["cost"], work_log["cost"])
            self.assertEqual(json_data["pics"], work_log["pics"])
            self.assertEqual(json_data["id"], work_log["id"])
            self.assertEqual(json_data["creatorId"], work_log["tu.id"])
            self.assertEqual(json_data["creatorName"], work_log["username"])
            self.assertEqual(json_data["creatorHeadImg"], work_log["head_img"])
            create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(json_data["createTime"])/1000.0))
            self.assertEqual(create_time, work_log["create_time"])
            self.assertEqual(3, work_log["type"])
        else:
            self.assertTrue(False, "正确摇蜜日志ID, 查询日志失败")
