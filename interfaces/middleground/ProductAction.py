#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
import json


class ProductAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('MP_PRODUCT')

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

    def _admin_biz_add(self, ruleName_=None):
        if self.user is None:
            data = {'ruleName': ruleName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'ruleName': ruleName_}
        response = self.request.post(url=self.url+'/admin/biz/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_biz_list_all(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/biz/list-all', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_biz_list_enable(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/biz/list-enable', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_biz_page_list(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/admin/biz/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_brand_add(self, name_=None, logo_=None):
        if self.user is None:
            data = {'name': name_, 'logo': logo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'logo': logo_}
        response = self.request.post(url=self.url+'/admin/brand/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_brand_list_all(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/brand/list-all', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_brand_list_enable(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/brand/list-enable', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_brand_page_list(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/admin/brand/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_category_add(self, bizId_=None, name_=None, isSale_=None, remark_=None):
        if self.user is None:
            data = {'bizId': bizId_, 'name': name_, 'isSale': isSale_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'bizId': bizId_, 'name': name_, 'isSale': isSale_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/category/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_category_page_list(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/admin/category/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_label_add(self, name_=None, type_=None):
        if self.user is None:
            data = {'name': name_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'type': type_}
        response = self.request.post(url=self.url+'/admin/label/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_label_list_all(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/label/list-all', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_label_list_by_type(self, type_=None, status_=None):
        if self.user is None:
            data = {'type': type_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'type': type_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/label/list-by-type', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_label_page_list(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/admin/label/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_section_add(self, prefix_=None, bizId_=None, num_=None):
        if self.user is None:
            data = {'prefix': prefix_, 'bizId': bizId_, 'num': num_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'prefix': prefix_, 'bizId': bizId_, 'num': num_}
        response = self.request.post(url=self.url+'/admin/section/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_section_list_all(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/section/list-all', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_section_page_list(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/admin/section/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
