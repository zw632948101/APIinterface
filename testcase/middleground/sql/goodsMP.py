#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/10/27 18:22
# @Author: wei.zhang
# @File : goodsMP.py
# @Software: PyCharm

from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class mp_label(DataBaseOperate):
    def __init__(self):
        super(mp_label, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def query_mp_label_info(self, label_name, label_type):
        """
        查询商品标签
        :param label_name:
        :param label_type:
        :return:
        """
        sql = "SELECT tl.id,tl.name,tl.type,tl.creator_id FROM `mp-product`.t_label tl WHERE tl.name = '%s' AND  tl.type = '%s';" % (label_name, label_type)
        return self.operate_db(sql=sql)
    def query_mp_section_info(self,section_prefix=None,section_bizId=None):
        """
        查询商品属性
        ：param section_prefix
        ：param section_bizId
        ：param section_num
        """
        if section_prefix and section_bizId:
            sql = "select * from `mp-product`.t_section_no where biz_id={0} and prefix='{1}';"\
                .format(section_bizId,section_prefix)
        else:
            sql = "select * from `mp-product`.t_section_no order by id desc limit 1;"
        return self.operate_db(sql=sql)


class MPcategory(DataBaseOperate):
    """
    商品类目使用SQL
    """

    def __init__(self):
        super(MPcategory, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)


if __name__ == '__main__':
    sql = mp_label()
    a = sql.query_mp_section_info("T",1)
    print(a)