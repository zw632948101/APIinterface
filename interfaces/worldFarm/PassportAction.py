#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
import json


class PassportAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('WF_PASSPORT')

    def set_user(self, mobile=None, account_type='wf_account', password=None):
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

    def _admin_sso_automatic_login(self, token=None, encryptedPwd=None, deviceId=None):
        if self.user is None:
            data = {'token': token, 'encryptedPwd': encryptedPwd, 'deviceId': deviceId, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'token': token, 'encryptedPwd': encryptedPwd, 'deviceId': deviceId}
        response = self.request.post(url=self.url+'/admin/sso/automatic-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sso_email_login(self, appId=None, deviceType=None, deviceId=None, account=None, password=None):
        if self.user is None:
            data = {'appId': appId, 'deviceType': deviceType, 'deviceId': deviceId, 'account': account, 'password': password, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId, 'deviceType': deviceType, 'deviceId': deviceId, 'account': account, 'password': password}
        response = self.request.post(url=self.url+'/admin/sso/email-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sso_login_by_wechat(self, code=None, deviceId=None, deviceType=None, authType=None, appId=None):
        if self.user is None:
            data = {'code': code, 'deviceId': deviceId, 'deviceType': deviceType, 'authType': authType, 'appId': appId, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code, 'deviceId': deviceId, 'deviceType': deviceType, 'authType': authType, 'appId': appId}
        response = self.request.post(url=self.url+'/admin/sso/login-by-wechat', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sso_logout(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/sso/logout', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sso_sms_login(self, appId=None, mobile=None, verifyCode=None, deviceType=None, deviceId=None):
        if self.user is None:
            data = {'appId': appId, 'mobile': mobile, 'verifyCode': verifyCode, 'deviceType': deviceType, 'deviceId': deviceId, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId, 'mobile': mobile, 'verifyCode': verifyCode, 'deviceType': deviceType, 'deviceId': deviceId}
        response = self.request.post(url=self.url+'/admin/sso/sms-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sso_verify_code_get(self, mobile=None, bizType=None):
        if self.user is None:
            data = {'mobile': mobile, 'bizType': bizType, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile, 'bizType': bizType}
        response = self.request.post(url=self.url+'/admin/sso/verify-code-get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_sso_automatic_login(self, token=None, encryptedPwd=None, deviceId=None):
        if self.user is None:
            data = {'token': token, 'encryptedPwd': encryptedPwd, 'deviceId': deviceId, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'token': token, 'encryptedPwd': encryptedPwd, 'deviceId': deviceId}
        response = self.request.post(url=self.url+'/mobile/sso/automatic-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_sso_email_login(self, appId=None, deviceType=None, deviceId=None, account=None, password=None):
        if self.user is None:
            data = {'appId': appId, 'deviceType': deviceType, 'deviceId': deviceId, 'account': account, 'password': password, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId, 'deviceType': deviceType, 'deviceId': deviceId, 'account': account, 'password': password}
        response = self.request.post(url=self.url+'/mobile/sso/email-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_sso_email_registe(self, appId=None, deviceType=None, deviceId=None, account=None, userName=None, headImg=None, password=None):
        if self.user is None:
            data = {'appId': appId, 'deviceType': deviceType, 'deviceId': deviceId, 'account': account, 'userName': userName, 'headImg': headImg, 'password': password, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId, 'deviceType': deviceType, 'deviceId': deviceId, 'account': account, 'userName': userName, 'headImg': headImg, 'password': password}
        response = self.request.post(url=self.url+'/mobile/sso/email-registe', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_sso_logout(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/sso/logout', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_sso_sms_login(self, appId=None, mobile=None, verifyCode=None, deviceType=None, deviceId=None):
        if self.user is None:
            data = {'appId': appId, 'mobile': mobile, 'verifyCode': verifyCode, 'deviceType': deviceType, 'deviceId': deviceId, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId, 'mobile': mobile, 'verifyCode': verifyCode, 'deviceType': deviceType, 'deviceId': deviceId}
        response = self.request.post(url=self.url+'/mobile/sso/sms-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_sso_third_bind_weixin(self, userName=None, userHeadImg=None, mobile=None, verifyCode=None, openId=None, accessToken=None, deviceId=None, authType=None, deviceType=None, appId=None):
        if self.user is None:
            data = {'userName': userName, 'userHeadImg': userHeadImg, 'mobile': mobile, 'verifyCode': verifyCode, 'openId': openId, 'accessToken': accessToken, 'deviceId': deviceId, 'authType': authType, 'deviceType': deviceType, 'appId': appId, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userName': userName, 'userHeadImg': userHeadImg, 'mobile': mobile, 'verifyCode': verifyCode, 'openId': openId, 'accessToken': accessToken, 'deviceId': deviceId, 'authType': authType, 'deviceType': deviceType, 'appId': appId}
        response = self.request.post(url=self.url+'/mobile/sso/third-bind-weixin', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_sso_third_login_weixin(self, code=None, deviceId=None, deviceType=None, authType=None, appId=None):
        if self.user is None:
            data = {'code': code, 'deviceId': deviceId, 'deviceType': deviceType, 'authType': authType, 'appId': appId, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code, 'deviceId': deviceId, 'deviceType': deviceType, 'authType': authType, 'appId': appId}
        response = self.request.post(url=self.url+'/mobile/sso/third-login-weixin', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_sso_verify_code_get(self, mobile=None, bizType=None):
        if self.user is None:
            data = {'mobile': mobile, 'bizType': bizType, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile, 'bizType': bizType}
        response = self.request.post(url=self.url+'/mobile/sso/verify-code-get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sso_check_account(self, email=None):
        if self.user is None:
            data = {'email': email, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'email': email}
        response = self.request.post(url=self.url+'/web/sso/check-account', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sso_email_login(self, appId=None, deviceType=None, deviceId=None, account=None, password=None):
        if self.user is None:
            data = {'appId': appId, 'deviceType': deviceType, 'deviceId': deviceId, 'account': account, 'password': password, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId, 'deviceType': deviceType, 'deviceId': deviceId, 'account': account, 'password': password}
        response = self.request.post(url=self.url+'/web/sso/email-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sso_email_registe(self, token=None):
        if self.user is None:
            data = {'token': token, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'token': token}
        response = self.request.post(url=self.url+'/web/sso/email-registe', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sso_logout(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/sso/logout', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sso_validate_email(self, appId=None, deviceType=None, deviceId=None, account=None, userName=None, headImg=None, password=None):
        if self.user is None:
            data = {'appId': appId, 'deviceType': deviceType, 'deviceId': deviceId, 'account': account, 'userName': userName, 'headImg': headImg, 'password': password, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId, 'deviceType': deviceType, 'deviceId': deviceId, 'account': account, 'userName': userName, 'headImg': headImg, 'password': password}
        response = self.request.post(url=self.url+'/web/sso/validate-email', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
