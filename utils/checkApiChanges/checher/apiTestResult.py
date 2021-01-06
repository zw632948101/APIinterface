#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/1/5 16:08
# @Author: wei.zhang
# @File : apiTestResult.py
# @Software: PyCharm
from utils.log import log
from utils.checkApiChanges.model.dbEngine import DBEngine
import asyncio
from sqlalchemy.sql import and_, or_
import json
from utils.checkApiChanges.model.tInterface import Interface
from utils.checkApiChanges.model.tServer import Server
from utils.checkApiChanges.model.tExtractParameters import ExecutionApi


class InternalServerError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        print(self.msg)


class apiTestResult(object):
    def __init__(self, api, host, datas, resp):
        self.__db_engine = DBEngine()
        asyncio.run(self.tested_interface(api, host, datas, resp))

    async def tested_interface(self, api, host, datas, resp):
        log.info("从数据库获取接口信息")
        session = self.__db_engine.creat_session()
        whichServer = session.query(Server.id).filter(
            or_(Server.qaURL == host, Server.devURL == host),
            and_(Server.serverStatus == 0)).first()
        if whichServer == [] or whichServer is None:
            log.error("无当前执行服务：%s" % host)
            raise InternalServerError("无当前执行服务：%s" % host)

        whichapi = session.query(Interface.id).filter(
            and_(Interface.apiPath == api, Interface.apiStatus == 1,
                 Interface.apiServerId == whichServer.id)).first()

        if whichapi == [] or whichapi is None:
            log.error("无当前执行接口：%s" % api)
            raise InternalServerError("无当前执行接口：%s" % api)
        apiInterface = session.query(Interface).filter(
            and_(Interface.id == whichapi.id, Interface.apiStatus == 1)).all()
        apiInterface.testStatus = 1
        casepar = session.query(ExecutionApi).filter(
            and_(ExecutionApi.apiId == whichapi.id, ExecutionApi.isDelete == 0,
                 ExecutionApi.respStatus == json.loads(resp).get('status'))).all()
        if casepar == [] and casepar is None:
            ExecutionApi(apiId=whichapi.id, extParameter=str(resp), inParameter=str(datas),
                           respStatus=json.loads(resp).get('status'))
        if resp.get('status') == 'OK':
            log.info('已有测试通过案例，更新已有用例')
            casepar.extParameter = str(resp)
            casepar.inParameter = str(datas)
        if resp.get('status') == 'ERROR' and str(resp) in casepar.extParameter:
            log.info('已有相同失败案例，不记录')
        if resp.get('status') == 'ERROR' and str(resp) not in casepar.extParameter:
            ExecutionApi(apiId=whichapi.id, extParameter=str(resp), inParameter=str(datas),
                           respStatus=json.loads(resp).get('status'))
        session.commit()
        self.__db_engine.close_session()
