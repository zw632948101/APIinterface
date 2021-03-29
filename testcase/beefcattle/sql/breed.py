#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/20 14:47
# @Author: wei.zhang
# @File : breed.py
# @Software: PyCharm

from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class BullLibrary(DataBaseOperate):
    def __init__(self):
        super(BullLibrary, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def query_cattle_farm_id(self, userid=None):
        """
        查询牛场信息
        :param userid: 根据创建人查询牛场id
        :return:
        """
        userid = f'AND tcf.creator_id = {userid}' if userid else ''
        sql = f"""
                SELECT tcf.id
                FROM `bf-wagy`.t_service_point tcf
                WHERE tcf.is_delete = 0
                  {userid};
              """
        return self.operate_db(sql=sql)

    def query_cattle_config_variety(self):
        """
        查询全部牛品种
        :return:
        """
        sql = """
            SELECT *
            FROM `bf-breed`.t_config tc
            WHERE tc.type = '10001'
              AND tc.is_delete = 0;
              """
        return self.operate_db(sql=sql)

    def query_bull_info_list(self, cattle_no=None, farmid=None, frozen_no=None, variety=None,
                             pn=1, ps=20):
        """
        查询公牛库列表信息
        :param cattle_no:
        :param farmid:
        :param frozen_no:
        :param variety:
        :param pn:
        :param ps:
        :return:
        """
        cattle_no = f'AND tb.cattle_no LIKE "%{cattle_no}%"' if cattle_no else ''
        farmid = f'AND tb.cattle_farm_id = "{farmid}"' if farmid else ''
        frozen_no = f'AND tb.frozen_semen_no LIKE "%{frozen_no}%"' if frozen_no else ''
        variety = f'AND tb.variety = "{variety}"' if variety else ''
        pn = ps * pn - ps
        ps = pn + ps - 1
        sql = f"""
            SELECT tb.variety,
                   tb.id,
                   tb.sex_control_status AS sexControlStatus,
                   tb.frozen_semen_no    AS frozenSemenNo,
                   tb.mother_no          AS motherNo,
                   tb.father_no          AS fatherNo,
                   tb.cattle_no          AS cattleNo,
                   tb.cattle_farm_id     AS cattleFarmId,
                   tb.remark,
                   tc.name AS varietyDesc
            FROM `bf-breed`.t_bull tb
                     LEFT JOIN `bf-breed`.t_config tc ON tc.code = tb.variety AND tc.type = '10001'
            WHERE tb.is_delete = 0
            {cattle_no} {farmid} {frozen_no} {variety}
            ORDER BY tb.id ASC
            LIMIT {pn},{ps}; 
              """
        return self.operate_db(sql=sql)


class CowshedSql(DataBaseOperate):
    """
    牛舍模块查询
    """

    def __init__(self):
        super(CowshedSql, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def query_cowshed_list_info(self, farm_id=None, cowshed_no=None, cowshed_name=None, epc_no=None,
                                ps=20, pn=1):
        """
        根据农场id，查询农场下的牛舍
        :param farm_id: 牛场编号
        :param cowshed_no: 牛舍编号
        :param cowshed_name: 牛舍名称
        :param epc_no:
        :param ps: 条数
        :param pn: 页码
        :return: 牛舍列表
        """
        farm_id = f'AND tc.cattle_farm_id = {farm_id}' if farm_id else ''
        cowshed_no = f'AND tc.cowshed_no LIKE \'%{cowshed_no}%\'' if cowshed_no else ''
        cowshed_name = f'AND tc.cowshed_name LIKE \'%{cowshed_name}%\'' if cowshed_name else ''
        epc_no = f'AND tc.epc_no LIKE \'%{epc_no}%\'' if epc_no else ''
        pn = ps * pn - ps
        sql = f"""
            SELECT tc.cattle_farm_id AS cattleFarmId,
                   tc.cowshed_name   AS cowshedName,
                   tc.cowshed_no     AS cowshedNo,
                   tc.id,
                   count(tcf.id)     AS fenceNum,
                   tc.epc_no         AS epcNo,
                   tc.area,
                   tc.remark
            FROM `bf-breed`.t_cowshed tc
                     LEFT JOIN `bf-breed`.t_cattle_fence tcf ON tcf.cowshed_id = tc.id
            WHERE tc.is_delete = 0
              {farm_id} {cowshed_no} {cowshed_name} {epc_no}
            GROUP BY tc.id
            LIMIT {pn},{ps};
              """
        return self.operate_db(sql=sql)


class CattleFence(DataBaseOperate):
    """
    牛栏模块查询
    """

    def __init__(self):
        super(CattleFence, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def query_cattle_fence_list(self, farm_id=None, fence_no=None, fence_name=None, cowshed_id=None,
                                type_=None, area=None, epc_no=None, remark=None, exist_filter=None,
                                pn=1, ps=20):
        """
        根据牛场id查询牛栏信息
        :param farm_id: 牛场id
        :param fence_no: 牛栏编号
        :param fence_name: 牛栏名称
        :param cowshed_id: 牛舍id
        :param type_: 牛栏养殖类型
        :param area: 牛栏面积
        :param epc_no: 牛栏硬件编号
        :param remark: 牛栏备注
        :param exist_filter: 过滤无牛的牛栏
        :param pn: 页码
        :param ps: 条数
        :return: 牛栏列表
        """
        farm_id = f'AND tf.cattle_farm_id = {farm_id}' if farm_id else ''
        cowshed_id = f'AND tf.cowshed_id = {cowshed_id}' if cowshed_id else ''
        type_ = f'AND tf.type = {type_}' if type_ else ''
        area = f'AND tf.area = {area}' if area else ''
        fence_no = f'AND tf.fence_no LIKE \'%{fence_no}%\'' if fence_no else ''
        fence_name = f'AND tf.fence_name LIKE \'%{fence_name}%\'' if fence_name else ''
        epc_no = f'AND tf.epc_no LIKE \'%{epc_no}%\'' if epc_no else ''
        remark = f'AND tf.remark LIKE \'%{remark}%\'' if remark else ''
        exist_filter = 'HAVING COUNT(tca.id) > 0' if exist_filter else ''
        pn = pn * ps - ps
        sql = f"""
            SELECT tf.area,
                   tf.cattle_farm_id                                                AS cattleFarmId,
                   COUNT(tca.id)                                                    AS cattleNum,
                   tf.cowshed_id                                                    AS cowshedId,
                   tc.cowshed_name                                                  AS cowshedName,
                   tf.epc_no                                                        AS epcNo,
                   tf.fence_name                                                    AS fenceName,
                   tf.fence_no                                                      AS fenceNo,
                   tf.id,
                   tf.remark,
                   tf.`type`,
                   (SELECT tcf.name FROM `bf-breed`.t_config tcf 
                    WHERE tcf.code = tf.type AND tcf.type = '10002') AS typeDesc
            FROM `bf-breed`.t_cattle_fence tf
                     LEFT JOIN `bf-breed`.t_cowshed tc ON tc.id = tf.cowshed_id
                     LEFT JOIN `bf-breed`.t_cattle tca ON tca.cattle_fence_id = tf.id 
                                                            AND tca.is_delete = 0
            WHERE tf.is_delete = 0
              {farm_id} {fence_no} {fence_name} {cowshed_id} {type_} {area} {epc_no} {remark}
            GROUP BY tf.id
            {exist_filter}
            ORDER BY tf.id ASC
            LIMIT {pn},{ps};
              """
        return self.operate_db(sql=sql)


class PennStateSeparator(DataBaseOperate):
    """
    滨州筛模块
    """

    def __init__(self):
        super(PennStateSeparator, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def query_penn_state_separator_list(self, farm_id=None, fence_no=None, start_date=None,
                                        end_date=None, ps=20, pn=1):
        """

        :param farm_id:
        :param fence_no:
        :param start_date:
        :param end_date:
        :param ps:
        :param pn:
        :return:
        """
        farm_id = f"AND tp.cattle_farm_id = {farm_id}" if farm_id else ''
        fence_no = f"AND tf.fence_no = {fence_no}" if fence_no else ''
        start_date = f"AND unix_timestamp(tp.make_date) >= {start_date / 1000}" if start_date else ''
        end_date = f"AND unix_timestamp(tp.make_date) <= {end_date / 1000}" if end_date else ''
        pn = 1 if pn > 1 else pn
        pn = ps * pn - ps
        sql = f"""
                SELECT tp.cattle_farm_id                   AS cattleFarmId,
                       tp.dry_matter_ratio                 AS dryMatterRatio,
                       unix_timestamp(tp.edit_time) * 1000 AS editTime,
                       tp.fence_id                         AS fenceId,
                       tf.fence_no                         AS fenceNo,
                       tp.fence_remark                     AS fenceRemark,
                       tp.first_floor_ratio                AS firstFloorRatio,
                       tp.four_floor_ratio                 AS fourFloorRatio,
                       tp.id,
                       unix_timestamp(tp.make_date) * 1000 AS makeDate,
                       tp.second_floor_ratio               AS secondFloorRatio,
                       tp.three_floor_ratio                AS threeFloorRatio,
                       tp.water_ratio                      AS waterRatio
                FROM `bf-breed`.t_penn_state_separator tp
                         LEFT JOIN `bf-breed`.t_cattle_fence tf ON tf.id = tp.fence_id
                WHERE tp.is_delete = 0
                {farm_id} {fence_no} {start_date} {end_date}
                ORDER BY tp.create_time desc, tp.id ASC
                LIMIT {pn},{ps};
              """
        return self.operate_db(sql=sql)


class FaecesSeparator(DataBaseOperate):
    """
    粪便筛模块
    """

    def __init__(self):
        super(FaecesSeparator, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def query_faeces_separator_list_info(self, farm_id=None, fence_id=None, fence_no=None,
                                         up_ratio=None, middle_ratio=None, down_ratio=None,
                                         editor_id=None, start_date=None, end_date=None, ps=20,
                                         pn=1):
        """
        根据传入字段查询粪便筛列表信息
        :param farm_id:牛场编号
        :param fence_id:牛栏编号
        :param fence_no:牛栏编号
        :param up_ratio:上层占比
        :param middle_ratio:中层占比
        :param down_ratio:下层占比
        :param editor_id:编辑人id
        :param start_date:制作开始时间
        :param end_date:制作结束时间
        :param ps:分页条数
        :param pn:分页页码
        :return:粪便筛列表
        """
        farm_id = f'AND tf.cattle_farm_id = {farm_id}' if farm_id else ''
        fence_id = f'AND tf.fence_id = {fence_id}' if fence_id else ''
        fence_no = f'AND tcf.fence_no = \'{fence_no}\'' if fence_no else ''
        up_ratio = f'AND tf.up_floor_ratio = {up_ratio}' if up_ratio else ''
        middle_ratio = f'AND tf.middle_floor_ratio = {middle_ratio}' if middle_ratio else ''
        down_ratio = f'AND tf.down_floor_ratio = {down_ratio}' if down_ratio else ''
        editor_id = f'AND tf.editor_id = {editor_id}' if editor_id else ''
        start_date = f'AND unix_timestamp(tf.make_date) * 1000 >= {start_date}' if start_date else ''
        end_date = f'AND unix_timestamp(tf.make_date) * 1000 <= {end_date}' if end_date else ''
        pn = ps * pn - ps
        sql = f"""
            SELECT tf.cattle_farm_id                   AS cattleFarmId,
                   tf.down_floor_ratio                 AS downFloorRatio,
                   unix_timestamp(tf.edit_time) * 1000 AS editTime,
                   tf.fence_id                         AS fenceId,
                   tcf.fence_no                        AS fenceNo,
                   tf.fence_remark                     AS fenceRemark,
                   tf.id,
                   unix_timestamp(tf.make_date) * 1000 AS makeDate,
                   tf.middle_floor_ratio               AS middleFloorRatio,
                   tf.up_floor_ratio                   AS upFloorRatio
            FROM `bf-breed`.t_faeces_separator tf
                     LEFT JOIN `bf-breed`.t_cattle_fence tcf ON tcf.id = tf.fence_id
            WHERE tf.is_delete = 0
            {farm_id} {fence_no} {fence_id} {up_ratio} {middle_ratio} {down_ratio} {editor_id} {start_date} {end_date}
              ORDER BY tf.id DESC
            LIMIT {pn},{ps};
              """
        return self.operate_db(sql=sql)
