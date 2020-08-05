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

    def _admin_invoice_apply_comfirm(self, applyId_=None, comfirmDate_=None, realAmount_=None):
        if self.user is None:
            data = {'applyId': applyId_, 'comfirmDate': comfirmDate_, 'realAmount': realAmount_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_, 'comfirmDate': comfirmDate_, 'realAmount': realAmount_}
        response = self.request.post(url=self.url+'/admin/invoice-apply/comfirm', data=data, hosts=self.url)
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

    def _admin_pay_apply_add(self, orderNo_=None, amount_=None, type_=None, payeeId_=None, remark_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, 'amount': amount_, 'type': type_, 'payeeId': payeeId_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_, 'amount': amount_, 'type': type_, 'payeeId': payeeId_, 'remark': remark_}
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

    def _admin_pay_apply_comfirm(self, applyId_=None):
        if self.user is None:
            data = {'applyId': applyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_}
        response = self.request.post(url=self.url+'/admin/pay-apply/comfirm', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_pay_apply_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/pay-apply/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_pay_apply_detail(self, applyId_=None):
        if self.user is None:
            data = {'applyId': applyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_}
        response = self.request.post(url=self.url+'/admin/pay-apply/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_pay_apply_page_list(self, pn_=None, ps_=None, payee_=None, applyer_=None, orderNo_=None, applyTimeStart_=None, applyTimeEnd_=None, status_=None, applyOrderType_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'payee': payee_, 'applyer': applyer_, 'orderNo': orderNo_, 'applyTimeStart': applyTimeStart_, 'applyTimeEnd': applyTimeEnd_, 'status': status_, 'applyOrderType': applyOrderType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'payee': payee_, 'applyer': applyer_, 'orderNo': orderNo_, 'applyTimeStart': applyTimeStart_, 'applyTimeEnd': applyTimeEnd_, 'status': status_, 'applyOrderType': applyOrderType_}
        response = self.request.post(url=self.url+'/admin/pay-apply/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_base_info(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/admin/purchase/base-info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_opt_log(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/admin/purchase/opt-log', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_page_list(self, pn_=None, ps_=None, createDate_=None, status_=None, province_=None, city_=None, county_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'createDate': createDate_, 'status': status_, 'province': province_, 'city': city_, 'county': county_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'createDate': createDate_, 'status': status_, 'province': province_, 'city': city_, 'county': county_}
        response = self.request.post(url=self.url+'/admin/purchase/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_pay_apply(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/admin/purchase/pay-apply', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_product_info(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/admin/purchase/product-info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_purchase_status_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/purchase/status-count', data=data, hosts=self.url)
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

    def _admin_quality_edit(self, qualityId_=None, type_=None, remark_=None, deductPrice_=None):
        if self.user is None:
            data = {'qualityId': qualityId_, 'type': type_, 'remark': remark_, 'deductPrice': deductPrice_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'qualityId': qualityId_, 'type': type_, 'remark': remark_, 'deductPrice': deductPrice_}
        response = self.request.post(url=self.url+'/admin/quality/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_quality_info(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/admin/quality/info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _config_common_get_all_enum_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/config/common/get-all-enum-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_extract_apply_cancel(self, applyId_=None, reasonType_=None):
        if self.user is None:
            data = {'applyId': applyId_, 'reasonType': reasonType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_, 'reasonType': reasonType_}
        response = self.request.post(url=self.url+'/mobile/extract-apply/cancel', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_extract_apply_close(self, applyId_=None, reasonType_=None):
        if self.user is None:
            data = {'applyId': applyId_, 'reasonType': reasonType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_, 'reasonType': reasonType_}
        response = self.request.post(url=self.url+'/mobile/extract-apply/close', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_extract_apply_confirm(self, pics_=None, applyId_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, extractDate_=None, remark_=None):
        if self.user is None:
            data = {'pics': pics_, 'applyId': applyId_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'extractDate': extractDate_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'applyId': applyId_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'extractDate': extractDate_, 'remark': remark_}
        response = self.request.post(url=self.url+'/mobile/extract-apply/confirm', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_extract_apply_detail(self, applyId_=None):
        if self.user is None:
            data = {'applyId': applyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_}
        response = self.request.post(url=self.url+'/mobile/extract-apply/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_extract_apply_list(self, pn_=None, ps_=None, searchType_=None, province_=None, city_=None, county_=None, status_=None, keyWord_=None, distanceType_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'searchType': searchType_, 'province': province_, 'city': city_, 'county': county_, 'status': status_, 'keyWord': keyWord_, 'distanceType': distanceType_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'searchType': searchType_, 'province': province_, 'city': city_, 'county': county_, 'status': status_, 'keyWord': keyWord_, 'distanceType': distanceType_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/mobile/extract-apply/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_invoice_apply_info_detail(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/invoice-apply/info-detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_invoice_apply_replenish(self, realName_=None, idCardNo_=None, idCardFrontImage_=None, address_=None):
        if self.user is None:
            data = {'realName': realName_, 'idCardNo': idCardNo_, 'idCardFrontImage': idCardFrontImage_, 'address': address_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'realName': realName_, 'idCardNo': idCardNo_, 'idCardFrontImage': idCardFrontImage_, 'address': address_}
        response = self.request.post(url=self.url+'/mobile/invoice-apply/replenish', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_pay_apply_receipt(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/mobile/pay-apply/receipt', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_product_add(self, pics_=None, sellerId_=None, category_=None, variety_=None, weight_=None, purity_=None, consistence_=None, humidity_=None, province_=None, city_=None, county_=None, manufactureDate_=None, remark_=None):
        if self.user is None:
            data = {'pics': pics_, 'sellerId': sellerId_, 'category': category_, 'variety': variety_, 'weight': weight_, 'purity': purity_, 'consistence': consistence_, 'humidity': humidity_, 'province': province_, 'city': city_, 'county': county_, 'manufactureDate': manufactureDate_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'sellerId': sellerId_, 'category': category_, 'variety': variety_, 'weight': weight_, 'purity': purity_, 'consistence': consistence_, 'humidity': humidity_, 'province': province_, 'city': city_, 'county': county_, 'manufactureDate': manufactureDate_, 'remark': remark_}
        response = self.request.post(url=self.url+'/mobile/product/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_product_del(self, applyId_=None):
        if self.user is None:
            data = {'applyId': applyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_}
        response = self.request.post(url=self.url+'/mobile/product/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_product_edit(self, pics_=None, id_=None, sellerId_=None, category_=None, variety_=None, weight_=None, purity_=None, consistence_=None, humidity_=None, province_=None, city_=None, county_=None, manufactureDate_=None, remark_=None):
        if self.user is None:
            data = {'pics': pics_, 'id': id_, 'sellerId': sellerId_, 'category': category_, 'variety': variety_, 'weight': weight_, 'purity': purity_, 'consistence': consistence_, 'humidity': humidity_, 'province': province_, 'city': city_, 'county': county_, 'manufactureDate': manufactureDate_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'id': id_, 'sellerId': sellerId_, 'category': category_, 'variety': variety_, 'weight': weight_, 'purity': purity_, 'consistence': consistence_, 'humidity': humidity_, 'province': province_, 'city': city_, 'county': county_, 'manufactureDate': manufactureDate_, 'remark': remark_}
        response = self.request.post(url=self.url+'/mobile/product/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_product_list(self, variety_=None, pn_=None, ps_=None, manufactureDate_=None, province_=None, city_=None, county_=None, category_=None, status_=None, searchKey_=None):
        if self.user is None:
            data = {'variety': variety_, 'pn': pn_, 'ps': ps_, 'manufactureDate': manufactureDate_, 'province': province_, 'city': city_, 'county': county_, 'category': category_, 'status': status_, 'searchKey': searchKey_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'variety': variety_, 'pn': pn_, 'ps': ps_, 'manufactureDate': manufactureDate_, 'province': province_, 'city': city_, 'county': county_, 'category': category_, 'status': status_, 'searchKey': searchKey_}
        response = self.request.post(url=self.url+'/mobile/product/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    # def _mobile_purchase_add(self, products[0]_productId_=None, products[0]_grade_=None, products[0]_price_=None, userId_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, remark_=None):
    #     if self.user is None:
    #         data = {'products[0]_productId': products[0]_productId_, 'products[0]_grade': products[0]_grade_, 'products[0]_price': products[0]_price_, 'userId': userId_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'remark': remark_, }
    #     else:
    #         data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'products[0]_productId': products[0]_productId_, 'products[0]_grade': products[0]_grade_, 'products[0]_price': products[0]_price_, 'userId': userId_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'remark': remark_}
    #     response = self.request.post(url=self.url+'/mobile/purchase/add', data=data, hosts=self.url)
    #     return self.__judge_response_status(json.loads(response))

    def _mobile_purchase_base_info(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/mobile/purchase/base-info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_purchase_confirm_grade(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/mobile/purchase/confirm-grade', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_purchase_deduction_confirm(self, orderId_=None):
        if self.user is None:
            data = {'orderId': orderId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderId': orderId_}
        response = self.request.post(url=self.url+'/mobile/purchase/deduction-confirm', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_purchase_del(self, orderId_=None):
        if self.user is None:
            data = {'orderId': orderId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderId': orderId_}
        response = self.request.post(url=self.url+'/mobile/purchase/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    # def _mobile_purchase_edit(self, products[0]_productId_=None, products[0]_grade_=None, products[0]_price_=None, orderId_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, remark_=None):
    #     if self.user is None:
    #         data = {'products[0]_productId': products[0]_productId_, 'products[0]_grade': products[0]_grade_, 'products[0]_price': products[0]_price_, 'orderId': orderId_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'remark': remark_, }
    #     else:
    #         data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'products[0]_productId': products[0]_productId_, 'products[0]_grade': products[0]_grade_, 'products[0]_price': products[0]_price_, 'orderId': orderId_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'remark': remark_}
    #     response = self.request.post(url=self.url+'/mobile/purchase/edit', data=data, hosts=self.url)
    #     return self.__judge_response_status(json.loads(response))

    def _mobile_purchase_edit_grade(self, productId_=None, grade_=None, price_=None):
        if self.user is None:
            data = {'productId': productId_, 'grade': grade_, 'price': price_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productId': productId_, 'grade': grade_, 'price': price_}
        response = self.request.post(url=self.url+'/mobile/purchase/edit-grade', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_purchase_friend_list(self, lat_=None, lng_=None):
        if self.user is None:
            data = {'lat': lat_, 'lng': lng_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'lat': lat_, 'lng': lng_}
        response = self.request.post(url=self.url+'/mobile/purchase/friend-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_purchase_page_list(self, pn_=None, ps_=None, createDate_=None, status_=None, province_=None, city_=None, county_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'createDate': createDate_, 'status': status_, 'province': province_, 'city': city_, 'county': county_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'createDate': createDate_, 'status': status_, 'province': province_, 'city': city_, 'county': county_}
        response = self.request.post(url=self.url+'/mobile/purchase/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_purchase_product_grade_list(self, catagory_=None):
        if self.user is None:
            data = {'catagory': catagory_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'catagory': catagory_}
        response = self.request.post(url=self.url+'/mobile/purchase/product-grade-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_purchase_product_list(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/mobile/purchase/product-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_purchase_product_sale_list(self, sellerId_=None):
        if self.user is None:
            data = {'sellerId': sellerId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'sellerId': sellerId_}
        response = self.request.post(url=self.url+'/mobile/purchase/product-sale-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_purchase_quality_commit(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/mobile/purchase/quality-commit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_extract_apply_add(self, userId_=None, extractDate_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'userId': userId_, 'extractDate': extractDate_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_, 'extractDate': extractDate_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/web/extract-apply/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_extract_apply_allot(self, applyId_=None, chargeId_=None):
        if self.user is None:
            data = {'applyId': applyId_, 'chargeId': chargeId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_, 'chargeId': chargeId_}
        response = self.request.post(url=self.url+'/web/extract-apply/allot', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_extract_apply_close(self, applyId_=None, reasonType_=None):
        if self.user is None:
            data = {'applyId': applyId_, 'reasonType': reasonType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_, 'reasonType': reasonType_}
        response = self.request.post(url=self.url+'/web/extract-apply/close', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_extract_apply_detail(self, applyId_=None):
        if self.user is None:
            data = {'applyId': applyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'applyId': applyId_}
        response = self.request.post(url=self.url+'/web/extract-apply/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_extract_apply_edit(self, id_=None, status_=None, extractDate_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'id': id_, 'status': status_, 'extractDate': extractDate_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'status': status_, 'extractDate': extractDate_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/web/extract-apply/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_extract_apply_list(self, pn_=None, ps_=None, applyNo_=None, status_=None, province_=None, city_=None, county_=None, creatorKeyWord_=None, chargeKeyWord_=None, extractDateStart_=None, extractDateEnd_=None, createDateStart_=None, createDateEnd_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'applyNo': applyNo_, 'status': status_, 'province': province_, 'city': city_, 'county': county_, 'creatorKeyWord': creatorKeyWord_, 'chargeKeyWord': chargeKeyWord_, 'extractDateStart': extractDateStart_, 'extractDateEnd': extractDateEnd_, 'createDateStart': createDateStart_, 'createDateEnd': createDateEnd_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'applyNo': applyNo_, 'status': status_, 'province': province_, 'city': city_, 'county': county_, 'creatorKeyWord': creatorKeyWord_, 'chargeKeyWord': chargeKeyWord_, 'extractDateStart': extractDateStart_, 'extractDateEnd': extractDateEnd_, 'createDateStart': createDateStart_, 'createDateEnd': createDateEnd_}
        response = self.request.post(url=self.url+'/web/extract-apply/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_extract_apply_my_extract_apply(self, userId_=None):
        if self.user is None:
            data = {'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_}
        response = self.request.post(url=self.url+'/web/extract-apply/my-extract-apply', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_extract_apply_stat(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/extract-apply/stat', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
