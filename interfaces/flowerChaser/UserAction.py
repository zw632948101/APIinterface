#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
import json


class UserAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('FC_USER')

    def set_user(self, mobile=None, account_type='user'):
        if mobile is None:
            self.user = None
        else:
            self.user = User(mobile, account_type)
            self.request.headers.update({"_Device-Id_": self.user.device_id})
            self.request.headers.update({"_Token_": self.user.token})
        return self.user

    def __judge_response_status(self, json_response):
        if json_response['status'] in ("OK", "ERROR"):
            return json_response
        else:
            raise Exception('status未返回OK或ERROR')

    def _admin_user_agr_add(self, account_=None, userName_=None):
        if self.user is None:
            data = {'account': account_, 'userName': userName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'account': account_, 'userName': userName_}
        response = self.request.post(url=self.url+'/admin/user/agr/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_user_agr_edit(self, id_=None, userName_=None):
        if self.user is None:
            data = {'id': id_, 'userName': userName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'userName': userName_}
        response = self.request.post(url=self.url+'/admin/user/agr/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_user_agr_page_list(self, pageSize_=None, pageNum_=None, userName_=None, status_=None, email_=None):
        if self.user is None:
            data = {'pageSize': pageSize_, 'pageNum': pageNum_, 'userName': userName_, 'status': status_, 'email': email_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pageSize': pageSize_, 'pageNum': pageNum_, 'userName': userName_, 'status': status_, 'email': email_}
        response = self.request.post(url=self.url+'/admin/user/agr/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_user_agr_reset_password(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/user/agr/reset-password', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_user_detail(self, userId_=None):
        if self.user is None:
            data = {'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_}
        response = self.request.post(url=self.url+'/admin/user/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_user_inner_list(self, pn_=None, ps_=None, status_=None, userName_=None, email_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'status': status_, 'userName': userName_, 'email': email_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'status': status_, 'userName': userName_, 'email': email_}
        response = self.request.post(url=self.url+'/admin/user/inner-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_user_user_list(self, pn_=None, ps_=None, status_=None, userName_=None, email_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'status': status_, 'userName': userName_, 'email': email_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'status': status_, 'userName': userName_, 'email': email_}
        response = self.request.post(url=self.url+'/admin/user/user-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_statistics_bee_friend_login_total(self, excludeUserIds_=None):
        if self.user is None:
            data = {'excludeUserIds': excludeUserIds_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'excludeUserIds': excludeUserIds_}
        response = self.request.post(url=self.url+'/api/user-statistics/bee-friend-login-total', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_statistics_bee_friend_register_total(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/user-statistics/bee-friend-register-total', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_third_change_weichat(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/user-third/change-weichat', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_third_get_by_openid(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/user-third/get-by-openid', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_third_login_or_register(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/user-third/login-or-register', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_add_user(self, userAddInput_=None):
        if self.user is None:
            data = {'userAddInput': userAddInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userAddInput': userAddInput_}
        response = self.request.post(url=self.url+'/api/user/add-user', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_auto_userinfo(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/user/auto-userinfo', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_get(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/user/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_get_by_email(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/user/get-by-email', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_get_by_mobile(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/user/get-by-mobile', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_list_account(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/user/list-account', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_list_ids(self, userIds_=None):
        if self.user is None:
            data = {'userIds': userIds_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userIds': userIds_}
        response = self.request.post(url=self.url+'/api/user/list-ids', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_login_check(self, loginInput_=None):
        if self.user is None:
            data = {'loginInput': loginInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'loginInput': loginInput_}
        response = self.request.post(url=self.url+'/api/user/login-check', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_login_with_register(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/user/login-with-register', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_page_list_account(self, userListInput_=None):
        if self.user is None:
            data = {'userListInput': userListInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userListInput': userListInput_}
        response = self.request.post(url=self.url+'/api/user/page-list-account', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_register(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/user/register', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_sorted_name_list(self, userIds_=None):
        if self.user is None:
            data = {'userIds': userIds_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userIds': userIds_}
        response = self.request.post(url=self.url+'/api/user/sorted-name-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_sorted_user_list(self, userIds_=None):
        if self.user is None:
            data = {'userIds': userIds_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userIds': userIds_}
        response = self.request.post(url=self.url+'/api/user/sorted-user-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_update_status(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/user/update-status', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_user_update_user(self, userUpdateInput_=None):
        if self.user is None:
            data = {'userUpdateInput': userUpdateInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userUpdateInput': userUpdateInput_}
        response = self.request.post(url=self.url+'/api/user/update-user', data=data, hosts=self.url)
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

    def _mobile_user_send_pass_email(self, email_=None):
        if self.user is None:
            data = {'email': email_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'email': email_}
        response = self.request.post(url=self.url+'/mobile/user/send-pass-email', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_send_update_email(self, email_=None):
        if self.user is None:
            data = {'email': email_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'email': email_}
        response = self.request.post(url=self.url+'/mobile/user/send-update-email', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_update(self, userName_=None, headImg_=None, region_=None, phone_=None, gender_=None, birthday_=None, introduce_=None, area_=None):
        if self.user is None:
            data = {'userName': userName_, 'headImg': headImg_, 'region': region_, 'phone': phone_, 'gender': gender_, 'birthday': birthday_, 'introduce': introduce_, 'area': area_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userName': userName_, 'headImg': headImg_, 'region': region_, 'phone': phone_, 'gender': gender_, 'birthday': birthday_, 'introduce': introduce_, 'area': area_}
        response = self.request.post(url=self.url+'/mobile/user/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_update_locale(self, locale_=None):
        if self.user is None:
            data = {'locale': locale_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'locale': locale_}
        response = self.request.post(url=self.url+'/mobile/user/update-locale', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_update_password(self, oldPassword_=None, newPassword_=None):
        if self.user is None:
            data = {'oldPassword': oldPassword_, 'newPassword': newPassword_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'oldPassword': oldPassword_, 'newPassword': newPassword_}
        response = self.request.post(url=self.url+'/mobile/user/update-password', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_upload_headImg(self, headImgFile_=None):
        if self.user is None:
            data = {'headImgFile': headImgFile_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'headImgFile': headImgFile_}
        response = self.request.post(url=self.url+'/mobile/user/upload-headImg', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_im_get_accid(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/im/get-accid', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_im_get_seller_accid(self, toUserId_=None):
        if self.user is None:
            data = {'toUserId': toUserId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'toUserId': toUserId_}
        response = self.request.post(url=self.url+'/web/im/get-seller-accid', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_detail(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/user/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_init_im_account(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/user/init-im-account', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_send_pass_email(self, email_=None):
        if self.user is None:
            data = {'email': email_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'email': email_}
        response = self.request.post(url=self.url+'/web/user/send-pass-email', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_send_update_email(self, email_=None):
        if self.user is None:
            data = {'email': email_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'email': email_}
        response = self.request.post(url=self.url+'/web/user/send-update-email', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_set_pass(self, password_=None, token_=None):
        if self.user is None:
            data = {'password': password_, 'token': token_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'password': password_, 'token': token_}
        response = self.request.post(url=self.url+'/web/user/set-pass', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_update(self, userName_=None, headImg_=None, region_=None, phone_=None, gender_=None, birthday_=None, introduce_=None, area_=None):
        if self.user is None:
            data = {'userName': userName_, 'headImg': headImg_, 'region': region_, 'phone': phone_, 'gender': gender_, 'birthday': birthday_, 'introduce': introduce_, 'area': area_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userName': userName_, 'headImg': headImg_, 'region': region_, 'phone': phone_, 'gender': gender_, 'birthday': birthday_, 'introduce': introduce_, 'area': area_}
        response = self.request.post(url=self.url+'/web/user/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_update_email(self, token_=None):
        if self.user is None:
            data = {'token': token_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'token': token_}
        response = self.request.post(url=self.url+'/web/user/update-email', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_update_password(self, oldPassword_=None, newPassword_=None):
        if self.user is None:
            data = {'oldPassword': oldPassword_, 'newPassword': newPassword_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'oldPassword': oldPassword_, 'newPassword': newPassword_}
        response = self.request.post(url=self.url+'/web/user/update-password', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_user_upload_headImg(self, headImgFile_=None):
        if self.user is None:
            data = {'headImgFile': headImgFile_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'headImgFile': headImgFile_}
        response = self.request.post(url=self.url+'/web/user/upload-headImg', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
