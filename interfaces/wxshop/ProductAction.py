#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
import json


class ProductAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('WX_PRODUCT')

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

    def _web_category_list_by_level(self, level_=None):
        if self.user is None:
            data = {'level': level_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'level': level_}
        response = self.request.post(url=self.url+'/web/category/list-by-level', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sku_detail_group_cate(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/web/sku/detail-group-cate', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sku_list_group_by_cate(self, cate_=None):
        if self.user is None:
            data = {'cate': cate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cate': cate_}
        response = self.request.post(url=self.url+'/web/sku/list-group-by-cate', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
