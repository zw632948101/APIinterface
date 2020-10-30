#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/10/27 18:22
# @Author: wei.zhang
# @File : goodsMP.py
# @Software: PyCharm

from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config
import re

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
    def query_mp_section_info(self,id=None,all=None,pn=None,ps=None,lastOne=None):
        """
        查询商品属性:
        """
        if id:
            sql = "select * from `mp-product`.t_section_no where id={0};".format(id)
        elif lastOne:
            sql = "select * from `mp-product`.t_section_no order by id desc limit 1;"
        elif all:
            sql = "select * from `mp-product`.t_section_no;"
        elif pn == "" or pn == 0 or pn == " ":
            sql = "select * from `mp-product`.t_section_no order by id desc limit 0,{0};".format(ps)
        elif ps == "" or ps == 0 or ps == " ":
            sql = "select * from `mp-product`.t_section_no order by id desc limit {},20;".format(pn)
        elif pn and ps:
            sql = "select * from `mp-product`.t_section_no order by id desc limit {0},{1};".format((pn - 1) * ps, ps)
        elif not pn and not ps:
            sql = "select * from `mp-product`.t_section_no order by id desc limit 1,20;"
        return self.operate_db(sql=sql)
    def query_mp_brand_info(self,all=None,enable=None,pn=None,ps=None):
        """
        查询品牌:
        """
        if all:
            sql = "select * from `mp-product`.t_brand order by id desc;"
        elif enable:
            sql = "select * from `mp-product`.t_brand where status = 1 order by id desc;"
        elif pn == "" or pn == 0 or pn == " ":
            sql = "select * from `mp-product`.t_brand order by id desc limit 0,{0};".format(ps)
        elif ps == "" or ps == 0 or ps == " ":
            sql = "select * from `mp-product`.t_brand order by id desc limit {},20;".format(pn)
        elif pn and ps:
            sql = "select * from `mp-product`.t_brand order by id desc limit {0},{1};".format((pn - 1) * ps, ps)
        elif not pn and not ps:
            sql = "select * from `mp-product`.t_brand order by id desc limit 1,20;"
        else:
            sql = "select * from `mp-product`.t_brand order by id desc limit 1;"
        return self.operate_db(sql=sql)


class MPcategory(DataBaseOperate):
    """
    商品类目使用SQL 是
    """

    def __init__(self):
        super(MPcategory, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)



if __name__ == '__main__':
    sql = mp_label()
    a = sql.query_mp_brand_info(all=1)
    print(a)
    # b = [{'id': 95, 'name': '追花族-蜂蜜', 'prefix': 'a'}]
    #
    #
    # c = [{'id': 95, 'biz_id': 1, 'name': '追花族-蜂蜜', 'prefix': 'a', 'start_serial': 6, 'end_serial': 6, 'serial': 6, 'creator_id': 694, 'create_time': '2020-10-29 11:36:40', 'editor_id': 694, 'edit_time': '2020-10-29 14:38:34', 'is_delete': 0},
    #      {'id': 94, 'biz_id': 1, 'name': '追花族-蜂蜜', 'prefix': ' ', 'start_serial': 86, 'end_serial': 150, 'serial': 88, 'creator_id': 694, 'create_time': '2020-10-29 10:42:59', 'editor_id': 694, 'edit_time': '2020-10-29 11:27:29', 'is_delete': 0}]
    #
    #
    # for l in c[0].items():
    #     if b[0].items() not in l:
    #         raise AssertionError