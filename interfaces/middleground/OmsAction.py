#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
from utils.checkApiChanges.checher.apiTestResult import apiTestResult
import json


class omsAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('MP_OMS')

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

    def _admin_order_delivery_info(self, omsOrderNo_=None):
        if self.user is None:
            data = {'omsOrderNo': omsOrderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'omsOrderNo': omsOrderNo_}
        response = self.request.post(url=self.url+'/admin/order/delivery-info', data=data, hosts=self.url)
        apiTestResult(api='/admin/order/delivery-info', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_order_detail(self, omsOrderNo_=None):
        if self.user is None:
            data = {'omsOrderNo': omsOrderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'omsOrderNo': omsOrderNo_}
        response = self.request.post(url=self.url+'/admin/order/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/order/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_order_list(self, orderStatus_=None, pn_=None, ps_=None, channelOrderNo_=None, startTime_=None, endTime_=None, buyerName_=None, channelCode_=None):
        if self.user is None:
            data = {'orderStatus': orderStatus_, 'pn': pn_, 'ps': ps_, 'channelOrderNo': channelOrderNo_, 'startTime': startTime_, 'endTime': endTime_, 'buyerName': buyerName_, 'channelCode': channelCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'orderStatus': orderStatus_, 'pn': pn_, 'ps': ps_, 'channelOrderNo': channelOrderNo_, 'startTime': startTime_, 'endTime': endTime_, 'buyerName': buyerName_, 'channelCode': channelCode_}
        response = self.request.post(url=self.url+'/admin/order/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/order/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_order_remark_add(self, omsOrderNo_=None, remark_=None):
        if self.user is None:
            data = {'omsOrderNo': omsOrderNo_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'omsOrderNo': omsOrderNo_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/order/remark/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/order/remark/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_order_remark_list(self, pn_=None, ps_=None, omsOrderNo_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'omsOrderNo': omsOrderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'omsOrderNo': omsOrderNo_}
        response = self.request.post(url=self.url+'/admin/order/remark/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/order/remark/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_order_shipment(self, omsOrderNo_=None):
        if self.user is None:
            data = {'omsOrderNo': omsOrderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'omsOrderNo': omsOrderNo_}
        response = self.request.post(url=self.url+'/admin/order/shipment', data=data, hosts=self.url)
        apiTestResult(api='/admin/order/shipment', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_delivery_status_change(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/delivery/status-change', data=data, hosts=self.url)
        apiTestResult(api='/api/delivery/status-change', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_mallOrder_order_sync(self, list_=None):
        if self.user is None:
            data = {'list': list_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'list': list_}
        response = self.request.post(url=self.url+'/api/mallOrder/order-sync', data=data, hosts=self.url)
        apiTestResult(api='/api/mallOrder/order-sync', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_mallOrder_status_sync(self, list_=None):
        if self.user is None:
            data = {'list': list_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'list': list_}
        response = self.request.post(url=self.url+'/api/mallOrder/status-sync', data=data, hosts=self.url)
        apiTestResult(api='/api/mallOrder/status-sync', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_task_deliveryBill_create(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/task/deliveryBill/create', data=data, hosts=self.url)
        apiTestResult(api='/api/task/deliveryBill/create', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_task_transportBill_create(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/task/transportBill/create', data=data, hosts=self.url)
        apiTestResult(api='/api/task/transportBill/create', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_mallOrder_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/mallOrder/get', data=data, hosts=self.url)
        apiTestResult(api='/mobile/mallOrder/get', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _web_mallOrder_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/mallOrder/get', data=data, hosts=self.url)
        apiTestResult(api='/web/mallOrder/get', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))
