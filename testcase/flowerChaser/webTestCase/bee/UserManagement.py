#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2020/04/14
@Author: xiujuan chen
"""


import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log.logger import logger
from faker import Faker
from testcase.flowerChaser.sql.Passport import PassportInfoSql
import random


class RegisterLoginMain(unittest.TestCase):
    """
    接口文档: http://192.168.62.242:36054/swagger-ui.html
    """
    ba = BeeAction()
    ps = PassportInfoSql()
    mobile = '19982917912'
    log = logger('BeeInformationMain').logger
    log.info("开始执行用户管理模块测试用例")
    fake = Faker(locale="zh_CN")
    ba.set_user(mobile)

    def test_admin_fc_user_current_info(self):
        """
        POST /admin/fc-user/current-info  V 1.0
        用户管理-当前登录用户信息
        :return:
        """
        self.ba._admin_fc_user_current_info()

    def test_admin_fc_user_set_role(self):
        """
        POST /admin/fc-user/set-role  V 1.0
        用户管理-角色调整
        :return:
        """
        user_info_list = self.ps.query_user_info_by_phone(phone=self.mobile)
        user_id = user_info_list[0]['id']
        key_dict = {1000: '蜂友', 1001: '管理员', 1002: '养蜂总监', 1003: '养蜂技师', 1004: '养蜂助理', 1005: '项目经理',
                    1006: '项目专员', 1007: '后端运营'}
        key = random.choice(list(key_dict))
        self.ba._admin_fc_user_set_role(userId_=user_id, key_=key)

    def test_admin_fc_user_detail(self):
        """
        POST /admin/fc-user/detail  V 1.0
        用户管理-详情
        :return:
        """
        user_info_list = self.ps.query_user_info_by_phone(phone=self.mobile)
        user_id = user_info_list[0]['id']
        self.ba._admin_fc_user_detail(userId_=user_id)

    def test_admin_fc_user_role_count(self):
        """
        POST /admin/fc-user/role-count  V 1.0
        用户管理-分类统计
        :return:
        """
        self.ba._admin_fc_user_role_count()

    def test_admin_fc_user_page_list(self):
        """
        POST /admin/fc-user/page-list  V 1.0
        用户管理-分页列表
        :return:
        """
        role_type_dict = {0: '全部', 1: '养蜂老师', 2: '内部员工', 3: '外部蜂农'}
        role_type = random.choice(list(role_type_dict))
        order_type_dict = ['ASC', 'DESC']
        order_type = order_type_dict[random.randint(0, (len(order_type_dict))-1)]
        self.ba._admin_fc_user_page_list(pn_=10, ps_=10, roleType_=role_type, userInfo_=None, userStatus_=None,
                                         rgStartTime_=None, rgEndTime_=None, rgOrderType_=order_type,
                                         loStartTime_=None, loEndTime_=None, loOrderType_=order_type)

    def test_admin_fc_user_freeze(self):
        """
        POST /admin/fc-user/freeze  V 1.0
        用户管理-冻结，解冻
        :return:
        """
        user_info_list = self.ps.query_user_info_by_phone(phone='19982917912')
        user_id = user_info_list[0]['id']
        status_dict = {1: '正常', 2: '冻结'}
        status = random.choice(list(status_dict))
        self.ba._admin_fc_user_freeze(userId_=user_id, status_=status)
        user_info_sql = self.ps.query_user_info_by_id(user_id=user_id)
        self.assertEqual(status, user_info_sql[0]['status'])

    def test_admin_fc_user_permission_check(self):
        """
        POST /admin/fc-user/permission-check  V 1.0
        用户管理-登录权限校验
        :return:
        """
        self.ba._admin_fc_user_permission_check()

    def test_admin_excel_export_user(self):
        """
        GET /admin/excel-export/user  V 1.0
        用户列表导出
        :return:
        """
        role_type_dict = {0: '全部', 1: '养蜂老师', 2: '内部员工', 3: '外部蜂农'}
        role_type = random.choice(list(role_type_dict))
        order_type_dict = ['ASC', 'DESC']
        order_type = order_type_dict[random.randint(0, (len(order_type_dict)) - 1)]
        status_dict = {1: '正常', 2: '冻结'}
        status = random.choice(list(status_dict))
        response = self.ba._admin_excel_export_user(pn_=10, ps_=10, roleType_=role_type, userInfo_=None,
                                                    userStatus_=status, rgStartTime_=None, rgEndTime_=None,
                                                    rgOrderType_=order_type, loStartTime_=None, loEndTime_=None,
                                                    loOrderType_=order_type)
        f = open("用户信息导出_20200416.xlxs", 'wb+')
        f.write(response)
        f.close()

    def test_admin_fc_user_log_list(self):
        """
        POST /admin/fc-user/log/list  V 1.0
        操作日志-列表
        :return:
        """
        user_info_list = self.ps.query_user_info_by_phone(phone='19982917912')
        user_id = user_info_list[0]['id']
        self.ba._admin_fc_user_log_list(userId_=user_id)

    def test_admin_fc_user_log_page_list(self):
        """
        POST /admin/fc-user/log/page-list  V 1.0
        操作日志-分页列表
        :return:
        """
        user_info_list = self.ps.query_user_info_by_phone(phone='19982917912')
        user_id = user_info_list[0]['id']
        self.ba._admin_fc_user_log_page_list(pn_=5, ps_=10, userId_=user_id)
