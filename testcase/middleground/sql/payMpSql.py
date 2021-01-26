#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/1/14 18:56
# @Author: wei.zhang
# @File : payMpSql.py
# @Software: PyCharm
from . import Base

"""
支付中台 查询数据
"""


class TradeSql(Base):
    def __init__(self):
        super(TradeSql,self).__init__()