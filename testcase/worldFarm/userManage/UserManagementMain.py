#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Wei'
__date__ = '2019/ / '

用户管理

"""

from testcase.worldFarm import testCase


class UserManagement(testCase):
    email1 = '632948101@qq.com'

    def __init__(self, methodName='runTest'):
        super(UserManagement, self).__init__(methodName=methodName)
        # self.ua._set_user(mobile=self.email, password=self.password)

    def test_admin_user_user_list(self):
        """
        运营后台-用户管理-查询用户账号列表
        :return:
        """
        register = self.ua._admin_user_user_list(pn=0, ps=20, status=1, userName=None, email=None)
        self.assertEqual(register['status'], 'OK')
        return register['content']['datas'][0]['id']

    def test_admin_user_detail(self):
        """
        运营后台-用户管理-用户详情
        :return:
        """
        userId = self.test_admin_user_user_list()
        register = self.ua._admin_user_detail(userId=userId)
        self.assertEqual(register['status'], 'OK')
        self.assertEqual(register['content']['id'], userId)

    def test_admin_user_inner_list(self):
        """
        运营后台-用户管理-查询内部账号列表
        :return:
        """
        register = self.ua._admin_user_inner_list(pn=0, ps=20, status=1, userName=None, email=None)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_user_detail(self):
        """
        移动端-用户管理-获取用户个人信息
        :return:
        """
        register = self.ua._mobile_user_detail()
        self.assertEqual(register['status'], 'OK')

    def test_mobile_user_get_push_alias(self):
        """
        移动端-用户管理-获取推送别名
        :return:
        """
        register = self.ua._mobile_user_get_push_alias()
        self.assertEqual(register['status'], 'OK')

    def test_mobile_user_send_pass_email(self):
        """
        移动端-用户管理-发送找回密码邮件
        :return:
        """
        register = self.ua._mobile_user_send_pass_email(email=self.email)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_user_upload_headImg(self):
        """
        移动端-用户管理-上传用户头像
        :return:
        """
        file = './../tempAttach/Screen.png'
        register = self.ua._mobile_user_upload_headImg(headImgFile=file)
        self.assertEqual(register['status'], 'OK')


if __name__ == '__main__':
    m = UserManagement()
