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
                FROM `bf-wagy`.t_cattle_farm tcf
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
