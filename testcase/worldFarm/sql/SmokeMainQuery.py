#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2019 2019/12/30 13:53
__author__: wei.zhang

"""
from testcase.worldFarm.sql.FarmQuery import FarmQuery

class SmokeMainQuery(FarmQuery):
    def __init__(self):
        super(SmokeMainQuery, self).__init__()
        self.level = 'SmokeMainQuery'

    def query_role_info_buy_farm_id(self, farm_id):
        """
        通过农场id查询农场成员角色为普通人员的成员id
        :param farm_id: 用户所在农场id
        :return:
        """
        sql = """SELECT
                user_id 
            FROM
                t_user_role 
            WHERE
                farm_id = %s 
                AND role_id = 4 
                AND is_delete = 0;""" % farm_id
        info = self.operate(self.hostip,  sql)
        return info

    def query_role_id_buy_farm_id(self, farm_id):
        """
        通过农场id查询农场所有成员id
        :param farm_id: 用户所在农场id
        :return:
        """
        sql = """SELECT
                user_id 
            FROM
                t_user_role 
            WHERE
                farm_id = %s  
                AND is_delete = 0;""" % farm_id
        info = self.operate(self.hostip,  sql)
        return info

    def query_role_not_farmer_id_buy_farm_id(self, farm_id):
        """
        通过农场id非农场主成员id
        :param farm_id: 用户所在农场id
        :return:
        """
        sql = """SELECT
                user_id 
            FROM
                t_user_role 
            WHERE
                farm_id = %s 
                AND role_id != 1 
                AND is_delete = 0;""" % farm_id
        info = self.operate(self.hostip,  sql)
        return info

    def query_not_farm_role_user_id_buy_farm_id(self, farm_id):
        """
        查询一个非当前农场成员的用户id
        :param farm_id: 用户所在农场id
        :return:
        """
        sql = """SELECT
            tu.id 
        FROM
            `world-user`.t_user tu
            LEFT JOIN `world-koala`.t_user_role tur ON tur.user_id = tu.id 
        WHERE
            tur.farm_id != %s 
            LIMIT 1;""" % farm_id
        info = self.operate(self.hostip,  sql)
        return info

    def query_invite_info(self, farm_id, creator_id):
        """
        查询当前农场对应待接受邀请的邀请记录ID
        :param farm_id: 用户所在农场id
        :return:
        """
        sql = """SELECT
                id 
            FROM
                t_user_invite 
            WHERE
                farm_id = %s
                AND creator_id = %s
                AND status = 0;""" % (farm_id, creator_id)
        info = self.operate(self.hostip,  sql)
        return info

    def query_user_info_by_email(self, email):
        sql = 'SELECT * FROM `world-user`.t_user ' \
              'WHERE account_type = 1 AND status = 1 AND is_delete = 0 AND email = "%s";' % email
        info = self.operate(self.hostip, 'world-user', sql)
        # info = self.operate('120.79.59.233', 'world-user', sql)
        return info[0]

    def query_farm_info_by_uid(self, uid):
        sql = 'SELECT * FROM `world-koala`.t_farm WHERE is_delete = 0 AND farmer_id = %s' \
              ' ORDER BY create_time DESC;' % str(uid)
        info = self.operate(self.hostip,  sql)
        # info = self.operate('120.79.59.233',  sql)
        return info[0]
