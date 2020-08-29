#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/8/28 16:11 
# @Author : wei.zhang
# @File : NectarSourcePoint.py
# @Software: PyCharm
from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class CraneManagementSQL(DataBaseOperate):
    def __init__(self):
        super(CraneManagementSQL, self).__init__()

    def query_crane_binding_count(self):
        """
        查询添加的设备数量
        """
        sql = """SELECT COUNT(*) AS total FROM `fc-bee`.t_crane tc WHERE tc.binding_status != 0;"""
        return self.operate(host=host_ip, sql=sql)

    def query_crane_binding_serial(self):
        """
        查询已添加的设备信息
        """
        sql = """SELECT * FROM `fc-bee`.t_crane tc WHERE tc.binding_status != 0;"""
        return self.operate(host=host_ip, sql=sql)

    def query_crane_un_binding_list(self):
        """
        查询未绑定设备ID
        """
        sql = """SELECT tc.serial_no FROM `fc-bee`.t_crane tc WHERE tc.binding_status = 0 ORDER BY tc.id DESC;"""
        return self.operate(host=host_ip, sql=sql)

    def query_bee_fried_user_info(self):
        """
        查询真实姓名和手机号
        """
        sql = """SELECT tbf.contact_number,tbf.real_name FROM `fc-bee`.t_bee_friend tbf WHERE tbf.is_delete = 0 AND tbf.contact_number IS NOT NULL;"""
        return self.operate(host=host_ip, sql=sql)

    def query_age_gateway_on_all(self):
        """
        查询未绑定的网关ID
        """
        sql = """
            SELECT
                tg.gateway_no 
            FROM
                `agr-ant`.t_gateway tg 
            WHERE
                tg.platform_id = 2 
                AND tg.is_delete = 0 
                AND tg.gateway_no NOT IN (
                SELECT
                    tc.gateway_no 
                FROM
                    `fc-bee`.t_crane tc 
                WHERE
                tc.binding_status = 1 
                AND tc.is_delete = 0);
              """
        return self.operate(host=host_ip, sql=sql)

    def query_agr_gps_un_binding_all(self):
        """
        查询未绑定的GPS
        """
        sql = """
            SELECT
                tg.device_eui
            FROM
                `agr-ant`.t_bee_gps_device tg 
            WHERE
                 tg.is_delete = 0 
                AND tg.device_eui NOT IN (
                SELECT
                    tc.gps_no 
                FROM
                    `fc-bee`.t_crane tc 
                WHERE
                tc.binding_status = 2 
                AND tc.is_delete = 0);
              """
        return self.operate(host=host_ip, sql=sql)

    def query_crane_binding_user_list(self, serial_no, binding_status):
        """
        查询设备绑定的用户信息
        """
        sql = """
            SELECT
                tcr.id,
                UNIX_TIMESTAMP( tcr.join_time ) * 1000 AS joinTime,
                UNIX_TIMESTAMP( tcr.join_time ) * 1000 AS operatorTime,
                tcr.user_id AS userId,
                tcr.join_operator AS operatorId,
                tbfu.real_name AS realName ,
                tbfo.real_name AS operatorName ,
                tbfu.contact_number AS mobile,
                tbfo.contact_number AS operatorMobile
            FROM
                `fc-bee`.t_crane_relation tcr
                LEFT JOIN `fc-bee`.t_bee_friend tbfu ON tbfu.user_id = tcr.user_id 
                LEFT JOIN `fc-bee`.t_bee_friend tbfo ON tbfo.user_id = tcr.join_operator 
            WHERE
                tcr.serial_no = '%s' 
                AND tcr.`status` = %s;
              """ % (serial_no, binding_status)
        return self.operate(host=host_ip, sql=sql)

    def query_bind_users_by_device(self, serial_no):
        """
        根据设备查询绑定的用户
        """
        sql = """
            SELECT
                *
            FROM
                `fc-bee`.t_crane_relation tcr
            WHERE
                tcr.serial_no = '%s' 
                AND tcr.`status` = 0;
              """ % serial_no
        return self.operate(host=host_ip, sql=sql)

    def query_user_id_serial_on_list(self, userid):
        """
        根据用户ID查询绑定的设备信息
        """
        sql = """
            SELECT
                *
            FROM
                `fc-bee`.t_crane_relation tcr
            WHERE
                tcr.user_id = '%s' 
                AND tcr.`status` = 0;
              """ % userid
        return self.operate(host=host_ip, sql=sql)
