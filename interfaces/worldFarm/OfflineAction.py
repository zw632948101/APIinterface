#! /usr/bin/env python
# encoding: utf-8

from tools.Config import Config
from tools.Request import Request

import json

class OfflineAction(object):
    def __init__(self, offline):
        self.log = Log('Offline')
        self.request = Request()
        self.offline = offline
        self.request.headers['_Device-Id_'] = self.offline.device_id
        self.request.headers['_Token_'] = self.offline.token
        env = Config('config').data['run']
        hosts = Config('config').data['hosts'][env]
        self.url = hosts.get('WF_OFFLINE')

    def mobile_offline_search_condition_cattle(self):
        data = {'_tk_': self.offline.token, '_deviceId_': self.offline.device_id}
        response = self.request.post(url=self.url+'/mobile/offline-search-condition/cattle', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_offline_search_condition_cattle_position(self):
        data = {'_tk_': self.offline.token, '_deviceId_': self.offline.device_id}
        response = self.request.post(url=self.url+'/mobile/offline-search-condition/cattle-position', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_offline_upload_data(self, jsonParam=None):
        data = {'_tk_': self.offline.token, '_deviceId_': self.offline.device_id, 'jsonParam': jsonParam}
        response = self.request.post(url=self.url+'/mobile/offline-upload/data', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_offline_version_check(self, jsonParam=None):
        data = {'_tk_': self.offline.token, '_deviceId_': self.offline.device_id, 'jsonParam': jsonParam}
        response = self.request.post(url=self.url+'/mobile/offline-version/check', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_offline_camera(self, page=None):
        data = {'_tk_': self.offline.token, '_deviceId_': self.offline.device_id, 'page': page}
        response = self.request.post(url=self.url+'/mobile/offline/camera', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_offline_cattle(self, page=None):
        data = {'_tk_': self.offline.token, '_deviceId_': self.offline.device_id, 'page': page}
        response = self.request.post(url=self.url+'/mobile/offline/cattle', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_offline_cattle_position(self, page=None):
        data = {'_tk_': self.offline.token, '_deviceId_': self.offline.device_id, 'page': page}
        response = self.request.post(url=self.url+'/mobile/offline/cattle-position', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_offline_farm(self, page=None):
        data = {'_tk_': self.offline.token, '_deviceId_': self.offline.device_id, 'page': page}
        response = self.request.post(url=self.url+'/mobile/offline/farm', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_offline_farm_region(self, page=None):
        data = {'_tk_': self.offline.token, '_deviceId_': self.offline.device_id, 'page': page}
        response = self.request.post(url=self.url+'/mobile/offline/farm-region', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_offline_farm_signal(self, page=None):
        data = {'_tk_': self.offline.token, '_deviceId_': self.offline.device_id, 'page': page}
        response = self.request.post(url=self.url+'/mobile/offline/farm-signal', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_offline_farm_user(self, page=None):
        data = {'_tk_': self.offline.token, '_deviceId_': self.offline.device_id, 'page': page}
        response = self.request.post(url=self.url+'/mobile/offline/farm-user', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_offline_get_bind_signal_device(self, page=None):
        data = {'_tk_': self.offline.token, '_deviceId_': self.offline.device_id, 'page': page}
        response = self.request.post(url=self.url+'/mobile/offline/get-bind-signal-device', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def mobile_offline_landmark(self, page=None):
        data = {'_tk_': self.offline.token, '_deviceId_': self.offline.device_id, 'page': page}
        response = self.request.post(url=self.url+'/mobile/offline/landmark', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def v126_mobile_offline_cattle(self, page=None):
        data = {'_tk_': self.offline.token, '_deviceId_': self.offline.device_id, 'page': page}
        response = self.request.post(url=self.url+'/v1.2.6/mobile/offline/cattle', data=data, hosts=self.url)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")
