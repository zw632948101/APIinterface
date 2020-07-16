#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2020/04/14
@Author: xiujuan chen
"""


import unittest
from faker import Faker
from interfaces.flowerChaser.PassportAction import PassportAction
from utils.log import log
from utils.databaseConnection.RedisOperate import Redis
from testcase.flowerChaser.sql.Passport import PassportInfoSql


class RegisterLoginMain(unittest.TestCase):
    """
    接口文档: http://dev-passport.worldfarm.com/swagger-ui.html
    """
    pa = PassportAction()
    pis = PassportInfoSql()
    mobile = '19982917912'
    log.info("开始执行注册模块测试用例")
    fake = Faker()
    redis = Redis()
    pa.set_user(None)

    def test_admin_sso_verify_code_get(self):
        """
        POST /admin/sso/verify-code-get   V 1.0
        手机登录短信验证码
        :return:
        """
        self.pa._admin_sso_verify_code_get(mobile_=self.mobile, bizType_='MS_LOGIN')

    def test_login_and_automatic_login(self):
        """
        POST /admin/sso/sms-login  V 1.0
        手机号短信验证登录
        POST /admin/sso/automatic-login V 1.0
        自动登录
        :return:
        """
        response = self.pa._admin_sso_sms_login(appId_='FLOWER_CHASERS', mobile_=self.mobile, verifyCode_='8888',
                                                deviceType_='WEB', deviceId_=None)
        token = response["content"]["token"]
        encryptedPwd = response["content"]["encryptedPwd"]
        deviceId = response["content"]["deviceId"]
        self.pa._admin_sso_automatic_login(token_=token, encryptedPwd_=encryptedPwd, deviceId_=deviceId)

    def test_admin_sso_logout(self):
        """
        POST /admin/sso/logout  V 1.0
        退出登录
        :return:
        """
        response = self.pa._admin_sso_logout()
        self.assertEqual("OK", response["status"])




