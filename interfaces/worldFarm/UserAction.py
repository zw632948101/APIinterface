#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
import json


class UserAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('WF_USER')

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

    def _admin_user_agr_add(self, account=None, userName=None):
        if self.user is None:
            data = {'account': account, 'userName': userName, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'account': account, 'userName': userName}
        response = self.request.post(url=self.url+'/admin/user/agr/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_user_agr_edit(self, id=None, userName=None):
        if self.user is None:
            data = {'id': id, 'userName': userName, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id, 'userName': userName}
        response = self.request.post(url=self.url+'/admin/user/agr/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_user_agr_page_list(self, pageSize=None, pageNum=None, userName=None, status=None, email=None):
        if self.user is None:
            data = {'pageSize': pageSize, 'pageNum': pageNum, 'userName': userName, 'status': status, 'email': email, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pageSize': pageSize, 'pageNum': pageNum, 'userName': userName, 'status': status, 'email': email}
        response = self.request.post(url=self.url+'/admin/user/agr/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_user_agr_reset_password(self, id=None):
        if self.user is None:
            data = {'id': id, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id}
        response = self.request.post(url=self.url+'/admin/user/agr/reset-password', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_user_detail(self, userId=None):
        if self.user is None:
            data = {'userId': userId, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId}
        response = self.request.post(url=self.url+'/admin/user/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_user_inner_list(self, pn=None, ps=None, status=None, userName=None, email=None):
        if self.user is None:
            data = {'pn': pn, 'ps': ps, 'status': status, 'userName': userName, 'email': email, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn, 'ps': ps, 'status': status, 'userName': userName, 'email': email}
        response = self.request.post(url=self.url+'/admin/user/inner-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_user_user_list(self, pn=None, ps=None, status=None, userName=None, email=None):
        if self.user is None:
            data = {'pn': pn, 'ps': ps, 'status': status, 'userName': userName, 'email': email, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn, 'ps': ps, 'status': status, 'userName': userName, 'email': email}
        response = self.request.post(url=self.url+'/admin/user/user-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_bee_im_get_accid(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/bee/im/get-accid', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_bee_im_get_seller_accid(self, toUserId=None):
        if self.user is None:
            data = {'toUserId': toUserId, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'toUserId': toUserId}
        response = self.request.post(url=self.url+'/mobile/bee/im/get-seller-accid', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_detail(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/user/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_get_push_alias(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/user/get-push-alias', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_send_pass_email(self, email=None):
        if self.user is None:
            data = {'email': email, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'email': email}
        response = self.request.post(url=self.url+'/mobile/user/send-pass-email', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_send_update_email(self, email=None):
        if self.user is None:
            data = {'email': email, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'email': email}
        response = self.request.post(url=self.url+'/mobile/user/send-update-email', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_update(self, userName=None, headImg=None, region=None, phone=None, gender=None, birthday=None, introduce=None, area=None):
        if self.user is None:
            data = {'userName': userName, 'headImg': headImg, 'region': region, 'phone': phone, 'gender': gender, 'birthday': birthday, 'introduce': introduce, 'area': area, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userName': userName, 'headImg': headImg, 'region': region, 'phone': phone, 'gender': gender, 'birthday': birthday, 'introduce': introduce, 'area': area}
        response = self.request.post(url=self.url+'/mobile/user/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_update_locale(self, locale=None):
        if self.user is None:
            data = {'locale': locale, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'locale': locale}
        response = self.request.post(url=self.url+'/mobile/user/update-locale', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_update_password(self, oldPassword=None, newPassword=None):
        if self.user is None:
            data = {'oldPassword': oldPassword, 'newPassword': newPassword, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'oldPassword': oldPassword, 'newPassword': newPassword}
        response = self.request.post(url=self.url+'/mobile/user/update-password', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_upload_headImg(self, headImgFile=None):
        if self.user is None:
            data = {'headImgFile': headImgFile, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'headImgFile': headImgFile}
        response = self.request.post(url=self.url+'/mobile/user/upload-headImg', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_im_get_accid(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/im/get-accid', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_im_get_seller_accid(self, toUserId=None):
        if self.user is None:
            data = {'toUserId': toUserId, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'toUserId': toUserId}
        response = self.request.post(url=self.url+'/web/im/get-seller-accid', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_detail(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/user/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_init_im_account(self, accountType=None, userIds=None):
        if self.user is None:
            data = {'accountType': accountType, 'userIds': userIds, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'accountType': accountType, 'userIds': userIds}
        response = self.request.post(url=self.url+'/web/user/init-im-account', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_send_pass_email(self, email=None):
        if self.user is None:
            data = {'email': email, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'email': email}
        response = self.request.post(url=self.url+'/web/user/send-pass-email', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_send_update_email(self, email=None):
        if self.user is None:
            data = {'email': email, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'email': email}
        response = self.request.post(url=self.url+'/web/user/send-update-email', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_set_pass(self, password=None, token=None):
        if self.user is None:
            data = {'password': password, 'token': token, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'password': password, 'token': token}
        response = self.request.post(url=self.url+'/web/user/set-pass', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_update(self, userName=None, headImg=None, region=None, phone=None, gender=None, birthday=None, introduce=None, area=None):
        if self.user is None:
            data = {'userName': userName, 'headImg': headImg, 'region': region, 'phone': phone, 'gender': gender, 'birthday': birthday, 'introduce': introduce, 'area': area, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userName': userName, 'headImg': headImg, 'region': region, 'phone': phone, 'gender': gender, 'birthday': birthday, 'introduce': introduce, 'area': area}
        response = self.request.post(url=self.url+'/web/user/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_update_email(self, token=None):
        if self.user is None:
            data = {'token': token, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'token': token}
        response = self.request.post(url=self.url+'/web/user/update-email', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_update_password(self, oldPassword=None, newPassword=None):
        if self.user is None:
            data = {'oldPassword': oldPassword, 'newPassword': newPassword, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'oldPassword': oldPassword, 'newPassword': newPassword}
        response = self.request.post(url=self.url+'/web/user/update-password', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_upload_headImg(self, headImgFile=None):
        if self.user is None:
            data = {'headImgFile': headImgFile, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'headImgFile': headImgFile}
        response = self.request.post(url=self.url+'/web/user/upload-headImg', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
