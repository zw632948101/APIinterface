#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2019 2019/12/30 11:17
__author__: wei.zhang
__remark__: 离线
"""
from testcase.worldFarm.sql.FarmQuery import FarmQuery


class OffLine(FarmQuery):
    def __init__(self):
        super(OffLine, self).__init__()
        self.level = 'OffLine'
