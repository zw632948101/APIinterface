#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
from utils.checkApiChanges.checher.apiTestResult import apiTestResult
import json


class memberAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('MP_MEMBER')

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

    def _admin_excel_export_marketing_list(self, pn_=None, ps_=None, name_=None, realName_=None, mobile_=None, memberNo_=None, platform_=None, type_=None, memberLevelId_=None, memberRole_=None, startRegisterTime_=None, endRegisterTime_=None, startIntegral_=None, endIntegral_=None, mkType_=None, limitType_=None, startLimitTime_=None, endLimitTime_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, 'realName': realName_, 'mobile': mobile_, 'memberNo': memberNo_, 'platform': platform_, 'type': type_, 'memberLevelId': memberLevelId_, 'memberRole': memberRole_, 'startRegisterTime': startRegisterTime_, 'endRegisterTime': endRegisterTime_, 'startIntegral': startIntegral_, 'endIntegral': endIntegral_, 'mkType': mkType_, 'limitType': limitType_, 'startLimitTime': startLimitTime_, 'endLimitTime': endLimitTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_, 'realName': realName_, 'mobile': mobile_, 'memberNo': memberNo_, 'platform': platform_, 'type': type_, 'memberLevelId': memberLevelId_, 'memberRole': memberRole_, 'startRegisterTime': startRegisterTime_, 'endRegisterTime': endRegisterTime_, 'startIntegral': startIntegral_, 'endIntegral': endIntegral_, 'mkType': mkType_, 'limitType': limitType_, 'startLimitTime': startLimitTime_, 'endLimitTime': endLimitTime_}
        response = self.request.get(url=self.url+'/admin/excel-export/marketing-list', params=data, hosts=self.url)
        apiTestResult(api='/admin/excel-export/marketing-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_marketing_list_by_id(self, memberIds_=None, mkType_=None):
        if self.user is None:
            data = {'memberIds': memberIds_, 'mkType': mkType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'memberIds': memberIds_, 'mkType': mkType_}
        response = self.request.get(url=self.url+'/admin/excel-export/marketing-list-by-id', params=data, hosts=self.url)
        apiTestResult(api='/admin/excel-export/marketing-list-by-id', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_member(self, pn_=None, ps_=None, name_=None, realName_=None, mobile_=None, memberNo_=None, platform_=None, type_=None, memberLevelId_=None, memberRole_=None, startRegisterTime_=None, endRegisterTime_=None, startIntegral_=None, endIntegral_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, 'realName': realName_, 'mobile': mobile_, 'memberNo': memberNo_, 'platform': platform_, 'type': type_, 'memberLevelId': memberLevelId_, 'memberRole': memberRole_, 'startRegisterTime': startRegisterTime_, 'endRegisterTime': endRegisterTime_, 'startIntegral': startIntegral_, 'endIntegral': endIntegral_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_, 'realName': realName_, 'mobile': mobile_, 'memberNo': memberNo_, 'platform': platform_, 'type': type_, 'memberLevelId': memberLevelId_, 'memberRole': memberRole_, 'startRegisterTime': startRegisterTime_, 'endRegisterTime': endRegisterTime_, 'startIntegral': startIntegral_, 'endIntegral': endIntegral_}
        response = self.request.get(url=self.url+'/admin/excel-export/member', params=data, hosts=self.url)
        apiTestResult(api='/admin/excel-export/member', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_member_by_id(self, memberIds_=None, mkType_=None):
        if self.user is None:
            data = {'memberIds': memberIds_, 'mkType': mkType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'memberIds': memberIds_, 'mkType': mkType_}
        response = self.request.get(url=self.url+'/admin/excel-export/member-by-id', params=data, hosts=self.url)
        apiTestResult(api='/admin/excel-export/member-by-id', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_integralRule_add_normal(self, productIdList_=None, ruleType_=None, bizType_=None, ruleName_=None, remark_=None, applyRange_=None, reach_=None, integral_=None):
        if self.user is None:
            data = {'productIdList': productIdList_, 'ruleType': ruleType_, 'bizType': bizType_, 'ruleName': ruleName_, 'remark': remark_, 'applyRange': applyRange_, 'reach': reach_, 'integral': integral_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productIdList': productIdList_, 'ruleType': ruleType_, 'bizType': bizType_, 'ruleName': ruleName_, 'remark': remark_, 'applyRange': applyRange_, 'reach': reach_, 'integral': integral_}
        response = self.request.post(url=self.url+'/admin/integralRule/add-normal', data=data, hosts=self.url)
        apiTestResult(api='/admin/integralRule/add-normal', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_integralRule_add_rule_product(self, productIdList_=None, ruleId_=None, ruleType_=None):
        if self.user is None:
            data = {'productIdList': productIdList_, 'ruleId': ruleId_, 'ruleType': ruleType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productIdList': productIdList_, 'ruleId': ruleId_, 'ruleType': ruleType_}
        response = self.request.post(url=self.url+'/admin/integralRule/add-rule-product', data=data, hosts=self.url)
        apiTestResult(api='/admin/integralRule/add-rule-product', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_integralRule_del(self, ruleId_=None):
        if self.user is None:
            data = {'ruleId': ruleId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'ruleId': ruleId_}
        response = self.request.post(url=self.url+'/admin/integralRule/del', data=data, hosts=self.url)
        apiTestResult(api='/admin/integralRule/del', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_integralRule_del_rule_product(self, ruleProductId_=None):
        if self.user is None:
            data = {'ruleProductId': ruleProductId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'ruleProductId': ruleProductId_}
        response = self.request.post(url=self.url+'/admin/integralRule/del-rule-product', data=data, hosts=self.url)
        apiTestResult(api='/admin/integralRule/del-rule-product', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_integralRule_detail(self, ruleId_=None):
        if self.user is None:
            data = {'ruleId': ruleId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'ruleId': ruleId_}
        response = self.request.post(url=self.url+'/admin/integralRule/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/integralRule/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_integralRule_edit(self, productIdList_=None, ruleId_=None, ruleName_=None, remark_=None, applyRange_=None, reach_=None, integral_=None):
        if self.user is None:
            data = {'productIdList': productIdList_, 'ruleId': ruleId_, 'ruleName': ruleName_, 'remark': remark_, 'applyRange': applyRange_, 'reach': reach_, 'integral': integral_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'productIdList': productIdList_, 'ruleId': ruleId_, 'ruleName': ruleName_, 'remark': remark_, 'applyRange': applyRange_, 'reach': reach_, 'integral': integral_}
        response = self.request.post(url=self.url+'/admin/integralRule/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/integralRule/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_integralRule_list(self, ruleType_=None):
        if self.user is None:
            data = {'ruleType': ruleType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'ruleType': ruleType_}
        response = self.request.post(url=self.url+'/admin/integralRule/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/integralRule/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_integralRule_product_list(self, name_=None, class1_=None, class2_=None, class3_=None, ruleType_=None):
        if self.user is None:
            data = {'name': name_, 'class1': class1_, 'class2': class2_, 'class3': class3_, 'ruleType': ruleType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'class1': class1_, 'class2': class2_, 'class3': class3_, 'ruleType': ruleType_}
        response = self.request.post(url=self.url+'/admin/integralRule/product-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/integralRule/product-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_integralRule_update_status(self, ruleId_=None, isEnable_=None):
        if self.user is None:
            data = {'ruleId': ruleId_, 'isEnable': isEnable_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'ruleId': ruleId_, 'isEnable': isEnable_}
        response = self.request.post(url=self.url+'/admin/integralRule/update-status', data=data, hosts=self.url)
        apiTestResult(api='/admin/integralRule/update-status', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_marketingList_batch_add(self, memberIds_=None, type_=None, limitType_=None, dueDate_=None, remark_=None):
        if self.user is None:
            data = {'memberIds': memberIds_, 'type': type_, 'limitType': limitType_, 'dueDate': dueDate_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'memberIds': memberIds_, 'type': type_, 'limitType': limitType_, 'dueDate': dueDate_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/marketingList/batch-add', data=data, hosts=self.url)
        apiTestResult(api='/admin/marketingList/batch-add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_marketingList_batch_del(self, mkIds_=None, type_=None):
        if self.user is None:
            data = {'mkIds': mkIds_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mkIds': mkIds_, 'type': type_}
        response = self.request.post(url=self.url+'/admin/marketingList/batch-del', data=data, hosts=self.url)
        apiTestResult(api='/admin/marketingList/batch-del', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_marketingList_del_by_memberId(self, memberId_=None, type_=None):
        if self.user is None:
            data = {'memberId': memberId_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'memberId': memberId_, 'type': type_}
        response = self.request.post(url=self.url+'/admin/marketingList/del-by-memberId', data=data, hosts=self.url)
        apiTestResult(api='/admin/marketingList/del-by-memberId', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_marketingList_detail(self, mkId_=None):
        if self.user is None:
            data = {'mkId': mkId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mkId': mkId_}
        response = self.request.post(url=self.url+'/admin/marketingList/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/marketingList/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_marketingList_detail_by_memberId(self, memberId_=None, type_=None):
        if self.user is None:
            data = {'memberId': memberId_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'memberId': memberId_, 'type': type_}
        response = self.request.post(url=self.url+'/admin/marketingList/detail-by-memberId', data=data, hosts=self.url)
        apiTestResult(api='/admin/marketingList/detail-by-memberId', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_marketingList_list(self, pn_=None, ps_=None, name_=None, realName_=None, mobile_=None, memberNo_=None, platform_=None, type_=None, memberLevelId_=None, memberRole_=None, startRegisterTime_=None, endRegisterTime_=None, startIntegral_=None, endIntegral_=None, mkType_=None, limitType_=None, startLimitTime_=None, endLimitTime_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, 'realName': realName_, 'mobile': mobile_, 'memberNo': memberNo_, 'platform': platform_, 'type': type_, 'memberLevelId': memberLevelId_, 'memberRole': memberRole_, 'startRegisterTime': startRegisterTime_, 'endRegisterTime': endRegisterTime_, 'startIntegral': startIntegral_, 'endIntegral': endIntegral_, 'mkType': mkType_, 'limitType': limitType_, 'startLimitTime': startLimitTime_, 'endLimitTime': endLimitTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_, 'realName': realName_, 'mobile': mobile_, 'memberNo': memberNo_, 'platform': platform_, 'type': type_, 'memberLevelId': memberLevelId_, 'memberRole': memberRole_, 'startRegisterTime': startRegisterTime_, 'endRegisterTime': endRegisterTime_, 'startIntegral': startIntegral_, 'endIntegral': endIntegral_, 'mkType': mkType_, 'limitType': limitType_, 'startLimitTime': startLimitTime_, 'endLimitTime': endLimitTime_}
        response = self.request.post(url=self.url+'/admin/marketingList/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/marketingList/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_benefits_add(self, benefitsName_=None, benefitsDesc_=None, icoUrl_=None, status_=None):
        if self.user is None:
            data = {'benefitsName': benefitsName_, 'benefitsDesc': benefitsDesc_, 'icoUrl': icoUrl_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'benefitsName': benefitsName_, 'benefitsDesc': benefitsDesc_, 'icoUrl': icoUrl_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/member-benefits/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/member-benefits/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_benefits_detail(self, benefitsId_=None):
        if self.user is None:
            data = {'benefitsId': benefitsId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'benefitsId': benefitsId_}
        response = self.request.post(url=self.url+'/admin/member-benefits/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/member-benefits/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_benefits_edit(self, benefitsName_=None, benefitsDesc_=None, icoUrl_=None, status_=None, benefitsId_=None):
        if self.user is None:
            data = {'benefitsName': benefitsName_, 'benefitsDesc': benefitsDesc_, 'icoUrl': icoUrl_, 'status': status_, 'benefitsId': benefitsId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'benefitsName': benefitsName_, 'benefitsDesc': benefitsDesc_, 'icoUrl': icoUrl_, 'status': status_, 'benefitsId': benefitsId_}
        response = self.request.post(url=self.url+'/admin/member-benefits/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/member-benefits/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_benefits_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/member-benefits/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/member-benefits/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_benefits_update_status(self, benefitsId_=None, status_=None):
        if self.user is None:
            data = {'benefitsId': benefitsId_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'benefitsId': benefitsId_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/member-benefits/update-status', data=data, hosts=self.url)
        apiTestResult(api='/admin/member-benefits/update-status', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_level_log_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/member-level-log/get', data=data, hosts=self.url)
        apiTestResult(api='/admin/member-level-log/get', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_level_add(self, benefitsList_=None, levelName_=None, levelDesc_=None, consumeMin_=None, consumeMax_=None, status_=None):
        if self.user is None:
            data = {'benefitsList': benefitsList_, 'levelName': levelName_, 'levelDesc': levelDesc_, 'consumeMin': consumeMin_, 'consumeMax': consumeMax_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'benefitsList': benefitsList_, 'levelName': levelName_, 'levelDesc': levelDesc_, 'consumeMin': consumeMin_, 'consumeMax': consumeMax_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/member-level/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/member-level/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_level_detail(self, memberLevelId_=None):
        if self.user is None:
            data = {'memberLevelId': memberLevelId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'memberLevelId': memberLevelId_}
        response = self.request.post(url=self.url+'/admin/member-level/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/member-level/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_level_edit(self, benefitsList_=None, levelName_=None, levelDesc_=None, consumeMin_=None, consumeMax_=None, status_=None, levelId_=None):
        if self.user is None:
            data = {'benefitsList': benefitsList_, 'levelName': levelName_, 'levelDesc': levelDesc_, 'consumeMin': consumeMin_, 'consumeMax': consumeMax_, 'status': status_, 'levelId': levelId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'benefitsList': benefitsList_, 'levelName': levelName_, 'levelDesc': levelDesc_, 'consumeMin': consumeMin_, 'consumeMax': consumeMax_, 'status': status_, 'levelId': levelId_}
        response = self.request.post(url=self.url+'/admin/member-level/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/member-level/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_level_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/member-level/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/member-level/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_add(self, platform_=None, platformRole_=None, memberRole_=None, type_=None, companyName_=None, mobile_=None, name_=None, email_=None, realName_=None, idCardNo_=None, gender_=None, age_=None, birthday_=None, headImg_=None, province_=None, city_=None, county_=None, tbName_=None, jdName_=None, mallName_=None, wechatName_=None):
        if self.user is None:
            data = {'platform': platform_, 'platformRole': platformRole_, 'memberRole': memberRole_, 'type': type_, 'companyName': companyName_, 'mobile': mobile_, 'name': name_, 'email': email_, 'realName': realName_, 'idCardNo': idCardNo_, 'gender': gender_, 'age': age_, 'birthday': birthday_, 'headImg': headImg_, 'province': province_, 'city': city_, 'county': county_, 'tbName': tbName_, 'jdName': jdName_, 'mallName': mallName_, 'wechatName': wechatName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'platform': platform_, 'platformRole': platformRole_, 'memberRole': memberRole_, 'type': type_, 'companyName': companyName_, 'mobile': mobile_, 'name': name_, 'email': email_, 'realName': realName_, 'idCardNo': idCardNo_, 'gender': gender_, 'age': age_, 'birthday': birthday_, 'headImg': headImg_, 'province': province_, 'city': city_, 'county': county_, 'tbName': tbName_, 'jdName': jdName_, 'mallName': mallName_, 'wechatName': wechatName_}
        response = self.request.post(url=self.url+'/admin/member/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/member/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_batch_tagged(self, memberIds_=None, tagIds_=None):
        if self.user is None:
            data = {'memberIds': memberIds_, 'tagIds': tagIds_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'memberIds': memberIds_, 'tagIds': tagIds_}
        response = self.request.post(url=self.url+'/admin/member/batch-tagged', data=data, hosts=self.url)
        apiTestResult(api='/admin/member/batch-tagged', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_cancel_tag(self, memberId_=None, tagId_=None):
        if self.user is None:
            data = {'memberId': memberId_, 'tagId': tagId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'memberId': memberId_, 'tagId': tagId_}
        response = self.request.post(url=self.url+'/admin/member/cancel-tag', data=data, hosts=self.url)
        apiTestResult(api='/admin/member/cancel-tag', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_detail(self, memberId_=None):
        if self.user is None:
            data = {'memberId': memberId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'memberId': memberId_}
        response = self.request.post(url=self.url+'/admin/member/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/member/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_edit(self, platform_=None, platformRole_=None, memberRole_=None, type_=None, companyName_=None, mobile_=None, name_=None, email_=None, realName_=None, idCardNo_=None, gender_=None, age_=None, birthday_=None, headImg_=None, province_=None, city_=None, county_=None, tbName_=None, jdName_=None, mallName_=None, wechatName_=None, memberId_=None):
        if self.user is None:
            data = {'platform': platform_, 'platformRole': platformRole_, 'memberRole': memberRole_, 'type': type_, 'companyName': companyName_, 'mobile': mobile_, 'name': name_, 'email': email_, 'realName': realName_, 'idCardNo': idCardNo_, 'gender': gender_, 'age': age_, 'birthday': birthday_, 'headImg': headImg_, 'province': province_, 'city': city_, 'county': county_, 'tbName': tbName_, 'jdName': jdName_, 'mallName': mallName_, 'wechatName': wechatName_, 'memberId': memberId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'platform': platform_, 'platformRole': platformRole_, 'memberRole': memberRole_, 'type': type_, 'companyName': companyName_, 'mobile': mobile_, 'name': name_, 'email': email_, 'realName': realName_, 'idCardNo': idCardNo_, 'gender': gender_, 'age': age_, 'birthday': birthday_, 'headImg': headImg_, 'province': province_, 'city': city_, 'county': county_, 'tbName': tbName_, 'jdName': jdName_, 'mallName': mallName_, 'wechatName': wechatName_, 'memberId': memberId_}
        response = self.request.post(url=self.url+'/admin/member/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/member/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_level_logs(self, memberId_=None):
        if self.user is None:
            data = {'memberId': memberId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'memberId': memberId_}
        response = self.request.post(url=self.url+'/admin/member/level-logs', data=data, hosts=self.url)
        apiTestResult(api='/admin/member/level-logs', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_list(self, pn_=None, ps_=None, name_=None, realName_=None, mobile_=None, memberNo_=None, platform_=None, type_=None, memberLevelId_=None, memberRole_=None, startRegisterTime_=None, endRegisterTime_=None, startIntegral_=None, endIntegral_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, 'realName': realName_, 'mobile': mobile_, 'memberNo': memberNo_, 'platform': platform_, 'type': type_, 'memberLevelId': memberLevelId_, 'memberRole': memberRole_, 'startRegisterTime': startRegisterTime_, 'endRegisterTime': endRegisterTime_, 'startIntegral': startIntegral_, 'endIntegral': endIntegral_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_, 'realName': realName_, 'mobile': mobile_, 'memberNo': memberNo_, 'platform': platform_, 'type': type_, 'memberLevelId': memberLevelId_, 'memberRole': memberRole_, 'startRegisterTime': startRegisterTime_, 'endRegisterTime': endRegisterTime_, 'startIntegral': startIntegral_, 'endIntegral': endIntegral_}
        response = self.request.post(url=self.url+'/admin/member/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/member/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_member_lock(self, memberIds_=None, isLock_=None):
        if self.user is None:
            data = {'memberIds': memberIds_, 'isLock': isLock_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'memberIds': memberIds_, 'isLock': isLock_}
        response = self.request.post(url=self.url+'/admin/member/member-lock', data=data, hosts=self.url)
        apiTestResult(api='/admin/member/member-lock', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_order_list(self, pn_=None, ps_=None, memberId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'memberId': memberId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'memberId': memberId_}
        response = self.request.post(url=self.url+'/admin/member/order-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/member/order-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_tagged(self, tagIds_=None, memberId_=None):
        if self.user is None:
            data = {'tagIds': tagIds_, 'memberId': memberId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'tagIds': tagIds_, 'memberId': memberId_}
        response = self.request.post(url=self.url+'/admin/member/tagged', data=data, hosts=self.url)
        apiTestResult(api='/admin/member/tagged', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_tags_by_memberId(self, memberId_=None):
        if self.user is None:
            data = {'memberId': memberId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'memberId': memberId_}
        response = self.request.post(url=self.url+'/admin/member/tags-by-memberId', data=data, hosts=self.url)
        apiTestResult(api='/admin/member/tags-by-memberId', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_update_integral(self, memberId_=None, changeIntegral_=None, remark_=None):
        if self.user is None:
            data = {'memberId': memberId_, 'changeIntegral': changeIntegral_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'memberId': memberId_, 'changeIntegral': changeIntegral_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/member/update-integral', data=data, hosts=self.url)
        apiTestResult(api='/admin/member/update-integral', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_member_update_level(self, memberId_=None, levelId_=None, isLock_=None, remark_=None):
        if self.user is None:
            data = {'memberId': memberId_, 'levelId': levelId_, 'isLock': isLock_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'memberId': memberId_, 'levelId': levelId_, 'isLock': isLock_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/member/update-level', data=data, hosts=self.url)
        apiTestResult(api='/admin/member/update-level', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_memberAddress_get(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/memberAddress/get', data=data, hosts=self.url)
        apiTestResult(api='/admin/memberAddress/get', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_memberIntegralChange_list(self, pn_=None, ps_=None, memberId_=None, platform_=None, bizType_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'memberId': memberId_, 'platform': platform_, 'bizType': bizType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'memberId': memberId_, 'platform': platform_, 'bizType': bizType_}
        response = self.request.post(url=self.url+'/admin/memberIntegralChange/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/memberIntegralChange/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_tag_add(self, name_=None, remark_=None):
        if self.user is None:
            data = {'name': name_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/tag/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/tag/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_tag_del(self, tagId_=None):
        if self.user is None:
            data = {'tagId': tagId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'tagId': tagId_}
        response = self.request.post(url=self.url+'/admin/tag/del', data=data, hosts=self.url)
        apiTestResult(api='/admin/tag/del', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_tag_detail(self, tagId_=None):
        if self.user is None:
            data = {'tagId': tagId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'tagId': tagId_}
        response = self.request.post(url=self.url+'/admin/tag/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/tag/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_tag_edit(self, tagId_=None, name_=None, remark_=None):
        if self.user is None:
            data = {'tagId': tagId_, 'name': name_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'tagId': tagId_, 'name': name_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/tag/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/tag/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_tag_list(self, pn_=None, ps_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/tag/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/tag/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_tag_tagged_by_tag(self, memberIds_=None, tagId_=None):
        if self.user is None:
            data = {'memberIds': memberIds_, 'tagId': tagId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'memberIds': memberIds_, 'tagId': tagId_}
        response = self.request.post(url=self.url+'/admin/tag/tagged-by-tag', data=data, hosts=self.url)
        apiTestResult(api='/admin/tag/tagged-by-tag', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_member_job_black_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/member-job/black-list', data=data, hosts=self.url)
        apiTestResult(api='/api/member-job/black-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_member_benefits_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/member/benefits-list', data=data, hosts=self.url)
        apiTestResult(api='/api/member/benefits-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_member_blackList_by_userId(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/member/blackList-by-userId', data=data, hosts=self.url)
        apiTestResult(api='/api/member/blackList-by-userId', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_member_import_members(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/member/import-members', data=data, hosts=self.url)
        apiTestResult(api='/api/member/import-members', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_member_integral_sync(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/member/integral-sync', data=data, hosts=self.url)
        apiTestResult(api='/api/member/integral-sync', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_member_member_by_userId(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/member/member-by-userId', data=data, hosts=self.url)
        apiTestResult(api='/api/member/member-by-userId', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_member_sync_member(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/member/sync-member', data=data, hosts=self.url)
        apiTestResult(api='/api/member/sync-member', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_member_sync_user_address(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/member/sync-user-address', data=data, hosts=self.url)
        apiTestResult(api='/api/member/sync-user-address', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))
