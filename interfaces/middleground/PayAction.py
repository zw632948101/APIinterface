#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
from utils.checkApiChanges.checher.apiTestResult import apiTestResult
import json


class payAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('MP_PAY')

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

    def _admin_api_channel_channelConfig(self, bodyId_=None, bodyName_=None, remark_=None):
        if self.user is None:
            data = {'bodyId': bodyId_, 'bodyName': bodyName_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'bodyId': bodyId_, 'bodyName': bodyName_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/api/channel/channelConfig', data=data, hosts=self.url)
        apiTestResult(api='/admin/api/channel/channelConfig', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_api_channel_loadBodyInfo(self, pageNum_=None, pageSize_=None):
        if self.user is None:
            data = {'pageNum': pageNum_, 'pageSize': pageSize_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pageNum': pageNum_, 'pageSize': pageSize_}
        response = self.request.post(url=self.url+'/admin/api/channel/loadBodyInfo', data=data, hosts=self.url)
        apiTestResult(api='/admin/api/channel/loadBodyInfo', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_api_channel_query_channel(self, bodyId_=None):
        if self.user is None:
            data = {'bodyId': bodyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'bodyId': bodyId_}
        response = self.request.post(url=self.url+'/admin/api/channel/query-channel', data=data, hosts=self.url)
        apiTestResult(api='/admin/api/channel/query-channel', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_api_config_cashConfig(self, saveCycle_=None, savePoint_=None, reserveAmount_=None, creator_=None, channleStatus_=None, autoSave_=None, bodyId_=None):
        if self.user is None:
            data = {'saveCycle': saveCycle_, 'savePoint': savePoint_, 'reserveAmount': reserveAmount_, 'creator': creator_, 'channleStatus': channleStatus_, 'autoSave': autoSave_, 'bodyId': bodyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'saveCycle': saveCycle_, 'savePoint': savePoint_, 'reserveAmount': reserveAmount_, 'creator': creator_, 'channleStatus': channleStatus_, 'autoSave': autoSave_, 'bodyId': bodyId_}
        response = self.request.post(url=self.url+'/admin/api/config/cashConfig', data=data, hosts=self.url)
        apiTestResult(api='/admin/api/config/cashConfig', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_api_config_channelConfig(self, id_=None, channelMchNo_=None, appId_=None, channelNo_=None, signKey_=None, encryptKey_=None, publicKey_=None, mchStatus_=None, channelStatus_=None, creatTime_=None, creator_=None, operator_=None, shopId_=None, shopName_=None, payWay_=None, bodyId_=None, bodyName_=None, rootPublicKey_=None, applyPublicKey_=None, serialNo_=None, merPrivateKey_=None, fee_=None, other_=None):
        if self.user is None:
            data = {'id': id_, 'channelMchNo': channelMchNo_, 'appId': appId_, 'channelNo': channelNo_, 'signKey': signKey_, 'encryptKey': encryptKey_, 'publicKey': publicKey_, 'mchStatus': mchStatus_, 'channelStatus': channelStatus_, 'creatTime': creatTime_, 'creator': creator_, 'operator': operator_, 'shopId': shopId_, 'shopName': shopName_, 'payWay': payWay_, 'bodyId': bodyId_, 'bodyName': bodyName_, 'rootPublicKey': rootPublicKey_, 'applyPublicKey': applyPublicKey_, 'serialNo': serialNo_, 'merPrivateKey': merPrivateKey_, 'fee': fee_, 'other': other_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'channelMchNo': channelMchNo_, 'appId': appId_, 'channelNo': channelNo_, 'signKey': signKey_, 'encryptKey': encryptKey_, 'publicKey': publicKey_, 'mchStatus': mchStatus_, 'channelStatus': channelStatus_, 'creatTime': creatTime_, 'creator': creator_, 'operator': operator_, 'shopId': shopId_, 'shopName': shopName_, 'payWay': payWay_, 'bodyId': bodyId_, 'bodyName': bodyName_, 'rootPublicKey': rootPublicKey_, 'applyPublicKey': applyPublicKey_, 'serialNo': serialNo_, 'merPrivateKey': merPrivateKey_, 'fee': fee_, 'other': other_}
        response = self.request.post(url=self.url+'/admin/api/config/channelConfig', data=data, hosts=self.url)
        apiTestResult(api='/admin/api/config/channelConfig', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_api_config_queryCashConfig(self, 主体ID_=None):
        if self.user is None:
            data = {'主体ID': 主体ID_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, '主体ID': 主体ID_}
        response = self.request.post(url=self.url+'/admin/api/config/queryCashConfig', data=data, hosts=self.url)
        apiTestResult(api='/admin/api/config/queryCashConfig', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    # def _admin_api_config_queryChannelConfig(self, 主体ID_=None, 渠道编号(微信：WX_PAY 支付宝：ALI_PAY 银联：UNION_PAY)_=None):
    #     if self.user is None:
    #         data = {'主体ID': 主体ID_, '渠道编号(微信：WX_PAY 支付宝：ALI_PAY 银联：UNION_PAY)': 渠道编号(微信：WX_PAY 支付宝：ALI_PAY 银联：UNION_PAY)_, }
    #     else:
    #         data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, '主体ID': 主体ID_, '渠道编号(微信：WX_PAY 支付宝：ALI_PAY 银联：UNION_PAY)': 渠道编号(微信：WX_PAY 支付宝：ALI_PAY 银联：UNION_PAY)_}
    #     response = self.request.post(url=self.url+'/admin/api/config/queryChannelConfig', data=data, hosts=self.url)
    #     apiTestResult(api='/admin/api/config/queryChannelConfig', host=self.url,datas=data, resp=response)
    #     return self.__judge_response_status(json.loads(response))

    def _admin_api_config_updateChannelConfig(self, id_=None, channelMchNo_=None, appId_=None, channelNo_=None, signKey_=None, encryptKey_=None, publicKey_=None, mchStatus_=None, channelStatus_=None, creatTime_=None, creator_=None, operator_=None, shopId_=None, shopName_=None, payWay_=None, bodyId_=None, bodyName_=None, rootPublicKey_=None, applyPublicKey_=None, serialNo_=None, merPrivateKey_=None, fee_=None, other_=None):
        if self.user is None:
            data = {'id': id_, 'channelMchNo': channelMchNo_, 'appId': appId_, 'channelNo': channelNo_, 'signKey': signKey_, 'encryptKey': encryptKey_, 'publicKey': publicKey_, 'mchStatus': mchStatus_, 'channelStatus': channelStatus_, 'creatTime': creatTime_, 'creator': creator_, 'operator': operator_, 'shopId': shopId_, 'shopName': shopName_, 'payWay': payWay_, 'bodyId': bodyId_, 'bodyName': bodyName_, 'rootPublicKey': rootPublicKey_, 'applyPublicKey': applyPublicKey_, 'serialNo': serialNo_, 'merPrivateKey': merPrivateKey_, 'fee': fee_, 'other': other_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'channelMchNo': channelMchNo_, 'appId': appId_, 'channelNo': channelNo_, 'signKey': signKey_, 'encryptKey': encryptKey_, 'publicKey': publicKey_, 'mchStatus': mchStatus_, 'channelStatus': channelStatus_, 'creatTime': creatTime_, 'creator': creator_, 'operator': operator_, 'shopId': shopId_, 'shopName': shopName_, 'payWay': payWay_, 'bodyId': bodyId_, 'bodyName': bodyName_, 'rootPublicKey': rootPublicKey_, 'applyPublicKey': applyPublicKey_, 'serialNo': serialNo_, 'merPrivateKey': merPrivateKey_, 'fee': fee_, 'other': other_}
        response = self.request.post(url=self.url+'/admin/api/config/updateChannelConfig', data=data, hosts=self.url)
        apiTestResult(api='/admin/api/config/updateChannelConfig', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_api_payOrder_detail(self, payOrderNo_=None):
        if self.user is None:
            data = {'payOrderNo': payOrderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'payOrderNo': payOrderNo_}
        response = self.request.post(url=self.url+'/admin/api/payOrder/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/api/payOrder/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_api_payOrder_export(self, pageNum_=None, pageSize_=None, payOrderNo_=None, tradeOrderNo_=None, channelNo_=None, status_=None, bodyId_=None, bodyName_=None, startTime_=None, endTime_=None):
        if self.user is None:
            data = {'pageNum': pageNum_, 'pageSize': pageSize_, 'payOrderNo': payOrderNo_, 'tradeOrderNo': tradeOrderNo_, 'channelNo': channelNo_, 'status': status_, 'bodyId': bodyId_, 'bodyName': bodyName_, 'startTime': startTime_, 'endTime': endTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pageNum': pageNum_, 'pageSize': pageSize_, 'payOrderNo': payOrderNo_, 'tradeOrderNo': tradeOrderNo_, 'channelNo': channelNo_, 'status': status_, 'bodyId': bodyId_, 'bodyName': bodyName_, 'startTime': startTime_, 'endTime': endTime_}
        response = self.request.post(url=self.url+'/admin/api/payOrder/export', data=data, hosts=self.url)
        apiTestResult(api='/admin/api/payOrder/export', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_api_payOrder_query(self, pageNum_=None, pageSize_=None, payOrderNo_=None, tradeOrderNo_=None, channelNo_=None, status_=None, bodyId_=None, bodyName_=None, startTime_=None, endTime_=None):
        if self.user is None:
            data = {'pageNum': pageNum_, 'pageSize': pageSize_, 'payOrderNo': payOrderNo_, 'tradeOrderNo': tradeOrderNo_, 'channelNo': channelNo_, 'status': status_, 'bodyId': bodyId_, 'bodyName': bodyName_, 'startTime': startTime_, 'endTime': endTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pageNum': pageNum_, 'pageSize': pageSize_, 'payOrderNo': payOrderNo_, 'tradeOrderNo': tradeOrderNo_, 'channelNo': channelNo_, 'status': status_, 'bodyId': bodyId_, 'bodyName': bodyName_, 'startTime': startTime_, 'endTime': endTime_}
        response = self.request.post(url=self.url+'/admin/api/payOrder/query', data=data, hosts=self.url)
        apiTestResult(api='/admin/api/payOrder/query', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_api_refundOrder_detail(self, refundOrderNo_=None):
        if self.user is None:
            data = {'refundOrderNo': refundOrderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'refundOrderNo': refundOrderNo_}
        response = self.request.post(url=self.url+'/admin/api/refundOrder/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/api/refundOrder/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_api_refundOrder_export(self, pageNum_=None, pageSize_=None, refundOrderNo_=None, payOrderNo_=None, tradeOrderNo_=None, channelNo_=None, startTime_=None, endTime_=None):
        if self.user is None:
            data = {'pageNum': pageNum_, 'pageSize': pageSize_, 'refundOrderNo': refundOrderNo_, 'payOrderNo': payOrderNo_, 'tradeOrderNo': tradeOrderNo_, 'channelNo': channelNo_, 'startTime': startTime_, 'endTime': endTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pageNum': pageNum_, 'pageSize': pageSize_, 'refundOrderNo': refundOrderNo_, 'payOrderNo': payOrderNo_, 'tradeOrderNo': tradeOrderNo_, 'channelNo': channelNo_, 'startTime': startTime_, 'endTime': endTime_}
        response = self.request.post(url=self.url+'/admin/api/refundOrder/export', data=data, hosts=self.url)
        apiTestResult(api='/admin/api/refundOrder/export', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_api_refundOrder_query(self, pageNum_=None, pageSize_=None, refundOrderNo_=None, payOrderNo_=None, tradeOrderNo_=None, channelNo_=None, startTime_=None, endTime_=None):
        if self.user is None:
            data = {'pageNum': pageNum_, 'pageSize': pageSize_, 'refundOrderNo': refundOrderNo_, 'payOrderNo': payOrderNo_, 'tradeOrderNo': tradeOrderNo_, 'channelNo': channelNo_, 'startTime': startTime_, 'endTime': endTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pageNum': pageNum_, 'pageSize': pageSize_, 'refundOrderNo': refundOrderNo_, 'payOrderNo': payOrderNo_, 'tradeOrderNo': tradeOrderNo_, 'channelNo': channelNo_, 'startTime': startTime_, 'endTime': endTime_}
        response = self.request.post(url=self.url+'/admin/api/refundOrder/query', data=data, hosts=self.url)
        apiTestResult(api='/admin/api/refundOrder/query', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_api_tradeOrder_detail(self, tradeOrderNo_=None):
        if self.user is None:
            data = {'tradeOrderNo': tradeOrderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'tradeOrderNo': tradeOrderNo_}
        response = self.request.post(url=self.url+'/admin/api/tradeOrder/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/api/tradeOrder/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_api_tradeOrder_export(self, pageNum_=None, pageSize_=None, payOrderNo_=None, tradeOrderNo_=None, channelNo_=None, startTime_=None, endTime_=None, bodyName_=None, bodyId_=None):
        if self.user is None:
            data = {'pageNum': pageNum_, 'pageSize': pageSize_, 'payOrderNo': payOrderNo_, 'tradeOrderNo': tradeOrderNo_, 'channelNo': channelNo_, 'startTime': startTime_, 'endTime': endTime_, 'bodyName': bodyName_, 'bodyId': bodyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pageNum': pageNum_, 'pageSize': pageSize_, 'payOrderNo': payOrderNo_, 'tradeOrderNo': tradeOrderNo_, 'channelNo': channelNo_, 'startTime': startTime_, 'endTime': endTime_, 'bodyName': bodyName_, 'bodyId': bodyId_}
        response = self.request.post(url=self.url+'/admin/api/tradeOrder/export', data=data, hosts=self.url)
        apiTestResult(api='/admin/api/tradeOrder/export', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_api_tradeOrder_query(self, pageNum_=None, pageSize_=None, payOrderNo_=None, tradeOrderNo_=None, channelNo_=None, startTime_=None, endTime_=None, bodyName_=None, bodyId_=None):
        if self.user is None:
            data = {'pageNum': pageNum_, 'pageSize': pageSize_, 'payOrderNo': payOrderNo_, 'tradeOrderNo': tradeOrderNo_, 'channelNo': channelNo_, 'startTime': startTime_, 'endTime': endTime_, 'bodyName': bodyName_, 'bodyId': bodyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pageNum': pageNum_, 'pageSize': pageSize_, 'payOrderNo': payOrderNo_, 'tradeOrderNo': tradeOrderNo_, 'channelNo': channelNo_, 'startTime': startTime_, 'endTime': endTime_, 'bodyName': bodyName_, 'bodyId': bodyId_}
        response = self.request.post(url=self.url+'/admin/api/tradeOrder/query', data=data, hosts=self.url)
        apiTestResult(api='/admin/api/tradeOrder/query', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_bodyIncome_loadAllIncome(self, bodyId_=None, monthStart_=None, monthEnd_=None):
        if self.user is None:
            data = {'bodyId': bodyId_, 'monthStart': monthStart_, 'monthEnd': monthEnd_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'bodyId': bodyId_, 'monthStart': monthStart_, 'monthEnd': monthEnd_}
        response = self.request.post(url=self.url+'/admin/bodyIncome/loadAllIncome', data=data, hosts=self.url)
        apiTestResult(api='/admin/bodyIncome/loadAllIncome', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_bill_downloadTradeBill(self, accountType_=None, billDate_=None, billType_=None, bodyId_=None, channelNo_=None):
        if self.user is None:
            data = {'accountType': accountType_, 'billDate': billDate_, 'billType': billType_, 'bodyId': bodyId_, 'channelNo': channelNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'accountType': accountType_, 'billDate': billDate_, 'billType': billType_, 'bodyId': bodyId_, 'channelNo': channelNo_}
        response = self.request.post(url=self.url+'/api/bill/downloadTradeBill', data=data, hosts=self.url)
        apiTestResult(api='/api/bill/downloadTradeBill', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _common_api_file_uploadFile(self, file_=None, bodyId_=None):
        if self.user is None:
            data = {'file': file_, 'bodyId': bodyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'file': file_, 'bodyId': bodyId_}
        response = self.request.post(url=self.url+'/common/api/file/uploadFile', data=data, hosts=self.url)
        apiTestResult(api='/common/api/file/uploadFile', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _open_api_callBack_aliPayNotify(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/open/api/callBack/aliPayNotify', data=data, hosts=self.url)
        apiTestResult(api='/open/api/callBack/aliPayNotify', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _open_api_callBack_settleResultNotify(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/open/api/callBack/settleResultNotify', data=data, hosts=self.url)
        apiTestResult(api='/open/api/callBack/settleResultNotify', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _open_api_callBack_unifiedOrderNotify(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/open/api/callBack/unifiedOrderNotify', data=data, hosts=self.url)
        apiTestResult(api='/open/api/callBack/unifiedOrderNotify', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _open_api_onlineTrade_appletUnifiedOrder(self, body_=None, bodyId_=None, disregardaAmount_=None, due_=None, openId_=None, outTradeNo_=None, regardaAmount_=None, totalFee_=None):
        if self.user is None:
            data = {'body': body_, 'bodyId': bodyId_, 'disregardaAmount': disregardaAmount_, 'due': due_, 'openId': openId_, 'outTradeNo': outTradeNo_, 'regardaAmount': regardaAmount_, 'totalFee': totalFee_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'body': body_, 'bodyId': bodyId_, 'disregardaAmount': disregardaAmount_, 'due': due_, 'openId': openId_, 'outTradeNo': outTradeNo_, 'regardaAmount': regardaAmount_, 'totalFee': totalFee_}
        response = self.request.post(url=self.url+'/open/api/onlineTrade/appletUnifiedOrder', data=data, hosts=self.url)
        apiTestResult(api='/open/api/onlineTrade/appletUnifiedOrder', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _open_api_onlineTrade_querytOrder(self, bodyId_=None, outTradeNo_=None):
        if self.user is None:
            data = {'bodyId': bodyId_, 'outTradeNo': outTradeNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'bodyId': bodyId_, 'outTradeNo': outTradeNo_}
        response = self.request.post(url=self.url+'/open/api/onlineTrade/querytOrder', data=data, hosts=self.url)
        apiTestResult(api='/open/api/onlineTrade/querytOrder', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _open_api_trade_cashOrderPay(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/open/api/trade/cashOrderPay', jsons=input_, hosts=self.url)
        apiTestResult(api='/open/api/trade/cashOrderPay', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _open_api_trade_pay_query(self, bodyId_=None, outOrderNo_=None, source_=None, tradeOrderNo_=None):
        if self.user is None:
            data = {'bodyId': bodyId_, 'outOrderNo': outOrderNo_, 'source': source_, 'tradeOrderNo': tradeOrderNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'bodyId': bodyId_, 'outOrderNo': outOrderNo_, 'source': source_, 'tradeOrderNo': tradeOrderNo_}
        response = self.request.post(url=self.url+'/open/api/trade/pay-query', jsons=data, hosts=self.url)
        apiTestResult(api='/open/api/trade/pay-query', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _open_api_trade_refund(self, bodyId_=None, outOrderNo_=None, outRefundOrderNo_=None, refundAmount_=None, refundType_=None, source_=None):
        if self.user is None:
            data = {'bodyId': bodyId_, 'outOrderNo': outOrderNo_, 'outRefundOrderNo': outRefundOrderNo_, 'refundAmount': refundAmount_, 'refundType': refundType_, 'source': source_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'bodyId': bodyId_, 'outOrderNo': outOrderNo_, 'outRefundOrderNo': outRefundOrderNo_, 'refundAmount': refundAmount_, 'refundType': refundType_, 'source': source_}
        response = self.request.post(url=self.url+'/open/api/trade/refund', jsons=data, hosts=self.url)
        apiTestResult(api='/open/api/trade/refund', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _open_api_trade_refund_query(self, bodyId_=None, outRefundOrderNo_=None, source_=None):
        if self.user is None:
            data = {'bodyId': bodyId_, 'outRefundOrderNo': outRefundOrderNo_, 'source': source_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'bodyId': bodyId_, 'outRefundOrderNo': outRefundOrderNo_, 'source': source_}
        response = self.request.post(url=self.url+'/open/api/trade/refund-query', data=data, hosts=self.url)
        apiTestResult(api='/open/api/trade/refund-query', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _open_api_trade_tradePay(self, authCode_=None, bodyId_=None, disregardaAmount_=None, due_=None, mchCreateIp_=None, mchNo_=None, outOrderNo_=None, regardaAmount_=None, source_=None, subject_=None, totalAmount_=None):
        if self.user is None:
            data = {'authCode': authCode_, 'bodyId': bodyId_, 'disregardaAmount': disregardaAmount_, 'due': due_, 'mchCreateIp': mchCreateIp_, 'mchNo': mchNo_, 'outOrderNo': outOrderNo_, 'regardaAmount': regardaAmount_, 'source': source_, 'subject': subject_, 'totalAmount': totalAmount_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'authCode': authCode_, 'bodyId': bodyId_, 'disregardaAmount': disregardaAmount_, 'due': due_, 'mchCreateIp': mchCreateIp_, 'mchNo': mchNo_, 'outOrderNo': outOrderNo_, 'regardaAmount': regardaAmount_, 'source': source_, 'subject': subject_, 'totalAmount': totalAmount_}
        response = self.request.post(url=self.url+'/open/api/trade/tradePay', jsons=data, hosts=self.url)
        apiTestResult(api='/open/api/trade/tradePay', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _open_api_trade_withdraw(self, channelNo_=None, withdrawAmout_=None):
        if self.user is None:
            data = {'channelNo': channelNo_, 'withdrawAmout': withdrawAmout_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'channelNo': channelNo_, 'withdrawAmout': withdrawAmout_}
        response = self.request.post(url=self.url+'/open/api/trade/withdraw', jsons=data, hosts=self.url)
        apiTestResult(api='/open/api/trade/withdraw', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))
