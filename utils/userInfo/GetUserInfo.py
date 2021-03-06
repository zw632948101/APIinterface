#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.databaseConnection.DataBaseOperate import DataBaseOperate
import json


class DBUserInfo(object):
    host_ip = config.get('database').get(config.get('run')).get('host_ip')

    def mgr_query_user_info_by_account(self, account):
        sql = """
                SELECT tu.phone,
                       tu.username,
                       tk.*,
                       tu.is_delete
                FROM `world-user`.t_user tu
                         LEFT JOIN (SELECT user_id, device_id, token, create_time
                                    FROM `world-passport`.t_login_token tlt
                                    WHERE is_delete = 0) AS tk ON tu.id = tk.user_id
                WHERE (tu.phone = '%s' or tu.email = '%s')
                  AND tu.is_delete = 0
                ORDER BY create_time DESC
                LIMIT 1;
                        """ % (account, account)
        user_info = DataBaseOperate().operate(self.host_ip, sql)
        return user_info


class SessionTool(object):
    host_ip = config.get('hosts').get(config.get('run'))

    def __init__(self):
        pass

    def get_user_session(self, mobile, account_type='user', **kwargs):
        """
        追花族-邮箱密码登录
        :param：account 邮箱
        :param: account_type 密码
        :param: password 密码
        :param: wxcode 微信临时授权code，可以直接使用数据已绑定的微信openid
        :return:
        """
        data = {"appId": "FLOWER_CHASERS",
                "deviceType": "ANDROID",
                "deviceId": "cc4feebe419791332bbcff5e0fdf084a",
                "mobile": mobile,
                "verifyCode": 8888}
        host = config.get('loginhosts').get(config.get('run')).get('PASSPORT')
        if account_type == 'user':
            session = Request().post(url=host + "/mobile/sso/sms-login",
                                     data=data)
        elif account_type == 'employee':
            session = Request().post(url=host + "/admin/sso/email-login",
                                     data=data)
        elif account_type == 'web-mp':
            data['deviceType'] = 'WEB'
            session = Request().post(url=host + "/admin/sso/sms-login",
                                     data=data)
        elif account_type == 'wf_account':
            datas = {'appId': 'WORLD_FARM', 'deviceType': 'IOS', 'deviceId': 'qaTeam',
                     'account': mobile,
                     'password': kwargs['password']}
            session = Request().post(url=host + "/mobile/sso/email-login", data=datas)
        elif account_type == 'wxshop':
            data.update(kwargs)
            session = Request().post(url=host + "/web/sso/mall-login-wx",
                                     data=data)
        else:
            raise Exception("account_type非法, 仅支持user/employee")
        if account_type in ('web-mp') and json.loads(session).get('status') == 'OK':
            headers = Request.headers.copy()
            headers['_Device-Id_'] = json.loads(session)['content']['deviceId']
            headers['_Token_'] = json.loads(session)['content']['token']
            host = host.replace('world-passport', 'fc-bee')
            resp = Request().post(url=host + '/admin/fc-user/permission-check', headers=headers)
            if json.loads(resp).get('status') == 'ERROR':
                session = resp
        return session


class UserSession(object):
    def __init__(self, mobile, account_type='user', **kwargs):
        session = SessionTool().get_user_session(mobile, account_type, **kwargs)
        session_json = json.loads(session)
        if session_json.get('status') == 'OK':
            self.deviceId = str(session_json["content"]["deviceId"])
            self.encryptedPwd = str(session_json["content"]["encryptedPwd"])
            self.token = str(session_json["content"]["token"])
            self.userId = str(session_json["content"]["bizId"])
        if session_json.get('status') == 'ERROR':
            self.errorMsg = session_json.get("message")


class User(object):
    host_ip = config.get('hosts').get(config.get('run'))

    def __init__(self, mobile, account_type='user', **kwargs):
        self.db_user_info = DBUserInfo()
        self.request = Request()
        us = UserSession(mobile, account_type, **kwargs)
        self.token = us.token
        self.phone = mobile
        self.email = mobile
        self.user_id = us.userId
        self.device_id = us.deviceId
        # self.user_info = self.db_user_info.mgr_query_user_info_by_account(mobile)
        # if self.user_info != ():
        #     self.user_info = self.user_info[0]
        #     self.user_id = self.user_info["user_id"]
        #     self.phone = self.user_info["phone"]
        #     self.username = self.user_info["username"]
        #     self.create_time = self.user_info["create_time"]
        #     self.device_id = self.user_info["device_id"]
        #     self.is_delete = self.user_info["is_delete"]
