#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/8/20'
"""
import time

from testcase.worldFarm import testCase


class UserTest(testCase):
    def __init__(self, methodName='runTest'):
        super(UserTest, self).__init__(methodName=methodName)
        # self.ka.set_user(mobile=self.email, password=self.password)

    def test5002(self):
        """
        邮箱注册新账号测试
        :return:
        """
        email = str(int(time.time())) + '@qq.com'
        register = self.pa._mobile_sso_email_registe(account=email, password='123456', userName='鑫美账号',
                                                     headImg='https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                                                             '/data/world-user/headImg/1560498735030.jpg',
                                                     appId='WORLD_FARM', deviceType='IOS', deviceId='QaTeam')
        self.assertEqual(register['status'], "OK")

    def test5003(self):
        """
        邮箱格式不正确测试
        :return:
        """
        register = self.pa._mobile_sso_email_registe(account='test', password='123456', userName='鑫美账号',
                                                     headImg='https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                                                             '/data/world-user/headImg/1560498735030.jpg',
                                                     appId='WORLD_FARM', deviceType='IOS', deviceId='QaTeam')
        self.assertEqual(register['errorMsg'], "邮箱格式不正确，请重新输入")

    def test5004(self):
        """
        邮箱长度超过64位
        :return:
        """
        register = self.pa._mobile_sso_email_registe(
            account='testtesttesttesttesttesttesttesttesttesttesttesttesttesttes@qq.com',
            password='123456', userName='鑫美账号',
            headImg='https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                    '/data/world-user/headImg/1560498735030.jpg',
            appId='WORLD_FARM', deviceType='IOS', deviceId='QaTeam')
        self.assertEqual(register['errorMsg'], "邮箱长度不能超过64字符")

    def test5005(self):
        """
        未上传图片
        :return:
        """
        register = self.pa._mobile_sso_email_registe(
            account=str(int(time.time())) + '@qq.com',
            password='123456', userName='鑫美账号',
            headImg=None,
            appId='WORLD_FARM', deviceType='IOS', deviceId='QaTeam')
        self.assertEqual(register['status'], "OK")

    def test5006(self):
        """
        姓名为空校验测试
        :return:
        """
        register = self.pa._mobile_sso_email_registe(
            account='test1@qq.com',
            password='123456', userName=None,
            headImg='https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                    '/data/world-user/headImg/1560498735030.jpg',
            appId='WORLD_FARM', deviceType='IOS', deviceId='QaTeam')
        self.assertEqual(register['errorMsg'], "姓名不能为空")

    def test5007(self):
        """
        姓名超过20字校验测试
        :return:
        """
        register = self.pa._mobile_sso_email_registe(
            account='test@qq.com',
            password='123456', userName='测试姓名长度限制超过20字以后会提示什么呢',
            headImg='https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                    '/data/world-user/headImg/1560498735030.jpg',
            appId='WORLD_FARM', deviceType='IOS', deviceId='QaTeam')
        self.assertEqual(register['errorMsg'], "姓名不能超过20个字符")

    def test5008(self):
        """
        密码不能为空
        :return:
        """
        register = self.pa._mobile_sso_email_registe(
            account='test@qq.com',
            password='', userName='测试姓名长度限制超过20字以后会提示什么',
            headImg='https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                    '/data/world-user/headImg/1560498735030.jpg',
            appId='WORLD_FARM', deviceType='IOS', deviceId='QaTeam')
        self.assertEqual(register['errorMsg'], "密码不能为空")

    def test5034(self):
        """
        密码小于6位
        :return:
        """
        register = self.pa._mobile_sso_email_registe(
            account='test@qq.com',
            password='12345中', userName='测试',
            headImg='https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                    '/data/world-user/headImg/1560498735030.jpg',
            appId='WORLD_FARM', deviceType='IOS', deviceId='QaTeam')
        self.assertEqual(register['errorMsg'], "请输入6-15数字、字母密码")

    def test5009(self):
        """
        密码大于15位
        :return:
        """
        register = self.pa._mobile_sso_email_registe(
            account='test@qq.com',
            password='密码长度限制超过20字以后会提示什么呢', userName='测试',
            headImg='https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                    '/data/world-user/headImg/1560498735030.jpg',
            appId='WORLD_FARM', deviceType='IOS', deviceId='QaTeam')
        self.assertEqual(register['errorMsg'], "请输入6-15数字、字母密码")

    # def test5014(self):
    #     """
    #     移动端自动登录
    #     :return:
    #     """
    #     register = self.pa._mobile_sso_automatic_login(token=self.user.token,
    #                                                   encryptedPwd=self.user.encryptedPwd, deviceId=self.user.device_id)
    #     self.assertEqual(register['status'], "OK")

    def test5015(self):
        """
        更新用户性别为空
        :return:
        """
        info = self.ua._mobile_user_update(userName='更新用户名',
                                           headImg='http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                                                   '/data/farm/head/1530012206259.png',
                                           region=None, phone=None, gender=None,
                                           birthday=None, introduce=None, area=None)
        self.assertEqual(info['status'], "OK")

    def test5001(self):
        """
        邮箱已注册测试
        :return:
        """
        register = self.pa._mobile_sso_email_registe(account='heng.xin@qq.com', password='123456', userName='鑫美账号',
                                                     headImg='https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                                                             '/data/world-user/headImg/1560498735030.jpg',
                                                     appId='WORLD_FARM', deviceType='IOS', deviceId='QaTeam')
        self.assertEqual(register['errorMsg'], "当前邮箱已注册，请重新输入")

    def test5016(self):
        """
        更新用户性别选填
        :return:
        """
        info = self.ua._mobile_user_update(userName='test',
                                           headImg='http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                                                   '/data/farm/head/1530012206259.png',
                                           region=None, phone=None, gender=None,
                                           birthday=None, introduce=None, area=None)
        self.assertEqual(info['status'], "OK")

    def test5017(self):
        """
        更新用户姓名为None
        :return:
        """
        info = self.ua._mobile_user_update(userName=None,
                                           headImg='http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                                                   '/data/farm/head/1530012206259.png',
                                           region=None, phone=None, gender=1,
                                           birthday=None, introduce=None, area=None)
        self.assertEqual(info['errorMsg'], "姓名不能为空")

    def test5018(self):
        """
        更新用户姓名不能为空
        :return:
        """
        info = self.ua._mobile_user_update(userName='',
                                           headImg='http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                                                   '/data/farm/head/1530012206259.png',
                                           region=None, phone=None, gender=1,
                                           birthday=None, introduce=None, area=None)
        self.assertEqual(info['errorMsg'], "姓名不能为空")

    def test5019(self):
        """
        更新用户姓名长度不能超过20字
        :return:
        """
        info = self.ua._mobile_user_update(userName='用户姓名长度限制超过20字以后会提示什么呢',
                                           headImg='http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                                                   '/data/farm/head/1530012206259.png',
                                           region=None, phone=None, gender=1,
                                           birthday=None, introduce=None, area=None)
        self.assertEqual(info['errorMsg'], "姓名不超过20个字")

    def test5020(self):
        """
        更新用户头像为空
        :return:
        """
        info = self.ua._mobile_user_update(userName='用户姓名',
                                           headImg=None,
                                           region=None, phone=None, gender=1,
                                           birthday=None, introduce=None, area=None)
        self.assertEqual(info['status'], "OK")

    def test5021(self):
        """
        更换密码旧密码错误
        :return:
        """
        info = self.ua._mobile_user_update_password(oldPassword='000000', newPassword='123456')
        self.assertEqual(info['errorMsg'], "旧密码输入错误")

    def test5022(self):
        """
        更换密码旧密码长度不够
        :return:
        """
        info = self.ua._mobile_user_update_password(oldPassword='0', newPassword='123456')
        self.assertEqual(info['errorMsg'], "请输入6-15数字、字母密码")

    def test5023(self):
        """
        更换密码旧密码长度超长
        :return:
        """
        info = self.ua._mobile_user_update_password(oldPassword='0000000000000000', newPassword='123456')
        self.assertEqual(info['errorMsg'], "请输入6-15数字、字母密码")

    def test5024(self):
        """
        更换密码新旧密码不能一样
        :return:
        """
        info = self.ua._mobile_user_update_password(oldPassword='123456', newPassword='123456')
        self.assertEqual(info['errorMsg'], "旧密码不能和新密码一致")

    def test5025(self):
        """
        更换密码成功(修改后token无法获取)
        :return:
        """
        info = self.ua._mobile_user_update_password(oldPassword='123123', newPassword='123456')
        self.assertEqual(info['status'], "OK")

    def test5026(self):
        """
        更换密码旧密码不能为空
        :return:
        """
        info = self.ua._mobile_user_update_password(oldPassword='', newPassword='123456')
        self.assertEqual(info['errorMsg'], "旧密码不能为空")

    def test5027(self):
        """
        更换密码新密码不能为空
        :return:
        """
        info = self.ua._mobile_user_update_password(oldPassword='123456', newPassword=None)
        self.assertEqual(info['errorMsg'], "新密码不能为空")

    def test5028(self):
        """
        更换密码新密码过短
        :return:
        """
        info = self.ua._mobile_user_update_password(oldPassword='123456', newPassword='0')
        self.assertEqual(info['errorMsg'], "请输入6-15数字、字母密码")

    def test5029(self):
        """
        更换密码新密码过长
        :return:
        """
        info = self.ua._mobile_user_update_password(oldPassword='123456', newPassword='0000000000000000')
        self.assertEqual(info['errorMsg'], "请输入6-15数字、字母密码")

    def test5030(self):
        """
        更换邮箱邮箱为空
        :return:
        """
        info = self.ua._mobile_user_send_update_email(email=None)
        self.assertEqual(info['errorMsg'], "邮箱格式不正确，请重新输入")

    def test5031(self):
        """
        更换邮箱邮箱格式不正确
        :return:
        """
        info = self.ua._mobile_user_send_update_email(email='test')
        self.assertEqual(info['errorMsg'], "邮箱格式不正确，请重新输入")

    def test5032(self):
        """
        更换邮箱邮箱已被注册
        :return:
        """
        info = self.ua._mobile_user_send_update_email(email='26632629@qq.com')
        self.assertEqual(info['errorMsg'], "邮箱已存在")

    def test5033(self):
        """
        更换邮箱邮件发送成功(修改后token无法获取)
        :return:
        """
        info = self.ua._mobile_user_send_update_email(email='26632629@qq.com')
        self.assertEqual(info['status'], "OK")


if __name__ == '__main__':
    m = UserTest()
