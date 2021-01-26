#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
from utils.checkApiChanges.checher.apiTestResult import apiTestResult
import json


class assetAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('MP_ASSET')

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

    def _admin_apply_cancel(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/apply/cancel', data=data, hosts=self.url)
        apiTestResult(api='/admin/apply/cancel', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_apply_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/apply/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/apply/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_apply_page(self, pn_=None, ps_=None, applyNo_=None, productId_=None, type_=None, status_=None, isDistribute_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'applyNo': applyNo_, 'productId': productId_, 'type': type_, 'status': status_, 'isDistribute': isDistribute_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'applyNo': applyNo_, 'productId': productId_, 'type': type_, 'status': status_, 'isDistribute': isDistribute_}
        response = self.request.post(url=self.url+'/admin/apply/page', data=data, hosts=self.url)
        apiTestResult(api='/admin/apply/page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_apply_page_ex_warehouse(self, pn_=None, ps_=None, warehouseId_=None, applyNo_=None, status_=None, productId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'warehouseId': warehouseId_, 'applyNo': applyNo_, 'status': status_, 'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'warehouseId': warehouseId_, 'applyNo': applyNo_, 'status': status_, 'productId': productId_}
        response = self.request.post(url=self.url+'/admin/apply/page-ex-warehouse', data=data, hosts=self.url)
        apiTestResult(api='/admin/apply/page-ex-warehouse', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_apply_warehouse_apply(self, consigneeId_=None, productId_=None, total_=None, reason_=None):
        if self.user is None:
            data = {'consigneeId': consigneeId_, 'productId': productId_, 'total': total_, 'reason': reason_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'consigneeId': consigneeId_, 'productId': productId_, 'total': total_, 'reason': reason_}
        response = self.request.post(url=self.url+'/admin/apply/warehouse-apply', data=data, hosts=self.url)
        apiTestResult(api='/admin/apply/warehouse-apply', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_asset_ledger_page(self, pn_=None, ps_=None, code_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_}
        response = self.request.post(url=self.url+'/admin/asset-ledger/page', data=data, hosts=self.url)
        apiTestResult(api='/admin/asset-ledger/page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_asset_detail(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/admin/asset/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/asset/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_asset_init(self, codes_=None, warehouseId_=None, haveRfid_=None, supplierId_=None):
        if self.user is None:
            data = {'codes': codes_, 'warehouseId': warehouseId_, 'haveRfid': haveRfid_, 'supplierId': supplierId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'codes': codes_, 'warehouseId': warehouseId_, 'haveRfid': haveRfid_, 'supplierId': supplierId_}
        response = self.request.post(url=self.url+'/admin/asset/init', data=data, hosts=self.url)
        apiTestResult(api='/admin/asset/init', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_asset_page(self, pn_=None, ps_=None, productId_=None, code_=None, supplierIds_=None, statuses_=None, curOwner_=None, warehouseIds_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'productId': productId_, 'code': code_, 'supplierIds': supplierIds_, 'statuses': statuses_, 'curOwner': curOwner_, 'warehouseIds': warehouseIds_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'productId': productId_, 'code': code_, 'supplierIds': supplierIds_, 'statuses': statuses_, 'curOwner': curOwner_, 'warehouseIds': warehouseIds_}
        response = self.request.post(url=self.url+'/admin/asset/page', data=data, hosts=self.url)
        apiTestResult(api='/admin/asset/page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_asset_page_statics(self, pn_=None, ps_=None, productId_=None, code_=None, supplierIds_=None, statuses_=None, curOwner_=None, warehouseIds_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'productId': productId_, 'code': code_, 'supplierIds': supplierIds_, 'statuses': statuses_, 'curOwner': curOwner_, 'warehouseIds': warehouseIds_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'productId': productId_, 'code': code_, 'supplierIds': supplierIds_, 'statuses': statuses_, 'curOwner': curOwner_, 'warehouseIds': warehouseIds_}
        response = self.request.post(url=self.url+'/admin/asset/page-statics', data=data, hosts=self.url)
        apiTestResult(api='/admin/asset/page-statics', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_asset_statics_by_owner(self, id_=None, ownerType_=None, showCount_=None):
        if self.user is None:
            data = {'id': id_, 'ownerType': ownerType_, 'showCount': showCount_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'ownerType': ownerType_, 'showCount': showCount_}
        response = self.request.post(url=self.url+'/admin/asset/statics-by-owner', data=data, hosts=self.url)
        apiTestResult(api='/admin/asset/statics-by-owner', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_asset_transfer(self, address_province_=None, address_city_=None, address_county_=None, address_address_=None, address_lng_=None, address_lat_=None, senderRole_=None, receiverRole_=None, receiverId_=None, bizNo_=None, remark_=None, transferTime_=None, apiaryId_=None, recoveryDate_=None):
        if self.user is None:
            data = {'address_province': address_province_, 'address_city': address_city_, 'address_county': address_county_, 'address_address': address_address_, 'address_lng': address_lng_, 'address_lat': address_lat_, 'senderRole': senderRole_, 'receiverRole': receiverRole_, 'receiverId': receiverId_, 'bizNo': bizNo_, 'remark': remark_, 'transferTime': transferTime_, 'apiaryId': apiaryId_, 'recoveryDate': recoveryDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'address_province': address_province_, 'address_city': address_city_, 'address_county': address_county_, 'address_address': address_address_, 'address_lng': address_lng_, 'address_lat': address_lat_, 'senderRole': senderRole_, 'receiverRole': receiverRole_, 'receiverId': receiverId_, 'bizNo': bizNo_, 'remark': remark_, 'transferTime': transferTime_, 'apiaryId': apiaryId_, 'recoveryDate': recoveryDate_}
        response = self.request.post(url=self.url+'/admin/asset/transfer', data=data, hosts=self.url)
        apiTestResult(api='/admin/asset/transfer', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_code_base_page(self, pn_=None, ps_=None, code_=None, supplierIds_=None, statuses_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, 'supplierIds': supplierIds_, 'statuses': statuses_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_, 'supplierIds': supplierIds_, 'statuses': statuses_}
        response = self.request.post(url=self.url+'/admin/code-base/page', data=data, hosts=self.url)
        apiTestResult(api='/admin/code-base/page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_code_batch_add(self, codeType_=None, productId_=None, number_=None, supplierId_=None):
        if self.user is None:
            data = {'codeType': codeType_, 'productId': productId_, 'number': number_, 'supplierId': supplierId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'codeType': codeType_, 'productId': productId_, 'number': number_, 'supplierId': supplierId_}
        response = self.request.post(url=self.url+'/admin/code-batch/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/code-batch/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_code_batch_page(self, pn_=None, ps_=None, supplierId_=None, productId_=None, type_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'supplierId': supplierId_, 'productId': productId_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'supplierId': supplierId_, 'productId': productId_, 'type': type_}
        response = self.request.post(url=self.url+'/admin/code-batch/page', data=data, hosts=self.url)
        apiTestResult(api='/admin/code-batch/page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_code_goods_binding(self, assetCode_=None, codes_=None, operatorId_=None):
        if self.user is None:
            data = {'assetCode': assetCode_, 'codes': codes_, 'operatorId': operatorId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'assetCode': assetCode_, 'codes': codes_, 'operatorId': operatorId_}
        response = self.request.post(url=self.url+'/admin/code-goods/binding', data=data, hosts=self.url)
        apiTestResult(api='/admin/code-goods/binding', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_code_goods_completed(self, goodsCodes_=None):
        if self.user is None:
            data = {'goodsCodes': goodsCodes_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'goodsCodes': goodsCodes_}
        response = self.request.post(url=self.url+'/admin/code-goods/completed', data=data, hosts=self.url)
        apiTestResult(api='/admin/code-goods/completed', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_code_goods_page(self, pn_=None, ps_=None, code_=None, status_=None, dictId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, 'status': status_, 'dictId': dictId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_, 'status': status_, 'dictId': dictId_}
        response = self.request.post(url=self.url+'/admin/code-goods/page', data=data, hosts=self.url)
        apiTestResult(api='/admin/code-goods/page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_asset_statistics(self, productId_=None):
        if self.user is None:
            data = {'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_}
        response = self.request.get(url=self.url+'/admin/excel-export/asset-statistics', params=data, hosts=self.url)
        apiTestResult(api='/admin/excel-export/asset-statistics', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_code(self, batchId_=None):
        if self.user is None:
            data = {'batchId': batchId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'batchId': batchId_}
        response = self.request.get(url=self.url+'/admin/excel-export/code', params=data, hosts=self.url)
        apiTestResult(api='/admin/excel-export/code', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_goods_code(self, applyId_=None):
        if self.user is None:
            data = {'applyId': applyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_}
        response = self.request.get(url=self.url+'/admin/excel-export/goods-code', params=data, hosts=self.url)
        apiTestResult(api='/admin/excel-export/goods-code', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_in_warehouse(self, productId_=None):
        if self.user is None:
            data = {'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_}
        response = self.request.get(url=self.url+'/admin/excel-export/in-warehouse', params=data, hosts=self.url)
        apiTestResult(api='/admin/excel-export/in-warehouse', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_out_warehouse(self, productId_=None, type_=None):
        if self.user is None:
            data = {'productId': productId_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_, 'type': type_}
        response = self.request.get(url=self.url+'/admin/excel-export/out-warehouse', params=data, hosts=self.url)
        apiTestResult(api='/admin/excel-export/out-warehouse', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_import_init_asset(self, file_=None):
        if self.user is None:
            data = {'file': file_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'file': file_}
        response = self.request.post(url=self.url+'/admin/excel-import/init-asset', data=data, hosts=self.url)
        apiTestResult(api='/admin/excel-import/init-asset', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_file_upload(self, file_=None):
        if self.user is None:
            data = {'file': file_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'file': file_}
        response = self.request.post(url=self.url+'/admin/file/upload', data=data, hosts=self.url)
        apiTestResult(api='/admin/file/upload', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_goods_apply_apply(self, dictCode_=None, dictKey_=None, total_=None, applicantId_=None, assetCode_=None, applicantSource_=None):
        if self.user is None:
            data = {'dictCode': dictCode_, 'dictKey': dictKey_, 'total': total_, 'applicantId': applicantId_, 'assetCode': assetCode_, 'applicantSource': applicantSource_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'dictCode': dictCode_, 'dictKey': dictKey_, 'total': total_, 'applicantId': applicantId_, 'assetCode': assetCode_, 'applicantSource': applicantSource_}
        response = self.request.post(url=self.url+'/admin/goods-apply/apply', data=data, hosts=self.url)
        apiTestResult(api='/admin/goods-apply/apply', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_goods_apply_page(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/admin/goods-apply/page', data=data, hosts=self.url)
        apiTestResult(api='/admin/goods-apply/page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_goods_apply_query(self, applyId_=None):
        if self.user is None:
            data = {'applyId': applyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_}
        response = self.request.post(url=self.url+'/admin/goods-apply/query', data=data, hosts=self.url)
        apiTestResult(api='/admin/goods-apply/query', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_type_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/product-type/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/product-type/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_add(self, typeId_=None, code_=None, name_=None, unit_=None, desc_=None, attrs_=None):
        if self.user is None:
            data = {'typeId': typeId_, 'code': code_, 'name': name_, 'unit': unit_, 'desc': desc_, 'attrs': attrs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'typeId': typeId_, 'code': code_, 'name': name_, 'unit': unit_, 'desc': desc_, 'attrs': attrs_}
        response = self.request.post(url=self.url+'/admin/product/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/product/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/product/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/product/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_edit(self, id_=None, typeId_=None, code_=None, name_=None, unit_=None, desc_=None, attrs_=None):
        if self.user is None:
            data = {'id': id_, 'typeId': typeId_, 'code': code_, 'name': name_, 'unit': unit_, 'desc': desc_, 'attrs': attrs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'typeId': typeId_, 'code': code_, 'name': name_, 'unit': unit_, 'desc': desc_, 'attrs': attrs_}
        response = self.request.post(url=self.url+'/admin/product/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/product/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_get_product_attr(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/product/get-product-attr', data=data, hosts=self.url)
        apiTestResult(api='/admin/product/get-product-attr', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/product/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/product/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_list_page(self, pn_=None, ps_=None, typeId_=None, code_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'typeId': typeId_, 'code': code_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'typeId': typeId_, 'code': code_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/product/list-page', data=data, hosts=self.url)
        apiTestResult(api='/admin/product/list-page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_rfid_page(self, pn_=None, ps_=None, code_=None, supplierIds_=None, statuses_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, 'supplierIds': supplierIds_, 'statuses': statuses_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_, 'supplierIds': supplierIds_, 'statuses': statuses_}
        response = self.request.post(url=self.url+'/admin/rfid/page', data=data, hosts=self.url)
        apiTestResult(api='/admin/rfid/page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_add(self, address_=None, business_=None, city_=None, contacts_=None, county_=None, lat_=None, lng_=None, name_=None, phone_=None, province_=None, remark_=None, sku_=None, supplierExtInput_=None, supplierType_=None):
        if self.user is None:
            data = {'address': address_, 'business': business_, 'city': city_, 'contacts': contacts_, 'county': county_, 'lat': lat_, 'lng': lng_, 'name': name_, 'phone': phone_, 'province': province_, 'remark': remark_, 'sku': sku_, 'supplierExtInput': supplierExtInput_, 'supplierType': supplierType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'address': address_, 'business': business_, 'city': city_, 'contacts': contacts_, 'county': county_, 'lat': lat_, 'lng': lng_, 'name': name_, 'phone': phone_, 'province': province_, 'remark': remark_, 'sku': sku_, 'supplierExtInput': supplierExtInput_, 'supplierType': supplierType_}
        response = self.request.post(url=self.url+'/admin/supplier/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/supplier/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/supplier/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/supplier/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_edit(self, address_=None, business_=None, city_=None, contacts_=None, county_=None, id_=None, lat_=None, lng_=None, phone_=None, province_=None, remark_=None, supplierExtInput_=None):
        if self.user is None:
            data = {'address': address_, 'business': business_, 'city': city_, 'contacts': contacts_, 'county': county_, 'id': id_, 'lat': lat_, 'lng': lng_, 'phone': phone_, 'province': province_, 'remark': remark_, 'supplierExtInput': supplierExtInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'address': address_, 'business': business_, 'city': city_, 'contacts': contacts_, 'county': county_, 'id': id_, 'lat': lat_, 'lng': lng_, 'phone': phone_, 'province': province_, 'remark': remark_, 'supplierExtInput': supplierExtInput_}
        response = self.request.post(url=self.url+'/admin/supplier/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/supplier/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_enable(self, id_=None, enabled_=None):
        if self.user is None:
            data = {'id': id_, 'enabled': enabled_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'enabled': enabled_}
        response = self.request.post(url=self.url+'/admin/supplier/enable', data=data, hosts=self.url)
        apiTestResult(api='/admin/supplier/enable', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/supplier/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/supplier/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_list_sku(self, class3_=None):
        if self.user is None:
            data = {'class3': class3_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'class3': class3_}
        response = self.request.post(url=self.url+'/admin/supplier/list-sku', data=data, hosts=self.url)
        apiTestResult(api='/admin/supplier/list-sku', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_page(self, city_=None, county_=None, enabled_=None, name_=None, pn_=None, province_=None, ps_=None, supplierType_=None):
        if self.user is None:
            data = {'city': city_, 'county': county_, 'enabled': enabled_, 'name': name_, 'pn': pn_, 'province': province_, 'ps': ps_, 'supplierType': supplierType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'city': city_, 'county': county_, 'enabled': enabled_, 'name': name_, 'pn': pn_, 'province': province_, 'ps': ps_, 'supplierType': supplierType_}
        response = self.request.post(url=self.url+'/admin/supplier/page', data=data, hosts=self.url)
        apiTestResult(api='/admin/supplier/page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_record(self, pn_=None, ps_=None, supplierId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'supplierId': supplierId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'supplierId': supplierId_}
        response = self.request.post(url=self.url+'/admin/supplier/record', data=data, hosts=self.url)
        apiTestResult(api='/admin/supplier/record', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_sys_dict_list(self, dictCode_=None, dictKey_=None):
        if self.user is None:
            data = {'dictCode': dictCode_, 'dictKey': dictKey_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'dictCode': dictCode_, 'dictKey': dictKey_}
        response = self.request.post(url=self.url+'/admin/sys-dict/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/sys-dict/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_sys_dict_page(self, pn_=None, ps_=None, dictCode_=None, dictKey_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'dictCode': dictCode_, 'dictKey': dictKey_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'dictCode': dictCode_, 'dictKey': dictKey_}
        response = self.request.post(url=self.url+'/admin/sys-dict/page', data=data, hosts=self.url)
        apiTestResult(api='/admin/sys-dict/page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_type_dict_list_by_type(self, type_=None):
        if self.user is None:
            data = {'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'type': type_}
        response = self.request.post(url=self.url+'/admin/type-dict/list-by-type', data=data, hosts=self.url)
        apiTestResult(api='/admin/type-dict/list-by-type', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_add(self, code_=None, name_=None, type_=None, lng_=None, lat_=None, province_=None, city_=None, county_=None, address_=None, area_=None, capacity_=None, goodsTypeIds_=None, managerIds_=None, leaseStartTime_=None, leaseEndTime_=None, landlord_=None, landlordPhone_=None, rent_=None, rentUnit_=None, remark_=None, imgUrls_=None):
        if self.user is None:
            data = {'code': code_, 'name': name_, 'type': type_, 'lng': lng_, 'lat': lat_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'area': area_, 'capacity': capacity_, 'goodsTypeIds': goodsTypeIds_, 'managerIds': managerIds_, 'leaseStartTime': leaseStartTime_, 'leaseEndTime': leaseEndTime_, 'landlord': landlord_, 'landlordPhone': landlordPhone_, 'rent': rent_, 'rentUnit': rentUnit_, 'remark': remark_, 'imgUrls': imgUrls_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'name': name_, 'type': type_, 'lng': lng_, 'lat': lat_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'area': area_, 'capacity': capacity_, 'goodsTypeIds': goodsTypeIds_, 'managerIds': managerIds_, 'leaseStartTime': leaseStartTime_, 'leaseEndTime': leaseEndTime_, 'landlord': landlord_, 'landlordPhone': landlordPhone_, 'rent': rent_, 'rentUnit': rentUnit_, 'remark': remark_, 'imgUrls': imgUrls_}
        response = self.request.post(url=self.url+'/admin/warehouse/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_in_warehouse(self, codes_=None, warehouseId_=None):
        if self.user is None:
            data = {'codes': codes_, 'warehouseId': warehouseId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'codes': codes_, 'warehouseId': warehouseId_}
        response = self.request.post(url=self.url+'/admin/warehouse/in-warehouse', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/in-warehouse', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouse/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_list_owner(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouse/list-owner', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/list-owner', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_out_warehouse(self, id_=None, codes_=None):
        if self.user is None:
            data = {'id': id_, 'codes': codes_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'codes': codes_}
        response = self.request.post(url=self.url+'/admin/warehouse/out-warehouse', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/out-warehouse', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_page(self, pn_=None, ps_=None, code_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/warehouse/page', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_page_record(self, pn_=None, ps_=None, warehouseId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'warehouseId': warehouseId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'warehouseId': warehouseId_}
        response = self.request.post(url=self.url+'/admin/warehouse/page-record', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/page-record', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_stock(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/stock', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/stock', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_inner_allocate_asset_apply(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/inner/allocate/asset-apply', data=data, hosts=self.url)
        apiTestResult(api='/api/inner/allocate/asset-apply', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_inner_allocate_code_apply(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/inner/allocate/code-apply', data=data, hosts=self.url)
        apiTestResult(api='/api/inner/allocate/code-apply', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_inner_sync_asset(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/inner/sync/asset', data=data, hosts=self.url)
        apiTestResult(api='/api/inner/sync/asset', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_inner_sync_supplier(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/inner/sync/supplier', data=data, hosts=self.url)
        apiTestResult(api='/api/inner/sync/supplier', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_open_asset_asset_check(self, checkType_=None, codeList_=None, userId_=None, userRole_=None):
        if self.user is None:
            data = {'checkType': checkType_, 'codeList': codeList_, 'userId': userId_, 'userRole': userRole_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'checkType': checkType_, 'codeList': codeList_, 'userId': userId_, 'userRole': userRole_}
        response = self.request.post(url=self.url+'/api/open/asset/asset-check', data=data, hosts=self.url)
        apiTestResult(api='/api/open/asset/asset-check', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_open_asset_bee_friend_number(self, productCode_=None, userId_=None):
        if self.user is None:
            data = {'productCode': productCode_, 'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productCode': productCode_, 'userId': userId_}
        response = self.request.post(url=self.url+'/api/open/asset/bee-friend-number', data=data, hosts=self.url)
        apiTestResult(api='/api/open/asset/bee-friend-number', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_open_asset_get_grant_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/api/open/asset/get-grant-detail', data=data, hosts=self.url)
        apiTestResult(api='/api/open/asset/get-grant-detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_open_asset_get_recovery_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/api/open/asset/get-recovery-detail', data=data, hosts=self.url)
        apiTestResult(api='/api/open/asset/get-recovery-detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_open_asset_grant_page(self, beekeeperId_=None, pn_=None, ps_=None):
        if self.user is None:
            data = {'beekeeperId': beekeeperId_, 'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'beekeeperId': beekeeperId_, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/api/open/asset/grant-page', data=data, hosts=self.url)
        apiTestResult(api='/api/open/asset/grant-page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_open_asset_list_bee_friend(self, productCode_=None, userId_=None):
        if self.user is None:
            data = {'productCode': productCode_, 'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productCode': productCode_, 'userId': userId_}
        response = self.request.post(url=self.url+'/api/open/asset/list-bee-friend', data=data, hosts=self.url)
        apiTestResult(api='/api/open/asset/list-bee-friend', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_open_asset_page_grant_Number(self, bookEndTime_=None, bookStartTime_=None, city_=None, county_=None, pn_=None, province_=None, ps_=None, recoveryEndTime_=None, recoveryStartTime_=None, userIdList_=None):
        if self.user is None:
            data = {'bookEndTime': bookEndTime_, 'bookStartTime': bookStartTime_, 'city': city_, 'county': county_, 'pn': pn_, 'province': province_, 'ps': ps_, 'recoveryEndTime': recoveryEndTime_, 'recoveryStartTime': recoveryStartTime_, 'userIdList': userIdList_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'bookEndTime': bookEndTime_, 'bookStartTime': bookStartTime_, 'city': city_, 'county': county_, 'pn': pn_, 'province': province_, 'ps': ps_, 'recoveryEndTime': recoveryEndTime_, 'recoveryStartTime': recoveryStartTime_, 'userIdList': userIdList_}
        response = self.request.post(url=self.url+'/api/open/asset/page-grant-Number', data=data, hosts=self.url)
        apiTestResult(api='/api/open/asset/page-grant-Number', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_open_asset_page_recovery_Number(self, city_=None, county_=None, pn_=None, province_=None, ps_=None, recoveryEndTime_=None, recoveryStartTime_=None, recoveryType_=None, userIdList_=None):
        if self.user is None:
            data = {'city': city_, 'county': county_, 'pn': pn_, 'province': province_, 'ps': ps_, 'recoveryEndTime': recoveryEndTime_, 'recoveryStartTime': recoveryStartTime_, 'recoveryType': recoveryType_, 'userIdList': userIdList_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'city': city_, 'county': county_, 'pn': pn_, 'province': province_, 'ps': ps_, 'recoveryEndTime': recoveryEndTime_, 'recoveryStartTime': recoveryStartTime_, 'recoveryType': recoveryType_, 'userIdList': userIdList_}
        response = self.request.post(url=self.url+'/api/open/asset/page-recovery-Number', data=data, hosts=self.url)
        apiTestResult(api='/api/open/asset/page-recovery-Number', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_open_asset_query(self, assetCode_=None):
        if self.user is None:
            data = {'assetCode': assetCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'assetCode': assetCode_}
        response = self.request.post(url=self.url+'/api/open/asset/query', data=data, hosts=self.url)
        apiTestResult(api='/api/open/asset/query', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_open_asset_recovery(self, address_=None, apiaryId_=None, bizNo_=None, codes_=None, receiverId_=None, recoveryReason_=None, remark_=None, senderId_=None, transferTime_=None):
        if self.user is None:
            data = {'address': address_, 'apiaryId': apiaryId_, 'bizNo': bizNo_, 'codes': codes_, 'receiverId': receiverId_, 'recoveryReason': recoveryReason_, 'remark': remark_, 'senderId': senderId_, 'transferTime': transferTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'address': address_, 'apiaryId': apiaryId_, 'bizNo': bizNo_, 'codes': codes_, 'receiverId': receiverId_, 'recoveryReason': recoveryReason_, 'remark': remark_, 'senderId': senderId_, 'transferTime': transferTime_}
        response = self.request.post(url=self.url+'/api/open/asset/recovery', data=data, hosts=self.url)
        apiTestResult(api='/api/open/asset/recovery', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_open_asset_recovery_page(self, beekeeperIds_=None, city_=None, county_=None, endTime_=None, pn_=None, province_=None, ps_=None, staffId_=None, startTime_=None):
        if self.user is None:
            data = {'beekeeperIds': beekeeperIds_, 'city': city_, 'county': county_, 'endTime': endTime_, 'pn': pn_, 'province': province_, 'ps': ps_, 'staffId': staffId_, 'startTime': startTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'beekeeperIds': beekeeperIds_, 'city': city_, 'county': county_, 'endTime': endTime_, 'pn': pn_, 'province': province_, 'ps': ps_, 'staffId': staffId_, 'startTime': startTime_}
        response = self.request.post(url=self.url+'/api/open/asset/recovery-page', data=data, hosts=self.url)
        apiTestResult(api='/api/open/asset/recovery-page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_open_asset_transfer(self, action_=None, address_=None, assets_=None, bizNo_=None, bookTime_=None, operatorId_=None, receiver_=None, receiverType_=None, remark_=None, sender_=None, senderType_=None):
        if self.user is None:
            data = {'action': action_, 'address': address_, 'assets': assets_, 'bizNo': bizNo_, 'bookTime': bookTime_, 'operatorId': operatorId_, 'receiver': receiver_, 'receiverType': receiverType_, 'remark': remark_, 'sender': sender_, 'senderType': senderType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'action': action_, 'address': address_, 'assets': assets_, 'bizNo': bizNo_, 'bookTime': bookTime_, 'operatorId': operatorId_, 'receiver': receiver_, 'receiverType': receiverType_, 'remark': remark_, 'sender': sender_, 'senderType': senderType_}
        response = self.request.post(url=self.url+'/api/open/asset/transfer', data=data, hosts=self.url)
        apiTestResult(api='/api/open/asset/transfer', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_allocate_apply(self, consigneeId_=None, productId_=None, total_=None, reason_=None):
        if self.user is None:
            data = {'consigneeId': consigneeId_, 'productId': productId_, 'total': total_, 'reason': reason_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'consigneeId': consigneeId_, 'productId': productId_, 'total': total_, 'reason': reason_}
        response = self.request.post(url=self.url+'/mobile/allocate/apply', data=data, hosts=self.url)
        apiTestResult(api='/mobile/allocate/apply', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_allocate_cancel(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/allocate/cancel', data=data, hosts=self.url)
        apiTestResult(api='/mobile/allocate/cancel', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_allocate_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/allocate/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/allocate/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_allocate_page(self, pn_=None, ps_=None, consigneeId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'consigneeId': consigneeId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'consigneeId': consigneeId_}
        response = self.request.post(url=self.url+'/mobile/allocate/page', data=data, hosts=self.url)
        apiTestResult(api='/mobile/allocate/page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_add(self, consigneeId_=None, consigneeType_=None, productId_=None, total_=None, reason_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'consigneeId': consigneeId_, 'consigneeType': consigneeType_, 'productId': productId_, 'total': total_, 'reason': reason_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'consigneeId': consigneeId_, 'consigneeType': consigneeType_, 'productId': productId_, 'total': total_, 'reason': reason_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/mobile/apply/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/apply/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_cancel(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/apply/cancel', data=data, hosts=self.url)
        apiTestResult(api='/mobile/apply/cancel', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_confirm_receive(self, applyId_=None, receiveTime_=None, codes_=None):
        if self.user is None:
            data = {'applyId': applyId_, 'receiveTime': receiveTime_, 'codes': codes_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_, 'receiveTime': receiveTime_, 'codes': codes_}
        response = self.request.post(url=self.url+'/mobile/apply/confirm-receive', data=data, hosts=self.url)
        apiTestResult(api='/mobile/apply/confirm-receive', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/apply/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/apply/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_ex_warehouse(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/apply/ex-warehouse', data=data, hosts=self.url)
        apiTestResult(api='/mobile/apply/ex-warehouse', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_page(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/mobile/apply/page', data=data, hosts=self.url)
        apiTestResult(api='/mobile/apply/page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_apply_receive_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/apply/receive-detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/apply/receive-detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_asset_check_code_check(self, supplierId_=None, codes_=None):
        if self.user is None:
            data = {'supplierId': supplierId_, 'codes': codes_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'supplierId': supplierId_, 'codes': codes_}
        response = self.request.post(url=self.url+'/mobile/asset-check/code-check', data=data, hosts=self.url)
        apiTestResult(api='/mobile/asset-check/code-check', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_asset_check_page(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/mobile/asset-check/page', data=data, hosts=self.url)
        apiTestResult(api='/mobile/asset-check/page', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_asset_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/asset/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/asset/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_asset_launch_list(self, pn_=None, ps_=None, bookStartTime_=None, bookEndTime_=None, recoveryStartTime_=None, recoveryEndTime_=None, province_=None, city_=None, county_=None, searchKey_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'bookStartTime': bookStartTime_, 'bookEndTime': bookEndTime_, 'recoveryStartTime': recoveryStartTime_, 'recoveryEndTime': recoveryEndTime_, 'province': province_, 'city': city_, 'county': county_, 'searchKey': searchKey_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'bookStartTime': bookStartTime_, 'bookEndTime': bookEndTime_, 'recoveryStartTime': recoveryStartTime_, 'recoveryEndTime': recoveryEndTime_, 'province': province_, 'city': city_, 'county': county_, 'searchKey': searchKey_}
        response = self.request.post(url=self.url+'/mobile/asset/launch-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/asset/launch-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_asset_list_owner(self, productCode_=None, userId_=None):
        if self.user is None:
            data = {'productCode': productCode_, 'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productCode': productCode_, 'userId': userId_}
        response = self.request.post(url=self.url+'/mobile/asset/list-owner', data=data, hosts=self.url)
        apiTestResult(api='/mobile/asset/list-owner', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_asset_list_recovery_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/asset/list-recovery-detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/asset/list-recovery-detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_asset_page_grant(self, pn_=None, ps_=None, bookStartTime_=None, bookEndTime_=None, recoveryStartTime_=None, recoveryEndTime_=None, province_=None, city_=None, county_=None, searchKey_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'bookStartTime': bookStartTime_, 'bookEndTime': bookEndTime_, 'recoveryStartTime': recoveryStartTime_, 'recoveryEndTime': recoveryEndTime_, 'province': province_, 'city': city_, 'county': county_, 'searchKey': searchKey_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'bookStartTime': bookStartTime_, 'bookEndTime': bookEndTime_, 'recoveryStartTime': recoveryStartTime_, 'recoveryEndTime': recoveryEndTime_, 'province': province_, 'city': city_, 'county': county_, 'searchKey': searchKey_}
        response = self.request.post(url=self.url+'/mobile/asset/page-grant', data=data, hosts=self.url)
        apiTestResult(api='/mobile/asset/page-grant', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_asset_transfer(self, address_=None, apiaryId_=None, bizNo_=None, codes_=None, receiverId_=None, receiverRole_=None, recoveryDate_=None, remark_=None, senderRole_=None, transferTime_=None):
        if self.user is None:
            data = {'address': address_, 'apiaryId': apiaryId_, 'bizNo': bizNo_, 'codes': codes_, 'receiverId': receiverId_, 'receiverRole': receiverRole_, 'recoveryDate': recoveryDate_, 'remark': remark_, 'senderRole': senderRole_, 'transferTime': transferTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'address': address_, 'apiaryId': apiaryId_, 'bizNo': bizNo_, 'codes': codes_, 'receiverId': receiverId_, 'receiverRole': receiverRole_, 'recoveryDate': recoveryDate_, 'remark': remark_, 'senderRole': senderRole_, 'transferTime': transferTime_}
        response = self.request.post(url=self.url+'/mobile/asset/transfer', data=data, hosts=self.url)
        apiTestResult(api='/mobile/asset/transfer', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_offline_download_grant(self, batchIds_=None):
        if self.user is None:
            data = {'batchIds': batchIds_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'batchIds': batchIds_}
        response = self.request.post(url=self.url+'/mobile/offline/download-grant', data=data, hosts=self.url)
        apiTestResult(api='/mobile/offline/download-grant', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_offline_page_grant(self, pn_=None, ps_=None, bookStartTime_=None, bookEndTime_=None, recoveryStartTime_=None, recoveryEndTime_=None, province_=None, city_=None, county_=None, searchKey_=None, notIncludeIds_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'bookStartTime': bookStartTime_, 'bookEndTime': bookEndTime_, 'recoveryStartTime': recoveryStartTime_, 'recoveryEndTime': recoveryEndTime_, 'province': province_, 'city': city_, 'county': county_, 'searchKey': searchKey_, 'notIncludeIds': notIncludeIds_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'bookStartTime': bookStartTime_, 'bookEndTime': bookEndTime_, 'recoveryStartTime': recoveryStartTime_, 'recoveryEndTime': recoveryEndTime_, 'province': province_, 'city': city_, 'county': county_, 'searchKey': searchKey_, 'notIncludeIds': notIncludeIds_}
        response = self.request.post(url=self.url+'/mobile/offline/page-grant', data=data, hosts=self.url)
        apiTestResult(api='/mobile/offline/page-grant', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_product_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/product/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/product/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_supplier_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/supplier/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/supplier/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_type_dict_list_by_type(self, type_=None):
        if self.user is None:
            data = {'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'type': type_}
        response = self.request.post(url=self.url+'/mobile/type-dict/list-by-type', data=data, hosts=self.url)
        apiTestResult(api='/mobile/type-dict/list-by-type', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_id_check(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/warehouse/id-check', data=data, hosts=self.url)
        apiTestResult(api='/mobile/warehouse/id-check', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_in_warehouse(self, codes_=None, warehouseId_=None):
        if self.user is None:
            data = {'codes': codes_, 'warehouseId': warehouseId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'codes': codes_, 'warehouseId': warehouseId_}
        response = self.request.post(url=self.url+'/mobile/warehouse/in-warehouse', data=data, hosts=self.url)
        apiTestResult(api='/mobile/warehouse/in-warehouse', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_init(self, codes_=None, warehouseId_=None, haveRfid_=None, supplierId_=None):
        if self.user is None:
            data = {'codes': codes_, 'warehouseId': warehouseId_, 'haveRfid': haveRfid_, 'supplierId': supplierId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'codes': codes_, 'warehouseId': warehouseId_, 'haveRfid': haveRfid_, 'supplierId': supplierId_}
        response = self.request.post(url=self.url+'/mobile/warehouse/init', data=data, hosts=self.url)
        apiTestResult(api='/mobile/warehouse/init', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_list_owner(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/warehouse/list-owner', data=data, hosts=self.url)
        apiTestResult(api='/mobile/warehouse/list-owner', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_list_stock(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/warehouse/list-stock', data=data, hosts=self.url)
        apiTestResult(api='/mobile/warehouse/list-stock', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_out_warehouse(self, id_=None, codes_=None):
        if self.user is None:
            data = {'id': id_, 'codes': codes_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'codes': codes_}
        response = self.request.post(url=self.url+'/mobile/warehouse/out-warehouse', data=data, hosts=self.url)
        apiTestResult(api='/mobile/warehouse/out-warehouse', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_warehouse_page_ex_warehouse(self, pn_=None, ps_=None, warehouseId_=None, applyNo_=None, status_=None, productId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'warehouseId': warehouseId_, 'applyNo': applyNo_, 'status': status_, 'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'warehouseId': warehouseId_, 'applyNo': applyNo_, 'status': status_, 'productId': productId_}
        response = self.request.post(url=self.url+'/mobile/warehouse/page-ex-warehouse', data=data, hosts=self.url)
        apiTestResult(api='/mobile/warehouse/page-ex-warehouse', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))
