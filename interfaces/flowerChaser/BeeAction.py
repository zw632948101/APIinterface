#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
import json


class BeeAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('FC_BEE')

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

    def _admin_bee_friend_add(self, curNectarType_=None, labelType_=None, regularSource_=None, intention_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, vehicleLength_=None, expectHiveNum_=None, pics_=None, scale_=None, hiveNum_=None, standardNum_=None, smallNum_=None, queenType_=None, queenNum2_=None, queenNum1_=None, queenNum_=None, ekeNum_=None, platNum_=None, babyNum_=None, honeyNum_=None, remark_=None, nextNectarSource_=None, nextSourceEnterTime_=None, joinDate_=None, leaveDate_=None, contactNumber_=None, realName_=None, age_=None, gender_=None, nativeProvince_=None, nativeCity_=None, nativeCounty_=None, seniority_=None, regularRoute_=None, studyFrom_=None, heir_=None, yield_=None, income_=None, breedTime1_=None, breedPlace1_=None, breedTime2_=None, breedPlace2_=None, saleNum_=None, intentionPrice_=None, saleTime_=None, saleProvince_=None, saleCity_=None, saleCounty_=None, altitude_=None, distantPic_=None, tentPic_=None, sitePic_=None, roadPic_=None):
        if self.user is None:
            data = {'curNectarType': curNectarType_, 'labelType': labelType_, 'regularSource': regularSource_, 'intention': intention_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'vehicleLength': vehicleLength_, 'expectHiveNum': expectHiveNum_, 'pics': pics_, 'scale': scale_, 'hiveNum': hiveNum_, 'standardNum': standardNum_, 'smallNum': smallNum_, 'queenType': queenType_, 'queenNum2': queenNum2_, 'queenNum1': queenNum1_, 'queenNum': queenNum_, 'ekeNum': ekeNum_, 'platNum': platNum_, 'babyNum': babyNum_, 'honeyNum': honeyNum_, 'remark': remark_, 'nextNectarSource': nextNectarSource_, 'nextSourceEnterTime': nextSourceEnterTime_, 'joinDate': joinDate_, 'leaveDate': leaveDate_, 'contactNumber': contactNumber_, 'realName': realName_, 'age': age_, 'gender': gender_, 'nativeProvince': nativeProvince_, 'nativeCity': nativeCity_, 'nativeCounty': nativeCounty_, 'seniority': seniority_, 'regularRoute': regularRoute_, 'studyFrom': studyFrom_, 'heir': heir_, 'yield': yield_, 'income': income_, 'breedTime1': breedTime1_, 'breedPlace1': breedPlace1_, 'breedTime2': breedTime2_, 'breedPlace2': breedPlace2_, 'saleNum': saleNum_, 'intentionPrice': intentionPrice_, 'saleTime': saleTime_, 'saleProvince': saleProvince_, 'saleCity': saleCity_, 'saleCounty': saleCounty_, 'altitude': altitude_, 'distantPic': distantPic_, 'tentPic': tentPic_, 'sitePic': sitePic_, 'roadPic': roadPic_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'curNectarType': curNectarType_, 'labelType': labelType_, 'regularSource': regularSource_, 'intention': intention_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'vehicleLength': vehicleLength_, 'expectHiveNum': expectHiveNum_, 'pics': pics_, 'scale': scale_, 'hiveNum': hiveNum_, 'standardNum': standardNum_, 'smallNum': smallNum_, 'queenType': queenType_, 'queenNum2': queenNum2_, 'queenNum1': queenNum1_, 'queenNum': queenNum_, 'ekeNum': ekeNum_, 'platNum': platNum_, 'babyNum': babyNum_, 'honeyNum': honeyNum_, 'remark': remark_, 'nextNectarSource': nextNectarSource_, 'nextSourceEnterTime': nextSourceEnterTime_, 'joinDate': joinDate_, 'leaveDate': leaveDate_, 'contactNumber': contactNumber_, 'realName': realName_, 'age': age_, 'gender': gender_, 'nativeProvince': nativeProvince_, 'nativeCity': nativeCity_, 'nativeCounty': nativeCounty_, 'seniority': seniority_, 'regularRoute': regularRoute_, 'studyFrom': studyFrom_, 'heir': heir_, 'yield': yield_, 'income': income_, 'breedTime1': breedTime1_, 'breedPlace1': breedPlace1_, 'breedTime2': breedTime2_, 'breedPlace2': breedPlace2_, 'saleNum': saleNum_, 'intentionPrice': intentionPrice_, 'saleTime': saleTime_, 'saleProvince': saleProvince_, 'saleCity': saleCity_, 'saleCounty': saleCounty_, 'altitude': altitude_, 'distantPic': distantPic_, 'tentPic': tentPic_, 'sitePic': sitePic_, 'roadPic': roadPic_}
        response = self.request.post(url=self.url+'/admin/bee-friend/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_friend_add_check(self, userId_=None, mobile_=None):
        if self.user is None:
            data = {'userId': userId_, 'mobile': mobile_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_, 'mobile': mobile_}
        response = self.request.post(url=self.url+'/admin/bee-friend/add-check', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_friend_charge_man_list(self, searchKey_=None):
        if self.user is None:
            data = {'searchKey': searchKey_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'searchKey': searchKey_}
        response = self.request.post(url=self.url+'/admin/bee-friend/charge-man-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_friend_delete(self, id_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'id': id_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/admin/bee-friend/delete', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_friend_detail(self, id_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'id': id_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/admin/bee-friend/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_friend_edit(self, regularSource_=None, labelType_=None, intention_=None, id_=None, realName_=None, contactNumber_=None, gender_=None, nativeProvince_=None, nativeCity_=None, nativeCounty_=None, age_=None, seniority_=None, regularRoute_=None, studyFrom_=None, heir_=None, yield_=None, income_=None, breedTime1_=None, breedPlace1_=None, breedTime2_=None, breedPlace2_=None, saleNum_=None, intentionPrice_=None, saleTime_=None, saleProvince_=None, saleCity_=None, saleCounty_=None):
        if self.user is None:
            data = {'regularSource': regularSource_, 'labelType': labelType_, 'intention': intention_, 'id': id_, 'realName': realName_, 'contactNumber': contactNumber_, 'gender': gender_, 'nativeProvince': nativeProvince_, 'nativeCity': nativeCity_, 'nativeCounty': nativeCounty_, 'age': age_, 'seniority': seniority_, 'regularRoute': regularRoute_, 'studyFrom': studyFrom_, 'heir': heir_, 'yield': yield_, 'income': income_, 'breedTime1': breedTime1_, 'breedPlace1': breedPlace1_, 'breedTime2': breedTime2_, 'breedPlace2': breedPlace2_, 'saleNum': saleNum_, 'intentionPrice': intentionPrice_, 'saleTime': saleTime_, 'saleProvince': saleProvince_, 'saleCity': saleCity_, 'saleCounty': saleCounty_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'regularSource': regularSource_, 'labelType': labelType_, 'intention': intention_, 'id': id_, 'realName': realName_, 'contactNumber': contactNumber_, 'gender': gender_, 'nativeProvince': nativeProvince_, 'nativeCity': nativeCity_, 'nativeCounty': nativeCounty_, 'age': age_, 'seniority': seniority_, 'regularRoute': regularRoute_, 'studyFrom': studyFrom_, 'heir': heir_, 'yield': yield_, 'income': income_, 'breedTime1': breedTime1_, 'breedPlace1': breedPlace1_, 'breedTime2': breedTime2_, 'breedPlace2': breedPlace2_, 'saleNum': saleNum_, 'intentionPrice': intentionPrice_, 'saleTime': saleTime_, 'saleProvince': saleProvince_, 'saleCity': saleCity_, 'saleCounty': saleCounty_}
        response = self.request.post(url=self.url+'/admin/bee-friend/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_friend_friend_add(self, labelType_=None, regularSource_=None, intention_=None, contactNumber_=None, realName_=None, age_=None, gender_=None, nativeProvince_=None, nativeCity_=None, nativeCounty_=None, seniority_=None, regularRoute_=None, studyFrom_=None, heir_=None, yield_=None, income_=None, breedTime1_=None, breedPlace1_=None, breedTime2_=None, breedPlace2_=None, saleNum_=None, intentionPrice_=None, saleTime_=None, saleProvince_=None, saleCity_=None, saleCounty_=None):
        if self.user is None:
            data = {'labelType': labelType_, 'regularSource': regularSource_, 'intention': intention_, 'contactNumber': contactNumber_, 'realName': realName_, 'age': age_, 'gender': gender_, 'nativeProvince': nativeProvince_, 'nativeCity': nativeCity_, 'nativeCounty': nativeCounty_, 'seniority': seniority_, 'regularRoute': regularRoute_, 'studyFrom': studyFrom_, 'heir': heir_, 'yield': yield_, 'income': income_, 'breedTime1': breedTime1_, 'breedPlace1': breedPlace1_, 'breedTime2': breedTime2_, 'breedPlace2': breedPlace2_, 'saleNum': saleNum_, 'intentionPrice': intentionPrice_, 'saleTime': saleTime_, 'saleProvince': saleProvince_, 'saleCity': saleCity_, 'saleCounty': saleCounty_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'labelType': labelType_, 'regularSource': regularSource_, 'intention': intention_, 'contactNumber': contactNumber_, 'realName': realName_, 'age': age_, 'gender': gender_, 'nativeProvince': nativeProvince_, 'nativeCity': nativeCity_, 'nativeCounty': nativeCounty_, 'seniority': seniority_, 'regularRoute': regularRoute_, 'studyFrom': studyFrom_, 'heir': heir_, 'yield': yield_, 'income': income_, 'breedTime1': breedTime1_, 'breedPlace1': breedPlace1_, 'breedTime2': breedTime2_, 'breedPlace2': breedPlace2_, 'saleNum': saleNum_, 'intentionPrice': intentionPrice_, 'saleTime': saleTime_, 'saleProvince': saleProvince_, 'saleCity': saleCity_, 'saleCounty': saleCounty_}
        response = self.request.post(url=self.url+'/admin/bee-friend/friend-add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_friend_mobile_check(self, userId_=None, mobile_=None):
        if self.user is None:
            data = {'userId': userId_, 'mobile': mobile_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_, 'mobile': mobile_}
        response = self.request.post(url=self.url+'/admin/bee-friend/mobile-check', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_friend_normal_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/bee-friend/normal-count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_friend_operator_list(self, searchKey_=None):
        if self.user is None:
            data = {'searchKey': searchKey_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'searchKey': searchKey_}
        response = self.request.post(url=self.url+'/admin/bee-friend/operator-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_friend_own_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/bee-friend/own-count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_friend_own_list(self, pn_=None, ps_=None, searchKey_=None, province_=None, city_=None, county_=None, roleCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'province': province_, 'city': city_, 'county': county_, 'roleCode': roleCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'province': province_, 'city': city_, 'county': county_, 'roleCode': roleCode_}
        response = self.request.post(url=self.url+'/admin/bee-friend/own-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_friend_page_list(self, businessLabels_=None, swarmNums_=None, pn_=None, ps_=None, searchKey_=None, province_=None, city_=None, county_=None, collectTimeStart_=None, collectTimeEnd_=None, collector_=None, locOrderType_=None, ctOrderType_=None, registed_=None):
        if self.user is None:
            data = {'businessLabels': businessLabels_, 'swarmNums': swarmNums_, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'province': province_, 'city': city_, 'county': county_, 'collectTimeStart': collectTimeStart_, 'collectTimeEnd': collectTimeEnd_, 'collector': collector_, 'locOrderType': locOrderType_, 'ctOrderType': ctOrderType_, 'registed': registed_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'businessLabels': businessLabels_, 'swarmNums': swarmNums_, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'province': province_, 'city': city_, 'county': county_, 'collectTimeStart': collectTimeStart_, 'collectTimeEnd': collectTimeEnd_, 'collector': collector_, 'locOrderType': locOrderType_, 'ctOrderType': ctOrderType_, 'registed': registed_}
        response = self.request.post(url=self.url+'/admin/bee-friend/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_reserve_add(self, reserveName_=None, address_=None, lng_=None, lat_=None, addrProvince_=None, addrCity_=None, addrCounty_=None, province_=None, city_=None, county_=None, nectarType_=None, vehicleLength_=None, reserveArea_=None, altitude_=None, manager_=None, contact_=None, remark_=None, attaches_=None):
        if self.user is None:
            data = {'reserveName': reserveName_, 'address': address_, 'lng': lng_, 'lat': lat_, 'addrProvince': addrProvince_, 'addrCity': addrCity_, 'addrCounty': addrCounty_, 'province': province_, 'city': city_, 'county': county_, 'nectarType': nectarType_, 'vehicleLength': vehicleLength_, 'reserveArea': reserveArea_, 'altitude': altitude_, 'manager': manager_, 'contact': contact_, 'remark': remark_, 'attaches': attaches_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'reserveName': reserveName_, 'address': address_, 'lng': lng_, 'lat': lat_, 'addrProvince': addrProvince_, 'addrCity': addrCity_, 'addrCounty': addrCounty_, 'province': province_, 'city': city_, 'county': county_, 'nectarType': nectarType_, 'vehicleLength': vehicleLength_, 'reserveArea': reserveArea_, 'altitude': altitude_, 'manager': manager_, 'contact': contact_, 'remark': remark_, 'attaches': attaches_}
        response = self.request.post(url=self.url+'/admin/bee-reserve/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_reserve_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/bee-reserve/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_reserve_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/bee-reserve/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_reserve_edit(self, id_=None, reserveName_=None, address_=None, lng_=None, lat_=None, addrProvince_=None, addrCity_=None, addrCounty_=None, province_=None, city_=None, county_=None, nectarType_=None, vehicleLength_=None, reserveArea_=None, altitude_=None, manager_=None, contact_=None, remark_=None, attaches_=None):
        if self.user is None:
            data = {'id': id_, 'reserveName': reserveName_, 'address': address_, 'lng': lng_, 'lat': lat_, 'addrProvince': addrProvince_, 'addrCity': addrCity_, 'addrCounty': addrCounty_, 'province': province_, 'city': city_, 'county': county_, 'nectarType': nectarType_, 'vehicleLength': vehicleLength_, 'reserveArea': reserveArea_, 'altitude': altitude_, 'manager': manager_, 'contact': contact_, 'remark': remark_, 'attaches': attaches_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'reserveName': reserveName_, 'address': address_, 'lng': lng_, 'lat': lat_, 'addrProvince': addrProvince_, 'addrCity': addrCity_, 'addrCounty': addrCounty_, 'province': province_, 'city': city_, 'county': county_, 'nectarType': nectarType_, 'vehicleLength': vehicleLength_, 'reserveArea': reserveArea_, 'altitude': altitude_, 'manager': manager_, 'contact': contact_, 'remark': remark_, 'attaches': attaches_}
        response = self.request.post(url=self.url+'/admin/bee-reserve/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_reserve_page_list(self, pn_=None, ps_=None, reserveName_=None, nectarType_=None, creator_=None, gatherTimeStart_=None, gatherTimeEnd_=None, province_=None, city_=None, county_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'reserveName': reserveName_, 'nectarType': nectarType_, 'creator': creator_, 'gatherTimeStart': gatherTimeStart_, 'gatherTimeEnd': gatherTimeEnd_, 'province': province_, 'city': city_, 'county': county_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'reserveName': reserveName_, 'nectarType': nectarType_, 'creator': creator_, 'gatherTimeStart': gatherTimeStart_, 'gatherTimeEnd': gatherTimeEnd_, 'province': province_, 'city': city_, 'county': county_}
        response = self.request.post(url=self.url+'/admin/bee-reserve/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_bee_reserve_statistics(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/bee-reserve/statistics', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_config_close_nearby(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/config/close-nearby', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_config_edit(self, code_=None, key_=None, value_=None, valueEn_=None, parentKey_=None, level_=None, conCode_=None, remark_=None, remarkEn_=None, icon_=None, description_=None, order_=None):
        if self.user is None:
            data = {'code': code_, 'key': key_, 'value': value_, 'valueEn': valueEn_, 'parentKey': parentKey_, 'level': level_, 'conCode': conCode_, 'remark': remark_, 'remarkEn': remarkEn_, 'icon': icon_, 'description': description_, 'order': order_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_, 'key': key_, 'value': value_, 'valueEn': valueEn_, 'parentKey': parentKey_, 'level': level_, 'conCode': conCode_, 'remark': remark_, 'remarkEn': remarkEn_, 'icon': icon_, 'description': description_, 'order': order_}
        response = self.request.post(url=self.url+'/admin/config/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_config_open_nearby(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/config/open-nearby', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_config_redis_del(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/config/redis-del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_contract_page_list(self, pn_=None, ps_=None, userId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'userId': userId_}
        response = self.request.post(url=self.url+'/admin/contract/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_enter_enter_check(self, containerIds_=None, nectarSourceId_=None):
        if self.user is None:
            data = {'containerIds': containerIds_, 'nectarSourceId': nectarSourceId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'containerIds': containerIds_, 'nectarSourceId': nectarSourceId_}
        response = self.request.post(url=self.url+'/admin/enter/enter-check', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_enter_enter_save(self, containerIds_=None, nectarSourceId_=None, enterTime_=None, hiveNum_=None):
        if self.user is None:
            data = {'containerIds': containerIds_, 'nectarSourceId': nectarSourceId_, 'enterTime': enterTime_, 'hiveNum': hiveNum_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'containerIds': containerIds_, 'nectarSourceId': nectarSourceId_, 'enterTime': enterTime_, 'hiveNum': hiveNum_}
        response = self.request.post(url=self.url+'/admin/enter/enter-save', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_enter_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/enter/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_bee_friend(self, businessLabels_=None, swarmNums_=None, pn_=None, ps_=None, searchKey_=None, province_=None, city_=None, county_=None, collectTimeStart_=None, collectTimeEnd_=None, collector_=None, locOrderType_=None, ctOrderType_=None, registed_=None):
        if self.user is None:
            data = {'businessLabels': businessLabels_, 'swarmNums': swarmNums_, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'province': province_, 'city': city_, 'county': county_, 'collectTimeStart': collectTimeStart_, 'collectTimeEnd': collectTimeEnd_, 'collector': collector_, 'locOrderType': locOrderType_, 'ctOrderType': ctOrderType_, 'registed': registed_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'businessLabels': businessLabels_, 'swarmNums': swarmNums_, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'province': province_, 'city': city_, 'county': county_, 'collectTimeStart': collectTimeStart_, 'collectTimeEnd': collectTimeEnd_, 'collector': collector_, 'locOrderType': locOrderType_, 'ctOrderType': ctOrderType_, 'registed': registed_}
        response = self.request.get(url=self.url+'/admin/excel-export/bee-friend', params=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_nectar_source(self, excludeStatus_=None, includeStatus_=None, includeProvince_=None, includeCity_=None, includeType_=None, pn_=None, ps_=None, searchType_=None, province_=None, city_=None, county_=None, lng_=None, lat_=None, distanceType_=None, searchName_=None, searchFlowerStart_=None, searchFlowerEnd_=None, collectTimeStart_=None, collectTimeEnd_=None, collector_=None, vehicleLength_=None, ctOrderType_=None, isEnter_=None):
        if self.user is None:
            data = {'excludeStatus': excludeStatus_, 'includeStatus': includeStatus_, 'includeProvince': includeProvince_, 'includeCity': includeCity_, 'includeType': includeType_, 'pn': pn_, 'ps': ps_, 'searchType': searchType_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'distanceType': distanceType_, 'searchName': searchName_, 'searchFlowerStart': searchFlowerStart_, 'searchFlowerEnd': searchFlowerEnd_, 'collectTimeStart': collectTimeStart_, 'collectTimeEnd': collectTimeEnd_, 'collector': collector_, 'vehicleLength': vehicleLength_, 'ctOrderType': ctOrderType_, 'isEnter': isEnter_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'excludeStatus': excludeStatus_, 'includeStatus': includeStatus_, 'includeProvince': includeProvince_, 'includeCity': includeCity_, 'includeType': includeType_, 'pn': pn_, 'ps': ps_, 'searchType': searchType_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'distanceType': distanceType_, 'searchName': searchName_, 'searchFlowerStart': searchFlowerStart_, 'searchFlowerEnd': searchFlowerEnd_, 'collectTimeStart': collectTimeStart_, 'collectTimeEnd': collectTimeEnd_, 'collector': collector_, 'vehicleLength': vehicleLength_, 'ctOrderType': ctOrderType_, 'isEnter': isEnter_}
        response = self.request.get(url=self.url+'/admin/excel-export/nectar-source', params=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_own_friend(self, pn_=None, ps_=None, searchKey_=None, province_=None, city_=None, county_=None, roleCode_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'province': province_, 'city': city_, 'county': county_, 'roleCode': roleCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'province': province_, 'city': city_, 'county': county_, 'roleCode': roleCode_}
        response = self.request.get(url=self.url+'/admin/excel-export/own-friend', params=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_reserve(self, pn_=None, ps_=None, reserveName_=None, nectarType_=None, creator_=None, gatherTimeStart_=None, gatherTimeEnd_=None, province_=None, city_=None, county_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'reserveName': reserveName_, 'nectarType': nectarType_, 'creator': creator_, 'gatherTimeStart': gatherTimeStart_, 'gatherTimeEnd': gatherTimeEnd_, 'province': province_, 'city': city_, 'county': county_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'reserveName': reserveName_, 'nectarType': nectarType_, 'creator': creator_, 'gatherTimeStart': gatherTimeStart_, 'gatherTimeEnd': gatherTimeEnd_, 'province': province_, 'city': city_, 'county': county_}
        response = self.request.get(url=self.url+'/admin/excel-export/reserve', params=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_shunt(self, pn_=None, ps_=None, issuer_=None, shuntStatus_=None, startCreateTime_=None, endCreateTime_=None, startUseTime_=None, endUseTime_=None, createTimeSort_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'issuer': issuer_, 'shuntStatus': shuntStatus_, 'startCreateTime': startCreateTime_, 'endCreateTime': endCreateTime_, 'startUseTime': startUseTime_, 'endUseTime': endUseTime_, 'createTimeSort': createTimeSort_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'issuer': issuer_, 'shuntStatus': shuntStatus_, 'startCreateTime': startCreateTime_, 'endCreateTime': endCreateTime_, 'startUseTime': startUseTime_, 'endUseTime': endUseTime_, 'createTimeSort': createTimeSort_}
        response = self.request.get(url=self.url+'/admin/excel-export/shunt', params=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_swarm(self, vehicleLength_=None, curNectarType_=None, pn_=None, ps_=None, searchKey_=None, province_=None, city_=None, county_=None, collectTimeStart_=None, collectTimeEnd_=None, collector_=None, ctOrderType_=None, hiveNumMin_=None, hiveNumMax_=None, repeat_=None):
        if self.user is None:
            data = {'vehicleLength': vehicleLength_, 'curNectarType': curNectarType_, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'province': province_, 'city': city_, 'county': county_, 'collectTimeStart': collectTimeStart_, 'collectTimeEnd': collectTimeEnd_, 'collector': collector_, 'ctOrderType': ctOrderType_, 'hiveNumMin': hiveNumMin_, 'hiveNumMax': hiveNumMax_, 'repeat': repeat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'vehicleLength': vehicleLength_, 'curNectarType': curNectarType_, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'province': province_, 'city': city_, 'county': county_, 'collectTimeStart': collectTimeStart_, 'collectTimeEnd': collectTimeEnd_, 'collector': collector_, 'ctOrderType': ctOrderType_, 'hiveNumMin': hiveNumMin_, 'hiveNumMax': hiveNumMax_, 'repeat': repeat_}
        response = self.request.get(url=self.url+'/admin/excel-export/swarm', params=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_excel_export_user(self, pn_=None, ps_=None, roleType_=None, role_=None, userInfo_=None, userStatus_=None, rgStartTime_=None, rgEndTime_=None, rgOrderType_=None, loStartTime_=None, loEndTime_=None, loOrderType_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'roleType': roleType_, 'role': role_, 'userInfo': userInfo_, 'userStatus': userStatus_, 'rgStartTime': rgStartTime_, 'rgEndTime': rgEndTime_, 'rgOrderType': rgOrderType_, 'loStartTime': loStartTime_, 'loEndTime': loEndTime_, 'loOrderType': loOrderType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'roleType': roleType_, 'role': role_, 'userInfo': userInfo_, 'userStatus': userStatus_, 'rgStartTime': rgStartTime_, 'rgEndTime': rgEndTime_, 'rgOrderType': rgOrderType_, 'loStartTime': loStartTime_, 'loEndTime': loEndTime_, 'loOrderType': loOrderType_}
        response = self.request.get(url=self.url+'/admin/excel-export/user', params=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_fc_user_current_info(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/fc-user/current-info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_fc_user_detail(self, userId_=None):
        if self.user is None:
            data = {'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_}
        response = self.request.post(url=self.url+'/admin/fc-user/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_fc_user_edit(self, userId_=None, realName_=None, scale_=None, seniority_=None, nativeProvince_=None, nativeCity_=None, nativeCounty_=None, age_=None, gender_=None):
        if self.user is None:
            data = {'userId': userId_, 'realName': realName_, 'scale': scale_, 'seniority': seniority_, 'nativeProvince': nativeProvince_, 'nativeCity': nativeCity_, 'nativeCounty': nativeCounty_, 'age': age_, 'gender': gender_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_, 'realName': realName_, 'scale': scale_, 'seniority': seniority_, 'nativeProvince': nativeProvince_, 'nativeCity': nativeCity_, 'nativeCounty': nativeCounty_, 'age': age_, 'gender': gender_}
        response = self.request.post(url=self.url+'/admin/fc-user/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_fc_user_freeze(self, userId_=None, status_=None):
        if self.user is None:
            data = {'userId': userId_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/fc-user/freeze', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_fc_user_info(self, userId_=None):
        if self.user is None:
            data = {'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_}
        response = self.request.post(url=self.url+'/admin/fc-user/info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_fc_user_log_list(self, userId_=None):
        if self.user is None:
            data = {'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_}
        response = self.request.post(url=self.url+'/admin/fc-user/log/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_fc_user_log_page_list(self, pn_=None, ps_=None, userId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'userId': userId_}
        response = self.request.post(url=self.url+'/admin/fc-user/log/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_fc_user_page_list(self, pn_=None, ps_=None, roleType_=None, role_=None, userInfo_=None, userStatus_=None, rgStartTime_=None, rgEndTime_=None, rgOrderType_=None, loStartTime_=None, loEndTime_=None, loOrderType_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'roleType': roleType_, 'role': role_, 'userInfo': userInfo_, 'userStatus': userStatus_, 'rgStartTime': rgStartTime_, 'rgEndTime': rgEndTime_, 'rgOrderType': rgOrderType_, 'loStartTime': loStartTime_, 'loEndTime': loEndTime_, 'loOrderType': loOrderType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'roleType': roleType_, 'role': role_, 'userInfo': userInfo_, 'userStatus': userStatus_, 'rgStartTime': rgStartTime_, 'rgEndTime': rgEndTime_, 'rgOrderType': rgOrderType_, 'loStartTime': loStartTime_, 'loEndTime': loEndTime_, 'loOrderType': loOrderType_}
        response = self.request.post(url=self.url+'/admin/fc-user/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_fc_user_permission_check(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/fc-user/permission-check', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_fc_user_role(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/fc-user/role', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_fc_user_role_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/fc-user/role-count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_fc_user_set_role(self, userId_=None, key_=None, joinDate_=None):
        if self.user is None:
            data = {'userId': userId_, 'key': key_, 'joinDate': joinDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_, 'key': key_, 'joinDate': joinDate_}
        response = self.request.post(url=self.url+'/admin/fc-user/set-role', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_help_comment_del(self, helpCommentId_=None):
        if self.user is None:
            data = {'helpCommentId': helpCommentId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'helpCommentId': helpCommentId_}
        response = self.request.post(url=self.url+'/admin/help-comment/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_help_comment_list(self, pn_=None, ps_=None, helpInfoId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'helpInfoId': helpInfoId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'helpInfoId': helpInfoId_}
        response = self.request.post(url=self.url+'/admin/help-comment/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_help_info_close(self, helpInfoId_=None):
        if self.user is None:
            data = {'helpInfoId': helpInfoId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'helpInfoId': helpInfoId_}
        response = self.request.post(url=self.url+'/admin/help-info/close', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_help_info_del(self, helpInfoId_=None, reasonType_=None):
        if self.user is None:
            data = {'helpInfoId': helpInfoId_, 'reasonType': reasonType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'helpInfoId': helpInfoId_, 'reasonType': reasonType_}
        response = self.request.post(url=self.url+'/admin/help-info/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_help_info_detail(self, helpInfoId_=None, lng_=None, lat_=None, readStatus_=None):
        if self.user is None:
            data = {'helpInfoId': helpInfoId_, 'lng': lng_, 'lat': lat_, 'readStatus': readStatus_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'helpInfoId': helpInfoId_, 'lng': lng_, 'lat': lat_, 'readStatus': readStatus_}
        response = self.request.post(url=self.url+'/admin/help-info/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_help_info_list(self, types_=None, pn_=None, ps_=None, province_=None, city_=None, county_=None, startTime_=None, endTime_=None, magicStatus_=None, userSearch_=None, createTimeOrderType_=None):
        if self.user is None:
            data = {'types': types_, 'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'magicStatus': magicStatus_, 'userSearch': userSearch_, 'createTimeOrderType': createTimeOrderType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'types': types_, 'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'magicStatus': magicStatus_, 'userSearch': userSearch_, 'createTimeOrderType': createTimeOrderType_}
        response = self.request.post(url=self.url+'/admin/help-info/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_help_info_mock_add(self, type_=None, content_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, images_=None, phone_=None, createTime_=None):
        if self.user is None:
            data = {'type': type_, 'content': content_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'images': images_, 'phone': phone_, 'createTime': createTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'type': type_, 'content': content_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'images': images_, 'phone': phone_, 'createTime': createTime_}
        response = self.request.post(url=self.url+'/admin/help-info/mock-add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_help_info_total(self, pn_=None, ps_=None, type_=None, province_=None, city_=None, county_=None, queryDistance_=None, locationLng_=None, locationLat_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'type': type_, 'province': province_, 'city': city_, 'county': county_, 'queryDistance': queryDistance_, 'locationLng': locationLng_, 'locationLat': locationLat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'type': type_, 'province': province_, 'city': city_, 'county': county_, 'queryDistance': queryDistance_, 'locationLng': locationLng_, 'locationLat': locationLat_}
        response = self.request.post(url=self.url+'/admin/help-info/total', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_help_info_update_theme(self, helpInfoId_=None, type_=None):
        if self.user is None:
            data = {'helpInfoId': helpInfoId_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'helpInfoId': helpInfoId_, 'type': type_}
        response = self.request.post(url=self.url+'/admin/help-info/update-theme', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_help_operate_log_list(self, helpInfoId_=None):
        if self.user is None:
            data = {'helpInfoId': helpInfoId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'helpInfoId': helpInfoId_}
        response = self.request.post(url=self.url+'/admin/help-operate-log/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_hot_nectar_source_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/hot-nectar-source/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_index_position_data(self, dataTypes_=None, stDate_=None, edDate_=None, vehicle_=None, stHiveNum_=None, edHiveNum_=None, nectarType_=None, provinces_=None, cities_=None, counties_=None, address_=None):
        if self.user is None:
            data = {'dataTypes': dataTypes_, 'stDate': stDate_, 'edDate': edDate_, 'vehicle': vehicle_, 'stHiveNum': stHiveNum_, 'edHiveNum': edHiveNum_, 'nectarType': nectarType_, 'provinces': provinces_, 'cities': cities_, 'counties': counties_, 'address': address_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'dataTypes': dataTypes_, 'stDate': stDate_, 'edDate': edDate_, 'vehicle': vehicle_, 'stHiveNum': stHiveNum_, 'edHiveNum': edHiveNum_, 'nectarType': nectarType_, 'provinces': provinces_, 'cities': cities_, 'counties': counties_, 'address': address_}
        response = self.request.post(url=self.url+'/admin/index/position-data', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_index_swarm_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/index/swarm-count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_index_swarm_data(self, swarmId_=None, dataType_=None):
        if self.user is None:
            data = {'swarmId': swarmId_, 'dataType': dataType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'swarmId': swarmId_, 'dataType': dataType_}
        response = self.request.post(url=self.url+'/admin/index/swarm-data', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_plant_add(self, plantName_=None, type_=None, variety_=None, alias_=None, region_=None, area_=None, floweringDescription_=None, nectarFlowCondition_=None, powderType_=None, minHoneyYield_=None, maxHoneyYield_=None, codeIcon_=None, mapIcon_=None, remark_=None):
        if self.user is None:
            data = {'plantName': plantName_, 'type': type_, 'variety': variety_, 'alias': alias_, 'region': region_, 'area': area_, 'floweringDescription': floweringDescription_, 'nectarFlowCondition': nectarFlowCondition_, 'powderType': powderType_, 'minHoneyYield': minHoneyYield_, 'maxHoneyYield': maxHoneyYield_, 'codeIcon': codeIcon_, 'mapIcon': mapIcon_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'plantName': plantName_, 'type': type_, 'variety': variety_, 'alias': alias_, 'region': region_, 'area': area_, 'floweringDescription': floweringDescription_, 'nectarFlowCondition': nectarFlowCondition_, 'powderType': powderType_, 'minHoneyYield': minHoneyYield_, 'maxHoneyYield': maxHoneyYield_, 'codeIcon': codeIcon_, 'mapIcon': mapIcon_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/nectar-source-plant/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_plant_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/nectar-source-plant/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_plant_edit(self, plantName_=None, type_=None, variety_=None, alias_=None, region_=None, area_=None, floweringDescription_=None, nectarFlowCondition_=None, powderType_=None, minHoneyYield_=None, maxHoneyYield_=None, codeIcon_=None, mapIcon_=None, remark_=None, id_=None):
        if self.user is None:
            data = {'plantName': plantName_, 'type': type_, 'variety': variety_, 'alias': alias_, 'region': region_, 'area': area_, 'floweringDescription': floweringDescription_, 'nectarFlowCondition': nectarFlowCondition_, 'powderType': powderType_, 'minHoneyYield': minHoneyYield_, 'maxHoneyYield': maxHoneyYield_, 'codeIcon': codeIcon_, 'mapIcon': mapIcon_, 'remark': remark_, 'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'plantName': plantName_, 'type': type_, 'variety': variety_, 'alias': alias_, 'region': region_, 'area': area_, 'floweringDescription': floweringDescription_, 'nectarFlowCondition': nectarFlowCondition_, 'powderType': powderType_, 'minHoneyYield': minHoneyYield_, 'maxHoneyYield': maxHoneyYield_, 'codeIcon': codeIcon_, 'mapIcon': mapIcon_, 'remark': remark_, 'id': id_}
        response = self.request.post(url=self.url+'/admin/nectar-source-plant/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_plant_list(self, pn_=None, ps_=None, type_=None, powderType_=None, name_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'type': type_, 'powderType': powderType_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'type': type_, 'powderType': powderType_, 'name': name_}
        response = self.request.post(url=self.url+'/admin/nectar-source-plant/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_point_add(self, province_=None, city_=None, county_=None, lng_=None, lat_=None, plantCode_=None, floweringStartDate_=None, nectarFlow_=None, nectarSourceArea_=None, apiaryDensity_=None, entryDate_=None, departureDate_=None, purpose_=None, secondPlantCode_=None, pesticideCondition_=None, mainIntensively_=None, remark_=None, nectarSourceFlowInputs_=None, nectarSourcePointAttachInputs_=None):
        if self.user is None:
            data = {'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'plantCode': plantCode_, 'floweringStartDate': floweringStartDate_, 'nectarFlow': nectarFlow_, 'nectarSourceArea': nectarSourceArea_, 'apiaryDensity': apiaryDensity_, 'entryDate': entryDate_, 'departureDate': departureDate_, 'purpose': purpose_, 'secondPlantCode': secondPlantCode_, 'pesticideCondition': pesticideCondition_, 'mainIntensively': mainIntensively_, 'remark': remark_, 'nectarSourceFlowInputs': nectarSourceFlowInputs_, 'nectarSourcePointAttachInputs': nectarSourcePointAttachInputs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'plantCode': plantCode_, 'floweringStartDate': floweringStartDate_, 'nectarFlow': nectarFlow_, 'nectarSourceArea': nectarSourceArea_, 'apiaryDensity': apiaryDensity_, 'entryDate': entryDate_, 'departureDate': departureDate_, 'purpose': purpose_, 'secondPlantCode': secondPlantCode_, 'pesticideCondition': pesticideCondition_, 'mainIntensively': mainIntensively_, 'remark': remark_, 'nectarSourceFlowInputs': nectarSourceFlowInputs_, 'nectarSourcePointAttachInputs': nectarSourcePointAttachInputs_}
        response = self.request.post(url=self.url+'/admin/nectar-source-point/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_point_attach_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/nectar-source-point/attach/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_point_attach_list(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/nectar-source-point/attach/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_point_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/nectar-source-point/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_point_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/nectar-source-point/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_point_edit(self, id_=None, province_=None, city_=None, county_=None, lng_=None, lat_=None, plantCode_=None, floweringStartDate_=None, nectarFlow_=None, nectarSourceArea_=None, apiaryDensity_=None, entryDate_=None, departureDate_=None, purpose_=None, secondPlantCode_=None, pesticideCondition_=None, mainIntensively_=None, remark_=None, nectarSourceFlowInputs_=None, nectarSourcePointAttachInputs_=None):
        if self.user is None:
            data = {'id': id_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'plantCode': plantCode_, 'floweringStartDate': floweringStartDate_, 'nectarFlow': nectarFlow_, 'nectarSourceArea': nectarSourceArea_, 'apiaryDensity': apiaryDensity_, 'entryDate': entryDate_, 'departureDate': departureDate_, 'purpose': purpose_, 'secondPlantCode': secondPlantCode_, 'pesticideCondition': pesticideCondition_, 'mainIntensively': mainIntensively_, 'remark': remark_, 'nectarSourceFlowInputs': nectarSourceFlowInputs_, 'nectarSourcePointAttachInputs': nectarSourcePointAttachInputs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'plantCode': plantCode_, 'floweringStartDate': floweringStartDate_, 'nectarFlow': nectarFlow_, 'nectarSourceArea': nectarSourceArea_, 'apiaryDensity': apiaryDensity_, 'entryDate': entryDate_, 'departureDate': departureDate_, 'purpose': purpose_, 'secondPlantCode': secondPlantCode_, 'pesticideCondition': pesticideCondition_, 'mainIntensively': mainIntensively_, 'remark': remark_, 'nectarSourceFlowInputs': nectarSourceFlowInputs_, 'nectarSourcePointAttachInputs': nectarSourcePointAttachInputs_}
        response = self.request.post(url=self.url+'/admin/nectar-source-point/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_point_list(self, plantCodes_=None, purpose_=None, floweringStartDateBegin_=None, floweringStartDateEnd_=None, entryDateBegin_=None, entryDateEnd_=None, nectarSourceAreaMin_=None, nectarSourceAreaMax_=None, apiaryDensityMin_=None, apiaryDensityMax_=None):
        if self.user is None:
            data = {'plantCodes': plantCodes_, 'purpose': purpose_, 'floweringStartDateBegin': floweringStartDateBegin_, 'floweringStartDateEnd': floweringStartDateEnd_, 'entryDateBegin': entryDateBegin_, 'entryDateEnd': entryDateEnd_, 'nectarSourceAreaMin': nectarSourceAreaMin_, 'nectarSourceAreaMax': nectarSourceAreaMax_, 'apiaryDensityMin': apiaryDensityMin_, 'apiaryDensityMax': apiaryDensityMax_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'plantCodes': plantCodes_, 'purpose': purpose_, 'floweringStartDateBegin': floweringStartDateBegin_, 'floweringStartDateEnd': floweringStartDateEnd_, 'entryDateBegin': entryDateBegin_, 'entryDateEnd': entryDateEnd_, 'nectarSourceAreaMin': nectarSourceAreaMin_, 'nectarSourceAreaMax': nectarSourceAreaMax_, 'apiaryDensityMin': apiaryDensityMin_, 'apiaryDensityMax': apiaryDensityMax_}
        response = self.request.post(url=self.url+'/admin/nectar-source-point/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_add(self, type_=None, name_=None, baseType_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, altitude_=None, flowerStart_=None, flowerEnd_=None, bloomStart_=None, bloomEnd_=None, contacts_=None, contactNumber_=None, siteArea_=None, nectarSourceArea_=None, expectHiveNum_=None, price_=None, vehicleLength_=None, amNum_=None, acNum_=None, remark_=None, prospectPic_=None, tentPic_=None, sitePic_=None, roadPic_=None, waterPic_=None):
        if self.user is None:
            data = {'type': type_, 'name': name_, 'baseType': baseType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'altitude': altitude_, 'flowerStart': flowerStart_, 'flowerEnd': flowerEnd_, 'bloomStart': bloomStart_, 'bloomEnd': bloomEnd_, 'contacts': contacts_, 'contactNumber': contactNumber_, 'siteArea': siteArea_, 'nectarSourceArea': nectarSourceArea_, 'expectHiveNum': expectHiveNum_, 'price': price_, 'vehicleLength': vehicleLength_, 'amNum': amNum_, 'acNum': acNum_, 'remark': remark_, 'prospectPic': prospectPic_, 'tentPic': tentPic_, 'sitePic': sitePic_, 'roadPic': roadPic_, 'waterPic': waterPic_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'type': type_, 'name': name_, 'baseType': baseType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'altitude': altitude_, 'flowerStart': flowerStart_, 'flowerEnd': flowerEnd_, 'bloomStart': bloomStart_, 'bloomEnd': bloomEnd_, 'contacts': contacts_, 'contactNumber': contactNumber_, 'siteArea': siteArea_, 'nectarSourceArea': nectarSourceArea_, 'expectHiveNum': expectHiveNum_, 'price': price_, 'vehicleLength': vehicleLength_, 'amNum': amNum_, 'acNum': acNum_, 'remark': remark_, 'prospectPic': prospectPic_, 'tentPic': tentPic_, 'sitePic': sitePic_, 'roadPic': roadPic_, 'waterPic': waterPic_}
        response = self.request.post(url=self.url+'/admin/nectar-source/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/nectar-source/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/nectar-source/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/nectar-source/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_edit(self, type_=None, id_=None, name_=None, baseType_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, altitude_=None, flowerStart_=None, flowerEnd_=None, bloomStart_=None, bloomEnd_=None, contacts_=None, contactNumber_=None, siteArea_=None, nectarSourceArea_=None, expectHiveNum_=None, price_=None, vehicleLength_=None, amNum_=None, acNum_=None, remark_=None):
        if self.user is None:
            data = {'type': type_, 'id': id_, 'name': name_, 'baseType': baseType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'altitude': altitude_, 'flowerStart': flowerStart_, 'flowerEnd': flowerEnd_, 'bloomStart': bloomStart_, 'bloomEnd': bloomEnd_, 'contacts': contacts_, 'contactNumber': contactNumber_, 'siteArea': siteArea_, 'nectarSourceArea': nectarSourceArea_, 'expectHiveNum': expectHiveNum_, 'price': price_, 'vehicleLength': vehicleLength_, 'amNum': amNum_, 'acNum': acNum_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'type': type_, 'id': id_, 'name': name_, 'baseType': baseType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'altitude': altitude_, 'flowerStart': flowerStart_, 'flowerEnd': flowerEnd_, 'bloomStart': bloomStart_, 'bloomEnd': bloomEnd_, 'contacts': contacts_, 'contactNumber': contactNumber_, 'siteArea': siteArea_, 'nectarSourceArea': nectarSourceArea_, 'expectHiveNum': expectHiveNum_, 'price': price_, 'vehicleLength': vehicleLength_, 'amNum': amNum_, 'acNum': acNum_, 'remark': remark_}
        response = self.request.post(url=self.url+'/admin/nectar-source/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_edit_charge(self, nectarId_=None, userId_=None):
        if self.user is None:
            data = {'nectarId': nectarId_, 'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'nectarId': nectarId_, 'userId': userId_}
        response = self.request.post(url=self.url+'/admin/nectar-source/edit-charge', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_edit_pic(self, nectarId_=None, prospectPic_=None, tentPic_=None, sitePic_=None, roadPic_=None, waterPic_=None):
        if self.user is None:
            data = {'nectarId': nectarId_, 'prospectPic': prospectPic_, 'tentPic': tentPic_, 'sitePic': sitePic_, 'roadPic': roadPic_, 'waterPic': waterPic_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'nectarId': nectarId_, 'prospectPic': prospectPic_, 'tentPic': tentPic_, 'sitePic': sitePic_, 'roadPic': roadPic_, 'waterPic': waterPic_}
        response = self.request.post(url=self.url+'/admin/nectar-source/edit-pic', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_leave(self, nectarSourceId_=None, leaveTime_=None):
        if self.user is None:
            data = {'nectarSourceId': nectarSourceId_, 'leaveTime': leaveTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'nectarSourceId': nectarSourceId_, 'leaveTime': leaveTime_}
        response = self.request.post(url=self.url+'/admin/nectar-source/leave', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_nectar_source_list(self, excludeStatus_=None, includeStatus_=None, includeProvince_=None, includeCity_=None, includeType_=None, pn_=None, ps_=None, searchType_=None, province_=None, city_=None, county_=None, lng_=None, lat_=None, distanceType_=None, searchName_=None, searchFlowerStart_=None, searchFlowerEnd_=None, collectTimeStart_=None, collectTimeEnd_=None, collector_=None, vehicleLength_=None, ctOrderType_=None, isEnter_=None):
        if self.user is None:
            data = {'excludeStatus': excludeStatus_, 'includeStatus': includeStatus_, 'includeProvince': includeProvince_, 'includeCity': includeCity_, 'includeType': includeType_, 'pn': pn_, 'ps': ps_, 'searchType': searchType_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'distanceType': distanceType_, 'searchName': searchName_, 'searchFlowerStart': searchFlowerStart_, 'searchFlowerEnd': searchFlowerEnd_, 'collectTimeStart': collectTimeStart_, 'collectTimeEnd': collectTimeEnd_, 'collector': collector_, 'vehicleLength': vehicleLength_, 'ctOrderType': ctOrderType_, 'isEnter': isEnter_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'excludeStatus': excludeStatus_, 'includeStatus': includeStatus_, 'includeProvince': includeProvince_, 'includeCity': includeCity_, 'includeType': includeType_, 'pn': pn_, 'ps': ps_, 'searchType': searchType_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'distanceType': distanceType_, 'searchName': searchName_, 'searchFlowerStart': searchFlowerStart_, 'searchFlowerEnd': searchFlowerEnd_, 'collectTimeStart': collectTimeStart_, 'collectTimeEnd': collectTimeEnd_, 'collector': collector_, 'vehicleLength': vehicleLength_, 'ctOrderType': ctOrderType_, 'isEnter': isEnter_}
        response = self.request.post(url=self.url+'/admin/nectar-source/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_shunt_statistics_overview(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/shunt-statistics/overview', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_shunt_statistics_times(self, startDate_=None, endDate_=None):
        if self.user is None:
            data = {'startDate': startDate_, 'endDate': endDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'startDate': startDate_, 'endDate': endDate_}
        response = self.request.post(url=self.url+'/admin/shunt-statistics/times', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_shunt_list(self, pn_=None, ps_=None, userId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'userId': userId_}
        response = self.request.post(url=self.url+'/admin/shunt/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_shunt_page_list(self, pn_=None, ps_=None, issuer_=None, shuntStatus_=None, startCreateTime_=None, endCreateTime_=None, startUseTime_=None, endUseTime_=None, createTimeSort_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'issuer': issuer_, 'shuntStatus': shuntStatus_, 'startCreateTime': startCreateTime_, 'endCreateTime': endCreateTime_, 'startUseTime': startUseTime_, 'endUseTime': endUseTime_, 'createTimeSort': createTimeSort_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'issuer': issuer_, 'shuntStatus': shuntStatus_, 'startCreateTime': startCreateTime_, 'endCreateTime': endCreateTime_, 'startUseTime': startUseTime_, 'endUseTime': endUseTime_, 'createTimeSort': createTimeSort_}
        response = self.request.post(url=self.url+'/admin/shunt/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_shunt_statistics(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/shunt/statistics', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_staff_trail_detail_list(self, userId_=None, loStartTime_=None, loEndTime_=None):
        if self.user is None:
            data = {'userId': userId_, 'loStartTime': loStartTime_, 'loEndTime': loEndTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_, 'loStartTime': loStartTime_, 'loEndTime': loEndTime_}
        response = self.request.post(url=self.url+'/admin/staff-trail/detail-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_staff_trail_latest_list(self, pn_=None, ps_=None, userInfo_=None, province_=None, city_=None, county_=None, loStartTime_=None, loEndTime_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'userInfo': userInfo_, 'province': province_, 'city': city_, 'county': county_, 'loStartTime': loStartTime_, 'loEndTime': loEndTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'userInfo': userInfo_, 'province': province_, 'city': city_, 'county': county_, 'loStartTime': loStartTime_, 'loEndTime': loEndTime_}
        response = self.request.post(url=self.url+'/admin/staff-trail/latest-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_staff_trail_staff_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/staff-trail/staff-count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_statistics_user_login_bee_friend(self, startDate_=None, endDate_=None):
        if self.user is None:
            data = {'startDate': startDate_, 'endDate': endDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'startDate': startDate_, 'endDate': endDate_}
        response = self.request.post(url=self.url+'/admin/statistics/user-login/bee-friend', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_statistics_user_login_employee(self, roleType_=None, startDate_=None, endDate_=None):
        if self.user is None:
            data = {'roleType': roleType_, 'startDate': startDate_, 'endDate': endDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'roleType': roleType_, 'startDate': startDate_, 'endDate': endDate_}
        response = self.request.post(url=self.url+'/admin/statistics/user-login/employee', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_swarm_cancel_repeat(self, swarmId_=None):
        if self.user is None:
            data = {'swarmId': swarmId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'swarmId': swarmId_}
        response = self.request.post(url=self.url+'/admin/swarm/cancel-repeat', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_swarm_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/swarm/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_swarm_del(self, swarmId_=None):
        if self.user is None:
            data = {'swarmId': swarmId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'swarmId': swarmId_}
        response = self.request.post(url=self.url+'/admin/swarm/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_swarm_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/admin/swarm/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_swarm_edit(self, curNectarType_=None, id_=None, vehicleLength_=None, expectHiveNum_=None, pics_=None, scale_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, queenType_=None, hiveNum_=None, standardNum_=None, smallNum_=None, queenNum2_=None, queenNum1_=None, queenNum_=None, ekeNum_=None, platNum_=None, babyNum_=None, honeyNum_=None, colony_=None, mite_=None, chalkbrood_=None, poisoning_=None, nextNectarSource_=None, nextSourceEnterTime_=None, remark_=None, distantPic_=None, tentPic_=None, sitePic_=None, roadPic_=None, altitude_=None, joinDate_=None, leaveDate_=None):
        if self.user is None:
            data = {'curNectarType': curNectarType_, 'id': id_, 'vehicleLength': vehicleLength_, 'expectHiveNum': expectHiveNum_, 'pics': pics_, 'scale': scale_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'queenType': queenType_, 'hiveNum': hiveNum_, 'standardNum': standardNum_, 'smallNum': smallNum_, 'queenNum2': queenNum2_, 'queenNum1': queenNum1_, 'queenNum': queenNum_, 'ekeNum': ekeNum_, 'platNum': platNum_, 'babyNum': babyNum_, 'honeyNum': honeyNum_, 'colony': colony_, 'mite': mite_, 'chalkbrood': chalkbrood_, 'poisoning': poisoning_, 'nextNectarSource': nextNectarSource_, 'nextSourceEnterTime': nextSourceEnterTime_, 'remark': remark_, 'distantPic': distantPic_, 'tentPic': tentPic_, 'sitePic': sitePic_, 'roadPic': roadPic_, 'altitude': altitude_, 'joinDate': joinDate_, 'leaveDate': leaveDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'curNectarType': curNectarType_, 'id': id_, 'vehicleLength': vehicleLength_, 'expectHiveNum': expectHiveNum_, 'pics': pics_, 'scale': scale_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'queenType': queenType_, 'hiveNum': hiveNum_, 'standardNum': standardNum_, 'smallNum': smallNum_, 'queenNum2': queenNum2_, 'queenNum1': queenNum1_, 'queenNum': queenNum_, 'ekeNum': ekeNum_, 'platNum': platNum_, 'babyNum': babyNum_, 'honeyNum': honeyNum_, 'colony': colony_, 'mite': mite_, 'chalkbrood': chalkbrood_, 'poisoning': poisoning_, 'nextNectarSource': nextNectarSource_, 'nextSourceEnterTime': nextSourceEnterTime_, 'remark': remark_, 'distantPic': distantPic_, 'tentPic': tentPic_, 'sitePic': sitePic_, 'roadPic': roadPic_, 'altitude': altitude_, 'joinDate': joinDate_, 'leaveDate': leaveDate_}
        response = self.request.post(url=self.url+'/admin/swarm/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_swarm_get_by_friend(self, friendId_=None):
        if self.user is None:
            data = {'friendId': friendId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'friendId': friendId_}
        response = self.request.post(url=self.url+'/admin/swarm/get-by-friend', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _admin_swarm_page_list(self, vehicleLength_=None, curNectarType_=None, pn_=None, ps_=None, searchKey_=None, province_=None, city_=None, county_=None, collectTimeStart_=None, collectTimeEnd_=None, collector_=None, ctOrderType_=None, hiveNumMin_=None, hiveNumMax_=None, repeat_=None):
        if self.user is None:
            data = {'vehicleLength': vehicleLength_, 'curNectarType': curNectarType_, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'province': province_, 'city': city_, 'county': county_, 'collectTimeStart': collectTimeStart_, 'collectTimeEnd': collectTimeEnd_, 'collector': collector_, 'ctOrderType': ctOrderType_, 'hiveNumMin': hiveNumMin_, 'hiveNumMax': hiveNumMax_, 'repeat': repeat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'vehicleLength': vehicleLength_, 'curNectarType': curNectarType_, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'province': province_, 'city': city_, 'county': county_, 'collectTimeStart': collectTimeStart_, 'collectTimeEnd': collectTimeEnd_, 'collector': collector_, 'ctOrderType': ctOrderType_, 'hiveNumMin': hiveNumMin_, 'hiveNumMax': hiveNumMax_, 'repeat': repeat_}
        response = self.request.post(url=self.url+'/admin/swarm/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_bee_friend_list(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/bee-friend/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_common_config_map_by_code(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/common/config/map-by-code', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_common_region_map_by_codes(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/common/region/map-by-codes', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_extract_record_list(self, input_=None):
        if self.user is None:
            data = {'input': input_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_}
        response = self.request.post(url=self.url+'/api/extract-record/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_nectar_source_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/nectar-source/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_refresh_token_refresh(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/refresh-token/refresh', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_statistics_dashboard_overview(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/statistics/dashboard-overview', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_statistics_friend_collection(self, countDate_=None):
        if self.user is None:
            data = {'countDate': countDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'countDate': countDate_}
        response = self.request.post(url=self.url+'/api/statistics/friend-collection', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_statistics_friend_country(self, countDate_=None):
        if self.user is None:
            data = {'countDate': countDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'countDate': countDate_}
        response = self.request.post(url=self.url+'/api/statistics/friend-country', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_statistics_friend_overview(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/statistics/friend-overview', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_statistics_friend_promote(self, countDate_=None):
        if self.user is None:
            data = {'countDate': countDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'countDate': countDate_}
        response = self.request.post(url=self.url+'/api/statistics/friend-promote', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_statistics_friend_swarm(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/statistics/friend-swarm', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_statistics_generate(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/statistics/generate', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_statistics_incr_friend_phone(self, cond_=None):
        if self.user is None:
            data = {'cond': cond_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cond': cond_}
        response = self.request.post(url=self.url+'/api/statistics/incr-friend-phone', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_statistics_incr_register_source(self, cond_=None):
        if self.user is None:
            data = {'cond': cond_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cond': cond_}
        response = self.request.post(url=self.url+'/api/statistics/incr-register-source', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_statistics_incr_swarm(self, countDate_=None):
        if self.user is None:
            data = {'countDate': countDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'countDate': countDate_}
        response = self.request.post(url=self.url+'/api/statistics/incr-swarm', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_statistics_swarm_collection(self, countDate_=None):
        if self.user is None:
            data = {'countDate': countDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'countDate': countDate_}
        response = self.request.post(url=self.url+'/api/statistics/swarm-collection', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_statistics_swarm_country(self, countDate_=None):
        if self.user is None:
            data = {'countDate': countDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'countDate': countDate_}
        response = self.request.post(url=self.url+'/api/statistics/swarm-country', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_statistics_swarm_overview(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/statistics/swarm-overview', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_statistics_swarm_promote(self, countDate_=None):
        if self.user is None:
            data = {'countDate': countDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'countDate': countDate_}
        response = self.request.post(url=self.url+'/api/statistics/swarm-promote', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _api_weather_refresh(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/weather/refresh', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _config_common_attach_upload(self, file_=None):
        if self.user is None:
            data = {'file': file_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'file': file_}
        response = self.request.post(url=self.url+'/config/common/attach-upload', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _config_common_encryption_upload(self, file_=None):
        if self.user is None:
            data = {'file': file_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'file': file_}
        response = self.request.post(url=self.url+'/config/common/encryption-upload', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _config_common_get_all_enum_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/config/common/get-all-enum-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _config_common_get_config_list(self, codes_=None):
        if self.user is None:
            data = {'codes': codes_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'codes': codes_}
        response = self.request.post(url=self.url+'/config/common/get-config-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _config_common_icon_upload(self, file_=None):
        if self.user is None:
            data = {'file': file_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'file': file_}
        response = self.request.post(url=self.url+'/config/common/icon-upload', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _menu_common_list(self, parentId_=None):
        if self.user is None:
            data = {'parentId': parentId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'parentId': parentId_}
        response = self.request.post(url=self.url+'/menu/common/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_app_version_add(self, appId_=None, updateType_=None, downloadUrl_=None, appCode_=None, appName_=None, versionMilepost_=None, versionNum_=None, versionCode_=None, versionNumBefore_=None, versionBig_=None, updateTitle_=None, updateTitleEn_=None, updateMessage_=None, updateMessageEn_=None, status_=None):
        if self.user is None:
            data = {'appId': appId_, 'updateType': updateType_, 'downloadUrl': downloadUrl_, 'appCode': appCode_, 'appName': appName_, 'versionMilepost': versionMilepost_, 'versionNum': versionNum_, 'versionCode': versionCode_, 'versionNumBefore': versionNumBefore_, 'versionBig': versionBig_, 'updateTitle': updateTitle_, 'updateTitleEn': updateTitleEn_, 'updateMessage': updateMessage_, 'updateMessageEn': updateMessageEn_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId_, 'updateType': updateType_, 'downloadUrl': downloadUrl_, 'appCode': appCode_, 'appName': appName_, 'versionMilepost': versionMilepost_, 'versionNum': versionNum_, 'versionCode': versionCode_, 'versionNumBefore': versionNumBefore_, 'versionBig': versionBig_, 'updateTitle': updateTitle_, 'updateTitleEn': updateTitleEn_, 'updateMessage': updateMessage_, 'updateMessageEn': updateMessageEn_, 'status': status_}
        response = self.request.post(url=self.url+'/mobile/app-version/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_app_version_get(self, appId_=None):
        if self.user is None:
            data = {'appId': appId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'appId': appId_}
        response = self.request.post(url=self.url+'/mobile/app-version/get', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_app_version_upload_app(self, file_=None):
        if self.user is None:
            data = {'file': file_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'file': file_}
        response = self.request.post(url=self.url+'/mobile/app-version/upload-app', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_bee_clue_add(self, keeperName_=None, contactNumber_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, saleNum_=None, spleenNum_=None, intentionPrice_=None):
        if self.user is None:
            data = {'keeperName': keeperName_, 'contactNumber': contactNumber_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'saleNum': saleNum_, 'spleenNum': spleenNum_, 'intentionPrice': intentionPrice_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'keeperName': keeperName_, 'contactNumber': contactNumber_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'saleNum': saleNum_, 'spleenNum': spleenNum_, 'intentionPrice': intentionPrice_}
        response = self.request.post(url=self.url+'/mobile/bee-clue/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_bee_clue_add_contact_time(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/bee-clue/add-contact-time', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_bee_clue_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/bee-clue/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_bee_clue_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/bee-clue/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_bee_clue_edit(self, id_=None, keeperName_=None, contactNumber_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, saleNum_=None, spleenNum_=None, intentionPrice_=None):
        if self.user is None:
            data = {'id': id_, 'keeperName': keeperName_, 'contactNumber': contactNumber_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'saleNum': saleNum_, 'spleenNum': spleenNum_, 'intentionPrice': intentionPrice_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'keeperName': keeperName_, 'contactNumber': contactNumber_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'saleNum': saleNum_, 'spleenNum': spleenNum_, 'intentionPrice': intentionPrice_}
        response = self.request.post(url=self.url+'/mobile/bee-clue/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_bee_clue_list(self, pn_=None, ps_=None, mobile_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'mobile': mobile_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'mobile': mobile_}
        response = self.request.post(url=self.url+'/mobile/bee-clue/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_bee_friend_charge_man_list(self, searchKey_=None):
        if self.user is None:
            data = {'searchKey': searchKey_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'searchKey': searchKey_}
        response = self.request.post(url=self.url+'/mobile/bee-friend/charge-man-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_bee_friend_operator_list(self, searchKey_=None):
        if self.user is None:
            data = {'searchKey': searchKey_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'searchKey': searchKey_}
        response = self.request.post(url=self.url+'/mobile/bee-friend/operator-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_bee_reserve_add(self, reserveName_=None, address_=None, lng_=None, lat_=None, addrProvince_=None, addrCity_=None, addrCounty_=None, province_=None, city_=None, county_=None, nectarType_=None, vehicleLength_=None, reserveArea_=None, altitude_=None, manager_=None, contact_=None, remark_=None, attaches_=None):
        if self.user is None:
            data = {'reserveName': reserveName_, 'address': address_, 'lng': lng_, 'lat': lat_, 'addrProvince': addrProvince_, 'addrCity': addrCity_, 'addrCounty': addrCounty_, 'province': province_, 'city': city_, 'county': county_, 'nectarType': nectarType_, 'vehicleLength': vehicleLength_, 'reserveArea': reserveArea_, 'altitude': altitude_, 'manager': manager_, 'contact': contact_, 'remark': remark_, 'attaches': attaches_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'reserveName': reserveName_, 'address': address_, 'lng': lng_, 'lat': lat_, 'addrProvince': addrProvince_, 'addrCity': addrCity_, 'addrCounty': addrCounty_, 'province': province_, 'city': city_, 'county': county_, 'nectarType': nectarType_, 'vehicleLength': vehicleLength_, 'reserveArea': reserveArea_, 'altitude': altitude_, 'manager': manager_, 'contact': contact_, 'remark': remark_, 'attaches': attaches_}
        response = self.request.post(url=self.url+'/mobile/bee-reserve/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_bee_reserve_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/bee-reserve/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_bee_reserve_edit(self, id_=None, reserveName_=None, address_=None, lng_=None, lat_=None, addrProvince_=None, addrCity_=None, addrCounty_=None, province_=None, city_=None, county_=None, nectarType_=None, vehicleLength_=None, reserveArea_=None, altitude_=None, manager_=None, contact_=None, remark_=None, attaches_=None):
        if self.user is None:
            data = {'id': id_, 'reserveName': reserveName_, 'address': address_, 'lng': lng_, 'lat': lat_, 'addrProvince': addrProvince_, 'addrCity': addrCity_, 'addrCounty': addrCounty_, 'province': province_, 'city': city_, 'county': county_, 'nectarType': nectarType_, 'vehicleLength': vehicleLength_, 'reserveArea': reserveArea_, 'altitude': altitude_, 'manager': manager_, 'contact': contact_, 'remark': remark_, 'attaches': attaches_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'reserveName': reserveName_, 'address': address_, 'lng': lng_, 'lat': lat_, 'addrProvince': addrProvince_, 'addrCity': addrCity_, 'addrCounty': addrCounty_, 'province': province_, 'city': city_, 'county': county_, 'nectarType': nectarType_, 'vehicleLength': vehicleLength_, 'reserveArea': reserveArea_, 'altitude': altitude_, 'manager': manager_, 'contact': contact_, 'remark': remark_, 'attaches': attaches_}
        response = self.request.post(url=self.url+'/mobile/bee-reserve/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_bee_reserve_page_list(self, pn_=None, ps_=None, reserveName_=None, nectarType_=None, creator_=None, gatherTimeStart_=None, gatherTimeEnd_=None, province_=None, city_=None, county_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'reserveName': reserveName_, 'nectarType': nectarType_, 'creator': creator_, 'gatherTimeStart': gatherTimeStart_, 'gatherTimeEnd': gatherTimeEnd_, 'province': province_, 'city': city_, 'county': county_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'reserveName': reserveName_, 'nectarType': nectarType_, 'creator': creator_, 'gatherTimeStart': gatherTimeStart_, 'gatherTimeEnd': gatherTimeEnd_, 'province': province_, 'city': city_, 'county': county_}
        response = self.request.post(url=self.url+'/mobile/bee-reserve/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_comment_add(self, logId_=None, content_=None):
        if self.user is None:
            data = {'logId': logId_, 'content': content_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'logId': logId_, 'content': content_}
        response = self.request.post(url=self.url+'/mobile/comment/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_comment_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/comment/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_comment_list(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/comment/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_container_add(self, cameraNo_=None, serialNo_=None, type_=None, gatewayNo_=None, hiveNum_=None, picUrl_=None, remark_=None):
        if self.user is None:
            data = {'cameraNo': cameraNo_, 'serialNo': serialNo_, 'type': type_, 'gatewayNo': gatewayNo_, 'hiveNum': hiveNum_, 'picUrl': picUrl_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cameraNo': cameraNo_, 'serialNo': serialNo_, 'type': type_, 'gatewayNo': gatewayNo_, 'hiveNum': hiveNum_, 'picUrl': picUrl_, 'remark': remark_}
        response = self.request.post(url=self.url+'/mobile/container/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_container_camera_check(self, serialNos_=None, containerId_=None):
        if self.user is None:
            data = {'serialNos': serialNos_, 'containerId': containerId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'serialNos': serialNos_, 'containerId': containerId_}
        response = self.request.post(url=self.url+'/mobile/container/camera-check', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_container_camera_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/container/camera-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_container_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/container/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_container_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/container/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_container_edit(self, cameraNo_=None, id_=None, serialNo_=None, type_=None, gatewayNo_=None, hiveNum_=None, picUrl_=None, remark_=None):
        if self.user is None:
            data = {'cameraNo': cameraNo_, 'id': id_, 'serialNo': serialNo_, 'type': type_, 'gatewayNo': gatewayNo_, 'hiveNum': hiveNum_, 'picUrl': picUrl_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cameraNo': cameraNo_, 'id': id_, 'serialNo': serialNo_, 'type': type_, 'gatewayNo': gatewayNo_, 'hiveNum': hiveNum_, 'picUrl': picUrl_, 'remark': remark_}
        response = self.request.post(url=self.url+'/mobile/container/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_container_gateway_check(self, containerId_=None, gatewayNo_=None):
        if self.user is None:
            data = {'containerId': containerId_, 'gatewayNo': gatewayNo_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'containerId': containerId_, 'gatewayNo': gatewayNo_}
        response = self.request.post(url=self.url+'/mobile/container/gateway-check', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_container_gateway_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/container/gateway-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_container_get_token(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/container/get-token', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_container_list(self, excludeNectarSourceIds_=None, includeNectarSourceIds_=None, excludeStatus_=None, includeStatus_=None):
        if self.user is None:
            data = {'excludeNectarSourceIds': excludeNectarSourceIds_, 'includeNectarSourceIds': includeNectarSourceIds_, 'excludeStatus': excludeStatus_, 'includeStatus': includeStatus_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'excludeNectarSourceIds': excludeNectarSourceIds_, 'includeNectarSourceIds': includeNectarSourceIds_, 'excludeStatus': excludeStatus_, 'includeStatus': includeStatus_}
        response = self.request.post(url=self.url+'/mobile/container/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_container_page_list(self, excludeNectarSourceIds_=None, includeNectarSourceIds_=None, excludeStatus_=None, includeStatus_=None, pn_=None, ps_=None):
        if self.user is None:
            data = {'excludeNectarSourceIds': excludeNectarSourceIds_, 'includeNectarSourceIds': includeNectarSourceIds_, 'excludeStatus': excludeStatus_, 'includeStatus': includeStatus_, 'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'excludeNectarSourceIds': excludeNectarSourceIds_, 'includeNectarSourceIds': includeNectarSourceIds_, 'excludeStatus': excludeStatus_, 'includeStatus': includeStatus_, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/mobile/container/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_container_ready_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/container/ready-count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_contract_add(self, userId_=None, amount_=None, handsel_=None, identityFront_=None, identityBack_=None, bankFront_=None, bankBack_=None, contractPics_=None, signTime_=None, hiveNum_=None, standardNum_=None, smallNum_=None, tent_=None, honeyMachine_=None, scraper_=None, motorcycle_=None, honeypot_=None, alternator_=None, solarPanel_=None, remark_=None):
        if self.user is None:
            data = {'userId': userId_, 'amount': amount_, 'handsel': handsel_, 'identityFront': identityFront_, 'identityBack': identityBack_, 'bankFront': bankFront_, 'bankBack': bankBack_, 'contractPics': contractPics_, 'signTime': signTime_, 'hiveNum': hiveNum_, 'standardNum': standardNum_, 'smallNum': smallNum_, 'tent': tent_, 'honeyMachine': honeyMachine_, 'scraper': scraper_, 'motorcycle': motorcycle_, 'honeypot': honeypot_, 'alternator': alternator_, 'solarPanel': solarPanel_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_, 'amount': amount_, 'handsel': handsel_, 'identityFront': identityFront_, 'identityBack': identityBack_, 'bankFront': bankFront_, 'bankBack': bankBack_, 'contractPics': contractPics_, 'signTime': signTime_, 'hiveNum': hiveNum_, 'standardNum': standardNum_, 'smallNum': smallNum_, 'tent': tent_, 'honeyMachine': honeyMachine_, 'scraper': scraper_, 'motorcycle': motorcycle_, 'honeypot': honeypot_, 'alternator': alternator_, 'solarPanel': solarPanel_, 'remark': remark_}
        response = self.request.post(url=self.url+'/mobile/contract/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_contract_contract_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/contract/contract-detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_contract_contract_view(self, userId_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'userId': userId_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/mobile/contract/contract-view', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_contract_discard(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/contract/discard', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_contract_edit(self, id_=None, identityFront_=None, identityBack_=None, bankFront_=None, bankBack_=None, contractPics_=None, signTime_=None, standardNum_=None, smallNum_=None, tent_=None, honeyMachine_=None, scraper_=None, motorcycle_=None, honeypot_=None, alternator_=None, solarPanel_=None, remark_=None):
        if self.user is None:
            data = {'id': id_, 'identityFront': identityFront_, 'identityBack': identityBack_, 'bankFront': bankFront_, 'bankBack': bankBack_, 'contractPics': contractPics_, 'signTime': signTime_, 'standardNum': standardNum_, 'smallNum': smallNum_, 'tent': tent_, 'honeyMachine': honeyMachine_, 'scraper': scraper_, 'motorcycle': motorcycle_, 'honeypot': honeypot_, 'alternator': alternator_, 'solarPanel': solarPanel_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'identityFront': identityFront_, 'identityBack': identityBack_, 'bankFront': bankFront_, 'bankBack': bankBack_, 'contractPics': contractPics_, 'signTime': signTime_, 'standardNum': standardNum_, 'smallNum': smallNum_, 'tent': tent_, 'honeyMachine': honeyMachine_, 'scraper': scraper_, 'motorcycle': motorcycle_, 'honeypot': honeypot_, 'alternator': alternator_, 'solarPanel': solarPanel_, 'remark': remark_}
        response = self.request.post(url=self.url+'/mobile/contract/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_contract_friend_list(self, pn_=None, ps_=None, searchKey_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/mobile/contract/friend-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_contract_page_list(self, pn_=None, ps_=None, userId_=None, searchKey_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'userId': userId_, 'searchKey': searchKey_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'userId': userId_, 'searchKey': searchKey_}
        response = self.request.post(url=self.url+'/mobile/contract/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_contract_pay_off(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/contract/pay-off', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_enter_enter_check(self, containerIds_=None, nectarSourceId_=None):
        if self.user is None:
            data = {'containerIds': containerIds_, 'nectarSourceId': nectarSourceId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'containerIds': containerIds_, 'nectarSourceId': nectarSourceId_}
        response = self.request.post(url=self.url+'/mobile/enter/enter-check', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_enter_enter_save(self, containerIds_=None, nectarSourceId_=None, enterTime_=None, hiveNum_=None):
        if self.user is None:
            data = {'containerIds': containerIds_, 'nectarSourceId': nectarSourceId_, 'enterTime': enterTime_, 'hiveNum': hiveNum_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'containerIds': containerIds_, 'nectarSourceId': nectarSourceId_, 'enterTime': enterTime_, 'hiveNum': hiveNum_}
        response = self.request.post(url=self.url+'/mobile/enter/enter-save', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_extract_add(self, nectarSourceId_=None, nectarSourceType_=None, gatherTime_=None, weight_=None, operatorId_=None, unit_=None, scenePic_=None):
        if self.user is None:
            data = {'nectarSourceId': nectarSourceId_, 'nectarSourceType': nectarSourceType_, 'gatherTime': gatherTime_, 'weight': weight_, 'operatorId': operatorId_, 'unit': unit_, 'scenePic': scenePic_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'nectarSourceId': nectarSourceId_, 'nectarSourceType': nectarSourceType_, 'gatherTime': gatherTime_, 'weight': weight_, 'operatorId': operatorId_, 'unit': unit_, 'scenePic': scenePic_}
        response = self.request.post(url=self.url+'/mobile/extract/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_extract_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/extract/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_extract_edit(self, id_=None, gatherTime_=None, weight_=None, unit_=None, operatorId_=None, scenePic_=None):
        if self.user is None:
            data = {'id': id_, 'gatherTime': gatherTime_, 'weight': weight_, 'unit': unit_, 'operatorId': operatorId_, 'scenePic': scenePic_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'gatherTime': gatherTime_, 'weight': weight_, 'unit': unit_, 'operatorId': operatorId_, 'scenePic': scenePic_}
        response = self.request.post(url=self.url+'/mobile/extract/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_extract_list(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/mobile/extract/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_extract_nectar_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/extract/nectar-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_extract_operator_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/extract/operator-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_fc_user_change_verify_code(self, mobile_=None):
        if self.user is None:
            data = {'mobile': mobile_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile_}
        response = self.request.post(url=self.url+'/mobile/fc-user/change-verify-code', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_fc_user_change_weichat(self, code_=None):
        if self.user is None:
            data = {'code': code_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'code': code_}
        response = self.request.post(url=self.url+'/mobile/fc-user/change-weichat', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_fc_user_info(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/fc-user/info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_fc_user_mobile_check(self, mobile_=None):
        if self.user is None:
            data = {'mobile': mobile_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile_}
        response = self.request.post(url=self.url+'/mobile/fc-user/mobile-check', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_fc_user_update(self, regularSource_=None, userName_=None, headImg_=None, scale_=None, seniority_=None, nativeProvince_=None, nativeCity_=None, nativeCounty_=None, age_=None, gender_=None):
        if self.user is None:
            data = {'regularSource': regularSource_, 'userName': userName_, 'headImg': headImg_, 'scale': scale_, 'seniority': seniority_, 'nativeProvince': nativeProvince_, 'nativeCity': nativeCity_, 'nativeCounty': nativeCounty_, 'age': age_, 'gender': gender_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'regularSource': regularSource_, 'userName': userName_, 'headImg': headImg_, 'scale': scale_, 'seniority': seniority_, 'nativeProvince': nativeProvince_, 'nativeCity': nativeCity_, 'nativeCounty': nativeCounty_, 'age': age_, 'gender': gender_}
        response = self.request.post(url=self.url+'/mobile/fc-user/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_fc_user_update_location(self, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/mobile/fc-user/update-location', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_fc_user_update_mobile(self, mobile_=None, verifyCode_=None):
        if self.user is None:
            data = {'mobile': mobile_, 'verifyCode': verifyCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mobile': mobile_, 'verifyCode': verifyCode_}
        response = self.request.post(url=self.url+'/mobile/fc-user/update-mobile', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_fc_user_upload_headImg(self, headImgFile_=None):
        if self.user is None:
            data = {'headImgFile': headImgFile_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'headImgFile': headImgFile_}
        response = self.request.post(url=self.url+'/mobile/fc-user/upload-headImg', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_help_comment_comment(self, helpInfoId_=None, helpCommentId_=None, content_=None):
        if self.user is None:
            data = {'helpInfoId': helpInfoId_, 'helpCommentId': helpCommentId_, 'content': content_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'helpInfoId': helpInfoId_, 'helpCommentId': helpCommentId_, 'content': content_}
        response = self.request.post(url=self.url+'/mobile/help-comment/comment', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_help_comment_del(self, helpCommentId_=None):
        if self.user is None:
            data = {'helpCommentId': helpCommentId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'helpCommentId': helpCommentId_}
        response = self.request.post(url=self.url+'/mobile/help-comment/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_help_comment_detail(self, helpCommentId_=None):
        if self.user is None:
            data = {'helpCommentId': helpCommentId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'helpCommentId': helpCommentId_}
        response = self.request.post(url=self.url+'/mobile/help-comment/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_help_comment_list(self, pn_=None, ps_=None, helpInfoId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'helpInfoId': helpInfoId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'helpInfoId': helpInfoId_}
        response = self.request.post(url=self.url+'/mobile/help-comment/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_help_comment_unread_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/help-comment/unread-count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_help_info_add(self, type_=None, content_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, images_=None):
        if self.user is None:
            data = {'type': type_, 'content': content_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'images': images_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'type': type_, 'content': content_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'images': images_}
        response = self.request.post(url=self.url+'/mobile/help-info/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_help_info_attention_list(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/mobile/help-info/attention-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_help_info_close(self, helpInfoId_=None):
        if self.user is None:
            data = {'helpInfoId': helpInfoId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'helpInfoId': helpInfoId_}
        response = self.request.post(url=self.url+'/mobile/help-info/close', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_help_info_del(self, helpInfoId_=None):
        if self.user is None:
            data = {'helpInfoId': helpInfoId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'helpInfoId': helpInfoId_}
        response = self.request.post(url=self.url+'/mobile/help-info/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_help_info_detail(self, helpInfoId_=None, lng_=None, lat_=None, readStatus_=None):
        if self.user is None:
            data = {'helpInfoId': helpInfoId_, 'lng': lng_, 'lat': lat_, 'readStatus': readStatus_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'helpInfoId': helpInfoId_, 'lng': lng_, 'lat': lat_, 'readStatus': readStatus_}
        response = self.request.post(url=self.url+'/mobile/help-info/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_help_info_help_button(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/help-info/help-button', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_help_info_list(self, pn_=None, ps_=None, type_=None, province_=None, city_=None, county_=None, queryDistance_=None, locationLng_=None, locationLat_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'type': type_, 'province': province_, 'city': city_, 'county': county_, 'queryDistance': queryDistance_, 'locationLng': locationLng_, 'locationLat': locationLat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'type': type_, 'province': province_, 'city': city_, 'county': county_, 'queryDistance': queryDistance_, 'locationLng': locationLng_, 'locationLat': locationLat_}
        response = self.request.post(url=self.url+'/mobile/help-info/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_help_info_message_detail(self, helpInfoId_=None, lng_=None, lat_=None, readStatus_=None, helpCommentId_=None):
        if self.user is None:
            data = {'helpInfoId': helpInfoId_, 'lng': lng_, 'lat': lat_, 'readStatus': readStatus_, 'helpCommentId': helpCommentId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'helpInfoId': helpInfoId_, 'lng': lng_, 'lat': lat_, 'readStatus': readStatus_, 'helpCommentId': helpCommentId_}
        response = self.request.post(url=self.url+'/mobile/help-info/message-detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_help_info_self_list(self, pn_=None, ps_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/mobile/help-info/self-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_help_info_update(self, helpInfoId_=None, type_=None, content_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, images_=None):
        if self.user is None:
            data = {'helpInfoId': helpInfoId_, 'type': type_, 'content': content_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'images': images_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'helpInfoId': helpInfoId_, 'type': type_, 'content': content_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'images': images_}
        response = self.request.post(url=self.url+'/mobile/help-info/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_hot_nectar_source_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/hot-nectar-source/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_label_business_set(self, labelType_=None):
        if self.user is None:
            data = {'labelType': labelType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'labelType': labelType_}
        response = self.request.post(url=self.url+'/mobile/label/business/set', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_message_del(self, messageId_=None):
        if self.user is None:
            data = {'messageId': messageId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'messageId': messageId_}
        response = self.request.post(url=self.url+'/mobile/message/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_message_list(self, messageTypes_=None, status_=None, pn_=None, ps_=None):
        if self.user is None:
            data = {'messageTypes': messageTypes_, 'status': status_, 'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'messageTypes': messageTypes_, 'status': status_, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/mobile/message/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_message_read(self, messageId_=None):
        if self.user is None:
            data = {'messageId': messageId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'messageId': messageId_}
        response = self.request.post(url=self.url+'/mobile/message/read', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_message_read_all(self, messageTypes_=None, bizId_=None, title_=None):
        if self.user is None:
            data = {'messageTypes': messageTypes_, 'bizId': bizId_, 'title': title_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'messageTypes': messageTypes_, 'bizId': bizId_, 'title': title_}
        response = self.request.post(url=self.url+'/mobile/message/read-all', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_message_unread(self, messageTypes_=None):
        if self.user is None:
            data = {'messageTypes': messageTypes_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'messageTypes': messageTypes_}
        response = self.request.post(url=self.url+'/mobile/message/unread', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_nearby_bee_friend_associate(self, searchKey_=None):
        if self.user is None:
            data = {'searchKey': searchKey_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'searchKey': searchKey_}
        response = self.request.post(url=self.url+'/mobile/nearby-bee-friend/associate', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_nearby_bee_friend_detail(self, id_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'id': id_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/mobile/nearby-bee-friend/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_nearby_bee_friend_nearby_button(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/nearby-bee-friend/nearby-button', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_nearby_bee_friend_nearby_list(self, mutualLabels_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'mutualLabels': mutualLabels_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mutualLabels': mutualLabels_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/mobile/nearby-bee-friend/nearby-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_nearby_bee_friend_page_list(self, intentions_=None, businessLabels_=None, pn_=None, ps_=None, searchKey_=None, searchType_=None, province_=None, city_=None, county_=None, lng_=None, lat_=None, distanceType_=None, sortType_=None, onlySelf_=None, registed_=None):
        if self.user is None:
            data = {'intentions': intentions_, 'businessLabels': businessLabels_, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'searchType': searchType_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'distanceType': distanceType_, 'sortType': sortType_, 'onlySelf': onlySelf_, 'registed': registed_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'intentions': intentions_, 'businessLabels': businessLabels_, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'searchType': searchType_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'distanceType': distanceType_, 'sortType': sortType_, 'onlySelf': onlySelf_, 'registed': registed_}
        response = self.request.post(url=self.url+'/mobile/nearby-bee-friend/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_nectar_source_add(self, type_=None, name_=None, baseType_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, altitude_=None, flowerStart_=None, flowerEnd_=None, bloomStart_=None, bloomEnd_=None, contacts_=None, contactNumber_=None, siteArea_=None, nectarSourceArea_=None, expectHiveNum_=None, price_=None, vehicleLength_=None, amNum_=None, acNum_=None, remark_=None, prospectPic_=None, tentPic_=None, sitePic_=None, roadPic_=None, waterPic_=None):
        if self.user is None:
            data = {'type': type_, 'name': name_, 'baseType': baseType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'altitude': altitude_, 'flowerStart': flowerStart_, 'flowerEnd': flowerEnd_, 'bloomStart': bloomStart_, 'bloomEnd': bloomEnd_, 'contacts': contacts_, 'contactNumber': contactNumber_, 'siteArea': siteArea_, 'nectarSourceArea': nectarSourceArea_, 'expectHiveNum': expectHiveNum_, 'price': price_, 'vehicleLength': vehicleLength_, 'amNum': amNum_, 'acNum': acNum_, 'remark': remark_, 'prospectPic': prospectPic_, 'tentPic': tentPic_, 'sitePic': sitePic_, 'roadPic': roadPic_, 'waterPic': waterPic_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'type': type_, 'name': name_, 'baseType': baseType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'altitude': altitude_, 'flowerStart': flowerStart_, 'flowerEnd': flowerEnd_, 'bloomStart': bloomStart_, 'bloomEnd': bloomEnd_, 'contacts': contacts_, 'contactNumber': contactNumber_, 'siteArea': siteArea_, 'nectarSourceArea': nectarSourceArea_, 'expectHiveNum': expectHiveNum_, 'price': price_, 'vehicleLength': vehicleLength_, 'amNum': amNum_, 'acNum': acNum_, 'remark': remark_, 'prospectPic': prospectPic_, 'tentPic': tentPic_, 'sitePic': sitePic_, 'roadPic': roadPic_, 'waterPic': waterPic_}
        response = self.request.post(url=self.url+'/mobile/nectar-source/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_nectar_source_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/nectar-source/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_nectar_source_edit(self, type_=None, id_=None, name_=None, baseType_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, altitude_=None, flowerStart_=None, flowerEnd_=None, bloomStart_=None, bloomEnd_=None, contacts_=None, contactNumber_=None, siteArea_=None, nectarSourceArea_=None, expectHiveNum_=None, price_=None, vehicleLength_=None, amNum_=None, acNum_=None, remark_=None):
        if self.user is None:
            data = {'type': type_, 'id': id_, 'name': name_, 'baseType': baseType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'altitude': altitude_, 'flowerStart': flowerStart_, 'flowerEnd': flowerEnd_, 'bloomStart': bloomStart_, 'bloomEnd': bloomEnd_, 'contacts': contacts_, 'contactNumber': contactNumber_, 'siteArea': siteArea_, 'nectarSourceArea': nectarSourceArea_, 'expectHiveNum': expectHiveNum_, 'price': price_, 'vehicleLength': vehicleLength_, 'amNum': amNum_, 'acNum': acNum_, 'remark': remark_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'type': type_, 'id': id_, 'name': name_, 'baseType': baseType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'altitude': altitude_, 'flowerStart': flowerStart_, 'flowerEnd': flowerEnd_, 'bloomStart': bloomStart_, 'bloomEnd': bloomEnd_, 'contacts': contacts_, 'contactNumber': contactNumber_, 'siteArea': siteArea_, 'nectarSourceArea': nectarSourceArea_, 'expectHiveNum': expectHiveNum_, 'price': price_, 'vehicleLength': vehicleLength_, 'amNum': amNum_, 'acNum': acNum_, 'remark': remark_}
        response = self.request.post(url=self.url+'/mobile/nectar-source/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_nectar_source_edit_charge(self, nectarId_=None, userId_=None):
        if self.user is None:
            data = {'nectarId': nectarId_, 'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'nectarId': nectarId_, 'userId': userId_}
        response = self.request.post(url=self.url+'/mobile/nectar-source/edit-charge', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_nectar_source_edit_pic(self, nectarId_=None, prospectPic_=None, tentPic_=None, sitePic_=None, roadPic_=None, waterPic_=None):
        if self.user is None:
            data = {'nectarId': nectarId_, 'prospectPic': prospectPic_, 'tentPic': tentPic_, 'sitePic': sitePic_, 'roadPic': roadPic_, 'waterPic': waterPic_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'nectarId': nectarId_, 'prospectPic': prospectPic_, 'tentPic': tentPic_, 'sitePic': sitePic_, 'roadPic': roadPic_, 'waterPic': waterPic_}
        response = self.request.post(url=self.url+'/mobile/nectar-source/edit-pic', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_nectar_source_leave(self, nectarSourceId_=None, leaveTime_=None):
        if self.user is None:
            data = {'nectarSourceId': nectarSourceId_, 'leaveTime': leaveTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'nectarSourceId': nectarSourceId_, 'leaveTime': leaveTime_}
        response = self.request.post(url=self.url+'/mobile/nectar-source/leave', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_nectar_source_list(self, excludeStatus_=None, includeStatus_=None, includeProvince_=None, includeCity_=None, includeType_=None, pn_=None, ps_=None, searchType_=None, province_=None, city_=None, county_=None, lng_=None, lat_=None, distanceType_=None, searchName_=None, searchFlowerStart_=None, searchFlowerEnd_=None, collectTimeStart_=None, collectTimeEnd_=None, collector_=None, vehicleLength_=None, ctOrderType_=None, isEnter_=None):
        if self.user is None:
            data = {'excludeStatus': excludeStatus_, 'includeStatus': includeStatus_, 'includeProvince': includeProvince_, 'includeCity': includeCity_, 'includeType': includeType_, 'pn': pn_, 'ps': ps_, 'searchType': searchType_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'distanceType': distanceType_, 'searchName': searchName_, 'searchFlowerStart': searchFlowerStart_, 'searchFlowerEnd': searchFlowerEnd_, 'collectTimeStart': collectTimeStart_, 'collectTimeEnd': collectTimeEnd_, 'collector': collector_, 'vehicleLength': vehicleLength_, 'ctOrderType': ctOrderType_, 'isEnter': isEnter_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'excludeStatus': excludeStatus_, 'includeStatus': includeStatus_, 'includeProvince': includeProvince_, 'includeCity': includeCity_, 'includeType': includeType_, 'pn': pn_, 'ps': ps_, 'searchType': searchType_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'distanceType': distanceType_, 'searchName': searchName_, 'searchFlowerStart': searchFlowerStart_, 'searchFlowerEnd': searchFlowerEnd_, 'collectTimeStart': collectTimeStart_, 'collectTimeEnd': collectTimeEnd_, 'collector': collector_, 'vehicleLength': vehicleLength_, 'ctOrderType': ctOrderType_, 'isEnter': isEnter_}
        response = self.request.post(url=self.url+'/mobile/nectar-source/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_share_app(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/share/app', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_share_help_info(self, helpInfoId_=None):
        if self.user is None:
            data = {'helpInfoId': helpInfoId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'helpInfoId': helpInfoId_}
        response = self.request.post(url=self.url+'/mobile/share/help-info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_share_location(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/share/location', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_shunt_address_list(self, addressType_=None):
        if self.user is None:
            data = {'addressType': addressType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'addressType': addressType_}
        response = self.request.post(url=self.url+'/mobile/shunt-address/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_shunt_add(self, loadingType_=None, loadAddressId_=None, unloadAddressId_=None, useTime_=None, cargoType_=None, cargoName_=None, amount_=None, minWeight_=None, maxWeight_=None, minCapacity_=None, maxCapacity_=None, useType_=None, truckLengthList_=None, truckTypeList_=None, mileage_=None, isFindPickBees_=None, remark_=None, shuntAddressInputs_=None):
        if self.user is None:
            data = {'loadingType': loadingType_, 'loadAddressId': loadAddressId_, 'unloadAddressId': unloadAddressId_, 'useTime': useTime_, 'cargoType': cargoType_, 'cargoName': cargoName_, 'amount': amount_, 'minWeight': minWeight_, 'maxWeight': maxWeight_, 'minCapacity': minCapacity_, 'maxCapacity': maxCapacity_, 'useType': useType_, 'truckLengthList': truckLengthList_, 'truckTypeList': truckTypeList_, 'mileage': mileage_, 'isFindPickBees': isFindPickBees_, 'remark': remark_, 'shuntAddressInputs': shuntAddressInputs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'loadingType': loadingType_, 'loadAddressId': loadAddressId_, 'unloadAddressId': unloadAddressId_, 'useTime': useTime_, 'cargoType': cargoType_, 'cargoName': cargoName_, 'amount': amount_, 'minWeight': minWeight_, 'maxWeight': maxWeight_, 'minCapacity': minCapacity_, 'maxCapacity': maxCapacity_, 'useType': useType_, 'truckLengthList': truckLengthList_, 'truckTypeList': truckTypeList_, 'mileage': mileage_, 'isFindPickBees': isFindPickBees_, 'remark': remark_, 'shuntAddressInputs': shuntAddressInputs_}
        response = self.request.post(url=self.url+'/mobile/shunt/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_shunt_arrive(self, shuntId_=None, arriveTime_=None):
        if self.user is None:
            data = {'shuntId': shuntId_, 'arriveTime': arriveTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'shuntId': shuntId_, 'arriveTime': arriveTime_}
        response = self.request.post(url=self.url+'/mobile/shunt/arrive', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_shunt_cancel(self, shuntId_=None, cancelType_=None):
        if self.user is None:
            data = {'shuntId': shuntId_, 'cancelType': cancelType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'shuntId': shuntId_, 'cancelType': cancelType_}
        response = self.request.post(url=self.url+'/mobile/shunt/cancel', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_shunt_confirm(self, id_=None, driverName_=None, driverTelephone_=None, plateNumber_=None):
        if self.user is None:
            data = {'id': id_, 'driverName': driverName_, 'driverTelephone': driverTelephone_, 'plateNumber': plateNumber_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'driverName': driverName_, 'driverTelephone': driverTelephone_, 'plateNumber': plateNumber_}
        response = self.request.post(url=self.url+'/mobile/shunt/confirm', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_shunt_detail(self, shuntId_=None):
        if self.user is None:
            data = {'shuntId': shuntId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'shuntId': shuntId_}
        response = self.request.post(url=self.url+'/mobile/shunt/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_shunt_driver_list(self, shuntId_=None):
        if self.user is None:
            data = {'shuntId': shuntId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'shuntId': shuntId_}
        response = self.request.post(url=self.url+'/mobile/shunt/driver-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_shunt_list(self, pn_=None, ps_=None, userId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'userId': userId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'userId': userId_}
        response = self.request.post(url=self.url+'/mobile/shunt/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_shunt_nearby_list(self, mutualLabels_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'mutualLabels': mutualLabels_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'mutualLabels': mutualLabels_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/mobile/shunt/nearby-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_statistics_container(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/statistics/container', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_statistics_hive(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/statistics/hive', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_statistics_nectar(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/statistics/nectar', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_statistics_nectar_source(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/statistics/nectar-source', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_statistics_nectar_source_type(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/statistics/nectar-source-type', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_statistics_nectar_type(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/statistics/nectar-type', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_swarm_detail(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/swarm/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_swarm_edit(self, curNectarType_=None, id_=None, vehicleLength_=None, expectHiveNum_=None, pics_=None, scale_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, queenType_=None, hiveNum_=None, standardNum_=None, smallNum_=None, queenNum2_=None, queenNum1_=None, queenNum_=None, ekeNum_=None, platNum_=None, babyNum_=None, honeyNum_=None, colony_=None, mite_=None, chalkbrood_=None, poisoning_=None, nextNectarSource_=None, nextSourceEnterTime_=None, remark_=None, distantPic_=None, tentPic_=None, sitePic_=None, roadPic_=None, altitude_=None, joinDate_=None, leaveDate_=None):
        if self.user is None:
            data = {'curNectarType': curNectarType_, 'id': id_, 'vehicleLength': vehicleLength_, 'expectHiveNum': expectHiveNum_, 'pics': pics_, 'scale': scale_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'queenType': queenType_, 'hiveNum': hiveNum_, 'standardNum': standardNum_, 'smallNum': smallNum_, 'queenNum2': queenNum2_, 'queenNum1': queenNum1_, 'queenNum': queenNum_, 'ekeNum': ekeNum_, 'platNum': platNum_, 'babyNum': babyNum_, 'honeyNum': honeyNum_, 'colony': colony_, 'mite': mite_, 'chalkbrood': chalkbrood_, 'poisoning': poisoning_, 'nextNectarSource': nextNectarSource_, 'nextSourceEnterTime': nextSourceEnterTime_, 'remark': remark_, 'distantPic': distantPic_, 'tentPic': tentPic_, 'sitePic': sitePic_, 'roadPic': roadPic_, 'altitude': altitude_, 'joinDate': joinDate_, 'leaveDate': leaveDate_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'curNectarType': curNectarType_, 'id': id_, 'vehicleLength': vehicleLength_, 'expectHiveNum': expectHiveNum_, 'pics': pics_, 'scale': scale_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'queenType': queenType_, 'hiveNum': hiveNum_, 'standardNum': standardNum_, 'smallNum': smallNum_, 'queenNum2': queenNum2_, 'queenNum1': queenNum1_, 'queenNum': queenNum_, 'ekeNum': ekeNum_, 'platNum': platNum_, 'babyNum': babyNum_, 'honeyNum': honeyNum_, 'colony': colony_, 'mite': mite_, 'chalkbrood': chalkbrood_, 'poisoning': poisoning_, 'nextNectarSource': nextNectarSource_, 'nextSourceEnterTime': nextSourceEnterTime_, 'remark': remark_, 'distantPic': distantPic_, 'tentPic': tentPic_, 'sitePic': sitePic_, 'roadPic': roadPic_, 'altitude': altitude_, 'joinDate': joinDate_, 'leaveDate': leaveDate_}
        response = self.request.post(url=self.url+'/mobile/swarm/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_swarm_get_by_friend(self, friendId_=None):
        if self.user is None:
            data = {'friendId': friendId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'friendId': friendId_}
        response = self.request.post(url=self.url+'/mobile/swarm/get-by-friend', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_swarm_map_list(self, lng_=None, lat_=None, distanceType_=None):
        if self.user is None:
            data = {'lng': lng_, 'lat': lat_, 'distanceType': distanceType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'lng': lng_, 'lat': lat_, 'distanceType': distanceType_}
        response = self.request.post(url=self.url+'/mobile/swarm/map-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_auth_auth(self, telephone_=None, cardName_=None, idCardNo_=None, avatarsImage_=None, idCardFrontImage_=None):
        if self.user is None:
            data = {'telephone': telephone_, 'cardName': cardName_, 'idCardNo': idCardNo_, 'avatarsImage': avatarsImage_, 'idCardFrontImage': idCardFrontImage_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'telephone': telephone_, 'cardName': cardName_, 'idCardNo': idCardNo_, 'avatarsImage': avatarsImage_, 'idCardFrontImage': idCardFrontImage_}
        response = self.request.post(url=self.url+'/mobile/user-auth/auth', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_auth_get_auth_info(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/user-auth/get-auth-info', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_auth_get_status(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/user-auth/get-status', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_auth_token(self, authCode_=None):
        if self.user is None:
            data = {'authCode': authCode_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'authCode': authCode_}
        response = self.request.post(url=self.url+'/mobile/user-auth/token', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_nectar_source_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/user-nectar-source/count', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_nectar_source_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/user-nectar-source/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_user_nectar_source_update(self, nectarSources_=None):
        if self.user is None:
            data = {'nectarSources': nectarSources_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'nectarSources': nectarSources_}
        response = self.request.post(url=self.url+'/mobile/user-nectar-source/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_weather_detail(self, province_=None, city_=None, county_=None, lat_=None, lng_=None):
        if self.user is None:
            data = {'province': province_, 'city': city_, 'county': county_, 'lat': lat_, 'lng': lng_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'province': province_, 'city': city_, 'county': county_, 'lat': lat_, 'lng': lng_}
        response = self.request.post(url=self.url+'/mobile/weather/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_weather_home(self, province_=None, city_=None, county_=None, lat_=None, lng_=None, pn_=None, ps_=None):
        if self.user is None:
            data = {'province': province_, 'city': city_, 'county': county_, 'lat': lat_, 'lng': lng_, 'pn': pn_, 'ps': ps_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'province': province_, 'city': city_, 'county': county_, 'lat': lat_, 'lng': lng_, 'pn': pn_, 'ps': ps_}
        response = self.request.post(url=self.url+'/mobile/weather/home', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_work_log_add_extract(self, province_=None, city_=None, address_=None, lng_=None, lat_=None, nectarSourceId_=None, worker_=None, workerNum_=None, cost_=None, remark_=None, pics_=None):
        if self.user is None:
            data = {'province': province_, 'city': city_, 'address': address_, 'lng': lng_, 'lat': lat_, 'nectarSourceId': nectarSourceId_, 'worker': worker_, 'workerNum': workerNum_, 'cost': cost_, 'remark': remark_, 'pics': pics_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'province': province_, 'city': city_, 'address': address_, 'lng': lng_, 'lat': lat_, 'nectarSourceId': nectarSourceId_, 'worker': worker_, 'workerNum': workerNum_, 'cost': cost_, 'remark': remark_, 'pics': pics_}
        response = self.request.post(url=self.url+'/mobile/work-log/add-extract', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_work_log_add_keep(self, province_=None, city_=None, address_=None, lng_=None, lat_=None, gatherHoneyRemark_=None, gatherPollenRemark_=None, detail_=None):
        if self.user is None:
            data = {'province': province_, 'city': city_, 'address': address_, 'lng': lng_, 'lat': lat_, 'gatherHoneyRemark': gatherHoneyRemark_, 'gatherPollenRemark': gatherPollenRemark_, 'detail': detail_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'province': province_, 'city': city_, 'address': address_, 'lng': lng_, 'lat': lat_, 'gatherHoneyRemark': gatherHoneyRemark_, 'gatherPollenRemark': gatherPollenRemark_, 'detail': detail_}
        response = self.request.post(url=self.url+'/mobile/work-log/add-keep', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_work_log_add_seek(self, province_=None, city_=None, address_=None, lng_=None, lat_=None, isFit_=None, route_=None, worker_=None, flowerRemark_=None, env_=None, remark_=None, pics_=None):
        if self.user is None:
            data = {'province': province_, 'city': city_, 'address': address_, 'lng': lng_, 'lat': lat_, 'isFit': isFit_, 'route': route_, 'worker': worker_, 'flowerRemark': flowerRemark_, 'env': env_, 'remark': remark_, 'pics': pics_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'province': province_, 'city': city_, 'address': address_, 'lng': lng_, 'lat': lat_, 'isFit': isFit_, 'route': route_, 'worker': worker_, 'flowerRemark': flowerRemark_, 'env': env_, 'remark': remark_, 'pics': pics_}
        response = self.request.post(url=self.url+'/mobile/work-log/add-seek', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_work_log_detail_extract(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/work-log/detail-extract', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_work_log_detail_keep(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/work-log/detail-keep', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_work_log_detail_seek(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/mobile/work-log/detail-seek', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_work_log_edit_extract(self, logId_=None, nectarSourceId_=None, worker_=None, workerNum_=None, cost_=None, remark_=None, pics_=None):
        if self.user is None:
            data = {'logId': logId_, 'nectarSourceId': nectarSourceId_, 'worker': worker_, 'workerNum': workerNum_, 'cost': cost_, 'remark': remark_, 'pics': pics_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'logId': logId_, 'nectarSourceId': nectarSourceId_, 'worker': worker_, 'workerNum': workerNum_, 'cost': cost_, 'remark': remark_, 'pics': pics_}
        response = self.request.post(url=self.url+'/mobile/work-log/edit-extract', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_work_log_edit_keep(self, logId_=None, gatherHoneyRemark_=None, gatherPollenRemark_=None, detail_=None):
        if self.user is None:
            data = {'logId': logId_, 'gatherHoneyRemark': gatherHoneyRemark_, 'gatherPollenRemark': gatherPollenRemark_, 'detail': detail_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'logId': logId_, 'gatherHoneyRemark': gatherHoneyRemark_, 'gatherPollenRemark': gatherPollenRemark_, 'detail': detail_}
        response = self.request.post(url=self.url+'/mobile/work-log/edit-keep', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_work_log_edit_seek(self, logId_=None, isFit_=None, route_=None, worker_=None, flowerRemark_=None, env_=None, remark_=None, pics_=None):
        if self.user is None:
            data = {'logId': logId_, 'isFit': isFit_, 'route': route_, 'worker': worker_, 'flowerRemark': flowerRemark_, 'env': env_, 'remark': remark_, 'pics': pics_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'logId': logId_, 'isFit': isFit_, 'route': route_, 'worker': worker_, 'flowerRemark': flowerRemark_, 'env': env_, 'remark': remark_, 'pics': pics_}
        response = self.request.post(url=self.url+'/mobile/work-log/edit-seek', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_work_log_page_list(self, pn_=None, ps_=None, onlySelf_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'onlySelf': onlySelf_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'onlySelf': onlySelf_}
        response = self.request.post(url=self.url+'/mobile/work-log/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_workbench_bee_friend_add(self, curNectarType_=None, labelType_=None, regularSource_=None, intention_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, vehicleLength_=None, expectHiveNum_=None, pics_=None, scale_=None, hiveNum_=None, standardNum_=None, smallNum_=None, queenType_=None, queenNum2_=None, queenNum1_=None, queenNum_=None, ekeNum_=None, platNum_=None, babyNum_=None, honeyNum_=None, remark_=None, nextNectarSource_=None, nextSourceEnterTime_=None, joinDate_=None, leaveDate_=None, contactNumber_=None, realName_=None, age_=None, gender_=None, nativeProvince_=None, nativeCity_=None, nativeCounty_=None, seniority_=None, regularRoute_=None, studyFrom_=None, heir_=None, yield_=None, income_=None, breedTime1_=None, breedPlace1_=None, breedTime2_=None, breedPlace2_=None, saleNum_=None, intentionPrice_=None, saleTime_=None, saleProvince_=None, saleCity_=None, saleCounty_=None, altitude_=None, distantPic_=None, tentPic_=None, sitePic_=None, roadPic_=None):
        if self.user is None:
            data = {'curNectarType': curNectarType_, 'labelType': labelType_, 'regularSource': regularSource_, 'intention': intention_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'vehicleLength': vehicleLength_, 'expectHiveNum': expectHiveNum_, 'pics': pics_, 'scale': scale_, 'hiveNum': hiveNum_, 'standardNum': standardNum_, 'smallNum': smallNum_, 'queenType': queenType_, 'queenNum2': queenNum2_, 'queenNum1': queenNum1_, 'queenNum': queenNum_, 'ekeNum': ekeNum_, 'platNum': platNum_, 'babyNum': babyNum_, 'honeyNum': honeyNum_, 'remark': remark_, 'nextNectarSource': nextNectarSource_, 'nextSourceEnterTime': nextSourceEnterTime_, 'joinDate': joinDate_, 'leaveDate': leaveDate_, 'contactNumber': contactNumber_, 'realName': realName_, 'age': age_, 'gender': gender_, 'nativeProvince': nativeProvince_, 'nativeCity': nativeCity_, 'nativeCounty': nativeCounty_, 'seniority': seniority_, 'regularRoute': regularRoute_, 'studyFrom': studyFrom_, 'heir': heir_, 'yield': yield_, 'income': income_, 'breedTime1': breedTime1_, 'breedPlace1': breedPlace1_, 'breedTime2': breedTime2_, 'breedPlace2': breedPlace2_, 'saleNum': saleNum_, 'intentionPrice': intentionPrice_, 'saleTime': saleTime_, 'saleProvince': saleProvince_, 'saleCity': saleCity_, 'saleCounty': saleCounty_, 'altitude': altitude_, 'distantPic': distantPic_, 'tentPic': tentPic_, 'sitePic': sitePic_, 'roadPic': roadPic_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'curNectarType': curNectarType_, 'labelType': labelType_, 'regularSource': regularSource_, 'intention': intention_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'vehicleLength': vehicleLength_, 'expectHiveNum': expectHiveNum_, 'pics': pics_, 'scale': scale_, 'hiveNum': hiveNum_, 'standardNum': standardNum_, 'smallNum': smallNum_, 'queenType': queenType_, 'queenNum2': queenNum2_, 'queenNum1': queenNum1_, 'queenNum': queenNum_, 'ekeNum': ekeNum_, 'platNum': platNum_, 'babyNum': babyNum_, 'honeyNum': honeyNum_, 'remark': remark_, 'nextNectarSource': nextNectarSource_, 'nextSourceEnterTime': nextSourceEnterTime_, 'joinDate': joinDate_, 'leaveDate': leaveDate_, 'contactNumber': contactNumber_, 'realName': realName_, 'age': age_, 'gender': gender_, 'nativeProvince': nativeProvince_, 'nativeCity': nativeCity_, 'nativeCounty': nativeCounty_, 'seniority': seniority_, 'regularRoute': regularRoute_, 'studyFrom': studyFrom_, 'heir': heir_, 'yield': yield_, 'income': income_, 'breedTime1': breedTime1_, 'breedPlace1': breedPlace1_, 'breedTime2': breedTime2_, 'breedPlace2': breedPlace2_, 'saleNum': saleNum_, 'intentionPrice': intentionPrice_, 'saleTime': saleTime_, 'saleProvince': saleProvince_, 'saleCity': saleCity_, 'saleCounty': saleCounty_, 'altitude': altitude_, 'distantPic': distantPic_, 'tentPic': tentPic_, 'sitePic': sitePic_, 'roadPic': roadPic_}
        response = self.request.post(url=self.url+'/mobile/workbench-bee-friend/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_workbench_bee_friend_add_check(self, userId_=None, mobile_=None):
        if self.user is None:
            data = {'userId': userId_, 'mobile': mobile_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_, 'mobile': mobile_}
        response = self.request.post(url=self.url+'/mobile/workbench-bee-friend/add-check', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_workbench_bee_friend_detail(self, id_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'id': id_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/mobile/workbench-bee-friend/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_workbench_bee_friend_edit(self, regularSource_=None, labelType_=None, intention_=None, id_=None, realName_=None, contactNumber_=None, gender_=None, nativeProvince_=None, nativeCity_=None, nativeCounty_=None, age_=None, seniority_=None, regularRoute_=None, studyFrom_=None, heir_=None, yield_=None, income_=None, breedTime1_=None, breedPlace1_=None, breedTime2_=None, breedPlace2_=None, saleNum_=None, intentionPrice_=None, saleTime_=None, saleProvince_=None, saleCity_=None, saleCounty_=None):
        if self.user is None:
            data = {'regularSource': regularSource_, 'labelType': labelType_, 'intention': intention_, 'id': id_, 'realName': realName_, 'contactNumber': contactNumber_, 'gender': gender_, 'nativeProvince': nativeProvince_, 'nativeCity': nativeCity_, 'nativeCounty': nativeCounty_, 'age': age_, 'seniority': seniority_, 'regularRoute': regularRoute_, 'studyFrom': studyFrom_, 'heir': heir_, 'yield': yield_, 'income': income_, 'breedTime1': breedTime1_, 'breedPlace1': breedPlace1_, 'breedTime2': breedTime2_, 'breedPlace2': breedPlace2_, 'saleNum': saleNum_, 'intentionPrice': intentionPrice_, 'saleTime': saleTime_, 'saleProvince': saleProvince_, 'saleCity': saleCity_, 'saleCounty': saleCounty_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'regularSource': regularSource_, 'labelType': labelType_, 'intention': intention_, 'id': id_, 'realName': realName_, 'contactNumber': contactNumber_, 'gender': gender_, 'nativeProvince': nativeProvince_, 'nativeCity': nativeCity_, 'nativeCounty': nativeCounty_, 'age': age_, 'seniority': seniority_, 'regularRoute': regularRoute_, 'studyFrom': studyFrom_, 'heir': heir_, 'yield': yield_, 'income': income_, 'breedTime1': breedTime1_, 'breedPlace1': breedPlace1_, 'breedTime2': breedTime2_, 'breedPlace2': breedPlace2_, 'saleNum': saleNum_, 'intentionPrice': intentionPrice_, 'saleTime': saleTime_, 'saleProvince': saleProvince_, 'saleCity': saleCity_, 'saleCounty': saleCounty_}
        response = self.request.post(url=self.url+'/mobile/workbench-bee-friend/edit', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_workbench_bee_friend_mobile_check(self, userId_=None, mobile_=None):
        if self.user is None:
            data = {'userId': userId_, 'mobile': mobile_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'userId': userId_, 'mobile': mobile_}
        response = self.request.post(url=self.url+'/mobile/workbench-bee-friend/mobile-check', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _mobile_workbench_bee_friend_page_list(self, intentions_=None, businessLabels_=None, pn_=None, ps_=None, searchKey_=None, searchType_=None, province_=None, city_=None, county_=None, lng_=None, lat_=None, distanceType_=None, sortType_=None, onlySelf_=None, registed_=None):
        if self.user is None:
            data = {'intentions': intentions_, 'businessLabels': businessLabels_, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'searchType': searchType_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'distanceType': distanceType_, 'sortType': sortType_, 'onlySelf': onlySelf_, 'registed': registed_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'intentions': intentions_, 'businessLabels': businessLabels_, 'pn': pn_, 'ps': ps_, 'searchKey': searchKey_, 'searchType': searchType_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'distanceType': distanceType_, 'sortType': sortType_, 'onlySelf': onlySelf_, 'registed': registed_}
        response = self.request.post(url=self.url+'/mobile/workbench-bee-friend/page-list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _region_common_search(self, searchContent_=None):
        if self.user is None:
            data = {'searchContent': searchContent_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'searchContent': searchContent_}
        response = self.request.post(url=self.url+'/region/common/search', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_help_comment_list(self, pn_=None, ps_=None, helpInfoId_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'helpInfoId': helpInfoId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'helpInfoId': helpInfoId_}
        response = self.request.post(url=self.url+'/web/help-comment/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_help_info_detail(self, helpInfoId_=None, lng_=None, lat_=None, readStatus_=None):
        if self.user is None:
            data = {'helpInfoId': helpInfoId_, 'lng': lng_, 'lat': lat_, 'readStatus': readStatus_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'helpInfoId': helpInfoId_, 'lng': lng_, 'lat': lat_, 'readStatus': readStatus_}
        response = self.request.post(url=self.url+'/web/help-info/detail', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_map_mark_group_add(self, name_=None):
        if self.user is None:
            data = {'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_}
        response = self.request.post(url=self.url+'/web/map-mark-group/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_map_mark_group_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/web/map-mark-group/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_map_mark_group_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/map-mark-group/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_map_mark_group_update(self, id_=None, name_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_}
        response = self.request.post(url=self.url+'/web/map-mark-group/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_map_mark_add(self, markGroupId_=None, name_=None, lng_=None, color_=None, lat_=None):
        if self.user is None:
            data = {'markGroupId': markGroupId_, 'name': name_, 'lng': lng_, 'color': color_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'markGroupId': markGroupId_, 'name': name_, 'lng': lng_, 'color': color_, 'lat': lat_}
        response = self.request.post(url=self.url+'/web/map-mark/add', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_map_mark_del(self, id_=None):
        if self.user is None:
            data = {'id': id_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_}
        response = self.request.post(url=self.url+'/web/map-mark/del', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_map_mark_list(self, markGroupId_=None):
        if self.user is None:
            data = {'markGroupId': markGroupId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'markGroupId': markGroupId_}
        response = self.request.post(url=self.url+'/web/map-mark/list', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_map_mark_update(self, id_=None, markGroupId_=None, name_=None, lng_=None, color_=None, lat_=None):
        if self.user is None:
            data = {'id': id_, 'markGroupId': markGroupId_, 'name': name_, 'lng': lng_, 'color': color_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'markGroupId': markGroupId_, 'name': name_, 'lng': lng_, 'color': color_, 'lat': lat_}
        response = self.request.post(url=self.url+'/web/map-mark/update', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_wx_getAccessToken(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/wx/getAccessToken', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_wx_refreshAccessToken(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/web/wx/refreshAccessToken', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_wx_refreshSignature(self, url_=None):
        if self.user is None:
            data = {'url': url_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'url': url_}
        response = self.request.post(url=self.url+'/web/wx/refreshSignature', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))

    def _web_wx_signature(self, url_=None):
        if self.user is None:
            data = {'url': url_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'url': url_}
        response = self.request.post(url=self.url+'/web/wx/signature', data=data, hosts=self.url)
        return self.__judge_response_status(json.loads(response))
