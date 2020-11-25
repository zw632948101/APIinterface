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

    def _admin_attr_add(self, attrName_=None, isSale_=None):
        if self.user is None:
            data = {'attrName': attrName_, 'isSale': isSale_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'attrName': attrName_, 'isSale': isSale_}
        response = self.request.post(url=self.url+'/admin/attr/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_attr_change_status(self, id_=None, status_=None):
        if self.user is None:
            data = {'id': id_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/attr/change-status', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_attr_edit(self, id_=None, attrName_=None):
        if self.user is None:
            data = {'id': id_, 'attrName': attrName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'attrName': attrName_}
        response = self.request.post(url=self.url+'/admin/attr/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_attr_list_all(self, isSale_=None):
        if self.user is None:
            data = {'isSale': isSale_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'isSale': isSale_}
        response = self.request.post(url=self.url+'/admin/attr/list-all', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_attr_list_enable(self, isSale_=None):
        if self.user is None:
            data = {'isSale': isSale_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'isSale': isSale_}
        response = self.request.post(url=self.url+'/admin/attr/list-enable', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_attr_page_list(self, pn_=None, ps_=None, isSale_=None, attrName_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'isSale': isSale_, 'attrName': attrName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'isSale': isSale_, 'attrName': attrName_}
        response = self.request.post(url=self.url+'/admin/attr/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_biz_add(self, ruleName_=None):
        if self.user is None:
            data = {'ruleName': ruleName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'ruleName': ruleName_}
        response = self.request.post(url=self.url+'/admin/biz/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_biz_change_status(self, id_=None, status_=None):
        if self.user is None:
            data = {'id': id_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/biz/change-status', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_biz_edit(self, id_=None, name_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/biz/edit', data=data, hosts=self.url)
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

    def _admin_category_add(self, bizId_=None, pcode_=None, name_=None, isSale_=None, remark_=None):
        if self.user is None:
            data = {'bizId': bizId_, 'pcode': pcode_, 'name': name_, 'isSale': isSale_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'bizId': bizId_, 'pcode': pcode_, 'name': name_, 'isSale': isSale_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/category/add', data=data, hosts=self.url)
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
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/category/page-list', data=data, hosts=self.url)
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
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/label/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_release_opt_on_off_shelve(self, releaseId_=None, status_=None):
        if self.user is None:
            data = {'releaseId': releaseId_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'releaseId': releaseId_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/release-opt/on-off-shelve', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_release_opt_page_opt_list(self, pn_=None, ps_=None, channelId_=None, labelId_=None, labelName_=None, skuName_=None, skuCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'channelId': channelId_, 'labelId': labelId_, 'labelName': labelName_, 'skuName': skuName_, 'skuCode': skuCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'channelId': channelId_, 'labelId': labelId_, 'labelName': labelName_, 'skuName': skuName_, 'skuCode': skuCode_}
        response = self.request.post(url=self.url+'/admin/release-opt/page-opt-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_release_opt_qty_update(self, releaseId_=None):
        if self.user is None:
            data = {'releaseId': releaseId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'releaseId': releaseId_}
        response = self.request.post(url=self.url+'/admin/release-opt/qty-update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_release_opt_release(self, releaseId_=None):
        if self.user is None:
            data = {'releaseId': releaseId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'releaseId': releaseId_}
        response = self.request.post(url=self.url+'/admin/release-opt/release', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_release_add(self, channel_=None, skuCode_=None, name_=None, alias_=None, minimumPrice_=None, marketPrice_=None, labelId_=None, mediaIcon_=None, medias_=None, mediaDetails_=None):
        if self.user is None:
            data = {'channel': channel_, 'skuCode': skuCode_, 'name': name_, 'alias': alias_, 'minimumPrice': minimumPrice_, 'marketPrice': marketPrice_, 'labelId': labelId_, 'mediaIcon': mediaIcon_, 'medias': medias_, 'mediaDetails': mediaDetails_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'channel': channel_, 'skuCode': skuCode_, 'name': name_, 'alias': alias_, 'minimumPrice': minimumPrice_, 'marketPrice': marketPrice_, 'labelId': labelId_, 'mediaIcon': mediaIcon_, 'medias': medias_, 'mediaDetails': mediaDetails_}
        response = self.request.post(url=self.url+'/admin/release/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_release_detail(self, skuCode_=None):
        if self.user is None:
            data = {'skuCode': skuCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'skuCode': skuCode_}
        response = self.request.post(url=self.url+'/admin/release/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_release_page_list(self, pn_=None, ps_=None, skuCode_=None, name_=None, filterType_=None, channel_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'skuCode': skuCode_, 'name': name_, 'filterType': filterType_, 'channel': channel_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'skuCode': skuCode_, 'name': name_, 'filterType': filterType_, 'channel': channel_}
        response = self.request.post(url=self.url+'/admin/release/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_release_update(self, releaseId_=None, channel_=None, skuCode_=None, name_=None, alias_=None, minimumPrice_=None, marketPrice_=None, labelId_=None, mediaIcon_=None, medias_=None, mediaDetails_=None):
        if self.user is None:
            data = {'releaseId': releaseId_, 'channel': channel_, 'skuCode': skuCode_, 'name': name_, 'alias': alias_, 'minimumPrice': minimumPrice_, 'marketPrice': marketPrice_, 'labelId': labelId_, 'mediaIcon': mediaIcon_, 'medias': medias_, 'mediaDetails': mediaDetails_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'releaseId': releaseId_, 'channel': channel_, 'skuCode': skuCode_, 'name': name_, 'alias': alias_, 'minimumPrice': minimumPrice_, 'marketPrice': marketPrice_, 'labelId': labelId_, 'mediaIcon': mediaIcon_, 'medias': medias_, 'mediaDetails': mediaDetails_}
        response = self.request.post(url=self.url+'/admin/release/update', data=data, hosts=self.url)
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

    def _admin_section_prefix_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/section/prefix-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_add(self, name_=None, remark_=None):
        if self.user is None:
            data = {'name': name_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/shop/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_delete(self, id_=None, isDelete_=None):
        if self.user is None:
            data = {'id': id_, 'isDelete': isDelete_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'isDelete': isDelete_}
        response = self.request.post(url=self.url+'/admin/shop/delete', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_edit(self, id_=None, name_=None, remark_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/shop/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/shop/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_shop_list_all(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/shop/list-all', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sku_add(self, name_=None, alias_=None, class1_=None, class2_=None, class3_=None, brandId_=None, basicCost_=None, minimumPrice_=None, marketPrice_=None, validity_=None, validityUnit_=None, netWeight_=None, grossWeight_=None, baseUnit_=None, isSale_=None, airTransport_=None, basicAttr_=None, saleAttr_=None, length_=None, width_=None, height_=None, volume_=None, barCode_=None):
        if self.user is None:
            data = {'name': name_, 'alias': alias_, 'class1': class1_, 'class2': class2_, 'class3': class3_, 'brandId': brandId_, 'basicCost': basicCost_, 'minimumPrice': minimumPrice_, 'marketPrice': marketPrice_, 'validity': validity_, 'validityUnit': validityUnit_, 'netWeight': netWeight_, 'grossWeight': grossWeight_, 'baseUnit': baseUnit_, 'isSale': isSale_, 'airTransport': airTransport_, 'basicAttr': basicAttr_, 'saleAttr': saleAttr_, 'length': length_, 'width': width_, 'height': height_, 'volume': volume_, 'barCode': barCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'alias': alias_, 'class1': class1_, 'class2': class2_, 'class3': class3_, 'brandId': brandId_, 'basicCost': basicCost_, 'minimumPrice': minimumPrice_, 'marketPrice': marketPrice_, 'validity': validity_, 'validityUnit': validityUnit_, 'netWeight': netWeight_, 'grossWeight': grossWeight_, 'baseUnit': baseUnit_, 'isSale': isSale_, 'airTransport': airTransport_, 'basicAttr': basicAttr_, 'saleAttr': saleAttr_, 'length': length_, 'width': width_, 'height': height_, 'volume': volume_, 'barCode': barCode_}
        response = self.request.post(url=self.url+'/admin/sku/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sku_change_status(self, code_=None, status_=None):
        if self.user is None:
            data = {'code': code_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/sku/change-status', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sku_detail(self, skuCode_=None):
        if self.user is None:
            data = {'skuCode': skuCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'skuCode': skuCode_}
        response = self.request.post(url=self.url+'/admin/sku/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sku_edit(self, code_=None, name_=None, alias_=None, brandId_=None, basicCost_=None, minimumPrice_=None, marketPrice_=None, validity_=None, validityUnit_=None, netWeight_=None, grossWeight_=None, baseUnit_=None, isSale_=None, airTransport_=None, basicAttr_=None, saleAttr_=None, length_=None, width_=None, height_=None, volume_=None, barCode_=None):
        if self.user is None:
            data = {'code': code_, 'name': name_, 'alias': alias_, 'brandId': brandId_, 'basicCost': basicCost_, 'minimumPrice': minimumPrice_, 'marketPrice': marketPrice_, 'validity': validity_, 'validityUnit': validityUnit_, 'netWeight': netWeight_, 'grossWeight': grossWeight_, 'baseUnit': baseUnit_, 'isSale': isSale_, 'airTransport': airTransport_, 'basicAttr': basicAttr_, 'saleAttr': saleAttr_, 'length': length_, 'width': width_, 'height': height_, 'volume': volume_, 'barCode': barCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'name': name_, 'alias': alias_, 'brandId': brandId_, 'basicCost': basicCost_, 'minimumPrice': minimumPrice_, 'marketPrice': marketPrice_, 'validity': validity_, 'validityUnit': validityUnit_, 'netWeight': netWeight_, 'grossWeight': grossWeight_, 'baseUnit': baseUnit_, 'isSale': isSale_, 'airTransport': airTransport_, 'basicAttr': basicAttr_, 'saleAttr': saleAttr_, 'length': length_, 'width': width_, 'height': height_, 'volume': volume_, 'barCode': barCode_}
        response = self.request.post(url=self.url+'/admin/sku/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sku_page_list(self, pn_=None, ps_=None, skuCode_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'skuCode': skuCode_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'skuCode': skuCode_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/sku/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _attach_pic_upload(self, file_=None, type_=None):
        if self.user is None:
            data = {'file': file_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'file': file_, 'type': type_}
        response = self.request.post(url=self.url+'/attach/pic-upload', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
