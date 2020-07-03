#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2019 2019/12/27 10:51
@Author: hengxin
"""

import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from actions.UserAction import UserAction
from utils.log.logger import logger
from tools.RedisOperate import Redis
from sql.Passport import PassportInfoSql
from testcase.flowerChaser.sql.Bee  import PersonalSql
from faker import Faker
from utils.fake.FakeLocation import FakeLocation
from tools.Tool import Tool
import random
import json


class PersonalCenterMain(unittest.TestCase):
    """
    接口文档: http://dev-user.worldfarm.com/swagger-ui.html
    """
    ua = UserAction()
    ba = BeeAction()
    log = logger('UserManageMain').logger
    log.info("开始执行User接口测试用例")
    pis = PassportInfoSql()
    ps = PersonalSql()
    redis = Redis(db=2)
    fake = Faker(locale="zh_CN")
    fl = FakeLocation()
    # ba.set_user('19988776654')

    # From Worldfarm SaaS Test: UserManageCase.py Line 205
    def test00_mobile_user_detail_without_login(self):
        """
        POST /mobile/fc-user/info
        未登录获取个人信息详情
        :return:
        """
        json_response = self.ba._mobile_fc_user_info()
        if json_response["status"] == "ERROR":
            self.assertEqual("Request parameter missing", json_response["errorMsg"])
        else:
            self.assertTrue(False, "未登录获取个人信息详情成功")

    def test_mobile_user_detail_with_login(self):
        """
        POST /mobile/fc-user/info
        登录获取个人信息详情
        :return:
        """
        post_code = {"1000": "管理员", "1001": "蜂农", "1002": "项目专员", "1003": "驾驶员",
                     "1004": "后勤专员", "1005": "项目经理"}
        role_code = {"1001": "管理员", "1002": "普通员工"}
        phone = '19988776654'
        self.ba.set_user(phone)
        json_response = self.ba._mobile_fc_user_info()
        if json_response["status"] == "OK":
            db_info = self.pis.query_user_by_mobile(phone)[0]
            phone = str(db_info["phone"])
            # self.assertEqual(json_response["content"].get("phone", None), phone[:3] + "****" + phone[-4:])
            self.assertEqual(json_response["content"].get("phone", None), phone)
            self.assertEqual(json_response["content"].get("email", None), db_info["email"])
            self.assertEqual(json_response["content"]["userName"], db_info["username"])
            self.assertEqual(json_response["content"]["postCode"], db_info["post_code"])
            self.assertEqual(json_response["content"]["postStr"], post_code[db_info["post_code"]])
            self.assertEqual(json_response["content"]["roleCode"], db_info["role_code"])
            self.assertEqual(json_response["content"]["roleStr"], role_code[db_info["role_code"]])
            self.assertEqual(json_response["content"].get("gender", None), db_info["gender"])
            self.assertEqual(json_response["content"].get("headImg", None), db_info["head_img"])
        else:
            self.assertTrue(False, "登录获取个人信息详情失败")

    def test_mobile_user_upload_headimg_success(self):
        """
        POST /mobile/user/upload/headImg
        上传用户头像
        :return:
        """
        # 上传接口未做校验
        self.ua.set_user('19988776654')
        json_response = self.ua._mobile_user_upload_headImg(headImgFile_='./headImg.jpg')
        if json_response["status"] == "OK":
            self.assertTrue(json_response["content"].startswith("http"))
            self.assertTrue(json_response["content"].endswith("jpg"))
        else:
            self.assertTrue(False, "上传用户头像失败")

    # 兼容追花第一期, 姓名一直都可以为空, 二期要求创建账号时, 姓名不能为空
    # def test_mobile_user_update_without_name(self):
    #     """
    #     POST /mobile/fc-user/update
    #     姓名为空, 编辑个人信息
    #     :return:
    #     """
    #     self.ba.set_user("26632629@qq.com", "123456")
    #     # 追花一期: userName作为预留参数, 未做校验
    #     json_response = self.ba._mobile_fc_user_update(headImg_='', postCode_=1001)
    #     if json_response["status"] == "ERROR":
    #         self.assertEqual("用户名不能为空", json_response["errorMsg"])
    #     else:
    #         self.assertTrue(False, "姓名为空, 编辑个人信息成功")

    def test_mobile_user_update_with_long_name(self):
        """
        POST /mobile/fc-user/update
        姓名超过16个字, 编辑个人信息
        :return:
        """
        self.ba.set_user("19988776654")
        # 追花一期: userName作为预留参数, 未做校验
        json_response = self.ba._mobile_fc_user_update(headImg_='', userName_="26632629@qq.com123456")
        if json_response["status"] == "ERROR":
            self.assertEqual("姓名不能超过16个字", json_response["errorMsg"])
        else:
            self.assertTrue(False, "姓名超过16个字, 编辑个人信息成功")

    def test_mobile_user_update_without_postcode(self):
        """
        POST /mobile/fc-user/update
        岗位编码为空, 编辑个人信息
        :return:
        """
        self.ba.set_user("26632629@qq.com", "123456")
        # 追花一期: userName作为预留参数, 未做校验
        json_response = self.ba._mobile_fc_user_update(headImg_='', postCode_='', userName_='测试')
        if json_response["status"] == "ERROR":
            self.assertEqual("岗位编码不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "岗位编码为空, 编辑个人信息成功")

    def test_mobile_user_update_with_wrong_postcode(self):
        # 测试未通过, 岗位编码枚举未做校验
        # post_code = {"蜂农": 1001, "项目专员": 1002, "驾驶员": 1003, "后勤专员": 1004, "项目经理": 1005}
        """
        POST /mobile/fc-user/update
        岗位编码不正确, 编辑个人信息
        :return:
        """
        self.ba.set_user("26632629@qq.com", "123456")
        # 追花一期: userName作为预留参数, 未做校验
        json_response = self.ba._mobile_fc_user_update(headImg_='', postCode_=0000, userName_='测试')
        if json_response["status"] == "ERROR":
            self.assertEqual("岗位不存在", json_response["errorMsg"])
        else:
            self.assertTrue(False, "岗位编码不正确, 编辑个人信息成功")

    # def test_mobile_user_update_with_wrong_headimg(self):
    #     # PASS WITH WARNING, headImg未做校验
    #     """
    #     POST /mobile/fc-user/update
    #     非法HTTP链接, 编辑个人信息
    #     :return:
    #     """
    #     self.ba.set_user("26632629@qq.com", "123456")
    #     # 追花一期: userName作为预留参数, 未做校验
    #     # 追花一期: headImg由于前端有默认占位图, 暂未做校验, 任何字符串都可入库 _(¦3」∠)_
    #     json_response = self.ba._mobile_fc_user_update(headImg_="abc", postCode_=1005, userName_='测试')
    #     self.test_mobile_user_detail_with_login()
    #     if json_response["status"] == "ERROR":
    #         self.assertEqual("非法链接格式", json_response["errorMsg"])
    #     else:
    #         self.assertTrue(False, "非法链接格式, 编辑个人信息成功")

    def test_mobile_user_update_success(self):
        """
        POST /mobile/fc-user/update
        更新头像，更新姓名
        :return:
        """
        # post_code = {"1001": "蜂农", "1002": "项目专员", "1003": "驾驶员", "1004": "后勤专员", "1005": "项目经理"}
        # role_code = {"1001": "管理员", "1002": "普通员工"}
        # update_post_code = random.choice(["1001", "1002", "1003", "1004", "1005"])
        update_name = self.fake.name()
        update_image = "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1585725172697.jpg"
        phone = "19988776654"
        self.ba.set_user(phone)
        json_response = self.ba._mobile_fc_user_update(userName_=None,
                                                       headImg_=update_image)
        if json_response["status"] == "OK":
            db_info = self.pis.query_user_by_mobile(phone)[0]
            self.assertEqual(update_name, db_info["username"])
            self.assertEqual(update_image, db_info["head_img"])
        else:
            self.assertTrue(False, "更新个人信息详情失败")

    def test_mobile_user_update_username_after_auth(self):
        """
        POST /mobile/fc-user/update
        实名认证通过后，修改姓名
        :return:
        """
        update_name = self.fake.name()
        phone = "19988776654"
        self.ba.set_user(phone)
        self.ba._mobile_fc_user_update(userName_=update_name)

    # def test_fc_update_user_email_without_email(self):
    #     """
    #     POST /fc/mobile/user/update-email
    #     邮箱为空, 修改邮箱
    #     :return:
    #     """
    #     json_response = self.ua._fc_mobile_user_update_email(email_=None)
    #     if json_response["status"] == "ERROR":
    #         self.assertEqual("邮箱不能为空", json_response["errorMsg"])
    #     else:
    #         self.assertTrue(False, "邮箱为空, 修改邮箱成功")
    #
    # def test_fc_update_user_email_with_wrong_email(self):
    #     """
    #     POST /fc/mobile/user/update-email
    #     邮箱格式错误, 修改邮箱
    #     :return:
    #     """
    #     json_response = self.ua._fc_mobile_user_update_email(email_='qq.com')
    #     if json_response["status"] == "ERROR":
    #         self.assertEqual("邮箱格式有误", json_response["errorMsg"])
    #     else:
    #         self.assertTrue(False, "邮箱格式错误, 修改邮箱成功")
    #
    # def test_fc_update_user_email_with_long_email(self):
    #     """
    #     POST /fc/mobile/user/update-email
    #     邮箱长度超过64位, 修改邮箱
    #     :return:
    #     """
    #     self.ua.set_user("26632629@qq.com", 123456)
    #     json_response = self.ua._fc_mobile_user_update_email(email_='0123456789012345678901234567890123456789'
    #                                                                 '01234567890123456789@qq.com')
    #     if json_response["status"] == "ERROR":
    #         self.assertEqual("邮箱长度不能超过64位", json_response["errorMsg"])
    #     else:
    #         self.assertTrue(False, "邮箱长度超过64位, 修改邮箱成功")
    #
    # def test_fc_update_user_email_with_registered_email(self):
    #     """
    #     POST /fc/mobile/user/update-email
    #     已注册邮箱, 修改邮箱
    #     :return:
    #     """
    #     self.ua.set_user('26632629@qq.com', 123456)
    #     json_response = self.ua._fc_mobile_user_update_email(email_='26632629@qq.com')
    #     if json_response["status"] == "ERROR":
    #         self.assertEqual("新邮箱不能与原邮箱相同", json_response["errorMsg"])
    #     else:
    #         self.assertTrue(False, "已注册邮箱, 修改邮箱成功")
    #
    # def test_fc_update_user_email_success(self):
    #     """
    #     POST /fc/mobile/user/update-email
    #     新邮箱, 修改邮箱
    #     :return:
    #     """
    #     self.ua.set_user('26632629@qq.com', 123456)
    #     json_response = self.ua._fc_mobile_user_update_email(email_='343260924@qq.com')
    #     if json_response["status"] == "OK":
    #         self.ua.set_user('343260924@qq.com', 123456)
    #         self.ua._fc_mobile_user_update_email(email_='26632629@qq.com')
    #     else:
    #         self.assertTrue(False, "新邮箱, 修改邮箱成功")
    #
    # def test_fc_update_user_password_without_password(self):
    #     """
    #     POST /fc/mobile/user/update-password
    #     密码为空, 修改密码
    #     :return:
    #     """
    #     self.ua.set_user('26632629@qq.com', 123456)
    #     json_response = self.ua._fc_mobile_user_update_password(newPassword_=None)
    #     if json_response["status"] == "ERROR":
    #         self.assertEqual("新密码不能为空", json_response["errorMsg"])
    #     else:
    #         self.assertTrue(False, "密码为空, 修改密码成功")
    #
    # def test_fc_update_user_password_with_short_password(self):
    #     """
    #     POST /fc/mobile/user/update-password
    #     密码小于6位, 修改密码
    #     :return:
    #     """
    #     self.ua.set_user('26632629@qq.com', 123456)
    #     json_response = self.ua._fc_mobile_user_update_password(newPassword_='12345')
    #     if json_response["status"] == "ERROR":
    #         self.assertEqual("请输入6-15数字、字母密码", json_response["errorMsg"])
    #     else:
    #         self.assertTrue(False, "密码小于6位, 修改密码成功")
    #
    # def test_fc_update_user_password_with_long_password(self):
    #     """
    #     POST /fc/mobile/user/update-password
    #     密码大于15位, 修改密码
    #     :return:
    #     """
    #     self.ua.set_user('26632629@qq.com', 123456)
    #     json_response = self.ua._fc_mobile_user_update_password(newPassword_='0123456789012345')
    #     if json_response["status"] == "ERROR":
    #         self.assertEqual("请输入6-15数字、字母密码", json_response["errorMsg"])
    #     else:
    #         self.assertTrue(False, "密码小于6位, 修改密码成功")
    #
    # def test_fc_update_user_password_with_special_letter(self):
    #     """
    #     POST /fc/mobile/user/update-password
    #     密码含有非数字或非字母, 修改密码
    #     :return:
    #     """
    #     self.ua.set_user('26632629@qq.com', 123456)
    #     json_response = self.ua._fc_mobile_user_update_password(newPassword_='0123456_')
    #     if json_response["status"] == "ERROR":
    #         self.assertEqual("请输入6-15数字、字母密码", json_response["errorMsg"])
    #     else:
    #         self.assertTrue(False, "密码含有非数字或非字母, 修改密码成功")

    # def test_fc_update_user_password_success(self):
    #     """
    #     POST /fc/mobile/user/update-password
    #     密码合法, 修改密码
    #     :return:
    #     """
    #     self.ua.set_user('26632629@qq.com', 123456)
    #     json_response = self.ua._fc_mobile_user_update_password(newPassword_='0123456')
    #     if json_response["status"] == "OK":
    #         self.ua.set_user('26632629@qq.com', '0123456')
    #         self.ua._fc_mobile_user_update_password(newPassword_='123456')
    #     else:
    #         self.assertTrue(False, "密码合法, 修改密码失败")

    def test_fc_send_mobile_change_verify_code_without_mobile(self):
        """
        POST /fc/mobile/user/change-verify-code
        手机号为空, 发送验证码
        :return:
        """
        self.ua.set_user('19988776654')
        json_response = self.ua._fc_mobile_user_change_verify_code(mobile_=None)
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号为空, 发送验证码成功")

    def test_fc_send_mobile_change_verify_code_with_wrong_mobile(self):
        """
        POST /fc/mobile/user/change-verify-code
        手机号格式错误, 发送验证码
        :return:
        """
        self.ua.set_user('19988776654')
        json_response = self.ua._fc_mobile_user_change_verify_code(mobile_='11602832572')
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号格式错误, 发送验证码成功")

    def test_fc_send_mobile_change_verify_code_with_short_mobile(self):
        """
        POST /fc/mobile/user/change-verify-code
        手机号小于11位, 发送验证码
        :return:
        """
        self.ua.set_user('19988776654')
        json_response = self.ua._fc_mobile_user_change_verify_code(mobile_='1860283257')
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号小于11位, 发送验证码成功")

    def test_fc_send_mobile_change_verify_code_with_long_mobile(self):
        """
        POST /fc/mobile/user/change-verify-code
        手机号大于11位, 发送验证码
        :return:
        """
        self.ua.set_user('26632629@qq.com', 123456)
        json_response = self.ua._fc_mobile_user_change_verify_code(mobile_='018602832572')
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号格式有误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号小于11位, 发送验证码成功")

    def test_fc_send_mobile_change_verify_code_with_registered_phone(self):
        """
        POST /fc/mobile/user/change-verify-code
        手机号已注册, 发送验证码
        :return:
        """
        self.ua.set_user('19988776654')
        self.redis.set('SmsVerifyCode:ReplaceMobile:19988776654:times', 1)
        json_response = self.ua._fc_mobile_user_change_verify_code(mobile_='19988776654')
        if json_response["status"] == "ERROR":
            self.assertEqual("新手机号不能与原手机号相同", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号已注册, 发送验证码成功")

    def get_mobile_change_verify_code_success(self, mobile):
        """
        POST /fc/mobile/user/change-verify-code
        手机号正确, 发送验证码
        :return:
        """
        self.ua.set_user('19988776654')
        self.redis.set('SmsVerifyCode:ReplaceMobile:%s:times' % str(mobile), 1)
        json_response = self.ua._fc_mobile_user_change_verify_code(mobile_=mobile)
        if json_response["status"] == "OK":
            verify_code = json.loads(self.redis.get('SmsVerifyCode:ReplaceMobile:%s:code' % str(mobile)))['code']
            self.log.info('手机号 %s, 短信已发送, 验证码 %s' % (mobile, verify_code))
            return verify_code
        else:
            self.assertTrue(False, "手机号正确, 发送验证码失败")

    def test_fc_update_user_mobile_without_mobile(self):
        """
        POST /fc/mobile/user/update-mobile
        手机号为空, 修改手机号
        :return:
        """
        self.ua.set_user('19988776654')
        json_response = self.ua._fc_mobile_user_update_mobile(mobile_=None, verifyCode_=1234)
        if json_response["status"] == "ERROR":
            self.assertEqual("手机号不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "手机号已注册, 修改手机号成功")

    def test_fc_update_user_mobile_without_code(self):
        """
        POST /fc/mobile/user/update-mobile
        验证码为空, 修改手机号
        :return:
        """
        self.ua.set_user('19988776654')
        json_response = self.ua._fc_mobile_user_update_mobile(mobile_='19988776654', verifyCode_=None)
        if json_response["status"] == "ERROR":
            self.assertEqual("验证码不能为空", json_response["errorMsg"])
        else:
            self.assertTrue(False, "验证码为空, 修改手机号成功")

    def test_fc_update_user_mobile_with_wrong_code(self):
        """
        POST /fc/mobile/user/update-mobile
        验证码错误, 修改手机号
        :return:
        """
        self.ua.set_user('19988776654')
        json_response = self.ua._fc_mobile_user_update_mobile(mobile_='19988776653', verifyCode_='0000')
        if json_response["status"] == "ERROR":
            self.assertEqual("验证码错误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "验证码错误, 修改手机号成功")

    def test_fc_update_user_mobile_with_long_code(self):
        """
        POST /fc/mobile/user/update-mobile
        验证码大于4位, 修改手机号
        :return:
        """
        self.ua.set_user('19988776654')
        json_response = self.ua._fc_mobile_user_update_mobile(mobile_='19602832572', verifyCode_='12345')
        if json_response["status"] == "ERROR":
            self.assertEqual("验证码错误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "验证码大于4位, 修改手机号成功")

    def test_fc_update_user_mobile_with_short_code(self):
        """
        POST /fc/mobile/user/update-mobile
        验证码小于4位, 修改手机号
        :return:
        """
        self.ua.set_user('19988776654')
        json_response = self.ua._fc_mobile_user_update_mobile(mobile_='19602832572', verifyCode_='123')
        if json_response["status"] == "ERROR":
            self.assertEqual("验证码错误", json_response["errorMsg"])
        else:
            self.assertTrue(False, "验证码小于4位, 修改手机号成功")

    def test_fc_update_user_mobile_success(self):
        """
        POST /fc/mobile/user/update-mobile
        手机号验证码正确, 修改手机号
        :return:
        """
        # new_mobile = 19988776654
        # old_mobile = 19988776652
        # new_verify_code = self.get_mobile_change_verify_code_success(new_mobile)
        # self.ua.set_user('19988776600')
        # self.ua._fc_mobile_user_update_mobile(mobile_='19988776601', verifyCode_=8888)
        self.ba.set_user('19988776601')
        self.ba._mobile_fc_user_info()
        # if json_response["status"] == "OK":
        #     old_verify_code = self.get_mobile_change_verify_code_success(old_mobile)
        #     self.ua._fc_mobile_user_update_mobile(mobile_=old_mobile, verifyCode_=old_verify_code)
        # else:
        #     self.assertTrue(False, "手机号验证码正确, 修改手机号失败")

    def test_fc_mobile_user_mobile_check(self):
        """
        POST fc/mobile/user/mobile-check
        修改手机号前校验
        :return:
        """
        self.ua.set_user('19988776654')
        self.ua._fc_mobile_user_mobile_check(mobile_='19988776651')
        # self.ua._fc_mobile_user_mobile_check(mobile_='15388126072')  # 已注册账号，弹窗提示

    def test_mobile_fc_user_update(self):
        """
        POST /mobile/fc-user/update
        账户资料完善
        :return:
        """
        self.ba.set_user('19988776600')
        province_id, city_id, district_id, address, lng, lat = self.fl.fake_location()
        username = self.fake.name()
        db_regular_source = self.ps.sql_random_statistics_nectar_source_type(random.randint(1, 10))
        regular_source = Tool.data_assemble('typeCode', db_regular_source)  # 将字典处理为列表
        self.ba._mobile_fc_user_update(regularSource_=regular_source,
                                       userName_=username,
                                       headImg_="http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1585707418799.jpg",
                                       scale_=random.randint(1, 3),
                                       seniority_=random.randint(1, 30),
                                       nativeProvince_=province_id,
                                       nativeCity_=city_id,
                                       nativeCounty_=district_id,
                                       age_=random.randint(31, 99),
                                       gender_=2)

    def test_mobile_label_set(self):
        """
        POST /mobile/label/set
        设置互助标签
        :return:
        """
        self.ba.set_user('19988776600')
        db_mutual_label = self.ps.sql_mutual_label_type(random.randint(0, 9))
        mutual_label = Tool.data_assemble('typeCode', db_mutual_label)  # 将字典处理为列表
        self.ba._mobile_label_set(labelType_=mutual_label, userId_=538)

    def test_mobile_fc_user_info(self):
        """
        POST /mobile/fc-user/info
        获取用户信息
        :return:
        """
        self.ba.set_user("19999999990")
        self.ba._mobile_fc_user_info()

    def test_mobile_fc_user_update_location(self):
        """
        POST /mobile/fc-user/update-location
        更新当前用户定位经纬度
        :return:
        """
        province_id, city_id, district_id, address, lng, lat = self.fl.fake_location()
        self.ba.set_user('19988776654')
        self.ba._mobile_fc_user_update_location(lng_=lng, lat_=lat)

    def test_mobile_share_app(self):
        """
        POST /mobile/share/app
        APP分享
        :return:
        """
        self.ba.set_user('19988776600')
        self.ba._mobile_share_app()
