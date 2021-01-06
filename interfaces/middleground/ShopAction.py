#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
from utils.checkApiChanges.checher.apiTestResult import apiTestResult
import json


class shopAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('MP_SHOP')

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

    def _admin_region_add(self, name_=None, pid_=None, remark_=None):
        if self.user is None:
            data = {'name': name_, 'pid': pid_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'pid': pid_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/region/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/region/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_region_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/region/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/region/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_region_edit(self, id_=None, name_=None, pid_=None, remark_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, 'pid': pid_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_, 'pid': pid_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/region/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/region/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_region_list(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/admin/region/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/region/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/shop/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_equipment_add(self, shopId_=None, equipmentType_=None, name_=None, equipmentNo_=None, addType_=None, equipmentModel_=None, supplierName_=None):
        if self.user is None:
            data = {'shopId': shopId_, 'equipmentType': equipmentType_, 'name': name_, 'equipmentNo': equipmentNo_, 'addType': addType_, 'equipmentModel': equipmentModel_, 'supplierName': supplierName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'shopId': shopId_, 'equipmentType': equipmentType_, 'name': name_, 'equipmentNo': equipmentNo_, 'addType': addType_, 'equipmentModel': equipmentModel_, 'supplierName': supplierName_}
        response = self.request.post(url=self.url+'/admin/shop/equipment/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/equipment/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_equipment_asset_detail(self, assetCode_=None):
        if self.user is None:
            data = {'assetCode': assetCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'assetCode': assetCode_}
        response = self.request.post(url=self.url+'/admin/shop/equipment/asset-detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/equipment/asset-detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_equipment_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/shop/equipment/del', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/equipment/del', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_equipment_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/shop/equipment/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/equipment/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_equipment_list(self, pn_=None, ps_=None, shopId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'shopId': shopId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'shopId': shopId_}
        response = self.request.post(url=self.url+'/admin/shop/equipment/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/equipment/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_list(self, typeList_=None, pn_=None, ps_=None, searchKey_=None, subjectId_=None, regionId_=None, status_=None):
        if self.user is None:
            data = {'typeList': typeList_, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'subjectId': subjectId_, 'regionId': regionId_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'typeList': typeList_, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'subjectId': subjectId_, 'regionId': regionId_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/shop/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_online_add(self, name_=None, subjectId_=None, contact_=None, lng_=None, lat_=None, remark_=None):
        if self.user is None:
            data = {'name': name_, 'subjectId': subjectId_, 'contact': contact_, 'lng': lng_, 'lat': lat_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'subjectId': subjectId_, 'contact': contact_, 'lng': lng_, 'lat': lat_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/shop/online/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/online/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_pos_add(self, name_=None, subjectId_=None, regionId_=None, contact_=None, mobile_=None, type_=None, openTime_=None, closeTime_=None, address_=None, lat_=None, lng_=None, remark_=None):
        if self.user is None:
            data = {'name': name_, 'subjectId': subjectId_, 'regionId': regionId_, 'contact': contact_, 'mobile': mobile_, 'type': type_, 'openTime': openTime_, 'closeTime': closeTime_, 'address': address_, 'lat': lat_, 'lng': lng_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'subjectId': subjectId_, 'regionId': regionId_, 'contact': contact_, 'mobile': mobile_, 'type': type_, 'openTime': openTime_, 'closeTime': closeTime_, 'address': address_, 'lat': lat_, 'lng': lng_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/shop/pos/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/pos/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_pos_edit(self, id_=None, name_=None, subjectId_=None, regionId_=None, contact_=None, mobile_=None, type_=None, openTime_=None, closeTime_=None, address_=None, lat_=None, lng_=None, remark_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, 'subjectId': subjectId_, 'regionId': regionId_, 'contact': contact_, 'mobile': mobile_, 'type': type_, 'openTime': openTime_, 'closeTime': closeTime_, 'address': address_, 'lat': lat_, 'lng': lng_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_, 'subjectId': subjectId_, 'regionId': regionId_, 'contact': contact_, 'mobile': mobile_, 'type': type_, 'openTime': openTime_, 'closeTime': closeTime_, 'address': address_, 'lat': lat_, 'lng': lng_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/shop/pos/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/pos/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_shop_sta(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/shop/shop-sta', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/shop-sta', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_staff_add(self, roleCode_=None, userId_=None, shopId_=None):
        if self.user is None:
            data = {'roleCode': roleCode_, 'userId': userId_, 'shopId': shopId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'roleCode': roleCode_, 'userId': userId_, 'shopId': shopId_}
        response = self.request.post(url=self.url+'/admin/shop/staff/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/staff/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_staff_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/shop/staff/del', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/staff/del', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_staff_disable(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/shop/staff/disable', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/staff/disable', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_staff_enable(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/shop/staff/enable', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/staff/enable', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_staff_list(self, pn_=None, ps_=None, shopId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'shopId': shopId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'shopId': shopId_}
        response = self.request.post(url=self.url+'/admin/shop/staff/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/staff/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_staff_search_by_mobile(self, mobile_=None):
        if self.user is None:
            data = {'mobile': mobile_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile_}
        response = self.request.post(url=self.url+'/admin/shop/staff/search-by-mobile', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/staff/search-by-mobile', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_subject_add(self, name_=None, type_=None, operationNote_=None, pid_=None, remark_=None):
        if self.user is None:
            data = {'name': name_, 'type': type_, 'operationNote': operationNote_, 'pid': pid_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'type': type_, 'operationNote': operationNote_, 'pid': pid_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/subject/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/subject/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_subject_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/subject/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/subject/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_subject_edit(self, id_=None, name_=None, type_=None, operationNote_=None, pid_=None, remark_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, 'type': type_, 'operationNote': operationNote_, 'pid': pid_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_, 'type': type_, 'operationNote': operationNote_, 'pid': pid_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/subject/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/subject/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_subject_list(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/admin/subject/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/subject/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_shop_get(self, shopId_=None):
        if self.user is None:
            data = {'shopId': shopId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'shopId': shopId_}
        response = self.request.post(url=self.url+'/api/shop/get', data=data, hosts=self.url)
        apiTestResult(api='/api/shop/get', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_shop_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/shop/list', data=data, hosts=self.url)
        apiTestResult(api='/api/shop/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_shop_list_by_ids(self, shopIds_=None):
        if self.user is None:
            data = {'shopIds': shopIds_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'shopIds': shopIds_}
        response = self.request.post(url=self.url+'/api/shop/list-by-ids', data=data, hosts=self.url)
        apiTestResult(api='/api/shop/list-by-ids', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_subject_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/subject/list', data=data, hosts=self.url)
        apiTestResult(api='/api/subject/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_subject_list_by_ids(self, subjectIds_=None):
        if self.user is None:
            data = {'subjectIds': subjectIds_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'subjectIds': subjectIds_}
        response = self.request.post(url=self.url+'/api/subject/list-by-ids', data=data, hosts=self.url)
        apiTestResult(api='/api/subject/list-by-ids', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _config_common_get_all_enum_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/config/common/get-all-enum-list', data=data, hosts=self.url)
        apiTestResult(api='/config/common/get-all-enum-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))
