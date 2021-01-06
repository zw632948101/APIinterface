
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

    def _admin_erp_uncleared_order_purchase_list(self, companyCode_=None):
        if self.user is None:
            data = {'companyCode': companyCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'companyCode': companyCode_}
        response = self.request.post(url=self.url+'/admin/erp/uncleared/order/purchase-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_detail_page_list(self, pn_=None, ps_=None, orderCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/invoice-detail/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_confirm(self, orderCode_=None):
        if self.user is None:
            data = {'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/invoice/confirm', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_detail(self, pn_=None, ps_=None, orderCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/invoice/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_page_list(self, pn_=None, ps_=None, orderCode_=None, relevanceCode_=None, status_=None, type_=None, warehouseCode_=None, operatorId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, 'relevanceCode': relevanceCode_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'operatorId': operatorId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, 'relevanceCode': relevanceCode_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'operatorId': operatorId_}
        response = self.request.post(url=self.url+'/admin/invoice/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_lotRule_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/lotRule/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_move_pda_pick_detail_list(self, orderCode_=None):
        if self.user is None:
            data = {'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/move/pda/pick-detail-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_move_pda_pick_list(self, status_=None):
        if self.user is None:
            data = {'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'status': status_}
        response = self.request.post(url=self.url+'/admin/move/pda/pick-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_move_pda_pick_submit(self, products[0]_id_=None, products[0]_productCode_=None, products[0]_actualQuantity_=None, products[0]_tracingCode_=None, products[0]_weight_=None, invoiceCode_=None, code_=None, productJson_=None):
        if self.user is None:
            data = {'products[0]_id': products[0]_id_, 'products[0]_productCode': products[0]_productCode_, 'products[0]_actualQuantity': products[0]_actualQuantity_, 'products[0]_tracingCode': products[0]_tracingCode_, 'products[0]_weight': products[0]_weight_, 'invoiceCode': invoiceCode_, 'code': code_, 'productJson': productJson_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'products[0]_id': products[0]_id_, 'products[0]_productCode': products[0]_productCode_, 'products[0]_actualQuantity': products[0]_actualQuantity_, 'products[0]_tracingCode': products[0]_tracingCode_, 'products[0]_weight': products[0]_weight_, 'invoiceCode': invoiceCode_, 'code': code_, 'productJson': productJson_}
        response = self.request.post(url=self.url+'/admin/move/pda/pick-submit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_operation_log_list(self, bizCode_=None, biz_=None):
        if self.user is None:
            data = {'bizCode': bizCode_, 'biz': biz_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'bizCode': bizCode_, 'biz': biz_}
        response = self.request.post(url=self.url+'/admin/operation-log/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_order_erp_sync_log_list(self, orderCode_=None):
        if self.user is None:
            data = {'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/order/erp-sync-log/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_orderCodeRule_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/orderCodeRule/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_list(self, companyCode_=None):
        if self.user is None:
            data = {'companyCode': companyCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'companyCode': companyCode_}
        response = self.request.post(url=self.url+'/admin/shop/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_transfer_apply_add(self, details[0]_id_=None, details[0]_orderCode_=None, details[0]_productCode_=None, details[0]_planQuantity_=None, relevanceCode_=None, source_=None, type_=None, fromOrg_=None, fromWarehouse_=None, toOrg_=None, toWarehouse_=None, possessor_=None, arriveTime_=None, remark_=None, itemList_=None):
        if self.user is None:
            data = {'details[0]_id': details[0]_id_, 'details[0]_orderCode': details[0]_orderCode_, 'details[0]_productCode': details[0]_productCode_, 'details[0]_planQuantity': details[0]_planQuantity_, 'relevanceCode': relevanceCode_, 'source': source_, 'type': type_, 'fromOrg': fromOrg_, 'fromWarehouse': fromWarehouse_, 'toOrg': toOrg_, 'toWarehouse': toWarehouse_, 'possessor': possessor_, 'arriveTime': arriveTime_, 'remark': remark_, 'itemList': itemList_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'details[0]_id': details[0]_id_, 'details[0]_orderCode': details[0]_orderCode_, 'details[0]_productCode': details[0]_productCode_, 'details[0]_planQuantity': details[0]_planQuantity_, 'relevanceCode': relevanceCode_, 'source': source_, 'type': type_, 'fromOrg': fromOrg_, 'fromWarehouse': fromWarehouse_, 'toOrg': toOrg_, 'toWarehouse': toWarehouse_, 'possessor': possessor_, 'arriveTime': arriveTime_, 'remark': remark_, 'itemList': itemList_}
        response = self.request.post(url=self.url+'/admin/transfer-apply/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_transfer_apply_confirm(self, orderCode_=None, transferMethod_=None, fromOrg_=None, fromWarehouse_=None):
        if self.user is None:
            data = {'orderCode': orderCode_, 'transferMethod': transferMethod_, 'fromOrg': fromOrg_, 'fromWarehouse': fromWarehouse_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderCode': orderCode_, 'transferMethod': transferMethod_, 'fromOrg': fromOrg_, 'fromWarehouse': fromWarehouse_}
        response = self.request.post(url=self.url+'/admin/transfer-apply/confirm', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_add(self, name_=None, outWarehouseCode_=None, companyCode_=None, shopCode_=None, warehouseTypeId_=None, contactId_=None, province_=None, city_=None, county_=None, lng_=None, lat_=None, address_=None, status_=None, isThird_=None, isVirtual_=None, remark_=None):
        if self.user is None:
            data = {'name': name_, 'outWarehouseCode': outWarehouseCode_, 'companyCode': companyCode_, 'shopCode': shopCode_, 'warehouseTypeId': warehouseTypeId_, 'contactId': contactId_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'address': address_, 'status': status_, 'isThird': isThird_, 'isVirtual': isVirtual_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'outWarehouseCode': outWarehouseCode_, 'companyCode': companyCode_, 'shopCode': shopCode_, 'warehouseTypeId': warehouseTypeId_, 'contactId': contactId_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'address': address_, 'status': status_, 'isThird': isThird_, 'isVirtual': isVirtual_, 'remark': remark_}
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

    def _admin_warehouse_update(self, id_=None, name_=None, outWarehouseCode_=None, shopCode_=None, contactId_=None, province_=None, city_=None, county_=None, lng_=None, lat_=None, address_=None, status_=None, isThird_=None, isVirtual_=None, remark_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, 'outWarehouseCode': outWarehouseCode_, 'shopCode': shopCode_, 'contactId': contactId_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'address': address_, 'status': status_, 'isThird': isThird_, 'isVirtual': isVirtual_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_, 'outWarehouseCode': outWarehouseCode_, 'shopCode': shopCode_, 'contactId': contactId_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'address': address_, 'status': status_, 'isThird': isThird_, 'isVirtual': isVirtual_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/warehouse/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_pda_receipt_list(self, pn_=None, ps_=None, status_=None, type_=None, shopCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'status': status_, 'type': type_, 'shopCode': shopCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'status': status_, 'type': type_, 'shopCode': shopCode_}
        response = self.request.post(url=self.url+'/admin/whs/pda/receipt/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_pda_receipt_product_list(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/admin/whs/pda/receipt/product/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_pda_receipt_product_submit(self, receiptProducts[0]_receiptTracings[0]_tracingCode_=None, receiptProducts[0]_receiptTracings[0]_weight_=None, receiptQuality[0]_qualityReport_=None, code_=None, productJson_=None, qualityResult_=None):
        if self.user is None:
            data = {'receiptProducts[0]_receiptTracings[0]_tracingCode': receiptProducts[0]_receiptTracings[0]_tracingCode_, 'receiptProducts[0]_receiptTracings[0]_weight': receiptProducts[0]_receiptTracings[0]_weight_, 'receiptQuality[0]_qualityReport': receiptQuality[0]_qualityReport_, 'code': code_, 'productJson': productJson_, 'qualityResult': qualityResult_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'receiptProducts[0]_receiptTracings[0]_tracingCode': receiptProducts[0]_receiptTracings[0]_tracingCode_, 'receiptProducts[0]_receiptTracings[0]_weight': receiptProducts[0]_receiptTracings[0]_weight_, 'receiptQuality[0]_qualityReport': receiptQuality[0]_qualityReport_, 'code': code_, 'productJson': productJson_, 'qualityResult': qualityResult_}
        response = self.request.post(url=self.url+'/admin/whs/pda/receipt/product/submit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_receipt_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/whs/receipt/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_receipt_detail(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/admin/whs/receipt/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_receipt_notice_add(self, noticeProducts[0]_noticeTracings[0]_tracingCode_=None, noticeProducts[0]_noticeTracings[0]_purchaseWeight_=None, noticeProducts[0]_noticeTracings[0]_tareWeight_=None, noticeProducts[0]_productCode_=None, noticeProducts[0]_planQuantity_=None, noticeProducts[0]_price_=None, relevanceCode_=None, source_=None, type_=None, warehouseCode_=None, purchasingCompany_=None, possessor_=None, supplier_=None, remark_=None, productInfo_=None):
        if self.user is None:
            data = {'noticeProducts[0]_noticeTracings[0]_tracingCode': noticeProducts[0]_noticeTracings[0]_tracingCode_, 'noticeProducts[0]_noticeTracings[0]_purchaseWeight': noticeProducts[0]_noticeTracings[0]_purchaseWeight_, 'noticeProducts[0]_noticeTracings[0]_tareWeight': noticeProducts[0]_noticeTracings[0]_tareWeight_, 'noticeProducts[0]_productCode': noticeProducts[0]_productCode_, 'noticeProducts[0]_planQuantity': noticeProducts[0]_planQuantity_, 'noticeProducts[0]_price': noticeProducts[0]_price_, 'relevanceCode': relevanceCode_, 'source': source_, 'type': type_, 'warehouseCode': warehouseCode_, 'purchasingCompany': purchasingCompany_, 'possessor': possessor_, 'supplier': supplier_, 'remark': remark_, 'productInfo': productInfo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'noticeProducts[0]_noticeTracings[0]_tracingCode': noticeProducts[0]_noticeTracings[0]_tracingCode_, 'noticeProducts[0]_noticeTracings[0]_purchaseWeight': noticeProducts[0]_noticeTracings[0]_purchaseWeight_, 'noticeProducts[0]_noticeTracings[0]_tareWeight': noticeProducts[0]_noticeTracings[0]_tareWeight_, 'noticeProducts[0]_productCode': noticeProducts[0]_productCode_, 'noticeProducts[0]_planQuantity': noticeProducts[0]_planQuantity_, 'noticeProducts[0]_price': noticeProducts[0]_price_, 'relevanceCode': relevanceCode_, 'source': source_, 'type': type_, 'warehouseCode': warehouseCode_, 'purchasingCompany': purchasingCompany_, 'possessor': possessor_, 'supplier': supplier_, 'remark': remark_, 'productInfo': productInfo_}
        response = self.request.post(url=self.url+'/admin/whs/receipt/notice/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_receipt_notice_cancel(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/admin/whs/receipt/notice/cancel', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_receipt_notice_confirmed(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/admin/whs/receipt/notice/confirmed', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_receipt_notice_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/whs/receipt/notice/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_receipt_notice_detail(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/admin/whs/receipt/notice/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_receipt_notice_page_list(self, pn_=None, ps_=None, code_=None, status_=None, type_=None, warehouseCode_=None, creatorId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'creatorId': creatorId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'creatorId': creatorId_}
        response = self.request.post(url=self.url+'/admin/whs/receipt/notice/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_receipt_notice_product_page_list(self, pn_=None, ps_=None, orderCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/whs/receipt/notice/product/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_receipt_notice_update(self, code_=None, possessor_=None, purchasingCompany_=None, remark_=None):
        if self.user is None:
            data = {'code': code_, 'possessor': possessor_, 'purchasingCompany': purchasingCompany_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'possessor': possessor_, 'purchasingCompany': purchasingCompany_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/whs/receipt/notice/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_receipt_page_list(self, pn_=None, ps_=None, code_=None, status_=None, type_=None, warehouseCode_=None, creatorId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'creatorId': creatorId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'creatorId': creatorId_}
        response = self.request.post(url=self.url+'/admin/whs/receipt/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_receipt_product_page_list(self, pn_=None, ps_=None, orderCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/whs/receipt/product/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_receipt_sync_erp(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/admin/whs/receipt/sync-erp', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_whs_receipt_tracing_page_list(self, pn_=None, ps_=None, orderCode_=None, productCode_=None, tracingCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, 'productCode': productCode_, 'tracingCode': tracingCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, 'productCode': productCode_, 'tracingCode': tracingCode_}
        response = self.request.post(url=self.url+'/admin/whs/receipt/tracing/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))