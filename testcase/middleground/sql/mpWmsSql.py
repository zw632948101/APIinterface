#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/1/7 15:46
# @Author: wei.zhang
# @File : mpWmsSql.py
# @Software: PyCharm
from . import Base, OutStorehouseEnumerate, Source_Enumerate, Warehousing_Enumerate, \
    Transfer_Enumerate
from utils import conversion


class OutStorehouseSql(Base):
    def __init__(self):
        super(OutStorehouseSql, self).__init__()

    def query_invoice_count(self):
        """
        出库通知单-统计
        :return:
        """
        sql = """
            SELECT count(*) AS allCount, 
                   count(if(ti.status = 0, 1, NULL)) AS waitCount,
                   count(if(ti.status = 1, 1, NULL)) AS finishCount,
                   COUNT(IF(ti.status = 2, 1, NULL)) AS cancelCount
            FROM `mp-wms`.t_whs_invoice ti
            WHERE ti.is_delete = 0;
              """
        return self.operate_db(sql=sql)

    def query_admin_invoice_notice_info(self, code=None, relevanceCode=None, status=None,
                                        type_=None, warehouseCode=None, operatorId=None, pn=None,
                                        ps=20):
        """
        查询出库通知单单
        :param code:
        :param relevanceCode:
        :param status:
        :param type_:
        :param warehouseCode:
        :param operatorId:
        :return:
        """
        limit = "limit {ps}".format(ps=ps) if pn is None else "limit {pn},{ps}".format(
            pn=(pn - 1) * ps, ps=ps)
        code = "AND tn.code = '%s'" % code if code is not None else ''
        relevanceCode = "AND tn.relevance_code = '%s'" % relevanceCode if relevanceCode is not None else ''
        status = "AND tn.status = '%s'" % status if status is not None else ''
        type_ = "AND tn.type = '%s'" % type_ if type_ is not None else ''
        warehouseCode = "AND tn.warehouse_code = '%s'" % warehouseCode if warehouseCode is not None else ''
        operatorId = "AND tn.creator_id = '%s'" % operatorId if operatorId is not None else ''
        sql = """
            SELECT tn.code,
                   unix_timestamp(tn.create_time) * 1000 AS createTime,
                   tn.relevance_code                     AS relevanceCode,
                   tn.source                             AS sourceName,
                   tw.name                               AS warehouseName,
                   tn.type AS typeName,
                   CASE tn.status WHEN 0 THEN '待确认' WHEN 1 THEN '已确认' WHEN 2 THEN '已完成' WHEN 3 THEN '取消' END statusName
            FROM `mp-wms`.t_whs_invoice_notice tn,
                 `mp-wms`.t_warehouse tw
            WHERE tn.is_delete = 0
              AND tw.is_delete = 0
              AND tn.warehouse_code = tw.code {codestr} {relevance} {status}
              {type_} {warehouse} {operatorId} 
              ORDER BY tn.id DESC 
              {limit};
              """.format(codestr=code, relevance=relevanceCode, status=status, type_=type_,
                         warehouse=warehouseCode, operatorId=operatorId, limit=limit)
        dbinfo = conversion.replace_dict_value(replace_key='typeName',
                                               keep_dict=self.operate_db(sql=sql),
                                               enumerate_dict=OutStorehouseEnumerate)
        dbinfo = conversion.replace_dict_value(replace_key='sourceName',
                                               keep_dict=dbinfo,
                                               enumerate_dict=Source_Enumerate)
        return dbinfo

    def query_order_code_prdouct_info(self, order_code, pn=None, ps=20):
        """
        查询出库通知单明细
        :param order_code:关联出库通知单
        :param pn:页码
        :param ps:条数
        :return:
        """
        limit = "limit {ps}".format(ps=ps) if pn is None else "limit {pn},{ps}".format(
            pn=(pn - 1) * ps, ps=ps)
        sql = """
            SELECT tw.price,tw.tax_rate AS taxRate,
                   tw.plan_quantity AS planQuantity,
                   ti.name AS productName,
                   ti.alias AS productAlias,
                   ti.code AS productCode,
                   tc1.name AS class1Name,
                   tc2.name AS class2Name,
                   tc3.name AS class3Name,
                   tp.stock_unit AS stockUnit
            FROM `mp-wms`.t_item ti,
                 `mp-wms`.t_item_category tc1,
                 `mp-wms`.t_item_category tc2,
                 `mp-wms`.t_item_category tc3,
                 `mp-wms`.t_whs_invoice_notice_product tw,
                 `mp-wms`.t_product tp
            WHERE ti.class1 = tc1.code
              AND ti.class2 = tc2.code
              AND ti.class3 = tc3.code
              AND ti.code = tw.product_code
              AND ti.code = tp.code
              AND tw.order_code = '{order_code}'
              {limit};
              """.format(order_code=order_code, limit=limit)
        return self.operate_db(sql=sql)

    def query_admin_invoice_info(self, code=None, relevanceCode=None, status=None,
                                 type_=None, warehouseCode=None, operatorId=None, pn=None,
                                 ps=20):
        """
        查询出库单
        :param code:
        :param relevanceCode:
        :param status:
        :param type_:
        :param warehouseCode:
        :param operatorId:
        :return:
        """
        limit = "limit {ps}".format(ps=ps) if pn is None else "limit {pn},{ps}".format(
            pn=(pn - 1) * ps, ps=ps)
        code = "AND tn.code = '%s'" % code if code is not None else ''
        relevanceCode = "AND tn.relevance_code = '%s'" % relevanceCode if relevanceCode is not None else ''
        status = "AND tn.status = '%s'" % status if status is not None else ''
        type_ = "AND tn.type = '%s'" % type_ if type_ is not None else ''
        warehouseCode = "AND tn.warehouse_code = '%s'" % warehouseCode if warehouseCode is not None else ''
        operatorId = "AND tn.creator_id = '%s'" % operatorId if operatorId is not None else ''
        sql = """
            SELECT tn.code,
                   unix_timestamp(tn.create_time) * 1000 AS createTime,
                   tn.relevance_code                     AS relevanceCode,
                   tn.source                             AS sourceName,
                   tw.name                               AS warehouseName,
                   tn.type AS typeName,
                   CASE tn.status WHEN 0 THEN '待出库' WHEN 1 THEN '已确认' WHEN 2 THEN '取消' WHEN 3 THEN '已完成' END statusName,
                   CASE tn.erp_sync_status WHEN 0 THEN '待同步' WHEN 1 THEN '同步成功' WHEN 2 THEN '同步失败' END erpSyncStatus
            FROM `mp-wms`.t_whs_invoice tn,
                 `mp-wms`.t_warehouse tw
            WHERE tn.is_delete = 0
              AND tw.is_delete = 0
              AND tn.warehouse_code = tw.code {codestr} {relevance} {status}
              {type_} {warehouse} {operatorId} 
              ORDER BY tn.id DESC 
              {limit};
              """.format(codestr=code, relevance=relevanceCode, status=status, type_=type_,
                         warehouse=warehouseCode, operatorId=operatorId, limit=limit)
        dbinfo = conversion.replace_dict_value(replace_key='typeName',
                                               keep_dict=self.operate_db(sql=sql),
                                               enumerate_dict=OutStorehouseEnumerate)
        dbinfo = conversion.replace_dict_value(replace_key='sourceName',
                                               keep_dict=dbinfo,
                                               enumerate_dict=Source_Enumerate)
        return dbinfo


class MpMoveSql(Base):
    """
    分拣单模块
    """

    def __init__(self):
        super(MpMoveSql, self).__init__()

    def query_move_code(self, status=None):
        status = 't.status = %s' % status if status else ''
        sql = """
            SELECT t.code,
                   t.relevance_code AS                                                       invoiceCode,
                   t.status,
                   CASE t.status WHEN 0 THEN '待分拣' WHEN 1 THEN '分拣完成' WHEN 2 THEN '取消分拣' END 'statusName',
                   t.type           AS                                                       typeName,
                   tw.name AS warehouseName,
                   t.remark,
                   t.customer,
                   t.supplierName
            FROM `mp-wms`.t_whs_move_doc t LEFT JOIN `mp-wms`.t_warehouse tw ON tw.code = t.warehouse_code
            WHERE t.is_delete = 0
              {status}
            ORDER BY t.id DESC;
              """.format(status=status)
        return conversion.replace_dict_value(replace_key='typeName',
                                             keep_dict=self.operate_db(sql=sql),
                                             enumerate_dict=OutStorehouseEnumerate)

    def query_move_detail_list(self, orderCode):
        """
        拣货单-PDA分拣任务列表
        :param orderCode:
        :return:
        """
        sql = """
            SELECT tm.*,
                   tp.name       AS productName,
                   tp.stock_unit AS stockUnit,
                   tp.isTracing  AS tracing,
                   tp.isLot,
                   ti.alias      AS productAlias,
                   tc1.name      AS class1Name,
                   tc2.name      AS class2Name,
                   tc3.name      AS class3Name
            FROM (SELECT tmp.actual_quantity AS actualQuantity, tmp.id, tmp.lot, tmp.plan_quantity AS planQuantity, tmp.price, tmp.product_code AS productCode
                  FROM `mp-wms`.t_whs_move_doc td
                           LEFT JOIN `mp-wms`.t_whs_move_product tmp ON td.code = tmp.order_code
                  WHERE td.is_delete = 0
                    AND tmp.is_delete = 0
                    AND td.code = '{orderCode}') tm
                     LEFT JOIN `mp-wms`.t_product tp ON tm.productCode = tp.code
                     LEFT JOIN `mp-wms`.t_item ti ON tm.productCode = ti.code
                     LEFT JOIN `mp-wms`.t_item_category tc1 ON ti.class1 = tc1.code
                     LEFT JOIN `mp-wms`.t_item_category tc2 ON ti.class2 = tc2.code
                     LEFT JOIN `mp-wms`.t_item_category tc3 ON ti.class3 = tc3.code
            WHERE tp.is_delete = 0
              AND ti.is_delete = 0
              AND tc1.is_delete = 0
              AND tc2.is_delete = 0
              AND tc3.is_delete = 0;
              """.format(orderCode=orderCode)
        return conversion.del_dict_value_null(self.operate_db(sql=sql))

    def query_move_doc_count(self):
        """
        pda分拣单统计
        :return:
        """
        sql = """
            SELECT count(td.id) AS allCount,
                   count(if(td.status = 1, 1, NULL)) AS finishCount,
                   count(if(td.status = 2, 1, NULL)) AS cancelCount,
                   count(if(td.status = 0, 1, NULL)) AS waitCount
            FROM `mp-wms`.t_whs_move_doc td
            WHERE td.is_delete = 0;
              """
        return self.operate_db(sql=sql)

    def query_pick_doc_info(self, pn=None, ps=20, orderCode=None, status=None, type_=None,
                            warehouseCode=None, operatorId=None):
        """
        查询拣货单列表和拣货单详情
        :param pn: 分页
        :param ps: 条数，默认20
        :param orderCode: 拣货单号
        :param status: 拣货单状态
        :param type_: 单据类型
        :param warehouseCode: 仓库代码
        :param operatorId: 操作人
        :return:
        """
        limit = "limit {ps}".format(ps=ps) if pn is None else "limit {pn},{ps}".format(
            pn=(pn - 1) * ps, ps=ps)
        status = "AND t.status = '%s'" % status if status is not None else ''
        type_ = "AND t.type = '%s'" % type_ if type_ is not None else ''
        warehouseCode = "AND t.warehouse_code = '%s'" % warehouseCode if warehouseCode is not None else ''
        operatorId = "AND t.creator_id = '%s'" % operatorId if operatorId is not None else ''
        orderCode = "AND t.code = '%s'" % orderCode if orderCode else ''
        sql = """
            SELECT t.code,
                   t.relevance_code AS                                                       relevanceCode,
                   CASE t.status WHEN 0 THEN '待分拣' WHEN 1 THEN '分拣完成' WHEN 2 THEN '取消分拣' END 'statusName',
                   t.type           AS                                                       typeName,
                   tw.name          AS                                                       warehouseName,
                   t.source         AS                                                       sourceName,
                   (unix_timestamp(t.create_time)-8*3600) * 1000     AS                      createTime,
                   tu.phone                                          AS                      creatorPhone,
                   tu.username                                       AS                      creatorName
            FROM `mp-wms`.t_whs_move_doc t
                     LEFT JOIN `mp-wms`.t_warehouse tw ON tw.code = t.warehouse_code AND tw.is_delete = 0
                     LEFT JOIN `world-user`.t_user tu ON tu.id = t.creator_id AND tu.is_delete = 0
            WHERE t.is_delete = 0
            {ordercode}
            {status}
            {type_}
            {warehouseCode}
            {operatorId}
            ORDER BY t.id DESC {limit};
              """.format(ordercode=orderCode, status=status, type_=type_,
                         warehouseCode=warehouseCode, operatorId=operatorId, limit=limit)
        dbinfo = conversion.replace_dict_value('typeName', self.operate_db(sql=sql),
                                               OutStorehouseEnumerate)
        return conversion.replace_dict_value('sourceName', dbinfo, Source_Enumerate)


class ReeciptProduct(Base):
    def __init__(self):
        super(ReeciptProduct, self).__init__()

    def query_pda_receipt_product_list(self, ordercode):
        """
        根据入库订单查询商品清单
        :param ordercode:
        :return:
        """
        sql = """
            SELECT tp.product_code AS productCode, tp.plan_quantity AS actualQuantity
            FROM `mp-wms`.t_whs_receipt_product tp
            WHERE tp.is_delete = 0
              AND tp.order_code = '{ordercode}';
              """.format(ordercode=ordercode)
        return self.operate_db(sql=sql)
