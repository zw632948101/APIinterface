#! /usr/bin/env python
# encoding: utf-8

from tools.Config import Config
from tools.Request import Request

import json

class PassportAction(object):
    def __init__(self, passport):
        self.log = Log('Passport')
        self.request = Request()
        self.passport = passport
        self.request.headers['_Device-Id_'] = self.passport.device_id
        self.request.headers['_Token_'] = self.passport.token
        env = Config('config').data['run']
        hosts = Config('config').data['hosts'][env]
        self.url = hosts.get('WF_PASSPORT')

    def admin_sso_email_login(self, appId=None, deviceType=None, deviceId=None, account=None, password=None):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'appId': appId, 'deviceType': deviceType, 'deviceId': deviceId, 'account': account, 'password': password}
        response = self.request.post(url=self.url+'/admin/sso/email-login', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_sso_logout(self):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id}
        response = self.request.post(url=self.url+'/admin/sso/logout', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_sso_automatic_login(self, token=None, encryptedPwd=None, deviceId=None):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'token': token, 'encryptedPwd': encryptedPwd, 'deviceId': deviceId}
        response = self.request.post(url=self.url+'/mobile/sso/automatic-login', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_sso_email_login(self, appId=None, deviceType=None, deviceId=None, account=None, password=None):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'appId': appId, 'deviceType': deviceType, 'deviceId': deviceId, 'account': account, 'password': password}
        response = self.request.post(url=self.url+'/mobile/sso/email-login', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_sso_email_registe(self, appId=None, deviceType=None, deviceId=None, account=None, userName=None, headImg=None, password=None):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'appId': appId, 'deviceType': deviceType, 'deviceId': deviceId, 'account': account, 'userName': userName, 'headImg': headImg, 'password': password}
        response = self.request.post(url=self.url+'/mobile/sso/email-registe', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_sso_logout(self):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id}
        response = self.request.post(url=self.url+'/mobile/sso/logout', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_sso_sms_login(self, appId=None, mobile=None, verifyCode=None, deviceType=None, deviceId=None):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'appId': appId, 'mobile': mobile, 'verifyCode': verifyCode, 'deviceType': deviceType, 'deviceId': deviceId}
        response = self.request.post(url=self.url+'/mobile/sso/sms-login', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_sso_third_bind_weixin(self, userName=None, userHeadImg=None, email=None, password=None, openId=None, accessToken=None, deviceId=None, authType=None, deviceType=None, appId=None):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'userName': userName, 'userHeadImg': userHeadImg, 'email': email, 'password': password, 'openId': openId, 'accessToken': accessToken, 'deviceId': deviceId, 'authType': authType, 'deviceType': deviceType, 'appId': appId}
        response = self.request.post(url=self.url+'/mobile/sso/third-bind-weixin', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_sso_third_login_weixin(self, code=None, deviceId=None, deviceType=None, authType=None, appId=None):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'code': code, 'deviceId': deviceId, 'deviceType': deviceType, 'authType': authType, 'appId': appId}
        response = self.request.post(url=self.url+'/mobile/sso/third-login-weixin', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_sso_verify_code_get(self, appId=None, mobile=None, bizType=None):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'appId': appId, 'mobile': mobile, 'bizType': bizType}
        response = self.request.post(url=self.url+'/mobile/sso/verify-code-get', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def sso_test_feign_test(self):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id}
        response = self.request.post(url=self.url+'/sso/test/feign-test', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def web_sso_check_account(self, email=None):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'email': email}
        response = self.request.post(url=self.url+'/web/sso/check-account', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def web_sso_email_login(self, appId=None, deviceType=None, deviceId=None, account=None, password=None):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'appId': appId, 'deviceType': deviceType, 'deviceId': deviceId, 'account': account, 'password': password}
        response = self.request.post(url=self.url+'/web/sso/email-login', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def web_sso_email_registe(self, token=None):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'token': token}
        response = self.request.post(url=self.url+'/web/sso/email-registe', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def web_sso_logout(self):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id}
        response = self.request.post(url=self.url+'/web/sso/logout', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def web_sso_validate_email(self, appId=None, deviceType=None, deviceId=None, account=None, userName=None, headImg=None, password=None):
        data = {'_tk_': self.passport.token, '_deviceId_': self.passport.device_id, 'appId': appId, 'deviceType': deviceType, 'deviceId': deviceId, 'account': account, 'userName': userName, 'headImg': headImg, 'password': password}
        response = self.request.post(url=self.url+'/web/sso/validate-email', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")
