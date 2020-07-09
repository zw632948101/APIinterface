#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Wei'
__date__ = '2019/ / '

"""
from random import choice
from testcase.worldFarm import testCase,MessagesQuery


class Messages(testCase):

    fq = MessagesQuery()

    def test_mobile_message_cattle_warn_list(self):
        """
        查询牲畜预警消息列表
        :return:
        """
        farmid = self.fq.query_default_farm(self.email)[0]
        parent = choice(['10', '20', '30'])
        register = self.ka.mobile_message_cattle_warn_list(pn=None, ps=None, parentMsgType=parent, msgType=None,
                                                           farmId=farmid.get('farm_id'))
        self.assertEqual(register['status'], 'OK')

    def test_mobile_message_home_list(self):
        """
        消息列表首页
        1.2.4 修改
        1.2.5 修改
        :return:
        """
        farmid = self.fq.query_default_farm(self.email)[0]
        register = self.ka.mobile_message_home_list(farmId=farmid.get('farm_id'))
        self.assertEqual(register['status'], 'OK')
        mgs_k = register['content'].keys()
        self.assertEqual(list(mgs_k), ['messageCattleWarnOutputs', 'messageOtherTypeOutputs'])

    def test_mobile_message_page_list(self):
        """
        分页查询普通消息列表
        :return:
        """
        farmid = self.fq.query_default_farm(self.email)[0]
        parent = choice(['10', '30'])
        register = self.ka.mobile_message_page_list(pn=None, ps=None, parentMsgType=10, msgType=None,
                                                    farmId=farmid.get('farm_id'))
        self.assertEqual(register['status'], 'OK')

    def test_mobile_message_read(self):
        """
        更新未读为已读消息
        :return:
        """
        register = self.ka.mobile_message_read(msgId='607')
        self.assertEqual(register['status'], 'OK')

    def test_mobile_message_del(self):
        """
        删除消息
        :return:
        """
        register = self.ka.mobile_message_del(msgId='607')
        self.assertEqual(register['status'], 'OK')

    def test_mobile_message_read_all(self):
        """
        移动端-消息-更新该类消息为已读
        :return:
        """
        farmid = self.fq.query_default_farm(self.email)[0]
        parent = choice(['10', '20', '30'])
        register = self.ka.mobile_message_read_all(parentMsgType=parent, msgType=None, title=None,
                                                   farmId=farmid.get('farm_id'))
        self.assertEqual(register['status'], 'OK')

    def test_mobile_message_unread(self):
        """
        移动端-消息-获取未读消息数量
        :return:
        """
        farmid = self.fq.query_default_farm(self.email)[0]
        register = self.ka.mobile_message_unread(parentMsgType=None, farmId=farmid.get('farm_id'))
        self.assertEqual(register['status'], 'OK')
