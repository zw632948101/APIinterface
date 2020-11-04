#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/11/3 15:59
# @Author: wei.zhang
# @File : appletWX.py
# @Software: PyCharm

from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class wx_applet_evaluate(DataBaseOperate):
    """
    小程序评价模块
    """

    def __init__(self):
        super(wx_applet_evaluate, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)


class wx_applet_shoppingCart(DataBaseOperate):
    """
    小程序购物车模块
    """

    def __init__(self):
        super(wx_applet_shoppingCart, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def query_shop_all_sku(self):
        """
        查询全部的店铺id和商品code
        :return:
        """
        sql = """
            SELECT ts.id, tu.code
            FROM `wx-mall`.t_shop ts
                     LEFT JOIN `wx-product`.t_sku tu ON ts.id = tu.shop_id
                     LEFT JOIN `wx-product`.t_inventory ti ON ti.sku_code = tu.code
            WHERE ts.is_delete = 0
              AND tu.is_delete = 0
              AND tu.status = 1
              AND ti.quantity >= 1
            LIMIT 20;"""
        return self.operate_db(sql=sql)

    def query_add_cart_goods_num(self, userid, shopid, code):
        """
        查询用户添加的商品数据
        :param userid: 用户id
        :param shopid: 店铺id
        :param code: 商品code
        :return:
        """
        sql = """
            SELECT *
            FROM `wx-mall`.t_cart tc
            WHERE tc.buyer_id = '{userid}'
              AND tc.shop_id = '{shopid}'
              AND tc.sku_no = '{code}'
              AND tc.is_delete = 0;
              """.format(userid=userid, shopid=shopid, code=code)
        dbinfo = self.operate_db(sql=sql)
        if dbinfo:
            return dbinfo[0]
        return

    def query_cart_list_product(self, userid):
        """
        跟进用户id查询购物车商品列表
        :param userid:
        :return:
        """
        sql = """
                SELECT tc.amount,
                       tc.id            AS cartId,
                       tc.sku_no        AS code,
                       tc.shop_id       AS shopId,
                       ts.alias,
                       ts.name,
                       ts.status,
                       ts.sale_attr     AS saleAttr,
                       ts.market_price  AS marketPrice,
                       ts.basic_attr    AS basicAttr,
                       ts.snapshot_code AS snapshotCode,
                       tm.url           AS thumbnailUrl
                FROM `wx-mall`.t_cart tc
                         LEFT JOIN `wx-product`.t_sku ts ON tc.sku_no = ts.code
                         LEFT JOIN `wx-product`.t_sku_media tm ON tc.sku_no = tm.sku_code AND tm.type = 1
                WHERE tc.buyer_id = '{userid}' AND tc.is_delete = 0;
              """.format(userid=userid)
        return self.operate_db(sql=sql)

    def query_cart_list_shopinfo(self, shopid):
        """
        跟进店铺id查询商店信息
        :param shopid:
        :return:
        """
        if len(shopid) > 1:
            shopid = tuple(shopid)
        else:
            shopid = '(%s)' % shopid[0]
        sql = """
            SELECT ts.type, ts.certify_status AS certifyStatus, ts.id, ts.name, ts.seller_id AS sellerId, ts.shop_no AS shopNo, ts.status
            FROM `wx-mall`.t_shop ts
            WHERE ts.id IN {shopid};
              """.format(shopid=shopid)
        return self.operate_db(sql=sql)
