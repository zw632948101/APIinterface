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

    def _admin_deliveryStatus_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/deliveryStatus/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_orderInfo_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/orderInfo/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_delivery_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/delivery/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_deliveryStatus_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/deliveryStatus/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_orderInfo_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/orderInfo/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_delivery_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/delivery/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_deliveryStatus_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/deliveryStatus/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_orderInfo_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/orderInfo/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
