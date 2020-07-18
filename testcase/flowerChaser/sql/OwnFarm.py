#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2020 2020/07/17 10:08
__author__: xiujuan.chen
__remark__: 我的蜂场
"""
from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.log import log
from utils.environmentConfiguration import config
import random

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class OwnFarmSql(object):
    db = DataBaseOperate()

    def query_nearby_friend(self, lat, lng):
        """
        我的蜂场-周边蜂友地图50km以内数据
        :param lat:
        :param lng:
        :return:
        """
        sql = """SELECT
                    st_distance ( point ( '%s', '%s' ), point ( lat, lng ) ) * 111.195 AS distance,
                    id,
                    user_id,
                    address,
                    lng,
                    lat,
                    `status` 
                FROM
                    `fc-bee`.t_bee_friend 
                WHERE
                    is_delete = 0 
                    AND lng IS NOT NULL 
                    AND lat IS NOT NULL 
                    AND user_id IN ( SELECT user_id FROM `fc-bee`.t_user_role WHERE is_delete = 0 AND role_code IN ( '1002', '1003' ) GROUP BY user_id ) 
                    OR user_id NOT IN ( SELECT user_id FROM `fc-bee`.t_user_role WHERE is_delete = 0 GROUP BY user_id ) 
                    AND `status` !=3
                HAVING
                    distance <= 50;""" % (lat, lng)
        return self.db.operate(host_ip, sql)

    def query_follow_friend(self):
        """
        我的蜂场-周边蜂友地图展示的角色为蜂友，养蜂总监，养蜂技师的数据
        :return:
        """
        sql = """SELECT
                    *
                FROM
                    `fc-bee`.t_bee_friend 
                WHERE
                    is_delete = 0 
                    AND lng IS NOT NULL 
                    AND lat IS NOT NULL 
                    AND (user_id IN ( SELECT user_id FROM `fc-bee`.t_user_role WHERE is_delete = 0 AND role_code IN ( '1002', '1003' ) GROUP BY user_id ) OR user_id NOT IN ( SELECT user_id FROM `fc-bee`.t_user_role WHERE is_delete = 0 GROUP BY user_id ))
                    AND `status` !=3;"""
        return self.db.operate(host_ip, sql)
