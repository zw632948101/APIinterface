#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2020 2020/3/31 14:07
__author__: wei.zhang

    实名认证
"""

import unittest
from actions.BeeAction import BeeAction
from tools.Config import Log
from sql.Bee import UserAuthData
from faker import Faker


class UserAuth(unittest.TestCase, UserAuthData):
    log = Log('ContainerMain').logger
    fake = Faker(locale="zh_CN")
    bee = BeeAction()
    bee.set_user('15388126075')

    def setUp(self) -> None: pass

    def tearDown(self) -> None: pass

    def test_mobile_user_auth_get_auth_info(self):
        """
        获取蜂农实名认证信息 new 2.0
        :return:
        """
        resp = self.bee._mobile_user_auth_get_auth_info()
        self.assertEqual(resp.get('status'), 'OK')

    def test_mobile_user_auth_auth(self):
        """
        蜂农实名认证
        :return:
        """
        telephone_ = '15388126072'
        cardName_ = '张伟'
        idCardNo_ = '513029199204034955'
        avatarsImage_ = 'http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1585703137844.jpg'
        idCardFrontImage_ = 'http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1585703183260.jpg'
        response = self.bee._mobile_user_auth_auth(telephone_=telephone_, cardName_=cardName_, idCardNo_=idCardNo_,
                                                   avatarsImage_=avatarsImage_, idCardFrontImage_=idCardFrontImage_)
        self.assertEqual(response.get('status'), 'OK')

    def test_mobile_user_auth_get_status(self):
        """
        获取蜂农实名认证状态 new 2.0
        :return:
        """
        resp = self.bee._mobile_user_auth_get_status()
        self.assertEqual(resp.get('status'), 'OK')
        content = resp.get('content')
        self.assertEqual(content.get('userId'), int(self.bee.user.user_id))

    def test_mobile_user_auth_token(self):
        """
        满帮登录授权成功后生成accessToken new 2.0

        :return:
        """
        authcode = "D5731F5E06B245E1BE508E30DC4182A7"
        resp = self.bee._mobile_user_auth_token(authCode_=authcode)
        self.assertEqual(resp.get('status'), 'OK')
        # print(resp)
