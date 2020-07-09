#! /usr/bin/env python
# encoding: utf-8

from tools.Config import Config
from tools.Request import Request

from actions import judge_response_status
import json


class KoalaAction(object):
    def __init__(self, koala):
        self.log = Log('Koala')
        self.request = Request()
        self.koala = koala
        self.request.headers['_Device-Id_'] = self.koala.device_id
        self.request.headers['_Token_'] = self.koala.token
        env = Config('config').data['run']
        hosts = Config('config').data['hosts'][env]
        self.url = hosts.get('WF_KOALA')

    @judge_response_status
    def admin_cattle_activity_list(self, cattleId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId}
        response = self.request.post(url=self.url + '/admin/cattle/activity-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_cattle_detail(self, cattleId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId}
        response = self.request.post(url=self.url + '/admin/cattle/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_cattle_farm_search_cond(self, countryIds=None, provinceIds=None, farmName=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'countryIds': countryIds,
                'provinceIds': provinceIds, 'farmName': farmName}
        response = self.request.post(url=self.url + '/admin/cattle/farm-search-cond', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_cattle_list(self, countryIds=None, provinceIds=None, farmIds=None, pn=None, ps=None, cattleName=None,
                          cattleLabel=None, cattleVariety=None, earTagStatus=None, birthDateOrderTyp=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'countryIds': countryIds,
                'provinceIds': provinceIds, 'farmIds': farmIds, 'pn': pn, 'ps': ps, 'cattleName': cattleName,
                'cattleLabel': cattleLabel, 'cattleVariety': cattleVariety, 'earTagStatus': earTagStatus,
                'birthDateOrderTyp': birthDateOrderTyp}
        response = self.request.post(url=self.url + '/admin/cattle/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_config_list(self, code=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'code': code}
        response = self.request.post(url=self.url + '/admin/config/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_config_redis_del(self):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id}
        response = self.request.post(url=self.url + '/admin/config/redis-del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_farm_region_list(self, farmId=None, types=None, isNeedFilter=None, isNeedStoreNum=None,
                               isNeedNoPaddock=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'types': types,
                'isNeedFilter': isNeedFilter, 'isNeedStoreNum': isNeedStoreNum, 'isNeedNoPaddock': isNeedNoPaddock}
        response = self.request.post(url=self.url + '/admin/farm-region/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_farm_right_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/admin/farm-right/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_farm_cattle_list(self, countryIds=None, provinceIds=None, farmIds=None, pn=None, ps=None, cattleName=None,
                               cattleLabel=None, cattleVariety=None, earTagStatus=None, birthDateOrderTyp=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'countryIds': countryIds,
                'provinceIds': provinceIds, 'farmIds': farmIds, 'pn': pn, 'ps': ps, 'cattleName': cattleName,
                'cattleLabel': cattleLabel, 'cattleVariety': cattleVariety, 'earTagStatus': earTagStatus,
                'birthDateOrderTyp': birthDateOrderTyp}
        response = self.request.post(url=self.url + '/admin/farm/cattle-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_farm_detail(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/admin/farm/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_farm_get_qualification_auth(self, urls=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'urls': urls}
        response = self.request.post(url=self.url + '/admin/farm/get_qualification-auth', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_farm_landmark_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/admin/farm/landmark-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_farm_list(self, countryIds=None, provinceIds=None, pn=None, ps=None, number=None, farmName=None,
                        farmType=None, farmAcreage=None, acreageSort=None, createTimeSort=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'countryIds': countryIds,
                'provinceIds': provinceIds, 'pn': pn, 'ps': ps, 'number': number, 'farmName': farmName,
                'farmType': farmType, 'farmAcreage': farmAcreage, 'acreageSort': acreageSort,
                'createTimeSort': createTimeSort}
        response = self.request.post(url=self.url + '/admin/farm/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_farm_map_info(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/admin/farm/map-info', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_farm_qualification_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/admin/farm/qualification-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_farm_search_cond(self):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id}
        response = self.request.post(url=self.url + '/admin/farm/search-cond', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_farm_signal_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/admin/farm/signal-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_farm_user_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/admin/farm/user-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_region_country_list(self, name=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'name': name}
        response = self.request.post(url=self.url + '/admin/region/country-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_region_province_list(self, name=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'name': name}
        response = self.request.post(url=self.url + '/admin/region/province-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_user_detail(self, userId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'userId': userId}
        response = self.request.post(url=self.url + '/admin/user/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_user_search_list(self):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id}
        response = self.request.post(url=self.url + '/admin/user/search-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def admin_user_user_list(self, pn=None, ps=None, status=None, userName=None, email=None, farmId=None, farmName=None,
                             createTimeSort=None, loginTimeSort=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'pn': pn, 'ps': ps, 'status': status,
                'userName': userName, 'email': email, 'farmId': farmId, 'farmName': farmName,
                'createTimeSort': createTimeSort, 'loginTimeSort': loginTimeSort}
        response = self.request.post(url=self.url + '/admin/user/user-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def common_calculate(self, coordinate=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'coordinate': coordinate}
        response = self.request.post(url=self.url + '/common/calculate', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def config_common_get_all_enum_list(self):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id}
        response = self.request.post(url=self.url + '/config/common/get-all-enum-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def config_common_get_config_list(self, codes=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'codes': codes}
        response = self.request.post(url=self.url + '/config/common/get-config-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def config_common_get_post_code_list(self, code=None, pn=None, ps=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'code': code, 'pn': pn, 'ps': ps}
        response = self.request.post(url=self.url + '/config/common/get-post-code-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_app_version_add(self, appId=None, updateType=None, downloadUrl=None, appCode=None, appName=None,
                               versionMilepost=None, versionNum=None, versionCode=None, versionNumBefore=None,
                               versionBig=None, updateTitle=None, updateTitleEn=None, updateMessage=None,
                               updateMessageEn=None, status=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'appId': appId, 'updateType': updateType,
                'downloadUrl': downloadUrl, 'appCode': appCode, 'appName': appName, 'versionMilepost': versionMilepost,
                'versionNum': versionNum, 'versionCode': versionCode, 'versionNumBefore': versionNumBefore,
                'versionBig': versionBig, 'updateTitle': updateTitle, 'updateTitleEn': updateTitleEn,
                'updateMessage': updateMessage, 'updateMessageEn': updateMessageEn, 'status': status}
        response = self.request.post(url=self.url + '/mobile/app-version/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_app_version_get(self, appId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'appId': appId}
        response = self.request.post(url=self.url + '/mobile/app-version/get', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_app_version_upload_app(self, file=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'file': file}
        response = self.request.post(url=self.url + '/mobile/app-version/upload-app', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_camera_add_or_update_name(self, farmId=None, number=None, name=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'number': number,
                'name': name}
        response = self.request.post(url=self.url + '/mobile/camera/add-or-update-name', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_camera_get_token(self, appKey=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'appKey': appKey}
        response = self.request.post(url=self.url + '/mobile/camera/get-token', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_camera_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/camera/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_breeding_add(self, cattleIds=None, bullIds=None, startDate=None, endDate=None, breedingType=None,
                                   num=None, isRegionSame=None, remark=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleIds': cattleIds,
                'bullIds': bullIds, 'startDate': startDate, 'endDate': endDate, 'breedingType': breedingType,
                'num': num, 'isRegionSame': isRegionSame, 'remark': remark}
        response = self.request.post(url=self.url + '/mobile/cattle-breeding/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_breeding_detail(self, id=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id}
        response = self.request.post(url=self.url + '/mobile/cattle-breeding/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_breeding_list(self, cattleId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId}
        response = self.request.post(url=self.url + '/mobile/cattle-breeding/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_breeding_update(self, bullIds=None, id=None, startDate=None, endDate=None, breedingType=None,
                                      num=None, isRegionSame=None, remark=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'bullIds': bullIds, 'id': id,
                'startDate': startDate, 'endDate': endDate, 'breedingType': breedingType, 'num': num,
                'isRegionSame': isRegionSame, 'remark': remark}
        response = self.request.post(url=self.url + '/mobile/cattle-breeding/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_calving_add(self, cattleId=None, cattleBreedingId=None, calvingResult=None, calvingDate=None,
                                  calvingCount=None, calvingSex=None, remark=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId,
                'cattleBreedingId': cattleBreedingId, 'calvingResult': calvingResult, 'calvingDate': calvingDate,
                'calvingCount': calvingCount, 'calvingSex': calvingSex, 'remark': remark}
        response = self.request.post(url=self.url + '/mobile/cattle-calving/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_calving_del_offspring(self, calfId=None, cattleId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'calfId': calfId, 'cattleId': cattleId}
        response = self.request.post(url=self.url + '/mobile/cattle-calving/del-offspring', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_calving_detail(self, id=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id}
        response = self.request.post(url=self.url + '/mobile/cattle-calving/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_calving_get_offspring(self, cattleId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId}
        response = self.request.post(url=self.url + '/mobile/cattle-calving/get-offspring', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_calving_update(self, id=None, cattleBreedingId=None, calvingResult=None, calvingDate=None,
                                     remark=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id,
                'cattleBreedingId': cattleBreedingId, 'calvingResult': calvingResult, 'calvingDate': calvingDate,
                'remark': remark}
        response = self.request.post(url=self.url + '/mobile/cattle-calving/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_drug_use_add(self, cattleIds=None, type=None, useDate=None, drugName=None, usageDose=None,
                                   remark=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleIds': cattleIds, 'type': type,
                'useDate': useDate, 'drugName': drugName, 'usageDose': usageDose, 'remark': remark}
        response = self.request.post(url=self.url + '/mobile/cattle-drug-use/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_drug_use_del(self, drugUseId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'drugUseId': drugUseId}
        response = self.request.post(url=self.url + '/mobile/cattle-drug-use/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_drug_use_detail(self, drugUseId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'drugUseId': drugUseId}
        response = self.request.post(url=self.url + '/mobile/cattle-drug-use/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_drug_use_edit(self, id=None, type=None, useDate=None, drugName=None, usageDose=None, remark=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id, 'type': type,
                'useDate': useDate, 'drugName': drugName, 'usageDose': usageDose, 'remark': remark}
        response = self.request.post(url=self.url + '/mobile/cattle-drug-use/edit', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_map_add_or_update_name(self, farmId=None, number=None, type=None, name=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'number': number,
                'type': type, 'name': name}
        response = self.request.post(url=self.url + '/mobile/cattle-map/add-or-update-name', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_map_bluetooth_near_cattle_list(self, deviceEuis=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'deviceEuis': deviceEuis}
        response = self.request.post(url=self.url + '/mobile/cattle-map/bluetooth-near-cattle-list', data=data,
                                     hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_map_cattle_card(self, farmId=None, deviceEui=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url + '/mobile/cattle-map/cattle-card', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_map_farm_signal(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/cattle-map/farm-signal', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_map_frequency_trace(self, farmId=None, deviceEui=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url + '/mobile/cattle-map/frequency-trace', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_map_heat_map(self, farmId=None, positionTimeStart=None, positionTimeEnd=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'positionTimeStart': positionTimeStart, 'positionTimeEnd': positionTimeEnd}
        response = self.request.post(url=self.url + '/mobile/cattle-map/heat-map', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_map_near_cattle_list(self, farmId=None, deviceType=None, deviceEui=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'deviceType': deviceType, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url + '/mobile/cattle-map/near-cattle-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_map_position_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/cattle-map/position-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_map_position_type_num(self, farmId=None, fenceId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'fenceId': fenceId}
        response = self.request.post(url=self.url + '/mobile/cattle-map/position-type-num', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_map_region_cattle_list(self, activeStatus=None, deviceType=None, bindStatus=None, farmId=None,
                                             regionId=None, searchName=None, searchNameOrVisionNum=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'activeStatus': activeStatus,
                'deviceType': deviceType, 'bindStatus': bindStatus, 'farmId': farmId, 'regionId': regionId,
                'searchName': searchName, 'searchNameOrVisionNum': searchNameOrVisionNum}
        response = self.request.post(url=self.url + '/mobile/cattle-map/region-cattle-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_map_signal_relay_del(self, farmId=None, serialNo=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'serialNo': serialNo}
        response = self.request.post(url=self.url + '/mobile/cattle-map/signal-relay-del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_map_trace(self, farmId=None, deviceEui=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url + '/mobile/cattle-map/trace', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_preg_add(self, cattleIds=None, cattleBreedingId=None, checkDate=None, checkResult=None,
                               checkType=None, predictCalvingDate=None, farmId=None, regionId=None, remark=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleIds': cattleIds,
                'cattleBreedingId': cattleBreedingId, 'checkDate': checkDate, 'checkResult': checkResult,
                'checkType': checkType, 'predictCalvingDate': predictCalvingDate, 'farmId': farmId,
                'regionId': regionId, 'remark': remark}
        response = self.request.post(url=self.url + '/mobile/cattle-preg/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_preg_detail(self, id=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id}
        response = self.request.post(url=self.url + '/mobile/cattle-preg/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_preg_update(self, id=None, cattleBreedingId=None, checkDate=None, checkResult=None,
                                  checkType=None, predictCalvingDate=None, remark=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id,
                'cattleBreedingId': cattleBreedingId, 'checkDate': checkDate, 'checkResult': checkResult,
                'checkType': checkType, 'predictCalvingDate': predictCalvingDate, 'remark': remark}
        response = self.request.post(url=self.url + '/mobile/cattle-preg/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_search_detail(self, cattleId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId}
        response = self.request.post(url=self.url + '/mobile/cattle-search/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_search_detail_by_device(self, deviceId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'deviceId': deviceId}
        response = self.request.post(url=self.url + '/mobile/cattle-search/detail-by-device', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_search_get_blood_relation(self, cattleId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId}
        response = self.request.post(url=self.url + '/mobile/cattle-search/get-blood-relation', data=data,
                                     hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_search_get_offspring(self, cattleId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId}
        response = self.request.post(url=self.url + '/mobile/cattle-search/get-offspring', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_search_get_purchase_detail(self, cattleId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId}
        response = self.request.post(url=self.url + '/mobile/cattle-search/get-purchase-detail', data=data,
                                     hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_search_list(self, cattleId=None, regionId=None, type=None, level=None, varietyId=None, sexId=None,
                                  saleStatus=None, pn=None, ps=None, farmId=None, stage=None, orderType=None,
                                  isBindDevice=None, searchName=None, searchType=None, searchNameOrVisionNum=None,
                                  isSearchByUser=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId,
                'regionId': regionId, 'type': type, 'level': level, 'varietyId': varietyId, 'sexId': sexId,
                'saleStatus': saleStatus, 'pn': pn, 'ps': ps, 'farmId': farmId, 'stage': stage, 'orderType': orderType,
                'isBindDevice': isBindDevice, 'searchName': searchName, 'searchType': searchType,
                'searchNameOrVisionNum': searchNameOrVisionNum, 'isSearchByUser': isSearchByUser}
        response = self.request.post(url=self.url + '/mobile/cattle-search/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_search_list_enclosure(self, isNeedFilter=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'isNeedFilter': isNeedFilter}
        response = self.request.post(url=self.url + '/mobile/cattle-search/list-enclosure', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_search_whether_plan(self, cattleIds=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleIds': cattleIds}
        response = self.request.post(url=self.url + '/mobile/cattle-search/whether-plan', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_stage_cycle_del(self, id=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id}
        response = self.request.post(url=self.url + '/mobile/cattle-stage-cycle/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_stage_cycle_list(self, cattleId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId}
        response = self.request.post(url=self.url + '/mobile/cattle-stage-cycle/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_weaning_add(self, cattleIds=None, weaningDate=None, weaningWeight=None, farmId=None,
                                  regionId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleIds': cattleIds,
                'weaningDate': weaningDate, 'weaningWeight': weaningWeight, 'farmId': farmId, 'regionId': regionId}
        response = self.request.post(url=self.url + '/mobile/cattle-weaning/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_weaning_detail(self, cattleWeaningId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleWeaningId': cattleWeaningId}
        response = self.request.post(url=self.url + '/mobile/cattle-weaning/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_weaning_update(self, id=None, weaningDate=None, weaningWeight=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id, 'weaningDate': weaningDate,
                'weaningWeight': weaningWeight}
        response = self.request.post(url=self.url + '/mobile/cattle-weaning/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_add_bind(self, farmId=None, regionId=None, type=None, varietyId=None, birthDate=None,
                               cattleName=None, sourceType=None, nlis=None, pid=None, mid=None, pname=None, mname=None,
                               supplier=None, supplierPic=None, nvdNo=None, bodyColor=None, isHorn=None, remark=None,
                               deviceId=None, imgs=None, visionNum=None, sourceRemark=None, buyTime=None, buyPrice=None,
                               buyWeight=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'regionId': regionId,
                'type': type, 'varietyId': varietyId, 'birthDate': birthDate, 'cattleName': cattleName,
                'sourceType': sourceType, 'nlis': nlis, 'pid': pid, 'mid': mid, 'pname': pname, 'mname': mname,
                'supplier': supplier, 'supplierPic': supplierPic, 'nvdNo': nvdNo, 'bodyColor': bodyColor,
                'isHorn': isHorn, 'remark': remark, 'deviceId': deviceId, 'imgs': imgs, 'visionNum': visionNum,
                'sourceRemark': sourceRemark, 'buyTime': buyTime, 'buyPrice': buyPrice, 'buyWeight': buyWeight}
        response = self.request.post(url=self.url + '/mobile/cattle/add-bind', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_bind_semaphore(self, farmId=None, deviceId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'deviceId': deviceId}
        response = self.request.post(url=self.url + '/mobile/cattle/bind-semaphore', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_change_fence(self, cattleIds=None, farmId=None, regionId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleIds': cattleIds, 'farmId': farmId,
                'regionId': regionId}
        response = self.request.post(url=self.url + '/mobile/cattle/change-fence', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_close_frequency(self, farmId=None, deviceEui=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url + '/mobile/cattle/close-frequency', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_del(self, cattleId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId}
        response = self.request.post(url=self.url + '/mobile/cattle/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_frequency_list(self, farmId=None, status=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'status': status}
        response = self.request.post(url=self.url + '/mobile/cattle/frequency-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_frequency_num(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/cattle/frequency-num', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_rebind(self, id=None, deviceId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id, 'deviceId': deviceId}
        response = self.request.post(url=self.url + '/mobile/cattle/rebind', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_rich_scan(self, deviceEui=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url + '/mobile/cattle/rich-scan', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_set_frequency_clever(self, farmId=None, deviceEui=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url + '/mobile/cattle/set-frequency-clever', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_set_frequency_clever_batch(self, farmId=None, deviceEuis=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'deviceEuis': deviceEuis}
        response = self.request.post(url=self.url + '/mobile/cattle/set-frequency-clever-batch', data=data,
                                     hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_unbind(self, farmId=None, cattleId=None, deviceId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'cattleId': cattleId,
                'deviceId': deviceId}
        response = self.request.post(url=self.url + '/mobile/cattle/unbind', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_update(self, id=None, farmId=None, regionId=None, varietyId=None, storedStatus=None,
                             birthDate=None, cattleName=None, sourceType=None, nlis=None, pid=None, mid=None,
                             pname=None, mname=None, supplier=None, supplierPic=None, nvdNo=None, bodyColor=None,
                             isHorn=None, remark=None, imgs=None, visionNum=None, sourceRemark=None, buyTime=None,
                             buyPrice=None, buyWeight=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id, 'farmId': farmId,
                'regionId': regionId, 'varietyId': varietyId, 'storedStatus': storedStatus, 'birthDate': birthDate,
                'cattleName': cattleName, 'sourceType': sourceType, 'nlis': nlis, 'pid': pid, 'mid': mid,
                'pname': pname, 'mname': mname, 'supplier': supplier, 'supplierPic': supplierPic, 'nvdNo': nvdNo,
                'bodyColor': bodyColor, 'isHorn': isHorn, 'remark': remark, 'imgs': imgs, 'visionNum': visionNum,
                'sourceRemark': sourceRemark, 'buyTime': buyTime, 'buyPrice': buyPrice, 'buyWeight': buyWeight}
        response = self.request.post(url=self.url + '/mobile/cattle/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_update_blood(self, cattleId=None, pid=None, mid=None, pname=None, mname=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId, 'pid': pid,
                'mid': mid, 'pname': pname, 'mname': mname}
        response = self.request.post(url=self.url + '/mobile/cattle/update-blood', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattle_update_purchase(self, id=None, sourceType=None, supplier=None, supplierPic=None, nvdNo=None,
                                      buyTime=None, sourceRemark=None, buyPrice=None, buyWeight=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id, 'sourceType': sourceType,
                'supplier': supplier, 'supplierPic': supplierPic, 'nvdNo': nvdNo, 'buyTime': buyTime,
                'sourceRemark': sourceRemark, 'buyPrice': buyPrice, 'buyWeight': buyWeight}
        response = self.request.post(url=self.url + '/mobile/cattle/update-purchase', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattleRemark_get(self):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id}
        response = self.request.post(url=self.url + '/mobile/cattleRemark/get', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_cattleSale_get(self):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id}
        response = self.request.post(url=self.url + '/mobile/cattleSale/get', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_attach_add_qualification(self, farmId=None, attachment=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'attachment': attachment}
        response = self.request.post(url=self.url + '/mobile/farm-attach/add-qualification', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_attach_album_add(self, lable_id=None, lable_name=None, farmId=None, fileName=None, fileType=None,
                                     fileSize=None, fileUrl=None, isCover=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'lable_id': lable_id,
                'lable_name': lable_name, 'farmId': farmId, 'fileName': fileName, 'fileType': fileType,
                'fileSize': fileSize, 'fileUrl': fileUrl, 'isCover': isCover}
        response = self.request.post(url=self.url + '/mobile/farm-attach/album-add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_attach_album_del(self, attachId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'attachId': attachId}
        response = self.request.post(url=self.url + '/mobile/farm-attach/album-del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_attach_album_upload(self, file=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'file': file}
        response = self.request.post(url=self.url + '/mobile/farm-attach/album-upload', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_attach_cover_set(self, attachId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'attachId': attachId}
        response = self.request.post(url=self.url + '/mobile/farm-attach/cover-set', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_attach_del_qualification(self, attachId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'attachId': attachId}
        response = self.request.post(url=self.url + '/mobile/farm-attach/del-qualification', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_attach_get_qualification_auth(self, urls=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'urls': urls}
        response = self.request.post(url=self.url + '/mobile/farm-attach/get_qualification-auth', data=data,
                                     hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_attach_list(self, pn=None, ps=None, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'pn': pn, 'ps': ps, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm-attach/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_attach_one_qualification_list(self, pn=None, ps=None, farmId=None, bizType=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'pn': pn, 'ps': ps, 'farmId': farmId,
                'bizType': bizType}
        response = self.request.post(url=self.url + '/mobile/farm-attach/one-qualification-list', data=data,
                                     hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_attach_qualification_type_count(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm-attach/qualification-type-count', data=data,
                                     hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_attach_qualification_upload(self, file=None, fileId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'file': file, 'fileId': fileId}
        response = self.request.post(url=self.url + '/mobile/farm-attach/qualification-upload', data=data,
                                     hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_attach_qualification_upload_process(self, fileId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'fileId': fileId}
        response = self.request.post(url=self.url + '/mobile/farm-attach/qualification-upload-process', data=data,
                                     hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_attach_qualification_upload_send_email(self, farmId=None, bizType=None, email=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'bizType': bizType,
                'email': email}
        response = self.request.post(url=self.url + '/mobile/farm-attach/qualification-upload-send-email', data=data,
                                     hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_book_add(self, farmId=None, accountBookName=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'accountBookName': accountBookName}
        response = self.request.post(url=self.url + '/mobile/farm-book/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_book_del(self, bookId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'bookId': bookId}
        response = self.request.post(url=self.url + '/mobile/farm-book/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_book_detail(self, bookId=None, countType=None, startDate=None, endDate=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'bookId': bookId, 'countType': countType,
                'startDate': startDate, 'endDate': endDate}
        response = self.request.post(url=self.url + '/mobile/farm-book/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_book_get_default_book(self, farmId=None, countType=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'countType': countType}
        response = self.request.post(url=self.url + '/mobile/farm-book/get-default-book', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_book_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm-book/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_book_set_default(self, bookId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'bookId': bookId}
        response = self.request.post(url=self.url + '/mobile/farm-book/set-default', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_book_statistic(self, farmId=None, countType=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'countType': countType}
        response = self.request.post(url=self.url + '/mobile/farm-book/statistic', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_book_update(self, farmId=None, accountBookId=None, accountBookName=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'accountBookId': accountBookId, 'accountBookName': accountBookName}
        response = self.request.post(url=self.url + '/mobile/farm-book/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_contacts_add(self, farmId=None, type=None, name=None, region=None, phone=None, email=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'type': type,
                'name': name, 'region': region, 'phone': phone, 'email': email}
        response = self.request.post(url=self.url + '/mobile/farm-contacts/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_contacts_change_farmer(self, farmId=None, farmerId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'farmerId': farmerId}
        response = self.request.post(url=self.url + '/mobile/farm-contacts/change-farmer', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_contacts_del(self, contactId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'contactId': contactId}
        response = self.request.post(url=self.url + '/mobile/farm-contacts/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_contacts_farmer(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm-contacts/farmer', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_contacts_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm-contacts/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_contacts_update(self, id=None, name=None, region=None, phone=None, email=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id, 'name': name, 'region': region,
                'phone': phone, 'email': email}
        response = self.request.post(url=self.url + '/mobile/farm-contacts/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_graze_plan_add(self, farmId=None, regionId=None, planType=None, planStartTime=None,
                                   currentQuality=None, endQuality=None, growRate=None, consumeRate=None,
                                   expectDate=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'regionId': regionId,
                'planType': planType, 'planStartTime': planStartTime, 'currentQuality': currentQuality,
                'endQuality': endQuality, 'growRate': growRate, 'consumeRate': consumeRate, 'expectDate': expectDate}
        response = self.request.post(url=self.url + '/mobile/farm-graze-plan/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_graze_plan_del(self, planId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'planId': planId}
        response = self.request.post(url=self.url + '/mobile/farm-graze-plan/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_graze_plan_detail(self, planId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'planId': planId}
        response = self.request.post(url=self.url + '/mobile/farm-graze-plan/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_graze_plan_list(self, farmId=None, status=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'status': status}
        response = self.request.post(url=self.url + '/mobile/farm-graze-plan/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_graze_plan_preview(self, farmId=None, regionId=None, planType=None, planStartTime=None,
                                       currentQuality=None, endQuality=None, growRate=None, consumeRate=None,
                                       expectDate=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'regionId': regionId,
                'planType': planType, 'planStartTime': planStartTime, 'currentQuality': currentQuality,
                'endQuality': endQuality, 'growRate': growRate, 'consumeRate': consumeRate, 'expectDate': expectDate}
        response = self.request.post(url=self.url + '/mobile/farm-graze-plan/preview', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_graze_plan_region_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm-graze-plan/region-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_graze_plan_update_status(self, planId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'planId': planId}
        response = self.request.post(url=self.url + '/mobile/farm-graze-plan/update-status', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_raise_add(self, farmId=None, regionId=None, feedingDate=None, remark=None, detailList=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'regionId': regionId,
                'feedingDate': feedingDate, 'remark': remark, 'detailList': detailList}
        response = self.request.post(url=self.url + '/mobile/farm-raise/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_raise_del(self, raiseId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'raiseId': raiseId}
        response = self.request.post(url=self.url + '/mobile/farm-raise/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_raise_detail(self, raiseId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'raiseId': raiseId}
        response = self.request.post(url=self.url + '/mobile/farm-raise/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_raise_edit(self, id=None, farmId=None, regionId=None, feedingDate=None, remark=None,
                               detailList=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id, 'farmId': farmId,
                'regionId': regionId, 'feedingDate': feedingDate, 'remark': remark, 'detailList': detailList}
        response = self.request.post(url=self.url + '/mobile/farm-raise/edit', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_raise_list(self, regionId=None, pn=None, ps=None, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'regionId': regionId, 'pn': pn, 'ps': ps,
                'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm-raise/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_region_add(self, farmId=None, regionType=None, name=None, perimeter=None, area=None, colorType=None,
                               soilType=None, soilPh=None, pastureType=None, remark=None, locations=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'regionType': regionType, 'name': name, 'perimeter': perimeter, 'area': area, 'colorType': colorType,
                'soilType': soilType, 'soilPh': soilPh, 'pastureType': pastureType, 'remark': remark,
                'locations': locations}
        response = self.request.post(url=self.url + '/mobile/farm-region/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_region_del(self, regionId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'regionId': regionId}
        response = self.request.post(url=self.url + '/mobile/farm-region/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_region_get(self, regionId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'regionId': regionId}
        response = self.request.post(url=self.url + '/mobile/farm-region/get', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_region_list(self, farmId=None, types=None, isNeedFilter=None, isNeedStoreNum=None,
                                isNeedNoPaddock=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'types': types,
                'isNeedFilter': isNeedFilter, 'isNeedStoreNum': isNeedStoreNum, 'isNeedNoPaddock': isNeedNoPaddock}
        response = self.request.post(url=self.url + '/mobile/farm-region/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_region_paddock_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm-region/paddock-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_region_set_state(self, id=None, paddockState=None, grassState=None, remark=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id, 'paddockState': paddockState,
                'grassState': grassState, 'remark': remark}
        response = self.request.post(url=self.url + '/mobile/farm-region/set-state', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_region_update(self, id=None, name=None, perimeter=None, area=None, colorType=None, soilType=None,
                                  soilPh=None, pastureType=None, remark=None, locations=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id, 'name': name,
                'perimeter': perimeter, 'area': area, 'colorType': colorType, 'soilType': soilType, 'soilPh': soilPh,
                'pastureType': pastureType, 'remark': remark, 'locations': locations}
        response = self.request.post(url=self.url + '/mobile/farm-region/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_right_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm-right/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_signal_del(self, farmId=None, deviceId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'deviceId': deviceId}
        response = self.request.post(url=self.url + '/mobile/farm-signal/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_signal_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm-signal/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_supplies_add(self, farmId=None, suppliesType=None, suppliesName=None, specs=None, resource=None,
                                 price=None, stock=None, unit=None, acqDate=None, expDate=None, remark=None, imgs=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'suppliesType': suppliesType, 'suppliesName': suppliesName, 'specs': specs, 'resource': resource,
                'price': price, 'stock': stock, 'unit': unit, 'acqDate': acqDate, 'expDate': expDate, 'remark': remark,
                'imgs': imgs}
        response = self.request.post(url=self.url + '/mobile/farm-supplies/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_supplies_count(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm-supplies/count', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_supplies_del(self, suppliesId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'suppliesId': suppliesId}
        response = self.request.post(url=self.url + '/mobile/farm-supplies/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_supplies_detail(self, suppliesId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'suppliesId': suppliesId}
        response = self.request.post(url=self.url + '/mobile/farm-supplies/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_supplies_list(self, pn=None, ps=None, farmId=None, suppliesType=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'pn': pn, 'ps': ps, 'farmId': farmId,
                'suppliesType': suppliesType}
        response = self.request.post(url=self.url + '/mobile/farm-supplies/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_supplies_update(self, id=None, farmId=None, suppliesType=None, suppliesName=None, specs=None,
                                    resource=None, price=None, stock=None, unit=None, acqDate=None, expDate=None,
                                    remark=None, imgs=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id, 'farmId': farmId,
                'suppliesType': suppliesType, 'suppliesName': suppliesName, 'specs': specs, 'resource': resource,
                'price': price, 'stock': stock, 'unit': unit, 'acqDate': acqDate, 'expDate': expDate, 'remark': remark,
                'imgs': imgs}
        response = self.request.post(url=self.url + '/mobile/farm-supplies/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_task_add(self, userIds=None, farmId=None, taskName=None, startTime=None, endTime=None,
                             description=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'userIds': userIds, 'farmId': farmId,
                'taskName': taskName, 'startTime': startTime, 'endTime': endTime, 'description': description}
        response = self.request.post(url=self.url + '/mobile/farm-task/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_task_del(self, taskId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'taskId': taskId}
        response = self.request.post(url=self.url + '/mobile/farm-task/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_task_detail(self, taskId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'taskId': taskId}
        response = self.request.post(url=self.url + '/mobile/farm-task/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_task_home(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm-task/home', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_task_list(self, pn=None, ps=None, farmId=None, status=None, selectType=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'pn': pn, 'ps': ps, 'farmId': farmId,
                'status': status, 'selectType': selectType}
        response = self.request.post(url=self.url + '/mobile/farm-task/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_task_update(self, userIds=None, id=None, farmId=None, taskName=None, startTime=None, endTime=None,
                                description=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'userIds': userIds, 'id': id,
                'farmId': farmId, 'taskName': taskName, 'startTime': startTime, 'endTime': endTime,
                'description': description}
        response = self.request.post(url=self.url + '/mobile/farm-task/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_task_update_status(self, taskId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'taskId': taskId}
        response = self.request.post(url=self.url + '/mobile/farm-task/update-status', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_user_detail(self, farmId=None, userId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'userId': userId}
        response = self.request.post(url=self.url + '/mobile/farm-user/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_user_list_by_farm(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm-user/list-by-farm', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_user_list_by_user(self):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id}
        response = self.request.post(url=self.url + '/mobile/farm-user/list-by-user', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_user_remove(self, farmId=None, userId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'userId': userId}
        response = self.request.post(url=self.url + '/mobile/farm-user/remove', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_user_roles(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm-user/roles', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_user_user_role(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm-user/user-role', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_add(self, name=None, postcodeId=None, address=None, pic=None, lng=None, lat=None, currencyType=None,
                        farmRightAddList=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'name': name, 'postcodeId': postcodeId,
                'address': address, 'pic': pic, 'lng': lng, 'lat': lat, 'currencyType': currencyType,
                'farmRightAddList': farmRightAddList}
        response = self.request.post(url=self.url + '/mobile/farm/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_del(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_detail(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_get_default(self):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id}
        response = self.request.post(url=self.url + '/mobile/farm/get-default', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_list(self):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id}
        response = self.request.post(url=self.url + '/mobile/farm/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_search_condition(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm/search-condition', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_set_default(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/farm/set-default', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farm_update(self, farmId=None, name=None, postcodeId=None, address=None, pic=None, lng=None, lat=None,
                           rightArea=None, type=None, rightNum=None, purchasePrice=None, farmRightUpdateList=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'name': name,
                'postcodeId': postcodeId, 'address': address, 'pic': pic, 'lng': lng, 'lat': lat,
                'rightArea': rightArea, 'type': type, 'rightNum': rightNum, 'purchasePrice': purchasePrice,
                'farmRightUpdateList': farmRightUpdateList}
        response = self.request.post(url=self.url + '/mobile/farm/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farmBill_add(self, farmId=None, bookId=None, budgetType=None, billTypeId=None, price=None,
                            recordDate=None, remark=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'bookId': bookId,
                'budgetType': budgetType, 'billTypeId': billTypeId, 'price': price, 'recordDate': recordDate,
                'remark': remark}
        response = self.request.post(url=self.url + '/mobile/farmBill/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farmBill_bill_count_page_list(self, pn=None, ps=None, farmId=None, bookId=None, budgetType=None,
                                             billTypeId=None, queryDate=None, startDate=None, endDate=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'pn': pn, 'ps': ps, 'farmId': farmId,
                'bookId': bookId, 'budgetType': budgetType, 'billTypeId': billTypeId, 'queryDate': queryDate,
                'startDate': startDate, 'endDate': endDate}
        response = self.request.post(url=self.url + '/mobile/farmBill/bill-count-page-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farmBill_count_bill_num(self, farmId=None, bookId=None, startDate=None, endDate=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'bookId': bookId,
                'startDate': startDate, 'endDate': endDate}
        response = self.request.post(url=self.url + '/mobile/farmBill/count-bill-num', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farmBill_del(self, billId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'billId': billId}
        response = self.request.post(url=self.url + '/mobile/farmBill/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farmBill_detail(self, billId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'billId': billId}
        response = self.request.post(url=self.url + '/mobile/farmBill/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farmBill_update(self, id=None, farmId=None, bookId=None, budgetType=None, billTypeId=None, price=None,
                               recordDate=None, remark=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id, 'farmId': farmId,
                'bookId': bookId, 'budgetType': budgetType, 'billTypeId': billTypeId, 'price': price,
                'recordDate': recordDate, 'remark': remark}
        response = self.request.post(url=self.url + '/mobile/farmBill/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farmBillType_add(self, farmId=None, budgetType=None, billTypeName=None, iconUrl=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'budgetType': budgetType, 'billTypeName': billTypeName, 'iconUrl': iconUrl}
        response = self.request.post(url=self.url + '/mobile/farmBillType/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farmBillType_book_filter(self, farmId=None, bookId=None, budgetType=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'bookId': bookId,
                'budgetType': budgetType}
        response = self.request.post(url=self.url + '/mobile/farmBillType/book-filter', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farmBillType_del(self, billTypeId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'billTypeId': billTypeId}
        response = self.request.post(url=self.url + '/mobile/farmBillType/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_farmBillType_list(self, farmId=None, budgetType=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'budgetType': budgetType}
        response = self.request.post(url=self.url + '/mobile/farmBillType/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_label_list(self, id=None, bizId=None, nameLike=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id, 'bizId': bizId,
                'nameLike': nameLike}
        response = self.request.post(url=self.url + '/mobile/label/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_landmark_add(self, farmId=None, regionId=None, type1=None, type2=None, name=None, buildDate=None,
                            buildPrice=None, remark=None, length=None, specs=None, waterCapacity=None, imageList=None,
                            locations=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'regionId': regionId,
                'type1': type1, 'type2': type2, 'name': name, 'buildDate': buildDate, 'buildPrice': buildPrice,
                'remark': remark, 'length': length, 'specs': specs, 'waterCapacity': waterCapacity,
                'imageList': imageList, 'locations': locations}
        response = self.request.post(url=self.url + '/mobile/landmark/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_landmark_del(self, landmarkId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'landmarkId': landmarkId}
        response = self.request.post(url=self.url + '/mobile/landmark/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_landmark_detail(self, landmarkId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'landmarkId': landmarkId}
        response = self.request.post(url=self.url + '/mobile/landmark/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_landmark_list(self, farmId=None, types=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'types': types}
        response = self.request.post(url=self.url + '/mobile/landmark/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_landmark_type_count(self, farmId=None, regionId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'regionId': regionId}
        response = self.request.post(url=self.url + '/mobile/landmark/type-count', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_landmark_update(self, farmId=None, regionId=None, type1=None, type2=None, name=None, buildDate=None,
                               buildPrice=None, remark=None, length=None, specs=None, waterCapacity=None,
                               imageList=None, landmarkId=None, locations=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'regionId': regionId,
                'type1': type1, 'type2': type2, 'name': name, 'buildDate': buildDate, 'buildPrice': buildPrice,
                'remark': remark, 'length': length, 'specs': specs, 'waterCapacity': waterCapacity,
                'imageList': imageList, 'landmarkId': landmarkId, 'locations': locations}
        response = self.request.post(url=self.url + '/mobile/landmark/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_message_cattle_warn_list(self, pn=None, ps=None, parentMsgType=None, msgType=None, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'pn': pn, 'ps': ps,
                'parentMsgType': parentMsgType, 'msgType': msgType, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/message/cattle-warn-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_message_del(self, msgId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'msgId': msgId}
        response = self.request.post(url=self.url + '/mobile/message/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_message_home_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/message/home-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_message_page_list(self, pn=None, ps=None, parentMsgType=None, msgType=None, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'pn': pn, 'ps': ps,
                'parentMsgType': parentMsgType, 'msgType': msgType, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/message/page-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_message_read(self, msgId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'msgId': msgId}
        response = self.request.post(url=self.url + '/mobile/message/read', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_message_read_all(self, parentMsgType=None, msgType=None, title=None, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'parentMsgType': parentMsgType,
                'msgType': msgType, 'title': title, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/message/read-all', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_message_unread(self, parentMsgType=None, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'parentMsgType': parentMsgType,
                'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/message/unread', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_share_add(self, farmId=None, content=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'content': content}
        response = self.request.post(url=self.url + '/mobile/share/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_statistics_cattle_home(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/statistics/cattle-home', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_statistics_group_detail(self, farmId=None, regionId=None, type=None, stage=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'regionId': regionId,
                'type': type, 'stage': stage}
        response = self.request.post(url=self.url + '/mobile/statistics/group-detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_statistics_group_location(self, farmId=None, regionId=None, type=None, stage=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'regionId': regionId,
                'type': type, 'stage': stage}
        response = self.request.post(url=self.url + '/mobile/statistics/group-location', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_statistics_home_cattle_count(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/statistics/home-cattle-count', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_statistics_stat_abnormal_list(self, farmId=None, positionStatus=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'positionStatus': positionStatus}
        response = self.request.post(url=self.url + '/mobile/statistics/stat-abnormal-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_statistics_stat_abnormal_map(self, farmId=None, positionStatus=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'positionStatus': positionStatus}
        response = self.request.post(url=self.url + '/mobile/statistics/stat-abnormal-map', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_statistics_stat_abnormal_near(self, farmId=None, positionStatus=None, deviceEui=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'positionStatus': positionStatus, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url + '/mobile/statistics/stat-abnormal-near', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_user_invite_email_invite(self, farmId=None, email=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'email': email}
        response = self.request.post(url=self.url + '/mobile/user-invite/email-invite', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_user_invite_inner_accept(self, inviteId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'inviteId': inviteId}
        response = self.request.post(url=self.url + '/mobile/user-invite/inner-accept', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_user_invite_inner_invite(self, farmId=None, inviteeId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'inviteeId': inviteeId}
        response = self.request.post(url=self.url + '/mobile/user-invite/inner-invite', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_user_invite_inner_invite_info(self, inviteId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'inviteId': inviteId}
        response = self.request.post(url=self.url + '/mobile/user-invite/inner-invite-info', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_user_invite_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/user-invite/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_user_invite_search(self, farmId=None, account=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'account': account}
        response = self.request.post(url=self.url + '/mobile/user-invite/search', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_user_role_set_role(self, farmId=None, userId=None, roleId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'userId': userId,
                'roleId': roleId}
        response = self.request.post(url=self.url + '/mobile/user-role/set-role', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_water_resource_home_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/water-resource/home-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_water_resource_list(self, pn=None, ps=None, farmId=None, type=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'pn': pn, 'ps': ps, 'farmId': farmId,
                'type': type}
        response = self.request.post(url=self.url + '/mobile/water-resource/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_weather_detail(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/weather/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_weather_home_rain(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/mobile/weather/home-rain', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_wx_getAccessToken(self):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id}
        response = self.request.post(url=self.url + '/mobile/wx/getAccessToken', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_wx_refreshAccessToken(self):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id}
        response = self.request.post(url=self.url + '/mobile/wx/refreshAccessToken', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_wx_refreshSignature(self, url=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'url': url}
        response = self.request.post(url=self.url + '/mobile/wx/refreshSignature', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def mobile_wx_signature(self, url=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'url': url}
        response = self.request.post(url=self.url + '/mobile/wx/signature', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def v126_mobile_cattle_search_detail(self, cattleId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId}
        response = self.request.post(url=self.url + '/v1.2.6/mobile/cattle-search/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def v126_mobile_cattle_search_detail_by_device(self, deviceId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'deviceId': deviceId}
        response = self.request.post(url=self.url + '/v1.2.6/mobile/cattle-search/detail-by-device', data=data,
                                     hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def v126_mobile_cattle_search_get_blood_relation(self, cattleId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId}
        response = self.request.post(url=self.url + '/v1.2.6/mobile/cattle-search/get-blood-relation', data=data,
                                     hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def v126_mobile_cattle_add_bind(self, farmId=None, regionId=None, type=None, blood=None, level=None, tattoo=None,
                                    varietyId=None, birthDate=None, cattleName=None, sourceType=None, nlis=None,
                                    pid=None, mid=None, pname=None, mname=None, supplier=None, supplierPic=None,
                                    nvdNo=None, bodyColor=None, isHorn=None, remark=None, deviceId=None, imgs=None,
                                    visionNum=None, sourceRemark=None, buyTime=None, buyPrice=None, buyWeight=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'regionId': regionId,
                'type': type, 'blood': blood, 'level': level, 'tattoo': tattoo, 'varietyId': varietyId,
                'birthDate': birthDate, 'cattleName': cattleName, 'sourceType': sourceType, 'nlis': nlis, 'pid': pid,
                'mid': mid, 'pname': pname, 'mname': mname, 'supplier': supplier, 'supplierPic': supplierPic,
                'nvdNo': nvdNo, 'bodyColor': bodyColor, 'isHorn': isHorn, 'remark': remark, 'deviceId': deviceId,
                'imgs': imgs, 'visionNum': visionNum, 'sourceRemark': sourceRemark, 'buyTime': buyTime,
                'buyPrice': buyPrice, 'buyWeight': buyWeight}
        response = self.request.post(url=self.url + '/v1.2.6/mobile/cattle/add-bind', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def v126_mobile_cattle_update(self, id=None, farmId=None, regionId=None, type=None, varietyId=None, blood=None,
                                  level=None, tattoo=None, birthDate=None, cattleName=None, sourceType=None, nlis=None,
                                  pid=None, mid=None, pname=None, mname=None, supplier=None, supplierPic=None,
                                  nvdNo=None, bodyColor=None, isHorn=None, remark=None, imgs=None, visionNum=None,
                                  sourceRemark=None, buyTime=None, buyPrice=None, buyWeight=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id, 'farmId': farmId,
                'regionId': regionId, 'type': type, 'varietyId': varietyId, 'blood': blood, 'level': level,
                'tattoo': tattoo, 'birthDate': birthDate, 'cattleName': cattleName, 'sourceType': sourceType,
                'nlis': nlis, 'pid': pid, 'mid': mid, 'pname': pname, 'mname': mname, 'supplier': supplier,
                'supplierPic': supplierPic, 'nvdNo': nvdNo, 'bodyColor': bodyColor, 'isHorn': isHorn, 'remark': remark,
                'imgs': imgs, 'visionNum': visionNum, 'sourceRemark': sourceRemark, 'buyTime': buyTime,
                'buyPrice': buyPrice, 'buyWeight': buyWeight}
        response = self.request.post(url=self.url + '/v1.2.6/mobile/cattle/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_camera_get_token(self, appKey=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'appKey': appKey}
        response = self.request.post(url=self.url + '/web/camera/get-token', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_camera_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/camera/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_camera_rename(self, farmId=None, number=None, name=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'number': number,
                'name': name}
        response = self.request.post(url=self.url + '/web/camera/rename', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_abnormal_count(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/cattle-abnormal/count', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_abnormal_list(self, farmId=None, positionStatus=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'positionStatus': positionStatus}
        response = self.request.post(url=self.url + '/web/cattle-abnormal/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_breeding_add(self, cattleIds=None, bullIds=None, startDate=None, endDate=None, breedingType=None,
                                num=None, isRegionSame=None, remark=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleIds': cattleIds,
                'bullIds': bullIds, 'startDate': startDate, 'endDate': endDate, 'breedingType': breedingType,
                'num': num, 'isRegionSame': isRegionSame, 'remark': remark}
        response = self.request.post(url=self.url + '/web/cattle-breeding/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_calving_add(self, calvingResult=None, remark=None, calvingDetail=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'calvingResult': calvingResult,
                'remark': remark, 'calvingDetail': calvingDetail}
        response = self.request.post(url=self.url + '/web/cattle-calving/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_drug_use_add(self, cattleIds=None, type=None, useDate=None, drugName=None, usageDose=None,
                                remark=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleIds': cattleIds, 'type': type,
                'useDate': useDate, 'drugName': drugName, 'usageDose': usageDose, 'remark': remark}
        response = self.request.post(url=self.url + '/web/cattle-drug-use/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_map_cattle_card(self, farmId=None, deviceEui=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url + '/web/cattle-map/cattle-card', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_map_heat_map(self, farmId=None, positionTimeStart=None, positionTimeEnd=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'positionTimeStart': positionTimeStart, 'positionTimeEnd': positionTimeEnd}
        response = self.request.post(url=self.url + '/web/cattle-map/heat-map', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_map_near_cattle_list(self, farmId=None, deviceType=None, deviceEui=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'deviceType': deviceType, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url + '/web/cattle-map/near-cattle-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_map_position_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/cattle-map/position-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_map_trace(self, farmId=None, deviceEui=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'deviceEui': deviceEui}
        response = self.request.post(url=self.url + '/web/cattle-map/trace', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_preg_add(self, cattleIds=None, cattleBreedingId=None, checkDate=None, checkResult=None,
                            checkType=None, predictCalvingDate=None, farmId=None, regionId=None, remark=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleIds': cattleIds,
                'cattleBreedingId': cattleBreedingId, 'checkDate': checkDate, 'checkResult': checkResult,
                'checkType': checkType, 'predictCalvingDate': predictCalvingDate, 'farmId': farmId,
                'regionId': regionId, 'remark': remark}
        response = self.request.post(url=self.url + '/web/cattle-preg/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_search_associate(self, type=None, pn=None, ps=None, farmId=None, cattleName=None, visionNum=None,
                                    nlis=None, tattoo=None, searchKey=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'type': type, 'pn': pn, 'ps': ps,
                'farmId': farmId, 'cattleName': cattleName, 'visionNum': visionNum, 'nlis': nlis, 'tattoo': tattoo,
                'searchKey': searchKey}
        response = self.request.post(url=self.url + '/web/cattle-search/associate', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_search_detail(self, cattleId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId}
        response = self.request.post(url=self.url + '/web/cattle-search/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_search_list(self, regionId=None, type=None, varietyId=None, level=None, stages=None, pn=None,
                               ps=None, farmId=None, cattleName=None, visionNum=None, deviceId=None, nlis=None,
                               tattoo=None, parentId=None, stageDetail=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'regionId': regionId, 'type': type,
                'varietyId': varietyId, 'level': level, 'stages': stages, 'pn': pn, 'ps': ps, 'farmId': farmId,
                'cattleName': cattleName, 'visionNum': visionNum, 'deviceId': deviceId, 'nlis': nlis, 'tattoo': tattoo,
                'parentId': parentId, 'stageDetail': stageDetail}
        response = self.request.post(url=self.url + '/web/cattle-search/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_search_whether_plan(self, cattleIds=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleIds': cattleIds}
        response = self.request.post(url=self.url + '/web/cattle-search/whether-plan', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_weaning_add(self, cattleIds=None, weaningDate=None, weaningWeight=None, farmId=None, regionId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleIds': cattleIds,
                'weaningDate': weaningDate, 'weaningWeight': weaningWeight, 'farmId': farmId, 'regionId': regionId}
        response = self.request.post(url=self.url + '/web/cattle-weaning/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_add(self, farmId=None, regionId=None, type=None, blood=None, level=None, tattoo=None, varietyId=None,
                       birthDate=None, cattleName=None, sourceType=None, nlis=None, pid=None, mid=None, pname=None,
                       mname=None, supplier=None, supplierPic=None, nvdNo=None, bodyColor=None, isHorn=None,
                       remark=None, deviceId=None, imgs=None, visionNum=None, sourceRemark=None, buyTime=None,
                       buyPrice=None, buyWeight=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'regionId': regionId,
                'type': type, 'blood': blood, 'level': level, 'tattoo': tattoo, 'varietyId': varietyId,
                'birthDate': birthDate, 'cattleName': cattleName, 'sourceType': sourceType, 'nlis': nlis, 'pid': pid,
                'mid': mid, 'pname': pname, 'mname': mname, 'supplier': supplier, 'supplierPic': supplierPic,
                'nvdNo': nvdNo, 'bodyColor': bodyColor, 'isHorn': isHorn, 'remark': remark, 'deviceId': deviceId,
                'imgs': imgs, 'visionNum': visionNum, 'sourceRemark': sourceRemark, 'buyTime': buyTime,
                'buyPrice': buyPrice, 'buyWeight': buyWeight}
        response = self.request.post(url=self.url + '/web/cattle/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_change_fence(self, cattleIds=None, farmId=None, regionId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleIds': cattleIds, 'farmId': farmId,
                'regionId': regionId}
        response = self.request.post(url=self.url + '/web/cattle/change-fence', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_del(self, cattleId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'cattleId': cattleId}
        response = self.request.post(url=self.url + '/web/cattle/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_download_template(self):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id}
        response = self.request.get(url=self.url + '/web/cattle/download-template', params=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_edit(self, id=None, farmId=None, regionId=None, type=None, varietyId=None, blood=None, level=None,
                        tattoo=None, birthDate=None, cattleName=None, sourceType=None, nlis=None, pid=None, mid=None,
                        pname=None, mname=None, supplier=None, supplierPic=None, nvdNo=None, bodyColor=None,
                        isHorn=None, remark=None, imgs=None, visionNum=None, sourceRemark=None, buyTime=None,
                        buyPrice=None, buyWeight=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id, 'farmId': farmId,
                'regionId': regionId, 'type': type, 'varietyId': varietyId, 'blood': blood, 'level': level,
                'tattoo': tattoo, 'birthDate': birthDate, 'cattleName': cattleName, 'sourceType': sourceType,
                'nlis': nlis, 'pid': pid, 'mid': mid, 'pname': pname, 'mname': mname, 'supplier': supplier,
                'supplierPic': supplierPic, 'nvdNo': nvdNo, 'bodyColor': bodyColor, 'isHorn': isHorn, 'remark': remark,
                'imgs': imgs, 'visionNum': visionNum, 'sourceRemark': sourceRemark, 'buyTime': buyTime,
                'buyPrice': buyPrice, 'buyWeight': buyWeight}
        response = self.request.post(url=self.url + '/web/cattle/edit', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_cattle_import_template(self, file=None, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'file': file, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/cattle/import-template', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_config_list(self, codes=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'codes': codes}
        response = self.request.post(url=self.url + '/web/config/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_attach_album_upload(self, file=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'file': file}
        response = self.request.post(url=self.url + '/web/farm-attach/album-upload', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_bill_type_add(self, farmId=None, budgetType=None, billTypeName=None, iconUrl=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'budgetType': budgetType, 'billTypeName': billTypeName, 'iconUrl': iconUrl}
        response = self.request.post(url=self.url + '/web/farm-bill-type/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_bill_type_book_bill_filter(self, farmId=None, bookId=None, budgetType=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'bookId': bookId,
                'budgetType': budgetType}
        response = self.request.post(url=self.url + '/web/farm-bill-type/book-bill-filter', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_bill_type_del(self, billTypeId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'billTypeId': billTypeId}
        response = self.request.post(url=self.url + '/web/farm-bill-type/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_bill_type_detail(self, billTypeId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'billTypeId': billTypeId}
        response = self.request.post(url=self.url + '/web/farm-bill-type/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_bill_type_list(self, farmId=None, budgetType=None, dataStatus=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'budgetType': budgetType, 'dataStatus': dataStatus}
        response = self.request.post(url=self.url + '/web/farm-bill-type/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_bill_add(self, farmId=None, bookId=None, budgetType=None, billTypeId=None, price=None, recordDate=None,
                          remark=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'bookId': bookId,
                'budgetType': budgetType, 'billTypeId': billTypeId, 'price': price, 'recordDate': recordDate,
                'remark': remark}
        response = self.request.post(url=self.url + '/web/farm-bill/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_bill_count_page_list(self, bookId=None, billTypeId=None, creatorId=None, pn=None, ps=None, farmId=None,
                                      startDate=None, endDate=None, budgetType=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'bookId': bookId,
                'billTypeId': billTypeId, 'creatorId': creatorId, 'pn': pn, 'ps': ps, 'farmId': farmId,
                'startDate': startDate, 'endDate': endDate, 'budgetType': budgetType}
        response = self.request.post(url=self.url + '/web/farm-bill/count-page-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_bill_del(self, billId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'billId': billId}
        response = self.request.post(url=self.url + '/web/farm-bill/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_bill_detail(self, billId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'billId': billId}
        response = self.request.post(url=self.url + '/web/farm-bill/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_bill_export(self):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id}
        response = self.request.get(url=self.url + '/web/farm-bill/export', params=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_bill_recorder_list(self, farmId=None, billTypeId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'billTypeId': billTypeId}
        response = self.request.post(url=self.url + '/web/farm-bill/recorder-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_bill_update(self, id=None, farmId=None, bookId=None, budgetType=None, billTypeId=None, price=None,
                             recordDate=None, remark=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'id': id, 'farmId': farmId,
                'bookId': bookId, 'budgetType': budgetType, 'billTypeId': billTypeId, 'price': price,
                'recordDate': recordDate, 'remark': remark}
        response = self.request.post(url=self.url + '/web/farm-bill/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_board_account_book_statistic(self, farmId=None, countType=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'countType': countType}
        response = self.request.post(url=self.url + '/web/farm-board/account-book-statistic', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_board_backlog(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/farm-board/backlog', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_board_cattle_alert_count(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/farm-board/cattle-alert-count', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_board_cattle_count(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/farm-board/cattle-count', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_board_cattle_tagged_count(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/farm-board/cattle-tagged-count', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_board_paddock_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/farm-board/paddock-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_board_right_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/farm-board/right-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_board_water_resource(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/farm-board/water-resource', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_board_weather(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/farm-board/weather', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_book_add(self, farmId=None, accountBookName=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'accountBookName': accountBookName}
        response = self.request.post(url=self.url + '/web/farm-book/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_book_del(self, bookId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'bookId': bookId}
        response = self.request.post(url=self.url + '/web/farm-book/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_book_detail(self, billTypeId=None, bookId=None, budgetType=None, startDate=None, endDate=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'billTypeId': billTypeId,
                'bookId': bookId, 'budgetType': budgetType, 'startDate': startDate, 'endDate': endDate}
        response = self.request.post(url=self.url + '/web/farm-book/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_book_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/farm-book/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_book_simple_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/farm-book/simple-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_book_statistic(self, farmId=None, countType=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'countType': countType}
        response = self.request.post(url=self.url + '/web/farm-book/statistic', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_book_update(self, farmId=None, accountBookId=None, accountBookName=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId,
                'accountBookId': accountBookId, 'accountBookName': accountBookName}
        response = self.request.post(url=self.url + '/web/farm-book/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_region_list(self, farmId=None, types=None, isNeedFilter=None, isNeedStoreNum=None,
                             isNeedNoPaddock=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'types': types,
                'isNeedFilter': isNeedFilter, 'isNeedStoreNum': isNeedStoreNum, 'isNeedNoPaddock': isNeedNoPaddock}
        response = self.request.post(url=self.url + '/web/farm-region/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_right_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/farm-right/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_signal_list(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/farm-signal/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_signal_rename(self, farmId=None, number=None, type=None, name=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'number': number,
                'type': type, 'name': name}
        response = self.request.post(url=self.url + '/web/farm-signal/rename', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_task_add(self, userIds=None, farmId=None, taskName=None, startTime=None, endTime=None,
                          description=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'userIds': userIds, 'farmId': farmId,
                'taskName': taskName, 'startTime': startTime, 'endTime': endTime, 'description': description}
        response = self.request.post(url=self.url + '/web/farm-task/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_task_del(self, taskId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'taskId': taskId}
        response = self.request.post(url=self.url + '/web/farm-task/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_task_detail(self, taskId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'taskId': taskId}
        response = self.request.post(url=self.url + '/web/farm-task/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_task_page_list(self, distributorIds=None, recipientIds=None, pn=None, ps=None, farmId=None,
                                status=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'distributorIds': distributorIds,
                'recipientIds': recipientIds, 'pn': pn, 'ps': ps, 'farmId': farmId, 'status': status}
        response = self.request.post(url=self.url + '/web/farm-task/page-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_task_update(self, userIds=None, id=None, farmId=None, taskName=None, startTime=None, endTime=None,
                             description=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'userIds': userIds, 'id': id,
                'farmId': farmId, 'taskName': taskName, 'startTime': startTime, 'endTime': endTime,
                'description': description}
        response = self.request.post(url=self.url + '/web/farm-task/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_task_update_status(self, taskId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'taskId': taskId}
        response = self.request.post(url=self.url + '/web/farm-task/update-status', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_task_user_list(self, farmId=None, type=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'type': type}
        response = self.request.post(url=self.url + '/web/farm-task/user-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_user_list_by_farm(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/farm-user/list-by-farm', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_add(self, name=None, postcodeId=None, address=None, pic=None, lng=None, lat=None, currencyType=None,
                     farmRightAddList=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'name': name, 'postcodeId': postcodeId,
                'address': address, 'pic': pic, 'lng': lng, 'lat': lat, 'currencyType': currencyType,
                'farmRightAddList': farmRightAddList}
        response = self.request.post(url=self.url + '/web/farm/add', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_del(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/farm/del', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_detail(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/farm/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_get_default(self):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id}
        response = self.request.post(url=self.url + '/web/farm/get-default', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_list(self):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id}
        response = self.request.post(url=self.url + '/web/farm/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_set_default(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/farm/set-default', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_farm_update(self, farmId=None, name=None, postcodeId=None, address=None, pic=None, lng=None, lat=None,
                        rightArea=None, type=None, rightNum=None, purchasePrice=None, farmRightUpdateList=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'name': name,
                'postcodeId': postcodeId, 'address': address, 'pic': pic, 'lng': lng, 'lat': lat,
                'rightArea': rightArea, 'type': type, 'rightNum': rightNum, 'purchasePrice': purchasePrice,
                'farmRightUpdateList': farmRightUpdateList}
        response = self.request.post(url=self.url + '/web/farm/update', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_landmark_detail(self, landmarkId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'landmarkId': landmarkId}
        response = self.request.post(url=self.url + '/web/landmark/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_landmark_list(self, farmId=None, types=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'types': types}
        response = self.request.post(url=self.url + '/web/landmark/list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_region_city_list(self, name=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'name': name}
        response = self.request.post(url=self.url + '/web/region/city-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_region_country_list(self, name=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'name': name}
        response = self.request.post(url=self.url + '/web/region/country-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_region_get_region_by_name(self, regionNames=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'regionNames': regionNames}
        response = self.request.post(url=self.url + '/web/region/get-region-by-name', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_region_province_city_list(self, name=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'name': name}
        response = self.request.post(url=self.url + '/web/region/province-city-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_region_province_list(self, name=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'name': name}
        response = self.request.post(url=self.url + '/web/region/province-list', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_share_detail(self, shareId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'shareId': shareId}
        response = self.request.post(url=self.url + '/web/share/detail', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_statistics_cattle_manage_count(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/statistics/cattle-manage-count', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_statistics_cattle_wait_mating_detail_count(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/statistics/cattle-wait-mating-detail-count', data=data,
                                     hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_user_invite_email_accept(self, token=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'token': token}
        response = self.request.post(url=self.url + '/web/user-invite/email-accept', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_user_invite_email_invite(self, farmId=None, email=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId, 'email': email}
        response = self.request.post(url=self.url + '/web/user-invite/email-invite', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_user_invite_email_invite_info(self, token=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'token': token}
        response = self.request.post(url=self.url + '/web/user-invite/email-invite-info', data=data, hosts=self.url)
        return json.loads(response)

    @judge_response_status
    def web_weather_home_rain(self, farmId=None):
        data = {'_tk_': self.koala.token, '_deviceId_': self.koala.device_id, 'farmId': farmId}
        response = self.request.post(url=self.url + '/web/weather/home-rain', data=data, hosts=self.url)
        return json.loads(response)
