#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Wei'
__date__ = '2019/ / '

"""
from testcase.worldFarm import testCase, PersonnelManage
from random import choice


class PersonnelMain(testCase):
    fq = PersonnelManage()

    def __init__(self, methodName='runTest'):
        super(PersonnelMain, self).__init__(methodName=methodName)
        self.ka.set_user(mobile=self.email, password=self.password)

    def test_mobile_message_page_list(self):
        """
        分页查询普通消息列表
        :return:
        """
        register = self.ka._mobile_message_page_list(pn_=1, ps_=20, parentMsgType_=10, msgType_=1002, farmId_=None)
        self.assertEqual(register['status'], 'OK')
        if register['content']['test_case'] == []:
            return
        return register['content']['test_case'][0]['extras']

    def test_mobile_user_invite_search(self, farmId=678, account='632948101@qq.com'):
        """
        搜索站内成员
        :param farmId:
        :param account:
        :return:
        """
        register = self.ka._mobile_user_invite_search(farmId=farmId, account=account)
        self.assertEqual(register['status'], 'OK')
        return register['content'][0]['id']

    def test_mobile_user_invite_inner_invite(self, farmId=678, inviteeId=191):
        """
        发送站内邀请
        :param farmId:
        :param inviteeId:
        :return:
        """
        if inviteeId is None:
            inviteeId = self.test_mobile_user_invite_search()

        register = self.ka._mobile_user_invite_inner_invite(farmId=farmId, inviteeId=inviteeId)
        self.assertEqual(register['status'], 'OK')
        return register

    def test_mobile_user_invite_list(self):
        """
        已邀请列表
        :param farmId:
        :param account:
        :return:
        """
        farmId = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        register = self.ka._mobile_user_invite_list(farmId=farmId)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_user_invite_inner_invite_info(self, inviteId=107):
        """
        移动端-成员邀请-查询站内邀请信息
        :param inviteId:
        :return:
        """
        register = self.ka._mobile_user_invite_inner_invite_info(inviteId=inviteId)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_user_invite_inner_accept(self, inviteId=126):
        """
        接受站内邀请
        :param farmId:
        :param account:
        :return:
        """
        register = self.ka._mobile_user_invite_inner_accept(inviteId=inviteId)
        self.assertEqual(register['status'], 'OK')
        return register

    def test_invite(self):
        """
        查询站内用户,发送邀请
        :return:
        """
        inviteeid = self.test_mobile_user_invite_search(farmId=678, account='632948101@qq.com')
        self.test_mobile_user_invite_inner_invite(farmId=678, inviteeId=inviteeid)

    def test_accept(self):
        """
        接受邀请,
        注意   必须登录被邀请的账号
        :return:
        """
        extras = self.test_mobile_message_page_list()
        inviteId = extras.split('inviteId=')[1]
        self.test_mobile_user_invite_inner_invite_info(inviteId=inviteId)
        self.test_mobile_user_invite_inner_accept(inviteId=inviteId)

    def test_mobile_user_invite_email_invite(self):
        """
        发送邮箱邀请
        :return:
        """
        register = self.ka._mobile_user_invite_email_invite(farmId=678, email='xiujuan.chen@worldfarm.com')
        self.assertEqual(register['status'], 'OK')

    def test_web_user_invite_email_invite(self):
        """
        发送邮箱邀请
        :return:
        """
        register = self.ka._web_user_invite_email_invite(farmId=678, email='xiujuan.chen@worldfarm.com')
        self.assertEqual(register['status'], 'OK')

    def test_web_user_invite_email_accept(self):
        """
        Web-成员邀请-接收邮箱邀请
        :return:
        """
        register = self.ka._web_user_invite_email_accept(
            token='6C471458692D1205CECE30AC48ABE33A0476037986DBF3ED0BC35F6D68E3D6007EE29D549E5CAB8EEBEB78A59F73C7DD2D7E5E3ADC9D2969F9F9D90BD895942325D2FD61C2A8FA39CAFAB7FF7F255213DC7FF872F3480B07D1994E2473C7E3EA')
        self.assertEqual(register['status'], 'OK')

    def test_web_user_invite_email_invite_info(self):
        """
        Web-成员邀请-邮箱邀请信息
        :return:
        """
        register = self.ka._web_user_invite_email_invite_info(
            token='6C471458692D1205CECE30AC48ABE33A0476037986DBF3ED0BC35F6D68E3D6007EE29D549E5CAB8EEBEB78A59F73C7DD2D7E5E3ADC9D2969F9F9D90BD895942325D2FD61C2A8FA39CAFAB7FF7F255213DC7FF872F3480B07D1994E2473C7E3EA')
        self.assertEqual(register['status'], 'OK')

    def test_mobile_farm_user_list_by_farm(self):
        """
        获取指定农场的成员列表
        :return:
        """
        farm_id = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        register = self.ka._mobile_farm_user_list_by_farm(farmId=farm_id)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_farm_user_list_by_user(self):
        """
        获取当前所在农场的所有成员列表
        :return:
        """
        register = self.ka._mobile_farm_user_list_by_user()
        self.assertEqual(register['status'], 'OK')

    def test_mobile_farm_user_remove(self):
        """
        移除人员
        :return:
        """
        register = self.ka._mobile_farm_user_remove(farmId=678, userId=191)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_farm_user_roles(self):
        """
        获取可分配的角色列表
        :return:
        """
        farm_id = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        register = self.ka._mobile_farm_user_roles(farmId=farm_id)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_user_role_set_role(self):
        """
        设置成员角色
        :return:
        """
        register = self.ka._mobile_user_role_set_role(farmId=533, userId=203, roleId=2)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_farm_user_user_role(self):
        """
        移动端-首页侧边栏-个人信息-角色名称【v1.2.5】
        :return:
        """
        farm_info = self.fq.query_default_farm(self.email)[0]
        register = self.ka._mobile_farm_user_user_role(farmId=farm_info.get('farm_id'))
        self.assertEqual(register['status'], 'OK')
        # 判断是否为当前登录用户
        self.assertEqual(register['content']['userId'], farm_info.get('user_id'))
        self.assertEqual(register['content']['farmId'], farm_info.get('farm_id'))
