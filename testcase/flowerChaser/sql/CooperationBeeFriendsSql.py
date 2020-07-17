#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/7/16 17:28 
# @Author : wei.zhang
# @File : CooperationBeeFriendsSql.py
# @Software: PyCharm
from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class CooperationBeeFriendsSql(DataBaseOperate):
    def __init__(self):
        super(CooperationBeeFriendsSql, self).__init__()

    def query_bee_container_gateway_list(self):
        """
        查询追花族网关列表
        """
        sql = """
                SELECT
                    tg.gateway_name AS gatewayName,
                    tg.gateway_no AS gatewayNo,
                    tgd.`status` AS `status` ,
                    CASE tgd.`status` WHEN -1 THEN '未激活' WHEN 0 THEN '离线' WHEN 1 THEN '在线' WHEN 2 THEN '重启中' WHEN 3 THEN '升级中' ELSE '未知' END as statusStr
                FROM
                    `agr-ant`.t_gateway tg
                    LEFT JOIN `agr-heart`.t_gateway_data tgd ON tgd.gateway_no = tg.gateway_no 
                    AND tgd.is_delete = 0 
                WHERE
                    tg.platform_id = 2 
                    AND tg.is_delete = 0;
              """
        return self.operate(host_ip, sql)

    def query_bee_container_camera_list(self):
        """
        获取全部摄像头列表
        """
        sql = """SELECT tc.channel,tc.channel_name as channelName,tc.`name`,tc.serial_no as serialNo
                 FROM `agr-ant`.t_camera tc WHERE tc.platform_id = 2 ORDER BY tc.channel_name ASC;"""
        return self.operate(host_ip, sql)
