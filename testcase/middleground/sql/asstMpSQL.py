#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/11/7 18:02
# @Author: wei.zhang
# @File : asstMpSQL.py
# @Software: PyCharm

from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config

host_ip = config.get('database').get(config.get('run')).get('host_ip')


class codeBaseSQL(DataBaseOperate):
    def __init__(self):
        super(codeBaseSQL, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)


class productSQL(DataBaseOperate):
    def __init__(self):
        super(productSQL, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def query_product_info(self):
        """
        查询全部的资产产品信息
        :return:
        """
        sql = """
                SELECT * FROM `mp-asset`.t_product tp WHERE tp.is_delete = 0;
              """
        return self.operate_db(sql=sql)

    def query_product_type_info(self, pid):
        """
        查询资产类型属性
        :return:
        """
        sql = """
            SELECT ta.attr_name   AS attrName,
               ta.product_id  AS productId,
               ta.type,
               if(ta.unit IS NULL, '', ta.unit)            AS unit,
               unix_timestamp(ta.create_time) * 1000 AS createTime,
               unix_timestamp(ta.edit_time) * 1000 AS editTime,
               ta.id,
               ta.is_delete   AS isDelete,
               ''             AS orderField,
               ''             AS orderFieldType
            FROM `mp-asset`.t_attribute_dict ta
            WHERE ta.is_delete = 0
              AND ta.product_id = {pid}
            ORDER BY ta.id DESC;
              """.format(pid=pid)
        return self.operate_db(sql=sql)

    def query_product_list_page(self, typeid=None, name=None, code=None, pn=None, ps=None):
        """
        查询资产产品列表
        :param typeid:
        :param name:
        :param code:
        :param pn:
        :param ps:
        :return:
        """
        typeid = "AND tp.type_id = '%s'" % typeid if typeid is not None else ''
        name = "AND tp.name = '%s'" % name if name is not None else ''
        code = "AND tp.code = '%s'" % code if code is not None else ''
        if pn is not None and ps is not None:
            p = int(ps)
            ps = int(ps) * int(pn)
            pn = ps - p
            limit = 'LIMIT %s,%s' % (pn, ps)
        else:
            limit = ''
        sql = """
            SELECT tp.id,
                   tp.type_id                                                                                                                            AS typeId,
                   tt.name                                                                                                                               AS type,
                   tp.code,
                   tp.name,
                   tp.model,
                   tp.`desc`,
                   tt.prefix,
                   unix_timestamp(tp.create_time) * 1000                                                                                         AS createTime,
                   (SELECT count(*) FROM `mp-asset`.t_code_base tc WHERE tc.product_id = tp.id AND tc.is_delete = 0)                                     AS baseTotal,
                   (SELECT count(*) FROM `mp-asset`.t_code_base tc WHERE tc.product_id = tp.id AND tc.is_delete = 0 AND tc.storage_batch_id IS NOT NULL) AS baseUsed,
                   (SELECT count(*) FROM `mp-asset`.t_code_base_rfid tc WHERE tc.product_id = tp.id AND tc.is_delete = 0) AS rfidTotal,
                   (SELECT count(*) FROM `mp-asset`.t_code_base_rfid tc WHERE tc.product_id = tp.id AND tc.is_delete = 0 AND tc.storage_batch_id) AS rfidUsed
            FROM `mp-asset`.t_product tp
                     LEFT JOIN `mp-asset`.t_product_type tt ON tp.type_id = tt.id
            WHERE tp.is_delete = 0
            {typeid} {name} {code} {limit};
              """.format(typeid=typeid, name=name, code=code, limit=limit)
        return self.operate_db(sql=sql)


class supplierSQL(DataBaseOperate):
    def __init__(self):
        super(supplierSQL, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)


class warehouseSQL(DataBaseOperate):
    def __init__(self):
        super(warehouseSQL, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)


class excelExportSQL(DataBaseOperate):
    def __init__(self):
        super(excelExportSQL, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)
