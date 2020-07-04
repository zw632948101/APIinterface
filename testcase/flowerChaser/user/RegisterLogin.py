#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2019 2019/12/27 10:51
@Author: hengxin
"""


import unittest
import json
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
    mobile = '19988776655'
    log.info("开始执行注册模块测试用例")
    fake = Faker()
    redis = Redis()
    pa.set_user(None)

    def test_email_register_without_required(self):
        """
        POST /mobile/sso/email-registe
        注册判断顺序: 姓名>邮箱>密码
        :return:
        """
        json_response = self.pa._mobile_sso_email_registe(appId_='FLOWER_CHASERS', deviceType_='IOS',
                                                          deviceId_='mac_kNIGHT',
                                                          account_='', userName_='', password_='', headImg_='')
        if json_response["status"] == "ERROR":
            self.assertEqual(True, json_response["errorMsg"].endswith("不能为空"))
        else:
            self.assertTrue(False, "注册判断顺序错误: 姓名>邮箱>密码")

    def test_email_register_without_username(self):
        """
        POST /mobile/sso/email-registe
        注册姓名不能为空
        :return:
        """
        json_response = self.pa._mobile_sso_email_registe(appId_='FLOWER_CHASERS', deviceType_='ANDROID',
                                                          deviceId_='mac_kNIGHT', account_='26632629@qq.com',
                                                          userName_='', password_='123456', headImg_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("姓名不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "姓名为空, 注册成功")

    def test_email_register_without_mail(self):
        """
        POST /mobile/sso/email-registe
        注册邮箱不能为空
        :return:
        """
        json_response = self.pa._mobile_sso_email_registe(appId_='FLOWER_CHASERS', deviceType_='IOS',
                                                          deviceId_='mac_kNIGHT', account_='', userName_='姓名',
                                                          password_='123456', headImg_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("邮箱不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "邮箱为空, 注册成功")

    def test_email_register_without_password(self):
        """
        POST /mobile/sso/email-registe
        注册密码不能为空
        :return:
        """
        json_response = self.pa._mobile_sso_email_registe(appId_='FLOWER_CHASERS', deviceType_='ANDROID',
                                                          deviceId_='mac_kNIGHT', account_='26632629@qq.com',
                                                          userName_='姓名', password_='', headImg_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("密码不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "密码为空, 注册成功")

    def test_email_register_with_short_password(self):
        """
        POST /mobile/sso/email-registe
        注册密码小于6位
        :return:
        """
        json_response = self.pa._mobile_sso_email_registe(appId_='FLOWER_CHASERS', deviceType_='ANDROID',
                                                          deviceId_='mac_kNIGHT', account_='26632629@qq.com',
                                                          userName_='姓名', password_='12345', headImg_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("请输入6-15数字、字母密码", json_response["errorMsg"])
        else:
            self.assertTrue(False, "密码小于6位, 注册成功")

    def test_email_register_with_long_password(self):
        """
        POST /mobile/sso/email-registe
        注册密码大于15位
        :return:
        """
        json_response = self.pa._mobile_sso_email_registe(appId_='FLOWER_CHASERS', deviceType_='ANDROID',
                                                          deviceId_='mac_kNIGHT', account_='26632629@qq.com',
                                                          userName_='姓名', headImg_='', password_='1234567890123456')
        if json_response["status"] == "ERROR":
            self.assertEqual("请输入6-15数字、字母密码", json_response["errorMsg"])
        else:
            self.assertTrue(False, "密码大于15位, 注册成功")

    def test_email_register_with_non_alphanumeric(self):
        """
        POST /mobile/sso/email-registe
        注册密码含有非数字字母
        :return:
        """
        json_response = self.pa._mobile_sso_email_registe(appId_='FLOWER_CHASERS', deviceType_='ANDROID',
                                                          deviceId_='mac_kNIGHT', account_='26632629@qq.com',
                                                          userName_='姓名', headImg_='', password_='中文')
        if json_response["status"] == "ERROR":
            self.assertEqual("请输入6-15数字、字母密码", json_response["errorMsg"])
        else:
            self.assertTrue(False, "密码含有非字母或数字, 注册成功")

    def test_email_register_with_long_name(self):
        """
        POST /mobile/sso/email-registe
        注册姓名不能超过20个字
        :return:
        """
        json_response = self.pa._mobile_sso_email_registe(appId_='FLOWER_CHASERS', deviceType_='ANDROID',
                                                          deviceId_='mac_kNIGHT', account_='26632629@qq.com',
                                                          password_='123456', headImg_='',
                                                          userName_='注册时使用姓名字符串长度超过20字异常测试')
        if json_response["status"] == "ERROR":
            self.assertEqual("姓名不能超过20个字符", json_response["errorMsg"])
        else:
            self.assertTrue(False, "姓名大于20个字, 注册成功")

    def test_email_register_with_long_mail(self):
        """
        POST /mobile/sso/email-registe
        注册邮箱长度不能超过64位
        :return:
        """
        json_response = self.pa._mobile_sso_email_registe(
            appId_='FLOWER_CHASERS', deviceType_='ANDROID', deviceId_='mac_kNIGHT', userName_='姓名', password_='123456',
            headImg_='', account_='26632629266326292663262926632629266326292663262926632629@qq.com.au')
        if json_response["status"] == "ERROR":
            self.assertEqual("邮箱长度不能超过64字符", json_response["errorMsg"])
        else:
            self.assertTrue(False, "邮箱长度超过64位, 注册成功")

    def test_email_register_with_registered_mail(self):
        """
        POST /mobile/sso/email-registe
        注册邮箱已注册
        :return:
        """
        json_response = self.pa._mobile_sso_email_registe(
            appId_='FLOWER_CHASERS', deviceType_='ANDROID', deviceId_='mac_kNIGHT', userName_='姓名', password_='123456',
            headImg_='', account_='26632629@qq.com')
        if json_response["status"] == "ERROR":
            self.assertEqual("当前邮箱已注册，请重新输入", json_response["errorMsg"])
        else:
            self.assertTrue(False, "邮箱已注册, 注册成功")

    def test_email_register_success(self):
        """
        POST /mobile/sso/email-registe
        注册邮箱成功
        :return:
        """
        email = "535914342@qq.com"
        username = self.fake.name()
        json_response = self.pa._mobile_sso_email_registe(
            appId_='FLOWER_CHASERS', deviceType_='ANDROID', deviceId_='mac_kNIGHT',
            userName_=username, password_='123456',
            headImg_='', account_=email)
        if json_response["status"] == "OK":
            user_info = self.pis.query_user_by_email(email)[0]
            self.assertEqual(user_info["username"], username)
            self.assertEqual(user_info["email"], email)
            self.pis.update_specified_mail()
        else:
            self.assertTrue(False, "邮箱注册失败")

    def test_email_login_without_required(self):
        """
        POST /mobile/sso/email-login
        登录判断顺序: 邮箱>密码
        :return:
        """
        json_response = self.pa._mobile_sso_email_login(appId_='FLOWER_CHASERS', deviceType_='ANDROID',
                                                        deviceId_='mac_kNIGHT', account_='', password_='')
        if json_response["status"] == "ERROR":
            self.assertIn(json_response["errorMsg"], ["账号不能为空", "密码不能为空"])
        else:
            self.assertTrue(False, "登录判断顺序错误: 邮箱>密码")

    def test_email_login_without_mail(self):
        """
        POST /mobile/sso/email-login
        登录账号不能为空
        :return:
        """
        json_response = self.pa._mobile_sso_email_login(appId_='FLOWER_CHASERS', deviceType_='ANDROID',
                                                        deviceId_='mac_kNIGHT', account_='', password_='123456')
        if json_response["status"] == "ERROR":
            self.assertEqual("账号不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "账号为空, 登录成功")

    def test_email_login_with_new_mail(self):
        """
        POST /mobile/sso/email-login
        登录账号未注册
        :return:
        """
        json_response = self.pa._mobile_sso_email_login(
            appId_='FLOWER_CHASERS', deviceType_='ANDROID', deviceId_='mac_kNIGHT', password_='123456',
            account_='26632629266326292663262926632629266326292663262926632629@qq.com.au')
        if json_response["status"] == "ERROR":
            self.assertEqual("邮箱未注册，请重新输入", json_response["errorMsg"])
        else:
            self.assertTrue(False, "账号未注册, 登录成功")

    def test_email_login_without_password(self):
        """
        POST /mobile/sso/email-login
        登录密码不能为空
        :return:
        """
        json_response = self.pa._mobile_sso_email_login(appId_='FLOWER_CHASERS', deviceType_='ANDROID',
                                                        deviceId_='mac_kNIGHT', account_='abc@d.com', password_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("密码不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "密码为空, 登录成功")

    def test_email_login_with_mismatched(self):
        """
        POST /mobile/sso/email-login
        账号密码不匹配
        :return:
        """
        json_response = self.pa._mobile_sso_email_login(appId_='FLOWER_CHASERS', deviceType_='ANDROID',
                                                        deviceId_='mac_kNIGHT', account_='26632629@qq.com',
                                                        password_='26632628@qq.com')
        if json_response["status"] == "ERROR":
            self.assertEqual("账号或密码不正确，请重新输入", json_response["errorMsg"])
        else:
            self.assertTrue(False, "账号密码不匹配, 登录成功")

    def test_email_login_success(self):
        """
        POST /mobile/sso/email-login
        正确账号密码登录成功
        :return:
        """
        email = '26632629@qq.com'
        json_response = self.pa._mobile_sso_email_login(appId_='FLOWER_CHASERS', deviceType_='ANDROID',
                                                        deviceId_='mac_kNIGHT', account_=email, password_='123456')
        if json_response["status"] == "OK":
            token = self.pis.query_latest_token(email)[0]['token']
            self.assertEqual(token, json_response["content"]["token"])
            log.info('邮箱方式登录成功')
        else:
            self.assertTrue(False, "账号密码正确, 登录失败")

    def test_logout_success(self):
        """
        POST /mobile/sso/logout
        使用Header中的token登出
        :return:
        """
        self.pa.set_user("19988776655")
        json_response = self.pa._mobile_sso_logout()
        if json_response["status"] == "OK":
            pass
        else:
            self.assertTrue(False, "登出失败")

    def test_get_verify_code_without_biz_type(self):
        """
        POST /mobile/sso/verify-code-get
        业务类型为空, 发送验证码
        :return:
        """
        json_response = self.pa._mobile_sso_verify_code_get(mobile_='19988776655',
                                                            bizType_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("业务类型不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "业务类型为空, 发送验证码成功")

    def test_get_verify_code_without_mobile(self):
        """
        POST /mobile/sso/verify-code-get
        手机号为空, 发送验证码
        :return:
        """
        json_response = self.pa._mobile_sso_verify_code_get(mobile_=None,
                                                            bizType_='MS_LOGIN')
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号为空, 发送验证码成功")

    def test_get_verify_code_with_unregister_mobile(self):
        """
        POST /mobile/sso/verify-code-get
        未注册手机号发送验证码
        :return:
        """
        json_response = self.pa._mobile_sso_verify_code_get(mobile_='18877665544',
                                                            bizType_='MS_LOGIN')
        if json_response["status"] == "OK":
            log.info('未注册手机号验证码获取成功')
        else:
            self.assertTrue(False, "手机号和验证码正确, 登录失败")

    def test_get_verify_code_with_wrong_mobile(self):
        """
        POST /mobile/sso/verify-code-get
        手机号格式有误, 发送验证码
        :return:
        """
        json_response = self.pa._mobile_sso_verify_code_get(mobile_='11202831234',
                                                            bizType_='MS_LOGIN')
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号格式有误, 发送验证码成功")

    def test_get_verify_code_with_long_mobile(self):
        """
        POST /mobile/sso/verify-code-get
        手机号大于11位, 发送验证码
        :return:
        """
        json_response = self.pa._mobile_sso_verify_code_get(mobile_='186028325723',
                                                            bizType_='MS_LOGIN')
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号格式有误, 发送验证码成功")

    def test_get_verify_code_with_short_mobile(self):
        """
        POST /mobile/sso/verify-code-get
        手机号短于11位, 发送验证码
        :return:
        """
        json_response = self.pa._mobile_sso_verify_code_get(mobile_='186028325723',
                                                            bizType_='MS_LOGIN')
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号格式有误, 发送验证码成功")

    def test_get_verify_code_with_max_time(self):
        """
        POST /mobile/sso/verify-code-get
        当日验证码发送超过10次, 继续尝试
        :return:
        """
        self.redis.set('SmsVerifyCode:MobileLogin:18602832572:times', 10)
        json_response = self.pa._mobile_sso_verify_code_get(mobile_='18602832572',
                                                            bizType_='MS_LOGIN')
        if json_response["status"] == "ERROR":
            self.assertEqual("今天短信验证码次数已经用完", json_response["errorMsg"])
        else:
            self.assertTrue(False, "当日验证码发送超过10次后, 发送验证码成功")

    def get_verify_code_success(self):
        """
        POST /mobile/sso/verify-code-get
        正确手机号, 发送验证码
        :return:
        """
        self.redis.set('SmsVerifyCode:MobileLogin:19988776655:times', 1)
        json_response = self.pa._mobile_sso_verify_code_get(mobile_=self.mobile,
                                                            bizType_='MS_LOGIN')
        if json_response["status"] == "OK":
            verify_code = json.loads(self.redis.get('SmsVerifyCode:MobileLogin:19988776655:code'))['code']
            log.info('手机号 %s, 短信已发送, 验证码 %s' % (self.mobile, verify_code))
            return verify_code
        else:
            self.assertTrue(False, "正确手机号, 发送验证码失败")

    def test_mobile_sso_sms_login_without_app_id(self):
        """
        POST /mobile/sso/sms-login
        平台ID为空, 尝试登录
        :return:
        """
        json_response = self.pa._mobile_sso_sms_login(appId_='', mobile_='18602832572', verifyCode_=1234,
                                                      deviceType_='ANDROID', deviceId_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("平台不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "平台ID为空, 登录成功")

    def test_mobile_sso_sms_login_without_mobile(self):
        """
        POST /mobile/sso/sms-login
        手机号为空, 尝试登录
        :return:
        """
        json_response = self.pa._mobile_sso_sms_login(appId_='FLOWER_CHASERS', mobile_=None, verifyCode_=1234,
                                                      deviceType_='ANDROID', deviceId_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号为空, 登录成功")

    def test_mobile_sso_sms_login_without_verify_code(self):
        """
        POST /mobile/sso/sms-login
        验证码为空, 尝试登录
        :return:
        """
        json_response = self.pa._mobile_sso_sms_login(appId_='FLOWER_CHASERS', mobile_='18602832572', verifyCode_='',
                                                      deviceType_='ANDROID', deviceId_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("验证码不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "验证码为空, 登录成功")

    def test_mobile_sso_sms_login_without_devivce_type(self):
        """
        POST /mobile/sso/sms-login
        设备类型为空, 尝试登录
        :return:
        """
        json_response = self.pa._mobile_sso_sms_login(appId_='FLOWER_CHASERS', mobile_='18602832572', verifyCode_=1234,
                                                      deviceType_='', deviceId_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("设备类型不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "设备类型为空, 登录成功")

    def test_mobile_sso_sms_login_with_wrong_mobile(self):
        """
        POST /mobile/sso/sms-login
        手机号格式有误, 尝试登录
        :return:
        """
        json_response = self.pa._mobile_sso_sms_login(appId_='FLOWER_CHASERS', mobile_='112302831234', verifyCode_=1234,
                                                      deviceType_='ANDROID', deviceId_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号格式有误, 登录成功")

    def test_mobile_sso_sms_login_with_long_mobile(self):
        """
        POST /mobile/sso/sms-login
        手机号大于11位, 尝试登录
        :return:
        """
        json_response = self.pa._mobile_sso_sms_login(appId_='FLOWER_CHASERS', mobile_='186028325723', verifyCode_=1234,
                                                      deviceType_='ANDROID', deviceId_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号大于11位, 登录成功")

    def test_mobile_sso_sms_login_with_short_mobile(self):
        """
        POST /mobile/sso/sms-login
        手机号小于11位, 尝试登录
        :return:
        """
        json_response = self.pa._mobile_sso_sms_login(appId_='FLOWER_CHASERS', mobile_='1860283257', verifyCode_=1234,
                                                      deviceType_='ANDROID', deviceId_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号小于11位, 登录成功")

    def test_mobile_sso_sms_login_with_unregister_mobile(self):
        """
        POST /mobile/sso/sms-login
        手机号未注册, 尝试登录
        :return:
        """
        json_response = self.pa._mobile_sso_sms_login(appId_='FLOWER_CHASERS', mobile_='19988776654', verifyCode_=8888,
                                                      deviceType_='ANDROID', deviceId_='')
        if json_response["status"] == "OK":
            log.info('首次登录即注册，手机号验证码方式登录成功')
        else:
            self.assertTrue(False, "手机号未注册, 登录成功")

    def test_mobile_sso_sms_login_with_wrong_code(self):
        """
        POST /mobile/sso/sms-login
        验证码错误, 尝试登录
        :return:
        """
        json_response = self.pa._mobile_sso_sms_login(appId_='FLOWER_CHASERS', mobile_='18602832572', verifyCode_=12345,
                                                      deviceType_='ANDROID', deviceId_='')
        if json_response["status"] == "ERROR":
            self.assertEqual("验证码错误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "验证码错误, 登录成功")

    def test_mobile_sso_sms_login_success(self):
        """
        POST /mobile/sso/sms-login
        手机号和验证码正确, 尝试登录
        :return:
        """
        verify_code = self.get_verify_code_success()
        json_response = self.pa._mobile_sso_sms_login(appId_='FLOWER_CHASERS', mobile_=19988776655,
                                                      verifyCode_=verify_code,
                                                      deviceType_='ANDROID', deviceId_='dwd')
        if json_response["status"] == "OK":
            log.info('手机号验证码方式登录成功')
        else:
            self.assertTrue(False, "手机号和验证码正确, 登录失败")

    def test_mobile_sso_third_bind_weixin(self):
        """
        POST /mobile/sso/third-bind-weixin
        微信授权后绑定手机并完善账户信息
        :return:
        """
        username = self.fake.name()
        self.pa._mobile_sso_third_bind_weixin(userName_=username,
                                              userHeadImg_="http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1585645410421.jpg",
                                              mobile_=19988776654,
                                              openId_='11111111',
                                              accessToken_="31_6NpW0Lw8mh5ZYGM1JDiwipTZHra0jH6Qxq6xeeTyhaX8SPaWxJySq5n9gsxCZe6az2cshlDvCtKRFVbTdYnoRTCZesNBvzHgi3k5jCSQfZ63MIMzjsO-GuU06oEnvq_rAilF8BWUSRTEwK2UZGRaACADKV",
                                              deviceId_='',
                                              authType_='WECHAT',
                                              deviceType_='ANDROID',
                                              appId_='FLOWER_CHASERS')

    def test_mobile_sso_third_login_weixin(self):
        """
        POST /mobile/sso/third-login-weixin
        微信登录
        :return:
        """
        self.pa._mobile_sso_third_login_weixin(code_="",
                                               deviceId_='8faf2300-da86-420d-be66-9c37853fddd1',
                                               deviceType_='ANDROID',
                                               appId_='FLOWER_CHASERS')


