#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from . import *


class InputParameters(Base):
    # 表名
    __tablename__ = 't_input_parameters'

    # 表结构
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True, index=True)
    apiId = Column(Integer, ForeignKey("t_interface.id", ondelete="CASCADE"), nullable=False, comment="接口ID")
    inParameter = Column(Text, nullable=False, comment="入参数信息")
    inParameterStatus = Column(SmallInteger, nullable=False, default=1, comment="参数状态 1启用，2禁用")

    createTime = Column(DateTime, nullable=False, server_default=func.now(), comment='记录创建时间')
    updateTime = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now(), comment='记录更新时间')

