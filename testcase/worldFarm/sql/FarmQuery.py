#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Heng Xin'
__date__ = '2019/7/13'
"""
from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config

class FarmQuery(DataBaseOperate):
    def __init__(self):
        super(FarmQuery, self).__init__()
        self.hostip = config.get('database').get(config.get('run')).get('host_ip')

    def query_cattle_config(self):
        """
        查询牲畜类型配置
        :return:
        """
        sql = "SELECT `code`,`key`,`value` FROM `world-koala`.t_config WHERE `code` in('10004','10012','10011','10003','10002') AND is_delete = '0';"
        info = self.operate(self.hostip,  sql)
        return info

    def query_farm_and_region(self, email):
        """
        查询用户加入的农场和围栏
        :param email:
        :return:
        """
        sql = """
                SELECT
                    tu.id,
                    tf.id farm_id,
                    tf.`name` farm_name,
                    tfr.id region_id,
                    tfr.`name` region_name
                FROM
                    `world-koala`.t_farm_user tfu
                    LEFT JOIN `world-user`.t_user tu ON tfu.user_id = tu.id
                    LEFT JOIN `world-koala`.t_farm_region tfr ON tfu.farm_id = tfr.farm_id
                    LEFT JOIN `world-koala`.t_farm tf ON tfu.farm_id =tf.id
                WHERE
                    1 = 1
                    AND tu.email = '%s'
                    AND tf.is_delete = '0'
                    AND tfr.is_delete = '0'
                    AND tfu.is_delete = '0'
                ORDER BY
                    tf.create_time DESC;
              """ % email
        # info = self.operate('120.79.59.233',  sql)
        info = self.operate(self.hostip,  sql)
        return info

    def query_device_eui(self):
        """
        查询当天新增的设备编号
        :return:
        """
        sql = """
                SELECT
                    td.device_eui 
                FROM
                    `agr-mgr`.t_device td
                    LEFT JOIN `world-shark`.t_sync_device_bind ts ON td.device_eui = ts.device_eui 
                WHERE
                    td.is_delete = '0' 
                    AND ts.device_eui IS NULL
                ORDER BY
                    td.create_time DESC LIMIT 10;
                """
        # info = self.operate('120.79.59.233',  sql)
        info = self.operate(self.hostip,  sql)
        return info

    def query_farm_region_locations(self, email):
        """
        查询用户最新添加的一个农场
        :param email:
        :return:
        """
        sql = """
                SELECT
                    tu.username,
                    tf.`name`,
                    tfr.locations
                FROM
                    `world-koala`.t_farm tf
                    LEFT JOIN `world-user`.t_user tu ON tf.farmer_id = tu.id 
                    LEFT JOIN `world-koala`.t_farm_region tfr ON tf.id = tfr.farm_id
                WHERE
                    tu.email = '%s' 
                    AND tf.is_delete = '0'
                    ORDER BY tf.create_time DESC
                    LIMIT 1;
                """ % email
        # info = self.operate('120.79.59.233',  sql)
        info = self.operate(self.hostip,  sql)
        return info[0]

    def query_device_eui_one(self, comparison):
        """
        查询device_eui排序最后一个返回
        :param comparison:
        :return:
        """
        sql = """
                SELECT
                    td.device_eui 
                FROM
                    `agr-mgr`.t_device td
                    LEFT JOIN `world-shark`.t_sync_device_bind ts ON td.device_eui = ts.device_eui 
                WHERE
                    td.is_delete = '0' 
                    AND td.device_eui NOT REGEXP '[a-z]'
                    AND LENGTH(td.device_eui) %s 10
                    AND td.platform_id = '1'
                GROUP BY td.device_eui
                ORDER BY td.device_eui DESC
                LIMIT 1;
                """ % comparison
        # info = self.operate('120.79.59.233',  sql)
        info = self.operate(self.hostip,  sql)
        return info[0]

    def query_cattle_info_buy_eui(self, device_Id):
        """
        通过设备ID查询牲畜信息
        :return:
        """
        sql = """SELECT id FROM t_cattle WHERE device_id="s%";""" % str(device_Id)
        # info = self.operate('120.79.59.233',  sql)
        info = self.operate(self.hostip,  sql)
        return info

    def query_cattle_bind_id(self, email):
        """
        查询用户的所有农场已绑定设备的牲畜
        :param email: 用户邮箱
        :return:
        """
        sql = """SELECT
                tc.id,
                tc.farm_id,
                tc.device_id
            FROM
                `world-koala`.t_farm_user tfu
                LEFT JOIN `world-user`.t_user tu ON tu.id = tfu.user_id
                LEFT JOIN `world-koala`.t_farm_region tfr ON tfu.farm_id = tfr.farm_id
                LEFT JOIN `world-koala`.t_cattle tc ON tfr.id = tc.region_id 
            WHERE
                tfu.is_delete = 0 
                AND tfr.is_delete = 0
                AND tc.is_delete = 0
                AND tc.device_id is not NULL
                AND tc.device_id != ''
                AND tu.email = '%s';""" % email
        # info = self.operate('120.79.59.233',  sql)
        info = self.operate(self.hostip,  sql)
        return info

    def query_cattle_id(self, email):
        """
        查询用户的所有农场的牲畜
        :param email: 用户邮箱
        :return:
        """
        sql = """SELECT
                tc.id
            FROM
                `world-koala`.t_farm_user tfu
                LEFT JOIN `world-user`.t_user tu ON tu.id = tfu.user_id
                LEFT JOIN `world-koala`.t_farm_region tfr ON tfu.farm_id = tfr.farm_id
                LEFT JOIN `world-koala`.t_cattle tc ON tfr.id = tc.region_id 
            WHERE
                tfu.is_delete = 0 
                AND tfr.is_delete = 0
                AND tc.is_delete = 0
                AND tu.email = '%s';""" % email
        # info = self.operate('120.79.59.233',  sql)
        info = self.operate(self.hostip,  sql)
        return info

    def query_farm_region_list(self, farmid, types=None, isNeedFilter=None, isNeedNoPaddock=None):
        """

        :param farmid: 农场ID
        :param types: 围栏/区域
        :param isNeedFilter:  1过滤没有牲畜的围栏
        :param isNeedStoreNum: 1统计围栏内牲畜数量
        :param isNeedNoPaddock: 1统计没有围栏的牲畜数据
        :return:
        """

        if isinstance(types, tuple):
            types = "AND tfr.region_type in %s" % types
        elif types is not None:
            types = "AND tfr.region_type = '%s'" % types
        else:
            types = ""
        # 过滤围栏并且统计围栏下牲畜数量还统计无围栏的牲畜数量
        sql = """
                SELECT
                    tc.farm_id,
                    tc.region_id,
                    tfr.region_type,
                    IFNULL(tfr.name,'未绑定围栏') as `name`,
                    tfr.perimeter,
                    tfr.area,
                    tfr.color_type,
                    tfr.soil_type,
                    tfr.soil_ph,
                    IFNULL(tfr.pasture_type,"") as pasture_type,
                    tfr.remark,
                    tfr.locations,
                    count(tc.id) as storedNum
                FROM
                    `world-koala`.t_cattle tc
                    LEFT JOIN `world-koala`.t_farm_region tfr ON  tc.region_id = tfr.id 
                WHERE
                    tc.farm_id = '%s' 
                    AND (tfr.is_delete = 0 OR tfr.is_delete IS NULL)
                    AND tc.is_delete = 0
                    %s
                    GROUP BY tc.region_id
                    ORDER BY tc.region_id DESC
              """ % (farmid, types)
        # 过滤围栏并且不统计无围栏的牲畜数量
        if isNeedNoPaddock != 1:
            sql = sql.replace("AND (tfr.is_delete = 0 OR tfr.is_delete IS NULL)", "AND tfr.is_delete = 0")
        # 不过滤无牲畜的围栏，统计围栏下牲畜，不统计无围栏的牲畜
        if isNeedFilter != 1:
            sql = sql.replace("`world-koala`.t_cattle tc", "`world-koala`.t_farm_region tfr")
            sql = sql.replace("`world-koala`.t_farm_region tfr ON  tc.region_id = tfr.id",
                              "`world-koala`.t_cattle tc ON tc.region_id = tfr.id")
            sql = sql.replace("tc.farm_id =", "tfr.farm_id =")
            if isNeedNoPaddock == 1:
                sql = sql.replace("AND (tfr.is_delete = 0 OR tfr.is_delete IS NULL)",
                                  "AND ( tc.is_delete = 0 OR tc.id IS NULL OR tc.region_id IS NULL)")
            else:
                sql = sql.replace("AND tfr.is_delete = 0",
                                  "AND ( tc.is_delete = 0 OR tc.id IS NULL OR tc.region_id IS NULL)")
            sql = sql.replace("AND tc.is_delete = 0", "AND tfr.is_delete = 0")
            sql = sql.replace("GROUP BY tc.region_id", "GROUP BY tfr.id")
            sql = sql.replace("ORDER BY tc.region_id DESC", "ORDER BY tfr.id DESC")
            sql = sql.replace("tc.farm_id,", "tfr.farm_id,")
            sql = sql.replace("tc.region_id,", "tfr.id AS region_id,")
            # 不过滤围栏并且统计无围栏的牲畜
        info = self.operate(self.hostip,  sql)
        if isNeedNoPaddock == 1 and (isNeedFilter != 1 or isNeedFilter == 1):
            nocattle = self.query_farm_region_no_cattle(farmid)
            if info:
                info.append(nocattle[0])
            else:
                info = nocattle
        if info:
            return info
        return

    def query_farm_region_no_cattle(self, farmid):
        sql = """
                 SELECT
                     tc.farm_id,
                     IFNULL(tc.region_id,'未绑定围栏') as `name`,
                     count(tc.id) as storedNum
                 FROM
                     `world-koala`.t_cattle tc
                 WHERE
                     tc.farm_id = '%s' 
                 AND tc.is_delete = 0
                 AND tc.region_id IS NULL;
               """ % farmid
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_cattle_device_rui_type(self, farmid, device_type):
        """
        根据农场id和设备类型查询设备id
        :param farmid:
        :param device_type:
        :return:
        """
        sql = """
                SELECT * FROM `world-koala`.t_cattle tc WHERE tc.farm_id = %s AND tc.is_delete = 0 AND tc.device_type = %s;
              """ % (farmid, device_type)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_default_farm(self, email):
        """
        查询默认农场
        :return:
        """
        sql = """SELECT
                        tfu.farm_id,
                        tfu.user_id,
                        tfu.is_default,
    	                tfr.locations,
    	                tfre.`name` region_name,
    	                tfre.id region_id,
    	                tfr.locations,
	                    tfre.locations as region_locations
                    FROM
                        `world-user`.t_user tu
                        LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                        LEFT JOIN `world-koala`.t_farm_right tfr ON tfu.farm_id = tfr.farm_id
                        LEFT JOIN `world-koala`.t_farm_region tfre ON tfu.farm_id = tfre.farm_id
                    WHERE
                        tu.email = '%s' 
                        AND tu.is_delete = 0 
                        AND tfu.is_delete = 0 
                        AND tfr.is_delete = 0
                        AND tfre.is_delete = 0
                        AND (tfre.is_delete = 0 OR tfre.id IS NULL)
                        AND tfu.is_default = 1
                        GROUP BY tfre.id;""" % email
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_only_default_farm_id(self, email):
        """
        只查询默认农场id信息
        :return:
        """
        sql = """SELECT
                        tfu.farm_id,
                        tfu.user_id,
                        tfu.is_default
                    FROM
                        `world-user`.t_user tu
                        LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                    WHERE
                        tu.email = '%s' 
                        AND tu.is_delete = 0 
                        AND tfu.is_delete = 0 
                        AND tfu.is_default = 1;""" % email
        info = self.operate(self.hostip, sql)
        if info:
            return info
        return

    def query_farm_all_user_id(self, farmid):
        """
        根据农场id查询农场员工id
        :param farmid:
        :return:
        """
        sql = """
            SELECT
                * 
            FROM
                `world-koala`.t_farm_user tfu 
                LEFT JOIN `world-user`.t_user tu ON tu.id = tfu.user_id
            WHERE
                tfu.farm_id = '%s' 
                AND tfu.is_delete = 0
                AND tu.is_delete = 0
              """ % farmid
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_livestock_by_farm_id(self, farmid):
        """
        根据农场id查询牲畜
        :param farmid:
        :return:
        """
        sql = """
            SELECT
                * 
            FROM
                `world-koala`.t_cattle tc 
            WHERE
                tc.farm_id = '%s' 
                AND tc.is_delete = 0;
              """ % farmid
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_cattle_drug_use_info(self, cattleIds, usedate):
        """
        根据牲畜id查询药物使用记录
        :param cattleIds:
        :param usedate:
        :return:
        """
        if isinstance(cattleIds, list):
            cattleIds = tuple(cattleIds)
            cattleIds = "in%s" % str(cattleIds)
        else:
            cattleIds = "= %s" % cattleIds
        sql = """
            SELECT
                * 
            FROM
                `world-koala`.t_cattle_drug_use tcdu 
            WHERE
                tcdu.cattle_id %s
                AND tcdu.is_delete = 0 
                AND UNIX_TIMESTAMP( tcdu.use_date ) = %s
              """ % (cattleIds, usedate / 1000)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_default_farn_cattle_drug(self, farmid):
        """
        查询默认农场的牲畜药物使用记录
        :param farmid:
        :return:
        """
        sql = """
            SELECT
                tcdu.* 
            FROM
                `world-koala`.t_cattle tc
                LEFT JOIN `world-koala`.t_cattle_drug_use tcdu ON tc.id = tcdu.cattle_id 
            WHERE
                tc.farm_id = %s 
                AND tcdu.is_delete = 0
              """ % farmid
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_farm_raise_id(self, farmid, limit=None):
        """
        根据农场id查询饲养记录
        :param farmid:
        :return:
        """
        if limit:
            limit = 'ORDER BY tr.id DESC LIMIT %s' % limit

        else:
            limit = ''
        sql = """
            SELECT * FROM `world-koala`.t_farm_raise tr WHERE tr.farm_id = '%s' AND tr.is_delete = 0 %s
              """ % (farmid, limit)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_farm_raise(self, raiseid):
        """
        根据饲养记录id查询饲养记录
        :param raiseid:
        :return:
        """
        sql = """
            SELECT * FROM `world-koala`.t_farm_raise tr WHERE tr.id = '%s'
              """ % raiseid
        info = self.operate(self.hostip,  sql)
        if info:
            return info[0]
        return

    def query_farm_raise_feeding_date(self, feedingDate):
        """
        根据饲养时间查询
        :param feedingDate:
        :return:
        """

        sql = """
            SELECT
                tr.remark,
                tr.id,
                UNIX_TIMESTAMP(tr.feeding_date) as feeding_date,
                tr.region_id,
                tr.farm_id
            FROM
                `world-koala`.t_farm_raise tr
            WHERE
                UNIX_TIMESTAMP(tr.feeding_date) = '%s'
              """ % feedingDate
        info = self.operate(self.hostip,  sql)
        if info:
            return info[0]
        return

    def query_farm_raise_detail(self, raiseid, feedTypeDesc=None):
        """
        根据农场id和饲养时间查询饲养记录
        :param farmid:
        :param feedingDate:
        :return:
        """
        if feedTypeDesc:
            feedTypeDesc = "CASE td.feed_type WHEN 1 THEN '青饲料' WHEN 2 THEN '粗饲料' WHEN 3 THEN '青贮饲料' WHEN 4 THEN '精饲料' WHEN 5 THEN '矿物质饲料' WHEN 6 THEN '维生素饲料' WHEN 7 THEN '添加剂饲料' END feedTypeDesc,"
            orderby = "ORDER BY td.id DESC"
        else:
            feedTypeDesc = ''
            orderby = ''
        sql = """
            SELECT
                td.feed_type as feedType,
                %s
                td.type,
                td.feeding_amount as feedingAmount
            FROM
                `world-koala`.t_farm_raise_detail td
            WHERE
                td.raise_id = '%s'
                AND td.is_delete = 0
                %s
              """ % (feedTypeDesc, raiseid, orderby)
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return

    def query_device_eui_id(self):
        """
        查询未绑定的设备编号
        :return:
        """
        sql = """  SELECT
                         td.device_eui,
                         td.product_type
                     FROM
                         `agr-ant`.t_device td 
                         LEFT JOIN `world-koala`.t_cattle tc ON td.device_eui = tc.device_id
                         LEFT JOIN `world-shark`.t_device_position tp ON td.device_eui = tp.device_eui
                         LEFT JOIN (SELECT tb.device_eui FROM `world-shark`.t_sync_device_bind tb WHERE tb.is_delete = 0 ) tb1 ON td.device_eui = tb1.device_eui
                     WHERE
                         td.is_delete = '0'
                         AND tp.farm_id IS NULL
                         AND tc.id IS NULL
                         AND td.device_eui NOT IN('12010503000000')
                         AND td.product_type = '耳标/LoRa耳标' 
                         AND tb1.device_eui IS NULL
                         ORDER BY td.id DESC
                         LIMIT 10;"""
        info = self.operate(self.hostip,  sql)
        if info:
            return info
        return


if __name__ == '__main__':
    fq = FarmQuery()
    # user_info = fq.query_default_farm('632948101@qq.com')
    fq.query_cattle_config()
    # fq.query_default_farm()
