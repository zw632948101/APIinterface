#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = "yong.guo"
__data__ = "2019/07/23"
"""
from . import *


class ExtractParameters(Base):
    # 表名
    __tablename__ = 't_extract_parameters'

    # 表结构
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True, index=True)
    apiId = Column(Integer, ForeignKey("t_interface.id", ondelete="CASCADE"), nullable=False, comment="接口ID")
    extParameter = Column(Text, nullable=False, comment="出参数信息")
    extParameterStatus = Column(SmallInteger, nullable=False, default=1, comment="参数状态 1启用，2禁用")

    createTime = Column(DateTime, nullable=False, server_default=func.now(), comment='记录创建时间')
    updateTime = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now(), comment='记录更新时间')






