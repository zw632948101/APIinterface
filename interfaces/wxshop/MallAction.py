#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
import json


class MallAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('WX_MALL')

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

    def _admin_evaluate_audit(self, evaluateNo_=None, status_=None):
        if self.user is None:
            data = {'evaluateNo': evaluateNo_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'evaluateNo': evaluateNo_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/evaluate/audit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_evaluate_list(self, pn_=None, ps_=None, contentStatus_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'contentStatus': contentStatus_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'contentStatus': contentStatus_}
        response = self.request.post(url=self.url+'/admin/evaluate/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_evaluate_order_detail(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/admin/evaluate/order-detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_evaluate_reply(self, evaluateNo_=None, comment_=None, replyEvaluateNo_=None):
        if self.user is None:
            data = {'evaluateNo': evaluateNo_, 'comment': comment_, 'replyEvaluateNo': replyEvaluateNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'evaluateNo': evaluateNo_, 'comment': comment_, 'replyEvaluateNo': replyEvaluateNo_}
        response = self.request.post(url=self.url+'/admin/evaluate/reply', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_callback_pay_notify(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/callback/pay/notify', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_favorite_check(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/favorite/check', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_omsDelivery_sync_logistics(self, logisticsList_=None):
        if self.user is None:
            data = {'logisticsList': logisticsList_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'logisticsList': logisticsList_}
        response = self.request.post(url=self.url+'/api/omsDelivery/sync-logistics', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_omsDelivery_sync_sign(self, signList_=None):
        if self.user is None:
            data = {'signList': signList_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'signList': signList_}
        response = self.request.post(url=self.url+'/api/omsDelivery/sync-sign', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_pay_trade_pay_notify_order(self, outTradeNo_=None):
        if self.user is None:
            data = {'outTradeNo': outTradeNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'outTradeNo': outTradeNo_}
        response = self.request.post(url=self.url+'/api/pay-trade/pay-notify-order', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_task_order_push_orders(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/task/order/push-orders', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_task_order_sync_order_status(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/task/order/sync-order-status', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_task_order_timed_close(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/api/task/order/timed-close', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_task_pay_channel_status_query(self, channelBillNos_=None):
        if self.user is None:
            data = {'channelBillNos': channelBillNos_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'channelBillNos': channelBillNos_}
        response = self.request.post(url=self.url+'/api/task/pay/channel/status/query', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_task_pay_notify_order(self, outTradeNo_=None):
        if self.user is None:
            data = {'outTradeNo': outTradeNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'outTradeNo': outTradeNo_}
        response = self.request.post(url=self.url+'/api/task/pay/notify-order', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_attach_upload(self, file_=None, type_=None):
        if self.user is None:
            data = {'file': file_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'file': file_, 'type': type_}
        response = self.request.post(url=self.url+'/web/attach/upload', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_cart_add(self, skuNo_=None, shopId_=None, amount_=None):
        if self.user is None:
            data = {'skuNo': skuNo_, 'shopId': shopId_, 'amount': amount_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'skuNo': skuNo_, 'shopId': shopId_, 'amount': amount_}
        response = self.request.post(url=self.url+'/web/cart/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_cart_balance(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/web/cart/balance', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_cart_buy_again(self, product_=None, shopId_=None):
        if self.user is None:
            data = {'product': product_, 'shopId': shopId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'product': product_, 'shopId': shopId_}
        response = self.request.post(url=self.url+'/web/cart/buy-again', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_cart_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/web/cart/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_cart_edit_amount(self, id_=None, amount_=None):
        if self.user is None:
            data = {'id': id_, 'amount': amount_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'amount': amount_}
        response = self.request.post(url=self.url+'/web/cart/edit-amount', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_cart_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/cart/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_cart_purchase(self, skuNo_=None, shopId_=None, amount_=None):
        if self.user is None:
            data = {'skuNo': skuNo_, 'shopId': shopId_, 'amount': amount_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'skuNo': skuNo_, 'shopId': shopId_, 'amount': amount_}
        response = self.request.post(url=self.url+'/web/cart/purchase', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_evaluate_add(self, orderNo_=None, serviceScore_=None, logisticsScore_=None, productEvaluateJson_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, 'serviceScore': serviceScore_, 'logisticsScore': logisticsScore_, 'productEvaluateJson': productEvaluateJson_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_, 'serviceScore': serviceScore_, 'logisticsScore': logisticsScore_, 'productEvaluateJson': productEvaluateJson_}
        response = self.request.post(url=self.url+'/web/evaluate/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_evaluate_count(self, skuNo_=None):
        if self.user is None:
            data = {'skuNo': skuNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'skuNo': skuNo_}
        response = self.request.post(url=self.url+'/web/evaluate/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_evaluate_list(self, pn_=None, ps_=None, skuNo_=None, evaluateStatus_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'skuNo': skuNo_, 'evaluateStatus': evaluateStatus_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'skuNo': skuNo_, 'evaluateStatus': evaluateStatus_}
        response = self.request.post(url=self.url+'/web/evaluate/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_favorite_add(self, skuNo_=None, shopId_=None):
        if self.user is None:
            data = {'skuNo': skuNo_, 'shopId': shopId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'skuNo': skuNo_, 'shopId': shopId_}
        response = self.request.post(url=self.url+'/web/favorite/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_favorite_cancel(self, skuNo_=None, shopId_=None):
        if self.user is None:
            data = {'skuNo': skuNo_, 'shopId': shopId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'skuNo': skuNo_, 'shopId': shopId_}
        response = self.request.post(url=self.url+'/web/favorite/cancel', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_favorite_list(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/web/favorite/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_order_close(self, pn_=None, ps_=None, orderNo_=None, reason_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'orderNo': orderNo_, 'reason': reason_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'orderNo': orderNo_, 'reason': reason_}
        response = self.request.post(url=self.url+'/web/order/close', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_order_delivery_info(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/web/order/delivery-info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_order_detail(self, orderNo_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/web/order/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_order_list(self, orderStatus_=None, pn_=None, ps_=None):
        if self.user is None:
            data = {'orderStatus': orderStatus_, 'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderStatus': orderStatus_, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/web/order/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_order_pending_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/order/pending-count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_order_submit_order(self, shopId_=None, product_=None, addressId_=None, freight_=None, deliveryType_=None, productPrice_=None, buyerMemo_=None):
        if self.user is None:
            data = {'shopId': shopId_, 'product': product_, 'addressId': addressId_, 'freight': freight_, 'deliveryType': deliveryType_, 'productPrice': productPrice_, 'buyerMemo': buyerMemo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'shopId': shopId_, 'product': product_, 'addressId': addressId_, 'freight': freight_, 'deliveryType': deliveryType_, 'productPrice': productPrice_, 'buyerMemo': buyerMemo_}
        response = self.request.post(url=self.url+'/web/order/submit-order', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_pay_trade_prepay_order(self, outTradeNo_=None, desAccountNo_=None, desAccountName_=None):
        if self.user is None:
            data = {'outTradeNo': outTradeNo_, 'desAccountNo': desAccountNo_, 'desAccountName': desAccountName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'outTradeNo': outTradeNo_, 'desAccountNo': desAccountNo_, 'desAccountName': desAccountName_}
        response = self.request.post(url=self.url+'/web/pay-trade/prepay-order', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
