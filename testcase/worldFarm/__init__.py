#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Wei'
__date__ = '2019/ / '

"""
__all__ = ['CattleManage', 'CattleMap', 'FarmManage', 'Finance', 'LoginAndRegister', 'MessagesQuery', 'OffLine',
           'OtherQuery', 'PaddockManage', 'PersonnelManage', 'ScheduleQuery', 'SmokeMainQuery', 'Statistics',
           'FarmQuery']

import unittest
from interfaces.worldFarm.KoalaAction import KoalaAction
from interfaces.worldFarm.PassportAction import PassportAction
from interfaces.worldFarm.UserAction import UserAction
from interfaces.worldFarm.OfflineAction import OfflineAction
from utils.environmentConfiguration import config
from utils.log import log
from .sql.cattleManage import CattleManage
from .sql.cattleMap import CattleMap
from .sql.farmManage import FarmManage
from .sql.finance import Finance
from .sql.loginAndRegister import LoginAndRegister
from .sql.messagesquery import MessagesQuery
from .sql.offLine import OffLine
from .sql.OtherQuery import OtherQuery
from .sql.paddockManage import PaddockManage
from .sql.personnelManage import PersonnelManage
from .sql.schedulequery import ScheduleQuery
from .sql.SmokeMainQuery import SmokeMainQuery
from .sql.statistics import Statistics
from .sql.FarmQuery import FarmQuery
from utils import DataConversion, coordinateCalculate, TimestampTransform


class testCase(unittest.TestCase):
    tool = DataConversion
    email = config.get('account').get('username')
    password = config.get('account').get('password')
    pa = PassportAction()
    ua = UserAction()
    oa = OfflineAction()
    ka = KoalaAction()
    tt = TimestampTransform()
    cc = coordinateCalculate
    log = log
    category = [{'房屋及建筑': '10030'}, {'水资源': '10040'}, {'道路': '10050'}]
    kinds = {'房屋及建筑': [{'房屋': '10060'}, {'干草棚': '10070'}, {'谷仓': '10080'}, {'棚子': '10090'},
                       {'操作栏': '10100'}, {'门': '10110'}, {'太阳能电站': '10130'}],
             '水资源': [{'水井': '10140'}, {'水坝': '10150'}, {'管道': '10160'}, {'水渠': '10170'},
                     {'饮水槽': '10180'}, {'风车': '10190'}, {'水箱': '10200'}, {'水泵': '10210'}, {'蓄水池': '10240'}],
             '道路': [{'道路': '10220'}]}

    def __init__(self, methodName='runTest'):
        super(testCase, self).__init__(methodName=methodName)

    def tearDown(self):
        pass

    def setUp(self):
        pass
