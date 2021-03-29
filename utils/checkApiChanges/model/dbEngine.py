#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from utils.dataDecryption import decrypt
from utils.environmentConfiguration import config
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session
from sqlalchemy.dialects.mysql import LONGTEXT
from migrate.versioning import api
import os.path
from . import Base


class DBEngine(object):
    def __init__(self):
        # 初始化数据库链接
        self.SQLALCHEMY_MIGRATE_REPO = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                    'db_repository')
        self.dataBaseURI = decrypt(config.get('dataBaseURI'))
        # self.dataBaseURI = 'mysql+pymysql://jira:jirapasswd@132.232.46.177:3306/jira'
        self.__engine = create_engine(self.dataBaseURI,
                                      max_overflow=5,  # 超过连接池大小外最多创建的数量,
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

    def db_create(self):
        if not os.path.exists(self.SQLALCHEMY_MIGRATE_REPO):
            api.create(self.SQLALCHEMY_MIGRATE_REPO, 'database repository')
            api.version_control(self.dataBaseURI, self.SQLALCHEMY_MIGRATE_REPO)
        else:
            api.version_control(self.dataBaseURI, self.SQLALCHEMY_MIGRATE_REPO,
                                api.version(self.SQLALCHEMY_MIGRATE_REPO))

    def update_migrate(self):
        import imp
        migration = self.SQLALCHEMY_MIGRATE_REPO + '/versions/%sd_migration.py' % (
                api.db_version(self.dataBaseURI, self.SQLALCHEMY_MIGRATE_REPO) + 1)
        tmp_module = imp.new_module('old_model')
        old_model = api.create_model(self.dataBaseURI, self.SQLALCHEMY_MIGRATE_REPO)
        exec(old_model, tmp_module.__dict__)
        script = api.make_update_script_for_model(self.dataBaseURI, self.SQLALCHEMY_MIGRATE_REPO,
                                                  tmp_module.meta, Base.metadata)
        open(migration, 'wt').write(script)
        api.upgrade(self.dataBaseURI, self.SQLALCHEMY_MIGRATE_REPO)
        api.update_db_from_model(self.dataBaseURI, self.SQLALCHEMY_MIGRATE_REPO, Base.metadata)
