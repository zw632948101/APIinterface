#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2019 2019/12/30 11:16
__author__: wei.zhang
__remark__: 农场管理
"""
from .. import FarmQuery


class FarmManage(FarmQuery):
    def __init__(self):
        super(FarmManage, self).__init__()
        self.level = 'CattleManage'

    def query_farm_attach_buy_email(self, email):
        """
        通过邮箱号查询用户的默认农场的最近上传的资质文件
        :return:
        """
        sql = """SELECT
                    tfu.farm_id,
                    tfa.id
                FROM
                    `world-koala`.t_farm_user tfu
                    LEFT JOIN `world-user`.t_user tu ON tfu.user_id = tu.id 
                    LEFT JOIN `world-koala`.t_farm_attach tfa ON tfu.farm_id = tfa.farm_id
                WHERE
                    tu.email = '%s'
                    AND tfu.is_delete = 0 
                    AND tfu.is_default = 1 
                    AND tfa.is_delete = 0;""" % email
        info = self.operate(self.hostip, 'world-koala', sql)
        return info

    def query_farm_default(self, eamil):
        """
        查詢默認農場
        :param eamil:
        :return:
        """
        sql = "select tf.id,tf.address,tf.name,tf.currency_type " \
              "from `world-koala`.`t_farm` tf " \
              "left join `world-user`.`t_user` tu on tf.farmer_id = tu.id " \
              "where tu.email = '%s' AND tf.is_delete='0';" % eamil
        info = self.operate(self.hostip, 'world-user', sql)
        if info == ():
            return
        return info

    def query_one_farm_info(self, farmid):
        """
        查询单个农场信息
        :param farmid:
        :return:
        """
        sql = """
                SELECT * FROM `world-koala`.t_farm tf WHERE tf.id = '%s';
              """ % farmid
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info[0]
        return

    def query_farm_my_farmer(self, email):
        """
        查询当前用户创建的农场
        :param email:
        :return:
        """
        sql = """
            SELECT
                * 
            FROM
                `world-koala`.t_farm tf
                LEFT JOIN `world-user`.t_user tu ON tf.farmer_id = tu.id 
            WHERE
                tu.email = '%s' 
                AND tf.is_delete = 0
                ORDER BY tf.id DESC;
              """ % email
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_update_farm_data(self, farmid):
        """
        以ID查询农场和农场坐标集
        :param farmid:
        :return:
        """
        sql = """
            SELECT
                * 
            FROM
                `world-koala`.t_farm tf
                LEFT JOIN `world-koala`.t_farm_right tr ON tf.id = tr.farm_id 
            WHERE
                tf.id = '%s'
              """ % farmid
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info[0]
        return

    def query_my_farm_list(self, email):
        """
        查询用户的农场列表
        :param email:
        :return:
        """
        sql = """
            SELECT
                tf.* 
            FROM
                `world-koala`.t_farm tf
                LEFT JOIN `world-koala`.t_farm_user tfu ON tf.id = tfu.farm_id
                LEFT JOIN `world-user`.t_user tu ON tfu.user_id = tu.id 
            WHERE
                tu.email = '%s' 
                AND tf.is_delete = '0' 
                AND tfu.is_delete = '0'
                ORDER BY tfu.is_default DESC,tfu.id DESC
              """ % email
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_default_farm_attach(self, email):
        """
        查询默认农场上传的图片
        :param email:
        :return:
        """
        sql = """
            SELECT
                ta.* 
            FROM
                `world-koala`.t_farm_user tfu
                LEFT JOIN `world-koala`.t_farm_attach ta ON tfu.farm_id = ta.farm_id
                LEFT JOIN `world-user`.t_user tu ON tfu.user_id = tu.id 
            WHERE
                tu.email = '%s' 
                AND tfu.is_default = 1 
                AND tfu.is_delete = 0 
                AND ta.is_delete = 0
              """ % email
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_all_farm_landmark(self, email):
        """
        查询用户加入的农场全部地标
        :param email:
        :return:
        """
        sql = """
            SELECT
                tl.* 
            FROM
                `world-koala`.t_landmark tl
                LEFT JOIN `world-koala`.t_farm_user tfu ON tl.farm_id = tfu.farm_id
                LEFT JOIN `world-user`.t_user tu ON tfu.user_id = tu.id 
            WHERE
                tu.email = '%s' 
                AND tl.is_delete = '0' 
                AND tfu.is_delete = '0'
                AND tfu.is_default = 1 
                GROUP BY tl.id DESC
            """ % email
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_farm_supplies_add_info(self, farmid):
        """
        查询最新一条新增的农场物资
        :param farmid:
        :return:
        """
        sql = """
            SELECT
                * 
            FROM
                `world-koala`.t_farm_supplies ts 
            WHERE
                ts.farm_id = '%s'
                AND ts.is_delete = '0'
                ORDER BY ts.id DESC LIMIT 1;
              """ % farmid
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info[0]
        return

    def query_farm_supplies_add_info_count(self, farmid):
        """
        查询农场物资条数
        :param farmid:
        :return:
        """
        sql = """
            SELECT
                count(1) supplies_num 
            FROM
                `world-koala`.t_farm_supplies ts 
            WHERE
                ts.farm_id = '%s'
                AND ts.is_delete = '0';
              """ % farmid
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info[0]
        return

    def query_farm_supplies_info(self, suppliesId):
        """
        根据物资ID查询物资信息
        :param farmid:
        :return:
        """
        sql = """
             SELECT
                 * 
             FROM
                 `world-koala`.t_farm_supplies ts 
             WHERE
                 ts.id = '%s';
               """ % suppliesId
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info[0]
        return

    def query_farm_supplies_info_list(self, farmid, suppliesType):
        """
        查询最新一条新增的农场物资
        :param farmid:
        :return:
        """
        sql = """
            SELECT
                * 
            FROM
                `world-koala`.t_farm_supplies ts 
            WHERE
                ts.farm_id = '%s' 
                AND ts.supplies_type = '%s'
                AND ts.is_delete = '0' 
                ORDER BY ts.id DESC;
              """ % (farmid, suppliesType)
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_farm_landmark_id(self, landmarkid):
        """
        通过地标id查询地标信息
        :param landmarkid:
        :return:
        """
        sql = """
            SELECT
                tf.currency_type,
                tf.name as farm_name,
                tf.id as farm_id,
                tl.id landmark_id,
                ta.length,
                tl.locations,
                tl.name as landmark_name,
                ta.remark,
                ta.type1,
                ta.type2,
                ta.water_capacity,
                ta.specs,
                tl.is_delete
            FROM
                `world-koala`.t_farm tf
                LEFT JOIN `world-koala`.t_landmark tl ON tf.id = tl.farm_id
                LEFT JOIN `world-koala`.t_fixed_assets ta ON tl.assets_id = ta.id
                WHERE 
                    tl.id = '%s'
              """ % landmarkid
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info[0]
        return

    def query_landmark_info_farmid(self, farmid):
        """
        根据农场id查询农场下全部地标
        :param farmid:
        :return:
        """
        sql = """
        SELECT * FROM `world-koala`.t_landmark tl WHERE tl.farm_id = '%s' AND tl.is_delete = 0
            """ % farmid
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_farm_home_water_resource(self, farmid):
        """
        通过农场id查询农场首页水资源统计数据
        :param farmid:
        :return:
        """
        sql = """
            SELECT
                tc.linear_icon as linearIcon,
                COUNT(tl.id) as num,
                tc.solid_icon as solidIcon,
                tl.type1,
                '水资源' type1Name ,
                tl.type2,
                tc.`value` as type2Name,
                SUM(ta.water_capacity) as waterCapacity
            FROM
                `world-koala`.t_landmark tl
                LEFT JOIN `world-koala`.t_fixed_assets ta ON tl.assets_id = ta.id
                LEFT JOIN `world-koala`.t_config tc ON tl.type2 = tc.`key`
                WHERE
                tl.farm_id = '%s'
                AND tl.type2 in(10180,10200,10240)
                AND tl.is_delete = 0
                AND tc.`code` = '10001'
                GROUP BY tl.type2
              """ % farmid
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_landmark_list_info_transit_farmid(self, farmid, landmarkType=None, type1='10040'):
        """
        通过农场id查询水资源列表
        :param farmid:
        :return:
        """
        if landmarkType:
            landmarkType = 'AND tl.type2 = %s' % landmarkType
        else:
            landmarkType = ''
        sql = """
            SELECT
                UNIX_TIMESTAMP( ta.build_date )*1000 AS buildDate,
                IFNULL(ta.build_price,0) AS buildPrice,
                UNIX_TIMESTAMP( ta.create_time )*1000 AS createTime,
                tl.creator_id AS creatorId,
                tf.currency_type AS currencyType,
                tl.farm_id AS farmId,
                tl.id AS id,
                tc.linear_icon AS linearIcon,
                tl.locations,
                tl.`name`,
                IFNULL(ta.remark,'') AS remark,
                tc.solid_icon AS solidIcon,
                ta.specs,
                tl.type1,
                CASE WHEN tl.type2 IN('10220','10170','10160') THEN 2 ELSE 1 END as shapeType,
                CASE tl.type1 WHEN 10040 THEN '水资源' WHEN 10050 THEN '道路' WHEN 10030 THEN '建筑' END type1Name,
                tl.type2,
                tc.`value` AS type2Name,
                ta.water_capacity AS waterCapacity 
            FROM
                `world-koala`.t_landmark tl
                LEFT JOIN `world-koala`.t_fixed_assets ta ON tl.assets_id = ta.id
                LEFT JOIN `world-koala`.t_config tc ON tl.type2 = tc.`key`
                LEFT JOIN `world-koala`.t_farm tf ON tl.farm_id = tf.id 
            WHERE
                tl.farm_id = '%s' 
                %s
                AND tl.is_delete = 0
                AND tl.type1 = '%s'
                GROUP BY tl.id
            ORDER BY
                tl.id DESC 
                LIMIT 0,
                20;
              """ % (farmid, landmarkType, type1)
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_landmark_png_info(self, farm_id):
        """
        通过农场id查询地标图片信息
        :param farm_id:
        :return:
        """
        sql = """
            SELECT
                UNIX_TIMESTAMP(tc.create_time)*1000 as createTime,
                tl.id ,
                tc.file_type as fileType,
                tc.sort_no as sortNo,
                tc.url 
            FROM
                `world-koala`.t_fixed_assets ta
                LEFT JOIN `world-koala`.t_landmark tl ON ta.id = tl.assets_id
                LEFT JOIN `world-koala`.t_common_attach tc ON tc.bid = ta.id 
            WHERE
                ta.farm_id = '%s' 
                AND ta.is_delete = 0 
                AND tl.is_delete = 0 
                AND tc.is_delete = 0
              """ % farm_id
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return
