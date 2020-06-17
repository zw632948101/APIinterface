#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
__author__ = "yong.guo"
__data__ = "2019/07/25"
"""
from utils.log import log
from utils.checkApiChanges.model.dbEngine import DBEngine
from utils.checkApiChanges.model.tInterface import Interface
from utils.checkApiChanges.model.tInputParameters import InputParameters
from utils.checkApiChanges.model.tExtractParameters import ExtractParameters
from sqlalchemy import orm
from sqlalchemy.sql import and_, or_
import json
from utils.checkApiChanges.model.tServer import Server


class AskDatabaseForApiData(object):
    def __init__(self):
        self.__db_engine = DBEngine()
        # self.database_data = self.get_database_data()

    def get_database_data(self, host):
        log.info("从数据库获取接口信息")
        session = self.__db_engine.creat_session()

        # 获取该服务器下所有接口
        whichService = session.query(Server.id).filter(or_(Server.qaURL == host, Server.devURL == host)).all()

        if whichService == []:
            return
        whichService = whichService[0][0]
        apis = session.query(Interface.id, Interface.apiPath, Interface.apiDesc, Interface.apiRequestMethod
                             ).filter(and_(Interface.apiServerId == whichService, Interface.apiStatus == 1)).all()
        api_result = {}

        # 获取接口中所有参数信息
        for api in apis:
            api_id = api[0]
            api_path = api[1]
            api_desc = api[2]
            api_method = api[3]

            # 组装要返回的api请求响应参数信息
            api_result.update({api_path: {"desc": api_desc,
                                          "method": api_method,
                                          "inParameter": None,
                                          "outParameter": None
                                          }})

            # 组装请求字段信息
            try:
                in_parameter = session.query(InputParameters.inParameter).filter(and_(InputParameters.apiId == api_id,
                                                                                      InputParameters.inParameterStatus == 1
                                                                                      )).one()
                api_result.get(api_path).update({"inParameter": json.loads(in_parameter[0])})
            except orm.exc.NoResultFound:
                api_result.get(api_path).update({"inParameter": None})

            # 组装响应字段信息
            try:
                out_parameter = session.query(ExtractParameters.extParameter).filter(
                    and_(ExtractParameters.apiId == api_id,
                         ExtractParameters.extParameterStatus == 1
                         )).one()
                api_result.get(api_path).update({"outParameter": json.loads(out_parameter[0])})
            except orm.exc.NoResultFound:
                api_result.get(api_path).update({"outParameter": None})

        self.__db_engine.close_session()
        return api_result
