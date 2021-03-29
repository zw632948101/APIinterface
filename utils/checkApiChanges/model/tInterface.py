#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from . import *


class Interface(Base):
    # 表名
    __tablename__ = 't_interface'

    # 表结构
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True, comment="接口ID", index=True)
    apiPath = Column(String(100), nullable=False, comment="接口路径", index=True)
    apiServerId = Column(Integer, ForeignKey("t_server.id", ondelete="CASCADE"), comment="所属服务ID")
    apiDesc = Column(String(100), comment="接口说明")
    apiRequestMethod = Column(String(10), nullable=False, comment="接口请求方法", index=True)
    testStatus = Column(SmallInteger, nullable=False, default=1, comment="测试状态 1未测试，2已测试")
    apiStatus = Column(SmallInteger, nullable=False, default=1, comment="接口状态 1启用，2禁用")
    createTime = Column(DateTime, nullable=False, server_default=func.now(), comment='记录创建时间')
    updateTime = Column(DateTime, nullable=False, server_default=func.now(), onupdate=func.now(), comment='记录更新时间')

    # input_parameters = relationship("InputParameters", backref="input_parameters_of_api")
    # interface = relationship("Interface", backref="interface_of_api")
    # extract_parameters = relationship("ExtractParameters", backref="extract_parameters_of_api")


