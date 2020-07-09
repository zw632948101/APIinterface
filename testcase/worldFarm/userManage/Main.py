#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2018/8/20'
"""
import time

from testcase.worldFarm import testCase


class Main(testCase):


    def test_mobile_sso_email_registe(self):
        """
        邮箱注册新账号测试
        :return:
        """
        email = str(int(time.time())) + '@qq.com'
        register = self.pa.mobile_sso_email_registe(account=email, password='123456', userName='鑫美账号',
                                                    headImg='https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                                                            '/data/world-user/headImg/1560498735030.jpg',
                                                    appId='WORLD_FARM', deviceType='IOS', deviceId='QaTeam')
        self.assertEqual(register['status'], "OK")

    def test5006(self):
        """
        姓名为空校验测试
        :return:
        """
        register = self.pa.mobile_sso_email_registe(
            account='test1@qq.com',
            password='123456', userName=None,
            headImg='https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com'
                    '/data/world-user/headImg/1560498735030.jpg',
            appId='WORLD_FARM', deviceType='IOS', deviceId='QaTeam')
        self.assertEqual(register['errorMsg'], "姓名不能为空")

    # def test_mobile_sso_logout(self):
    #     """
    #     退出登录
    #     :return:
    #     """
    #     register = self.pa.mobile_sso_logout()
    #     self.assertEqual(register['status'], "OK")

    # def test5013(self):
    #     """
    #     运营后台登出
    #     :return:
    #     """
    #     register = self.pa.web_sso_logout()
    #     self.assertEqual(register['status'], "OK")


if __name__ == '__main__':
    m = Main()
