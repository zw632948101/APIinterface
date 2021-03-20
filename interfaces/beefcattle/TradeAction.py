#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
from utils.checkApiChanges.checher.apiTestResult import apiTestResult
import json


class tradeAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('BF_TRADE')

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

    def _admin_cattleTrade_buy(self, servicePointId_=None, contactName_=None, contactPhone_=None, totalAmount_=None, deductAmount_=None, increaseAmount_=None, paymentMethod_=None, remark_=None, cattleHouseId_=None, cattlePenId_=None, cattleInfoJson_=None):
        if self.user is None:
            data = {'servicePointId': servicePointId_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'totalAmount': totalAmount_, 'deductAmount': deductAmount_, 'increaseAmount': increaseAmount_, 'paymentMethod': paymentMethod_, 'remark': remark_, 'cattleHouseId': cattleHouseId_, 'cattlePenId': cattlePenId_, 'cattleInfoJson': cattleInfoJson_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'servicePointId': servicePointId_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'totalAmount': totalAmount_, 'deductAmount': deductAmount_, 'increaseAmount': increaseAmount_, 'paymentMethod': paymentMethod_, 'remark': remark_, 'cattleHouseId': cattleHouseId_, 'cattlePenId': cattlePenId_, 'cattleInfoJson': cattleInfoJson_}
        response = self.request.post(url=self.url+'/admin/cattleTrade/buy', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleTrade/buy', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleTrade_detail(self, tradeId_=None):
        if self.user is None:
            data = {'tradeId': tradeId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'tradeId': tradeId_}
        response = self.request.post(url=self.url+'/admin/cattleTrade/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleTrade/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleTrade_page_list(self, pn_=None, ps_=None, servicePointId_=None, tradeType_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'servicePointId': servicePointId_, 'tradeType': tradeType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'servicePointId': servicePointId_, 'tradeType': tradeType_}
        response = self.request.post(url=self.url+'/admin/cattleTrade/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleTrade/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattleTrade_sell(self, servicePointId_=None, contactName_=None, contactPhone_=None, totalAmount_=None, deductAmount_=None, increaseAmount_=None, paymentMethod_=None, remark_=None, cattleHouseId_=None, cattlePenId_=None, cattleInfoJson_=None):
        if self.user is None:
            data = {'servicePointId': servicePointId_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'totalAmount': totalAmount_, 'deductAmount': deductAmount_, 'increaseAmount': increaseAmount_, 'paymentMethod': paymentMethod_, 'remark': remark_, 'cattleHouseId': cattleHouseId_, 'cattlePenId': cattlePenId_, 'cattleInfoJson': cattleInfoJson_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'servicePointId': servicePointId_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'totalAmount': totalAmount_, 'deductAmount': deductAmount_, 'increaseAmount': increaseAmount_, 'paymentMethod': paymentMethod_, 'remark': remark_, 'cattleHouseId': cattleHouseId_, 'cattlePenId': cattlePenId_, 'cattleInfoJson': cattleInfoJson_}
        response = self.request.post(url=self.url+'/admin/cattleTrade/sell', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattleTrade/sell', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_breed_buy_cattle_detail(self, servicePointId_=None, earTagNo_=None):
        if self.user is None:
            data = {'servicePointId': servicePointId_, 'earTagNo': earTagNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'servicePointId': servicePointId_, 'earTagNo': earTagNo_}
        response = self.request.post(url=self.url+'/mobile/breed/buy/cattle/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/breed/buy/cattle/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_breed_cattle_fence_list(self, cowshedId_=None):
        if self.user is None:
            data = {'cowshedId': cowshedId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cowshedId': cowshedId_}
        response = self.request.post(url=self.url+'/mobile/breed/cattle/fence/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/breed/cattle/fence/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_breed_cowshed_list(self, servicePointId_=None):
        if self.user is None:
            data = {'servicePointId': servicePointId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'servicePointId': servicePointId_}
        response = self.request.post(url=self.url+'/mobile/breed/cowshed/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/breed/cowshed/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_breed_sell_cattle_detail(self, servicePointId_=None, earTagNo_=None):
        if self.user is None:
            data = {'servicePointId': servicePointId_, 'earTagNo': earTagNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'servicePointId': servicePointId_, 'earTagNo': earTagNo_}
        response = self.request.post(url=self.url+'/mobile/breed/sell/cattle/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/breed/sell/cattle/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattle_trade_buy(self, servicePointId_=None, contactName_=None, contactPhone_=None, totalAmount_=None, deductAmount_=None, increaseAmount_=None, paymentMethod_=None, remark_=None, cattleHouseId_=None, cattlePenId_=None, cattleInfoJson_=None):
        if self.user is None:
            data = {'servicePointId': servicePointId_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'totalAmount': totalAmount_, 'deductAmount': deductAmount_, 'increaseAmount': increaseAmount_, 'paymentMethod': paymentMethod_, 'remark': remark_, 'cattleHouseId': cattleHouseId_, 'cattlePenId': cattlePenId_, 'cattleInfoJson': cattleInfoJson_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'servicePointId': servicePointId_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'totalAmount': totalAmount_, 'deductAmount': deductAmount_, 'increaseAmount': increaseAmount_, 'paymentMethod': paymentMethod_, 'remark': remark_, 'cattleHouseId': cattleHouseId_, 'cattlePenId': cattlePenId_, 'cattleInfoJson': cattleInfoJson_}
        response = self.request.post(url=self.url+'/mobile/cattle/trade/buy', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattle/trade/buy', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattle_trade_detail(self, tradeId_=None):
        if self.user is None:
            data = {'tradeId': tradeId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'tradeId': tradeId_}
        response = self.request.post(url=self.url+'/mobile/cattle/trade/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattle/trade/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattle_trade_page_list(self, pn_=None, ps_=None, servicePointId_=None, tradeType_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'servicePointId': servicePointId_, 'tradeType': tradeType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'servicePointId': servicePointId_, 'tradeType': tradeType_}
        response = self.request.post(url=self.url+'/mobile/cattle/trade/page-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattle/trade/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattle_trade_sell(self, servicePointId_=None, contactName_=None, contactPhone_=None, totalAmount_=None, deductAmount_=None, increaseAmount_=None, paymentMethod_=None, remark_=None, cattleHouseId_=None, cattlePenId_=None, cattleInfoJson_=None):
        if self.user is None:
            data = {'servicePointId': servicePointId_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'totalAmount': totalAmount_, 'deductAmount': deductAmount_, 'increaseAmount': increaseAmount_, 'paymentMethod': paymentMethod_, 'remark': remark_, 'cattleHouseId': cattleHouseId_, 'cattlePenId': cattlePenId_, 'cattleInfoJson': cattleInfoJson_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'servicePointId': servicePointId_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'totalAmount': totalAmount_, 'deductAmount': deductAmount_, 'increaseAmount': increaseAmount_, 'paymentMethod': paymentMethod_, 'remark': remark_, 'cattleHouseId': cattleHouseId_, 'cattlePenId': cattlePenId_, 'cattleInfoJson': cattleInfoJson_}
        response = self.request.post(url=self.url+'/mobile/cattle/trade/sell', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattle/trade/sell', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_item_apply_add(self, servicePointId_=None, warehouseCode_=None, companyCode_=None, applyDate_=None, remark_=None, itemDetailJson_=None):
        if self.user is None:
            data = {'servicePointId': servicePointId_, 'warehouseCode': warehouseCode_, 'companyCode': companyCode_, 'applyDate': applyDate_, 'remark': remark_, 'itemDetailJson': itemDetailJson_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'servicePointId': servicePointId_, 'warehouseCode': warehouseCode_, 'companyCode': companyCode_, 'applyDate': applyDate_, 'remark': remark_, 'itemDetailJson': itemDetailJson_}
        response = self.request.post(url=self.url+'/mobile/item/apply/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/item/apply/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_item_apply_detail(self, itemApplyId_=None):
        if self.user is None:
            data = {'itemApplyId': itemApplyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'itemApplyId': itemApplyId_}
        response = self.request.post(url=self.url+'/mobile/item/apply/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/item/apply/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_item_apply_page_list(self, pn_=None, ps_=None, servicePointId_=None, warehouseCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'servicePointId': servicePointId_, 'warehouseCode': warehouseCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'servicePointId': servicePointId_, 'warehouseCode': warehouseCode_}
        response = self.request.post(url=self.url+'/mobile/item/apply/page-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/item/apply/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_item_apply_sync_wms(self, itemApplyId_=None):
        if self.user is None:
            data = {'itemApplyId': itemApplyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'itemApplyId': itemApplyId_}
        response = self.request.post(url=self.url+'/mobile/item/apply/sync-wms', data=data, hosts=self.url)
        apiTestResult(api='/mobile/item/apply/sync-wms', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_wms_item_list(self, pn_=None, ps_=None, warehouseCode_=None, itemName_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'warehouseCode': warehouseCode_, 'itemName': itemName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'warehouseCode': warehouseCode_, 'itemName': itemName_}
        response = self.request.post(url=self.url+'/mobile/wms/item/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/wms/item/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_wms_warehouse_list(self, companyCode_=None):
        if self.user is None:
            data = {'companyCode': companyCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'companyCode': companyCode_}
        response = self.request.post(url=self.url+'/mobile/wms/warehouse/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/wms/warehouse/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))
