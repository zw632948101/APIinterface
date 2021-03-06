#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/1/5 16:02
# @Author: wei.zhang
# @File : tExtractParameters.py
# @Software: PyCharm
from . import *


class ExtractParameters(Base):
    # 表名
    __tablename__ = 't_extract_parameters'

    # 表结构
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True, index=True)
    apiId = Column(Integer, ForeignKey("t_interface.id", ondelete="CASCADE"), nullable=False,
                   comment="接口ID")
    extParameter = Column(Text, nullable=False, comment="出参数信息")
    extParameterStatus = Column(SmallInteger, nullable=False, default=1, comment="参数状态 1启用，2禁用")

    createTime = Column(DateTime, nullable=False, server_default=func.now(), comment='记录创建时间')
    updateTime = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                        comment='记录更新时间')


class ExecutionApi(Base):
    # 表名
    __tablename__ = 't_execution_api'

    # 表结构 执行
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True, index=True)
    apiId = Column(Integer, ForeignKey("t_interface.id", ondelete="CASCADE"), nullable=False,
                   comment="接口ID")
    extParameter = Column(Text, nullable=False, comment="出参数信息")
    inParameter = Column(Text, nullable=False, comment="入参数信息")
    respStatus = Column(String(10), nullable=False, comment="返回接口状态")
    isDelete = Column(SmallInteger, nullable=False, default=0, comment="0在用，1删除")

    createTime = Column(DateTime, nullable=False, server_default=func.now(), comment='记录创建时间')
    updateTime = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
                        comment='记录更新时间')
