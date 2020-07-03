#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2020/2/12 14:26
@Author: hengxin
"""


from tools.DataBaseOperate import DataBaseOperate
from tools.Config import Config, Log

host_ip = Config('config').data['database'][Config('config').data['run']]['host_ip']


class KeeperInfoSql(object):
    L = logger("KeeperInfoSql")
    db = DataBaseOperate()

    def query_keeper_by_name(self, name):
        sql = "SELECT * FROM `fc-bee`.t_bee_keeper tbk WHERE tbk.`name` = '%s' AND tbk.is_delete = 0;" % name
        return self.db.operate(host_ip, sql)

    def query_keeper_by_id(self, keeper_id):
        sql = "SELECT * FROM `fc-bee`.t_bee_keeper tbk WHERE tbk.`id` = '%s' AND tbk.is_delete = 0;" % str(keeper_id)
        return self.db.operate(host_ip, sql)

    def query_latest_keeper(self):
        sql = "SELECT * FROM `fc-bee`.t_bee_keeper tbk WHERE tbk.is_delete = 0 ORDER BY tbk.`id` DESC LIMIT 1;"
        return self.db.operate(host_ip, sql)
