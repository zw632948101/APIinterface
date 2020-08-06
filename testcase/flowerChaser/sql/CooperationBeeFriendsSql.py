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

    def query_user_id(self, moblie):
        """
        通过手机号查询用户ID
        """
        sql = """
                SELECT
                    tu.id 
                FROM
                    `world-user`.t_user tu 
                WHERE
                    tu.phone = '%s' 
                    AND tu.account_type = 21 
                    AND tu.`status` = 1 
                    AND tu.is_delete = 0;
              """ % moblie
        return self.operate(host_ip, sql)

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
        sql = """
                SELECT
                    tc.channel,
                    tc.channel_name AS channelName,
                    tc.`name`,
                    tc.serial_no AS serialNo 
                FROM
                    `agr-ant`.t_camera tc 
                WHERE
                    tc.platform_id = 2 
                ORDER BY
                    tc.channel_name ASC;
              """
        return self.operate(host_ip, sql)

    def query_bee_container_add_repetition(self, status=0):
        """
        查询已经添加网关的手机号
        """
        if status >= 0:
            status = 'AND tbc.`status` = %s' % status
        else:
            status = ''
        sql = """
                SELECT
                    tbf.user_id,
                    tbf.contact_number 
                FROM
                    `fc-bee`.t_bee_container tbc
                    LEFT JOIN `fc-bee`.t_bee_friend tbf ON tbf.user_id = tbc.user_id 
                    AND tbf.is_delete = 0 
                WHERE
                    tbc.is_delete = 0 
                    %s;
              """ % status
        return self.operate(host_ip, sql)

    def query_bee_container_add_mobile(self):
        """
        查询未添加网关的用户
        """
        sql = """
                SELECT
                    tu.phone,
                    tu.username
                FROM
                    `world-user`.t_user tu
                    LEFT JOIN `fc-bee`.t_bee_container tbc ON tbc.user_id = tu.id 
                    AND tbc.`status` = 0 
                    AND tbc.is_delete = 0 
                WHERE
                    tbc.id IS NULL 
                    AND tu.account_type = 21 
                    AND tu.`status` = 1 
                    AND tu.is_delete = 0
                    ORDER BY RAND() LIMIT 1;
              """
        return self.operate(host_ip, sql)

    def query_bee_container_add_devices(self, userid, num):
        """
        查询已添加的设备编号
        """
        sql = """
                SELECT
                    tbc.gateway_no AS gatewayNo,
                    tbc.camera_no AS cameraNo 
                FROM
                    `fc-bee`.t_bee_container tbc 
                WHERE
                    tbc.user_id = '%s' 
                ORDER BY
                    tbc.create_time DESC 
                    LIMIT %s;
              """ % (userid, num)
        return self.operate(host_ip, sql)

    def query_bee_friend_total(self):
        """
        获取列表总数
        """
        sql = """
            SELECT
                count(DISTINCT IF(tbf.platform_status = 1,tbf.user_id,NULL)) AS 'content_normal', 
                count(DISTINCT IF(tbf.platform_status = 2,tbf.user_id,NULL)) AS 'content_quit'
            FROM
                `fc-bee`.t_bee_friend tbf;
              """
        return self.operate(host_ip, sql)[0]

    def query_bee_container_list_devices_all(self, userid):
        """
        获取用户在用网关列表
        """
        sql = """
                SELECT
                    tbc.id,
                    tbc.gateway_no AS gatewayNo
                FROM
                    `fc-bee`.t_bee_container tbc 
                WHERE
                    tbc.user_id = '%s' 
                    AND tbc.`status` = 0
                ORDER BY
                    tbc.id DESC ;
              """ % userid
        return self.operate(host_ip, sql)

    def query_remov_devices_list(self, beeContainerIds):
        """
        根据航吊ID查询已移除信息
        """
        container = "in %s" % str(tuple(beeContainerIds)) if len(beeContainerIds) > 1 else "= '%s'" % beeContainerIds[0]
        sql = """
                SELECT
                    tbc.`status`,
                    tbc.quit_reason
                FROM
                    `fc-bee`.t_bee_container tbc 
                WHERE
                    tbc.id %s;
              """ % container
        return self.operate(host_ip, sql)

    def query_bee_container_user_record(self, userid, u_status):
        """
        获取平台添加移除蜂友设备信息
        """
        if u_status == 1:
            order_by = "ORDER BY tbc.quit_time DESC"
        else:
            order_by = "ORDER BY tbc.create_time DESC"
        sql = """
                SELECT
                    tbc.gateway_no AS gatewayNo,
                    UNIX_TIMESTAMP(tbc.join_time)*1000 AS joinTime,
                    UNIX_TIMESTAMP(tbc.quit_time)*1000 AS quitTime,
	                tbc.quit_reason AS quitReason
                FROM
                    `fc-bee`.t_bee_container tbc 
                WHERE
                    tbc.`status` = %s 
                    AND tbc.user_id = '%s'
                    %s;
              """ % (u_status, userid, order_by)
        return self.operate(host_ip, sql)

    def query_common_bee_friend(self, b_status, b_search=None, pn=0, ps=20):
        """
        查询平台添加蜂友基础信息
        """
        if b_search:
            search_str = " AND (tbf.real_name LIKE '%{0}%' OR tbf.user_name LIKE '%{0}%' OR tbf.contact_number LIKE '%{0}%')".format(
                b_search)
        else:
            search_str = ''
        if pn > 1:
            ps = ps * pn
            pn = ps - 20
        sql = """
                SELECT
                    tbf.address,
                    tbf.age,
                    COUNT( IF(tbc.`status` = 0,tbf.user_id,NULL) ) AS beeContainerCount,
                    tbf.contact_number AS contactNumber,
                    tbf.user_id AS userId,
                    tbf.user_name AS userName,
                    tbf.seniority AS seniority,
                    tbf.real_name AS realName
                FROM
                    `fc-bee`.t_bee_friend tbf
                    LEFT JOIN `fc-bee`.t_bee_container tbc ON tbc.user_id = tbf.user_id 
                    AND tbc.`status` = 0 
                WHERE
                    tbf.platform_status = %s  
                    AND tbf.`status` = 1  
                    %s
                GROUP BY
                    tbf.user_id 
                ORDER BY
                    tbf.create_time DESC 
                    LIMIT %s,%s ;
              """ % (b_status, search_str, pn, ps)
        return self.operate(host_ip, sql)

    def query_location_region(self, userid):
        """
        查询城市地址
        """
        sql = """
            SELECT
                tbf.city,
                tbf.province,
                tbf.county,
                (SELECT tr.`name` FROM `fc-bee`.t_region tr WHERE tbf.province = tr.id) AS provinceName,
                (SELECT tr.`name` FROM `fc-bee`.t_region tr WHERE tbf.city=tr.id) AS cityName,
                (SELECT tr.`name` FROM `fc-bee`.t_region tr WHERE tbf.county=tr.id) AS countyName
            FROM
                `fc-bee`.t_bee_friend tbf
            WHERE
                tbf.user_id = '%s'
                GROUP BY tbf.county;
              """ % userid
        info = self.operate(host_ip, sql)
        if info:
            return info[0]
        return

    def query_native_region(self, userid):
        """
        根据userID 查询籍贯地址
        """
        sql = """
                SELECT
                    tbf.native_city AS city,
                    tbf.native_province AS province,
                    tbf.native_county AS county ,
                    (SELECT tr.`name` FROM `fc-bee`.t_region tr WHERE tbf.native_province = tr.id) AS provinceName,
                    (SELECT tr.`name` FROM `fc-bee`.t_region tr WHERE tbf.native_city=tr.id) AS cityName,
                    (SELECT tr.`name` FROM `fc-bee`.t_region tr WHERE tbf.native_county=tr.id) AS countyName
                FROM
                    `fc-bee`.t_bee_friend tbf
                WHERE
                    tbf.user_id = '%s';
              """ % userid
        info = self.operate(host_ip, sql)
        if info:
            return info[0]
        return

    def query_all_platform_bee_friend(self, b_status):
        """
        查询全部平台蜂友
        """
        sql = """
                SELECT
                    tbf.user_id,
                    tbf.contact_number AS contactNumber,
                    tbf.user_name AS userName,
                    tbf.real_name AS realName 
                FROM
                    `fc-bee`.t_bee_friend tbf
                WHERE
                    tbf.platform_status = %s
                    AND tbf.`status` = 1 
                GROUP BY
                    tbf.user_id
                    ORDER BY rand() LIMIT 1;
              """ % b_status
        info = self.operate(host_ip, sql)
        if info:
            return info[0]
        return

    def query_one_platform_bee_friend(self, userid):
        """
        根据userID查询蜂友信息
        """
        sql = """
                SELECT
                    tbf.user_id AS userId,
                    tbf.contact_number AS contactNumber,
                    tbf.user_name AS userName,
                    tbf.real_name AS realName,
                    tu.head_img AS headImg 
                FROM
                    `fc-bee`.t_bee_friend tbf
                    LEFT JOIN `world-user`.t_user tu ON tu.id = tbf.user_id
                WHERE
                    tbf.platform_status IN(1,2)
                    AND tbf.`status` = 1 
                    AND tbf.user_id = '%s';
              """ % userid
        info = self.operate(host_ip, sql)
        if info:
            return info[0]
        return

    def query_my_bee_field_info(self, userid):
        """
        根据userID查询我的蜂场信息
        """
        sql = """
                SELECT
                    ta.integrated_num AS integratedNum,
                    ta.swarm_num AS swarmNum,
                IF
                    ( ta.major_nectar IS NOT NULL, ta.major_nectar, "" ) AS majorNectar,
                    tnsp.plant_name AS majorNectarStr,
                IF
                    ( ta.queen_bee_species IS NOT NULL, ta.queen_bee_species, "" ) AS queenBeeSpecies,
                CASE
                        ta.queen_bee_species 
                        WHEN 1 THEN
                        '喀尔巴阡' 
                        WHEN 2 THEN
                        '喀意单交' 
                        WHEN 3 THEN
                        '美意' 
                        WHEN 4 THEN
                        '东北黑蜂' 
                        WHEN 5 THEN
                        '国蜂213' 
                        WHEN 6 THEN
                        '黑三交' 
                        WHEN 7 THEN
                        '黄山1号' 
                        WHEN 8 THEN
                        '喀意黄山黑王' 
                        WHEN 9 THEN
                        '喀意黄山2号' 
                        WHEN 10 THEN
                        '喀意黄山蜜王' 
                        WHEN 11 THEN
                        '白山6号' ELSE NULL 
                    END AS queenBeeSpeciesStr,
                    ta.queen_bee_type AS queenBeeType,
                CASE
                        ta.queen_bee_type 
                        WHEN 1 THEN
                        '浆王' 
                        WHEN 2 THEN
                        '糖王' 
                        WHEN 3 THEN
                        '糖浆王' ELSE NULL 
                    END 'queenBeeTypeStr',
                CASE
                        ta.product 
                        WHEN '1' THEN
                        '蜂王浆' 
                        WHEN '2' THEN
                        '花粉' 
                        WHEN '3' THEN
                        '蜂蜜' 
                        WHEN '1,2' THEN
                        '蜂王浆,花粉' 
                        WHEN '1,3' THEN
                        '蜂王浆,蜂蜜' 
                        WHEN '2,3' THEN
                        '花粉,蜂蜜' 
                        WHEN '1,2,3' THEN
                        '蜂王浆,花粉,蜂蜜' ELSE NULL 
                    END 'products',
                IF
                    ( ta.remark IS NOT NULL, ta.remark, "" ) AS remark 
                FROM
                    `fc-bee`.t_apiary ta
                    LEFT JOIN `fc-bee`.t_nectar_source_plant tnsp ON ta.major_nectar = tnsp.`code` 
                    AND tnsp.is_delete = 0 
                WHERE
                    ta.is_delete = 0 
                    AND ta.user_id = '%s';
              """ % userid
        info = self.operate(host_ip, sql)
        if info:
            return info[0]
        return
