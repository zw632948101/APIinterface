#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
import json


class PassportAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('WX_PASSPORT')

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

    def _admin_sso_account_exist(self, appId_=None, mobile_=None):
        if self.user is None:
            data = {'appId': appId_, 'mobile': mobile_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId_, 'mobile': mobile_}
        response = self.request.post(url=self.url+'/admin/sso/account-exist', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sso_automatic_login(self, token_=None, encryptedPwd_=None, deviceId_=None):
        if self.user is None:
            data = {'token': token_, 'encryptedPwd': encryptedPwd_, 'deviceId': deviceId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'token': token_, 'encryptedPwd': encryptedPwd_, 'deviceId': deviceId_}
        response = self.request.post(url=self.url+'/admin/sso/automatic-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sso_email_login(self, appId_=None, deviceType_=None, deviceId_=None, account_=None, password_=None):
        if self.user is None:
            data = {'appId': appId_, 'deviceType': deviceType_, 'deviceId': deviceId_, 'account': account_, 'password': password_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId_, 'deviceType': deviceType_, 'deviceId': deviceId_, 'account': account_, 'password': password_}
        response = self.request.post(url=self.url+'/admin/sso/email-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sso_heart_beat(self, token_=None, encryptedPwd_=None, deviceId_=None):
        if self.user is None:
            data = {'token': token_, 'encryptedPwd': encryptedPwd_, 'deviceId': deviceId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'token': token_, 'encryptedPwd': encryptedPwd_, 'deviceId': deviceId_}
        response = self.request.post(url=self.url+'/admin/sso/heart-beat', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sso_login_by_wechat(self, code_=None, deviceId_=None, deviceType_=None, authType_=None, appId_=None):
        if self.user is None:
            data = {'code': code_, 'deviceId': deviceId_, 'deviceType': deviceType_, 'authType': authType_, 'appId': appId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'deviceId': deviceId_, 'deviceType': deviceType_, 'authType': authType_, 'appId': appId_}
        response = self.request.post(url=self.url+'/admin/sso/login-by-wechat', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sso_logout(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/sso/logout', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sso_sms_login(self, appId_=None, mobile_=None, verifyCode_=None, deviceType_=None, deviceId_=None):
        if self.user is None:
            data = {'appId': appId_, 'mobile': mobile_, 'verifyCode': verifyCode_, 'deviceType': deviceType_, 'deviceId': deviceId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId_, 'mobile': mobile_, 'verifyCode': verifyCode_, 'deviceType': deviceType_, 'deviceId': deviceId_}
        response = self.request.post(url=self.url+'/admin/sso/sms-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_sso_verify_code_get(self, mobile_=None, bizType_=None):
        if self.user is None:
            data = {'mobile': mobile_, 'bizType': bizType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile_, 'bizType': bizType_}
        response = self.request.post(url=self.url+'/admin/sso/verify-code-get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_sso_automatic_login(self, loginInput_=None):
        if self.user is None:
            data = {'loginInput': loginInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'loginInput': loginInput_}
        response = self.request.post(url=self.url+'/api/sso/automatic-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_sso_check_token(self, loginCheckInput_=None):
        if self.user is None:
            data = {'loginCheckInput': loginCheckInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'loginCheckInput': loginCheckInput_}
        response = self.request.post(url=self.url+'/api/sso/check-token', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_sso_exit(self, token_=None):
        if self.user is None:
            data = {'token': token_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'token': token_}
        response = self.request.post(url=self.url+'/api/sso/exit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_sso_frozen_id(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/sso/frozen-id', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_sso_kick(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/sso/kick', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_sso_logout(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/sso/logout', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_sso_send_login_code(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/sso/send-login-code', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_sso_sms_login(self, loginInput_=None):
        if self.user is None:
            data = {'loginInput': loginInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'loginInput': loginInput_}
        response = self.request.post(url=self.url+'/api/sso/sms-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_sso_wechat_login(self, loginInput_=None):
        if self.user is None:
            data = {'loginInput': loginInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'loginInput': loginInput_}
        response = self.request.post(url=self.url+'/api/sso/wechat-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_sso_automatic_login(self, token_=None, encryptedPwd_=None, deviceId_=None):
        if self.user is None:
            data = {'token': token_, 'encryptedPwd': encryptedPwd_, 'deviceId': deviceId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'token': token_, 'encryptedPwd': encryptedPwd_, 'deviceId': deviceId_}
        response = self.request.post(url=self.url+'/mobile/sso/automatic-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_sso_email_login(self, appId_=None, deviceType_=None, deviceId_=None, account_=None, password_=None):
        if self.user is None:
            data = {'appId': appId_, 'deviceType': deviceType_, 'deviceId': deviceId_, 'account': account_, 'password': password_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId_, 'deviceType': deviceType_, 'deviceId': deviceId_, 'account': account_, 'password': password_}
        response = self.request.post(url=self.url+'/mobile/sso/email-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_sso_email_registe(self, appId_=None, deviceType_=None, deviceId_=None, account_=None, userName_=None, headImg_=None, password_=None):
        if self.user is None:
            data = {'appId': appId_, 'deviceType': deviceType_, 'deviceId': deviceId_, 'account': account_, 'userName': userName_, 'headImg': headImg_, 'password': password_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId_, 'deviceType': deviceType_, 'deviceId': deviceId_, 'account': account_, 'userName': userName_, 'headImg': headImg_, 'password': password_}
        response = self.request.post(url=self.url+'/mobile/sso/email-registe', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_sso_logout(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/sso/logout', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_sso_sms_login(self, appId_=None, mobile_=None, verifyCode_=None, deviceType_=None, deviceId_=None):
        if self.user is None:
            data = {'appId': appId_, 'mobile': mobile_, 'verifyCode': verifyCode_, 'deviceType': deviceType_, 'deviceId': deviceId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId_, 'mobile': mobile_, 'verifyCode': verifyCode_, 'deviceType': deviceType_, 'deviceId': deviceId_}
        response = self.request.post(url=self.url+'/mobile/sso/sms-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_sso_third_bind_weixin(self, userName_=None, userHeadImg_=None, mobile_=None, verifyCode_=None, openId_=None, accessToken_=None, deviceId_=None, authType_=None, deviceType_=None, appId_=None):
        if self.user is None:
            data = {'userName': userName_, 'userHeadImg': userHeadImg_, 'mobile': mobile_, 'verifyCode': verifyCode_, 'openId': openId_, 'accessToken': accessToken_, 'deviceId': deviceId_, 'authType': authType_, 'deviceType': deviceType_, 'appId': appId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userName': userName_, 'userHeadImg': userHeadImg_, 'mobile': mobile_, 'verifyCode': verifyCode_, 'openId': openId_, 'accessToken': accessToken_, 'deviceId': deviceId_, 'authType': authType_, 'deviceType': deviceType_, 'appId': appId_}
        response = self.request.post(url=self.url+'/mobile/sso/third-bind-weixin', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_sso_third_login_weixin(self, code_=None, deviceId_=None, deviceType_=None, authType_=None, appId_=None):
        if self.user is None:
            data = {'code': code_, 'deviceId': deviceId_, 'deviceType': deviceType_, 'authType': authType_, 'appId': appId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'deviceId': deviceId_, 'deviceType': deviceType_, 'authType': authType_, 'appId': appId_}
        response = self.request.post(url=self.url+'/mobile/sso/third-login-weixin', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_sso_verify_code_get(self, mobile_=None, bizType_=None):
        if self.user is None:
            data = {'mobile': mobile_, 'bizType': bizType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile_, 'bizType': bizType_}
        response = self.request.post(url=self.url+'/mobile/sso/verify-code-get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sso_check_account(self, email_=None):
        if self.user is None:
            data = {'email': email_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'email': email_}
        response = self.request.post(url=self.url+'/web/sso/check-account', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sso_email_login(self, appId_=None, deviceType_=None, deviceId_=None, account_=None, password_=None):
        if self.user is None:
            data = {'appId': appId_, 'deviceType': deviceType_, 'deviceId': deviceId_, 'account': account_, 'password': password_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId_, 'deviceType': deviceType_, 'deviceId': deviceId_, 'account': account_, 'password': password_}
        response = self.request.post(url=self.url+'/web/sso/email-login', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sso_email_registe(self, token_=None):
        if self.user is None:
            data = {'token': token_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'token': token_}
        response = self.request.post(url=self.url+'/web/sso/email-registe', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sso_logout(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/sso/logout', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sso_mall_bind_wx(self, userName_=None, userHeadImg_=None, mobile_=None, verifyCode_=None, openId_=None, accessToken_=None, deviceId_=None, authType_=None, deviceType_=None, appId_=None):
        if self.user is None:
            data = {'userName': userName_, 'userHeadImg': userHeadImg_, 'mobile': mobile_, 'verifyCode': verifyCode_, 'openId': openId_, 'accessToken': accessToken_, 'deviceId': deviceId_, 'authType': authType_, 'deviceType': deviceType_, 'appId': appId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userName': userName_, 'userHeadImg': userHeadImg_, 'mobile': mobile_, 'verifyCode': verifyCode_, 'openId': openId_, 'accessToken': accessToken_, 'deviceId': deviceId_, 'authType': authType_, 'deviceType': deviceType_, 'appId': appId_}
        response = self.request.post(url=self.url+'/web/sso/mall-bind-wx', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sso_mall_login_wx(self, code_=None, encryptedData_=None, iv_=None, userName_=None, gender_=None, userHeadImg_=None, mobile_=None, deviceId_=None, deviceType_=None, authType_=None, appId_=None):
        if self.user is None:
            data = {'code': code_, 'encryptedData': encryptedData_, 'iv': iv_, 'userName': userName_, 'gender': gender_, 'userHeadImg': userHeadImg_, 'mobile': mobile_, 'deviceId': deviceId_, 'deviceType': deviceType_, 'authType': authType_, 'appId': appId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'encryptedData': encryptedData_, 'iv': iv_, 'userName': userName_, 'gender': gender_, 'userHeadImg': userHeadImg_, 'mobile': mobile_, 'deviceId': deviceId_, 'deviceType': deviceType_, 'authType': authType_, 'appId': appId_}
        response = self.request.post(url=self.url+'/web/sso/mall-login-wx', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_sso_validate_email(self, appId_=None, deviceType_=None, deviceId_=None, account_=None, userName_=None, headImg_=None, password_=None):
        if self.user is None:
            data = {'appId': appId_, 'deviceType': deviceType_, 'deviceId': deviceId_, 'account': account_, 'userName': userName_, 'headImg': headImg_, 'password': password_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId_, 'deviceType': deviceType_, 'deviceId': deviceId_, 'account': account_, 'userName': userName_, 'headImg': headImg_, 'password': password_}
        response = self.request.post(url=self.url+'/web/sso/validate-email', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
