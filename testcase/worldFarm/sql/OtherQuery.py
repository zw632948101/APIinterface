#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2019 2019/12/30 11:17
__author__: wei.zhang
__remark__:
"""
from testcase.worldFarm.sql.FarmQuery import FarmQuery


class OtherQuery(FarmQuery):
    def __init__(self):
        super(OtherQuery, self).__init__()
        self.level = 'OtherQuery'

    def query_get_app_version(self):
        """
        查询版最新的本号
        :return:
        """
        sql = "SELECT * FROM `world-koala`.t_app_version ta ORDER BY ta.id DESC LIMIT 1 ;"
        info = self.operate(self.hostip,  sql)
        if info == ():
            return
        return info[0]
