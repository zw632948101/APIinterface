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
               ta.is_delete   AS isDelete
            FROM `mp-asset`.t_attribute_dict ta
            WHERE ta.is_delete = 0
              AND ta.product_id = {pid}
            ORDER BY ta.id DESC;
              """.format(pid=pid)
        return self.operate_db(sql=sql)

    def query_product_list_page(self, typeid=None, name=None, code=None, pn=None, ps=None, productid=None):
        """
        查询资产产品列表
        :param typeid:
        :param name:
        :param code:
        :param pn:
        :param ps:
        :param productid:
        :return:
        """
        typeid = "AND tp.type_id = '%s'" % typeid if typeid is not None else ''
        name = "AND tp.name = '%s'" % name if name is not None else ''
        code = "AND tp.code = '%s'" % code if code is not None else ''
        productid = "AND tp.code = '%s'" % productid if productid is not None else ''
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
                   (SELECT count(*) FROM `mp-asset`.t_code_base tc WHERE tc.product_id = tp.id AND tc.is_delete = 0 AND tc.status = 20) AS baseUsed,
                   (SELECT count(*) FROM `mp-asset`.t_code_base_rfid tc WHERE tc.product_id = tp.id AND tc.is_delete = 0) AS rfidTotal,
                   (SELECT count(*) FROM `mp-asset`.t_code_base_rfid tc WHERE tc.product_id = tp.id AND tc.is_delete = 0 AND tc.status = 20) AS rfidUsed
            FROM `mp-asset`.t_product tp
                     LEFT JOIN `mp-asset`.t_product_type tt ON tp.type_id = tt.id
            WHERE tp.is_delete = 0
            {typeid} {name} {code} {productid}
            ORDER BY tp.type_id ASC ,tp.create_time ASC
            {limit};
              """.format(typeid=typeid, name=name, code=code, limit=limit, productid=productid)
        return self.operate_db(sql=sql)

    def query_product_type_id(self):
        """
        查询产品类型id
        :return:
        """
        sql = """
        SELECT id,prefix FROM `mp-asset`.t_product_type WHERE is_delete = 0;
              """
        return self.operate_db(sql=sql)

    def query_prodcut_parameter_info(self, code, name, unit, typeid):
        """
        根据参数查询资产信息
        :param code:
        :param name:
        :param unit:
        :param typeid:
        :return:
        """
        sql = """
            SELECT *
            FROM `mp-asset`.t_product
            WHERE code = '%s'
              AND name = '%s'
              AND unit = '%s'
              AND type_id = %s;
              """ % (code, name, unit, typeid)
        return self.operate_db(sql=sql)

    def query_admin_product_list(self):
        """
        查询资产产品
        :return:
        """
        sql = """
            SELECT tp.id,
                   tp.name
            FROM `mp-asset`.t_product tp
            WHERE tp.is_delete = 0
            ORDER BY tp.id DESC;
              """
        return self.operate_db(sql=sql)


class supplierSQL(DataBaseOperate):
    def __init__(self):
        super(supplierSQL, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)


class warehouseSQL(DataBaseOperate):
    def __init__(self):
        super(warehouseSQL, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def query_asset_apply_status_data(self, applicantid=None, status=10):
        """
        查询待出库的资产申请
        :param applicantid:
        :param status:
        :return:
        """
        applicantid = 'AND ta.applicant_id = %s' % applicantid if applicantid is not None else ''
        sql = """
            SELECT *
            FROM `mp-asset`.t_asset_apply ta
            WHERE ta.is_delete = 0
              AND ta.status = {status}
              AND ta.warehouse_id IS NOT NULL
              {applicantid}
            ORDER BY ta.id;
              """.format(applicantid=applicantid, status=status)
        return self.operate_db(sql=sql)

    def query_status_product_warehouse_aseet_code(self, status=10, warehouseid=None, product_id=None):
        """
        跟进资产id和仓库id查询待出库的编码
        :param status:
        :param warehouseid:
        :param product_id:
        :return:
        """
        product_id = "AND ta.product_id = %s" % product_id if product_id is not None else ''
        warehouseid = "AND ta.warehouse_id = %s" % warehouseid if warehouseid is not None else ''
        sql = """
                SELECT *
                FROM `mp-asset`.t_asset ta
                WHERE ta.status = {status}
                AND ta.is_delete = 0
                {product_id} {warehouseid};
              """.format(status=status, product_id=product_id, warehouseid=warehouseid)
        return self.operate_db(sql=sql)


class excelExportSQL(DataBaseOperate):
    def __init__(self):
        super(excelExportSQL, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)


class applySQL(DataBaseOperate):
    def __init__(self):
        super(applySQL, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)


class mobileWarehouseSQL(DataBaseOperate):
    def __init__(self):
        super(mobileWarehouseSQL, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def query_admin_type_dict(self, typeid=None):
        """
        根据传入参数查询类型
        :param typeid:
        :return:
        """
        sql = """
        SELECT tt.id,tt.name FROM `mp-asset`.t_type_dict tt WHERE tt.type = {typeid};
              """.format(typeid=typeid)
        return self.operate_db(sql=sql)

    def query_warehouse_detail(self, id_=None, code=None, name=None):
        """
        根据传入参数查询仓库详情
        :param id_:
        :param code:
        :param name:
        :return:
        """
        id_ = 'AND tw.id = %s' % id_ if id_ else ''
        code = "AND tw.code = '%s'" % code if code else ''
        name = "AND tw.name = '%s'" % name if name else ''
        sql = """
            SELECT tw.address,
                   tw.area,
                   tw.capacity,
                   tw.code,
                   unix_timestamp(tw.create_time) * 1000 AS createTime,
                   tw.id,
                   tw.landlord,
                   tw.landlord_phone                     AS landlordPhone,
                   tw.lat,
                   tw.lng,
                   tw.name,
                   tw.remark,
                   tw.rent,
                   tw.rent_unit                          AS rentUnit,
                   unix_timestamp(tw.lease_end_time)* 1000 AS leaseEndTime,
                   unix_timestamp(tw.lease_start_time)* 1000 AS leaseStartTime,
                   tw.goods_type_ids AS goodsType
            FROM `mp-asset`.t_warehouse tw
            WHERE tw.is_delete = 0
            {code} {name} {id} ;
              """.format(code=code, id=id_, name=name)
        return self.operate_db(sql)

    def query_asset_biz_attach(self, bizid):
        """
        查询业务附件
        :param bizid:
        :return:
        """
        sql = """
                SELECT *
                FROM `mp-asset`.t_biz_attach tb
                WHERE tb.is_delete = 0
                  AND tb.biz_id = %s
                  AND tb.file_type = 1
                  AND tb.biz_type = 1
                  ORDER BY tb.id DESC;
              """ % bizid
        return self.operate_db(sql=sql)

    def query_warehouse_user_base(self, warid):
        """
        根据仓库查询仓库管理员
        :param warid:
        :return:
        """
        sql = """
            SELECT tb.user_id, tb.name
            FROM `mp-asset`.t_storeman ts
                     LEFT JOIN `mp-asset`.t_user_base tb ON tb.user_id = ts.user_id
            WHERE ts.warehouse_id = %s;
              """ % warid
        return self.operate_db(sql)

    def query_my_warehouse_info(self, userid):
        """
        根据用户id查询当前用户的仓库
        :param userid:
        :return:
        """
        sql = """
            SELECT tw.code, tw.id, tw.name
            FROM `mp-asset`.t_warehouse tw
                     LEFT JOIN `mp-asset`.t_storeman ts ON tw.id = ts.warehouse_id
            WHERE tw.is_delete = 0
              AND ts.is_delete = 0
              AND ts.user_id = %s;
              """ % userid
        return self.operate_db(sql)


class assetSQL(DataBaseOperate):
    def __init__(self):
        super(assetSQL, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)

    def query_code_base_all_code(self, productid=3):
        """
        查询铭牌编码code
        :return:
        """
        sql = """
            SELECT tc.code AS qrCode
            FROM `mp-asset`.t_code_base tc
            WHERE tc.product_id = %s
              AND tc.is_delete = 0
              AND tc.status = 10 LIMIT 20;
              """ % productid
        return self.operate_db(sql=sql)

    def query_code_base_all_rfidcode(self, productid=3):
        """
        查询铭牌编码rfidcode
        :return:
        """
        sql = """
            SELECT tc.code AS rfidCode
            FROM `mp-asset`.t_code_base_rfid tc
            WHERE tc.product_id = %s
              AND tc.is_delete = 0
              AND tc.status = 10 LIMIT 20;
              """ % productid
        return self.operate_db(sql=sql)
