#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Wei'
__date__ = '2019/ / '

"""
__all__ = ['CattleManage', 'CattleMap', 'FarmManage', 'Finance', 'LoginAndRegister', 'MessagesQuery', 'OffLine',
           'OtherQuery', 'PaddockManage', 'PersonnelManage', 'ScheduleQuery', 'SmokeMainQuery', 'Statistics','FarmQuery']

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
from tools.Session import UserSession
from tools.Common import TimestampTransform, coordinateCalculate
from tools.Tool import Tool


class testCase(unittest.TestCase):
    tool = Tool
    email = config.get('account').get('username')
    user = UserSession()
    pa = PassportAction(user)
    ua = UserAction(user)
    oa = OfflineAction(user)
    ka = KoalaAction(user)
    tt = TimestampTransform()
    cc = coordinateCalculate
    log = log

    def tearDown(self):
        pass

    def setUp(self):
        pass
