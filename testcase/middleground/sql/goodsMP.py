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

    def query_mp_section_info(self, section_prefix=None, section_bizId=None):
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
    商品类目使用SQL 是
    """

    def __init__(self):
        super(MPcategory, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def query_category_add_info(self, bizid='', name='', isSale='', remark='', pcode=None):
        """
        查询新建的商品类目
        :param bizid:
        :param name:
        :param isSale:
        :param remark:
        :param pcode:
        :return:
        """
        pcode = '' if pcode is None else "AND tc.pcode = " + pcode
        sql = """
            SELECT *
            FROM `mp-product`.t_product_category tc
            WHERE tc.name = '%s'
              AND tc.is_sale = '%s'
              AND tc.biz_id = '%s'
              AND tc.remark = '%s'
              %s;
              """ % (name, isSale, bizid, remark, pcode)
        return self.operate_db(sql=sql)

    def query_category_edit_info(self, code, isSale):
        """
        编辑商品类目查询
        :param code:
        :param isSale:
        :return:
        """
        sql = """
            SELECT *
            FROM `mp-product`.t_product_category tc
            WHERE tc.is_sale = '%s'
              AND tc.code = '%s';
              """ % (isSale, code)
        return self.operate_db(sql=sql)

    def query_category_status_info(self, id_):
        """
        编辑商品类目查询
        :param code:
        :param isSale:
        :return:
        """
        sql = """
            SELECT *
            FROM `mp-product`.t_product_category tc
            WHERE tc.id = '%s';
              """ % (id_)
        return self.operate_db(sql=sql)

    def query_category_page_list(self, pn=1, ps=20):
        """
        分页查询类目列表
        :param pn:
        :param ps:
        :return:
        """
        if pn >= 1:
            ps1 = pn * ps
            pn = ps1 - ps
            ps = ps1

        sql = """
            SELECT tc.code AS code,
                   tc.name ,
                   tc.status AS status,
                   tc.id
            FROM `mp-product`.t_product_category tc
            ORDER BY tc.id DESC
            LIMIT %s,%s;
              """ % (pn, ps)
        return self.operate_db(sql=sql)



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