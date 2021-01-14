#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
from utils.checkApiChanges.checher.apiTestResult import apiTestResult
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
        apiTestResult(api='/admin/company/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_employee_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/employee/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/employee/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_erp_uncleared_order_purchase_list(self, companyCode_=None):
        if self.user is None:
            data = {'companyCode': companyCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'companyCode': companyCode_}
        response = self.request.post(url=self.url+'/admin/erp/uncleared/order/purchase-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/erp/uncleared/order/purchase-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_erp_uncleared_order_return_list(self, companyCode_=None):
        if self.user is None:
            data = {'companyCode': companyCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'companyCode': companyCode_}
        response = self.request.post(url=self.url+'/admin/erp/uncleared/order/return-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/erp/uncleared/order/return-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_product_page_list(self, pn_=None, ps_=None, orderCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/invoice-product/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/invoice-product/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/invoice/count', data=data, hosts=self.url)
        apiTestResult(api='/admin/invoice/count', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_detail(self, orderCode_=None):
        if self.user is None:
            data = {'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/invoice/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/invoice/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_notice_add(self, relevanceCode_=None, type_=None, source_=None, warehouseCode_=None, purchasingCompany_=None, possessor_=None, supplier_=None, remark_=None, itemList_=None):
        if self.user is None:
            data = {'relevanceCode': relevanceCode_, 'type': type_, 'source': source_, 'warehouseCode': warehouseCode_, 'purchasingCompany': purchasingCompany_, 'possessor': possessor_, 'supplier': supplier_, 'remark': remark_, 'itemList': itemList_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'relevanceCode': relevanceCode_, 'type': type_, 'source': source_, 'warehouseCode': warehouseCode_, 'purchasingCompany': purchasingCompany_, 'possessor': possessor_, 'supplier': supplier_, 'remark': remark_, 'itemList': itemList_}
        response = self.request.post(url=self.url+'/admin/invoice/notice/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/invoice/notice/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_notice_cancel(self, orderCode_=None):
        if self.user is None:
            data = {'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/invoice/notice/cancel', data=data, hosts=self.url)
        apiTestResult(api='/admin/invoice/notice/cancel', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_notice_confirm(self, orderCode_=None):
        if self.user is None:
            data = {'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/invoice/notice/confirm', data=data, hosts=self.url)
        apiTestResult(api='/admin/invoice/notice/confirm', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_notice_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/invoice/notice/count', data=data, hosts=self.url)
        apiTestResult(api='/admin/invoice/notice/count', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_notice_detail(self, orderCode_=None):
        if self.user is None:
            data = {'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/invoice/notice/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/invoice/notice/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_notice_edit(self, orderCode_=None, warehouseCode_=None, purchasingCompany_=None, remark_=None):
        if self.user is None:
            data = {'orderCode': orderCode_, 'warehouseCode': warehouseCode_, 'purchasingCompany': purchasingCompany_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderCode': orderCode_, 'warehouseCode': warehouseCode_, 'purchasingCompany': purchasingCompany_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/invoice/notice/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/invoice/notice/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_notice_page_list(self, pn_=None, ps_=None, orderCode_=None, relevanceCode_=None, status_=None, type_=None, warehouseCode_=None, operatorId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, 'relevanceCode': relevanceCode_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'operatorId': operatorId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, 'relevanceCode': relevanceCode_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'operatorId': operatorId_}
        response = self.request.post(url=self.url+'/admin/invoice/notice/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/invoice/notice/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_notice_product_page_list(self, pn_=None, ps_=None, orderCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/invoice/notice/product/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/invoice/notice/product/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_page_list(self, pn_=None, ps_=None, orderCode_=None, status_=None, type_=None, warehouseCode_=None, operatorId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'operatorId': operatorId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'operatorId': operatorId_}
        response = self.request.post(url=self.url+'/admin/invoice/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/invoice/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_sync_erp(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/admin/invoice/sync-erp', data=data, hosts=self.url)
        apiTestResult(api='/admin/invoice/sync-erp', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_item_detail_page_list(self, pn_=None, ps_=None, tracingCode_=None, noticeCode_=None, invoiceCode_=None, moveCode_=None, productCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'tracingCode': tracingCode_, 'noticeCode': noticeCode_, 'invoiceCode': invoiceCode_, 'moveCode': moveCode_, 'productCode': productCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'tracingCode': tracingCode_, 'noticeCode': noticeCode_, 'invoiceCode': invoiceCode_, 'moveCode': moveCode_, 'productCode': productCode_}
        response = self.request.post(url=self.url+'/admin/item-detail/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/item-detail/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_lotRule_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/lotRule/get', data=data, hosts=self.url)
        apiTestResult(api='/admin/lotRule/get', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_operation_log_list(self, bizCode_=None, biz_=None):
        if self.user is None:
            data = {'bizCode': bizCode_, 'biz': biz_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'bizCode': bizCode_, 'biz': biz_}
        response = self.request.post(url=self.url+'/admin/operation-log/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/operation-log/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_order_erp_sync_log_list(self, orderCode_=None):
        if self.user is None:
            data = {'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/order/erp-sync-log/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/order/erp-sync-log/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_pick_doc_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/pick-doc/count', data=data, hosts=self.url)
        apiTestResult(api='/admin/pick-doc/count', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_pick_doc_detail(self, pn_=None, ps_=None, orderCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/pick-doc/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/pick-doc/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_pick_doc_page_list(self, pn_=None, ps_=None, orderCode_=None, status_=None, type_=None, warehouseCode_=None, operatorId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'operatorId': operatorId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'operatorId': operatorId_}
        response = self.request.post(url=self.url+'/admin/pick-doc/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/pick-doc/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_pick_product_page_list(self, pn_=None, ps_=None, orderCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/pick-product/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/pick-product/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_page_list(self, pn_=None, ps_=None, code_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/product/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/product/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_receipt_cancel(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/admin/receipt/cancel', data=data, hosts=self.url)
        apiTestResult(api='/admin/receipt/cancel', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_receipt_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/receipt/count', data=data, hosts=self.url)
        apiTestResult(api='/admin/receipt/count', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_receipt_detail(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/admin/receipt/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/receipt/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_receipt_notice_add(self, relevanceCode_=None, source_=None, type_=None, warehouseCode_=None, purchasingCompany_=None, supplier_=None, supplierName_=None, remark_=None, erpType_=None, productInfo_=None):
        if self.user is None:
            data = {'relevanceCode': relevanceCode_, 'source': source_, 'type': type_, 'warehouseCode': warehouseCode_, 'purchasingCompany': purchasingCompany_, 'supplier': supplier_, 'supplierName': supplierName_, 'remark': remark_, 'erpType': erpType_, 'productInfo': productInfo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'relevanceCode': relevanceCode_, 'source': source_, 'type': type_, 'warehouseCode': warehouseCode_, 'purchasingCompany': purchasingCompany_, 'supplier': supplier_, 'supplierName': supplierName_, 'remark': remark_, 'erpType': erpType_, 'productInfo': productInfo_}
        response = self.request.post(url=self.url+'/admin/receipt/notice/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/receipt/notice/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_receipt_notice_cancel(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/admin/receipt/notice/cancel', data=data, hosts=self.url)
        apiTestResult(api='/admin/receipt/notice/cancel', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_receipt_notice_confirm(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/admin/receipt/notice/confirm', data=data, hosts=self.url)
        apiTestResult(api='/admin/receipt/notice/confirm', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_receipt_notice_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/receipt/notice/count', data=data, hosts=self.url)
        apiTestResult(api='/admin/receipt/notice/count', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_receipt_notice_detail(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/admin/receipt/notice/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/receipt/notice/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_receipt_notice_page_list(self, pn_=None, ps_=None, code_=None, status_=None, type_=None, warehouseCode_=None, creatorId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'creatorId': creatorId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'creatorId': creatorId_}
        response = self.request.post(url=self.url+'/admin/receipt/notice/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/receipt/notice/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_receipt_notice_product_page_list(self, pn_=None, ps_=None, orderCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/receipt/notice/product/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/receipt/notice/product/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_receipt_notice_update(self, code_=None, warehouseCode_=None, purchasingCompany_=None, remark_=None):
        if self.user is None:
            data = {'code': code_, 'warehouseCode': warehouseCode_, 'purchasingCompany': purchasingCompany_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'warehouseCode': warehouseCode_, 'purchasingCompany': purchasingCompany_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/receipt/notice/update', data=data, hosts=self.url)
        apiTestResult(api='/admin/receipt/notice/update', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_receipt_page_list(self, pn_=None, ps_=None, code_=None, status_=None, type_=None, warehouseCode_=None, creatorId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'code': code_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'creatorId': creatorId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'code': code_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'creatorId': creatorId_}
        response = self.request.post(url=self.url+'/admin/receipt/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/receipt/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_receipt_product_page_list(self, pn_=None, ps_=None, orderCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/receipt/product/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/receipt/product/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_receipt_sync_erp(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/admin/receipt/sync-erp', data=data, hosts=self.url)
        apiTestResult(api='/admin/receipt/sync-erp', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_receipt_tracing_page_list(self, pn_=None, ps_=None, orderCode_=None, productCode_=None, tracingCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, 'productCode': productCode_, 'tracingCode': tracingCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, 'productCode': productCode_, 'tracingCode': tracingCode_}
        response = self.request.post(url=self.url+'/admin/receipt/tracing/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/receipt/tracing/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_list(self, companyCode_=None):
        if self.user is None:
            data = {'companyCode': companyCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'companyCode': companyCode_}
        response = self.request.post(url=self.url+'/admin/shop/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/shop/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_transfer_apply_add(self, relevanceCode_=None, source_=None, type_=None, fromOrg_=None, fromWarehouse_=None, toOrg_=None, toWarehouse_=None, possessor_=None, arriveTime_=None, remark_=None, itemList_=None):
        if self.user is None:
            data = {'relevanceCode': relevanceCode_, 'source': source_, 'type': type_, 'fromOrg': fromOrg_, 'fromWarehouse': fromWarehouse_, 'toOrg': toOrg_, 'toWarehouse': toWarehouse_, 'possessor': possessor_, 'arriveTime': arriveTime_, 'remark': remark_, 'itemList': itemList_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'relevanceCode': relevanceCode_, 'source': source_, 'type': type_, 'fromOrg': fromOrg_, 'fromWarehouse': fromWarehouse_, 'toOrg': toOrg_, 'toWarehouse': toWarehouse_, 'possessor': possessor_, 'arriveTime': arriveTime_, 'remark': remark_, 'itemList': itemList_}
        response = self.request.post(url=self.url+'/admin/transfer-apply/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/transfer-apply/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_transfer_apply_cancel(self, orderCode_=None, reason_=None):
        if self.user is None:
            data = {'orderCode': orderCode_, 'reason': reason_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderCode': orderCode_, 'reason': reason_}
        response = self.request.post(url=self.url+'/admin/transfer-apply/cancel', data=data, hosts=self.url)
        apiTestResult(api='/admin/transfer-apply/cancel', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_transfer_apply_confirm(self, orderCode_=None, transferMethod_=None, fromOrg_=None, fromWarehouse_=None):
        if self.user is None:
            data = {'orderCode': orderCode_, 'transferMethod': transferMethod_, 'fromOrg': fromOrg_, 'fromWarehouse': fromWarehouse_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderCode': orderCode_, 'transferMethod': transferMethod_, 'fromOrg': fromOrg_, 'fromWarehouse': fromWarehouse_}
        response = self.request.post(url=self.url+'/admin/transfer-apply/confirm', data=data, hosts=self.url)
        apiTestResult(api='/admin/transfer-apply/confirm', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_transfer_apply_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/transfer-apply/count', data=data, hosts=self.url)
        apiTestResult(api='/admin/transfer-apply/count', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_transfer_apply_detail(self, orderCode_=None):
        if self.user is None:
            data = {'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/transfer-apply/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/transfer-apply/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_transfer_apply_page_list(self, pn_=None, ps_=None, orderCode_=None, status_=None, type_=None, warehouseCode_=None, startArriveTime_=None, endArriveTime_=None, operatorId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'startArriveTime': startArriveTime_, 'endArriveTime': endArriveTime_, 'operatorId': operatorId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, 'status': status_, 'type': type_, 'warehouseCode': warehouseCode_, 'startArriveTime': startArriveTime_, 'endArriveTime': endArriveTime_, 'operatorId': operatorId_}
        response = self.request.post(url=self.url+'/admin/transfer-apply/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/transfer-apply/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_transfer_apply_reject(self, orderCode_=None, reason_=None):
        if self.user is None:
            data = {'orderCode': orderCode_, 'reason': reason_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderCode': orderCode_, 'reason': reason_}
        response = self.request.post(url=self.url+'/admin/transfer-apply/reject', data=data, hosts=self.url)
        apiTestResult(api='/admin/transfer-apply/reject', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_transfer_item_page_list(self, pn_=None, ps_=None, orderCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/admin/transfer-item/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/transfer-item/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_add(self, name_=None, outWarehouseCode_=None, companyCode_=None, shopCode_=None, warehouseTypeId_=None, contactId_=None, province_=None, city_=None, county_=None, lng_=None, lat_=None, address_=None, status_=None, isThird_=None, isVirtual_=None, remark_=None):
        if self.user is None:
            data = {'name': name_, 'outWarehouseCode': outWarehouseCode_, 'companyCode': companyCode_, 'shopCode': shopCode_, 'warehouseTypeId': warehouseTypeId_, 'contactId': contactId_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'address': address_, 'status': status_, 'isThird': isThird_, 'isVirtual': isVirtual_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'outWarehouseCode': outWarehouseCode_, 'companyCode': companyCode_, 'shopCode': shopCode_, 'warehouseTypeId': warehouseTypeId_, 'contactId': contactId_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'address': address_, 'status': status_, 'isThird': isThird_, 'isVirtual': isVirtual_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/warehouse/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_additional_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/additional-detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/additional-detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_additional_update(self, images_=None, id_=None, area_=None, capacity_=None, cargoType_=None):
        if self.user is None:
            data = {'images': images_, 'id': id_, 'area': area_, 'capacity': capacity_, 'cargoType': cargoType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'images': images_, 'id': id_, 'area': area_, 'capacity': capacity_, 'cargoType': cargoType_}
        response = self.request.post(url=self.url+'/admin/warehouse/additional-update', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/additional-update', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_add(self, warehouseId_=None, name_=None, outWarehouseAreaCode_=None, warehouseAreaTypeId_=None, location_=None, status_=None, remark_=None):
        if self.user is None:
            data = {'warehouseId': warehouseId_, 'name': name_, 'outWarehouseAreaCode': outWarehouseAreaCode_, 'warehouseAreaTypeId': warehouseAreaTypeId_, 'location': location_, 'status': status_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'warehouseId': warehouseId_, 'name': name_, 'outWarehouseAreaCode': outWarehouseAreaCode_, 'warehouseAreaTypeId': warehouseAreaTypeId_, 'location': location_, 'status': status_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/area/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_bind_warehouse(self, warehouseAreaIds_=None, warehouseId_=None):
        if self.user is None:
            data = {'warehouseAreaIds': warehouseAreaIds_, 'warehouseId': warehouseId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'warehouseAreaIds': warehouseAreaIds_, 'warehouseId': warehouseId_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/bind-warehouse', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/area/bind-warehouse', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouse/area/count', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/area/count', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/del', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/area/del', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/area/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_list(self, warehouseId_=None, isRelevanceWarehouse_=None):
        if self.user is None:
            data = {'warehouseId': warehouseId_, 'isRelevanceWarehouse': isRelevanceWarehouse_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'warehouseId': warehouseId_, 'isRelevanceWarehouse': isRelevanceWarehouse_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/area/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_page_list(self, pn_=None, ps_=None, nameOrCode_=None, status_=None, warehouseAreaTypeId_=None, warehouseNameOrCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'nameOrCode': nameOrCode_, 'status': status_, 'warehouseAreaTypeId': warehouseAreaTypeId_, 'warehouseNameOrCode': warehouseNameOrCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'nameOrCode': nameOrCode_, 'status': status_, 'warehouseAreaTypeId': warehouseAreaTypeId_, 'warehouseNameOrCode': warehouseNameOrCode_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/area/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_type_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouse/area/type/count', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/area/type/count', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_type_list(self, pn_=None, ps_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/type/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/area/type/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_type_page_list(self, pn_=None, ps_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/type/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/area/type/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_unbind_warehouse(self, warehouseId_=None, warehouseAreaId_=None):
        if self.user is None:
            data = {'warehouseId': warehouseId_, 'warehouseAreaId': warehouseAreaId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'warehouseId': warehouseId_, 'warehouseAreaId': warehouseAreaId_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/unbind-warehouse', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/area/unbind-warehouse', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_area_update(self, id_=None, warehouseId_=None, name_=None, outWarehouseAreaCode_=None, location_=None, status_=None, remark_=None):
        if self.user is None:
            data = {'id': id_, 'warehouseId': warehouseId_, 'name': name_, 'outWarehouseAreaCode': outWarehouseAreaCode_, 'location': location_, 'status': status_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'warehouseId': warehouseId_, 'name': name_, 'outWarehouseAreaCode': outWarehouseAreaCode_, 'location': location_, 'status': status_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/warehouse/area/update', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/area/update', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouse/count', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/count', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/del', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/del', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_employee_add(self, userIds_=None, warehouseId_=None):
        if self.user is None:
            data = {'userIds': userIds_, 'warehouseId': warehouseId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userIds': userIds_, 'warehouseId': warehouseId_}
        response = self.request.post(url=self.url+'/admin/warehouse/employee/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/employee/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_employee_del(self, warehouseEmployeeId_=None):
        if self.user is None:
            data = {'warehouseEmployeeId': warehouseEmployeeId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'warehouseEmployeeId': warehouseEmployeeId_}
        response = self.request.post(url=self.url+'/admin/warehouse/employee/del', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/employee/del', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_employee_list(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/employee/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/employee/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_erp_sync_log_list(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/erp-sync-log/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/erp-sync-log/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_list(self, status_=None, code_=None):
        if self.user is None:
            data = {'status': status_, 'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'status': status_, 'code': code_}
        response = self.request.post(url=self.url+'/admin/warehouse/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_monitor_bind(self, cameraCodes_=None, warehouseId_=None):
        if self.user is None:
            data = {'cameraCodes': cameraCodes_, 'warehouseId': warehouseId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cameraCodes': cameraCodes_, 'warehouseId': warehouseId_}
        response = self.request.post(url=self.url+'/admin/warehouse/monitor/bind', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/monitor/bind', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_monitor_camera_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouse/monitor/camera-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/monitor/camera-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_monitor_list(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/monitor/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/monitor/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_monitor_rename(self, id_=None, name_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/warehouse/monitor/rename', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/monitor/rename', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_monitor_unbind(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/monitor/unbind', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/monitor/unbind', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_page_list(self, pn_=None, ps_=None, nameOrCode_=None, status_=None, typeId_=None, companyName_=None, province_=None, city_=None, county_=None, adminNameOrPhone_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'nameOrCode': nameOrCode_, 'status': status_, 'typeId': typeId_, 'companyName': companyName_, 'province': province_, 'city': city_, 'county': county_, 'adminNameOrPhone': adminNameOrPhone_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'nameOrCode': nameOrCode_, 'status': status_, 'typeId': typeId_, 'companyName': companyName_, 'province': province_, 'city': city_, 'county': county_, 'adminNameOrPhone': adminNameOrPhone_}
        response = self.request.post(url=self.url+'/admin/warehouse/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_push_to_erp(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/push-to-erp', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/push-to-erp', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_third_config_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/warehouse/third-config/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/third-config/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_third_config_update(self, warehouseId_=None, systemAccount_=None, appKey_=None, appSecret_=None, systemApi_=None, leaseStartTime_=None, leaseEndTime_=None, rent_=None, rentUnit_=None):
        if self.user is None:
            data = {'warehouseId': warehouseId_, 'systemAccount': systemAccount_, 'appKey': appKey_, 'appSecret': appSecret_, 'systemApi': systemApi_, 'leaseStartTime': leaseStartTime_, 'leaseEndTime': leaseEndTime_, 'rent': rent_, 'rentUnit': rentUnit_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'warehouseId': warehouseId_, 'systemAccount': systemAccount_, 'appKey': appKey_, 'appSecret': appSecret_, 'systemApi': systemApi_, 'leaseStartTime': leaseStartTime_, 'leaseEndTime': leaseEndTime_, 'rent': rent_, 'rentUnit': rentUnit_}
        response = self.request.post(url=self.url+'/admin/warehouse/third-config/update', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/third-config/update', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_type_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/warehouse/type/count', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/type/count', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_type_list(self, pn_=None, ps_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/warehouse/type/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/type/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_type_page_list(self, pn_=None, ps_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/warehouse/type/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/type/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_warehouse_update(self, id_=None, name_=None, outWarehouseCode_=None, shopCode_=None, contactId_=None, province_=None, city_=None, county_=None, lng_=None, lat_=None, address_=None, status_=None, isThird_=None, isVirtual_=None, remark_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, 'outWarehouseCode': outWarehouseCode_, 'shopCode': shopCode_, 'contactId': contactId_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'address': address_, 'status': status_, 'isThird': isThird_, 'isVirtual': isVirtual_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_, 'outWarehouseCode': outWarehouseCode_, 'shopCode': shopCode_, 'contactId': contactId_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'address': address_, 'status': status_, 'isThird': isThird_, 'isVirtual': isVirtual_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/warehouse/update', data=data, hosts=self.url)
        apiTestResult(api='/admin/warehouse/update', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_asset_sync_archives(self, assetList_=None):
        if self.user is None:
            data = {'assetList': assetList_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'assetList': assetList_}
        response = self.request.post(url=self.url+'/api/asset-sync/archives', data=data, hosts=self.url)
        apiTestResult(api='/api/asset-sync/archives', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_bill_sync(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/bill/sync', data=data, hosts=self.url)
        apiTestResult(api='/api/bill/sync', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_invoice_notice_add_ck07(self, itemList_=None, possessor_=None, purchasingCompany_=None, relevanceCode_=None, remark_=None, source_=None, supplier_=None, type_=None, warehouseCode_=None):
        if self.user is None:
            data = {'itemList': itemList_, 'possessor': possessor_, 'purchasingCompany': purchasingCompany_, 'relevanceCode': relevanceCode_, 'remark': remark_, 'source': source_, 'supplier': supplier_, 'type': type_, 'warehouseCode': warehouseCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'itemList': itemList_, 'possessor': possessor_, 'purchasingCompany': purchasingCompany_, 'relevanceCode': relevanceCode_, 'remark': remark_, 'source': source_, 'supplier': supplier_, 'type': type_, 'warehouseCode': warehouseCode_}
        response = self.request.post(url=self.url+'/api/invoice/notice/add-ck07', data=data, hosts=self.url)
        apiTestResult(api='/api/invoice/notice/add-ck07', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_pos_sales_out(self, details_=None, possessor_=None, relevanceCode_=None, remark_=None, shopCode_=None, type_=None):
        if self.user is None:
            data = {'details': details_, 'possessor': possessor_, 'relevanceCode': relevanceCode_, 'remark': remark_, 'shopCode': shopCode_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'details': details_, 'possessor': possessor_, 'relevanceCode': relevanceCode_, 'remark': remark_, 'shopCode': shopCode_, 'type': type_}
        response = self.request.post(url=self.url+'/api/pos/sales-out', data=data, hosts=self.url)
        apiTestResult(api='/api/pos/sales-out', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_pos_shake_out(self, details_=None, possessor_=None, relevanceCode_=None, remark_=None, shopCode_=None, type_=None):
        if self.user is None:
            data = {'details': details_, 'possessor': possessor_, 'relevanceCode': relevanceCode_, 'remark': remark_, 'shopCode': shopCode_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'details': details_, 'possessor': possessor_, 'relevanceCode': relevanceCode_, 'remark': remark_, 'shopCode': shopCode_, 'type': type_}
        response = self.request.post(url=self.url+'/api/pos/shake-out', data=data, hosts=self.url)
        apiTestResult(api='/api/pos/shake-out', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_pos_supplement(self, arriveTime_=None, details_=None, possessor_=None, relevanceCode_=None, remark_=None, shopCode_=None, type_=None):
        if self.user is None:
            data = {'arriveTime': arriveTime_, 'details': details_, 'possessor': possessor_, 'relevanceCode': relevanceCode_, 'remark': remark_, 'shopCode': shopCode_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'arriveTime': arriveTime_, 'details': details_, 'possessor': possessor_, 'relevanceCode': relevanceCode_, 'remark': remark_, 'shopCode': shopCode_, 'type': type_}
        response = self.request.post(url=self.url+'/api/pos/supplement', data=data, hosts=self.url)
        apiTestResult(api='/api/pos/supplement', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_receipt_notice_asset_recycle(self, creatorId_=None, possessor_=None, purchasingCompany_=None, relevanceCode_=None, source_=None, supplier_=None, supplierName_=None, tracingCodes_=None, warehouseCode_=None):
        if self.user is None:
            data = {'creatorId': creatorId_, 'possessor': possessor_, 'purchasingCompany': purchasingCompany_, 'relevanceCode': relevanceCode_, 'source': source_, 'supplier': supplier_, 'supplierName': supplierName_, 'tracingCodes': tracingCodes_, 'warehouseCode': warehouseCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'creatorId': creatorId_, 'possessor': possessor_, 'purchasingCompany': purchasingCompany_, 'relevanceCode': relevanceCode_, 'source': source_, 'supplier': supplier_, 'supplierName': supplierName_, 'tracingCodes': tracingCodes_, 'warehouseCode': warehouseCode_}
        response = self.request.post(url=self.url+'/api/receipt/notice/asset-recycle', data=data, hosts=self.url)
        apiTestResult(api='/api/receipt/notice/asset-recycle', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_receipt_notice_sales_return(self, creatorId_=None, invoiceRelevanceCode_=None, receiptRelevanceCode_=None):
        if self.user is None:
            data = {'creatorId': creatorId_, 'invoiceRelevanceCode': invoiceRelevanceCode_, 'receiptRelevanceCode': receiptRelevanceCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'creatorId': creatorId_, 'invoiceRelevanceCode': invoiceRelevanceCode_, 'receiptRelevanceCode': receiptRelevanceCode_}
        response = self.request.post(url=self.url+'/api/receipt/notice/sales-return', data=data, hosts=self.url)
        apiTestResult(api='/api/receipt/notice/sales-return', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_receipt_notice_shake_honey(self, creatorId_=None, possessor_=None, relevanceCode_=None, remark_=None, shakeHoneyDate_=None, shakeHoneyTracings_=None, stopCode_=None):
        if self.user is None:
            data = {'creatorId': creatorId_, 'possessor': possessor_, 'relevanceCode': relevanceCode_, 'remark': remark_, 'shakeHoneyDate': shakeHoneyDate_, 'shakeHoneyTracings': shakeHoneyTracings_, 'stopCode': stopCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'creatorId': creatorId_, 'possessor': possessor_, 'relevanceCode': relevanceCode_, 'remark': remark_, 'shakeHoneyDate': shakeHoneyDate_, 'shakeHoneyTracings': shakeHoneyTracings_, 'stopCode': stopCode_}
        response = self.request.post(url=self.url+'/api/receipt/notice/shake-honey', data=data, hosts=self.url)
        apiTestResult(api='/api/receipt/notice/shake-honey', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_receipt_notice_standard(self, creatorId_=None, noticeProducts_=None, possessor_=None, purchasingCompany_=None, relevanceCode_=None, source_=None, supplier_=None, supplierName_=None, type_=None, warehouseCode_=None):
        if self.user is None:
            data = {'creatorId': creatorId_, 'noticeProducts': noticeProducts_, 'possessor': possessor_, 'purchasingCompany': purchasingCompany_, 'relevanceCode': relevanceCode_, 'source': source_, 'supplier': supplier_, 'supplierName': supplierName_, 'type': type_, 'warehouseCode': warehouseCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'creatorId': creatorId_, 'noticeProducts': noticeProducts_, 'possessor': possessor_, 'purchasingCompany': purchasingCompany_, 'relevanceCode': relevanceCode_, 'source': source_, 'supplier': supplier_, 'supplierName': supplierName_, 'type': type_, 'warehouseCode': warehouseCode_}
        response = self.request.post(url=self.url+'/api/receipt/notice/standard', data=data, hosts=self.url)
        apiTestResult(api='/api/receipt/notice/standard', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_receipt_quality_deduction(self, deductionProducts_=None, isDeduction_=None, orderCode_=None):
        if self.user is None:
            data = {'deductionProducts': deductionProducts_, 'isDeduction': isDeduction_, 'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'deductionProducts': deductionProducts_, 'isDeduction': isDeduction_, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/api/receipt/quality/deduction', data=data, hosts=self.url)
        apiTestResult(api='/api/receipt/quality/deduction', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_receipt_task_sync_erp(self, codes_=None):
        if self.user is None:
            data = {'codes': codes_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'codes': codes_}
        response = self.request.post(url=self.url+'/api/receipt/task/sync-erp', data=data, hosts=self.url)
        apiTestResult(api='/api/receipt/task/sync-erp', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_sku_sync_archives(self, skuList_=None):
        if self.user is None:
            data = {'skuList': skuList_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'skuList': skuList_}
        response = self.request.post(url=self.url+'/api/sku-sync/archives', data=data, hosts=self.url)
        apiTestResult(api='/api/sku-sync/archives', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_warehouse_list(self, status_=None):
        if self.user is None:
            data = {'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'status': status_}
        response = self.request.post(url=self.url+'/api/warehouse/list', data=data, hosts=self.url)
        apiTestResult(api='/api/warehouse/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _common_config_list(self, types_=None, code_=None):
        if self.user is None:
            data = {'types': types_, 'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'types': types_, 'code': code_}
        response = self.request.post(url=self.url+'/common/config/list', data=data, hosts=self.url)
        apiTestResult(api='/common/config/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _common_enum_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/common/enum/list', data=data, hosts=self.url)
        apiTestResult(api='/common/enum/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _common_file_upload_public_file(self, file_=None, type_=None):
        if self.user is None:
            data = {'file': file_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'file': file_, 'type': type_}
        response = self.request.post(url=self.url+'/common/file/upload/public-file', data=data, hosts=self.url)
        apiTestResult(api='/common/file/upload/public-file', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _common_file_upload_public_pic(self, file_=None, type_=None):
        if self.user is None:
            data = {'file': file_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'file': file_, 'type': type_}
        response = self.request.post(url=self.url+'/common/file/upload/public-pic', data=data, hosts=self.url)
        apiTestResult(api='/common/file/upload/public-pic', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_inventory_shop_list(self, shopCode_=None, warehouseType_=None, productType_=None):
        if self.user is None:
            data = {'shopCode': shopCode_, 'warehouseType': warehouseType_, 'productType': productType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'shopCode': shopCode_, 'warehouseType': warehouseType_, 'productType': productType_}
        response = self.request.post(url=self.url+'/mobile/inventory/shop/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/inventory/shop/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_move_pda_pick_detail_list(self, orderCode_=None):
        if self.user is None:
            data = {'orderCode': orderCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderCode': orderCode_}
        response = self.request.post(url=self.url+'/mobile/move/pda/pick-detail-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/move/pda/pick-detail-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_move_pda_pick_list(self, status_=None):
        if self.user is None:
            data = {'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'status': status_}
        response = self.request.post(url=self.url+'/mobile/move/pda/pick-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/move/pda/pick-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_move_pda_pick_submit(self, invoiceCode_=None, code_=None, productJson_=None):
        if self.user is None:
            data = {'invoiceCode': invoiceCode_, 'code': code_, 'productJson': productJson_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'invoiceCode': invoiceCode_, 'code': code_, 'productJson': productJson_}
        response = self.request.post(url=self.url+'/mobile/move/pda/pick-submit', data=data, hosts=self.url)
        apiTestResult(api='/mobile/move/pda/pick-submit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_product_get_by_tracing_code(self, tracingCode_=None, isAsset_=None):
        if self.user is None:
            data = {'tracingCode': tracingCode_, 'isAsset': isAsset_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'tracingCode': tracingCode_, 'isAsset': isAsset_}
        response = self.request.post(url=self.url+'/mobile/product/get-by-tracing-code', data=data, hosts=self.url)
        apiTestResult(api='/mobile/product/get-by-tracing-code', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_receipt_pda_list(self, pn_=None, ps_=None, status_=None, type_=None, shopCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'status': status_, 'type': type_, 'shopCode': shopCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'status': status_, 'type': type_, 'shopCode': shopCode_}
        response = self.request.post(url=self.url+'/mobile/receipt/pda/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/receipt/pda/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_receipt_pda_product_list(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/mobile/receipt/pda/product/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/receipt/pda/product/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_receipt_pda_product_submit(self, code_=None, productInfo_=None, qualityResult_=None, receiptQualityInfo_=None):
        if self.user is None:
            data = {'code': code_, 'productInfo': productInfo_, 'qualityResult': qualityResult_, 'receiptQualityInfo': receiptQualityInfo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'productInfo': productInfo_, 'qualityResult': qualityResult_, 'receiptQualityInfo': receiptQualityInfo_}
        response = self.request.post(url=self.url+'/mobile/receipt/pda/product/submit', data=data, hosts=self.url)
        apiTestResult(api='/mobile/receipt/pda/product/submit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))
