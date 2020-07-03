#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2019/12/27 10:51
@Author: hengxin
"""


from tools.DataBaseOperate import DataBaseOperate
from tools.Config import Config, Log
import time

host_ip = Config('config').data['database'][Config('config').data['run']]['host_ip']


class PassportInfoSql(object):
    L = logger("PassportInfoSql")
    db = DataBaseOperate()

    def query_user_by_email(self, email):
        # 通过登录邮箱查询该追花用户
        sql = """
                SELECT tu.*, tui.post_code, tui.role_code FROM `world-user`.t_user tu
                LEFT JOIN `fc-bee`.t_user_info tui ON tui.user_id = tu.`id`
                WHERE tu.email = '%s' AND tu.is_delete = 0 AND tu.account_type = 21;
              """ % email
        return self.db.operate(host_ip, sql)

    def query_user_by_id(self, user_id):
        # 通过登录邮箱查询该追花用户
        sql = """
                SELECT tu.*, tui.post_code, tui.role_code FROM `world-user`.t_user tu
                LEFT JOIN `fc-bee`.t_user_info tui ON tui.user_id = tu.`id`
                WHERE tu.`id` = '%s' AND tu.is_delete = 0 AND tu.account_type = 21;
              """ % str(user_id)
        return self.db.operate(host_ip, sql)

    def query_earliest_user(self):
        # 查询最老的追花账号
        sql = """
                SELECT tu.*, tui.post_code, tui.role_code FROM `world-user`.t_user tu
                LEFT JOIN `fc-bee`.t_user_info tui ON tui.user_id = tu.`id`
                WHERE tu.is_delete = 0 AND tu.account_type = 21 ORDER BY tu.`id` ASC LIMIT 1;
              """
        return self.db.operate(host_ip, sql)

    def query_role_and_post_by_user_id(self, user_id):
        sql = """
                SELECT tu.*, tui.post_code, tui.role_code FROM `world-user`.t_user tu
                LEFT JOIN `fc-bee`.t_user_info tui ON tui.user_id = tu.`id`
                WHERE tu.is_delete = 0 AND tu.account_type = 21 AND tu.`id` = %s;
              """ % str(user_id)
        return self.db.operate(host_ip, sql)

    def remove_specified_mail(self):
        # 软删除固定邮箱
        sql = "UPDATE `world-user`.t_user SET is_delete = 1 WHERE email = 'a.b@c.com.au' " \
              "AND is_delete = 0 AND account_type = 21;"
        return self.db.operate(host_ip, sql)

    def update_specified_mail(self):
        # 更新固定邮箱
        time_stamp = int(time.time())
        sql = "UPDATE `world-user`.t_user SET email = '%d@hx.com' WHERE email = 'a.b@c.com.au';" % time_stamp
        return self.db.operate(host_ip, sql)

    def query_latest_token(self, email):
        # 查询登录邮箱最新token
        sql = """
            SELECT tlt.token FROM `world-passport`.t_login_token tlt 
            LEFT JOIN `world-user`.t_user tu ON tu.id = tlt.user_id
            WHERE tu.email = '%s' AND tu.is_delete = 0 AND tu.account_type = 21 ORDER BY tlt.id DESC LIMIT 1;
            """ % email
        return self.db.operate(host_ip, sql)

    def query_user_by_mobile(self, phone):
        # 通过手机号查询该追花用户
        sql = """
                SELECT tu.*, tui.post_code, tui.role_code FROM `world-user`.t_user tu
                LEFT JOIN `fc-bee`.t_user_info tui ON tui.user_id = tu.`id`
                WHERE tu.phone = '%s' AND tu.is_delete = 0 AND tu.account_type = 21;
              """ % phone
        return self.db.operate(host_ip, sql)

    def query_user_info_by_phone(self, phone):
        # 通过手机号查询追花账号信息
        sql = """
                SELECT
                    * 
                FROM
                    `world-user`.t_user tu 
                WHERE
                    tu.is_delete = 0 
                    AND tu.phone = '%s' 
                    AND tu.account_type IN ( '21', '22' );""" % phone
        return self.db.operate(host_ip, sql)

    def query_user_info_by_id(self, user_id):
        # 通过userId查询追花账号信息
        sql = """
                SELECT
                    * 
                FROM
                    `world-user`.t_user tu 
                WHERE
                    tu.is_delete = 0 
                    AND tu.id = '%s' 
                    AND tu.account_type IN ( '21', '22' );""" % user_id
        return self.db.operate(host_ip, sql)

    def query_user_info(self):
        # 获取所有追花蜂友信息
        sql = """
                SELECT
                    bf.*
                FROM
                    `fc-bee`.t_bee_friend bf
                WHERE
                    bf.is_delete =0;"""
        return self.db.operate(host_ip, sql)

#
# if __name__ == '__main__':
#     pis = PassportInfoSql()
#     pis.query_user_by_email('26632629@qq.com')
