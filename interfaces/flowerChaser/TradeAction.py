#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
import json


class TradeAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('FC_TRADE')

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

    def _admin_contract_abort(self, id_=None, abortType_=None):
        if self.user is None:
            data = {'id': id_, 'abortType': abortType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'abortType': abortType_}
        response = self.request.post(url=self.url+'/admin/contract/abort', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_contract_audit(self, id_=None, status_=None, failReason_=None):
        if self.user is None:
            data = {'id': id_, 'status': status_, 'failReason': failReason_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'status': status_, 'failReason': failReason_}
        response = self.request.post(url=self.url+'/admin/contract/audit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_contract_detail(self, contractId_=None):
        if self.user is None:
            data = {'contractId': contractId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'contractId': contractId_}
        response = self.request.post(url=self.url+'/admin/contract/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_contract_list(self, typeList_=None, pn_=None, ps_=None, contractNo_=None, userKeyWord_=None, creatorKeyWord_=None, province_=None, city_=None, county_=None, signTimeStart_=None, signTimeEnd_=None, sortType_=None):
        if self.user is None:
            data = {'typeList': typeList_, 'pn': pn_, 'ps': ps_, 'contractNo': contractNo_, 'userKeyWord': userKeyWord_, 'creatorKeyWord': creatorKeyWord_, 'province': province_, 'city': city_, 'county': county_, 'signTimeStart': signTimeStart_, 'signTimeEnd': signTimeEnd_, 'sortType': sortType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'typeList': typeList_, 'pn': pn_, 'ps': ps_, 'contractNo': contractNo_, 'userKeyWord': userKeyWord_, 'creatorKeyWord': creatorKeyWord_, 'province': province_, 'city': city_, 'county': county_, 'signTimeStart': signTimeStart_, 'signTimeEnd': signTimeEnd_, 'sortType': sortType_}
        response = self.request.post(url=self.url+'/admin/contract/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_contract_list_by_user(self, pn_=None, ps_=None, userId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'userId': userId_}
        response = self.request.post(url=self.url+'/admin/contract/list-by-user', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_contract_stat(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/contract/stat', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_extract_apply_allot(self, applyId_=None, chargeId_=None):
        if self.user is None:
            data = {'applyId': applyId_, 'chargeId': chargeId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_, 'chargeId': chargeId_}
        response = self.request.post(url=self.url+'/admin/extract-apply/allot', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_extract_apply_close(self, applyId_=None, reasonType_=None):
        if self.user is None:
            data = {'applyId': applyId_, 'reasonType': reasonType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_, 'reasonType': reasonType_}
        response = self.request.post(url=self.url+'/admin/extract-apply/close', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_extract_apply_detail(self, applyId_=None):
        if self.user is None:
            data = {'applyId': applyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_}
        response = self.request.post(url=self.url+'/admin/extract-apply/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_extract_apply_edit(self, id_=None, status_=None, extractDate_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'id': id_, 'status': status_, 'extractDate': extractDate_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'status': status_, 'extractDate': extractDate_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/admin/extract-apply/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_extract_apply_list(self, pn_=None, ps_=None, applyNo_=None, status_=None, province_=None, city_=None, county_=None, creatorKeyWord_=None, chargeKeyWord_=None, extractDateStart_=None, extractDateEnd_=None, createDateStart_=None, createDateEnd_=None, sortType_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'applyNo': applyNo_, 'status': status_, 'province': province_, 'city': city_, 'county': county_, 'creatorKeyWord': creatorKeyWord_, 'chargeKeyWord': chargeKeyWord_, 'extractDateStart': extractDateStart_, 'extractDateEnd': extractDateEnd_, 'createDateStart': createDateStart_, 'createDateEnd': createDateEnd_, 'sortType': sortType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'applyNo': applyNo_, 'status': status_, 'province': province_, 'city': city_, 'county': county_, 'creatorKeyWord': creatorKeyWord_, 'chargeKeyWord': chargeKeyWord_, 'extractDateStart': extractDateStart_, 'extractDateEnd': extractDateEnd_, 'createDateStart': createDateStart_, 'createDateEnd': createDateEnd_, 'sortType': sortType_}
        response = self.request.post(url=self.url+'/admin/extract-apply/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_extract_apply_stat(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/extract-apply/stat', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_apply_confirm(self, applyId_=None, confirmDate_=None, realAmount_=None):
        if self.user is None:
            data = {'applyId': applyId_, 'confirmDate': confirmDate_, 'realAmount': realAmount_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_, 'confirmDate': confirmDate_, 'realAmount': realAmount_}
        response = self.request.post(url=self.url+'/admin/invoice-apply/confirm', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_apply_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/invoice-apply/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_apply_detail(self, applyId_=None):
        if self.user is None:
            data = {'applyId': applyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_}
        response = self.request.post(url=self.url+'/admin/invoice-apply/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_invoice_apply_page_list(self, pn_=None, ps_=None, drawer_=None, orderNo_=None, status_=None, applyOrderType_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'drawer': drawer_, 'orderNo': orderNo_, 'status': status_, 'applyOrderType': applyOrderType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'drawer': drawer_, 'orderNo': orderNo_, 'status': status_, 'applyOrderType': applyOrderType_}
        response = self.request.post(url=self.url+'/admin/invoice-apply/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_pay_apply_add(self, orderNo_=None, amount_=None, type_=None, payMethod_=None, payeeId_=None, remark_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, 'amount': amount_, 'type': type_, 'payMethod': payMethod_, 'payeeId': payeeId_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_, 'amount': amount_, 'type': type_, 'payMethod': payMethod_, 'payeeId': payeeId_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/pay-apply/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_pay_apply_add_check(self, orderNo_=None, type_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_, 'type': type_}
        response = self.request.post(url=self.url+'/admin/pay-apply/add-check', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_pay_apply_audit(self, applyId_=None, type_=None, reason_=None):
        if self.user is None:
            data = {'applyId': applyId_, 'type': type_, 'reason': reason_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_, 'type': type_, 'reason': reason_}
        response = self.request.post(url=self.url+'/admin/pay-apply/audit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_pay_apply_confirm(self, applyId_=None, receiptNo_=None):
        if self.user is None:
            data = {'applyId': applyId_, 'receiptNo': receiptNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_, 'receiptNo': receiptNo_}
        response = self.request.post(url=self.url+'/admin/pay-apply/confirm', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_pay_apply_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/pay-apply/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_pay_apply_detail(self, applyId_=None, receiptNo_=None):
        if self.user is None:
            data = {'applyId': applyId_, 'receiptNo': receiptNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_, 'receiptNo': receiptNo_}
        response = self.request.post(url=self.url+'/admin/pay-apply/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_pay_apply_export_pay_bill(self, ids_=None):
        if self.user is None:
            data = {'ids': ids_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'ids': ids_}
        response = self.request.post(url=self.url+'/admin/pay-apply/export-pay-bill', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_pay_apply_export_pay_record(self, pn_=None, ps_=None, payee_=None, applyer_=None, orderNo_=None, type_=None, payMethod_=None, applyTimeStart_=None, applyTimeEnd_=None, status_=None, applyOrderType_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'payee': payee_, 'applyer': applyer_, 'orderNo': orderNo_, 'type': type_, 'payMethod': payMethod_, 'applyTimeStart': applyTimeStart_, 'applyTimeEnd': applyTimeEnd_, 'status': status_, 'applyOrderType': applyOrderType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'payee': payee_, 'applyer': applyer_, 'orderNo': orderNo_, 'type': type_, 'payMethod': payMethod_, 'applyTimeStart': applyTimeStart_, 'applyTimeEnd': applyTimeEnd_, 'status': status_, 'applyOrderType': applyOrderType_}
        response = self.request.post(url=self.url+'/admin/pay-apply/export-pay-record', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_pay_apply_get_wx_quota(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/pay-apply/get-wx-quota', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_pay_apply_get_wx_template(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/pay-apply/get-wx-template', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_pay_apply_import_pay_bill(self, file_=None):
        if self.user is None:
            data = {'file': file_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'file': file_}
        response = self.request.post(url=self.url+'/admin/pay-apply/import-pay-bill', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_pay_apply_page_list(self, pn_=None, ps_=None, payee_=None, applyer_=None, orderNo_=None, type_=None, payMethod_=None, applyTimeStart_=None, applyTimeEnd_=None, status_=None, applyOrderType_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'payee': payee_, 'applyer': applyer_, 'orderNo': orderNo_, 'type': type_, 'payMethod': payMethod_, 'applyTimeStart': applyTimeStart_, 'applyTimeEnd': applyTimeEnd_, 'status': status_, 'applyOrderType': applyOrderType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'payee': payee_, 'applyer': applyer_, 'orderNo': orderNo_, 'type': type_, 'payMethod': payMethod_, 'applyTimeStart': applyTimeStart_, 'applyTimeEnd': applyTimeEnd_, 'status': status_, 'applyOrderType': applyOrderType_}
        response = self.request.post(url=self.url+'/admin/pay-apply/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_price_add(self, category_=None, variety_=None, province_=None, city_=None, county_=None, requirement_=None, strategyInfo_=None):
        if self.user is None:
            data = {'category': category_, 'variety': variety_, 'province': province_, 'city': city_, 'county': county_, 'requirement': requirement_, 'strategyInfo': strategyInfo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'category': category_, 'variety': variety_, 'province': province_, 'city': city_, 'county': county_, 'requirement': requirement_, 'strategyInfo': strategyInfo_}
        response = self.request.post(url=self.url+'/admin/price/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_price_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/price/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_price_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/price/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_price_edit(self, category_=None, variety_=None, province_=None, city_=None, county_=None, requirement_=None, strategyInfo_=None, id_=None):
        if self.user is None:
            data = {'category': category_, 'variety': variety_, 'province': province_, 'city': city_, 'county': county_, 'requirement': requirement_, 'strategyInfo': strategyInfo_, 'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'category': category_, 'variety': variety_, 'province': province_, 'city': city_, 'county': county_, 'requirement': requirement_, 'strategyInfo': strategyInfo_, 'id': id_}
        response = self.request.post(url=self.url+'/admin/price/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_price_on_off(self, id_=None, status_=None):
        if self.user is None:
            data = {'id': id_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/price/on-off', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_price_page_list(self, category_=None, variety_=None, province_=None, city_=None, county_=None, pn_=None, ps_=None, status_=None, ctOrderType_=None):
        if self.user is None:
            data = {'category': category_, 'variety': variety_, 'province': province_, 'city': city_, 'county': county_, 'pn': pn_, 'ps': ps_, 'status': status_, 'ctOrderType': ctOrderType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'category': category_, 'variety': variety_, 'province': province_, 'city': city_, 'county': county_, 'pn': pn_, 'ps': ps_, 'status': status_, 'ctOrderType': ctOrderType_}
        response = self.request.post(url=self.url+'/admin/price/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/product/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_detail(self, productId_=None):
        if self.user is None:
            data = {'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_}
        response = self.request.post(url=self.url+'/admin/product/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_product_list(self, province_=None, city_=None, county_=None, category_=None, variety_=None, type_=None, status_=None, pn_=None, ps_=None, purchaseDateStart_=None, purchaseDateEnd_=None, productNo_=None, sellerKey_=None, creatorKey_=None):
        if self.user is None:
            data = {'province': province_, 'city': city_, 'county': county_, 'category': category_, 'variety': variety_, 'type': type_, 'status': status_, 'pn': pn_, 'ps': ps_, 'purchaseDateStart': purchaseDateStart_, 'purchaseDateEnd': purchaseDateEnd_, 'productNo': productNo_, 'sellerKey': sellerKey_, 'creatorKey': creatorKey_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'province': province_, 'city': city_, 'county': county_, 'category': category_, 'variety': variety_, 'type': type_, 'status': status_, 'pn': pn_, 'ps': ps_, 'purchaseDateStart': purchaseDateStart_, 'purchaseDateEnd': purchaseDateEnd_, 'productNo': productNo_, 'sellerKey': sellerKey_, 'creatorKey': creatorKey_}
        response = self.request.post(url=self.url+'/admin/product/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_order_base_info(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/admin/purchase-order/base-info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_order_check_price(self, productId_=None, price_=None, grade_=None, examineStatus_=None, examineRemark_=None):
        if self.user is None:
            data = {'productId': productId_, 'price': price_, 'grade': grade_, 'examineStatus': examineStatus_, 'examineRemark': examineRemark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_, 'price': price_, 'grade': grade_, 'examineStatus': examineStatus_, 'examineRemark': examineRemark_}
        response = self.request.post(url=self.url+'/admin/purchase-order/check-price', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_order_confirm_grade(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/admin/purchase-order/confirm-grade', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_order_confirm_info(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/admin/purchase-order/confirm-info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_order_confirm_price(self, orderNo_=None, contractNo_=None, isDeduction_=None, isQuality_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, 'contractNo': contractNo_, 'isDeduction': isDeduction_, 'isQuality': isQuality_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_, 'contractNo': contractNo_, 'isDeduction': isDeduction_, 'isQuality': isQuality_}
        response = self.request.post(url=self.url+'/admin/purchase-order/confirm-price', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_order_edit_base_info(self, orderNo_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/admin/purchase-order/edit-base-info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_order_opt_log(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/admin/purchase-order/opt-log', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_order_page_list(self, status_=None, pn_=None, ps_=None, startDate_=None, endDate_=None, location_=None, orderNo_=None, userInfo_=None, province_=None, city_=None, county_=None, sellerId_=None, ctOrderType_=None, utOrderType_=None):
        if self.user is None:
            data = {'status': status_, 'pn': pn_, 'ps': ps_, 'startDate': startDate_, 'endDate': endDate_, 'location': location_, 'orderNo': orderNo_, 'userInfo': userInfo_, 'province': province_, 'city': city_, 'county': county_, 'sellerId': sellerId_, 'ctOrderType': ctOrderType_, 'utOrderType': utOrderType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'status': status_, 'pn': pn_, 'ps': ps_, 'startDate': startDate_, 'endDate': endDate_, 'location': location_, 'orderNo': orderNo_, 'userInfo': userInfo_, 'province': province_, 'city': city_, 'county': county_, 'sellerId': sellerId_, 'ctOrderType': ctOrderType_, 'utOrderType': utOrderType_}
        response = self.request.post(url=self.url+'/admin/purchase-order/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_order_pay_apply(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/admin/purchase-order/pay-apply', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_order_product_info(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/admin/purchase-order/product-info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_order_quality_commit(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/admin/purchase-order/quality-commit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_order_standards(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/admin/purchase-order/standards', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_order_status_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/purchase-order/status-count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_quality_add(self, images_=None, orderNo_=None, type_=None, remark_=None, deductPrice_=None):
        if self.user is None:
            data = {'images': images_, 'orderNo': orderNo_, 'type': type_, 'remark': remark_, 'deductPrice': deductPrice_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'images': images_, 'orderNo': orderNo_, 'type': type_, 'remark': remark_, 'deductPrice': deductPrice_}
        response = self.request.post(url=self.url+'/admin/quality/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_quality_del(self, qualityId_=None):
        if self.user is None:
            data = {'qualityId': qualityId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'qualityId': qualityId_}
        response = self.request.post(url=self.url+'/admin/quality/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_quality_edit(self, images_=None, qualityId_=None, type_=None, remark_=None, deductPrice_=None):
        if self.user is None:
            data = {'images': images_, 'qualityId': qualityId_, 'type': type_, 'remark': remark_, 'deductPrice': deductPrice_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'images': images_, 'qualityId': qualityId_, 'type': type_, 'remark': remark_, 'deductPrice': deductPrice_}
        response = self.request.post(url=self.url+'/admin/quality/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_quality_info(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/admin/quality/info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_add(self, pics_=None, name_=None, mainBusiness_=None, province_=None, city_=None, county_=None, intro_=None):
        if self.user is None:
            data = {'pics': pics_, 'name': name_, 'mainBusiness': mainBusiness_, 'province': province_, 'city': city_, 'county': county_, 'intro': intro_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'name': name_, 'mainBusiness': mainBusiness_, 'province': province_, 'city': city_, 'county': county_, 'intro': intro_}
        response = self.request.post(url=self.url+'/admin/supplier/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/supplier/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_del(self, supplierId_=None):
        if self.user is None:
            data = {'supplierId': supplierId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'supplierId': supplierId_}
        response = self.request.post(url=self.url+'/admin/supplier/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_detail(self, supplierId_=None):
        if self.user is None:
            data = {'supplierId': supplierId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'supplierId': supplierId_}
        response = self.request.post(url=self.url+'/admin/supplier/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_edit(self, pics_=None, name_=None, mainBusiness_=None, province_=None, city_=None, county_=None, intro_=None, id_=None):
        if self.user is None:
            data = {'pics': pics_, 'name': name_, 'mainBusiness': mainBusiness_, 'province': province_, 'city': city_, 'county': county_, 'intro': intro_, 'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'name': name_, 'mainBusiness': mainBusiness_, 'province': province_, 'city': city_, 'county': county_, 'intro': intro_, 'id': id_}
        response = self.request.post(url=self.url+'/admin/supplier/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_list(self, pn_=None, ps_=None, name_=None, addProduct_=None, productOnline_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, 'addProduct': addProduct_, 'productOnline': productOnline_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_, 'addProduct': addProduct_, 'productOnline': productOnline_}
        response = self.request.post(url=self.url+'/admin/supplier/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_list(self, supplierId_=None):
        if self.user is None:
            data = {'supplierId': supplierId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'supplierId': supplierId_}
        response = self.request.post(url=self.url+'/admin/supplier/product-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_add(self, label_=None, productListImgUrl_=None, productImgUrl_=None, productParamImgUrl_=None, productDetailImgUrl_=None, supplierId_=None, name_=None, category_=None, title_=None, brand_=None, price_=None, sortNo_=None):
        if self.user is None:
            data = {'label': label_, 'productListImgUrl': productListImgUrl_, 'productImgUrl': productImgUrl_, 'productParamImgUrl': productParamImgUrl_, 'productDetailImgUrl': productDetailImgUrl_, 'supplierId': supplierId_, 'name': name_, 'category': category_, 'title': title_, 'brand': brand_, 'price': price_, 'sortNo': sortNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'label': label_, 'productListImgUrl': productListImgUrl_, 'productImgUrl': productImgUrl_, 'productParamImgUrl': productParamImgUrl_, 'productDetailImgUrl': productDetailImgUrl_, 'supplierId': supplierId_, 'name': name_, 'category': category_, 'title': title_, 'brand': brand_, 'price': price_, 'sortNo': sortNo_}
        response = self.request.post(url=self.url+'/admin/supplier/product/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_add_on_shelf(self, label_=None, productListImgUrl_=None, productImgUrl_=None, productParamImgUrl_=None, productDetailImgUrl_=None, supplierId_=None, name_=None, category_=None, title_=None, brand_=None, price_=None, sortNo_=None):
        if self.user is None:
            data = {'label': label_, 'productListImgUrl': productListImgUrl_, 'productImgUrl': productImgUrl_, 'productParamImgUrl': productParamImgUrl_, 'productDetailImgUrl': productDetailImgUrl_, 'supplierId': supplierId_, 'name': name_, 'category': category_, 'title': title_, 'brand': brand_, 'price': price_, 'sortNo': sortNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'label': label_, 'productListImgUrl': productListImgUrl_, 'productImgUrl': productImgUrl_, 'productParamImgUrl': productParamImgUrl_, 'productDetailImgUrl': productDetailImgUrl_, 'supplierId': supplierId_, 'name': name_, 'category': category_, 'title': title_, 'brand': brand_, 'price': price_, 'sortNo': sortNo_}
        response = self.request.post(url=self.url+'/admin/supplier/product/add-on-shelf', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/supplier/product/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_detail(self, productId_=None):
        if self.user is None:
            data = {'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_}
        response = self.request.post(url=self.url+'/admin/supplier/product/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_list(self, pn_=None, ps_=None, supplierName_=None, name_=None, status_=None, title_=None, onShelfTimeStart_=None, onShelfTimeEnd_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'supplierName': supplierName_, 'name': name_, 'status': status_, 'title': title_, 'onShelfTimeStart': onShelfTimeStart_, 'onShelfTimeEnd': onShelfTimeEnd_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'supplierName': supplierName_, 'name': name_, 'status': status_, 'title': title_, 'onShelfTimeStart': onShelfTimeStart_, 'onShelfTimeEnd': onShelfTimeEnd_}
        response = self.request.post(url=self.url+'/admin/supplier/product/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_off_shelf(self, productId_=None):
        if self.user is None:
            data = {'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_}
        response = self.request.post(url=self.url+'/admin/supplier/product/off-shelf', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_on_shelf(self, productId_=None):
        if self.user is None:
            data = {'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_}
        response = self.request.post(url=self.url+'/admin/supplier/product/on-shelf', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_purchase_add(self, purchaseInfoJson_=None):
        if self.user is None:
            data = {'purchaseInfoJson': purchaseInfoJson_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'purchaseInfoJson': purchaseInfoJson_}
        response = self.request.post(url=self.url+'/admin/supplier/product/purchase/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_purchase_list(self, productId_=None):
        if self.user is None:
            data = {'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_}
        response = self.request.post(url=self.url+'/admin/supplier/product/purchase/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_stock_add(self, stockAddJson_=None):
        if self.user is None:
            data = {'stockAddJson': stockAddJson_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'stockAddJson': stockAddJson_}
        response = self.request.post(url=self.url+'/admin/supplier/product/stock/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_stock_assignee_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/supplier/product/stock/assignee-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_stock_assignor_list(self, productId_=None):
        if self.user is None:
            data = {'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_}
        response = self.request.post(url=self.url+'/admin/supplier/product/stock/assignor-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_stock_list(self, productId_=None):
        if self.user is None:
            data = {'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_}
        response = self.request.post(url=self.url+'/admin/supplier/product/stock/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_stock_product_list(self, pn_=None, ps_=None, supplierName_=None, name_=None, status_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'supplierName': supplierName_, 'name': name_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'supplierName': supplierName_, 'name': name_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/supplier/product/stock/product-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_stock_record_list(self, productId_=None):
        if self.user is None:
            data = {'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_}
        response = self.request.post(url=self.url+'/admin/supplier/product/stock/record/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_supplier_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/supplier/product/supplier-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_supplier_product_update(self, label_=None, productListImgUrl_=None, productImgUrl_=None, productParamImgUrl_=None, productDetailImgUrl_=None, supplierId_=None, name_=None, category_=None, title_=None, brand_=None, price_=None, sortNo_=None, id_=None):
        if self.user is None:
            data = {'label': label_, 'productListImgUrl': productListImgUrl_, 'productImgUrl': productImgUrl_, 'productParamImgUrl': productParamImgUrl_, 'productDetailImgUrl': productDetailImgUrl_, 'supplierId': supplierId_, 'name': name_, 'category': category_, 'title': title_, 'brand': brand_, 'price': price_, 'sortNo': sortNo_, 'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'label': label_, 'productListImgUrl': productListImgUrl_, 'productImgUrl': productImgUrl_, 'productParamImgUrl': productParamImgUrl_, 'productDetailImgUrl': productDetailImgUrl_, 'supplierId': supplierId_, 'name': name_, 'category': category_, 'title': title_, 'brand': brand_, 'price': price_, 'sortNo': sortNo_, 'id': id_}
        response = self.request.post(url=self.url+'/admin/supplier/product/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _config_common_get_all_enum_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/config/common/get-all-enum-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _listener_wx_change_apply_status(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.get(url=self.url+'/listener/wx/change-apply-status', params=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_friend_extract_apply_cancel(self, applyId_=None, reasonType_=None):
        if self.user is None:
            data = {'applyId': applyId_, 'reasonType': reasonType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_, 'reasonType': reasonType_}
        response = self.request.post(url=self.url+'/mobile/friend/extract-apply/cancel', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_friend_invoice_apply_info_detail(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/friend/invoice-apply/info-detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_friend_invoice_apply_replenish(self, realName_=None, idCardNo_=None, idCardFrontImage_=None, address_=None):
        if self.user is None:
            data = {'realName': realName_, 'idCardNo': idCardNo_, 'idCardFrontImage': idCardFrontImage_, 'address': address_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'realName': realName_, 'idCardNo': idCardNo_, 'idCardFrontImage': idCardFrontImage_, 'address': address_}
        response = self.request.post(url=self.url+'/mobile/friend/invoice-apply/replenish', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_friend_overview_purchase(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/friend/overview/purchase', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_friend_pay_apply_receipt(self, pn_=None, ps_=None, year_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'year': year_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'year': year_}
        response = self.request.post(url=self.url+'/mobile/friend/pay-apply/receipt', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_friend_product_detail(self, productId_=None):
        if self.user is None:
            data = {'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_}
        response = self.request.post(url=self.url+'/mobile/friend/product/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_friend_product_list(self, province_=None, city_=None, county_=None, category_=None, variety_=None, type_=None, status_=None, pn_=None, ps_=None, purchaseDateStart_=None, purchaseDateEnd_=None, productNo_=None, sellerKey_=None, creatorKey_=None):
        if self.user is None:
            data = {'province': province_, 'city': city_, 'county': county_, 'category': category_, 'variety': variety_, 'type': type_, 'status': status_, 'pn': pn_, 'ps': ps_, 'purchaseDateStart': purchaseDateStart_, 'purchaseDateEnd': purchaseDateEnd_, 'productNo': productNo_, 'sellerKey': sellerKey_, 'creatorKey': creatorKey_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'province': province_, 'city': city_, 'county': county_, 'category': category_, 'variety': variety_, 'type': type_, 'status': status_, 'pn': pn_, 'ps': ps_, 'purchaseDateStart': purchaseDateStart_, 'purchaseDateEnd': purchaseDateEnd_, 'productNo': productNo_, 'sellerKey': sellerKey_, 'creatorKey': creatorKey_}
        response = self.request.post(url=self.url+'/mobile/friend/product/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_friend_purchase_order_base_info(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/mobile/friend/purchase-order/base-info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_friend_purchase_order_deduction_confirm(self, orderId_=None, realPrice_=None):
        if self.user is None:
            data = {'orderId': orderId_, 'realPrice': realPrice_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderId': orderId_, 'realPrice': realPrice_}
        response = self.request.post(url=self.url+'/mobile/friend/purchase-order/deduction-confirm', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_friend_purchase_order_page_list(self, status_=None, pn_=None, ps_=None, startDate_=None, endDate_=None, location_=None, orderNo_=None, userInfo_=None, province_=None, city_=None, county_=None, sellerId_=None, ctOrderType_=None, utOrderType_=None):
        if self.user is None:
            data = {'status': status_, 'pn': pn_, 'ps': ps_, 'startDate': startDate_, 'endDate': endDate_, 'location': location_, 'orderNo': orderNo_, 'userInfo': userInfo_, 'province': province_, 'city': city_, 'county': county_, 'sellerId': sellerId_, 'ctOrderType': ctOrderType_, 'utOrderType': utOrderType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'status': status_, 'pn': pn_, 'ps': ps_, 'startDate': startDate_, 'endDate': endDate_, 'location': location_, 'orderNo': orderNo_, 'userInfo': userInfo_, 'province': province_, 'city': city_, 'county': county_, 'sellerId': sellerId_, 'ctOrderType': ctOrderType_, 'utOrderType': utOrderType_}
        response = self.request.post(url=self.url+'/mobile/friend/purchase-order/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_friend_purchase_order_product_list(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/mobile/friend/purchase-order/product-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_hall_purchase_category_list(self, typeCodes_=None):
        if self.user is None:
            data = {'typeCodes': typeCodes_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'typeCodes': typeCodes_}
        response = self.request.post(url=self.url+'/mobile/hall/purchase/category/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_hall_purchase_consultation_user_add(self, buyInfoId_=None, type_=None):
        if self.user is None:
            data = {'buyInfoId': buyInfoId_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'buyInfoId': buyInfoId_, 'type': type_}
        response = self.request.post(url=self.url+'/mobile/hall/purchase/consultation-user/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_hall_purchase_consultation_user_list(self, buyInfoId_=None):
        if self.user is None:
            data = {'buyInfoId': buyInfoId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'buyInfoId': buyInfoId_}
        response = self.request.post(url=self.url+'/mobile/hall/purchase/consultation-user/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_hall_purchase_info_add(self, category_=None, subcategory_=None, buyQuantity_=None, buyQuantityUnit_=None, concentration_=None, purity_=None, season_=None, colony_=None, queenType_=None, receiptRegion_=None, productionRegion_=None, qualityRequirement_=None, otherRequirement_=None):
        if self.user is None:
            data = {'category': category_, 'subcategory': subcategory_, 'buyQuantity': buyQuantity_, 'buyQuantityUnit': buyQuantityUnit_, 'concentration': concentration_, 'purity': purity_, 'season': season_, 'colony': colony_, 'queenType': queenType_, 'receiptRegion': receiptRegion_, 'productionRegion': productionRegion_, 'qualityRequirement': qualityRequirement_, 'otherRequirement': otherRequirement_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'category': category_, 'subcategory': subcategory_, 'buyQuantity': buyQuantity_, 'buyQuantityUnit': buyQuantityUnit_, 'concentration': concentration_, 'purity': purity_, 'season': season_, 'colony': colony_, 'queenType': queenType_, 'receiptRegion': receiptRegion_, 'productionRegion': productionRegion_, 'qualityRequirement': qualityRequirement_, 'otherRequirement': otherRequirement_}
        response = self.request.post(url=self.url+'/mobile/hall/purchase/info/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_hall_purchase_info_buyer_list(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/mobile/hall/purchase/info/buyer-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_hall_purchase_info_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/hall/purchase/info/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_hall_purchase_info_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/hall/purchase/info/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_hall_purchase_info_detail_user(self, userId_=None):
        if self.user is None:
            data = {'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_}
        response = self.request.post(url=self.url+'/mobile/hall/purchase/info/detail/user', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_hall_purchase_info_home_list(self, pn_=None, ps_=None, category_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'category': category_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'category': category_}
        response = self.request.post(url=self.url+'/mobile/hall/purchase/info/home-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_hall_purchase_info_off_shelves(self, id_=None, reason_=None):
        if self.user is None:
            data = {'id': id_, 'reason': reason_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'reason': reason_}
        response = self.request.post(url=self.url+'/mobile/hall/purchase/info/off-shelves', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_hall_purchase_info_on_shelves(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/hall/purchase/info/on-shelves', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_hall_purchase_info_update(self, category_=None, subcategory_=None, buyQuantity_=None, buyQuantityUnit_=None, concentration_=None, purity_=None, season_=None, colony_=None, queenType_=None, receiptRegion_=None, productionRegion_=None, qualityRequirement_=None, otherRequirement_=None, id_=None):
        if self.user is None:
            data = {'category': category_, 'subcategory': subcategory_, 'buyQuantity': buyQuantity_, 'buyQuantityUnit': buyQuantityUnit_, 'concentration': concentration_, 'purity': purity_, 'season': season_, 'colony': colony_, 'queenType': queenType_, 'receiptRegion': receiptRegion_, 'productionRegion': productionRegion_, 'qualityRequirement': qualityRequirement_, 'otherRequirement': otherRequirement_, 'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'category': category_, 'subcategory': subcategory_, 'buyQuantity': buyQuantity_, 'buyQuantityUnit': buyQuantityUnit_, 'concentration': concentration_, 'purity': purity_, 'season': season_, 'colony': colony_, 'queenType': queenType_, 'receiptRegion': receiptRegion_, 'productionRegion': productionRegion_, 'qualityRequirement': qualityRequirement_, 'otherRequirement': otherRequirement_, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/hall/purchase/info/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_hall_purchase_scroll_info_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/hall/purchase/scroll-info/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manage_overview_data_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/manage/overview/data-count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_extract_apply_close(self, applyId_=None, reasonType_=None):
        if self.user is None:
            data = {'applyId': applyId_, 'reasonType': reasonType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_, 'reasonType': reasonType_}
        response = self.request.post(url=self.url+'/mobile/manager/extract-apply/close', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_extract_apply_confirm(self, pics_=None, applyId_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, extractDate_=None, remark_=None):
        if self.user is None:
            data = {'pics': pics_, 'applyId': applyId_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'extractDate': extractDate_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'applyId': applyId_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'extractDate': extractDate_, 'remark': remark_}
        response = self.request.post(url=self.url+'/mobile/manager/extract-apply/confirm', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_extract_apply_detail(self, applyId_=None):
        if self.user is None:
            data = {'applyId': applyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_}
        response = self.request.post(url=self.url+'/mobile/manager/extract-apply/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_extract_apply_list(self, pn_=None, ps_=None, searchType_=None, province_=None, city_=None, county_=None, status_=None, keyWord_=None, distanceType_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'searchType': searchType_, 'province': province_, 'city': city_, 'county': county_, 'status': status_, 'keyWord': keyWord_, 'distanceType': distanceType_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'searchType': searchType_, 'province': province_, 'city': city_, 'county': county_, 'status': status_, 'keyWord': keyWord_, 'distanceType': distanceType_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/mobile/manager/extract-apply/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_product_add(self, pics_=None, sellerId_=None, category_=None, variety_=None, type_=None, weight_=None, purity_=None, consistence_=None, capRate_=None, humidity_=None, province_=None, city_=None, county_=None, manufactureDate_=None, purchaseDate_=None, strategyId_=None, grade_=None, price_=None, otherAmount_=None, remark_=None):
        if self.user is None:
            data = {'pics': pics_, 'sellerId': sellerId_, 'category': category_, 'variety': variety_, 'type': type_, 'weight': weight_, 'purity': purity_, 'consistence': consistence_, 'capRate': capRate_, 'humidity': humidity_, 'province': province_, 'city': city_, 'county': county_, 'manufactureDate': manufactureDate_, 'purchaseDate': purchaseDate_, 'strategyId': strategyId_, 'grade': grade_, 'price': price_, 'otherAmount': otherAmount_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'sellerId': sellerId_, 'category': category_, 'variety': variety_, 'type': type_, 'weight': weight_, 'purity': purity_, 'consistence': consistence_, 'capRate': capRate_, 'humidity': humidity_, 'province': province_, 'city': city_, 'county': county_, 'manufactureDate': manufactureDate_, 'purchaseDate': purchaseDate_, 'strategyId': strategyId_, 'grade': grade_, 'price': price_, 'otherAmount': otherAmount_, 'remark': remark_}
        response = self.request.post(url=self.url+'/mobile/manager/product/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_product_del(self, productId_=None):
        if self.user is None:
            data = {'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_}
        response = self.request.post(url=self.url+'/mobile/manager/product/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_product_detail(self, productId_=None):
        if self.user is None:
            data = {'productId': productId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_}
        response = self.request.post(url=self.url+'/mobile/manager/product/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_product_edit(self, pics_=None, id_=None, sellerId_=None, weight_=None, purity_=None, consistence_=None, capRate_=None, humidity_=None, province_=None, city_=None, county_=None, manufactureDate_=None, purchaseDate_=None, strategyId_=None, grade_=None, price_=None, otherAmount_=None, remark_=None):
        if self.user is None:
            data = {'pics': pics_, 'id': id_, 'sellerId': sellerId_, 'weight': weight_, 'purity': purity_, 'consistence': consistence_, 'capRate': capRate_, 'humidity': humidity_, 'province': province_, 'city': city_, 'county': county_, 'manufactureDate': manufactureDate_, 'purchaseDate': purchaseDate_, 'strategyId': strategyId_, 'grade': grade_, 'price': price_, 'otherAmount': otherAmount_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'id': id_, 'sellerId': sellerId_, 'weight': weight_, 'purity': purity_, 'consistence': consistence_, 'capRate': capRate_, 'humidity': humidity_, 'province': province_, 'city': city_, 'county': county_, 'manufactureDate': manufactureDate_, 'purchaseDate': purchaseDate_, 'strategyId': strategyId_, 'grade': grade_, 'price': price_, 'otherAmount': otherAmount_, 'remark': remark_}
        response = self.request.post(url=self.url+'/mobile/manager/product/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_product_friend(self, mobile_=None):
        if self.user is None:
            data = {'mobile': mobile_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile_}
        response = self.request.post(url=self.url+'/mobile/manager/product/friend', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_product_info(self, productNo_=None):
        if self.user is None:
            data = {'productNo': productNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productNo': productNo_}
        response = self.request.post(url=self.url+'/mobile/manager/product/info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_product_list(self, province_=None, city_=None, county_=None, category_=None, variety_=None, type_=None, status_=None, pn_=None, ps_=None, purchaseDateStart_=None, purchaseDateEnd_=None, productNo_=None, sellerKey_=None, creatorKey_=None):
        if self.user is None:
            data = {'province': province_, 'city': city_, 'county': county_, 'category': category_, 'variety': variety_, 'type': type_, 'status': status_, 'pn': pn_, 'ps': ps_, 'purchaseDateStart': purchaseDateStart_, 'purchaseDateEnd': purchaseDateEnd_, 'productNo': productNo_, 'sellerKey': sellerKey_, 'creatorKey': creatorKey_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'province': province_, 'city': city_, 'county': county_, 'category': category_, 'variety': variety_, 'type': type_, 'status': status_, 'pn': pn_, 'ps': ps_, 'purchaseDateStart': purchaseDateStart_, 'purchaseDateEnd': purchaseDateEnd_, 'productNo': productNo_, 'sellerKey': sellerKey_, 'creatorKey': creatorKey_}
        response = self.request.post(url=self.url+'/mobile/manager/product/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_product_price_city(self, category_=None, variety_=None, province_=None, city_=None, county_=None):
        if self.user is None:
            data = {'category': category_, 'variety': variety_, 'province': province_, 'city': city_, 'county': county_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'category': category_, 'variety': variety_, 'province': province_, 'city': city_, 'county': county_}
        response = self.request.post(url=self.url+'/mobile/manager/product/price-city', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_product_product_price(self, category_=None, variety_=None, province_=None, city_=None, county_=None):
        if self.user is None:
            data = {'category': category_, 'variety': variety_, 'province': province_, 'city': city_, 'county': county_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'category': category_, 'variety': variety_, 'province': province_, 'city': city_, 'county': county_}
        response = self.request.post(url=self.url+'/mobile/manager/product/product-price', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_product_varieties(self, category_=None):
        if self.user is None:
            data = {'category': category_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'category': category_}
        response = self.request.post(url=self.url+'/mobile/manager/product/varieties', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_purchase_order_add(self, productIds_=None, userId_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, remark_=None, swarmId_=None, acquisitionDate_=None, isTail_=None, idCard_=None):
        if self.user is None:
            data = {'productIds': productIds_, 'userId': userId_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'remark': remark_, 'swarmId': swarmId_, 'acquisitionDate': acquisitionDate_, 'isTail': isTail_, 'idCard': idCard_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productIds': productIds_, 'userId': userId_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'remark': remark_, 'swarmId': swarmId_, 'acquisitionDate': acquisitionDate_, 'isTail': isTail_, 'idCard': idCard_}
        response = self.request.post(url=self.url+'/mobile/manager/purchase-order/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_purchase_order_base_info(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/mobile/manager/purchase-order/base-info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_purchase_order_del(self, orderId_=None):
        if self.user is None:
            data = {'orderId': orderId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderId': orderId_}
        response = self.request.post(url=self.url+'/mobile/manager/purchase-order/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_purchase_order_edit(self, productIds_=None, orderId_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, remark_=None, swarmId_=None, acquisitionDate_=None, isTail_=None, idCard_=None):
        if self.user is None:
            data = {'productIds': productIds_, 'orderId': orderId_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'remark': remark_, 'swarmId': swarmId_, 'acquisitionDate': acquisitionDate_, 'isTail': isTail_, 'idCard': idCard_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productIds': productIds_, 'orderId': orderId_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'remark': remark_, 'swarmId': swarmId_, 'acquisitionDate': acquisitionDate_, 'isTail': isTail_, 'idCard': idCard_}
        response = self.request.post(url=self.url+'/mobile/manager/purchase-order/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_purchase_order_friend_list(self, searchKey_=None, lat_=None, lng_=None):
        if self.user is None:
            data = {'searchKey': searchKey_, 'lat': lat_, 'lng': lng_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'searchKey': searchKey_, 'lat': lat_, 'lng': lng_}
        response = self.request.post(url=self.url+'/mobile/manager/purchase-order/friend-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_purchase_order_friend_swarm(self, userId_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'userId': userId_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/mobile/manager/purchase-order/friend-swarm', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_purchase_order_page_list(self, status_=None, pn_=None, ps_=None, startDate_=None, endDate_=None, location_=None, orderNo_=None, userInfo_=None, province_=None, city_=None, county_=None, sellerId_=None, ctOrderType_=None, utOrderType_=None):
        if self.user is None:
            data = {'status': status_, 'pn': pn_, 'ps': ps_, 'startDate': startDate_, 'endDate': endDate_, 'location': location_, 'orderNo': orderNo_, 'userInfo': userInfo_, 'province': province_, 'city': city_, 'county': county_, 'sellerId': sellerId_, 'ctOrderType': ctOrderType_, 'utOrderType': utOrderType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'status': status_, 'pn': pn_, 'ps': ps_, 'startDate': startDate_, 'endDate': endDate_, 'location': location_, 'orderNo': orderNo_, 'userInfo': userInfo_, 'province': province_, 'city': city_, 'county': county_, 'sellerId': sellerId_, 'ctOrderType': ctOrderType_, 'utOrderType': utOrderType_}
        response = self.request.post(url=self.url+'/mobile/manager/purchase-order/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_purchase_order_paid_list(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/mobile/manager/purchase-order/paid-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_purchase_order_product_list(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/mobile/manager/purchase-order/product-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_purchase_order_product_sale_list(self, sellerId_=None):
        if self.user is None:
            data = {'sellerId': sellerId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'sellerId': sellerId_}
        response = self.request.post(url=self.url+'/mobile/manager/purchase-order/product-sale-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_manager_purchase_order_upload_voucher(self, serialNo_=None, url_=None):
        if self.user is None:
            data = {'serialNo': serialNo_, 'url': url_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'serialNo': serialNo_, 'url': url_}
        response = self.request.post(url=self.url+'/mobile/manager/purchase-order/upload-voucher', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_contract_abort(self, id_=None, abortType_=None):
        if self.user is None:
            data = {'id': id_, 'abortType': abortType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'abortType': abortType_}
        response = self.request.post(url=self.url+'/web/contract/abort', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_contract_add_bee(self, pics_=None, userId_=None, swarmId_=None, signTime_=None, amount_=None, handsel_=None, hiveNum_=None, standardNum_=None, smallNum_=None, tent_=None, honeyMachine_=None, scraper_=None, motorcycle_=None, honeypot_=None, alternator_=None, solarPanel_=None, remark_=None, idCardNo_=None, identityFront_=None, identityBack_=None, realName_=None, bankName_=None, branchName_=None, cardNo_=None, bankFront_=None, bankBack_=None):
        if self.user is None:
            data = {'pics': pics_, 'userId': userId_, 'swarmId': swarmId_, 'signTime': signTime_, 'amount': amount_, 'handsel': handsel_, 'hiveNum': hiveNum_, 'standardNum': standardNum_, 'smallNum': smallNum_, 'tent': tent_, 'honeyMachine': honeyMachine_, 'scraper': scraper_, 'motorcycle': motorcycle_, 'honeypot': honeypot_, 'alternator': alternator_, 'solarPanel': solarPanel_, 'remark': remark_, 'idCardNo': idCardNo_, 'identityFront': identityFront_, 'identityBack': identityBack_, 'realName': realName_, 'bankName': bankName_, 'branchName': branchName_, 'cardNo': cardNo_, 'bankFront': bankFront_, 'bankBack': bankBack_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'userId': userId_, 'swarmId': swarmId_, 'signTime': signTime_, 'amount': amount_, 'handsel': handsel_, 'hiveNum': hiveNum_, 'standardNum': standardNum_, 'smallNum': smallNum_, 'tent': tent_, 'honeyMachine': honeyMachine_, 'scraper': scraper_, 'motorcycle': motorcycle_, 'honeypot': honeypot_, 'alternator': alternator_, 'solarPanel': solarPanel_, 'remark': remark_, 'idCardNo': idCardNo_, 'identityFront': identityFront_, 'identityBack': identityBack_, 'realName': realName_, 'bankName': bankName_, 'branchName': branchName_, 'cardNo': cardNo_, 'bankFront': bankFront_, 'bankBack': bankBack_}
        response = self.request.post(url=self.url+'/web/contract/add-bee', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_contract_add_honey(self, pics_=None, userId_=None, swarmId_=None, signTime_=None, amount_=None, handsel_=None, variety_=None, type_=None, purchaseNum_=None, remark_=None, idCardNo_=None, identityFront_=None, identityBack_=None, realName_=None, bankName_=None, branchName_=None, cardNo_=None, bankFront_=None, bankBack_=None):
        if self.user is None:
            data = {'pics': pics_, 'userId': userId_, 'swarmId': swarmId_, 'signTime': signTime_, 'amount': amount_, 'handsel': handsel_, 'variety': variety_, 'type': type_, 'purchaseNum': purchaseNum_, 'remark': remark_, 'idCardNo': idCardNo_, 'identityFront': identityFront_, 'identityBack': identityBack_, 'realName': realName_, 'bankName': bankName_, 'branchName': branchName_, 'cardNo': cardNo_, 'bankFront': bankFront_, 'bankBack': bankBack_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'userId': userId_, 'swarmId': swarmId_, 'signTime': signTime_, 'amount': amount_, 'handsel': handsel_, 'variety': variety_, 'type': type_, 'purchaseNum': purchaseNum_, 'remark': remark_, 'idCardNo': idCardNo_, 'identityFront': identityFront_, 'identityBack': identityBack_, 'realName': realName_, 'bankName': bankName_, 'branchName': branchName_, 'cardNo': cardNo_, 'bankFront': bankFront_, 'bankBack': bankBack_}
        response = self.request.post(url=self.url+'/web/contract/add-honey', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_contract_add_pollen(self, pics_=None, userId_=None, swarmId_=None, signTime_=None, amount_=None, handsel_=None, variety_=None, type_=None, purchaseNum_=None, remark_=None, idCardNo_=None, identityFront_=None, identityBack_=None, realName_=None, bankName_=None, branchName_=None, cardNo_=None, bankFront_=None, bankBack_=None):
        if self.user is None:
            data = {'pics': pics_, 'userId': userId_, 'swarmId': swarmId_, 'signTime': signTime_, 'amount': amount_, 'handsel': handsel_, 'variety': variety_, 'type': type_, 'purchaseNum': purchaseNum_, 'remark': remark_, 'idCardNo': idCardNo_, 'identityFront': identityFront_, 'identityBack': identityBack_, 'realName': realName_, 'bankName': bankName_, 'branchName': branchName_, 'cardNo': cardNo_, 'bankFront': bankFront_, 'bankBack': bankBack_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'userId': userId_, 'swarmId': swarmId_, 'signTime': signTime_, 'amount': amount_, 'handsel': handsel_, 'variety': variety_, 'type': type_, 'purchaseNum': purchaseNum_, 'remark': remark_, 'idCardNo': idCardNo_, 'identityFront': identityFront_, 'identityBack': identityBack_, 'realName': realName_, 'bankName': bankName_, 'branchName': branchName_, 'cardNo': cardNo_, 'bankFront': bankFront_, 'bankBack': bankBack_}
        response = self.request.post(url=self.url+'/web/contract/add-pollen', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_contract_check_phone(self, contractType_=None, phone_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'contractType': contractType_, 'phone': phone_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'contractType': contractType_, 'phone': phone_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/web/contract/check-phone', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_contract_detail(self, contractId_=None):
        if self.user is None:
            data = {'contractId': contractId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'contractId': contractId_}
        response = self.request.post(url=self.url+'/web/contract/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_contract_edit_bee(self, pics_=None, status_=None, id_=None, userId_=None, swarmId_=None, signTime_=None, amount_=None, handsel_=None, contractBeeId_=None, hiveNum_=None, standardNum_=None, smallNum_=None, tent_=None, honeyMachine_=None, scraper_=None, motorcycle_=None, honeypot_=None, alternator_=None, solarPanel_=None, remark_=None, idCardNo_=None, identityFront_=None, identityBack_=None, realName_=None, bankName_=None, branchName_=None, cardNo_=None, bankFront_=None, bankBack_=None):
        if self.user is None:
            data = {'pics': pics_, 'status': status_, 'id': id_, 'userId': userId_, 'swarmId': swarmId_, 'signTime': signTime_, 'amount': amount_, 'handsel': handsel_, 'contractBeeId': contractBeeId_, 'hiveNum': hiveNum_, 'standardNum': standardNum_, 'smallNum': smallNum_, 'tent': tent_, 'honeyMachine': honeyMachine_, 'scraper': scraper_, 'motorcycle': motorcycle_, 'honeypot': honeypot_, 'alternator': alternator_, 'solarPanel': solarPanel_, 'remark': remark_, 'idCardNo': idCardNo_, 'identityFront': identityFront_, 'identityBack': identityBack_, 'realName': realName_, 'bankName': bankName_, 'branchName': branchName_, 'cardNo': cardNo_, 'bankFront': bankFront_, 'bankBack': bankBack_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'status': status_, 'id': id_, 'userId': userId_, 'swarmId': swarmId_, 'signTime': signTime_, 'amount': amount_, 'handsel': handsel_, 'contractBeeId': contractBeeId_, 'hiveNum': hiveNum_, 'standardNum': standardNum_, 'smallNum': smallNum_, 'tent': tent_, 'honeyMachine': honeyMachine_, 'scraper': scraper_, 'motorcycle': motorcycle_, 'honeypot': honeypot_, 'alternator': alternator_, 'solarPanel': solarPanel_, 'remark': remark_, 'idCardNo': idCardNo_, 'identityFront': identityFront_, 'identityBack': identityBack_, 'realName': realName_, 'bankName': bankName_, 'branchName': branchName_, 'cardNo': cardNo_, 'bankFront': bankFront_, 'bankBack': bankBack_}
        response = self.request.post(url=self.url+'/web/contract/edit-bee', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_contract_edit_honey(self, pics_=None, status_=None, id_=None, userId_=None, swarmId_=None, signTime_=None, amount_=None, handsel_=None, contractHoneyId_=None, variety_=None, type_=None, purchaseNum_=None, remark_=None, idCardNo_=None, identityFront_=None, identityBack_=None, realName_=None, bankName_=None, branchName_=None, cardNo_=None, bankFront_=None, bankBack_=None):
        if self.user is None:
            data = {'pics': pics_, 'status': status_, 'id': id_, 'userId': userId_, 'swarmId': swarmId_, 'signTime': signTime_, 'amount': amount_, 'handsel': handsel_, 'contractHoneyId': contractHoneyId_, 'variety': variety_, 'type': type_, 'purchaseNum': purchaseNum_, 'remark': remark_, 'idCardNo': idCardNo_, 'identityFront': identityFront_, 'identityBack': identityBack_, 'realName': realName_, 'bankName': bankName_, 'branchName': branchName_, 'cardNo': cardNo_, 'bankFront': bankFront_, 'bankBack': bankBack_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'status': status_, 'id': id_, 'userId': userId_, 'swarmId': swarmId_, 'signTime': signTime_, 'amount': amount_, 'handsel': handsel_, 'contractHoneyId': contractHoneyId_, 'variety': variety_, 'type': type_, 'purchaseNum': purchaseNum_, 'remark': remark_, 'idCardNo': idCardNo_, 'identityFront': identityFront_, 'identityBack': identityBack_, 'realName': realName_, 'bankName': bankName_, 'branchName': branchName_, 'cardNo': cardNo_, 'bankFront': bankFront_, 'bankBack': bankBack_}
        response = self.request.post(url=self.url+'/web/contract/edit-honey', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_contract_edit_pollen(self, pics_=None, status_=None, id_=None, userId_=None, swarmId_=None, signTime_=None, amount_=None, handsel_=None, contractPollenId_=None, variety_=None, type_=None, purchaseNum_=None, remark_=None, idCardNo_=None, identityFront_=None, identityBack_=None, realName_=None, bankName_=None, branchName_=None, cardNo_=None, bankFront_=None, bankBack_=None):
        if self.user is None:
            data = {'pics': pics_, 'status': status_, 'id': id_, 'userId': userId_, 'swarmId': swarmId_, 'signTime': signTime_, 'amount': amount_, 'handsel': handsel_, 'contractPollenId': contractPollenId_, 'variety': variety_, 'type': type_, 'purchaseNum': purchaseNum_, 'remark': remark_, 'idCardNo': idCardNo_, 'identityFront': identityFront_, 'identityBack': identityBack_, 'realName': realName_, 'bankName': bankName_, 'branchName': branchName_, 'cardNo': cardNo_, 'bankFront': bankFront_, 'bankBack': bankBack_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'status': status_, 'id': id_, 'userId': userId_, 'swarmId': swarmId_, 'signTime': signTime_, 'amount': amount_, 'handsel': handsel_, 'contractPollenId': contractPollenId_, 'variety': variety_, 'type': type_, 'purchaseNum': purchaseNum_, 'remark': remark_, 'idCardNo': idCardNo_, 'identityFront': identityFront_, 'identityBack': identityBack_, 'realName': realName_, 'bankName': bankName_, 'branchName': branchName_, 'cardNo': cardNo_, 'bankFront': bankFront_, 'bankBack': bankBack_}
        response = self.request.post(url=self.url+'/web/contract/edit-pollen', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_contract_list(self, statusList_=None, pn_=None, ps_=None, type_=None, sortType_=None):
        if self.user is None:
            data = {'statusList': statusList_, 'pn': pn_, 'ps': ps_, 'type': type_, 'sortType': sortType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'statusList': statusList_, 'pn': pn_, 'ps': ps_, 'type': type_, 'sortType': sortType_}
        response = self.request.post(url=self.url+'/web/contract/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_extract_apply_add(self, extractDate_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'extractDate': extractDate_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'extractDate': extractDate_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/web/extract-apply/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_extract_apply_my_extract_apply(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/extract-apply/my-extract-apply', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_price_list(self, category_=None, variety_=None):
        if self.user is None:
            data = {'category': category_, 'variety': variety_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'category': category_, 'variety': variety_}
        response = self.request.post(url=self.url+'/web/price/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_price_ref_price(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/price/ref-price', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_price_total(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/price/total', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
