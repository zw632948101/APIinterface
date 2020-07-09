# encoding: utf_8

from tools.Config import Config
from tools.Request import Request

import json

class MgrAction(object):

    def __init__(self, mgr):
        self.log = Log('Mgr')
        self.request = Request()
        self.mgr = mgr
        self.request.headers['_Device_Id_'] = self.mgr.device_id
        self.request.headers['_Token_'] = self.mgr.token
        env = Config('config').data['run']
        hosts = Config('config').data['hosts'][env]
        self.url = hosts.get('WF_MGR')

    def admin_account_add(self, Authentication_Token=None, account=None, userName=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'account': account, 'userName': userName}
        response = self.request.post(url=self.url+'/admin/account/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_account_edit(self, Authentication_Token=None, id=None, userName=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id, 'userName': userName}
        response = self.request.post(url=self.url+'/admin/account/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_account_freeze(self, Authentication_Token=None, id=None, status=None, reason=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id, 'status': status, 'reason': reason}
        response = self.request.post(url=self.url+'/admin/account/freeze', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_account_login(self, Authentication_Token=None, userName=None, password=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'userName': userName, 'password': password}
        response = self.request.post(url=self.url+'/admin/account/login', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_account_pagelist(self, Authentication_Token=None, pageSize=None, pageNum=None, userName=None, status=None, email=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'userName': userName, 'status': status, 'email': email}
        response = self.request.post(url=self.url+'/admin/account/pagelist', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_account_reset_password(self, Authentication_Token=None, id=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id}
        response = self.request.post(url=self.url+'/admin/account/reset_password', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_camera_add(self, Authentication_Token=None, serialNo=None, platformId=None, name=None, verificationCode=None, gatewayId=None, subPowerNo=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'serialNo': serialNo, 'platformId': platformId, 'name': name, 'verificationCode': verificationCode, 'gatewayId': gatewayId, 'subPowerNo': subPowerNo}
        response = self.request.post(url=self.url+'/admin/camera/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_camera_detail(self, Authentication_Token=None, serialNo=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'serialNo': serialNo}
        response = self.request.post(url=self.url+'/admin/camera/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_camera_encrypt(self, Authentication_Token=None, cameraId=None, encryptStatus=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'cameraId': cameraId, 'encryptStatus': encryptStatus}
        response = self.request.post(url=self.url+'/admin/camera/encrypt', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_camera_get_by_gateway_no(self, Authentication_Token=None, gatewayNo=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayNo': gatewayNo}
        response = self.request.post(url=self.url+'/admin/camera/get_by_gateway_no', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_camera_get_live_url(self, Authentication_Token=None, cameraId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'cameraId': cameraId}
        response = self.request.post(url=self.url+'/admin/camera/get_live_url', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_camera_page_list(self, Authentication_Token=None, pageSize=None, pageNum=None, name=None, platformId=None, serialNo=None, customerId=None, customerName=None, status=None, customerBeNull=None, queryType=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'name': name, 'platformId': platformId, 'serialNo': serialNo, 'customerId': customerId, 'customerName': customerName, 'status': status, 'customerBeNull': customerBeNull, 'queryType': queryType}
        response = self.request.post(url=self.url+'/admin/camera/page_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_camera_update(self, Authentication_Token=None, serialNo=None, platformId=None, name=None, gatewayId=None, subPowerNo=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'serialNo': serialNo, 'platformId': platformId, 'name': name, 'gatewayId': gatewayId, 'subPowerNo': subPowerNo}
        response = self.request.post(url=self.url+'/admin/camera/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_customer_add(self, Authentication_Token=None, name=None, description=None, type=None, address=None, contacts=None, contactNumber=None, email=None, surveyAccessory=None, planAccessory=None, solutionAccessory=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'name': name, 'description': description, 'type': type, 'address': address, 'contacts': contacts, 'contactNumber': contactNumber, 'email': email, 'surveyAccessory': surveyAccessory, 'planAccessory': planAccessory, 'solutionAccessory': solutionAccessory}
        response = self.request.post(url=self.url+'/admin/customer/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_customer_bind_pd(self, Authentication_Token=None, dataIds=None, customerId=None, firstLevelType=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'dataIds': dataIds, 'customerId': customerId, 'firstLevelType': firstLevelType}
        response = self.request.post(url=self.url+'/admin/customer/bind_pd', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_customer_detail(self, Authentication_Token=None, customerId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'customerId': customerId}
        response = self.request.post(url=self.url+'/admin/customer/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_customer_edit(self, Authentication_Token=None, id=None, name=None, description=None, type=None, address=None, contacts=None, contactNumber=None, email=None, surveyAccessory=None, planAccessory=None, solutionAccessory=None, bizType=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id, 'name': name, 'description': description, 'type': type, 'address': address, 'contacts': contacts, 'contactNumber': contactNumber, 'email': email, 'surveyAccessory': surveyAccessory, 'planAccessory': planAccessory, 'solutionAccessory': solutionAccessory, 'bizType': bizType}
        response = self.request.post(url=self.url+'/admin/customer/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_customer_page_list(self, Authentication_Token=None, pageSize=None, pageNum=None, name=None, type=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'name': name, 'type': type}
        response = self.request.post(url=self.url+'/admin/customer/page_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_customer_product_catogry(self, Authentication_Token=None, customerId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'customerId': customerId}
        response = self.request.post(url=self.url+'/admin/customer/product_catogry', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_customer_unbinding(self, Authentication_Token=None, deviceId=None, customerId=None, firstLevelType=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceId': deviceId, 'customerId': customerId, 'firstLevelType': firstLevelType}
        response = self.request.post(url=self.url+'/admin/customer/unbinding', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_customer_warning_count(self, Authentication_Token=None, customerId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'customerId': customerId}
        response = self.request.post(url=self.url+'/admin/customer/warning_count', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_batch_add(self, Authentication_Token=None, batchNo=None, platformId=None, productId=None, bluetoothFirmwareId=None, loraFirmwareId=None, fullFirmwareId=None, batchDesc=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'batchNo': batchNo, 'platformId': platformId, 'productId': productId, 'bluetoothFirmwareId': bluetoothFirmwareId, 'loraFirmwareId': loraFirmwareId, 'fullFirmwareId': fullFirmwareId, 'batchDesc': batchDesc}
        response = self.request.post(url=self.url+'/admin/device_batch/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_batch_add_device(self, Authentication_Token=None, batchId=None, deviceNum=None, startedEui=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'batchId': batchId, 'deviceNum': deviceNum, 'startedEui': startedEui}
        response = self.request.post(url=self.url+'/admin/device_batch/add_device', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_batch_detail(self, Authentication_Token=None, id=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id}
        response = self.request.post(url=self.url+'/admin/device_batch/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_batch_edit(self, Authentication_Token=None, batchId=None, batchNo=None, batchDesc=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'batchId': batchId, 'batchNo': batchNo, 'batchDesc': batchDesc}
        response = self.request.post(url=self.url+'/admin/device_batch/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_batch_list(self, Authentication_Token=None, batchId=None, productId=None, batchNo=None, firstLevelType=None, secondLevelType=None, loraFirmwareId=None, bluetoothFirmwareId=None, fullFirmwareId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'batchId': batchId, 'productId': productId, 'batchNo': batchNo, 'firstLevelType': firstLevelType, 'secondLevelType': secondLevelType, 'loraFirmwareId': loraFirmwareId, 'bluetoothFirmwareId': bluetoothFirmwareId, 'fullFirmwareId': fullFirmwareId}
        response = self.request.post(url=self.url+'/admin/device_batch/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_batch_page_list(self, Authentication_Token=None, pageSize=None, pageNum=None, batchId=None, productId=None, batchNo=None, firstLevelType=None, secondLevelType=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'batchId': batchId, 'productId': productId, 'batchNo': batchNo, 'firstLevelType': firstLevelType, 'secondLevelType': secondLevelType}
        response = self.request.post(url=self.url+'/admin/device_batch/page_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_log_list(self, Authentication_Token=None, pageSize=None, pageNum=None, deviceEui=None, startTime=None, endTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'deviceEui': deviceEui, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.url+'/admin/device_log/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_reports_list(self, Authentication_Token=None, pageSize=None, pageNum=None, deviceEui=None, productTypeId=None, productId=None, firmwareId=None, customerName=None, period=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'deviceEui': deviceEui, 'productTypeId': productTypeId, 'productId': productId, 'firmwareId': firmwareId, 'customerName': customerName, 'period': period}
        response = self.request.post(url=self.url+'/admin/device_reports/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_add(self, Authentication_Token=None, startDevEui=None, endDevEui=None, productId=None, platformId=None, batchId=None, isTest=None, loraFirmwareId=None, bluetoothFirmwareId=None, remark=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'startDevEui': startDevEui, 'endDevEui': endDevEui, 'productId': productId, 'platformId': platformId, 'batchId': batchId, 'isTest': isTest, 'loraFirmwareId': loraFirmwareId, 'bluetoothFirmwareId': bluetoothFirmwareId, 'remark': remark}
        response = self.request.post(url=self.url+'/admin/device/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_data_situation(self, Authentication_Token=None, deviceEui=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url+'/admin/device/data_situation', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_detail(self, Authentication_Token=None, deviceEui=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url+'/admin/device/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_electricity_records(self, Authentication_Token=None, deviceEui=None, startTime=None, endTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.url+'/admin/device/electricity_records', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_enable(self, Authentication_Token=None, deviceEui=None, enable=None, mark=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui, 'enable': enable, 'mark': mark}
        response = self.request.post(url=self.url+'/admin/device/enable', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_last_all_position(self, Authentication_Token=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token}
        response = self.request.post(url=self.url+'/admin/device/last_all_position', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_last_position(self, Authentication_Token=None, deviceEui=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url+'/admin/device/last_position', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_list(self, Authentication_Token=None, pageSize=None, pageNum=None, deviceEui=None, productTypeId=None, productId=None, batchId=None, deviceStatus=None, firmwareId=None, customerId=None, bindStatus=None, queryType=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'deviceEui': deviceEui, 'productTypeId': productTypeId, 'productId': productId, 'batchId': batchId, 'deviceStatus': deviceStatus, 'firmwareId': firmwareId, 'customerId': customerId, 'bindStatus': bindStatus, 'queryType': queryType}
        response = self.request.post(url=self.url+'/admin/device/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_location_factors_statistics(self, Authentication_Token=None, deviceEui=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url+'/admin/device/location_factors_statistics', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_location_statistics(self, Authentication_Token=None, deviceEui=None, startTime=None, endTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.url+'/admin/device/location_statistics', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_mark(self, Authentication_Token=None, deviceEui=None, isTest=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui, 'isTest': isTest}
        response = self.request.post(url=self.url+'/admin/device/mark', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_motion_by_page(self, Authentication_Token=None, pageSize=None, pageNum=None, deviceEui=None, startTime=None, endTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'deviceEui': deviceEui, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.url+'/admin/device/motion_by_page', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_motion_records(self, Authentication_Token=None, deviceEui=None, startTime=None, endTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.url+'/admin/device/motion_records', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_position_Statistics(self, Authentication_Token=None, deviceEui=None, startTime=None, endTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.url+'/admin/device/position_Statistics', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_position_page_list(self, Authentication_Token=None, pageSize=None, pageNum=None, deviceEui=None, startTime=None, endTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'deviceEui': deviceEui, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.url+'/admin/device/position_page_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_position_records(self, Authentication_Token=None, deviceEui=None, startTime=None, endTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.url+'/admin/device/position_records', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_power(self, Authentication_Token=None, deviceEui=None, startTime=None, endTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.url+'/admin/device/power', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_set_fixed_frequency(self, Authentication_Token=None, devEuis=None, dayInterval=None, nightInterval=None, useDefault=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'devEuis': devEuis, 'dayInterval': dayInterval, 'nightInterval': nightInterval, 'useDefault': useDefault}
        response = self.request.post(url=self.url+'/admin/device/set_fixed_frequency', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_set_temp_frequency(self, Authentication_Token=None, devEuis=None, interval=None, duration=None, useDefault=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'devEuis': devEuis, 'interval': interval, 'duration': duration, 'useDefault': useDefault}
        response = self.request.post(url=self.url+'/admin/device/set_temp_frequency', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_update(self, Authentication_Token=None, deviceEui=None, deviceName=None, remark=None, platformId=None, isTest=None, batchNo=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui, 'deviceName': deviceName, 'remark': remark, 'platformId': platformId, 'isTest': isTest, 'batchNo': batchNo}
        response = self.request.post(url=self.url+'/admin/device/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_device_update_remark(self, Authentication_Token=None, id=None, remark=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id, 'remark': remark}
        response = self.request.post(url=self.url+'/admin/device/update_remark', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_excel_device_export(self, Authentication_Token=None, pageSize=None, pageNum=None, deviceEui=None, productTypeId=None, productId=None, batchId=None, deviceStatus=None, firmwareId=None, customerId=None, bindStatus=None, queryType=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'deviceEui': deviceEui, 'productTypeId': productTypeId, 'productId': productId, 'batchId': batchId, 'deviceStatus': deviceStatus, 'firmwareId': firmwareId, 'customerId': customerId, 'bindStatus': bindStatus, 'queryType': queryType}
        response = self.request.post(url=self.url+'/admin/excel/device_export', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_excel_device_reports_export(self, Authentication_Token=None, pageSize=None, pageNum=None, deviceEui=None, productTypeId=None, productId=None, firmwareId=None, customerName=None, period=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'deviceEui': deviceEui, 'productTypeId': productTypeId, 'productId': productId, 'firmwareId': firmwareId, 'customerName': customerName, 'period': period}
        response = self.request.post(url=self.url+'/admin/excel/device_reports_export', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_excel_gateway_export(self, Authentication_Token=None, pageSize=None, pageNum=None, gatewayNo=None, productTypeId=None, productId=None, firmwareId=None, gatewayStatus=None, batchId=None, customerId=None, queryType=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'gatewayNo': gatewayNo, 'productTypeId': productTypeId, 'productId': productId, 'firmwareId': firmwareId, 'gatewayStatus': gatewayStatus, 'batchId': batchId, 'customerId': customerId, 'queryType': queryType}
        response = self.request.post(url=self.url+'/admin/excel/gateway_export', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_excel_gateway_reports_export(self, Authentication_Token=None, pageSize=None, pageNum=None, gatewayNo=None, productTypeId=None, productId=None, firmwareId=None, customerName=None, period=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'gatewayNo': gatewayNo, 'productTypeId': productTypeId, 'productId': productId, 'firmwareId': firmwareId, 'customerName': customerName, 'period': period}
        response = self.request.post(url=self.url+'/admin/excel/gateway_reports_export', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_file_upload(self, Authentication_Token=None, file=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'file': file}
        response = self.request.post(url=self.url+'/admin/file/upload', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_file_upload_private(self, Authentication_Token=None, file=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'file': file}
        response = self.request.post(url=self.url+'/admin/file/upload_private', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_file_upload_validate_md5(self, Authentication_Token=None, file=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'file': file}
        response = self.request.post(url=self.url+'/admin/file/upload_validate_md5', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_firmware_adaptation_delete(self, Authentication_Token=None, firmwareAdaptationId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'firmwareAdaptationId': firmwareAdaptationId}
        response = self.request.post(url=self.url+'/admin/firmware_adaptation/delete', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_firmware_add(self, Authentication_Token=None, productTypeId=None, productId=None, packageType=None, firmwareVersionCode=None, firmwareVersion=None, isInitialVersion=None, packageName=None, packageUrl=None, packageMd5=None, firmwareDesc=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'productTypeId': productTypeId, 'productId': productId, 'packageType': packageType, 'firmwareVersionCode': firmwareVersionCode, 'firmwareVersion': firmwareVersion, 'isInitialVersion': isInitialVersion, 'packageName': packageName, 'packageUrl': packageUrl, 'packageMd5': packageMd5, 'firmwareDesc': firmwareDesc}
        response = self.request.post(url=self.url+'/admin/firmware/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_firmware_detail(self, Authentication_Token=None, id=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id}
        response = self.request.post(url=self.url+'/admin/firmware/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_firmware_edit(self, Authentication_Token=None, id=None, firmwareVersion=None, packageName=None, packageUrl=None, packageMd5=None, firmwareDesc=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id, 'firmwareVersion': firmwareVersion, 'packageName': packageName, 'packageUrl': packageUrl, 'packageMd5': packageMd5, 'firmwareDesc': firmwareDesc}
        response = self.request.post(url=self.url+'/admin/firmware/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_firmware_eligible_device(self, Authentication_Token=None, firmwareId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'firmwareId': firmwareId}
        response = self.request.post(url=self.url+'/admin/firmware/eligible_device', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_firmware_firmware_type_list(self, Authentication_Token=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token}
        response = self.request.post(url=self.url+'/admin/firmware/firmware_type_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_firmware_higher_option_list(self, Authentication_Token=None, firmwareId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'firmwareId': firmwareId}
        response = self.request.post(url=self.url+'/admin/firmware/higher_option_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_firmware_list(self, Authentication_Token=None, productTypeId=None, productId=None, packageType=None, validateStatus=None, isInitialVersion=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'productTypeId': productTypeId, 'productId': productId, 'packageType': packageType, 'validateStatus': validateStatus, 'isInitialVersion': isInitialVersion}
        response = self.request.post(url=self.url+'/admin/firmware/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_firmware_list_by_type(self, Authentication_Token=None, firmwareId=None, productId=None, packageType=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'firmwareId': firmwareId, 'productId': productId, 'packageType': packageType}
        response = self.request.post(url=self.url+'/admin/firmware/list_by_type', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_firmware_lower_option_list(self, Authentication_Token=None, firmwareId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'firmwareId': firmwareId}
        response = self.request.post(url=self.url+'/admin/firmware/lower_option_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_firmware_option_list(self, Authentication_Token=None, productId=None, packageType=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'productId': productId, 'packageType': packageType}
        response = self.request.post(url=self.url+'/admin/firmware/option_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_firmware_page_list(self, Authentication_Token=None, pageSize=None, pageNum=None, productTypePId=None, productTypeId=None, productVersionName=None, firmwareVersion=None, packageType=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'productTypePId': productTypePId, 'productTypeId': productTypeId, 'productVersionName': productVersionName, 'firmwareVersion': firmwareVersion, 'packageType': packageType}
        response = self.request.post(url=self.url+'/admin/firmware/page_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_firmware_test_devices(self, Authentication_Token=None, id=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id}
        response = self.request.post(url=self.url+'/admin/firmware/test_devices', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_firmware_upgrade_list(self, Authentication_Token=None, pageSize=None, pageNum=None, upgradeStatus=None, strategyStatus=None, firmwareId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'upgradeStatus': upgradeStatus, 'strategyStatus': strategyStatus, 'firmwareId': firmwareId}
        response = self.request.post(url=self.url+'/admin/firmware/upgrade_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_firmware_validate(self, Authentication_Token=None, firmwareId=None, devices=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'firmwareId': firmwareId, 'devices': devices}
        response = self.request.post(url=self.url+'/admin/firmware/validate', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_firmware_version_code_generate(self, Authentication_Token=None, productId=None, packageType=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'productId': productId, 'packageType': packageType}
        response = self.request.post(url=self.url+'/admin/firmware/version_code_generate', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_reports_list(self, Authentication_Token=None, pageSize=None, pageNum=None, gatewayNo=None, productTypeId=None, productId=None, firmwareId=None, customerName=None, period=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'gatewayNo': gatewayNo, 'productTypeId': productTypeId, 'productId': productId, 'firmwareId': firmwareId, 'customerName': customerName, 'period': period}
        response = self.request.post(url=self.url+'/admin/gateway_reports/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_sub_power_list(self, Authentication_Token=None, gatewayNo=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayNo': gatewayNo}
        response = self.request.post(url=self.url+'/admin/gateway_sub_power/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_sub_power_option_list(self, Authentication_Token=None, gatewayId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId}
        response = self.request.post(url=self.url+'/admin/gateway_sub_power/option_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_bind(self, Authentication_Token=None, deviceTypeId=None, deviceId=None, gatewayId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceTypeId': deviceTypeId, 'deviceId': deviceId, 'gatewayId': gatewayId}
        response = self.request.post(url=self.url+'/admin/gateway/bind', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_bind_sim(self, Authentication_Token=None, gatewayId=None, simId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId, 'simId': simId}
        response = self.request.post(url=self.url+'/admin/gateway/bind_sim', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_bind_sub_power(self, Authentication_Token=None, gatewayId=None, deviceTypeId=None, deviceId=None, subPowerNo=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId, 'deviceTypeId': deviceTypeId, 'deviceId': deviceId, 'subPowerNo': subPowerNo}
        response = self.request.post(url=self.url+'/admin/gateway/bind_sub_power', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_check_upgrade(self, Authentication_Token=None, gatewayId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId}
        response = self.request.post(url=self.url+'/admin/gateway/check_upgrade', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_detail(self, Authentication_Token=None, gatewayNo=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayNo': gatewayNo}
        response = self.request.post(url=self.url+'/admin/gateway/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_electricity_list(self, Authentication_Token=None, deviceEui=None, startTime=None, endTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.url+'/admin/gateway/electricity_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_get_bind_device(self, Authentication_Token=None, gatewayId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId}
        response = self.request.post(url=self.url+'/admin/gateway/get_bind_device', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_get_bind_type(self, Authentication_Token=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token}
        response = self.request.post(url=self.url+'/admin/gateway/get_bind_type', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_get_bound_sim(self, Authentication_Token=None, gatewayId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId}
        response = self.request.post(url=self.url+'/admin/gateway/get_bound_sim', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_get_not_bind_device_list(self, Authentication_Token=None, deviceTypeId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceTypeId': deviceTypeId}
        response = self.request.post(url=self.url+'/admin/gateway/get_not_bind_device_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_get_not_bind_sub_power_device(self, Authentication_Token=None, gatewayId=None, deviceTypeId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId, 'deviceTypeId': deviceTypeId}
        response = self.request.post(url=self.url+'/admin/gateway/get_not_bind_sub_power_device', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_get_not_bound_sim_list(self, Authentication_Token=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token}
        response = self.request.post(url=self.url+'/admin/gateway/get_not_bound_sim_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_get_sub_power(self, Authentication_Token=None, gatewayId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId}
        response = self.request.post(url=self.url+'/admin/gateway/get_sub_power', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_get_sub_power_bind_type(self, Authentication_Token=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token}
        response = self.request.post(url=self.url+'/admin/gateway/get_sub_power_bind_type', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_humidity_list(self, Authentication_Token=None, deviceEui=None, startTime=None, endTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.url+'/admin/gateway/humidity_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_id_list(self, Authentication_Token=None, bindType=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'bindType': bindType}
        response = self.request.post(url=self.url+'/admin/gateway/id_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_lora_update(self, Authentication_Token=None, gatewayId=None, loraAddr=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId, 'loraAddr': loraAddr}
        response = self.request.post(url=self.url+'/admin/gateway/lora_update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_mark_status_update(self, Authentication_Token=None, gatewayId=None, markStatus=None, remark=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId, 'markStatus': markStatus, 'remark': remark}
        response = self.request.post(url=self.url+'/admin/gateway/mark_status_update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_option_list(self, Authentication_Token=None, platformId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'platformId': platformId}
        response = self.request.post(url=self.url+'/admin/gateway/option_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_page_list(self, Authentication_Token=None, pageSize=None, pageNum=None, gatewayNo=None, productTypeId=None, productId=None, firmwareId=None, gatewayStatus=None, batchId=None, customerId=None, queryType=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'gatewayNo': gatewayNo, 'productTypeId': productTypeId, 'productId': productId, 'firmwareId': firmwareId, 'gatewayStatus': gatewayStatus, 'batchId': batchId, 'customerId': customerId, 'queryType': queryType}
        response = self.request.post(url=self.url+'/admin/gateway/page_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_reboot(self, Authentication_Token=None, gatewayId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId}
        response = self.request.post(url=self.url+'/admin/gateway/reboot', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_save(self, Authentication_Token=None, gatewayNo=None, platformId=None, productTypeId=None, productId=None, firmwareId=None, batchId=None, isTest=None, remark=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayNo': gatewayNo, 'platformId': platformId, 'productTypeId': productTypeId, 'productId': productId, 'firmwareId': firmwareId, 'batchId': batchId, 'isTest': isTest, 'remark': remark}
        response = self.request.post(url=self.url+'/admin/gateway/save', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_software_upgrade(self, Authentication_Token=None, gatewayId=None, firmwareId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId, 'firmwareId': firmwareId}
        response = self.request.post(url=self.url+'/admin/gateway/software_upgrade', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_software_upgrade_batch(self, Authentication_Token=None, gatewayIds=None, firmwareId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayIds': gatewayIds, 'firmwareId': firmwareId}
        response = self.request.post(url=self.url+'/admin/gateway/software_upgrade_batch', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_status_detail(self, Authentication_Token=None, gatewayId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId}
        response = self.request.post(url=self.url+'/admin/gateway/status_detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_strike_switch(self, Authentication_Token=None, gatewayId=None, strikeSwitch=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId, 'strikeSwitch': strikeSwitch}
        response = self.request.post(url=self.url+'/admin/gateway/strike_switch', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_sub_power_switch(self, Authentication_Token=None, gatewayId=None, subPowerNo=None, subPowerSwitch=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId, 'subPowerNo': subPowerNo, 'subPowerSwitch': subPowerSwitch}
        response = self.request.post(url=self.url+'/admin/gateway/sub_power_switch', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_sub_power_switch_timer(self, Authentication_Token=None, openDay=None, gatewayId=None, subPowerNo=None, openTime=None, closeTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'openDay': openDay, 'gatewayId': gatewayId, 'subPowerNo': subPowerNo, 'openTime': openTime, 'closeTime': closeTime}
        response = self.request.post(url=self.url+'/admin/gateway/sub_power_switch_timer', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_temperature_list(self, Authentication_Token=None, deviceEui=None, startTime=None, endTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.url+'/admin/gateway/temperature_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_unbind(self, Authentication_Token=None, gatewayId=None, deviceTypeId=None, deviceId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId, 'deviceTypeId': deviceTypeId, 'deviceId': deviceId}
        response = self.request.post(url=self.url+'/admin/gateway/unbind', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_unbind_sim(self, Authentication_Token=None, simId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'simId': simId}
        response = self.request.post(url=self.url+'/admin/gateway/unbind_sim', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_unbind_sub_power(self, Authentication_Token=None, gatewayId=None, deviceTypeId=None, deviceId=None, subPowerNo=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId, 'deviceTypeId': deviceTypeId, 'deviceId': deviceId, 'subPowerNo': subPowerNo}
        response = self.request.post(url=self.url+'/admin/gateway/unbind_sub_power', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_update(self, Authentication_Token=None, id=None, installLng=None, installLat=None, isTest=None, remark=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id, 'installLng': installLng, 'installLat': installLat, 'isTest': isTest, 'remark': remark}
        response = self.request.post(url=self.url+'/admin/gateway/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_update_remark(self, Authentication_Token=None, id=None, remark=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id, 'remark': remark}
        response = self.request.post(url=self.url+'/admin/gateway/update_remark', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_gateway_wifi_switch(self, Authentication_Token=None, gatewayId=None, wifiName=None, wifiSwitch=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayId': gatewayId, 'wifiName': wifiName, 'wifiSwitch': wifiSwitch}
        response = self.request.post(url=self.url+'/admin/gateway/wifi_switch', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_home_device_count(self, Authentication_Token=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token}
        response = self.request.post(url=self.url+'/admin/home/device_count', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_home_device_data(self, Authentication_Token=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token}
        response = self.request.post(url=self.url+'/admin/home/device_data', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_home_device_statics(self, Authentication_Token=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token}
        response = self.request.post(url=self.url+'/admin/home/device_statics', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_monitor_change_model(self, Authentication_Token=None, devEui=None, workModel=None, duration=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'devEui': devEui, 'workModel': workModel, 'duration': duration}
        response = self.request.post(url=self.url+'/admin/monitor/change_model', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_monitor_report_frequency(self, Authentication_Token=None, devEui=None, frequency=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'devEui': devEui, 'frequency': frequency}
        response = self.request.post(url=self.url+'/admin/monitor/report_frequency', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_monitor_send_control(self, Authentication_Token=None, devEui=None, cmdparams=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'devEui': devEui, 'cmdparams': cmdparams}
        response = self.request.post(url=self.url+'/admin/monitor/send_control', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_offline_strategy_detail(self, Authentication_Token=None, id=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id}
        response = self.request.post(url=self.url+'/admin/offline_strategy/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_offline_strategy_device_type_option(self, Authentication_Token=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token}
        response = self.request.post(url=self.url+'/admin/offline_strategy/device_type_option', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_offline_strategy_page_list(self, Authentication_Token=None, pageSize=None, pageNum=None, deviceType=None, status=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'deviceType': deviceType, 'status': status}
        response = self.request.post(url=self.url+'/admin/offline_strategy/page_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_offline_strategy_save(self, Authentication_Token=None, deviceType=None, rules=None, status=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceType': deviceType, 'rules': rules, 'status': status}
        response = self.request.post(url=self.url+'/admin/offline_strategy/save', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_offline_strategy_update(self, Authentication_Token=None, id=None, rules=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id, 'rules': rules}
        response = self.request.post(url=self.url+'/admin/offline_strategy/update', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_offline_strategy_update_status(self, Authentication_Token=None, id=None, status=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id, 'status': status}
        response = self.request.post(url=self.url+'/admin/offline_strategy/update_status', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_platform_add(self, Authentication_Token=None, name=None, callbackUrl=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'name': name, 'callbackUrl': callbackUrl}
        response = self.request.post(url=self.url+'/admin/platform/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_platform_list(self, Authentication_Token=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token}
        response = self.request.post(url=self.url+'/admin/platform/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_product_type_edit(self, Authentication_Token=None, id=None, name=None, status=None, desc=None, terminalProtocol=None, gatewayProtocol=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id, 'name': name, 'status': status, 'desc': desc, 'terminalProtocol': terminalProtocol, 'gatewayProtocol': gatewayProtocol}
        response = self.request.post(url=self.url+'/admin/product_type/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_product_type_list(self, Authentication_Token=None, name=None, status=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'name': name, 'status': status}
        response = self.request.post(url=self.url+'/admin/product_type/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_product_type_list_by_pid(self, Authentication_Token=None, pid=None, status=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pid': pid, 'status': status}
        response = self.request.post(url=self.url+'/admin/product_type/list_by_pid', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_product_add(self, Authentication_Token=None, secondLevelType=None, productVersionCode=None, productVersion=None, versionDesc=None, hardwareVersionCode=None, hardwareVersion=None, hardwareVersionDesc=None, structureDocUrl=None, structureDesignUrl=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'secondLevelType': secondLevelType, 'productVersionCode': productVersionCode, 'productVersion': productVersion, 'versionDesc': versionDesc, 'hardwareVersionCode': hardwareVersionCode, 'hardwareVersion': hardwareVersion, 'hardwareVersionDesc': hardwareVersionDesc, 'structureDocUrl': structureDocUrl, 'structureDesignUrl': structureDesignUrl}
        response = self.request.post(url=self.url+'/admin/product/add', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_product_create_eui(self, Authentication_Token=None, secondLevelType=None, productId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'secondLevelType': secondLevelType, 'productId': productId}
        response = self.request.post(url=self.url+'/admin/product/create_eui', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_product_detail(self, Authentication_Token=None, productId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'productId': productId}
        response = self.request.post(url=self.url+'/admin/product/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_product_edit(self, Authentication_Token=None, id=None, productVersion=None, versionDesc=None, hardwareVersion=None, hardwareVersionDesc=None, structureDocUrl=None, structureDesignUrl=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id, 'productVersion': productVersion, 'versionDesc': versionDesc, 'hardwareVersion': hardwareVersion, 'hardwareVersionDesc': hardwareVersionDesc, 'structureDocUrl': structureDocUrl, 'structureDesignUrl': structureDesignUrl}
        response = self.request.post(url=self.url+'/admin/product/edit', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_product_get_eui(self, Authentication_Token=None, secondLevelType=None, productId=None, deviceNum=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'secondLevelType': secondLevelType, 'productId': productId, 'deviceNum': deviceNum}
        response = self.request.post(url=self.url+'/admin/product/get_eui', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_product_get_serial_code(self, Authentication_Token=None, firstLevelType=None, deviceNum=None, bizType=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'firstLevelType': firstLevelType, 'deviceNum': deviceNum, 'bizType': bizType}
        response = self.request.post(url=self.url+'/admin/product/get_serial_code', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_product_list(self, Authentication_Token=None, secondLevelType=None, firstLevelType=None, customerId=None, productVersionStatus=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'secondLevelType': secondLevelType, 'firstLevelType': firstLevelType, 'customerId': customerId, 'productVersionStatus': productVersionStatus}
        response = self.request.post(url=self.url+'/admin/product/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_product_page_list(self, Authentication_Token=None, pageSize=None, pageNum=None, secondLevelType=None, firstLevelType=None, productVersion=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'secondLevelType': secondLevelType, 'firstLevelType': firstLevelType, 'productVersion': productVersion}
        response = self.request.post(url=self.url+'/admin/product/page_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_product_status_exchange(self, Authentication_Token=None, id=None, status=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id, 'status': status}
        response = self.request.post(url=self.url+'/admin/product/status_exchange', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_product_version_code(self, Authentication_Token=None, secondLevelType=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'secondLevelType': secondLevelType}
        response = self.request.post(url=self.url+'/admin/product/version_code', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_upgrade_strategy_create(self, Authentication_Token=None, deviceList=None, firmwareId=None, upgradeScope=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceList': deviceList, 'firmwareId': firmwareId, 'upgradeScope': upgradeScope}
        response = self.request.post(url=self.url+'/admin/upgrade_strategy/create', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_upgrade_strategy_detail(self, Authentication_Token=None, id=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id}
        response = self.request.post(url=self.url+'/admin/upgrade_strategy/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_upgrade_strategy_device_list(self, Authentication_Token=None, pageSize=None, pageNum=None, id=None, deviceEui=None, upgradeStatus=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'id': id, 'deviceEui': deviceEui, 'upgradeStatus': upgradeStatus}
        response = self.request.post(url=self.url+'/admin/upgrade_strategy/device_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_upgrade_strategy_disable(self, Authentication_Token=None, id=None, remark=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id, 'remark': remark}
        response = self.request.post(url=self.url+'/admin/upgrade_strategy/disable', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_upgrade_strategy_page_list(self, Authentication_Token=None, pageSize=None, pageNum=None, productTypeId=None, productId=None, firmwareId=None, status=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'productTypeId': productTypeId, 'productId': productId, 'firmwareId': firmwareId, 'status': status}
        response = self.request.post(url=self.url+'/admin/upgrade_strategy/page_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_warn_log_detail(self, Authentication_Token=None, id=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id}
        response = self.request.post(url=self.url+'/admin/warn_log/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_warn_log_offline_gateway_list(self, Authentication_Token=None, id=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'id': id}
        response = self.request.post(url=self.url+'/admin/warn_log/offline_gateway_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_warn_log_page_list(self, Authentication_Token=None, pageSize=None, pageNum=None, deviceType=None, productId=None, deviceEui=None, warnType=None, customerName=None, startTime=None, endTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'deviceType': deviceType, 'productId': productId, 'deviceEui': deviceEui, 'warnType': warnType, 'customerName': customerName, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.url+'/admin/warn_log/page_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_warn_home_list(self, Authentication_Token=None, size=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'size': size}
        response = self.request.post(url=self.url+'/admin/warn/home_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_warn_page_list(self, Authentication_Token=None, pageSize=None, pageNum=None, deviceNo=None, startTime=None, endTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'pageSize': pageSize, 'pageNum': pageNum, 'deviceNo': deviceNo, 'startTime': startTime, 'endTime': endTime}
        response = self.request.post(url=self.url+'/admin/warn/page_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_warnSubscribe_list(self, Authentication_Token=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token}
        response = self.request.post(url=self.url+'/admin/warnSubscribe/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def admin_warnSubscribe_save(self, Authentication_Token=None, emails=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'emails': emails}
        response = self.request.post(url=self.url+'/admin/warnSubscribe/save', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_camera_get_by_gateway_no(self, Authentication_Token=None, gatewayNo=None, platformCode=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayNo': gatewayNo, 'platformCode': platformCode}
        response = self.request.post(url=self.url+'/api/camera/get_by_gateway_no', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_camera_get_by_platform_code(self, Authentication_Token=None, platformCode=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'platformCode': platformCode}
        response = self.request.post(url=self.url+'/api/camera/get_by_platform_code', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_camera_get_ys_token(self, Authentication_Token=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token}
        response = self.request.post(url=self.url+'/api/camera/get_ys_token', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_camera_list(self, Authentication_Token=None, serialNos=None, platformCode=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'serialNos': serialNos, 'platformCode': platformCode}
        response = self.request.post(url=self.url+'/api/camera/list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_camera_list_by_platform_code(self, Authentication_Token=None, platformCode=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'platformCode': platformCode}
        response = self.request.post(url=self.url+'/api/camera/list_by_platform_code', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_device_batch_bind(self, Authentication_Token=None, inputs=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'inputs': inputs}
        response = self.request.post(url=self.url+'/api/device/batch_bind', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_device_batch_detail(self, Authentication_Token=None, deviceEui=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url+'/api/device/batch_detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_device_detail(self, Authentication_Token=None, deviceEui=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url+'/api/device/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_device_set_temp_freq(self, Authentication_Token=None, deviceEui=None, frequency=None, periodValidity=None, platformCode=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui, 'frequency': frequency, 'periodValidity': periodValidity, 'platformCode': platformCode}
        response = self.request.post(url=self.url+'/api/device/set_temp_freq', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_device_temp_frequency_set(self, Authentication_Token=None, deviceEui=None, frequency=None, periodValidity=None, platformCode=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui, 'frequency': frequency, 'periodValidity': periodValidity, 'platformCode': platformCode}
        response = self.request.post(url=self.url+'/api/device/temp_frequency_set', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_gateway_control_board_get_by_gateway_no(self, Authentication_Token=None, gatewayNo=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayNo': gatewayNo}
        response = self.request.post(url=self.url+'/api/gateway/control_board/get_by_gateway_no', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_gateway_control_board_get_by_gateway_nos(self, Authentication_Token=None, gatewayNos=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayNos': gatewayNos}
        response = self.request.post(url=self.url+'/api/gateway/control_board/get_by_gateway_nos', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_gateway_control_board_lifting_rod(self, Authentication_Token=None, gatewayNo=None, liftingRodNo=None, liftingRodSwitch=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayNo': gatewayNo, 'liftingRodNo': liftingRodNo, 'liftingRodSwitch': liftingRodSwitch}
        response = self.request.post(url=self.url+'/api/gateway/control_board/lifting_rod', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_gateway_control_board_power(self, Authentication_Token=None, gatewayNo=None, powerNo=None, powerSwitch=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayNo': gatewayNo, 'powerNo': powerNo, 'powerSwitch': powerSwitch}
        response = self.request.post(url=self.url+'/api/gateway/control_board/power', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_gateway_detail(self, Authentication_Token=None, gatewayNo=None, platformCode=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayNo': gatewayNo, 'platformCode': platformCode}
        response = self.request.post(url=self.url+'/api/gateway/detail', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_gateway_gateway_list(self, Authentication_Token=None, gatewayNos=None, platformCode=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayNos': gatewayNos, 'platformCode': platformCode}
        response = self.request.post(url=self.url+'/api/gateway/gateway_list', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_gateway_get_by_platform_code(self, Authentication_Token=None, platformCode=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'platformCode': platformCode}
        response = self.request.post(url=self.url+'/api/gateway/get_by_platform_code', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_inner_lora_save_log(self, Authentication_Token=None, gatewayNo=None, runId=None, level=None, type=None, recordRowNo=None, voltage=None, time=None, message=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayNo': gatewayNo, 'runId': runId, 'level': level, 'type': type, 'recordRowNo': recordRowNo, 'voltage': voltage, 'time': time, 'message': message}
        response = self.request.post(url=self.url+'/api/inner/lora/save_log', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_inner_lora_sync_device(self, Authentication_Token=None, maxId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'maxId': maxId}
        response = self.request.post(url=self.url+'/api/inner/lora/sync_device', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_inner_lora_sync_gateway(self, Authentication_Token=None, maxId=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'maxId': maxId}
        response = self.request.post(url=self.url+'/api/inner/lora/sync_gateway', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_inner_platform_get_by_device_eui(self, Authentication_Token=None, deviceEui=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url+'/api/inner/platform/get_by_device_eui', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_inner_platform_get_by_device_euies(self, Authentication_Token=None, deviceEui=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url+'/api/inner/platform/get_by_device_euies', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_inner_platform_get_by_gateway_no(self, Authentication_Token=None, gatewayNo=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'gatewayNo': gatewayNo}
        response = self.request.post(url=self.url+'/api/inner/platform/get_by_gateway_no', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_inner_platform_get_by_platform_code(self, Authentication_Token=None, platformCode=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'platformCode': platformCode}
        response = self.request.post(url=self.url+'/api/inner/platform/get_by_platform_code', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_inner_platform_get_by_platform_ids(self, Authentication_Token=None, platformIds=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'platformIds': platformIds}
        response = self.request.post(url=self.url+'/api/inner/platform/get_by_platform_ids', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def api_inner_warn_push(self, Authentication_Token=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token}
        response = self.request.post(url=self.url+'/api/inner/warn/push', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def test_device_reports(self, Authentication_Token=None, aheadTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'aheadTime': aheadTime}
        response = self.request.post(url=self.url+'/test/device_reports', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")

    def test_gateway_reports(self, Authentication_Token=None, aheadTime=None):
        data = {'_tk_': self.mgr.token, '_deviceId_': self.mgr.device_id, 'Authentication_Token': Authentication_Token, 'aheadTime': aheadTime}
        response = self.request.post(url=self.url+'/test/gateway_reports', data=data)
        json_response = json.loads(response)
        if json_response["status"] == "OK":
            return json_response
        elif json_response["status"] == "ERROR":
            return json_response
        else:
            raise Exception("status未返回OK或ERROR")
