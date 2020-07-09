#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2019 2019/12/30 11:18
__author__: wei.zhang
__remark__: 围栏管理
"""
from testcase.worldFarm.sql.FarmQuery import FarmQuery


class PaddockManage(FarmQuery):
    def __init__(self):
        super(PaddockManage, self).__init__()
        self.level = 'PaddockManage'

    def query_new_region(self, email):
        """
        查詢最新一條圍欄信息
        :param email:
        :return:
        """
        sql = """
                SELECT
                    tfr.`name`,
                    tfr.soil_ph,
                    tfr.soil_type,
                    tfr.color_type,
                    tfr.pasture_type,
                    tfr.id,
                    tfr.perimeter,
                    tfr.region_type,
                    tfr.farm_id,
                    tfr.remark,
                    tfr.area 
                FROM
                    `world-koala`.t_farm_region tfr
                    LEFT JOIN `world-koala`.t_farm_user tf ON tfr.farm_id = tf.farm_id
                    LEFT JOIN `world-user`.t_user tu ON tu.id = tf.user_id 
                WHERE
                    tu.email = '%s' 
                    AND tfr.is_delete = '0' 
                    AND tf.is_default = 1 
                    AND tf.is_delete = 0 
                ORDER BY
                    tfr.id DESC 
                    LIMIT 1;
            """ % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info[0]
        return

    def query_del_region_data_info(self, regionid):
        """
        查詢當前刪除的圍欄
        :param regionid:
        :return:
        """
        sql = "SELECT * FROM `world-koala`.t_farm_region tfr WHERE tfr.id = '%s'" % regionid
        info = self.operate(self.hostip,  sql)
        if info:
            return info[0]
        return

    def query_region_cattle_statistics(self, regionid):
        """
        根据围栏ID查询围栏牲畜统计
        :param regionid:
        :return:
        """
        sql = """
            SELECT
                tc.farm_id,
                tc.region_id,
                IFNULL(sum( CASE WHEN tc.type IN ( '1003', '1005' ) THEN 1 END ),0) AS '幼公牛',
                IFNULL(sum( CASE WHEN tc.type = '1001' THEN 1 END ),0) AS '幼母牛',
                IFNULL(sum( CASE WHEN tc.type IN ( '1004', '1006', '1008' ) THEN 1 END ),0) AS '成年公牛',
                IFNULL(sum( CASE WHEN tc.type IN ('1002','1007') THEN 1 END ),0) AS '成年母牛',
                IFNULL(count( tc.id ),0) AS '围栏牲畜总数' 
            FROM
                `world-koala`.t_cattle tc
            WHERE
                tc.is_delete = '0' 
                AND tc.region_id = '%s'
            ORDER BY
                tc.region_id DESC;
            """ % regionid
        info = self.operate(self.hostip,  sql)
        if info:
            return info[0]
        return

    def query_farm_task_region_data(self, farmid):
        """
        查询带有放牧计划的围栏
        :param farmid:
        :return:
        """
        sql = """
            SELECT
                *,
                IFNULL(ROUND( ( tf.expect_date / ( tf.region_count / tf.grazing_capacity ) ), 3 ),0) AS calculate_day,
                IFNULL(
                ROUND( ( tf.expect_date / ( tf.region_count / tf.grazing_capacity ) - tf.day_delta ), 3 ),
                999999 
                ) AS date_line 
            FROM
                (
            SELECT
                tfg.*,
                ( ( tfg.final_grass_quality + tfg.grow_total ) / tfg.consume_total ) AS temp,
                ( ( ( tfg.final_grass_quality + tfg.grow_total ) / tfg.consume_total ) * tfg.region_area ) AS grazing_capacity 
            FROM
                (
            SELECT
                tfr.*,
                tfgp.id AS tfgp_id,
                tfgp.STATUS,
                tfgp.plan_type,
                tfgp.plan_start_time,
                tfgp.current_quality,
                tfgp.end_quality,
                tfgp.grow_rate,
                tfgp.consume_rate,
                tfgp.expect_date,
                tfgp.create_time AS tfgp_create_time,
                ( CASE WHEN tfgp.expect_date > 6 THEN ( tfgp.expect_date * tfgp.grow_rate ) ELSE tfgp.expect_date END ) AS grow_total,
                ( tfgp.consume_rate * tfgp.expect_date ) AS consume_total,
                ( tfgp.current_quality - tfgp.end_quality ) AS final_grass_quality,
                ( tfr.area / 10000 ) AS region_area,
                ( TIMESTAMPDIFF( MINUTE, tfgp.plan_start_time, NOW( ) ) / ( 24 * 60 ) ) AS day_delta,
                COUNT( tc.id ) AS region_count 
            FROM
                `world-koala`.t_farm_region tfr
                LEFT JOIN (SELECT * FROM `world-koala`.t_cattle t2 WHERE t2.is_delete = 0) tc ON tfr.id = tc.region_id
                LEFT JOIN ( SELECT * FROM `world-koala`.t_farm_graze_plan t1 WHERE t1.is_delete = 0 AND t1.STATUS = 10 ) AS tfgp ON tfr.id = tfgp.region_id 
            WHERE
                tfr.is_delete = 0 
                AND tfr.farm_id = '%s' 
                AND ( tc.is_delete = 0 OR tc.is_delete IS NULL OR ( tfr.is_delete = 0 AND tc.is_delete = 1 ) ) 
                AND ( tfgp.is_delete = 0 OR tfgp.is_delete IS NULL ) 
            GROUP BY
                tfr.id 
                ) AS tfg 
                ) AS tf 
            ORDER BY
                date_line ASC,
                tf.grazing_capacity DESC,
                tf.region_count DESC,
                tf.create_time DESC
              """ % farmid
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return
