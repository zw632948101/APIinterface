#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = "yong.guo"
__data__ = "2019/07/23"
"""
from . import *


class Server(Base):
    # 表名
    __tablename__ = 't_server'

    # 表结构
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True, index=True)
    serverName = Column(String(20), nullable=False, comment='服务名称')
    swaggerURI = Column(String(100), nullable=False, comment="接口说明地址-swagger")
    qaURL = Column(String(100), nullable=False, comment='测试环境地址')
    devURL = Column(String(100), nullable=False, comment='开发环境地址')
    serverStatus = Column(SmallInteger, nullable=False, default=1, comment="服务状态 1启用，2禁用")

    createTime = Column(DateTime, nullable=False, server_default=func.now(), comment='记录创建时间')
    updateTime = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now(), comment='记录更新时间')
    interface = relationship("Interface", backref="interface_of_server")
