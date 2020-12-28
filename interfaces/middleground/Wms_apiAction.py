#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
import json


class wms_apiAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('MP_WMS')

    def set_user(self, mobile=None, account_type='user', password=None):
        if mobile is None:
            self.user = None
        else:
            self.user = User(mobile, account_type, password=password)
            self.request.headers.update({"_Device-Id_": self.user.device_id})
            self.request.headers.update({"_Token_": self.user.token})
        return self.user

    def __judge_response_status(self, json_response):
        if json_response['status'] in ("OK", "ERROR"):
            return json_response
        else:
            raise Exception('status未返回OK或ERROR')

    def _admin_company_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/company/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_employee_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/employee/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_lotRule_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/lotRule/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_orderCodeRule_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/orderCodeRule/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_orderErpSyncLog_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/orderErpSyncLog/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_add(self, name_=None, outWarehouseCode_=None, companyCode_=None, warehouseTypeId_=None, contactId_=None, province_=None, city_=None, county_=None, lng_=None, lat_=None, address_=None, status_=None, isThird_=None, isVirtual_=None, remark_=None):
        if self.user is None:
            data = {'name': name_, 'outWarehouseCode': outWarehouseCode_, 'companyCode': companyCode_, 'warehouseTypeId': warehouseTypeId_, 'contactId': contactId_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'address': address_, 'status': status_, 'isThird': isThird_, 'isVirtual': isVirtual_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'outWarehouseCode': outWarehouseCode_, 'companyCode': companyCode_, 'warehouseTypeId': warehouseTypeId_, 'contactId': contactId_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'address': address_, 'status': status_, 'isThird': isThird_, 'isVirtual': isVirtual_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/warehouse/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_additional_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/additional-detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_additional_update(self, images_=None, id_=None, area_=None, capacity_=None, cargoType_=None):
        if self.user is None:
            data = {'images': images_, 'id': id_, 'area': area_, 'capacity': capacity_, 'cargoType': cargoType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'images': images_, 'id': id_, 'area': area_, 'capacity': capacity_, 'cargoType': cargoType_}
        response = self.request.post(url=self.url+'/admin/warehouse/additional-update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_add(self, warehouseId_=None, name_=None, outWarehouseAreaCode_=None, warehouseAreaTypeId_=None, location_=None, status_=None, remark_=None):
        if self.user is None:
            data = {'warehouseId': warehouseId_, 'name': name_, 'outWarehouseAreaCode': outWarehouseAreaCode_, 'warehouseAreaTypeId': warehouseAreaTypeId_, 'location': location_, 'status': status_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'warehouseId': warehouseId_, 'name': name_, 'outWarehouseAreaCode': outWarehouseAreaCode_, 'warehouseAreaTypeId': warehouseAreaTypeId_, 'location': location_, 'status': status_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_bind_warehouse(self, warehouseAreaIds_=None, warehouseId_=None):
        if self.user is None:
            data = {'warehouseAreaIds': warehouseAreaIds_, 'warehouseId': warehouseId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'warehouseAreaIds': warehouseAreaIds_, 'warehouseId': warehouseId_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/bind-warehouse', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouse/area/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_list(self, warehouseId_=None, isRelevanceWarehouse_=None):
        if self.user is None:
            data = {'warehouseId': warehouseId_, 'isRelevanceWarehouse': isRelevanceWarehouse_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'warehouseId': warehouseId_, 'isRelevanceWarehouse': isRelevanceWarehouse_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_page_list(self, pn_=None, ps_=None, nameOrCode_=None, status_=None, warehouseAreaTypeId_=None, warehouseNameOrCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'nameOrCode': nameOrCode_, 'status': status_, 'warehouseAreaTypeId': warehouseAreaTypeId_, 'warehouseNameOrCode': warehouseNameOrCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'nameOrCode': nameOrCode_, 'status': status_, 'warehouseAreaTypeId': warehouseAreaTypeId_, 'warehouseNameOrCode': warehouseNameOrCode_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_type_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouse/area/type/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_type_list(self, pn_=None, ps_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/type/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_type_page_list(self, pn_=None, ps_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/type/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_unbind_warehouse(self, warehouseId_=None, warehouseAreaId_=None):
        if self.user is None:
            data = {'warehouseId': warehouseId_, 'warehouseAreaId': warehouseAreaId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'warehouseId': warehouseId_, 'warehouseAreaId': warehouseAreaId_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/unbind-warehouse', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_update(self, id_=None, warehouseId_=None, name_=None, outWarehouseAreaCode_=None, location_=None, status_=None, remark_=None):
        if self.user is None:
            data = {'id': id_, 'warehouseId': warehouseId_, 'name': name_, 'outWarehouseAreaCode': outWarehouseAreaCode_, 'location': location_, 'status': status_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'warehouseId': warehouseId_, 'name': name_, 'outWarehouseAreaCode': outWarehouseAreaCode_, 'location': location_, 'status': status_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouse/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_employee_add(self, userIds_=None, warehouseId_=None):
        if self.user is None:
            data = {'userIds': userIds_, 'warehouseId': warehouseId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userIds': userIds_, 'warehouseId': warehouseId_}
        response = self.request.post(url=self.url+'/admin/warehouse/employee/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_employee_del(self, warehouseEmployeeId_=None):
        if self.user is None:
            data = {'warehouseEmployeeId': warehouseEmployeeId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'warehouseEmployeeId': warehouseEmployeeId_}
        response = self.request.post(url=self.url+'/admin/warehouse/employee/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_employee_list(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/employee/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_erp_sync_log_list(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/erp-sync-log/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_list(self, status_=None):
        if self.user is None:
            data = {'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'status': status_}
        response = self.request.post(url=self.url+'/admin/warehouse/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_monitor_bind(self, cameraCodes_=None, warehouseId_=None):
        if self.user is None:
            data = {'cameraCodes': cameraCodes_, 'warehouseId': warehouseId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cameraCodes': cameraCodes_, 'warehouseId': warehouseId_}
        response = self.request.post(url=self.url+'/admin/warehouse/monitor/bind', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_monitor_camera_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouse/monitor/camera-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_monitor_list(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/monitor/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_monitor_rename(self, id_=None, name_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/warehouse/monitor/rename', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_monitor_unbind(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/monitor/unbind', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_page_list(self, pn_=None, ps_=None, nameOrCode_=None, status_=None, typeId_=None, companyName_=None, province_=None, city_=None, county_=None, adminNameOrPhone_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'nameOrCode': nameOrCode_, 'status': status_, 'typeId': typeId_, 'companyName': companyName_, 'province': province_, 'city': city_, 'county': county_, 'adminNameOrPhone': adminNameOrPhone_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'nameOrCode': nameOrCode_, 'status': status_, 'typeId': typeId_, 'companyName': companyName_, 'province': province_, 'city': city_, 'county': county_, 'adminNameOrPhone': adminNameOrPhone_}
        response = self.request.post(url=self.url+'/admin/warehouse/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_push_to_erp(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/push-to-erp', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_third_config_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/third-config/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_third_config_update(self, warehouseId_=None, systemAccount_=None, appKey_=None, appSecret_=None, systemApi_=None, leaseStartTime_=None, leaseEndTime_=None, rent_=None, rentUnit_=None):
        if self.user is None:
            data = {'warehouseId': warehouseId_, 'systemAccount': systemAccount_, 'appKey': appKey_, 'appSecret': appSecret_, 'systemApi': systemApi_, 'leaseStartTime': leaseStartTime_, 'leaseEndTime': leaseEndTime_, 'rent': rent_, 'rentUnit': rentUnit_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'warehouseId': warehouseId_, 'systemAccount': systemAccount_, 'appKey': appKey_, 'appSecret': appSecret_, 'systemApi': systemApi_, 'leaseStartTime': leaseStartTime_, 'leaseEndTime': leaseEndTime_, 'rent': rent_, 'rentUnit': rentUnit_}
        response = self.request.post(url=self.url+'/admin/warehouse/third-config/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_type_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouse/type/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_type_list(self, pn_=None, ps_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/warehouse/type/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_type_page_list(self, pn_=None, ps_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/warehouse/type/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_update(self, id_=None, name_=None, outWarehouseCode_=None, contactId_=None, province_=None, city_=None, county_=None, lng_=None, lat_=None, address_=None, status_=None, isThird_=None, isVirtual_=None, remark_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, 'outWarehouseCode': outWarehouseCode_, 'contactId': contactId_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'address': address_, 'status': status_, 'isThird': isThird_, 'isVirtual': isVirtual_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_, 'outWarehouseCode': outWarehouseCode_, 'contactId': contactId_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'address': address_, 'status': status_, 'isThird': isThird_, 'isVirtual': isVirtual_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/warehouse/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouseAllot_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouseAllot/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouseAllotProduct_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouseAllotProduct/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouseInvoice_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouseInvoice/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouseInvoiceNotice_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouseInvoiceNotice/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehousePick_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehousePick/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehousePickProduct_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehousePickProduct/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouseReceip_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouseReceip/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouseReceipNotice_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouseReceipNotice/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_asset_sync_archives(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/asset-sync/archives', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_sku_sync_archives(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/sku-sync/archives', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _common_config_list(self, types_=None, code_=None):
        if self.user is None:
            data = {'types': types_, 'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'types': types_, 'code': code_}
        response = self.request.post(url=self.url+'/common/config/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _common_enum_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/common/enum/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _common_file_upload_public_pic(self, file_=None, type_=None):
        if self.user is None:
            data = {'file': file_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'file': file_, 'type': type_}
        response = self.request.post(url=self.url+'/common/file/upload/public-pic', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
