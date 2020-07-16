#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2020/1/6 11:40
@Author: hengxin
"""


from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.log import log
from utils.environmentConfiguration import config


host_ip = config.get('database').get(config.get('run')).get('host_ip')


class LogCommentSql(object):
    db = DataBaseOperate()

    def query_comment_by_log_id(self, log_id, is_delete=0):
        # 通过日志ID查询评论
        sql = """
            SELECT 
             *
            FROM `fc-bee`.t_comment tc
            LEFT JOIN `world-user`.t_user tu ON tu.`id` = tc.creator_id
            WHERE tc.is_delete = %s AND tc.log_id = '%s'
            ORDER BY tc.create_time, tc.`id`;
              """ % (is_delete, log_id)
        return self.db.operate(host_ip, sql)

    def query_comment_by_comment_id(self, comment_id, is_delete=0):
        # 通过日志ID查询评论
        sql = """
            SELECT * FROM `fc-bee`.t_comment tc
            WHERE tc.is_delete = %s AND tc.`id` = '%s';
              """ % (is_delete, comment_id)
        return self.db.operate(host_ip, sql)
