#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2019/12/31 16:13
@Author: hengxin
"""


from tools.DataBaseOperate import DataBaseOperate
from tools.Config import Config, Log
import random

host_ip = Config('config').data['database'][Config('config').data['run']]['host_ip']


class WorkRecordSql(object):
    L = logger("WorkLogInfoSql").logger
    db = DataBaseOperate()

    def query_all_log_by_email(self, email):
        # 通过登录邮箱查询所有类型日志
        sql = """
            SELECT * FROM `fc-bee`.t_work_log wl
            LEFT JOIN `fc-bee`.t_extract_log_extend ele ON ele.work_log_id = wl.`id`
            LEFT JOIN `fc-bee`.t_keep_log_detail kld ON kld.log_id = wl.`id`
            LEFT JOIN `fc-bee`.t_keep_log_extend kle ON kle.work_log_id = wl.`id`
            LEFT JOIN `world-user`.t_user tu ON wl.creator_id = tu.`id`
            WHERE wl.is_delete = 0 AND tu.email = '%s'
            GROUP BY wl.id
            ORDER BY wl.`id` DESC LIMIT 20;
            """ % email
        return self.db.operate(host_ip, sql)

    def query_keep_log_by_email(self, email):
        # 通过登录邮箱查询养蜂日志
        sql = """
            SELECT * FROM `fc-bee`.t_work_log wl
            LEFT JOIN `fc-bee`.t_keep_log_detail kld ON kld.log_id = wl.`id`
            LEFT JOIN `fc-bee`.t_keep_log_extend kle ON kle.work_log_id = wl.`id`
            LEFT JOIN `world-user`.t_user tu ON wl.creator_id = tu.`id`
            WHERE wl.is_delete = 0 AND kld.is_delete = 0 AND tu.email = '%s' AND wl.`type` = 2
            ORDER BY wl.`id` DESC;
            """ % email
        return self.db.operate(host_ip, sql)

    def query_keep_log_by_email_without_extend(self, email):
        # 通过登录邮箱查询养蜂日志
        sql = """
            SELECT * FROM `fc-bee`.t_work_log wl
            LEFT JOIN `fc-bee`.t_keep_log_detail kld ON kld.log_id = wl.`id`
            LEFT JOIN `fc-bee`.t_keep_log_extend kle ON kle.work_log_id = wl.`id`
            LEFT JOIN `world-user`.t_user tu ON wl.creator_id = tu.`id`
            WHERE wl.is_delete = 0 AND tu.email = '%s' AND wl.`type` = 2
            ORDER BY wl.`id` DESC;
            """ % email
        return self.db.operate(host_ip, sql)

    def query_extract_log_by_email(self, email):
        # 通过登录邮箱查询摇蜜日志
        sql = """
            SELECT * FROM `fc-bee`.t_work_log wl
            LEFT JOIN `fc-bee`.t_extract_log_extend ele ON ele.work_log_id = wl.`id`
            LEFT JOIN `fc-bee`.t_nectar_source tns ON tns.`id` = ele.nectar_source_id
            LEFT JOIN `world-user`.t_user tu ON wl.creator_id = tu.`id`
            WHERE wl.is_delete = 0 AND tu.email = '%s' AND wl.`type` = 3
            ORDER BY wl.`id` DESC;
            """ % email
        return self.db.operate(host_ip, sql)

    def query_seek_log_by_email(self, email):
        # 通过登录邮箱查询寻蜜日志
        sql = """
            SELECT * FROM `fc-bee`.t_work_log wl
            LEFT JOIN `fc-bee`.t_seek_log_extend sle ON sle.work_log_id = wl.`id`
            LEFT JOIN `world-user`.t_user tu ON wl.creator_id = tu.`id`
            WHERE wl.is_delete = 0 AND tu.email = '%s' AND wl.`type` = 1
            ORDER BY wl.`id` DESC;
            """ % email
        return self.db.operate(host_ip, sql)

    def get_random_type_for_keep_log(self):
        # 通过数据库获取对应类型, 随机生成workType, groupType, detailType
        sql = """
                 # 获取workType字典
                 SELECT tc.`key`, tc.`value` FROM `fc-bee`.t_config tc WHERE tc.`level` = 1 AND tc.`code` = 10004;
                 # 获取groupType字典
                 SELECT tc.parent_key, tc.`key`, tc.`value` FROM `fc-bee`.t_config tc 
                 WHERE tc.`level` = 2 AND tc.`code` = 10004;
                 # 获取detailType字典
                 SELECT tc.parent_key, tc.`key`, tc.`value` FROM `fc-bee`.t_config tc 
                 WHERE tc.`level` = 3 AND tc.`code` = 10004;
               """
        types = self.db.operate(host_ip, sql)
        # work_type_dict = random.choice(types[0])
        random_list = []
        for w in types[0]:
            work_type_id = w['key']
            work_type = w['value']
            self.L.info("workType: %s --> %s" % (work_type, work_type_id))
            group_types = []
            for g in types[1]:
                if g["parent_key"] == work_type_id:
                    group_types.append(g)
            group_type_dict = random.choice(group_types)
            group_type_id = group_type_dict['key']
            group_type = group_type_dict['value']
            self.L.info("groupType: %s --> %s" % (group_type, group_type_id))
            detail_types = []
            for d in types[2]:
                if d["parent_key"] == group_type_id:
                    detail_types.append(d)
            if detail_types:
                detail_type_dict = random.choice(detail_types)
                detail_type_id = detail_type_dict['key']
                detail_type = detail_type_dict['value']
                self.L.info("detailType: %s --> %s" % (detail_type, detail_type_id))
            else:
                detail_type_id = None
                self.L.info("detailType: %s" % detail_type_id)
            random_list.append((work_type_id, group_type_id, detail_type_id))
        return random_list
        # work_type_id = work_type_dict['key']
        # work_type = work_type_dict['value']
        # self.L.info("workType: %s --> %s" % (work_type, work_type_id))
        # group_types = []
        # for g in types[1]:
        #     if g["parent_key"] == work_type_id:
        #         group_types.append(g)
        # group_type_dict = random.choice(group_types)
        # group_type_id = group_type_dict['key']
        # group_type = group_type_dict['value']
        # self.L.info("groupType: %s --> %s" % (group_type, group_type_id))
        # detail_types = []
        # for d in types[2]:
        #     if d["parent_key"] == group_type_id:
        #         detail_types.append(d)
        # if detail_types:
        #     detail_type_dict = random.choice(detail_types)
        #     detail_type_id = detail_type_dict['key']
        #     detail_type = detail_type_dict['value']
        #     self.L.info("groupType: %s --> %s" % (detail_type, detail_type_id))
        # else:
        #     detail_type_id = ""
        #     self.L.info("groupType: %s" % detail_type_id)
        # return work_type_id, group_type_id, detail_type_id\

    def get_all_work_log(self):
        sql = """SELECT * FROM `fc-bee`.t_work_log WHERE is_delete=0;"""
        return self.db.operate(host_ip, sql)

    def get_all_comment_by_email(self, email, is_delete=0):
        sql = """
        SELECT tc.* FROM `fc-bee`.t_comment tc
        LEFT JOIN `world-user`.t_user tu ON tc.creator_id = tu.`id` 
        WHERE tc.is_delete = %s AND tu.email = '%s' 
        ORDER BY tc.`id` DESC;""" % (is_delete, email)
        return self.db.operate(host_ip, sql)


# if __name__ == '__main__':
#     wrs = WorkRecordSql()
#     wrs.get_random_type_for_keep_log()
#     wrs.query_user_by_email('26632629@qq.com')
