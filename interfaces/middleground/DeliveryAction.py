#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
import json


class deliveryAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('MP_DELIVERY')

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

    def _admin_delivery_detail(self, deliveryId_=None):
        if self.user is None:
            data = {'deliveryId': deliveryId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'deliveryId': deliveryId_}
        response = self.request.post(url=self.url+'/admin/delivery/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_delivery_list(self, pn_=None, ps_=None, deliveryNo_=None, orderNo_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'deliveryNo': deliveryNo_, 'orderNo': orderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'deliveryNo': deliveryNo_, 'orderNo': orderNo_}
        response = self.request.post(url=self.url+'/admin/delivery/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_common_create_accessToken(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/api/common/create-accessToken', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_delivery_notify_receive(self, message_id_=None, token_=None, format_=None, request_body_=None, timestamp_=None):
        if self.user is None:
            data = {'message_id': message_id_, 'token': token_, 'format': format_, 'request_body': request_body_, 'timestamp': timestamp_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'message_id': message_id_, 'token': token_, 'format': format_, 'request_body': request_body_, 'timestamp': timestamp_}
        response = self.request.post(url=self.url+'/api/delivery-notify/receive', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_delivery_create(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/delivery/create', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_delivery_get_deliveryInfo(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/delivery/get-deliveryInfo', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_delivery_order_intercept(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/delivery/order-intercept', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_delivery_trace_list(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/delivery/trace-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
