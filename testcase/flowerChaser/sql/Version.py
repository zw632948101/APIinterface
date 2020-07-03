#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2020/1/16 11:41
@Author: hengxin
"""


from tools.DataBaseOperate import DataBaseOperate
from tools.Config import Config, Log
import time

host_ip = Config('config').data['database'][Config('config').data['run']]['host_ip']


class VersionInfoSql(object):
    L = logger("VersionInfoSql")
    db = DataBaseOperate()

    def query_latest_update_version(self):
        # 查询最新可升级版本信息
        sql = "SELECT tav.* FROM `fc-bee`.t_app_version tav WHERE tav.is_delete = 0;"
        return self.db.operate(host_ip, sql)


