#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/8/5 11:12 
# @Author : wei.zhang
# @File : applicationExtractApplySql.py
# @Software: PyCharm


from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class applicationExtractApplySql(DataBaseOperate):
    def __init__(self):
        super(applicationExtractApplySql, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def query_added_as_platform_befriend(self):
        """
        查询已添加为平台蜂友的账户并且未添加摇蜜申请
        """
        sql = """
                SELECT
                    tbf.user_id,
                    tsi.province,
                    tsi.city,
                    tsi.county,
                    tsi.address,
                    tsi.lng,
                    tsi.lat
                FROM
                    `fc-bee`.t_bee_friend tbf
                    INNER JOIN `fc-bee`.t_swarm_info tsi ON tbf.user_id = tsi.user_id AND tsi.province IS NOT NULL
                WHERE
                    tbf.platform_status = 1 
                    AND tbf.`status` = 1 
                    AND tbf.is_delete = 0
                    AND tbf.user_id NOT IN(SELECT tea.creator_id FROM `fc-trade`.t_extract_apply tea WHERE tea.`status` IN(10,20,30));
              """
        return self.operate_db(sql=sql)

    def query_extract_apply_data_info(self, userid, status, extractDate):
        """
        查询申请摇蜜信息
        """
        sql = """
                SELECT
                    * 
                FROM
                    `fc-trade`.t_extract_apply tea 
                WHERE
                    tea.creator_id = {0} 
                    AND tea.is_delete = 0 AND tea.`status` = {1} 
                    AND tea.extract_date = FROM_UNIXTIME({2},'%Y-%m-%d')
                    ORDER BY tea.create_time DESC LIMIT 1;
              """.format(userid, status, extractDate / 1000)
        info = self.operate_db(sql=sql)
        if info:
            return info[0]
        return

    def query_application_for_molasses_has_been_added(self):
        """
        查询已添加摇蜜申请的用户 ID
        """
        sql = """
                SELECT
                    tea.creator_id  
                FROM
                    `fc-trade`.t_extract_apply tea 
                WHERE
                    tea.is_delete = 0 
                    AND tea.`status` IN ( 10, 20, 30 ) 
                ORDER BY
                    tea.create_time DESC;
              """
        return self.operate_db(sql=sql)
