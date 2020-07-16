#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2019 2019/12/30 11:18
__author__: wei.zhang
__remark__: 人员管理
"""
from testcase.worldFarm.sql.FarmQuery import FarmQuery


class PersonnelManage(FarmQuery):
    def __init__(self):
        super(PersonnelManage, self).__init__()
        self.level = 'PersonnelManage'
