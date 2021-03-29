#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from utils.log import log
from utils.checkApiChanges.model.dbEngine import DBEngine
from sqlalchemy import orm
from sqlalchemy.sql import and_, or_
import json
from utils.checkApiChanges.model.tServer import Server
from utils.checkApiChanges.model.tInputParameters import InputParameters
from utils.checkApiChanges.model.tInterface import Interface
from utils.checkApiChanges.model.tExtractParameters import ExtractParameters
from utils.environmentConfiguration import config


class AskDatabaseForApiData(object):
    def __init__(self):
        self.__db_engine = DBEngine()
        # self.database_data = self.get_database_data()
        self.env = config.get('hosts').get(config.get('updateActionAPI'))

    def get_database_data(self, host):
        log.info("从数据库获取接口信息")
        session = self.__db_engine.creat_session()

        # 获取该服务器下所有接口
        whichService = session.query(Server.id).filter(
            or_(Server.qaURL == host, Server.devURL == host),
            and_(Server.serverStatus == 1)).first()
        if whichService == [] or whichService is None:
            servername = ''
            for i in self.env.keys():
                if self.env.get(i) == host:
                    servername = i
                    break
            serverid = session.query(Server).filter(
                and_(Server.serverName == servername, Server.serverStatus == 1)).first()
            if config.get('updateActionAPI') in ('DEV_API', 'DEV'):
                devurl = host
                qaurl = config.get('hosts').get('QA').get(servername)
            else:
                qaurl = host
                devurl = config.get('hosts').get('DEV').get(servername)
            if serverid == [] or serverid is None:
                addserver = Server(serverName=servername, swaggerURI='/v2/api-docs', qaURL=qaurl,
                                   devURL=devurl, serverStatus=1)
                session.add(addserver)
            else:
                log.info('数据库中已有相同的服务名：%s' % servername)
            session.commit()
            whichService = session.query(Server.id).filter(
                or_(Server.qaURL == host, Server.devURL == host)).first()
        whichService = whichService.id
        apis = session.query(Interface.id, Interface.apiPath, Interface.apiDesc,
                             Interface.apiRequestMethod
                             ).filter(
            and_(Interface.apiServerId == whichService, Interface.apiStatus == 1)).all()
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
                in_parameter = session.query(InputParameters.inParameter).filter(
                    and_(InputParameters.apiId == api_id,
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

    def updata_database(self, keys, host):
        """
        读取校验后的数据对数据库进行增删改
        :param dict keys:
        :param str host:
        :return:
        """
        log.info('执行数据更新接口信息')
        session = self.__db_engine.creat_session()
        serverid = session.query(Server.id).filter(
            or_(Server.qaURL == host, Server.devURL == host),
            and_(Server.serverStatus == 1)).first()
        for status in keys.keys():
            if status == 'new_info':
                nwe_info = keys.get(status)
                for api in nwe_info.keys():
                    apiparameter = nwe_info.get(api)
                    desc = str(apiparameter.get('desc'))
                    method = str(apiparameter.get('method'))
                    apiId = session.query(Interface.id).filter(
                        and_(Interface.apiPath == api, Interface.apiStatus == 1,
                             Interface.apiServerId == serverid.id)).first()
                    if apiId is None:
                        ifs = Interface(apiPath=api, apiServerId=serverid.id, apiDesc=desc,
                                        apiRequestMethod=method, apiStatus=1)
                        session.add(ifs)
                        session.commit()
                        apiId = session.query(Interface.id).filter(
                            and_(Interface.apiPath == api, Interface.apiStatus == 1,
                                 Interface.apiServerId == serverid.id)).first()
                    inParameter = json.dumps(apiparameter.get('inParameter'))
                    extParameter = json.dumps(apiparameter.get('outParameter'))
                    ips = InputParameters(apiId=apiId.id, inParameter=inParameter,
                                          inParameterStatus=1)
                    eps = ExtractParameters(apiId=apiId.id, extParameter=extParameter,
                                            extParameterStatus=1)
                    session.add_all([ips, eps])
                    session.commit()
            elif status == 'update_info':
                update_info = keys.get(status)
                for api in update_info.keys():
                    apiparameter = update_info.get(api)
                    apiId = session.query(Interface.id).filter(
                        and_(Interface.apiPath == api, Interface.apiStatus == 1,
                             Interface.apiServerId == serverid.id)).first()
                    inParameter = json.dumps(apiparameter.get('inParameter'))
                    extParameter = json.dumps(apiparameter.get('outParameter'))
                    ips = session.query(InputParameters).filter(
                        and_(InputParameters.apiId == apiId.id,
                             InputParameters.inParameterStatus == 1)).first()
                    ips.inParameter = inParameter
                    eps = session.query(ExtractParameters).filter(
                        and_(ExtractParameters.apiId == apiId.id,
                             ExtractParameters.extParameterStatus == 1)).first()
                    eps.extParameter = extParameter
                    session.commit()
            elif status == 'del_info':
                update_info = keys.get(status)
                for api in update_info.keys():
                    apiId = session.query(Interface).filter(
                        and_(Interface.apiPath == api, Interface.apiStatus == 1,
                             Interface.apiServerId == serverid.id)).first()
                    ips = session.query(InputParameters).filter(
                        and_(InputParameters.apiId == apiId.id,
                             InputParameters.inParameterStatus == 1)).first()
                    ips.inParameterStatus = 2
                    eps = session.query(ExtractParameters).filter(
                        and_(ExtractParameters.apiId == apiId.id,
                             ExtractParameters.extParameterStatus == 1)).first()
                    eps.extParameterStatus = 2
                    apiId.apiStatus = 2
                    session.commit()
        self.__db_engine.close_session()
