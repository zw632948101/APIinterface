from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.log import log
from utils.environmentConfiguration import config
import random
import os
import datetime

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class ConfigProductSql(object):
    db = DataBaseOperate()

    def query_user_id(self):
        """
        随机查询user_id
        :return:
        """
        sql = """SELECT
                    bf.user_id 
                FROM
                    `fc-bee`.t_bee_friend bf 
                WHERE
                    is_delete = 0 
                    AND user_id IS NOT NULL LIMIT 0,100;"""
        info = self.db.operate(host_ip, sql)
        i = random.randint(0, len(info))
        info = info[i]
        return info

    def query_variety(self, parent_key):
        """
        查询种类下对应的品种
        :param parent_key: 种类key
        :return:
        """
        sql = """SELECT
                    * 
                FROM
                    `fc-bee`.t_config c 
                WHERE
                    c.is_delete = 0 
                    AND c.`code` = 10014 
                    AND c.parent_key = '%s';""" % parent_key
        info = self.db.operate(host_ip, sql)
        i = random.randint(0, len(info))
        info = info[i]
        return info

    def query_province(self):
        """
        查询系统配置的省份编码
        :return:
        """
        sql = """SELECT * FROM `fc-bee`.t_region r WHERE r.is_delete= 0 AND r.`level` = 0;"""
        info = self.db.operate(host_ip, sql)
        i = random.randint(0, len(info))
        info = info[i]
        return info

    def query_city(self, province):
        """
        查询系统配置的市编码
        :return:
        """
        sql = """SELECT * FROM `fc-bee`.t_region r WHERE r.is_delete= 0 AND r.`level` = 1 AND parent_id = '%s';""" \
              % province
        info = self.db.operate(host_ip, sql)
        i = random.randint(0, len(info))
        info = info[i]
        return info

    def query_county(self, city):
        """
        查询系统配置的区/县编码
        :return:
        """
        sql = """SELECT * FROM `fc-bee`.t_region r WHERE r.is_delete= 0 AND r.`level` = 2 AND parent_id = '%s';""" \
              % city
        info = self.db.operate(host_ip, sql)
        if len(info) == 0:
            return None
        else:
            i = random.randint(0, len(info))
            info = info[i]
            return info

    def query_product_seller_id(self):
        """
        查询含有未收购的商品的用户id
        :return:
        """
        sql = """SELECT DISTINCT(p.seller_id) FROM `fc-trade`.t_product p WHERE p.is_delete = 0 AND p.`status` = 1;"""
        info = self.db.operate(host_ip, sql)
        if len(info) == 0:
            return None
        else:
            i = random.randint(0, len(info))
            info = info[i]
            return info

    def query_product_info_by_seller_id(self, seller_id):
        """
        通过蜂友id查询商品信息
        :return:
        """
        sql = """SELECT
                    p.*,
                    c.`value`,
                    c.`key`
                FROM `fc-trade`.t_product p LEFT JOIN `fc-bee`.t_config c ON p.variety = c.`key` 
                WHERE p.is_delete = 0 AND p.seller_id = '%s' AND p.`status` = 1;""" % seller_id
        info = self.db.operate(host_ip, sql)
        if len(info) == 0:
            return None
        else:
            i = random.randint(0, len(info))
            info = info[i]
            return info