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

    def _mall_banner_config_add(self, type_=None, url_=None, link_=None, sort_=None):
        if self.user is None:
            data = {'type': type_, 'url': url_, 'link': link_, 'sort': sort_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'type': type_, 'url': url_, 'link': link_, 'sort': sort_}
        response = self.request.post(url=self.url+'/mall/banner-config/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mall_banner_config_info(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mall/banner-config/info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mall_banner_config_on_off(self, id_=None, status_=None, sort_=None):
        if self.user is None:
            data = {'id': id_, 'status': status_, 'sort': sort_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'status': status_, 'sort': sort_}
        response = self.request.post(url=self.url+'/mall/banner-config/on-off', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mall_banner_config_sort(self, sortStr_=None):
        if self.user is None:
            data = {'sortStr': sortStr_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'sortStr': sortStr_}
        response = self.request.post(url=self.url+'/mall/banner-config/sort', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mall_hot_sale_config_info(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mall/hot-sale-config/info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mall_hot_sale_config_save(self, id_=None, url_=None, link_=None, sort_=None):
        if self.user is None:
            data = {'id': id_, 'url': url_, 'link': link_, 'sort': sort_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'url': url_, 'link': link_, 'sort': sort_}
        response = self.request.post(url=self.url+'/mall/hot-sale-config/save', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mall_hot_sale_config_sort(self, sortStr_=None):
        if self.user is None:
            data = {'sortStr': sortStr_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'sortStr': sortStr_}
        response = self.request.post(url=self.url+'/mall/hot-sale-config/sort', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mall_navigation_config_info(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mall/navigation-config/info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mall_navigation_config_save(self, id_=None, type_=None, url_=None, link_=None, sort_=None):
        if self.user is None:
            data = {'id': id_, 'type': type_, 'url': url_, 'link': link_, 'sort': sort_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'type': type_, 'url': url_, 'link': link_, 'sort': sort_}
        response = self.request.post(url=self.url+'/mall/navigation-config/save', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mall_navigation_config_sort(self, sortStr_=None):
        if self.user is None:
            data = {'sortStr': sortStr_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'sortStr': sortStr_}
        response = self.request.post(url=self.url+'/mall/navigation-config/sort', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mall_promotion_config_info(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mall/promotion-config/info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mall_promotion_config_save_group(self, id_=None, skuCode_=None):
        if self.user is None:
            data = {'id': id_, 'skuCode': skuCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'skuCode': skuCode_}
        response = self.request.post(url=self.url+'/mall/promotion-config/save-group', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mall_promotion_config_save_seckill(self, id_=None, skuCode_=None, startTime_=None, endTime_=None):
        if self.user is None:
            data = {'id': id_, 'skuCode': skuCode_, 'startTime': startTime_, 'endTime': endTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'skuCode': skuCode_, 'startTime': startTime_, 'endTime': endTime_}
        response = self.request.post(url=self.url+'/mall/promotion-config/save-seckill', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mall_recommend_config_info(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mall/recommend-config/info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mall_recommend_config_save(self, id_=None, skuCode_=None):
        if self.user is None:
            data = {'id': id_, 'skuCode': skuCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'skuCode': skuCode_}
        response = self.request.post(url=self.url+'/mall/recommend-config/save', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mall_switch_config_switch(self, type_=None, status_=None):
        if self.user is None:
            data = {'type': type_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'type': type_, 'status': status_}
        response = self.request.post(url=self.url+'/mall/switch-config/switch', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mall_switch_config_switch_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mall/switch-config/switch-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_category_list_by_level(self, level_=None):
        if self.user is None:
            data = {'level': level_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'level': level_}
        response = self.request.post(url=self.url+'/web/category/list-by-level', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_index_banner_hits(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/web/index/banner-hits', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_index_home_page(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/index/home-page', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sku_detail_group_cate(self, code_=None, userId_=None):
        if self.user is None:
            data = {'code': code_, 'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'userId': userId_}
        response = self.request.post(url=self.url+'/web/sku/detail-group-cate', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sku_list_group_by_cate(self, cate_=None):
        if self.user is None:
            data = {'cate': cate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cate': cate_}
        response = self.request.post(url=self.url+'/web/sku/list-group-by-cate', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sku_recommend_list(self, pn_=None, ps_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_}
        response = self.request.post(url=self.url+'/web/sku/recommend-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sku_search_list(self, pn_=None, ps_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_}
        response = self.request.post(url=self.url+'/web/sku/search-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
