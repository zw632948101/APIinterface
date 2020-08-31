#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/8/29 15:37 
# @Author : wei.zhang
# @File : NectarSourcePointSql.py
# @Software: PyCharm

from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class NectarSourcePointSql(DataBaseOperate):
    def __init__(self):
        super(NectarSourcePointSql, self).__init__()

    def query_plant_code_all(self):
        """
        查询全部蜜源植物code
        """
        sql = """SELECT `code` FROM `fc-bee`.t_nectar_source_plant;"""
        return self.operate(host=host_ip, sql=sql)

    def query_add_nectar_point(self, province, city, county, plantCode):
        """
        查询蜜源点信息
        """
        sql = """SELECT * FROM `fc-bee`.t_nectar_source_point WHERE province=%s AND city=%s AND county=%s AND plant_code=%s ;""" % (
            province, city, county, plantCode)
        return self.operate(host=host_ip, sql=sql)

    def query_nectar_source_point_all(self):
        """
        查询全部的蜜源点 V2.5
        """
        sql = """
            SELECT * FROM `fc-bee`.t_nectar_source_point tp WHERE tp.is_delete = 0;
              """
        return self.operate(host=host_ip, sql=sql)

    def query_current_user_creation_point(self, userid, usertype=1):
        """
        根据type类型组装查询，1查询当前用户，2查询非当前用户
        """
        if usertype == 1:
            user = "tp.creator_id = %s" % userid
        else:
            user = "tp.creator_id != %s" % userid
        sql = """SELECT * FROM `fc-bee`.t_nectar_source_point tp WHERE tp.is_delete = 0 AND %s;""" % user
        return self.operate(host=host_ip, sql=sql)
