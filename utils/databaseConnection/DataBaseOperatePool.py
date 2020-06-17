#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2020/04/02 19:43
@Author: guoyong
"""


import pymysql
import datetime
import decimal
from utils.log import log
from DBUtils.PooledDB import PooledDB
from os import getenv
from utils.dataDecryption import decrypt


class DataBaseOperate(object):
    def __init__(self):
        self.__db_pool = None

    def creat_db_pool(self, host):
        connection_config = decrypt(getenv('INTERFACE_CIPHER'))

        if connection_config.get(host, None) is None:
            log.error("IP域名错误")
            exit(0)

        user = connection_config.get(host).get('user')
        password = connection_config.get(host).get('password')
        port = connection_config.get(host).get('port')

        log.debug('创建数据库连接池：%s' % host)
        self.__db_pool = PooledDB(creator=pymysql,
                                  mincached=3,
                                  maxcached=5,
                                  maxshared=0,
                                  maxconnections=20,
                                  blocking=True,
                                  maxusage=None,
                                  setsession=None,
                                  host=host,
                                  port=port,
                                  user=user,
                                  db=None,
                                  passwd=password)
        log.debug('创建数据库连接池完成!')

    def query_data(self, sql):
        con = self.__db_pool.connection()
        cursor = con.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            log.debug('执行sql:%s' % sql)
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                for fields in result:
                    if isinstance(result[fields], datetime.datetime):
                        result[fields] = str(result[fields].strftime('%Y-%m-%d %H:%M:%S'))
                    elif isinstance(result[fields], datetime.date):
                        result[fields] = str(result[fields].strftime('%Y-%m-%d'))
                    elif isinstance(result[fields], decimal.Decimal):
                        result[fields] = float(result[fields])
            # if len(results) >= 1:
                # log.debug('sql查询结果:\n %s' % results)
            else:
                log.debug('sql查询结果为空')
            return results
        except Exception as e:
            log.error('执行sql异常：\n%s' % e)
        finally:
            cursor.close()
            con.close()

    def close_db_pool(self):
        self.__db_pool.close()
