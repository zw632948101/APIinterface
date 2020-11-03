#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
import json
import random

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
        response = self.request.post(url=self.url + '/admin/biz/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_biz_list_all(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url + '/admin/biz/list-all', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_biz_list_enable(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url + '/admin/biz/list-enable', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_biz_page_list(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url + '/admin/biz/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_brand_add(self, name_=None, logo_=None):
        if self.user is None:
            data = {'name': name_, 'logo': logo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'logo': logo_}
        response = self.request.post(url=self.url + '/admin/brand/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_brand_change_status(self, id_=None, status_=None):
        if self.user is None:
            data = {'id': id_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/brand/change-status', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_brand_edit(self, id_=None, name_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/brand/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_brand_change_status(self, id_=None, status_=None):
        if self.user is None:
            data = {'id': id_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/brand/change-status', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_brand_edit(self, id_=None, name_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/brand/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_brand_list_all(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url + '/admin/brand/list-all', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_brand_list_enable(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url + '/admin/brand/list-enable', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_brand_page_list(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url + '/admin/brand/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_category_add(self, bizId_=None, name_=None, isSale_=None, remark_=None):
        if self.user is None:
            data = {'bizId': bizId_, 'name': name_, 'isSale': isSale_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'bizId': bizId_, 'name': name_,
                    'isSale': isSale_, 'remark': remark_}
        response = self.request.post(url=self.url + '/admin/category/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_category_change_status(self, id_=None, status_=None):
        if self.user is None:
            data = {'id': id_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/category/change-status', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_category_edit(self, code_=None, remark_=None, isSale_=None):
        if self.user is None:
            data = {'code': code_, 'remark': remark_, 'isSale': isSale_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'remark': remark_, 'isSale': isSale_}
        response = self.request.post(url=self.url+'/admin/category/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_category_change_status(self, id_=None, status_=None):
        if self.user is None:
            data = {'id': id_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/category/change-status', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_category_edit(self, code_=None, remark_=None, isSale_=None):
        if self.user is None:
            data = {'code': code_, 'remark': remark_, 'isSale': isSale_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'remark': remark_, 'isSale': isSale_}
        response = self.request.post(url=self.url+'/admin/category/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_category_enable_tree(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/category/enable-tree', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_category_page_list(self, pn_=None, ps_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url + '/admin/category/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_inventory_add(self, skuId_=None, skuCode_=None, quantity_=None):
        if self.user is None:
            data = {'skuId': skuId_, 'skuCode': skuCode_, 'quantity': quantity_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'skuId': skuId_, 'skuCode': skuCode_, 'quantity': quantity_}
        response = self.request.post(url=self.url+'/admin/inventory/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_inventory_page_list(self, pn_=None, ps_=None, skuCode_=None, skuName_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'skuCode': skuCode_, 'skuName': skuName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'skuCode': skuCode_, 'skuName': skuName_}
        response = self.request.post(url=self.url+'/admin/inventory/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_inventory_update(self, skuCode_=None, quantity_=None):
        if self.user is None:
            data = {'skuCode': skuCode_, 'quantity': quantity_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'skuCode': skuCode_, 'quantity': quantity_}
        response = self.request.post(url=self.url+'/admin/inventory/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_label_add(self, name_=None, type_=None):
        if self.user is None:
            data = {'name': name_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'type': type_}
        response = self.request.post(url=self.url+'/admin/label/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_label_change_status(self, id_=None, status_=None):
        if self.user is None:
            data = {'id': id_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/label/change-status', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_label_change_status(self, id_=None, status_=None):
        if self.user is None:
            data = {'id': id_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/label/change-status', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_label_edit(self, id_=None, name_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/label/edit', data=data, hosts=self.url)
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

    def _admin_label_page_list(self, pn_=None, ps_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, }
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

    def _admin_attr_add(self, attrName_=None, isSale_=None):
        if self.user is None:
            data = {'attrName': attrName_, 'isSale': isSale_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'attrName': attrName_,
                    'isSale': isSale_}
        response = self.request.post(url=self.url + '/admin/attr/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sku_page_list(self, pn_=None, ps_=None, skuCode_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'skuCode': skuCode_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url + '/admin/attr/list-all', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sku_edit(self, code_=None, name_=None, alias_=None, brandId_=None, basicCost_=None, minimumPrice_=None, marketPrice_=None, validity_=None, validityUnit_=None, netWeight_=None, grossWeight_=None, weightUnit_=None, baseUnit_=None, basicAttr_=None, saleAttr_=None):
        if self.user is None:
            data = {'code': code_, 'name': name_, 'alias': alias_, 'brandId': brandId_, 'basicCost': basicCost_, 'minimumPrice': minimumPrice_, 'marketPrice': marketPrice_, 'validity': validity_, 'validityUnit': validityUnit_, 'netWeight': netWeight_, 'grossWeight': grossWeight_, 'weightUnit': weightUnit_, 'baseUnit': baseUnit_, 'basicAttr': basicAttr_, 'saleAttr': saleAttr_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'name': name_, 'alias': alias_, 'brandId': brandId_, 'basicCost': basicCost_, 'minimumPrice': minimumPrice_, 'marketPrice': marketPrice_, 'validity': validity_, 'validityUnit': validityUnit_, 'netWeight': netWeight_, 'grossWeight': grossWeight_, 'weightUnit': weightUnit_, 'baseUnit': baseUnit_, 'basicAttr': basicAttr_, 'saleAttr': saleAttr_}
        response = self.request.post(url=self.url+'/admin/sku/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sku_page_list(self, pn_=None, ps_=None, skuCode_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'skuCode': skuCode_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'skuCode': skuCode_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/sku/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))


    '''data = {
	'_tk_': 'eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJjYzRmZWViZTQxOTc5MTMzMmJiY2ZmNWUwZmRmMDg0YSIsImRldmljZUdyb3VwIjoiVVNFUiIsImlwIjoiMTkyLjE2OC44OS4xNzUiLCJpc3MiOiJaWVBfU1NPIiwidXNlciI6IntcImFjY291bnRUeXBlXCI6MjEsXCJhcHBJZFwiOlwiMTFcIixcImRldmljZVR5cGVcIjpcIkFORFJPSUQtVVNFUlwiLFwiaGVhZEltZ1wiOlwiaHR0cDovL3p5cC1mYXJtLTIub3NzLWFwLXNvdXRoZWFzdC0xLmFsaXl1bmNzLmNvbS9kYXRhL2ZjLXVzZXIvaGVhZEltZy8xNTkzNTgyNTM0ODAzLmpwZ1wiLFwiaWRcIjo2OTQsXCJuZXdcIjpmYWxzZSxcInBhc3N3b3JkXCI6XCI3Mzc1MzA0MWY3NzZiNjg0MjE0NmFlNTA0MTQ4NjBiMzdmMzY5Nzg2Njk4N2NiMGZcIixcInBob25lXCI6XCIxNTM4ODEyNjA3MlwiLFwic3RhdHVzXCI6MSxcInVzZXJOYW1lXCI6XCLlvKDkuInlkbXlkbXlkbVcIn0iLCJpYXQiOjE2MDM5NTQxMTZ9.hdVU_wHvuasXDSZp9Rngu6KKeV41jl-ec6CXBGbvBHrQueIO5N4RWaB2GboL4brBzneHGAyLtDAsVg65QAaSdA',
	'_deviceId_': 'cc4feebe419791332bbcff5e0fdf084a',
	'id': 50,
	'status': 1
}
    re = requests.post(url="http://dev-gateway.worldfarm.com/mp-product/admin/label/change-status",data=data)
    result = re.json()
    print(result)'''