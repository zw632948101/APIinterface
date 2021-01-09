#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2020/10/27 17:28
# @Author: wei.zhang
# @File : __init__.py.py
# @Software: PyCharm

from utils.databaseConnection.DataBaseOperate import DataBaseOperate
from utils.environmentConfiguration import config

host_ip = config.get('database').get(config.get('run')).get('host_ip')
Source_Enumerate = {"ZH": "追花族管理版", "DS": "电商端", "POS": "POS端", "ZC": "资产管理端", "GYL": "供应链端",
                    "ERP": "ERP端"}
Warehousing_Enumerate = {"RK01": "原料采购入库", "RK02": "物资采购入库", "RK03": "副产品采购入库", "RK04": "补货入库",
                         "RK05": "要货入库", "RK06": "紧急要货入库", "RK07": "资产调拨入库", "RK08": "资产回收入库",
                         "RK09": "资产加工入库", "RK10": "销售退货入库", "RK11": "摇蜜入库", "RK12": "副产品入库",
                         "RK13": "生产入库", "RK14": "供应链调拨入库", "RK15": "其他入库", "RK16": "辅料采购入库",
                         "RK17": "生产调拨入库"}
OutStorehouseEnumerate = {"CK01": "销售出库", "CK02": "副产品销售出库", "CK03": "补货出库", "CK04": "要货出库",
                          "CK05": "紧急要货出库", "CK06": "资产调拨出库", "CK07": "资产领用出库", "CK08": "资产加工出库",
                          "CK09": "资产采购退货出库", "CK10": "辅料采购退货出库", "CK11": "摇蜜出库", "CK12": "生产出库",
                          "CK13": "供应链调拨出库", "CK14": "其他出库（损耗）", "CK15": "生产调拨出库"}
Transfer_Enumerate = {"DB01": "补货调拨", "DB02": "要货调拨", "DB03": "紧急调拨", "DB04": "生产调拨",
                      "DB05": "资产调拨", "DB06": "供应链调拨", "DB07": "其他调拨"}


class Base(DataBaseOperate):
    def __init__(self):
        super(Base, self).__init__()
        self.operate_db = lambda sql: self.operate(host=host_ip, sql=sql)
