#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
from utils.checkApiChanges.checher.apiTestResult import apiTestResult
import json


class plantAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('BF_PLANT')

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

    def _mobile_apply_add(self, details_=None, expectUseTime_=None, remark_=None, subjectId_=None, warehouseCode_=None):
        if self.user is None:
            data = {'details': details_, 'expectUseTime': expectUseTime_, 'remark': remark_, 'subjectId': subjectId_, 'warehouseCode': warehouseCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'details': details_, 'expectUseTime': expectUseTime_, 'remark': remark_, 'subjectId': subjectId_, 'warehouseCode': warehouseCode_}
        response = self.request.post(url=self.url+'/mobile/apply/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/apply/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_get_materiel_stock(self, materielCode_=None, warehouseCode_=None):
        if self.user is None:
            data = {'materielCode': materielCode_, 'warehouseCode': warehouseCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'materielCode': materielCode_, 'warehouseCode': warehouseCode_}
        response = self.request.post(url=self.url+'/mobile/apply/get-materiel-stock', data=data, hosts=self.url)
        apiTestResult(api='/mobile/apply/get-materiel-stock', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_list_materiel_by_type(self, code_=None, type_=None, name_=None):
        if self.user is None:
            data = {'code': code_, 'type': type_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'type': type_, 'name': name_}
        response = self.request.post(url=self.url+'/mobile/apply/list-materiel-by-type', data=data, hosts=self.url)
        apiTestResult(api='/mobile/apply/list-materiel-by-type', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_list_materiel_type(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/apply/list-materiel-type', data=data, hosts=self.url)
        apiTestResult(api='/mobile/apply/list-materiel-type', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_list_sub_materiel_type(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/mobile/apply/list-sub-materiel-type', data=data, hosts=self.url)
        apiTestResult(api='/mobile/apply/list-sub-materiel-type', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_list_subject(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/apply/list-subject', data=data, hosts=self.url)
        apiTestResult(api='/mobile/apply/list-subject', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_list_warehouse(self, name_=None, subjectId_=None, lat_=None, lng_=None):
        if self.user is None:
            data = {'name': name_, 'subjectId': subjectId_, 'lat': lat_, 'lng': lng_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'subjectId': subjectId_, 'lat': lat_, 'lng': lng_}
        response = self.request.post(url=self.url+'/mobile/apply/list-warehouse', data=data, hosts=self.url)
        apiTestResult(api='/mobile/apply/list-warehouse', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_page_materiel_by_type(self, pn_=None, ps_=None, code_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_, 'name': name_}
        response = self.request.post(url=self.url+'/mobile/apply/page-materiel-by-type', data=data, hosts=self.url)
        apiTestResult(api='/mobile/apply/page-materiel-by-type', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_dict_list(self, dictCode_=None):
        if self.user is None:
            data = {'dictCode': dictCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'dictCode': dictCode_}
        response = self.request.post(url=self.url+'/mobile/dict/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/dict/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_file_upload(self, file_=None):
        if self.user is None:
            data = {'file': file_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'file': file_}
        response = self.request.post(url=self.url+'/mobile/file/upload', data=data, hosts=self.url)
        apiTestResult(api='/mobile/file/upload', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_add(self, landName_=None, transferLandIds_=None, area_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, master_=None, remark_=None, urls_=None):
        if self.user is None:
            data = {'landName': landName_, 'transferLandIds': transferLandIds_, 'area': area_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'master': master_, 'remark': remark_, 'urls': urls_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'landName': landName_, 'transferLandIds': transferLandIds_, 'area': area_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'master': master_, 'remark': remark_, 'urls': urls_}
        response = self.request.post(url=self.url+'/mobile/land/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_delete(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/land/delete', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/delete', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_edit(self, landName_=None, transferLandIds_=None, area_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, master_=None, remark_=None, urls_=None, id_=None):
        if self.user is None:
            data = {'landName': landName_, 'transferLandIds': transferLandIds_, 'area': area_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'master': master_, 'remark': remark_, 'urls': urls_, 'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'landName': landName_, 'transferLandIds': transferLandIds_, 'area': area_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'master': master_, 'remark': remark_, 'urls': urls_, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/land/edit', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_list_transfer(self, province_=None, city_=None, county_=None, landUse_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'province': province_, 'city': city_, 'county': county_, 'landUse': landUse_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'province': province_, 'city': city_, 'county': county_, 'landUse': landUse_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/mobile/land/list-transfer', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/list-transfer', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_overView(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/land/overView', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/overView', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_page_list(self, pn_=None, ps_=None, lng_=None, lat_=None, searchLandName_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'lng': lng_, 'lat': lat_, 'searchLandName': searchLandName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'lng': lng_, 'lat': lat_, 'searchLandName': searchLandName_}
        response = self.request.post(url=self.url+'/mobile/land/page-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_plant_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/land/plant-detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/plant-detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_search_list(self, province_=None, city_=None, county_=None, plantStatuses_=None, plantKeys_=None):
        if self.user is None:
            data = {'province': province_, 'city': city_, 'county': county_, 'plantStatuses': plantStatuses_, 'plantKeys': plantKeys_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'province': province_, 'city': city_, 'county': county_, 'plantStatuses': plantStatuses_, 'plantKeys': plantKeys_}
        response = self.request.post(url=self.url+'/mobile/land/search-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/search-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_search_page(self, pn_=None, ps_=None, province_=None, city_=None, county_=None, plantStatuses_=None, plantKeys_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'plantStatuses': plantStatuses_, 'plantKeys': plantKeys_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'plantStatuses': plantStatuses_, 'plantKeys': plantKeys_}
        response = self.request.post(url=self.url+'/mobile/land/search-page', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/search-page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_plant_task_add(self, address_=None, area_=None, attachPic_=None, city_=None, county_=None, drugsInput_=None, fertilInput_=None, landId_=None, lat_=None, lng_=None, price_=None, province_=None, reapInput_=None, remark_=None, sowInput_=None, taskDate_=None, taskType_=None, workerNumber_=None):
        if self.user is None:
            data = {'address': address_, 'area': area_, 'attachPic': attachPic_, 'city': city_, 'county': county_, 'drugsInput': drugsInput_, 'fertilInput': fertilInput_, 'landId': landId_, 'lat': lat_, 'lng': lng_, 'price': price_, 'province': province_, 'reapInput': reapInput_, 'remark': remark_, 'sowInput': sowInput_, 'taskDate': taskDate_, 'taskType': taskType_, 'workerNumber': workerNumber_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'address': address_, 'area': area_, 'attachPic': attachPic_, 'city': city_, 'county': county_, 'drugsInput': drugsInput_, 'fertilInput': fertilInput_, 'landId': landId_, 'lat': lat_, 'lng': lng_, 'price': price_, 'province': province_, 'reapInput': reapInput_, 'remark': remark_, 'sowInput': sowInput_, 'taskDate': taskDate_, 'taskType': taskType_, 'workerNumber': workerNumber_}
        response = self.request.post(url=self.url+'/mobile/plant-task/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/plant-task/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_plant_task_detail(self, taskNo_=None):
        if self.user is None:
            data = {'taskNo': taskNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'taskNo': taskNo_}
        response = self.request.post(url=self.url+'/mobile/plant-task/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/plant-task/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_plant_task_edit(self, address_=None, area_=None, attachPic_=None, city_=None, county_=None, drugsInput_=None, fertilInput_=None, landId_=None, lat_=None, lng_=None, price_=None, province_=None, reapInput_=None, remark_=None, sowInput_=None, taskDate_=None, taskNo_=None, taskType_=None, workerNumber_=None):
        if self.user is None:
            data = {'address': address_, 'area': area_, 'attachPic': attachPic_, 'city': city_, 'county': county_, 'drugsInput': drugsInput_, 'fertilInput': fertilInput_, 'landId': landId_, 'lat': lat_, 'lng': lng_, 'price': price_, 'province': province_, 'reapInput': reapInput_, 'remark': remark_, 'sowInput': sowInput_, 'taskDate': taskDate_, 'taskNo': taskNo_, 'taskType': taskType_, 'workerNumber': workerNumber_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'address': address_, 'area': area_, 'attachPic': attachPic_, 'city': city_, 'county': county_, 'drugsInput': drugsInput_, 'fertilInput': fertilInput_, 'landId': landId_, 'lat': lat_, 'lng': lng_, 'price': price_, 'province': province_, 'reapInput': reapInput_, 'remark': remark_, 'sowInput': sowInput_, 'taskDate': taskDate_, 'taskNo': taskNo_, 'taskType': taskType_, 'workerNumber': workerNumber_}
        response = self.request.post(url=self.url+'/mobile/plant-task/edit', data=data, hosts=self.url)
        apiTestResult(api='/mobile/plant-task/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_plant_task_page_list(self, pn_=None, ps_=None, province_=None, city_=None, county_=None, taskStartTime_=None, taskEndTime_=None, taskTypeStr_=None, landId_=None, searchLandName_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'taskStartTime': taskStartTime_, 'taskEndTime': taskEndTime_, 'taskTypeStr': taskTypeStr_, 'landId': landId_, 'searchLandName': searchLandName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'taskStartTime': taskStartTime_, 'taskEndTime': taskEndTime_, 'taskTypeStr': taskTypeStr_, 'landId': landId_, 'searchLandName': searchLandName_}
        response = self.request.post(url=self.url+'/mobile/plant-task/page-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/plant-task/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_detail_invoice_notice(self, prodouctCode_=None):
        if self.user is None:
            data = {'prodouctCode': prodouctCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'prodouctCode': prodouctCode_}
        response = self.request.post(url=self.url+'/mobile/warehouse/detail-invoice-notice', data=data, hosts=self.url)
        apiTestResult(api='/mobile/warehouse/detail-invoice-notice', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_detail_receipt_notice(self, prodouctCode_=None):
        if self.user is None:
            data = {'prodouctCode': prodouctCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'prodouctCode': prodouctCode_}
        response = self.request.post(url=self.url+'/mobile/warehouse/detail-receipt-notice', data=data, hosts=self.url)
        apiTestResult(api='/mobile/warehouse/detail-receipt-notice', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_list_invoice_notice(self, wareHouseCode_=None):
        if self.user is None:
            data = {'wareHouseCode': wareHouseCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'wareHouseCode': wareHouseCode_}
        response = self.request.post(url=self.url+'/mobile/warehouse/list-invoice-notice', data=data, hosts=self.url)
        apiTestResult(api='/mobile/warehouse/list-invoice-notice', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_list_matrial_stock(self, materielCode_=None, warehouseCode_=None):
        if self.user is None:
            data = {'materielCode': materielCode_, 'warehouseCode': warehouseCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'materielCode': materielCode_, 'warehouseCode': warehouseCode_}
        response = self.request.post(url=self.url+'/mobile/warehouse/list-matrial-stock', data=data, hosts=self.url)
        apiTestResult(api='/mobile/warehouse/list-matrial-stock', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_list_my(self, name_=None, subjectId_=None, lat_=None, lng_=None):
        if self.user is None:
            data = {'name': name_, 'subjectId': subjectId_, 'lat': lat_, 'lng': lng_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'subjectId': subjectId_, 'lat': lat_, 'lng': lng_}
        response = self.request.post(url=self.url+'/mobile/warehouse/list-my', data=data, hosts=self.url)
        apiTestResult(api='/mobile/warehouse/list-my', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_list_receipt_notice(self, wareHouseCode_=None):
        if self.user is None:
            data = {'wareHouseCode': wareHouseCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'wareHouseCode': wareHouseCode_}
        response = self.request.post(url=self.url+'/mobile/warehouse/list-receipt-notice', data=data, hosts=self.url)
        apiTestResult(api='/mobile/warehouse/list-receipt-notice', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))
