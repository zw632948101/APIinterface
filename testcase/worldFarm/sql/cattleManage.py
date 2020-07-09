#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2019 2019/12/30 9:39
__author__: wei.zhang
__remark__: 牲畜管理
"""
from testcase.worldFarm.sql.FarmQuery import FarmQuery


class CattleManage(FarmQuery):
    def __init__(self):
        super(CattleManage, self).__init__()
        self.level = 'CattleManage'

    def query_bull_id_buy_email(self, email):
        """
        通过邮箱号查询用户默认农场的成年公牛牲畜id
        :param email: 用户邮箱
        :return:
        """
        sql = """SELECT
                    tc.id,
                    tc.cattle_name
                FROM
                    `world-user`.t_user tu
                LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                LEFT JOIN `world-koala`.t_cattle tc ON tfu.farm_id = tc.farm_id
                WHERE
                    tu.email = '%s'
                    AND tu.is_delete = 0
                    AND tfu.is_delete = 0
                    AND tc.is_delete = 0
                    AND tfu.is_default = 1
                    AND tc.type in('1004','1008');""" % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_all_bull_id_buy_email(self, email):
        """
        通过邮箱号查询用户默认农场的公牛牲畜id
        :param email: 用户邮箱
        :return:
        """
        sql = """SELECT
                    tc.id,
                    tc.cattle_name
                FROM
                    `world-user`.t_user tu
                    LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                    LEFT JOIN `world-koala`.t_cattle tc ON tfu.farm_id = tc.farm_id 
                WHERE
                    tu.email = '%s' 
                    AND tu.is_delete = 0 
                    AND tfu.is_delete = 0 
                    AND tc.is_delete = 0 
                    AND tfu.is_default = 1 
                    AND tc.type in('1004','1003','1008','1005','1006');""" % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_no_breeding_cow_id_buy_email(self, email):
        """
        通过邮箱号查询用户默认农场下未添加交配记录的成年母牛牲畜id
        :return:
        """
        sql = """SELECT
                    tc.id
                FROM
                    `world-user`.t_user tu
                    LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                    LEFT JOIN `world-koala`.t_cattle tc ON tfu.farm_id = tc.farm_id 
                WHERE
                    tu.email = '%s' 
                    AND tfu.is_delete = 0 
                    AND tc.is_delete = 0 
                    AND tfu.is_default = 1 
                    AND tc.stage_status != 10
                    AND tc.type in('1002','1007');""" % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_breeding_cow_id_buy_email(self, email):
        """
        通过邮箱号查询用户默认农场下已经添加交配记录的成年母牛/种母牛牲畜id
        :return:
        """
        sql = """SELECT
                    tc.id
                FROM
                    `world-user`.t_user tu
                    LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                    LEFT JOIN `world-koala`.t_cattle tc ON tfu.farm_id = tc.farm_id 
                WHERE
                    tu.email = '%s' 
                    AND tu.is_delete = 0 
                    AND tfu.is_delete = 0 
                    AND tc.is_delete = 0 
                    AND tfu.is_default = 1 
                    AND tc.stage_status != 10
                    AND tc.stage_status != 20
                    AND tc.stage_status != 30
                    AND tc.is_delete = 0
                    AND (tc.type = '1002' OR tc.type = '1007');""" % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_breeding_cow_id_buy_email(self, email):
        """
        通过邮箱号查询用户默认农场下处于已交配状态下的成年母牛牲畜id
        :return:
        """
        sql = """SELECT
                    tc.id
                FROM
                    `world-user`.t_user tu
                    LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                    LEFT JOIN `world-koala`.t_cattle tc ON tfu.farm_id = tc.farm_id 
                WHERE
                    tu.email = '%s' 
                    AND tu.is_delete = 0 
                    AND tfu.is_delete = 0 
                    AND tc.is_delete = 0 
                    AND tfu.is_default = 1 
                    AND tc.is_delete = 0
                    AND tc.type = '1002';""" % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_freq_cow_id_buy_email(self, email):
        """
        通过邮箱号查询用户默认农场下处于怀孕状态下的成年母牛牲畜id
        :return:
        """
        sql = """SELECT
                    tc.id,
                    tc.cattle_name,
                    tc.farm_id,
                    tc.type
                FROM
                    `world-user`.t_user tu
                LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                LEFT JOIN `world-koala`.t_cattle tc ON tfu.farm_id = tc.farm_id
                WHERE
                    tu.email = '%s'
                    AND tu.is_delete = 0
                    AND tfu.is_delete = 0
                    AND tc.is_delete = 0
                    AND tc.stage_status = 50
                    AND tfu.is_default = 1
                    AND tc.type = '1002';""" % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_relationship_buy_email(self, email):
        """
        通过邮箱号查询用户默认农场下含血缘关系的牲畜信息
        :return:
        """
        sql = """SELECT
                    tc.id,
                    tc.p_id,
                    tc.m_id,
                    tc.farm_id,
                    tc.p_name,
                    tc.m_name,
                    tc.cattle_name
                FROM
                    `world-user`.t_user tu
                    LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                    LEFT JOIN  `world-koala`.t_cattle tc ON tfu.farm_id = tc.farm_id
                WHERE
                    tu.email = '%s'
                    AND tu.is_delete = 0
                    AND tfu.is_delete = 0
                    AND tfu.is_default = 1
                    AND (tc.p_id IS NOT NULL OR tc.m_id IS NOT NULL )
                    AND tc.is_delete = 0 ;""" % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_stage_cycle(self, email, stage_status):
        """
        查询默认农场下处于怀孕周期内的牲畜怀孕周期记录信息
        :return:
        """
        sql = """SELECT
                    tcsc.id,
                    tcsc.cattle_id,
                    tcsc.stage_status,
                    tcsc.calving_date
                FROM
                    `world-user`.t_user tu
                    LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                    LEFT JOIN  `world-koala`.t_cattle tc ON tfu.farm_id = tc.farm_id
                    LEFT JOIN `world-koala`.t_cattle_stage_cycle tcsc ON tcsc.cattle_id = tc.id
                WHERE
                    tu.email = '%s'
                    AND tcsc.stage_status = '%s'
                    AND tu.is_delete = 0
                    AND tfu.is_delete = 0
                    AND tfu.is_default = 1
                    AND tc.is_delete = 0
                    AND tcsc.is_delete = 0;""" % (email, stage_status)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_cattle_all_cycle(self, cattle_id, is_delete=0):
        """
        查询牲畜生理周期信息
        :return:
        """
        if is_delete == 0:
            is_delete = "AND is_delete = 0"
        else:
            is_delete = "AND is_delete = '%s'" % is_delete
        sql = """SELECT
                        tcsc.*
                    FROM
                        `world-koala`.t_cattle_stage_cycle tcsc
                    WHERE
                        tcsc.cattle_id = '%s'
                        '%s'
                        """ % (cattle_id, is_delete)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_stage_cycle_info_buy_stage_id(self, cycle_id):
        """
        通过怀孕周期记录id查询记录信息
        :return:
        """
        sql = """SELECT
                    tcsc.*
                FROM
                    `world-koala`.t_cattle_stage_cycle tcsc
                WHERE
                    tcsc.id = '%s';""" % cycle_id
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_preg_info_buy_id(self, preg_id):
        """
        通过怀孕记录id查询记录信息
        :return:
        """
        sql = """SELECT
                        tcp.* 
                    FROM
                        `world-koala`.t_cattle_preg tcp 
                    WHERE
                        tcp.id = '%s';""" % preg_id
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_calving_info_buy_cattle_id(self, cattle_id):
        """
        通过牲畜id查询产犊记录信息
        :return:
        """
        sql = """SELECT
                        tcc.* 
                    FROM
                        `world-koala`.t_cattle_calving tcc 
                    WHERE
                        tcc.is_delete = 0 
                        AND tcc.cattle_id = '%s'
                        ORDER BY tcc.id DESC ;""" % cattle_id
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_offspring_info_buy_cattle_id(self, cattle_id):
        """
        通过牲畜公牛id查询牲畜的后代信息
        :return:
        """
        sql = """
                SELECT
                    tc.*,
                    tco.`value` 
                FROM
                    `world-koala`.t_cattle tc
                    LEFT JOIN `world-koala`.t_config tco ON tco.`key` = tc.type 
                WHERE
                    ( tc.p_id = '%s' OR tc.m_id = '%s' ) 
                    AND tc.is_delete = 0 
                    AND tco.is_delete = 0 
                    AND tco.`code` = 10004 
                ORDER BY
                    tc.id DESC;""" % (cattle_id, cattle_id)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_cow_id_buy_email_unbreeding_num(self, email, stagestatus=None):
        """
        通过邮箱号查询用户默认农场的成年母牛牲畜id
        :return:
        """
        if stagestatus is None:
            stagestatus = "IN(30, 31, 32, 33)"
        else:
            stagestatus = "= %s" % stagestatus
        sql = """SELECT
                    tc.id
                FROM
                    `world-user`.t_user tu
                LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                LEFT JOIN `world-koala`.t_cattle tc ON tfu.farm_id = tc.farm_id
                WHERE
                    tu.email = '%s'
                    AND tu.is_delete = 0
                    AND tfu.is_delete = 0
                    AND tc.is_delete = 0
                    AND tfu.is_default = 1
                    AND tc.stage_status %s 
                    AND tc.type = '1002';""" % (email, stagestatus)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_new_cattle_breeding_date_buy_email(self, email):
        """
        通过邮箱号查询当前用户默认农场下添加最新的牲畜交配记录
        :return:
        """
        sql = """SELECT
                    tcb.id,
                    tcb.cattle_id,
                    tcb.start_date,
                    tcb.end_date,
                    tcb.remark,
                    tcb.create_time,
                    tfu.farm_id,
                    tcb.predict_calving_date
                FROM
                    `world-user`.t_user tu
                    LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                    LEFT JOIN `world-koala`.t_farm tf ON tf.id = tfu.farm_id
                    LEFT JOIN `world-koala`.t_cattle tc ON tc.farm_id = tfu.farm_id
                    LEFT JOIN `world-koala`.t_cattle_breeding tcb ON tcb.cattle_id = tc.id
                WHERE
                    tu.email = '%s'
                    AND tcb.is_delete = 0 
                    AND tfu.is_default = 1
                ORDER BY
                    tcb.create_time DESC 
                    LIMIT 1;""" % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_breeding_date_buy_cattle_id(self, cattle_id, btype=None, sdate=None):
        """
        通过牲畜id查询牲畜的最新交配记录
        :return:
        """

        btype = "AND tcb.breeding_type = %s" % btype if btype else ''
        sdate = "AND tcb.start_date = '%s'" % sdate if sdate else ''
        if cattle_id and btype and sdate:
            num = len(cattle_id) if isinstance(cattle_id, tuple) else 1
        else:
            num = 10
        if isinstance(cattle_id, tuple):
            cattle_id = "in%s" % str(cattle_id)
        else:
            cattle_id = "= %s" % cattle_id

        sql = """SELECT
                    tcb.id,
                    tcb.cattle_id,
                    tcb.start_date,
                    tcb.end_date,
                    tcb.remark,
                    tcb.breeding_type,
                    tcbr.num,
                    GROUP_CONCAT( tcbr.cattle_id SEPARATOR ',' ) AS bull_id 
                FROM
                    `world-koala`.t_cattle_breeding tcb 
                    LEFT JOIN `world-koala`.t_cattle_breeding_relation tcbr ON tcbr.batch_no = tcb.batch_no
                WHERE
                    tcb.is_delete = 0 
                    AND tcb.cattle_id %s 
                    AND (tcbr.is_delete = 0  OR tcbr.is_delete IS NULL)
                    %s
	                %s
                GROUP BY 
                    tcb.id
                ORDER BY
                    tcb.create_time DESC
                    LIMIT %s;""" % (cattle_id, btype, sdate, num)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_breeding_detail_buy_id(self, breeding_id):
        """
        通过交配记录id查询交配记录详情信息
        :param breeding_id:
        :return:
        """
        sql = """SELECT
                        tcb.* ,
                        tcbr.num,
                        tcbr.cattle_id as bull_id
                    FROM
                        `world-koala`.t_cattle_breeding tcb
                        LEFT JOIN `world-koala`.t_cattle_breeding_relation tcbr ON tcb.batch_no = tcbr.batch_no
                    WHERE 
                        tcb.id = '%s' 
                        AND tcb.is_delete = 0;""" % breeding_id
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_breeding_bull_cattle(self, cattleid):
        """
        查询母牛对应交配公牛
        :param cattleids:
        :return:
        """
        sql = """
                SELECT 
                    tcbr.cattle_id 
                FROM `world-koala`.t_cattle_breeding tcb 
                LEFT JOIN `world-koala`.t_cattle_breeding_relation tcbr 
                ON tcb.batch_no = tcbr.batch_no 
                WHERE tcb.cattle_id = '%s';
              """ % cattleid
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_cattle_preg_date_info(self, cttleids, check_type=None, check_date=None, check_result=None):
        """
        查询母牛新加怀孕记录
        :param cttleids:
        :return:
        """
        if isinstance(cttleids, tuple):
            cttleids = "in%s" % str(cttleids)
        else:
            cttleids = "= %s" % cttleids

        check_date = "AND tcp.check_date = '%s'" % check_date if check_date else ''
        check_type = "AND tcp.check_type = '%s'" % check_type if check_type else ''
        check_result = "AND tcp.check_result = '%s'" % check_result if check_result else ''

        sql = """
            SELECT tcp.id,tcp.cattle_id,tcp.check_date,tcp.check_result,tcp.remark 
            FROM `world-koala`.t_cattle_preg tcp 
            WHERE tcp.cattle_id %s 
            AND tcp.is_delete = '0'
            %s
            %s
            %s
            ORDER BY tcp.id DESC
        """ % (cttleids, check_type, check_date, check_result)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_preg_date_buy_email(self, email):
        """
        通过邮箱号查询当前用户默认农场添加的怀孕记录
        :return:
        """
        sql = """SELECT
                    tcp.id,
                    tcp.cattle_id,
                    tcp.check_date,
                    tcp.check_result,
                    tcp.remark,
                    tcp.creator_id,
                    tcp.editor_id
                FROM
                    `world-user`.t_user tu
                    LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                    LEFT JOIN `world-koala`.t_farm tf ON tf.id = tfu.farm_id
                    LEFT JOIN `world-koala`.t_cattle tc ON tc.farm_id = tfu.farm_id
                    LEFT JOIN `world-koala`.t_cattle_preg tcp ON tu.id = tcp.creator_id 
                WHERE
                    tu.email = '%s' 
                    AND tfu.is_default = 1
                    AND tcp.is_delete = 0 
                    AND tc.is_delete = 0
                    AND tcp.is_delete = 0
                    group by tcp.cattle_id;""" % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return


    def query_cattle_weaning_info(self, cattleid):
        """
        查询断奶记录
        :return:
        """
        if isinstance(cattleid, tuple):
            cattleid = "in%s" % str(cattleid)
        else:
            cattleid = "= %s" % cattleid
        sql = "SELECT tcw.cattle_id,tcw.weaning_date,tcw.weaning_weight FROM " \
              "`world-koala`.t_cattle_weaning tcw WHERE tcw.cattle_id %s " \
              "ORDER BY tcw.id DESC;" % cattleid
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_cow_cattle_id_list(self, email):
        """
        查询农场所有成年母牛
        :return:
        """
        sql = """SELECT
                        tc.id,
                        tc.type,
                        tc.cattle_name
                    FROM
                        `world-user`.t_user tu
                        LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                        LEFT JOIN `world-koala`.t_cattle tc ON tfu.farm_id = tc.farm_id 
                    WHERE
                        tu.email = '%s' 
                        AND tu.is_delete = 0 
                        AND tfu.is_delete = 0 
                        AND tc.is_delete = 0 
                        AND tfu.is_default = 1 
                        AND tc.type in(1002,1007);""" % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_weaning_detail(self):
        """
        查询断奶记录
        :return:
        """
        sql = "select * from `world-koala`.`t_cattle_weaning` tcw order by tcw.id desc limit 1;"
        info = self.operate(self.hostip,  sql)
        if info:
            return info[0]
        return

    def query_weaning_detail_buy_id(self, weaning_id):
        """
        通过断奶记录id查询断奶信息
        :param weaning_id:
        :return:
        """
        sql = """SELECT
                    *
                FROM
                    `world-koala`.t_cattle_weaning tcw
                WHERE
                     tcw.id = '%s';""" % weaning_id
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_cattle_farm_region_id(self, cattleid='', deviceid=''):
        """
        查询最新一条牲畜ID和所在围栏
        :return:
        """
        if cattleid != '':
            cattleid = "AND tc.id = '%s'" % cattleid

        if deviceid != '':
            deviceid = "AND tc.device_id IS NOT NULL AND tc.device_id != ''"

        sql = "SELECT tc.id,tc.farm_id,tc.region_id,tc.device_id FROM `world-koala`.t_cattle tc " \
              "WHERE tc.is_delete = '0' %s%s ORDER BY tc.id DESC;" % (cattleid, deviceid)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_farm_id_and_region_id(self, email):
        """
        查询农场信息和围栏
        :return:
        """
        sql = "SELECT tf.id farm_id,tg.id region_id,tf.number,tf.name,tf.farmer_id,tf.address,tf.province_id," \
              "tf.lng,tf.lat,tf.right_area,tf.currency_type FROM `world-koala`.t_farm tf " \
              "LEFT JOIN `world-user`.t_user tu ON tf.farmer_id = tu.id " \
              "LEFT JOIN `world-koala`.t_farm_region tg ON tf.id = tg.farm_id  " \
              "WHERE tu.email = '%s' AND tf.is_delete = '0' AND (tg.is_delete = '0' OR tg.is_delete IS NULL);" % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_new_cattle_info(self, farmid, regionid, cattlename, nlis):
        """
        查询最新添加的牲畜详情
        :param farmid:
        :param regionid:
        :param cattlename:
        :param nlis:
        :return:
        """
        regionid = "AND tc.region_id = '%s'" % regionid if regionid else ''
        sql = """
                SELECT
                    * 
                FROM
                    `world-koala`.t_cattle tc 
                WHERE
                    tc.farm_id = '%s' 
                    %s
                    AND tc.cattle_name = '%s'
                    AND tc.nlis = '%s';
        """ % (farmid, regionid, cattlename, nlis)
        info = self.operate(self.hostip,  sql)
        if info:
            return info[0]
        return

    def query_cattle_detail_buy_email(self, email):
        """
        通过邮箱号查询默认农场下的牲畜信息
        :return:
        """
        sql = """SELECT
                    tc.*
                FROM
                    `world-user`.t_user tu
                    LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                    LEFT JOIN `world-koala`.t_cattle tc ON tc.farm_id = tfu.farm_id
                WHERE
                    tu.email = '%s'
                    AND tfu.is_delete = 0
                    AND tfu.is_default = 1
                    AND tc.is_delete = 0 ORDER BY id DESC;""" % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_cattle_detail_buy_cattle_id(self, cattle_id):
        """
        通过牲畜id查询牲畜详情
        :return:
        """
        sql = """SELECT
                    tc.*
                FROM
                    `world-koala`.t_cattle tc
                WHERE
                    tc.id = '%s' LIMIT 1;""" % cattle_id
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_default_farm_cattle_info_list(self, email, devicetype=None):
        """
        查询当前农场的所有绑定设备的牲畜
        :param farmid:
        :param devicetype:
        :return:
        """

        devicetype = "AND tc.device_type in(%s)" % devicetype if devicetype else ''

        sql = """
                SELECT
                    tc.id,
                    tc.device_id,
                    tc.farm_id,
                    tc.region_id
                FROM
                    `world-koala`.t_cattle tc
                    LEFT JOIN `world-shark`.t_sync_device_bind ts ON tc.id = ts.cattle_id 
                    LEFT JOIN `agr-ant`.t_device td ON tc.device_id = td.device_eui
                    LEFT JOIN `world-koala`.t_farm_user tfu ON tc.farm_id = tfu.farm_id
                    LEFT JOIN `world-user`.t_user tu ON tu.id = tfu.user_id
                WHERE
                    tu.email = '%s'
                    AND tc.is_delete = '0' 
                    AND ts.is_delete = '0'
                    AND tfu.is_default = 1
                    AND td.device_eui is not NULL
                    %s
              """ % (email, devicetype)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_all_farm_not_bind_cattle(self, email):
        """
        查询农场内没有绑定设备的牲畜
        :param email:
        :return:
        """
        sql = """
            SELECT
                tc.id,
                tc.device_id,
                tc.farm_id,
                tc.region_id 
            FROM
                `world-koala`.t_cattle tc
                LEFT JOIN `world-koala`.t_farm_user tfu ON tc.farm_id = tfu.farm_id
                LEFT JOIN `world-user`.t_user tu ON tu.id = tfu.user_id 
            WHERE
                tu.email = '%s' 
                AND tc.is_delete = '0' 
                AND tfu.is_default = 1
                AND tc.device_type IS NULL
                GROUP BY tc.id
              """ % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_may_device_update(self, email):
        """
        查询已加入农场的所有信号中继设备
        :param farmid:
        :return:
        """
        sql = """
                SELECT
                    tdp.device_eui,
                    tdp.farm_id
                FROM
                    `world-shark`.t_sync_device_bind tdp
                    LEFT JOIN `world-koala`.t_farm_user tf ON tdp.farm_id = tf.farm_id
                    LEFT JOIN `world-user`.t_user tu ON tf.user_id = tu.id 
                    LEFT JOIN `agr-ant`.t_device td ON tdp.device_eui = td.device_eui
                WHERE
                    tu.email = '%s' 
                    AND tf.is_delete = '0' 
                    AND tdp.cattle_id IS NULL
                    AND td.product_type = '耳标/LoRa耳标'
                    AND tdp.is_delete = '0';
              """ % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_bind_device_id(self, farmid, deviceid):
        """
        查询绑定的信号中继
        :param farmid:
        :param deviceid:
        :return:
        """
        sql = """
                SELECT
                    * 
                FROM
                    `world-shark`.t_sync_device_bind ts 
                WHERE
                    ts.farm_id = '%s' 
                    AND ts.device_eui = '%s' 
                    AND ts.is_delete = 0;
              """ % (farmid, deviceid)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_farm_all_cattle_list(self, farmid, regionid=None, varietyid=None, type_=None, sex=None, level=None,
                                   stage=None, bind=None):
        """

        :param farmid:
        :param regionid:
        :param varietyid:
        :param type_:
        :param sex:
        :param level:
        :param stage:
        :param bind:
        :return:
        """
        regionid = "tc.region_id IN %s\n" % regionid if regionid else ''
        varietyid = "tc.variety_id IN %s\n" % varietyid if varietyid else ''
        type_ = "tc.type IN %s\n" % type_ if type_ else ''
        sex = "tc.sex IN %s\n" % sex if sex else ''
        level = "tc.level IN %s\n" % level if level else ''
        stage = "tc.stage_status IN %s\n" % stage if stage else ''
        if bind is None:
            bind = "AND ( tc.device_id IS NULL OR tc.device_id = '' )"
        else:
            bind = "AND (tc.device_type is not NULL or tc.device_type != '')"
        sqlstr = regionid + varietyid + type_ + sex + level + stage + bind
        sql = """
                SELECT
                    * 
                FROM
                    `world-koala`.t_cattle tc 
                WHERE
                  tc.is_delete = 0
                    %s
                    ORDER BY tc.id DESC
              """ % sqlstr

        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_no_weaning_cattle(self, farmid):
        """

        :param farmid:
        :return:
        """
        sql = """
                SELECT
                    * 
                FROM
                    `world-koala`.t_cattle tc 
                WHERE
                  tc.is_delete = 0
                    AND tc.farm_id = '%s'
                    AND tc.type in(1003,1001,1005)
                    ORDER BY tc.id DESC
              """ % farmid
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_cattle_breeding_id_info(self, bid):
        """
        通过交配记录id查询交配记录信息
        :param bid:
        :return:
        """
        sql = """
            SELECT
                tcb.id,
                tcb.cattle_id,
                tcb.start_date,
                tcb.end_date,
                tcb.remark,
                tcb.breeding_type,
                tcbr.num,
                GROUP_CONCAT( tcbr.cattle_id SEPARATOR ',' ) AS bull_id 
            FROM
                `world-koala`.t_cattle_breeding tcb
                LEFT JOIN `world-koala`.t_cattle_breeding_relation tcbr ON tcbr.batch_no = tcb.batch_no 
            WHERE
                tcb.id = '%s'
              """ % bid
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_user_create_farm_all_user_id(self, email):
        """
        查询当前用户创建农场中的全部人员id
        :param email:
        :return:
        """
        sql = """
                SELECT
                    tfu.farm_id,
                    tfu.user_id 
                FROM
                    `world-koala`.t_farm_user tfu 
                WHERE
                    tfu.farm_id IN (
                SELECT
                    tf.id 
                FROM
                    `world-user`.t_user tu
                    LEFT JOIN `world-koala`.t_farm tf ON tf.creator_id = tu.id 
                WHERE
                    tu.email = '%s' 
                    AND tf.is_delete = 0 
                    ) 
                    AND tfu.is_delete = 0 
                    AND tfu.user_id <> ( SELECT t.id FROM `world-user`.t_user t WHERE t.email = '%s' );
              """ % (email, email)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return
