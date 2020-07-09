#! /usr/bin/env python
# encoding: utf-8

from tools.Config import Config
from tools.Request import Request

import json

class UserAction(object):
    def __init__(self, user):
        self.log = Log('User')
        self.request = Request()
        self.user = user
        self.request.headers['_Device-Id_'] = self.user.device_id
        self.request.headers['_Token_'] = self.user.token
        env = Config('config').data['run']
        hosts = Config('config').data['hosts'][env]
        self.url = hosts.get('WF_USER')

    def admin_user_detail(self, userId=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId}
        response = self.request.post(url=self.url+'/admin/user/detail', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_user_inner_list(self, pn=None, ps=None, status=None, userName=None, email=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn, 'ps': ps, 'status': status, 'userName': userName, 'email': email}
        response = self.request.post(url=self.url+'/admin/user/inner-list', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_user_user_list(self, pn=None, ps=None, status=None, userName=None, email=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn, 'ps': ps, 'status': status, 'userName': userName, 'email': email}
        response = self.request.post(url=self.url+'/admin/user/user-list', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def fc_admin_user_add(self, email=None, phone=None, userName=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'email': email, 'phone': phone, 'userName': userName}
        response = self.request.post(url=self.url+'/fc/admin/user/add', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def fc_admin_user_edit(self, userId=None, email=None, phone=None, userName=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId, 'email': email, 'phone': phone, 'userName': userName}
        response = self.request.post(url=self.url+'/fc/admin/user/edit', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def fc_mobile_user_change_verify_code(self, mobile=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile}
        response = self.request.post(url=self.url+'/fc/mobile/user/change-verify-code', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def fc_mobile_user_update_email(self, email=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'email': email}
        response = self.request.post(url=self.url+'/fc/mobile/user/update-email', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def fc_mobile_user_update_mobile(self, mobile=None, verifyCode=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile, 'verifyCode': verifyCode}
        response = self.request.post(url=self.url+'/fc/mobile/user/update-mobile', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def fc_mobile_user_update_password(self, newPassword=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'newPassword': newPassword}
        response = self.request.post(url=self.url+'/fc/mobile/user/update-password', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_user_detail(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/user/detail', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_user_get_push_alias(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/user/get-push-alias', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_user_send_pass_email(self, email=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'email': email}
        response = self.request.post(url=self.url+'/mobile/user/send-pass-email', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_user_send_update_email(self, email=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'email': email}
        response = self.request.post(url=self.url+'/mobile/user/send-update-email', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_user_update(self, userName=None, headImg=None, region=None, phone=None, gender=None, birthday=None, introduce=None, area=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userName': userName, 'headImg': headImg, 'region': region, 'phone': phone, 'gender': gender, 'birthday': birthday, 'introduce': introduce, 'area': area}
        response = self.request.post(url=self.url+'/mobile/user/update', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_user_update_locale(self, locale=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'locale': locale}
        response = self.request.post(url=self.url+'/mobile/user/update-locale', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_user_update_password(self, oldPassword=None, newPassword=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'oldPassword': oldPassword, 'newPassword': newPassword}
        response = self.request.post(url=self.url+'/mobile/user/update-password', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_user_upload_headImg(self, headImgFile=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'headImgFile': headImgFile}
        response = self.request.post(url=self.url+'/mobile/user/upload-headImg', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def web_im_get_accid(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/im/get-accid', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def web_im_get_seller_accid(self, toUserId=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'toUserId': toUserId}
        response = self.request.post(url=self.url+'/web/im/get-seller-accid', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def web_user_detail(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/user/detail', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def web_user_init_im_account(self):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/user/init-im-account', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def web_user_send_pass_email(self, email=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'email': email}
        response = self.request.post(url=self.url+'/web/user/send-pass-email', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def web_user_send_update_email(self, email=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'email': email}
        response = self.request.post(url=self.url+'/web/user/send-update-email', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def web_user_set_pass(self, password=None, token=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'password': password, 'token': token}
        response = self.request.post(url=self.url+'/web/user/set-pass', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def web_user_update(self, userName=None, headImg=None, region=None, phone=None, gender=None, birthday=None, introduce=None, area=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userName': userName, 'headImg': headImg, 'region': region, 'phone': phone, 'gender': gender, 'birthday': birthday, 'introduce': introduce, 'area': area}
        response = self.request.post(url=self.url+'/web/user/update', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def web_user_update_email(self, token=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'token': token}
        response = self.request.post(url=self.url+'/web/user/update-email', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def web_user_update_password(self, oldPassword=None, newPassword=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'oldPassword': oldPassword, 'newPassword': newPassword}
        response = self.request.post(url=self.url+'/web/user/update-password', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def web_user_upload_headImg(self, headImgFile=None):
        data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'headImgFile': headImgFile}
        response = self.request.post(url=self.url+'/web/user/upload-headImg', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")
