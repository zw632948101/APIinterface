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
from utils import conversion


class InternalServerError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        print(self.msg)


class apiTestResult(object):
    def __init__(self, api, host, datas, resp):
        self.__db_engine = DBEngine()
        self.api = api
        self.host = host
        self.datas = datas
        self.resp = resp
        # asyncio.run(self.tested_interface())
        asyncio.get_event_loop().run_until_complete(self.tested_interface())

    async def tested_interface(self):
        log.info("从数据库获取接口信息")
        session = self.__db_engine.creat_session()
        whichServer = session.query(Server.id).filter(
            or_(Server.qaURL == self.host, Server.devURL == self.host),
            and_(Server.serverStatus == 1)).first()
        if whichServer == [] or whichServer is None:
            log.error("无当前执行服务：%s" % self.host)
            raise InternalServerError("无当前执行服务：%s" % self.host)

        whichapi = session.query(Interface.id).filter(
            and_(Interface.apiPath == self.api, Interface.apiStatus == 1,
                 Interface.apiServerId == whichServer.id)).first()

        if whichapi == [] or whichapi is None:
            log.error("无当前执行接口：%s" % self.api)
            raise InternalServerError("无当前执行接口：%s" % self.api)
        apiInterface = session.query(Interface).filter(
            and_(Interface.id == whichapi.id, Interface.apiStatus == 1)).first()
        apiInterface.testStatus = 1
        casepar = session.query(ExecutionApi).filter(
            and_(ExecutionApi.apiId == whichapi.id, ExecutionApi.isDelete == 0,
                 ExecutionApi.respStatus == json.loads(self.resp).get('status'))).all()
        session.commit()
        ca = []
        for i in casepar:
            ca.append(i.extParameter)
        if casepar == [] or casepar is None:
            ea = ExecutionApi(apiId=whichapi.id, extParameter=str(self.resp),
                              inParameter=str(self.datas),
                              respStatus=json.loads(self.resp).get('status'))
            session.add(ea)
        elif json.loads(self.resp).get('status') == 'OK':
            log.info('已有测试通过案例，更新已有用例')
            for i in range(len(casepar)):
                casepar[i].extParameter = str(self.resp)
                casepar[i].inParameter = str(self.datas)
        elif json.loads(self.resp).get('status') == 'ERROR' and str(self.resp) in ca:
            log.info('已有相同失败案例，不记录')
        elif json.loads(self.resp).get('status') in ('ERROR', 'OK') and str(self.resp) not in ca:
            ea = ExecutionApi(apiId=whichapi.id, extParameter=str(self.resp),
                              inParameter=str(self.datas),
                              respStatus=json.loads(self.resp).get('status'))
            session.add(ea)
        session.commit()
        self.__db_engine.close_session()


# if __name__ == '__main__':
#     host = "http://qa-gateway.worldfarm.com/mp-asset"
#     api = "/admin/product/edit"
#     datas = '{"attrName": "\\u6570\\u91cf", "unit": "\\u53f0", "type": "2"}'
#     resp = '{"errorCode": "11050003","errorMsg": "编码必须是字母或字母+数字1","status": "ERROR"}'
#     a = apiTestResult(api=api, host=host, datas=datas, resp=resp)
