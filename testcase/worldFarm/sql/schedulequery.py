#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2019 2019/12/30 11:19
__author__: wei.zhang
__remark__: 任务计划
"""
from testcase.worldFarm.sql.FarmQuery import FarmQuery


class ScheduleQuery(FarmQuery):
    def __init__(self):
        super(ScheduleQuery, self).__init__()
        self.level = 'Schedule'

    def query_task_info_buy_farm_id(self, farm_id):
        """
        通过农场Id查询农场待完成、已过期任务
        :return:
        """
        sql = """SELECT
                    tft.*
                FROM
                    `world-koala`.t_farm_task tft
                WHERE
                    tft.farm_id = '%s'
                    AND tft.is_delete = 0;""" % farm_id
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_task_info_buy_task_id(self, task_id):
        """
        通过任务id查询任务信息
        :return:
        """
        sql = """SELECT
                    tft.*,
                    tu.id as user_id,
                    tu.username,
                    tu.head_img,
                    tu.phone,
                    tu.email
                FROM
                    `world-koala`.t_farm_task tft
                    LEFT JOIN `world-user`.t_user tu ON tu.id = tft.creator_id
                WHERE
                    tft.id = '%s'  
                ORDER BY
                    tft.id DESC;""" % task_id
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_task_info_complete_user(self, task_id):
        """
        通过任务id查询任务信息
        :return:
        """
        sql = """SELECT
                     tu.id,
                     tu.username as userName,
                     tu.head_img as headImg,
                     tu.phone,
                     tu.email
                 FROM
                     `world-koala`.t_farm_task tft
                     LEFT JOIN `world-user`.t_user tu ON tu.id = tft.editor_id
                 WHERE
                     tft.id = '%s'  
                     AND tft.is_delete = 0 
                 ORDER BY
                     tft.id DESC;""" % task_id
        info = self.operate(self.hostip,  sql)
        if info:
            return info[0]
        return

    def query_task_list_buy_farm_id(self, farm_id):
        """
        通过农场id查询任务列表
        :return:
        """
        sql = """SELECT
                    tft.*
                FROM
                    `world-koala`.t_farm_task tft
                WHERE
                    tft.farm_id = '%s'
                AND 
                    tft.is_delete = 0 
                ORDER BY 
                    tft.end_time ASC;""" % farm_id
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_task_list_buy_farm_id_sort(self, farm_id):
        """
        通过农场id查询任务列表,根据当前用户排序，在根据结束时间排序
        :return:
        """
        sql = """
            SELECT
                tft.*
            FROM
                `world-koala`.t_farm_task tft 
            WHERE
                tft.farm_id = '%s' 
                AND tft.is_delete = 0 
            ORDER BY
                tft.end_time ASC;
              """ % farm_id
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_task_list_buy_farm_id_create_task_info(self, farm_id):
        """
        通过农场id查询最新添加的农场任务
        :return:
        """
        sql = """SELECT
                    tft.*
                FROM
                    `world-koala`.t_farm_task tft
                WHERE
                    tft.farm_id = '%s'
                    AND tft.is_delete = 0 ORDER BY tft.id DESC LIMIT 1;""" % farm_id
        info = self.operate(self.hostip,  sql)
        if info:
            return info[0]
        return

    def query_region_list_buy_email(self, email):
        """
        通过邮箱号查询默认农场的围栏信息
        :return:
        """
        sql = """SELECT
                    tfr.* 
                FROM
                    `world-user`.t_user tu
                    LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                    LEFT JOIN `world-koala`.t_farm_region tfr ON tfr.farm_id = tfu.farm_id
                    LEFT JOIN `world-koala`.t_cattle tc ON tfr.id = tc.region_id 
                WHERE
                    tu.email = '%s' 
                    AND tu.is_delete = 0 
                    AND tfu.is_delete = 0 
                    AND tfu.is_default = 1 
                    AND tfr.is_delete = 0 
                    AND tc.is_delete = 0 
                    AND tc.region_id IS NOT NULL 
                    AND tfr.id NOT IN ( SELECT tfg.region_id FROM `world-koala`.t_farm_graze_plan tfg WHERE tfg.is_delete = 0 AND tfg.STATUS = 10 ) 
                GROUP BY
                    tfr.id 
                ORDER BY
                    id DESC;""" % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_graze_plan_buy_region_id(self, regionid):
        """
        通过围栏id查询围栏放牧计划信息
        :return:
        """
        datestr = '%Y-%m-%d %H'
        sql = """SELECT
                    tfgp.*
                FROM
                    `world-koala`.t_farm_graze_plan tfgp
                WHERE
                    tfgp.region_id = '%s'
                    AND tfgp.status = '10'
                    AND tfgp.plan_start_time >= DATE_FORMAT(NOW(),'%s')
                    AND tfgp.is_delete = 0""" % (regionid, datestr)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_graze_plan_buy_farm_id(self, farmid):
        """
        通过农场id查询围栏放牧计划信息
        :return:
        """
        sql = """SELECT
                    tfgp.*
                FROM
                    `world-koala`.t_farm_graze_plan tfgp
                WHERE
                    tfgp.farm_id = '%s'
                    AND tfgp.status = '10'
                    AND tfgp.is_delete = 0""" % farmid
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_plan_info_buy_plan_id(self, plan_id):
        """
        通过计划id查询围栏放牧计划信息
        :return:
        """
        sql = """SELECT
                    tfgp.*
                FROM
                    `world-koala`.t_farm_graze_plan tfgp
                WHERE
                    tfgp.id = '%s';""" % plan_id
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_famr_region_task_list(self, farmid, status):
        """
        查询放牧计划列表
        :param farmid:
        :param status:
        :return:
        """
        sql = """
            SELECT
                * 
            FROM
                `world-koala`.t_farm_graze_plan tfgp 
            WHERE
                tfgp.farm_id = '%s' 
                AND tfgp.STATUS = '%s' 
                AND tfgp.is_delete = 0
                GROUP BY tfgp.region_id
                ORDER BY tfgp.id DESC
              """ % (farmid, status)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_farm_task_receiver_info(self, taskid):
        """
        根据任务查询接收人信息
        :param taskid:
        :return:
        """
        sql = """
            SELECT
                tu.username as userName,
                tu.id,
                tu.email,
                tu.head_img as headImg,
                tu.phone
            FROM
                `world-koala`.t_farm_task_allocation ta
                LEFT JOIN `world-user`.t_user tu ON tu.id = ta.receiver_id 
            WHERE
                ta.task_id = '%s'
                AND tu.is_delete = 0
                AND ta.is_delete = 0
                ORDER BY ta.id DESC;
              """ % taskid
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return
