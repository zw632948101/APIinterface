#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = "yong.guo"
__data__ = "2019/07/23"
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.dataDecryption import decrypt
from utils.environmentConfiguration import config
from . import Base


class DBEngine(object):
    def __init__(self):
        # 初始化数据库链接
        dataBaseURI = decrypt(config.get('dataBaseURI'))
        self.__engine = create_engine(dataBaseURI,
                                      max_overflow=2,  # 超过连接池大小外最多创建的数量,
                                      pool_size=5,  # 连接池的大小
                                      pool_timeout=30,  # 池中没有线程最多等待的时间
                                      pool_recycle=-1,  # 多久之后对线程中的线程进行一次连接的回收(重置)
                                      encoding="utf-8",
                                      echo=False)
        Base.metadata.create_all(self.__engine)
        self.session = None

    def creat_session(self):
        self.session = sessionmaker(bind=self.__engine)()
        return self.session

    def close_session(self):
        self.session.close()
        return "OK"
