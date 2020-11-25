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

    def _api_callback_pay_notify(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/callback/pay/notify', data=data, hosts=self.url)
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

    def _api_shop_get(self, shopId_=None):
        if self.user is None:
            data = {'shopId': shopId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'shopId': shopId_}
        response = self.request.post(url=self.url+'/api/shop/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_shop_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/shop/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_shop_list_by_ids(self, shopIds_=None):
        if self.user is None:
            data = {'shopIds': shopIds_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'shopIds': shopIds_}
        response = self.request.post(url=self.url+'/api/shop/list-by-ids', data=data, hosts=self.url)
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

    def _mobile_evaluate_order_add_(self, orderNo_=None, comment_=None, totalScore_=None, serviceScore_=None, logisticsScore_=None, productScore_=None):
        if self.user is None:
            data = {'orderNo': orderNo_, 'comment': comment_, 'totalScore': totalScore_, 'serviceScore': serviceScore_, 'logisticsScore': logisticsScore_, 'productScore': productScore_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderNo': orderNo_, 'comment': comment_, 'totalScore': totalScore_, 'serviceScore': serviceScore_, 'logisticsScore': logisticsScore_, 'productScore': productScore_}
        response = self.request.post(url=self.url+'/mobile/evaluate/order/add/', data=data, hosts=self.url)
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

    def _web_pay_trade_prepay_order(self, outTradeNos_=None, desAccountNo_=None, desAccountName_=None):
        if self.user is None:
            data = {'outTradeNos': outTradeNos_, 'desAccountNo': desAccountNo_, 'desAccountName': desAccountName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'outTradeNos': outTradeNos_, 'desAccountNo': desAccountNo_, 'desAccountName': desAccountName_}
        response = self.request.post(url=self.url+'/web/pay-trade/prepay-order', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
