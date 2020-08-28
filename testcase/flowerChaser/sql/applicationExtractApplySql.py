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

    def query_my_extractionOfHoney_info(self,userid):
        """
        根据userID查询摇蜜详情
        """
        sql = """
                SELECT
                    tea.address,
                    tea.province,
                    tea.city,
                    tea.county,
                    tea.lng,
                    tea.lat,
                    tea.remark,
                    tea.reason,
                    tea.id,
                    tea.`status`,
                    tea.apply_no AS applyNo,
                    tea.charge_id AS chargeId,
                    UNIX_TIMESTAMP(tea.extract_date)*1000 AS extractDate,
                    UNIX_TIMESTAMP(tea.create_time)*1000 AS createTime,
                    tbf.contact_number AS chargeMobile,
                    IF(tbf.real_name IS NOT NULL,tbf.real_name,tbf.user_name) AS chargeName,
                    (SELECT tc.value_en FROM `fc-bee`.t_config tc WHERE tc.`code` = '10001' AND tc.`key` = tur.role_code) AS chargeRole,
                    CASE tea.`status` WHEN 10 THEN '待处理' WHEN 20 THEN '待审核' WHEN 10 THEN '待摇蜜' END statusDesc
                FROM
                    `fc-trade`.t_extract_apply tea 
                    LEFT JOIN `fc-bee`.t_bee_friend tbf ON tbf.user_id = tea.charge_id AND tbf.is_delete = 0 AND tbf.`status` = 1 AND tbf.user_id IS NOT NULL
                    LEFT JOIN `fc-bee`.t_user_role tur ON tur.user_id = tea.charge_id AND tur.is_delete = 0
                WHERE
                    tea.creator_id = %s 
                    AND tea.is_delete = 0 
                    AND tea.`status` IN ( 10, 20, 30);
              """ % userid
        info = self.operate_db(sql=sql)
        if info:
            return info[0]
        return

    def query_userInfo_containerCount(self,userid):
        """
        查询用户信息和航吊数量
        """
        sql = """
                SELECT
                    tbf.province,
                    tbf.city,
                    tbf.county,
                    tbf.address,
                    tbf.lat,
                    tbf.lng,
                    tbf.user_name AS userName,
                    IF(tbf.real_name IS NOT NULL,tbf.real_name,'') AS realName,
                    COUNT(tbc.gateway_no) AS beeContainerCount
                FROM
                    `fc-bee`.t_bee_friend tbf 
                    LEFT JOIN `fc-bee`.t_bee_container tbc ON tbf.user_id = tbc.user_id AND tbc.is_delete = 0 AND tbc.`status` = 0
                WHERE
                    tbf.user_id = %s 
                    AND tbf.is_delete = 0 
                    AND tbf.`status` = 1
                    GROUP BY tbf.user_id ;
              """ % userid
        info = self.operate_db(sql=sql)
        if info:
            return info[0]
        return