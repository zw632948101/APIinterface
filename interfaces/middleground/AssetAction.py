#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
import json


class assetAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('MP_ASSET')

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

    def _admin_apply_cancel(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/apply/cancel', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_apply_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/apply/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_apply_page(self, pn_=None, ps_=None, applyNo_=None, productId_=None, type_=None, status_=None, isDistribute_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'applyNo': applyNo_, 'productId': productId_, 'type': type_, 'status': status_, 'isDistribute': isDistribute_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'applyNo': applyNo_, 'productId': productId_, 'type': type_, 'status': status_, 'isDistribute': isDistribute_}
        response = self.request.post(url=self.url+'/admin/apply/page', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_apply_page_ex_warehouse(self, pn_=None, ps_=None, warehouseId_=None, applyNo_=None, status_=None, productId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'warehouseId': warehouseId_, 'applyNo': applyNo_, 'status': status_, 'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'warehouseId': warehouseId_, 'applyNo': applyNo_, 'status': status_, 'productId': productId_}
        response = self.request.post(url=self.url+'/admin/apply/page-ex-warehouse', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_apply_warehouse_apply(self, consigneeId_=None, productId_=None, total_=None, reason_=None):
        if self.user is None:
            data = {'consigneeId': consigneeId_, 'productId': productId_, 'total': total_, 'reason': reason_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'consigneeId': consigneeId_, 'productId': productId_, 'total': total_, 'reason': reason_}
        response = self.request.post(url=self.url+'/admin/apply/warehouse-apply', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_asset_ledger_page(self, pn_=None, ps_=None, code_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_}
        response = self.request.post(url=self.url+'/admin/asset-ledger/page', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_asset_detail(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/admin/asset/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_asset_init(self, codes_=None, warehouseId_=None, supplierId_=None):
        if self.user is None:
            data = {'codes': codes_, 'warehouseId': warehouseId_, 'supplierId': supplierId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'codes': codes_, 'warehouseId': warehouseId_, 'supplierId': supplierId_}
        response = self.request.post(url=self.url+'/admin/asset/init', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_asset_page(self, pn_=None, ps_=None, code_=None, supplierIds_=None, statuses_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, 'supplierIds': supplierIds_, 'statuses': statuses_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_, 'supplierIds': supplierIds_, 'statuses': statuses_}
        response = self.request.post(url=self.url+'/admin/asset/page', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_asset_page_statics(self, pn_=None, ps_=None, code_=None, supplierIds_=None, statuses_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, 'supplierIds': supplierIds_, 'statuses': statuses_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_, 'supplierIds': supplierIds_, 'statuses': statuses_}
        response = self.request.post(url=self.url+'/admin/asset/page-statics', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_asset_statics_by_owner(self, id_=None, ownerType_=None):
        if self.user is None:
            data = {'id': id_, 'ownerType': ownerType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'ownerType': ownerType_}
        response = self.request.post(url=self.url+'/admin/asset/statics-by-owner', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    # def _admin_asset_transfer(self, address_province_=None, address_city_=None, address_county_=None, address_address_=None, address_lng_=None, address_lat_=None, codes[0]_attrs[0]_attrId_=None, codes[0]_attrs[0]_type_=None, codes[0]_attrs[0]_attrName_=None, codes[0]_attrs[0]_unit_=None, codes[0]_attrs[0]_value_=None, codes[0]_code_=None, codes[0]_weight_=None, senderRole_=None, receiverRole_=None, receiverId_=None, remark_=None, transferTime_=None, apiaryId_=None):
    #     if self.user is None:
    #         data = {'address_province': address_province_, 'address_city': address_city_, 'address_county': address_county_, 'address_address': address_address_, 'address_lng': address_lng_, 'address_lat': address_lat_, 'codes[0]_attrs[0]_attrId': codes[0]_attrs[0]_attrId_, 'codes[0]_attrs[0]_type': codes[0]_attrs[0]_type_, 'codes[0]_attrs[0]_attrName': codes[0]_attrs[0]_attrName_, 'codes[0]_attrs[0]_unit': codes[0]_attrs[0]_unit_, 'codes[0]_attrs[0]_value': codes[0]_attrs[0]_value_, 'codes[0]_code': codes[0]_code_, 'codes[0]_weight': codes[0]_weight_, 'senderRole': senderRole_, 'receiverRole': receiverRole_, 'receiverId': receiverId_, 'remark': remark_, 'transferTime': transferTime_, 'apiaryId': apiaryId_, }
    #     else:
    #         data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'address_province': address_province_, 'address_city': address_city_, 'address_county': address_county_, 'address_address': address_address_, 'address_lng': address_lng_, 'address_lat': address_lat_, 'codes[0]_attrs[0]_attrId': codes[0]_attrs[0]_attrId_, 'codes[0]_attrs[0]_type': codes[0]_attrs[0]_type_, 'codes[0]_attrs[0]_attrName': codes[0]_attrs[0]_attrName_, 'codes[0]_attrs[0]_unit': codes[0]_attrs[0]_unit_, 'codes[0]_attrs[0]_value': codes[0]_attrs[0]_value_, 'codes[0]_code': codes[0]_code_, 'codes[0]_weight': codes[0]_weight_, 'senderRole': senderRole_, 'receiverRole': receiverRole_, 'receiverId': receiverId_, 'remark': remark_, 'transferTime': transferTime_, 'apiaryId': apiaryId_}
    #     response = self.request.post(url=self.url+'/admin/asset/transfer', data=data, hosts=self.url)
    #     return self.__judge_response_status(json.loads(response))

    def _admin_code_base_add(self, codeType_=None, productId_=None, number_=None, supplierId_=None):
        if self.user is None:
            data = {'codeType': codeType_, 'productId': productId_, 'number': number_, 'supplierId': supplierId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'codeType': codeType_, 'productId': productId_, 'number': number_, 'supplierId': supplierId_}
        response = self.request.post(url=self.url+'/admin/code-base/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_code_base_page(self, pn_=None, ps_=None, code_=None, supplierIds_=None, statuses_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, 'supplierIds': supplierIds_, 'statuses': statuses_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_, 'supplierIds': supplierIds_, 'statuses': statuses_}
        response = self.request.post(url=self.url+'/admin/code-base/page', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_code_batch_page(self, pn_=None, ps_=None, supplierId_=None, productId_=None, type_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'supplierId': supplierId_, 'productId': productId_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'supplierId': supplierId_, 'productId': productId_, 'type': type_}
        response = self.request.post(url=self.url+'/admin/code-batch/page', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_code(self, batchId_=None):
        if self.user is None:
            data = {'batchId': batchId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'batchId': batchId_}
        response = self.request.get(url=self.url+'/admin/excel-export/code', params=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_in_warehouse(self, productId_=None):
        if self.user is None:
            data = {'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_}
        response = self.request.get(url=self.url+'/admin/excel-export/in-warehouse', params=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_out_warehouse(self, productId_=None, type_=None):
        if self.user is None:
            data = {'productId': productId_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_, 'type': type_}
        response = self.request.get(url=self.url+'/admin/excel-export/out-warehouse', params=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_file_upload(self, file_=None):
        if self.user is None:
            data = {'file': file_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'file': file_}
        response = self.request.post(url=self.url+'/admin/file/upload', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_type_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/product-type/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_add(self, typeId_=None, code_=None, name_=None, unit_=None, desc_=None, attrs_=None):
        if self.user is None:
            data = {'typeId': typeId_, 'code': code_, 'name': name_, 'unit': unit_, 'desc': desc_, 'attrs': attrs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'typeId': typeId_, 'code': code_, 'name': name_, 'unit': unit_, 'desc': desc_, 'attrs': attrs_}
        response = self.request.post(url=self.url+'/admin/product/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/product/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_get_product_attr(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/product/get-product-attr', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/product/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_list_page(self, pn_=None, ps_=None, typeId_=None, code_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'typeId': typeId_, 'code': code_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'typeId': typeId_, 'code': code_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/product/list-page', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_rfid_page(self, pn_=None, ps_=None, code_=None, supplierIds_=None, statuses_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, 'supplierIds': supplierIds_, 'statuses': statuses_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_, 'supplierIds': supplierIds_, 'statuses': statuses_}
        response = self.request.post(url=self.url+'/admin/rfid/page', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_add(self, code_=None, name_=None, supplierTypeId_=None, address_=None, contacts_=None, phone_=None, business_=None):
        if self.user is None:
            data = {'code': code_, 'name': name_, 'supplierTypeId': supplierTypeId_, 'address': address_, 'contacts': contacts_, 'phone': phone_, 'business': business_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'name': name_, 'supplierTypeId': supplierTypeId_, 'address': address_, 'contacts': contacts_, 'phone': phone_, 'business': business_}
        response = self.request.post(url=self.url+'/admin/supplier/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/supplier/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_edit(self, id_=None, name_=None, address_=None, phone_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, 'address': address_, 'phone': phone_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_, 'address': address_, 'phone': phone_}
        response = self.request.post(url=self.url+'/admin/supplier/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_list(self, supplierTypeId_=None):
        if self.user is None:
            data = {'supplierTypeId': supplierTypeId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'supplierTypeId': supplierTypeId_}
        response = self.request.post(url=self.url+'/admin/supplier/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_list_category(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/supplier/list-category', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_page(self, pn_=None, ps_=None, code_=None, name_=None, supplierTypeId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, 'name': name_, 'supplierTypeId': supplierTypeId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_, 'name': name_, 'supplierTypeId': supplierTypeId_}
        response = self.request.post(url=self.url+'/admin/supplier/page', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_record(self, pn_=None, ps_=None, id_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'id': id_}
        response = self.request.post(url=self.url+'/admin/supplier/record', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_type_dict_list_by_type(self, type_=None):
        if self.user is None:
            data = {'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'type': type_}
        response = self.request.post(url=self.url+'/admin/type-dict/list-by-type', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_add(self, code_=None, name_=None, lng_=None, lat_=None, province_=None, city_=None, county_=None, address_=None, area_=None, goodsTypeIds_=None, managerId_=None, leaseStartTime_=None, leaseEndTime_=None, landlord_=None, landlordPhone_=None, remark_=None, imgUrls_=None):
        if self.user is None:
            data = {'code': code_, 'name': name_, 'lng': lng_, 'lat': lat_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'area': area_, 'goodsTypeIds': goodsTypeIds_, 'managerId': managerId_, 'leaseStartTime': leaseStartTime_, 'leaseEndTime': leaseEndTime_, 'landlord': landlord_, 'landlordPhone': landlordPhone_, 'remark': remark_, 'imgUrls': imgUrls_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'name': name_, 'lng': lng_, 'lat': lat_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'area': area_, 'goodsTypeIds': goodsTypeIds_, 'managerId': managerId_, 'leaseStartTime': leaseStartTime_, 'leaseEndTime': leaseEndTime_, 'landlord': landlord_, 'landlordPhone': landlordPhone_, 'remark': remark_, 'imgUrls': imgUrls_}
        response = self.request.post(url=self.url+'/admin/warehouse/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_in_warehouse(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/admin/warehouse/in-warehouse', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_list_owner(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouse/list-owner', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_out_warehouse(self, id_=None, codes_=None):
        if self.user is None:
            data = {'id': id_, 'codes': codes_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'codes': codes_}
        response = self.request.post(url=self.url+'/admin/warehouse/out-warehouse', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_page(self, pn_=None, ps_=None, code_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/warehouse/page', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_page_record(self, pn_=None, ps_=None, warehouseId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'warehouseId': warehouseId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'warehouseId': warehouseId_}
        response = self.request.post(url=self.url+'/admin/warehouse/page-record', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_stock(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/stock', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_allocate_apply(self, consigneeId_=None, productId_=None, total_=None, reason_=None):
        if self.user is None:
            data = {'consigneeId': consigneeId_, 'productId': productId_, 'total': total_, 'reason': reason_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'consigneeId': consigneeId_, 'productId': productId_, 'total': total_, 'reason': reason_}
        response = self.request.post(url=self.url+'/mobile/allocate/apply', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_allocate_cancel(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/allocate/cancel', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_allocate_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/allocate/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_allocate_page(self, pn_=None, ps_=None, consigneeId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'consigneeId': consigneeId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'consigneeId': consigneeId_}
        response = self.request.post(url=self.url+'/mobile/allocate/page', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_add(self, consigneeId_=None, consigneeType_=None, productId_=None, total_=None, reason_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'consigneeId': consigneeId_, 'consigneeType': consigneeType_, 'productId': productId_, 'total': total_, 'reason': reason_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'consigneeId': consigneeId_, 'consigneeType': consigneeType_, 'productId': productId_, 'total': total_, 'reason': reason_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/mobile/apply/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_cancel(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/apply/cancel', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/apply/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_page(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/mobile/apply/page', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_asset_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/asset/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_asset_page_grant(self, pn_=None, ps_=None, startTime_=None, endTime_=None, province_=None, city_=None, county_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'startTime': startTime_, 'endTime': endTime_, 'province': province_, 'city': city_, 'county': county_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'startTime': startTime_, 'endTime': endTime_, 'province': province_, 'city': city_, 'county': county_}
        response = self.request.post(url=self.url+'/mobile/asset/page-grant', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_asset_transfer(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/mobile/asset/transfer', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_product_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/product/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_supplier_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/supplier/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_type_dict_list_by_type(self, type_=None):
        if self.user is None:
            data = {'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'type': type_}
        response = self.request.post(url=self.url+'/mobile/type-dict/list-by-type', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_id_check(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/warehouse/id-check', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_in_warehouse(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/mobile/warehouse/in-warehouse', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_init(self, codes_=None, warehouseId_=None, supplierId_=None):
        if self.user is None:
            data = {'codes': codes_, 'warehouseId': warehouseId_, 'supplierId': supplierId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'codes': codes_, 'warehouseId': warehouseId_, 'supplierId': supplierId_}
        response = self.request.post(url=self.url+'/mobile/warehouse/init', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_list_owner(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/warehouse/list-owner', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_list_stock(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/warehouse/list-stock', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_out_warehouse(self, id_=None, codes_=None):
        if self.user is None:
            data = {'id': id_, 'codes': codes_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'codes': codes_}
        response = self.request.post(url=self.url+'/mobile/warehouse/out-warehouse', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_page_ex_warehouse(self, pn_=None, ps_=None, warehouseId_=None, applyNo_=None, status_=None, productId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'warehouseId': warehouseId_, 'applyNo': applyNo_, 'status': status_, 'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'warehouseId': warehouseId_, 'applyNo': applyNo_, 'status': status_, 'productId': productId_}
        response = self.request.post(url=self.url+'/mobile/warehouse/page-ex-warehouse', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
