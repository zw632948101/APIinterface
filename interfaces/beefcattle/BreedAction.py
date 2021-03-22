#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
from utils.checkApiChanges.checher.apiTestResult import apiTestResult
import json


class breedAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('BF_BREED')

    def set_user(self, mobile=None, account_type='user', **kwargs):
        if mobile is None:
            self.user = None
        else:
            self.user = User(mobile, account_type, **kwargs)
            self.request.headers.update({"_Device-Id_": self.user.device_id})
            self.request.headers.update({"_Token_": self.user.token})
        return self.user

    def __judge_response_status(self, json_response):
        if json_response['status'] in ("OK", "ERROR"):
            return json_response
        else:
            raise Exception('status未返回OK或ERROR')

    def _admin_bizAttach_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/bizAttach/get', data=data, hosts=self.url)
        apiTestResult(api='/admin/bizAttach/get', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_bull_add(self, cattleNo_=None, cattleFarmId_=None, frozenSemenNo_=None, variety_=None, fatherNo_=None, motherNo_=None, sexControlStatus_=None, remark_=None):
        if self.user is None:
            data = {'cattleNo': cattleNo_, 'cattleFarmId': cattleFarmId_, 'frozenSemenNo': frozenSemenNo_, 'variety': variety_, 'fatherNo': fatherNo_, 'motherNo': motherNo_, 'sexControlStatus': sexControlStatus_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleNo': cattleNo_, 'cattleFarmId': cattleFarmId_, 'frozenSemenNo': frozenSemenNo_, 'variety': variety_, 'fatherNo': fatherNo_, 'motherNo': motherNo_, 'sexControlStatus': sexControlStatus_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/bull/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/bull/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_bull_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/bull/del', data=data, hosts=self.url)
        apiTestResult(api='/admin/bull/del', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_bull_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/bull/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/bull/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_bull_edit(self, cattleNo_=None, id_=None, frozenSemenNo_=None, variety_=None, fatherNo_=None, motherNo_=None, sexControlStatus_=None, remark_=None):
        if self.user is None:
            data = {'cattleNo':cattleNo_, 'id': id_, 'frozenSemenNo': frozenSemenNo_, 'variety': variety_, 'fatherNo': fatherNo_, 'motherNo': motherNo_, 'sexControlStatus': sexControlStatus_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleNo':cattleNo_, 'id': id_, 'frozenSemenNo': frozenSemenNo_, 'variety': variety_, 'fatherNo': fatherNo_, 'motherNo': motherNo_, 'sexControlStatus': sexControlStatus_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/bull/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/bull/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_bull_list(self, pn_=None, ps_=None, cattleFarmId_=None, cattleNo_=None, frozenSemenNo_=None, variety_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'cattleNo': cattleNo_, 'frozenSemenNo': frozenSemenNo_, 'variety': variety_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'cattleNo': cattleNo_, 'frozenSemenNo': frozenSemenNo_, 'variety': variety_}
        response = self.request.post(url=self.url+'/admin/bull/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/bull/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_bull_newBullNo(self, cattleFarmId_=None):
        if self.user is None:
            data = {'cattleFarmId': cattleFarmId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleFarmId': cattleFarmId_}
        response = self.request.post(url=self.url+'/admin/bull/newBullNo', data=data, hosts=self.url)
        apiTestResult(api='/admin/bull/newBullNo', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_add(self, cattleEarTagNo_=None, cattleFenceId_=None, variety_=None, gender_=None, birthday_=None, entryDate_=None, currentChildTime_=None, birthWeight_=None, feedType_=None, fatherNo_=None, motherNo_=None, rfidCode_=None, nucleusGroupStatus_=None, insureNo_=None, purchaseOrderNo_=None, skuCode_=None, usedNo_=None, pics_=None):
        if self.user is None:
            data = {'cattleEarTagNo': cattleEarTagNo_, 'cattleFenceId': cattleFenceId_, 'variety': variety_, 'gender': gender_, 'birthday': birthday_, 'entryDate': entryDate_, 'currentChildTime': currentChildTime_, 'birthWeight': birthWeight_, 'feedType': feedType_, 'fatherNo': fatherNo_, 'motherNo': motherNo_, 'rfidCode': rfidCode_, 'nucleusGroupStatus': nucleusGroupStatus_, 'insureNo': insureNo_, 'purchaseOrderNo': purchaseOrderNo_, 'skuCode': skuCode_, 'usedNo': usedNo_, 'pics': pics_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleEarTagNo': cattleEarTagNo_, 'cattleFenceId': cattleFenceId_, 'variety': variety_, 'gender': gender_, 'birthday': birthday_, 'entryDate': entryDate_, 'currentChildTime': currentChildTime_, 'birthWeight': birthWeight_, 'feedType': feedType_, 'fatherNo': fatherNo_, 'motherNo': motherNo_, 'rfidCode': rfidCode_, 'nucleusGroupStatus': nucleusGroupStatus_, 'insureNo': insureNo_, 'purchaseOrderNo': purchaseOrderNo_, 'skuCode': skuCode_, 'usedNo': usedNo_, 'pics': pics_}
        response = self.request.post(url=self.url+'/admin/cattle/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_allot_add(self, earTagNo_=None, inFarmId_=None, remark_=None):
        if self.user is None:
            data = {'earTagNo': earTagNo_, 'inFarmId': inFarmId_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'earTagNo': earTagNo_, 'inFarmId': inFarmId_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/cattle/allot/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle/allot/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_allot_apply(self, allotIds_=None):
        if self.user is None:
            data = {'allotIds': allotIds_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'allotIds': allotIds_}
        response = self.request.post(url=self.url+'/admin/cattle/allot/apply', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle/allot/apply', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_allot_cancel(self, allotIds_=None):
        if self.user is None:
            data = {'allotIds': allotIds_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'allotIds': allotIds_}
        response = self.request.post(url=self.url+'/admin/cattle/allot/cancel', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle/allot/cancel', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_allot_cattle_check(self, earTagNo_=None):
        if self.user is None:
            data = {'earTagNo': earTagNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'earTagNo': earTagNo_}
        response = self.request.post(url=self.url+'/admin/cattle/allot/cattle-check', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle/allot/cattle-check', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_allot_finish(self, allotIds_=None, cattleFenceId_=None):
        if self.user is None:
            data = {'allotIds': allotIds_, 'cattleFenceId': cattleFenceId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'allotIds': allotIds_, 'cattleFenceId': cattleFenceId_}
        response = self.request.post(url=self.url+'/admin/cattle/allot/finish', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle/allot/finish', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_allot_in_page_list(self, pn_=None, ps_=None, farmId_=None, earTagNo_=None, applyDate_=None, status_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'farmId': farmId_, 'earTagNo': earTagNo_, 'applyDate': applyDate_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'farmId': farmId_, 'earTagNo': earTagNo_, 'applyDate': applyDate_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/cattle/allot/in/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle/allot/in/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_allot_out_page_list(self, pn_=None, ps_=None, farmId_=None, earTagNo_=None, applyDate_=None, status_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'farmId': farmId_, 'earTagNo': earTagNo_, 'applyDate': applyDate_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'farmId': farmId_, 'earTagNo': earTagNo_, 'applyDate': applyDate_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/cattle/allot/out/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle/allot/out/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_allot_refuse(self, allotIds_=None):
        if self.user is None:
            data = {'allotIds': allotIds_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'allotIds': allotIds_}
        response = self.request.post(url=self.url+'/admin/cattle/allot/refuse', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle/allot/refuse', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_batch_add(self, purchaseOrderNo_=None, jsonStr_=None):
        if self.user is None:
            data = {'purchaseOrderNo': purchaseOrderNo_, 'jsonStr': jsonStr_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'purchaseOrderNo': purchaseOrderNo_, 'jsonStr': jsonStr_}
        response = self.request.post(url=self.url+'/admin/cattle/batch-add', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle/batch-add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_detail(self, cattleId_=None):
        if self.user is None:
            data = {'cattleId': cattleId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleId': cattleId_}
        response = self.request.post(url=self.url+'/admin/cattle/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_edit(self, id_=None, cattleFenceId_=None, variety_=None, gender_=None, birthday_=None, entryDate_=None, currentChildTime_=None, birthWeight_=None, feedType_=None, fatherNo_=None, motherNo_=None, nucleusGroupStatus_=None, insureNo_=None, pics_=None):
        if self.user is None:
            data = {'id': id_, 'cattleFenceId': cattleFenceId_, 'variety': variety_, 'gender': gender_, 'birthday': birthday_, 'entryDate': entryDate_, 'currentChildTime': currentChildTime_, 'birthWeight': birthWeight_, 'feedType': feedType_, 'fatherNo': fatherNo_, 'motherNo': motherNo_, 'nucleusGroupStatus': nucleusGroupStatus_, 'insureNo': insureNo_, 'pics': pics_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'cattleFenceId': cattleFenceId_, 'variety': variety_, 'gender': gender_, 'birthday': birthday_, 'entryDate': entryDate_, 'currentChildTime': currentChildTime_, 'birthWeight': birthWeight_, 'feedType': feedType_, 'fatherNo': fatherNo_, 'motherNo': motherNo_, 'nucleusGroupStatus': nucleusGroupStatus_, 'insureNo': insureNo_, 'pics': pics_}
        response = self.request.post(url=self.url+'/admin/cattle/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_list(self, pn_=None, ps_=None, cattleEarTagNo_=None, cowshedId_=None, cattleFenceId_=None, nucleusGroupStatus_=None, gender_=None, inGroupStatus_=None, variety_=None, currentChildTime_=None, startEntryDate_=None, endEntryDate_=None, startDepartureDate_=None, endDepartureDate_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleEarTagNo': cattleEarTagNo_, 'cowshedId': cowshedId_, 'cattleFenceId': cattleFenceId_, 'nucleusGroupStatus': nucleusGroupStatus_, 'gender': gender_, 'inGroupStatus': inGroupStatus_, 'variety': variety_, 'currentChildTime': currentChildTime_, 'startEntryDate': startEntryDate_, 'endEntryDate': endEntryDate_, 'startDepartureDate': startDepartureDate_, 'endDepartureDate': endDepartureDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleEarTagNo': cattleEarTagNo_, 'cowshedId': cowshedId_, 'cattleFenceId': cattleFenceId_, 'nucleusGroupStatus': nucleusGroupStatus_, 'gender': gender_, 'inGroupStatus': inGroupStatus_, 'variety': variety_, 'currentChildTime': currentChildTime_, 'startEntryDate': startEntryDate_, 'endEntryDate': endEntryDate_, 'startDepartureDate': startDepartureDate_, 'endDepartureDate': endDepartureDate_}
        response = self.request.post(url=self.url+'/admin/cattle/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleDeparture_add(self, cattleEarTagNo_=None, departureWay_=None, departureReason_=None, dispositon_=None, departureDate_=None, weight_=None, price_=None, accidentStatus_=None, remark_=None, pics_=None):
        if self.user is None:
            data = {'cattleEarTagNo': cattleEarTagNo_, 'departureWay': departureWay_, 'departureReason': departureReason_, 'dispositon': dispositon_, 'departureDate': departureDate_, 'weight': weight_, 'price': price_, 'accidentStatus': accidentStatus_, 'remark': remark_, 'pics': pics_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleEarTagNo': cattleEarTagNo_, 'departureWay': departureWay_, 'departureReason': departureReason_, 'dispositon': dispositon_, 'departureDate': departureDate_, 'weight': weight_, 'price': price_, 'accidentStatus': accidentStatus_, 'remark': remark_, 'pics': pics_}
        response = self.request.post(url=self.url+'/admin/cattleDeparture/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleDeparture/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleDeparture_batch_add(self, jsonStr_=None):
        if self.user is None:
            data = {'jsonStr': jsonStr_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'jsonStr': jsonStr_}
        response = self.request.post(url=self.url+'/admin/cattleDeparture/batch-add', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleDeparture/batch-add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleDeparture_detail(self, departureId_=None):
        if self.user is None:
            data = {'departureId': departureId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'departureId': departureId_}
        response = self.request.post(url=self.url+'/admin/cattleDeparture/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleDeparture/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleDeparture_edit(self, id_=None, departureWay_=None, departureReason_=None, dispositon_=None, departureDate_=None, weight_=None, price_=None, accidentStatus_=None, remark_=None, pics_=None):
        if self.user is None:
            data = {'id': id_, 'departureWay': departureWay_, 'departureReason': departureReason_, 'dispositon': dispositon_, 'departureDate': departureDate_, 'weight': weight_, 'price': price_, 'accidentStatus': accidentStatus_, 'remark': remark_, 'pics': pics_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'departureWay': departureWay_, 'departureReason': departureReason_, 'dispositon': dispositon_, 'departureDate': departureDate_, 'weight': weight_, 'price': price_, 'accidentStatus': accidentStatus_, 'remark': remark_, 'pics': pics_}
        response = self.request.post(url=self.url+'/admin/cattleDeparture/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleDeparture/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleDeparture_list(self, pn_=None, ps_=None, cattleNo_=None, departureWay_=None, status_=None, startDepartureDate_=None, endDepartureDate_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleNo': cattleNo_, 'departureWay': departureWay_, 'status': status_, 'startDepartureDate': startDepartureDate_, 'endDepartureDate': endDepartureDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleNo': cattleNo_, 'departureWay': departureWay_, 'status': status_, 'startDepartureDate': startDepartureDate_, 'endDepartureDate': endDepartureDate_}
        response = self.request.post(url=self.url+'/admin/cattleDeparture/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleDeparture/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleDeparture_revocation(self, departureId_=None):
        if self.user is None:
            data = {'departureId': departureId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'departureId': departureId_}
        response = self.request.post(url=self.url+'/admin/cattleDeparture/revocation', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleDeparture/revocation', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleDeviceChange_add(self, cattleId_=None, newCattleEarTagNo_=None, newRfidCode_=None):
        if self.user is None:
            data = {'cattleId': cattleId_, 'newCattleEarTagNo': newCattleEarTagNo_, 'newRfidCode': newRfidCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleId': cattleId_, 'newCattleEarTagNo': newCattleEarTagNo_, 'newRfidCode': newRfidCode_}
        response = self.request.post(url=self.url+'/admin/cattleDeviceChange/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleDeviceChange/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleDeviceChange_import_add(self, jsonStr_=None):
        if self.user is None:
            data = {'jsonStr': jsonStr_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'jsonStr': jsonStr_}
        response = self.request.post(url=self.url+'/admin/cattleDeviceChange/import-add', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleDeviceChange/import-add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleDeviceChange_list(self, pn_=None, ps_=None, cattleFarmId_=None, cattleNos_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'cattleNos': cattleNos_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'cattleNos': cattleNos_}
        response = self.request.post(url=self.url+'/admin/cattleDeviceChange/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleDeviceChange/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleFamilyTree_add(self, cattleEarTagNo_=None, gender_=None, fatherNo_=None, motherNo_=None):
        if self.user is None:
            data = {'cattleEarTagNo': cattleEarTagNo_, 'gender': gender_, 'fatherNo': fatherNo_, 'motherNo': motherNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleEarTagNo': cattleEarTagNo_, 'gender': gender_, 'fatherNo': fatherNo_, 'motherNo': motherNo_}
        response = self.request.post(url=self.url+'/admin/cattleFamilyTree/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleFamilyTree/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleFamilyTree_batch_add(self, jsonStr_=None):
        if self.user is None:
            data = {'jsonStr': jsonStr_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'jsonStr': jsonStr_}
        response = self.request.post(url=self.url+'/admin/cattleFamilyTree/batch-add', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleFamilyTree/batch-add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleFamilyTree_del(self, treeId_=None):
        if self.user is None:
            data = {'treeId': treeId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'treeId': treeId_}
        response = self.request.post(url=self.url+'/admin/cattleFamilyTree/del', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleFamilyTree/del', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleFamilyTree_detail(self, treeId_=None):
        if self.user is None:
            data = {'treeId': treeId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'treeId': treeId_}
        response = self.request.post(url=self.url+'/admin/cattleFamilyTree/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleFamilyTree/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleFamilyTree_edit(self, id_=None, gender_=None, fatherNo_=None, motherNo_=None):
        if self.user is None:
            data = {'id': id_, 'gender': gender_, 'fatherNo': fatherNo_, 'motherNo': motherNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'gender': gender_, 'fatherNo': fatherNo_, 'motherNo': motherNo_}
        response = self.request.post(url=self.url+'/admin/cattleFamilyTree/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleFamilyTree/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleFamilyTree_list(self, pn_=None, ps_=None, cattleEarTagNo_=None, gender_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleEarTagNo': cattleEarTagNo_, 'gender': gender_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleEarTagNo': cattleEarTagNo_, 'gender': gender_}
        response = self.request.post(url=self.url+'/admin/cattleFamilyTree/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleFamilyTree/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleFence_add(self, fenceNo_=None, fenceName_=None, cowshedId_=None, cattleFarmId_=None, type_=None, area_=None, epcNo_=None, remark_=None):
        if self.user is None:
            data = {'fenceNo': fenceNo_, 'fenceName': fenceName_, 'cowshedId': cowshedId_, 'cattleFarmId': cattleFarmId_, 'type': type_, 'area': area_, 'epcNo': epcNo_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'fenceNo': fenceNo_, 'fenceName': fenceName_, 'cowshedId': cowshedId_, 'cattleFarmId': cattleFarmId_, 'type': type_, 'area': area_, 'epcNo': epcNo_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/cattleFence/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleFence/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleFence_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/cattleFence/del', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleFence/del', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleFence_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/cattleFence/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleFence/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleFence_edit(self, id_=None, fenceName_=None, type_=None, area_=None, epcNo_=None, remark_=None):
        if self.user is None:
            data = {'id': id_, 'fenceName': fenceName_, 'type': type_, 'area': area_, 'epcNo': epcNo_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'fenceName': fenceName_, 'type': type_, 'area': area_, 'epcNo': epcNo_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/cattleFence/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleFence/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleFence_list(self, pn_=None, ps_=None, cattleFarmId_=None, fenceName_=None, fenceNo_=None, cowshedId_=None, cattleExistFilter_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'fenceName': fenceName_, 'fenceNo': fenceNo_, 'cowshedId': cowshedId_, 'cattleExistFilter': cattleExistFilter_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'fenceName': fenceName_, 'fenceNo': fenceNo_, 'cowshedId': cowshedId_, 'cattleExistFilter': cattleExistFilter_}
        response = self.request.post(url=self.url+'/admin/cattleFence/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleFence/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleFence_newFenceNo(self, cowshedId_=None, cattleFarmId_=None):
        if self.user is None:
            data = {'cowshedId': cowshedId_, 'cattleFarmId': cattleFarmId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cowshedId': cowshedId_, 'cattleFarmId': cattleFarmId_}
        response = self.request.post(url=self.url+'/admin/cattleFence/newFenceNo', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleFence/newFenceNo', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleGrowthRecord_add(self, cattleEarTagNoList_=None, measureStage_=None, weight_=None, height_=None, hipCrossHeight_=None, chestDepth_=None, chestWidth_=None, tajiriLong_=None, waistLegsWidth_=None, hipWidth_=None, backAround_=None, backThickness_=None, ischiumWidth_=None, bodyLength_=None, chestAround_=None, abdomenAround_=None, tubeAround_=None, testisAround_=None, eyeMuscleHeight_=None, qib_=None, eyeMuscleArea_=None, entiretyStructure_=None, beforeAfterDrive_=None, breastStructure_=None, limbHoof_=None, synthesisScore_=None, measureDate_=None, operator_=None, remark_=None):
        if self.user is None:
            data = {'cattleEarTagNoList': cattleEarTagNoList_, 'measureStage': measureStage_, 'weight': weight_, 'height': height_, 'hipCrossHeight': hipCrossHeight_, 'chestDepth': chestDepth_, 'chestWidth': chestWidth_, 'tajiriLong': tajiriLong_, 'waistLegsWidth': waistLegsWidth_, 'hipWidth': hipWidth_, 'backAround': backAround_, 'backThickness': backThickness_, 'ischiumWidth': ischiumWidth_, 'bodyLength': bodyLength_, 'chestAround': chestAround_, 'abdomenAround': abdomenAround_, 'tubeAround': tubeAround_, 'testisAround': testisAround_, 'eyeMuscleHeight': eyeMuscleHeight_, 'qib': qib_, 'eyeMuscleArea': eyeMuscleArea_, 'entiretyStructure': entiretyStructure_, 'beforeAfterDrive': beforeAfterDrive_, 'breastStructure': breastStructure_, 'limbHoof': limbHoof_, 'synthesisScore': synthesisScore_, 'measureDate': measureDate_, 'operator': operator_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleEarTagNoList': cattleEarTagNoList_, 'measureStage': measureStage_, 'weight': weight_, 'height': height_, 'hipCrossHeight': hipCrossHeight_, 'chestDepth': chestDepth_, 'chestWidth': chestWidth_, 'tajiriLong': tajiriLong_, 'waistLegsWidth': waistLegsWidth_, 'hipWidth': hipWidth_, 'backAround': backAround_, 'backThickness': backThickness_, 'ischiumWidth': ischiumWidth_, 'bodyLength': bodyLength_, 'chestAround': chestAround_, 'abdomenAround': abdomenAround_, 'tubeAround': tubeAround_, 'testisAround': testisAround_, 'eyeMuscleHeight': eyeMuscleHeight_, 'qib': qib_, 'eyeMuscleArea': eyeMuscleArea_, 'entiretyStructure': entiretyStructure_, 'beforeAfterDrive': beforeAfterDrive_, 'breastStructure': breastStructure_, 'limbHoof': limbHoof_, 'synthesisScore': synthesisScore_, 'measureDate': measureDate_, 'operator': operator_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/cattleGrowthRecord/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleGrowthRecord/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleGrowthRecord_batch_add(self, jsonStr_=None):
        if self.user is None:
            data = {'jsonStr': jsonStr_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'jsonStr': jsonStr_}
        response = self.request.post(url=self.url+'/admin/cattleGrowthRecord/batch-add', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleGrowthRecord/batch-add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleGrowthRecord_detail(self, recordId_=None):
        if self.user is None:
            data = {'recordId': recordId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'recordId': recordId_}
        response = self.request.post(url=self.url+'/admin/cattleGrowthRecord/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleGrowthRecord/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleGrowthRecord_edit(self, id_=None, measureStage_=None, weight_=None, height_=None, hipCrossHeight_=None, chestDepth_=None, chestWidth_=None, tajiriLong_=None, waistLegsWidth_=None, hipWidth_=None, backAround_=None, backThickness_=None, ischiumWidth_=None, bodyLength_=None, chestAround_=None, abdomenAround_=None, tubeAround_=None, testisAround_=None, eyeMuscleHeight_=None, qib_=None, eyeMuscleArea_=None, entiretyStructure_=None, beforeAfterDrive_=None, breastStructure_=None, limbHoof_=None, synthesisScore_=None, measureDate_=None, operator_=None, remark_=None):
        if self.user is None:
            data = {'id': id_, 'measureStage': measureStage_, 'weight': weight_, 'height': height_, 'hipCrossHeight': hipCrossHeight_, 'chestDepth': chestDepth_, 'chestWidth': chestWidth_, 'tajiriLong': tajiriLong_, 'waistLegsWidth': waistLegsWidth_, 'hipWidth': hipWidth_, 'backAround': backAround_, 'backThickness': backThickness_, 'ischiumWidth': ischiumWidth_, 'bodyLength': bodyLength_, 'chestAround': chestAround_, 'abdomenAround': abdomenAround_, 'tubeAround': tubeAround_, 'testisAround': testisAround_, 'eyeMuscleHeight': eyeMuscleHeight_, 'qib': qib_, 'eyeMuscleArea': eyeMuscleArea_, 'entiretyStructure': entiretyStructure_, 'beforeAfterDrive': beforeAfterDrive_, 'breastStructure': breastStructure_, 'limbHoof': limbHoof_, 'synthesisScore': synthesisScore_, 'measureDate': measureDate_, 'operator': operator_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'measureStage': measureStage_, 'weight': weight_, 'height': height_, 'hipCrossHeight': hipCrossHeight_, 'chestDepth': chestDepth_, 'chestWidth': chestWidth_, 'tajiriLong': tajiriLong_, 'waistLegsWidth': waistLegsWidth_, 'hipWidth': hipWidth_, 'backAround': backAround_, 'backThickness': backThickness_, 'ischiumWidth': ischiumWidth_, 'bodyLength': bodyLength_, 'chestAround': chestAround_, 'abdomenAround': abdomenAround_, 'tubeAround': tubeAround_, 'testisAround': testisAround_, 'eyeMuscleHeight': eyeMuscleHeight_, 'qib': qib_, 'eyeMuscleArea': eyeMuscleArea_, 'entiretyStructure': entiretyStructure_, 'beforeAfterDrive': beforeAfterDrive_, 'breastStructure': breastStructure_, 'limbHoof': limbHoof_, 'synthesisScore': synthesisScore_, 'measureDate': measureDate_, 'operator': operator_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/cattleGrowthRecord/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleGrowthRecord/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleGrowthRecord_list(self, pn_=None, ps_=None, cattleNo_=None, measureStage_=None, startMeasureDate_=None, endMeasureDate_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleNo': cattleNo_, 'measureStage': measureStage_, 'startMeasureDate': startMeasureDate_, 'endMeasureDate': endMeasureDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleNo': cattleNo_, 'measureStage': measureStage_, 'startMeasureDate': startMeasureDate_, 'endMeasureDate': endMeasureDate_}
        response = self.request.post(url=self.url+'/admin/cattleGrowthRecord/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleGrowthRecord/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleGrowthRecord_revocation(self, recordId_=None):
        if self.user is None:
            data = {'recordId': recordId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'recordId': recordId_}
        response = self.request.post(url=self.url+'/admin/cattleGrowthRecord/revocation', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleGrowthRecord/revocation', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleInGroup_cattle_list(self, fenceIds_=None):
        if self.user is None:
            data = {'fenceIds': fenceIds_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'fenceIds': fenceIds_}
        response = self.request.post(url=self.url+'/admin/cattleInGroup/cattle-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleInGroup/cattle-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleInGroup_list(self, cattleFarmId_=None):
        if self.user is None:
            data = {'cattleFarmId': cattleFarmId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleFarmId': cattleFarmId_}
        response = self.request.post(url=self.url+'/admin/cattleInGroup/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleInGroup/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cowshed_add(self, cowshedNo_=None, cowshedName_=None, cattleFarmId_=None, area_=None, epcNo_=None, remark_=None):
        if self.user is None:
            data = {'cowshedNo': cowshedNo_, 'cowshedName': cowshedName_, 'cattleFarmId': cattleFarmId_, 'area': area_, 'epcNo': epcNo_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cowshedNo': cowshedNo_, 'cowshedName': cowshedName_, 'cattleFarmId': cattleFarmId_, 'area': area_, 'epcNo': epcNo_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/cowshed/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/cowshed/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cowshed_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/cowshed/del', data=data, hosts=self.url)
        apiTestResult(api='/admin/cowshed/del', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cowshed_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/cowshed/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/cowshed/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cowshed_edit(self, id_=None, cowshedName_=None, area_=None, epcNo_=None, remark_=None):
        if self.user is None:
            data = {'id': id_, 'cowshedName': cowshedName_, 'area': area_, 'epcNo': epcNo_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'cowshedName': cowshedName_, 'area': area_, 'epcNo': epcNo_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/cowshed/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/cowshed/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cowshed_list(self, pn_=None, ps_=None, cattleFarmId_=None, cowshedName_=None, cowshedNo_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'cowshedName': cowshedName_, 'cowshedNo': cowshedNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'cowshedName': cowshedName_, 'cowshedNo': cowshedNo_}
        response = self.request.post(url=self.url+'/admin/cowshed/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/cowshed/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cowshed_newCowshedNo(self, cattleFarmId_=None):
        if self.user is None:
            data = {'cattleFarmId': cattleFarmId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleFarmId': cattleFarmId_}
        response = self.request.post(url=self.url+'/admin/cowshed/newCowshedNo', data=data, hosts=self.url)
        apiTestResult(api='/admin/cowshed/newCowshedNo', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_faecesSeparator_add(self, cattleFarmId_=None, fenceId_=None, makeDate_=None, upFloorRatio_=None, middleFloorRatio_=None, downFloorRatio_=None, fenceRemark_=None):
        if self.user is None:
            data = {'cattleFarmId': cattleFarmId_, 'fenceId': fenceId_, 'makeDate': makeDate_, 'upFloorRatio': upFloorRatio_, 'middleFloorRatio': middleFloorRatio_, 'downFloorRatio': downFloorRatio_, 'fenceRemark': fenceRemark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleFarmId': cattleFarmId_, 'fenceId': fenceId_, 'makeDate': makeDate_, 'upFloorRatio': upFloorRatio_, 'middleFloorRatio': middleFloorRatio_, 'downFloorRatio': downFloorRatio_, 'fenceRemark': fenceRemark_}
        response = self.request.post(url=self.url+'/admin/faecesSeparator/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/faecesSeparator/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_faecesSeparator_batch_add(self, cattleFarmId_=None, jsonString_=None):
        if self.user is None:
            data = {'cattleFarmId': cattleFarmId_, 'jsonString': jsonString_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleFarmId': cattleFarmId_, 'jsonString': jsonString_}
        response = self.request.post(url=self.url+'/admin/faecesSeparator/batch-add', data=data, hosts=self.url)
        apiTestResult(api='/admin/faecesSeparator/batch-add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_faecesSeparator_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/faecesSeparator/del', data=data, hosts=self.url)
        apiTestResult(api='/admin/faecesSeparator/del', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_faecesSeparator_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/faecesSeparator/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/faecesSeparator/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_faecesSeparator_edit(self, id_=None, fenceId_=None, makeDate_=None, upFloorRatio_=None, middleFloorRatio_=None, downFloorRatio_=None, fenceRemark_=None):
        if self.user is None:
            data = {'id': id_, 'fenceId': fenceId_, 'makeDate': makeDate_, 'upFloorRatio': upFloorRatio_, 'middleFloorRatio': middleFloorRatio_, 'downFloorRatio': downFloorRatio_, 'fenceRemark': fenceRemark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'fenceId': fenceId_, 'makeDate': makeDate_, 'upFloorRatio': upFloorRatio_, 'middleFloorRatio': middleFloorRatio_, 'downFloorRatio': downFloorRatio_, 'fenceRemark': fenceRemark_}
        response = self.request.post(url=self.url+'/admin/faecesSeparator/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/faecesSeparator/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_faecesSeparator_list(self, pn_=None, ps_=None, cattleFarmId_=None, fenceNo_=None, startMakeDate_=None, endMakeDate_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'fenceNo': fenceNo_, 'startMakeDate': startMakeDate_, 'endMakeDate': endMakeDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'fenceNo': fenceNo_, 'startMakeDate': startMakeDate_, 'endMakeDate': endMakeDate_}
        response = self.request.post(url=self.url+'/admin/faecesSeparator/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/faecesSeparator/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_feed_add(self, fenceId_=None, cattleFarmId_=None, feedDate_=None, fodderJson_=None):
        if self.user is None:
            data = {'fenceId': fenceId_, 'cattleFarmId': cattleFarmId_, 'feedDate': feedDate_, 'fodderJson': fodderJson_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'fenceId': fenceId_, 'cattleFarmId': cattleFarmId_, 'feedDate': feedDate_, 'fodderJson': fodderJson_}
        response = self.request.post(url=self.url+'/admin/feed/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/feed/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_feed_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/feed/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/feed/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_feed_list(self, pn_=None, ps_=None, cattleFarmId_=None, fenceNo_=None, startFeedDate_=None, endFeedDate_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'fenceNo': fenceNo_, 'startFeedDate': startFeedDate_, 'endFeedDate': endFeedDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'fenceNo': fenceNo_, 'startFeedDate': startFeedDate_, 'endFeedDate': endFeedDate_}
        response = self.request.post(url=self.url+'/admin/feed/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/feed/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_materials_inventory_detail(self, warehouseCode_=None, productCode_=None):
        if self.user is None:
            data = {'warehouseCode': warehouseCode_, 'productCode': productCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'warehouseCode': warehouseCode_, 'productCode': productCode_}
        response = self.request.post(url=self.url+'/admin/materials/inventory-detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/materials/inventory-detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_materials_inventory_list(self, pn_=None, ps_=None, warehouseCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'warehouseCode': warehouseCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'warehouseCode': warehouseCode_}
        response = self.request.post(url=self.url+'/admin/materials/inventory-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/materials/inventory-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_materials_warehouse_list(self, companyCode_=None):
        if self.user is None:
            data = {'companyCode': companyCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'companyCode': companyCode_}
        response = self.request.post(url=self.url+'/admin/materials/warehouse-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/materials/warehouse-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_pennStateSeparator_add(self, cattleFarmId_=None, fenceId_=None, makeDate_=None, dryMatterRatio_=None, waterRatio_=None, firstFloorRatio_=None, secondFloorRatio_=None, threeFloorRatio_=None, fourFloorRatio_=None, fenceRemark_=None):
        if self.user is None:
            data = {'cattleFarmId': cattleFarmId_, 'fenceId': fenceId_, 'makeDate': makeDate_, 'dryMatterRatio': dryMatterRatio_, 'waterRatio': waterRatio_, 'firstFloorRatio': firstFloorRatio_, 'secondFloorRatio': secondFloorRatio_, 'threeFloorRatio': threeFloorRatio_, 'fourFloorRatio': fourFloorRatio_, 'fenceRemark': fenceRemark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleFarmId': cattleFarmId_, 'fenceId': fenceId_, 'makeDate': makeDate_, 'dryMatterRatio': dryMatterRatio_, 'waterRatio': waterRatio_, 'firstFloorRatio': firstFloorRatio_, 'secondFloorRatio': secondFloorRatio_, 'threeFloorRatio': threeFloorRatio_, 'fourFloorRatio': fourFloorRatio_, 'fenceRemark': fenceRemark_}
        response = self.request.post(url=self.url+'/admin/pennStateSeparator/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/pennStateSeparator/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_pennStateSeparator_batch_add(self, cattleFarmId_=None, jsonString_=None):
        if self.user is None:
            data = {'cattleFarmId': cattleFarmId_, 'jsonString': jsonString_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleFarmId': cattleFarmId_, 'jsonString': jsonString_}
        response = self.request.post(url=self.url+'/admin/pennStateSeparator/batch-add', data=data, hosts=self.url)
        apiTestResult(api='/admin/pennStateSeparator/batch-add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_pennStateSeparator_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/pennStateSeparator/del', data=data, hosts=self.url)
        apiTestResult(api='/admin/pennStateSeparator/del', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_pennStateSeparator_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/pennStateSeparator/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/pennStateSeparator/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_pennStateSeparator_edit(self, id_=None, fenceId_=None, makeDate_=None, dryMatterRatio_=None, waterRatio_=None, firstFloorRatio_=None, secondFloorRatio_=None, threeFloorRatio_=None, fourFloorRatio_=None, fenceRemark_=None):
        if self.user is None:
            data = {'id': id_, 'fenceId': fenceId_, 'makeDate': makeDate_, 'dryMatterRatio': dryMatterRatio_, 'waterRatio': waterRatio_, 'firstFloorRatio': firstFloorRatio_, 'secondFloorRatio': secondFloorRatio_, 'threeFloorRatio': threeFloorRatio_, 'fourFloorRatio': fourFloorRatio_, 'fenceRemark': fenceRemark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'fenceId': fenceId_, 'makeDate': makeDate_, 'dryMatterRatio': dryMatterRatio_, 'waterRatio': waterRatio_, 'firstFloorRatio': firstFloorRatio_, 'secondFloorRatio': secondFloorRatio_, 'threeFloorRatio': threeFloorRatio_, 'fourFloorRatio': fourFloorRatio_, 'fenceRemark': fenceRemark_}
        response = self.request.post(url=self.url+'/admin/pennStateSeparator/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/pennStateSeparator/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_pennStateSeparator_list(self, pn_=None, ps_=None, cattleFarmId_=None, fenceNo_=None, startMakeDate_=None, endMakeDate_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'fenceNo': fenceNo_, 'startMakeDate': startMakeDate_, 'endMakeDate': endMakeDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'fenceNo': fenceNo_, 'startMakeDate': startMakeDate_, 'endMakeDate': endMakeDate_}
        response = self.request.post(url=self.url+'/admin/pennStateSeparator/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/pennStateSeparator/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_productCategoryMapping_init(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/productCategoryMapping/init', data=data, hosts=self.url)
        apiTestResult(api='/admin/productCategoryMapping/init', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_productCategoryMapping_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/productCategoryMapping/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/productCategoryMapping/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_productCategoryMapping_list_category_by_pcode(self, pcode_=None):
        if self.user is None:
            data = {'pcode': pcode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pcode': pcode_}
        response = self.request.post(url=self.url+'/admin/productCategoryMapping/list-category-by-pcode', data=data, hosts=self.url)
        apiTestResult(api='/admin/productCategoryMapping/list-category-by-pcode', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_statistics_cattle_qty(self, cattleFarmId_=None):
        if self.user is None:
            data = {'cattleFarmId': cattleFarmId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleFarmId': cattleFarmId_}
        response = self.request.post(url=self.url+'/admin/statistics/cattle-qty', data=data, hosts=self.url)
        apiTestResult(api='/admin/statistics/cattle-qty', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_statistics_weight_growth(self, cattleFarmId_=None):
        if self.user is None:
            data = {'cattleFarmId': cattleFarmId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleFarmId': cattleFarmId_}
        response = self.request.post(url=self.url+'/admin/statistics/weight-growth', data=data, hosts=self.url)
        apiTestResult(api='/admin/statistics/weight-growth', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_transferFence_add(self, cattleEarTagNoList_=None, inFenceId_=None, reason_=None, transferDate_=None, operator_=None, remark_=None):
        if self.user is None:
            data = {'cattleEarTagNoList': cattleEarTagNoList_, 'inFenceId': inFenceId_, 'reason': reason_, 'transferDate': transferDate_, 'operator': operator_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleEarTagNoList': cattleEarTagNoList_, 'inFenceId': inFenceId_, 'reason': reason_, 'transferDate': transferDate_, 'operator': operator_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/transferFence/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/transferFence/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_transferFence_batch_add(self, jsonStr_=None):
        if self.user is None:
            data = {'jsonStr': jsonStr_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'jsonStr': jsonStr_}
        response = self.request.post(url=self.url+'/admin/transferFence/batch-add', data=data, hosts=self.url)
        apiTestResult(api='/admin/transferFence/batch-add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_transferFence_detail(self, tfdId_=None):
        if self.user is None:
            data = {'tfdId': tfdId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'tfdId': tfdId_}
        response = self.request.post(url=self.url+'/admin/transferFence/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/transferFence/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_transferFence_list(self, pn_=None, ps_=None, cattleNo_=None, reasonType_=None, startTransferDate_=None, endTransferDate_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleNo': cattleNo_, 'reasonType': reasonType_, 'startTransferDate': startTransferDate_, 'endTransferDate': endTransferDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleNo': cattleNo_, 'reasonType': reasonType_, 'startTransferDate': startTransferDate_, 'endTransferDate': endTransferDate_}
        response = self.request.post(url=self.url+'/admin/transferFence/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/transferFence/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _config_common_get_all_enum_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/config/common/get-all-enum-list', data=data, hosts=self.url)
        apiTestResult(api='/config/common/get-all-enum-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _config_common_get_config_list(self, types_=None, code_=None):
        if self.user is None:
            data = {'types': types_, 'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'types': types_, 'code': code_}
        response = self.request.post(url=self.url+'/config/common/get-config-list', data=data, hosts=self.url)
        apiTestResult(api='/config/common/get-config-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_bizAttach_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/bizAttach/get', data=data, hosts=self.url)
        apiTestResult(api='/mobile/bizAttach/get', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattle_add(self, cattleEarTagNo_=None, cattleFenceId_=None, variety_=None, gender_=None, birthday_=None, entryDate_=None, currentChildTime_=None, birthWeight_=None, feedType_=None, fatherNo_=None, motherNo_=None, rfidCode_=None, nucleusGroupStatus_=None, insureNo_=None, purchaseOrderNo_=None, skuCode_=None, usedNo_=None, pics_=None):
        if self.user is None:
            data = {'cattleEarTagNo': cattleEarTagNo_, 'cattleFenceId': cattleFenceId_, 'variety': variety_, 'gender': gender_, 'birthday': birthday_, 'entryDate': entryDate_, 'currentChildTime': currentChildTime_, 'birthWeight': birthWeight_, 'feedType': feedType_, 'fatherNo': fatherNo_, 'motherNo': motherNo_, 'rfidCode': rfidCode_, 'nucleusGroupStatus': nucleusGroupStatus_, 'insureNo': insureNo_, 'purchaseOrderNo': purchaseOrderNo_, 'skuCode': skuCode_, 'usedNo': usedNo_, 'pics': pics_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleEarTagNo': cattleEarTagNo_, 'cattleFenceId': cattleFenceId_, 'variety': variety_, 'gender': gender_, 'birthday': birthday_, 'entryDate': entryDate_, 'currentChildTime': currentChildTime_, 'birthWeight': birthWeight_, 'feedType': feedType_, 'fatherNo': fatherNo_, 'motherNo': motherNo_, 'rfidCode': rfidCode_, 'nucleusGroupStatus': nucleusGroupStatus_, 'insureNo': insureNo_, 'purchaseOrderNo': purchaseOrderNo_, 'skuCode': skuCode_, 'usedNo': usedNo_, 'pics': pics_}
        response = self.request.post(url=self.url+'/mobile/cattle/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattle/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattle_detail(self, cattleId_=None):
        if self.user is None:
            data = {'cattleId': cattleId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleId': cattleId_}
        response = self.request.post(url=self.url+'/mobile/cattle/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattle/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattle_edit(self, id_=None, cattleFenceId_=None, variety_=None, gender_=None, birthday_=None, entryDate_=None, currentChildTime_=None, birthWeight_=None, feedType_=None, fatherNo_=None, motherNo_=None, nucleusGroupStatus_=None, insureNo_=None, pics_=None):
        if self.user is None:
            data = {'id': id_, 'cattleFenceId': cattleFenceId_, 'variety': variety_, 'gender': gender_, 'birthday': birthday_, 'entryDate': entryDate_, 'currentChildTime': currentChildTime_, 'birthWeight': birthWeight_, 'feedType': feedType_, 'fatherNo': fatherNo_, 'motherNo': motherNo_, 'nucleusGroupStatus': nucleusGroupStatus_, 'insureNo': insureNo_, 'pics': pics_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'cattleFenceId': cattleFenceId_, 'variety': variety_, 'gender': gender_, 'birthday': birthday_, 'entryDate': entryDate_, 'currentChildTime': currentChildTime_, 'birthWeight': birthWeight_, 'feedType': feedType_, 'fatherNo': fatherNo_, 'motherNo': motherNo_, 'nucleusGroupStatus': nucleusGroupStatus_, 'insureNo': insureNo_, 'pics': pics_}
        response = self.request.post(url=self.url+'/mobile/cattle/edit', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattle/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattle_list(self, pn_=None, ps_=None, cattleEarTagNo_=None, cowshedId_=None, cattleFenceId_=None, nucleusGroupStatus_=None, gender_=None, inGroupStatus_=None, variety_=None, currentChildTime_=None, startEntryDate_=None, endEntryDate_=None, startDepartureDate_=None, endDepartureDate_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleEarTagNo': cattleEarTagNo_, 'cowshedId': cowshedId_, 'cattleFenceId': cattleFenceId_, 'nucleusGroupStatus': nucleusGroupStatus_, 'gender': gender_, 'inGroupStatus': inGroupStatus_, 'variety': variety_, 'currentChildTime': currentChildTime_, 'startEntryDate': startEntryDate_, 'endEntryDate': endEntryDate_, 'startDepartureDate': startDepartureDate_, 'endDepartureDate': endDepartureDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleEarTagNo': cattleEarTagNo_, 'cowshedId': cowshedId_, 'cattleFenceId': cattleFenceId_, 'nucleusGroupStatus': nucleusGroupStatus_, 'gender': gender_, 'inGroupStatus': inGroupStatus_, 'variety': variety_, 'currentChildTime': currentChildTime_, 'startEntryDate': startEntryDate_, 'endEntryDate': endEntryDate_, 'startDepartureDate': startDepartureDate_, 'endDepartureDate': endDepartureDate_}
        response = self.request.post(url=self.url+'/mobile/cattle/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattle/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleAllot_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/cattleAllot/get', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleAllot/get', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleAllotBatch_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/cattleAllotBatch/get', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleAllotBatch/get', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleDeparture_add(self, cattleEarTagNo_=None, departureWay_=None, departureReason_=None, dispositon_=None, departureDate_=None, weight_=None, price_=None, accidentStatus_=None, remark_=None, pics_=None):
        if self.user is None:
            data = {'cattleEarTagNo': cattleEarTagNo_, 'departureWay': departureWay_, 'departureReason': departureReason_, 'dispositon': dispositon_, 'departureDate': departureDate_, 'weight': weight_, 'price': price_, 'accidentStatus': accidentStatus_, 'remark': remark_, 'pics': pics_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleEarTagNo': cattleEarTagNo_, 'departureWay': departureWay_, 'departureReason': departureReason_, 'dispositon': dispositon_, 'departureDate': departureDate_, 'weight': weight_, 'price': price_, 'accidentStatus': accidentStatus_, 'remark': remark_, 'pics': pics_}
        response = self.request.post(url=self.url+'/mobile/cattleDeparture/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleDeparture/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleDeparture_detail(self, departureId_=None):
        if self.user is None:
            data = {'departureId': departureId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'departureId': departureId_}
        response = self.request.post(url=self.url+'/mobile/cattleDeparture/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleDeparture/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleDeparture_edit(self, id_=None, departureWay_=None, departureReason_=None, dispositon_=None, departureDate_=None, weight_=None, price_=None, accidentStatus_=None, remark_=None, pics_=None):
        if self.user is None:
            data = {'id': id_, 'departureWay': departureWay_, 'departureReason': departureReason_, 'dispositon': dispositon_, 'departureDate': departureDate_, 'weight': weight_, 'price': price_, 'accidentStatus': accidentStatus_, 'remark': remark_, 'pics': pics_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'departureWay': departureWay_, 'departureReason': departureReason_, 'dispositon': dispositon_, 'departureDate': departureDate_, 'weight': weight_, 'price': price_, 'accidentStatus': accidentStatus_, 'remark': remark_, 'pics': pics_}
        response = self.request.post(url=self.url+'/mobile/cattleDeparture/edit', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleDeparture/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleDeparture_list(self, pn_=None, ps_=None, cattleNo_=None, departureWay_=None, status_=None, startDepartureDate_=None, endDepartureDate_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleNo': cattleNo_, 'departureWay': departureWay_, 'status': status_, 'startDepartureDate': startDepartureDate_, 'endDepartureDate': endDepartureDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleNo': cattleNo_, 'departureWay': departureWay_, 'status': status_, 'startDepartureDate': startDepartureDate_, 'endDepartureDate': endDepartureDate_}
        response = self.request.post(url=self.url+'/mobile/cattleDeparture/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleDeparture/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleDeparture_revocation(self, departureId_=None):
        if self.user is None:
            data = {'departureId': departureId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'departureId': departureId_}
        response = self.request.post(url=self.url+'/mobile/cattleDeparture/revocation', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleDeparture/revocation', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleDeviceChange_add(self, cattleId_=None, newCattleEarTagNo_=None, newRfidCode_=None):
        if self.user is None:
            data = {'cattleId': cattleId_, 'newCattleEarTagNo': newCattleEarTagNo_, 'newRfidCode': newRfidCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleId': cattleId_, 'newCattleEarTagNo': newCattleEarTagNo_, 'newRfidCode': newRfidCode_}
        response = self.request.post(url=self.url+'/mobile/cattleDeviceChange/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleDeviceChange/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleDeviceChange_list(self, pn_=None, ps_=None, cattleFarmId_=None, cattleNos_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'cattleNos': cattleNos_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'cattleNos': cattleNos_}
        response = self.request.post(url=self.url+'/mobile/cattleDeviceChange/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleDeviceChange/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleFamilyTree_add(self, cattleEarTagNo_=None, gender_=None, fatherNo_=None, motherNo_=None):
        if self.user is None:
            data = {'cattleEarTagNo': cattleEarTagNo_, 'gender': gender_, 'fatherNo': fatherNo_, 'motherNo': motherNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleEarTagNo': cattleEarTagNo_, 'gender': gender_, 'fatherNo': fatherNo_, 'motherNo': motherNo_}
        response = self.request.post(url=self.url+'/mobile/cattleFamilyTree/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleFamilyTree/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleFamilyTree_del(self, treeId_=None):
        if self.user is None:
            data = {'treeId': treeId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'treeId': treeId_}
        response = self.request.post(url=self.url+'/mobile/cattleFamilyTree/del', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleFamilyTree/del', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleFamilyTree_detail(self, treeId_=None):
        if self.user is None:
            data = {'treeId': treeId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'treeId': treeId_}
        response = self.request.post(url=self.url+'/mobile/cattleFamilyTree/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleFamilyTree/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleFamilyTree_edit(self, id_=None, gender_=None, fatherNo_=None, motherNo_=None):
        if self.user is None:
            data = {'id': id_, 'gender': gender_, 'fatherNo': fatherNo_, 'motherNo': motherNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'gender': gender_, 'fatherNo': fatherNo_, 'motherNo': motherNo_}
        response = self.request.post(url=self.url+'/mobile/cattleFamilyTree/edit', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleFamilyTree/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleFamilyTree_list(self, pn_=None, ps_=None, cattleEarTagNo_=None, gender_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleEarTagNo': cattleEarTagNo_, 'gender': gender_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleEarTagNo': cattleEarTagNo_, 'gender': gender_}
        response = self.request.post(url=self.url+'/mobile/cattleFamilyTree/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleFamilyTree/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleFence_detail(self, pn_=None, ps_=None, id_=None, cattleNo_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'id': id_, 'cattleNo': cattleNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'id': id_, 'cattleNo': cattleNo_}
        response = self.request.post(url=self.url+'/mobile/cattleFence/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleFence/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleFence_list(self, pn_=None, ps_=None, cattleFarmId_=None, fenceName_=None, cattleNo_=None, cattleExistFilter_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'fenceName': fenceName_, 'cattleNo': cattleNo_, 'cattleExistFilter': cattleExistFilter_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'fenceName': fenceName_, 'cattleNo': cattleNo_, 'cattleExistFilter': cattleExistFilter_}
        response = self.request.post(url=self.url+'/mobile/cattleFence/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleFence/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleGrowthRecord_add(self, cattleEarTagNoList_=None, measureStage_=None, weight_=None, height_=None, hipCrossHeight_=None, chestDepth_=None, chestWidth_=None, tajiriLong_=None, waistLegsWidth_=None, hipWidth_=None, backAround_=None, backThickness_=None, ischiumWidth_=None, bodyLength_=None, chestAround_=None, abdomenAround_=None, tubeAround_=None, testisAround_=None, eyeMuscleHeight_=None, qib_=None, eyeMuscleArea_=None, entiretyStructure_=None, beforeAfterDrive_=None, breastStructure_=None, limbHoof_=None, synthesisScore_=None, measureDate_=None, operator_=None, remark_=None):
        if self.user is None:
            data = {'cattleEarTagNoList': cattleEarTagNoList_, 'measureStage': measureStage_, 'weight': weight_, 'height': height_, 'hipCrossHeight': hipCrossHeight_, 'chestDepth': chestDepth_, 'chestWidth': chestWidth_, 'tajiriLong': tajiriLong_, 'waistLegsWidth': waistLegsWidth_, 'hipWidth': hipWidth_, 'backAround': backAround_, 'backThickness': backThickness_, 'ischiumWidth': ischiumWidth_, 'bodyLength': bodyLength_, 'chestAround': chestAround_, 'abdomenAround': abdomenAround_, 'tubeAround': tubeAround_, 'testisAround': testisAround_, 'eyeMuscleHeight': eyeMuscleHeight_, 'qib': qib_, 'eyeMuscleArea': eyeMuscleArea_, 'entiretyStructure': entiretyStructure_, 'beforeAfterDrive': beforeAfterDrive_, 'breastStructure': breastStructure_, 'limbHoof': limbHoof_, 'synthesisScore': synthesisScore_, 'measureDate': measureDate_, 'operator': operator_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleEarTagNoList': cattleEarTagNoList_, 'measureStage': measureStage_, 'weight': weight_, 'height': height_, 'hipCrossHeight': hipCrossHeight_, 'chestDepth': chestDepth_, 'chestWidth': chestWidth_, 'tajiriLong': tajiriLong_, 'waistLegsWidth': waistLegsWidth_, 'hipWidth': hipWidth_, 'backAround': backAround_, 'backThickness': backThickness_, 'ischiumWidth': ischiumWidth_, 'bodyLength': bodyLength_, 'chestAround': chestAround_, 'abdomenAround': abdomenAround_, 'tubeAround': tubeAround_, 'testisAround': testisAround_, 'eyeMuscleHeight': eyeMuscleHeight_, 'qib': qib_, 'eyeMuscleArea': eyeMuscleArea_, 'entiretyStructure': entiretyStructure_, 'beforeAfterDrive': beforeAfterDrive_, 'breastStructure': breastStructure_, 'limbHoof': limbHoof_, 'synthesisScore': synthesisScore_, 'measureDate': measureDate_, 'operator': operator_, 'remark': remark_}
        response = self.request.post(url=self.url+'/mobile/cattleGrowthRecord/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleGrowthRecord/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleGrowthRecord_detail(self, recordId_=None):
        if self.user is None:
            data = {'recordId': recordId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'recordId': recordId_}
        response = self.request.post(url=self.url+'/mobile/cattleGrowthRecord/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleGrowthRecord/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleGrowthRecord_edit(self, id_=None, measureStage_=None, weight_=None, height_=None, hipCrossHeight_=None, chestDepth_=None, chestWidth_=None, tajiriLong_=None, waistLegsWidth_=None, hipWidth_=None, backAround_=None, backThickness_=None, ischiumWidth_=None, bodyLength_=None, chestAround_=None, abdomenAround_=None, tubeAround_=None, testisAround_=None, eyeMuscleHeight_=None, qib_=None, eyeMuscleArea_=None, entiretyStructure_=None, beforeAfterDrive_=None, breastStructure_=None, limbHoof_=None, synthesisScore_=None, measureDate_=None, operator_=None, remark_=None):
        if self.user is None:
            data = {'id': id_, 'measureStage': measureStage_, 'weight': weight_, 'height': height_, 'hipCrossHeight': hipCrossHeight_, 'chestDepth': chestDepth_, 'chestWidth': chestWidth_, 'tajiriLong': tajiriLong_, 'waistLegsWidth': waistLegsWidth_, 'hipWidth': hipWidth_, 'backAround': backAround_, 'backThickness': backThickness_, 'ischiumWidth': ischiumWidth_, 'bodyLength': bodyLength_, 'chestAround': chestAround_, 'abdomenAround': abdomenAround_, 'tubeAround': tubeAround_, 'testisAround': testisAround_, 'eyeMuscleHeight': eyeMuscleHeight_, 'qib': qib_, 'eyeMuscleArea': eyeMuscleArea_, 'entiretyStructure': entiretyStructure_, 'beforeAfterDrive': beforeAfterDrive_, 'breastStructure': breastStructure_, 'limbHoof': limbHoof_, 'synthesisScore': synthesisScore_, 'measureDate': measureDate_, 'operator': operator_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'measureStage': measureStage_, 'weight': weight_, 'height': height_, 'hipCrossHeight': hipCrossHeight_, 'chestDepth': chestDepth_, 'chestWidth': chestWidth_, 'tajiriLong': tajiriLong_, 'waistLegsWidth': waistLegsWidth_, 'hipWidth': hipWidth_, 'backAround': backAround_, 'backThickness': backThickness_, 'ischiumWidth': ischiumWidth_, 'bodyLength': bodyLength_, 'chestAround': chestAround_, 'abdomenAround': abdomenAround_, 'tubeAround': tubeAround_, 'testisAround': testisAround_, 'eyeMuscleHeight': eyeMuscleHeight_, 'qib': qib_, 'eyeMuscleArea': eyeMuscleArea_, 'entiretyStructure': entiretyStructure_, 'beforeAfterDrive': beforeAfterDrive_, 'breastStructure': breastStructure_, 'limbHoof': limbHoof_, 'synthesisScore': synthesisScore_, 'measureDate': measureDate_, 'operator': operator_, 'remark': remark_}
        response = self.request.post(url=self.url+'/mobile/cattleGrowthRecord/edit', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleGrowthRecord/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleGrowthRecord_list(self, pn_=None, ps_=None, cattleNo_=None, measureStage_=None, startMeasureDate_=None, endMeasureDate_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleNo': cattleNo_, 'measureStage': measureStage_, 'startMeasureDate': startMeasureDate_, 'endMeasureDate': endMeasureDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleNo': cattleNo_, 'measureStage': measureStage_, 'startMeasureDate': startMeasureDate_, 'endMeasureDate': endMeasureDate_}
        response = self.request.post(url=self.url+'/mobile/cattleGrowthRecord/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleGrowthRecord/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleGrowthRecord_revocation(self, recordId_=None):
        if self.user is None:
            data = {'recordId': recordId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'recordId': recordId_}
        response = self.request.post(url=self.url+'/mobile/cattleGrowthRecord/revocation', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleGrowthRecord/revocation', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattleReceive_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/cattleReceive/get', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattleReceive/get', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_feed_add(self, fenceId_=None, cattleFarmId_=None, feedDate_=None, fodderJson_=None):
        if self.user is None:
            data = {'fenceId': fenceId_, 'cattleFarmId': cattleFarmId_, 'feedDate': feedDate_, 'fodderJson': fodderJson_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'fenceId': fenceId_, 'cattleFarmId': cattleFarmId_, 'feedDate': feedDate_, 'fodderJson': fodderJson_}
        response = self.request.post(url=self.url+'/mobile/feed/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/feed/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_feed_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/feed/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/feed/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_feed_list(self, pn_=None, ps_=None, cattleFarmId_=None, fenceNo_=None, startFeedDate_=None, endFeedDate_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'fenceNo': fenceNo_, 'startFeedDate': startFeedDate_, 'endFeedDate': endFeedDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleFarmId': cattleFarmId_, 'fenceNo': fenceNo_, 'startFeedDate': startFeedDate_, 'endFeedDate': endFeedDate_}
        response = self.request.post(url=self.url+'/mobile/feed/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/feed/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_materials_inventory_list(self, pn_=None, ps_=None, warehouseCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'warehouseCode': warehouseCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'warehouseCode': warehouseCode_}
        response = self.request.post(url=self.url+'/mobile/materials/inventory-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/materials/inventory-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_materials_warehouse_list(self, companyCode_=None):
        if self.user is None:
            data = {'companyCode': companyCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'companyCode': companyCode_}
        response = self.request.post(url=self.url+'/mobile/materials/warehouse-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/materials/warehouse-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_statistics_cattle_qty(self, cattleFarmId_=None):
        if self.user is None:
            data = {'cattleFarmId': cattleFarmId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleFarmId': cattleFarmId_}
        response = self.request.post(url=self.url+'/mobile/statistics/cattle-qty', data=data, hosts=self.url)
        apiTestResult(api='/mobile/statistics/cattle-qty', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_statistics_weight_growth(self, cattleFarmId_=None):
        if self.user is None:
            data = {'cattleFarmId': cattleFarmId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleFarmId': cattleFarmId_}
        response = self.request.post(url=self.url+'/mobile/statistics/weight-growth', data=data, hosts=self.url)
        apiTestResult(api='/mobile/statistics/weight-growth', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_transferFence_add(self, cattleEarTagNoList_=None, inFenceId_=None, reason_=None, transferDate_=None, operator_=None, remark_=None):
        if self.user is None:
            data = {'cattleEarTagNoList': cattleEarTagNoList_, 'inFenceId': inFenceId_, 'reason': reason_, 'transferDate': transferDate_, 'operator': operator_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleEarTagNoList': cattleEarTagNoList_, 'inFenceId': inFenceId_, 'reason': reason_, 'transferDate': transferDate_, 'operator': operator_, 'remark': remark_}
        response = self.request.post(url=self.url+'/mobile/transferFence/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/transferFence/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_transferFence_detail(self, tfdId_=None):
        if self.user is None:
            data = {'tfdId': tfdId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'tfdId': tfdId_}
        response = self.request.post(url=self.url+'/mobile/transferFence/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/transferFence/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_transferFence_list(self, pn_=None, ps_=None, cattleNo_=None, reasonType_=None, startTransferDate_=None, endTransferDate_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'cattleNo': cattleNo_, 'reasonType': reasonType_, 'startTransferDate': startTransferDate_, 'endTransferDate': endTransferDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'cattleNo': cattleNo_, 'reasonType': reasonType_, 'startTransferDate': startTransferDate_, 'endTransferDate': endTransferDate_}
        response = self.request.post(url=self.url+'/mobile/transferFence/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/transferFence/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))
