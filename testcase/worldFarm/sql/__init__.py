#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Zhang Wei'
__date__ = '2019/ / '

"""
__all__ = ['cattleManage', 'cattleMap', 'farmManage', 'finance', 'loginAndRegister', 'messagesquery', 'offLine',
           'OtherQuery', 'paddockManage', 'personnelManage', 'schedulequery', 'SmokeMainQuery', 'statistics']

from . import *
from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config

class farmSQL(DataBaseOperate):
    def __init__(self):
        super(farmSQL, self).__init__()
        env = config.get['run']
        hostip_dict = config.get('detabase').get(env)
        self.hostip = hostip_dict
