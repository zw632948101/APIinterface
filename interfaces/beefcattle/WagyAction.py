#! /usr/bin/env python
# encoding: utf-8

from utils.dataRequest.dataRequester import Request
from utils.environmentConfiguration import config
from utils.userInfo.GetUserInfo import User
from utils.checkApiChanges.checher.apiTestResult import apiTestResult
import json


class wagyAction(object):
    def __init__(self):
        self.request = Request()
        self.url = config.get('hosts').get(config.get('run')).get('BF_WAGY')

    def set_user(self, mobile=None, account_type='user', **kwargs):
        if mobile is None:
            self.user = None
        else:
            self.user = User(mobile, account_type, **kwargs)
            self.request.headers.update({"_Device-Id_": self.user.device_id})
            self.request.headers.update({"_Token_": self.user.token})
        return self.user

    def __judge_response_status(self, json_response):
        if json_response['status'] in ("OK", "ERROR"):
            return json_response
        else:
            raise Exception('status未返回OK或ERROR')

    def _admin_cattle_farm_add(self, pics_=None, farmName_=None, ownerName_=None, sellTo_=None, farmScale_=None, actualOwnCount_=None, cattleSource_=None, contactName_=None, contactPhone_=None, breedType_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, categoryAddInputs_=None, extendAddInput_=None):
        if self.user is None:
            data = {'pics': pics_, 'farmName': farmName_, 'ownerName': ownerName_, 'sellTo': sellTo_, 'farmScale': farmScale_, 'actualOwnCount': actualOwnCount_, 'cattleSource': cattleSource_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'breedType': breedType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'categoryAddInputs': categoryAddInputs_, 'extendAddInput': extendAddInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'farmName': farmName_, 'ownerName': ownerName_, 'sellTo': sellTo_, 'farmScale': farmScale_, 'actualOwnCount': actualOwnCount_, 'cattleSource': cattleSource_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'breedType': breedType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'categoryAddInputs': categoryAddInputs_, 'extendAddInput': extendAddInput_}
        response = self.request.post(url=self.url+'/admin/cattle-farm/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle-farm/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_farm_detail(self, cattleFarmId_=None):
        if self.user is None:
            data = {'cattleFarmId': cattleFarmId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleFarmId': cattleFarmId_}
        response = self.request.post(url=self.url+'/admin/cattle-farm/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle-farm/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_farm_edit(self, id_=None, farmName_=None, ownerName_=None, sellTo_=None, farmScale_=None, actualOwnCount_=None, cattleSource_=None, contactName_=None, contactPhone_=None, breedType_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, categoryAddInputs_=None):
        if self.user is None:
            data = {'id': id_, 'farmName': farmName_, 'ownerName': ownerName_, 'sellTo': sellTo_, 'farmScale': farmScale_, 'actualOwnCount': actualOwnCount_, 'cattleSource': cattleSource_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'breedType': breedType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'categoryAddInputs': categoryAddInputs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'farmName': farmName_, 'ownerName': ownerName_, 'sellTo': sellTo_, 'farmScale': farmScale_, 'actualOwnCount': actualOwnCount_, 'cattleSource': cattleSource_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'breedType': breedType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'categoryAddInputs': categoryAddInputs_}
        response = self.request.post(url=self.url+'/admin/cattle-farm/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle-farm/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_farm_edit_extend(self, pics_=None, id_=None, cattleFarmId_=None, slaughterSellStatus_=None, growRoughageStatus_=None, roughagePurchaseWay_=None, grazeStatus_=None, feedProcessStatus_=None, silageCellarStatus_=None, liveCattleIndexStatus_=None, addFencePlanStatus_=None, organicFertilizerStatus_=None, autoFeedStatus_=None, dealFaecesType_=None, nearbyBreedState_=None, cowshedType_=None):
        if self.user is None:
            data = {'pics': pics_, 'id': id_, 'cattleFarmId': cattleFarmId_, 'slaughterSellStatus': slaughterSellStatus_, 'growRoughageStatus': growRoughageStatus_, 'roughagePurchaseWay': roughagePurchaseWay_, 'grazeStatus': grazeStatus_, 'feedProcessStatus': feedProcessStatus_, 'silageCellarStatus': silageCellarStatus_, 'liveCattleIndexStatus': liveCattleIndexStatus_, 'addFencePlanStatus': addFencePlanStatus_, 'organicFertilizerStatus': organicFertilizerStatus_, 'autoFeedStatus': autoFeedStatus_, 'dealFaecesType': dealFaecesType_, 'nearbyBreedState': nearbyBreedState_, 'cowshedType': cowshedType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'id': id_, 'cattleFarmId': cattleFarmId_, 'slaughterSellStatus': slaughterSellStatus_, 'growRoughageStatus': growRoughageStatus_, 'roughagePurchaseWay': roughagePurchaseWay_, 'grazeStatus': grazeStatus_, 'feedProcessStatus': feedProcessStatus_, 'silageCellarStatus': silageCellarStatus_, 'liveCattleIndexStatus': liveCattleIndexStatus_, 'addFencePlanStatus': addFencePlanStatus_, 'organicFertilizerStatus': organicFertilizerStatus_, 'autoFeedStatus': autoFeedStatus_, 'dealFaecesType': dealFaecesType_, 'nearbyBreedState': nearbyBreedState_, 'cowshedType': cowshedType_}
        response = self.request.post(url=self.url+'/admin/cattle-farm/edit-extend', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle-farm/edit-extend', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_cattle_farm_list(self, pn_=None, ps_=None, farmName_=None, province_=None, city_=None, county_=None, lng_=None, lat_=None, startTime_=None, endTime_=None, searchKey_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'farmName': farmName_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'startTime': startTime_, 'endTime': endTime_, 'searchKey': searchKey_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'farmName': farmName_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'startTime': startTime_, 'endTime': endTime_, 'searchKey': searchKey_}
        response = self.request.post(url=self.url+'/admin/cattle-farm/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/cattle-farm/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_company_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/admin/company/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/company/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_farm_retail_detail(self, farmRetailId_=None):
        if self.user is None:
            data = {'farmRetailId': farmRetailId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'farmRetailId': farmRetailId_}
        response = self.request.post(url=self.url+'/admin/farm-retail/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/farm-retail/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_farm_retail_detail_extend(self, farmRetailId_=None):
        if self.user is None:
            data = {'farmRetailId': farmRetailId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'farmRetailId': farmRetailId_}
        response = self.request.post(url=self.url+'/admin/farm-retail/detail-extend', data=data, hosts=self.url)
        apiTestResult(api='/admin/farm-retail/detail-extend', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_farm_retail_list(self, pn_=None, ps_=None, province_=None, city_=None, county_=None, startTime_=None, endTime_=None, categoryType_=None, searchKey_=None, creatorKey_=None, lat_=None, lng_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'categoryType': categoryType_, 'searchKey': searchKey_, 'creatorKey': creatorKey_, 'lat': lat_, 'lng': lng_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'categoryType': categoryType_, 'searchKey': searchKey_, 'creatorKey': creatorKey_, 'lat': lat_, 'lng': lng_}
        response = self.request.post(url=self.url+'/admin/farm-retail/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/farm-retail/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_land_detail(self, landId_=None):
        if self.user is None:
            data = {'landId': landId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'landId': landId_}
        response = self.request.post(url=self.url+'/admin/land/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/land/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_land_edit(self, id_=None, landArea_=None, circulationStartTime_=None, circulationEndTime_=None, landLocationAddInput_=None, landTradeAddInput_=None):
        if self.user is None:
            data = {'id': id_, 'landArea': landArea_, 'circulationStartTime': circulationStartTime_, 'circulationEndTime': circulationEndTime_, 'landLocationAddInput': landLocationAddInput_, 'landTradeAddInput': landTradeAddInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'landArea': landArea_, 'circulationStartTime': circulationStartTime_, 'circulationEndTime': circulationEndTime_, 'landLocationAddInput': landLocationAddInput_, 'landTradeAddInput': landTradeAddInput_}
        response = self.request.post(url=self.url+'/admin/land/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/land/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_land_editNotCirculation(self, id_=None, landArea_=None, lng_=None, lat_=None, province_=None, city_=None, county_=None, address_=None, landType_=None, plantType_=None, plantOtherName_=None, vehicleLength_=None, villageName_=None, contactName_=None, contactPhone_=None, remark_=None, bizAttachAddInputs_=None, landUse_=None, raiseCrops_=None, raiseCropsOther_=None, plantWay_=None, landLocationAddInput_=None, landTradeAddInput_=None):
        if self.user is None:
            data = {'id': id_, 'landArea': landArea_, 'lng': lng_, 'lat': lat_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'landType': landType_, 'plantType': plantType_, 'plantOtherName': plantOtherName_, 'vehicleLength': vehicleLength_, 'villageName': villageName_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'remark': remark_, 'bizAttachAddInputs': bizAttachAddInputs_, 'landUse': landUse_, 'raiseCrops': raiseCrops_, 'raiseCropsOther': raiseCropsOther_, 'plantWay': plantWay_, 'landLocationAddInput': landLocationAddInput_, 'landTradeAddInput': landTradeAddInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'landArea': landArea_, 'lng': lng_, 'lat': lat_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'landType': landType_, 'plantType': plantType_, 'plantOtherName': plantOtherName_, 'vehicleLength': vehicleLength_, 'villageName': villageName_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'remark': remark_, 'bizAttachAddInputs': bizAttachAddInputs_, 'landUse': landUse_, 'raiseCrops': raiseCrops_, 'raiseCropsOther': raiseCropsOther_, 'plantWay': plantWay_, 'landLocationAddInput': landLocationAddInput_, 'landTradeAddInput': landTradeAddInput_}
        response = self.request.post(url=self.url+'/admin/land/editNotCirculation', data=data, hosts=self.url)
        apiTestResult(api='/admin/land/editNotCirculation', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_land_page_list(self, pn_=None, ps_=None, startTime_=None, endTime_=None, province_=None, city_=None, county_=None, searchKey_=None, circulationStartTime_=None, circulationEndTime_=None, landAreaBegin_=None, landAreaEnd_=None, plantType_=None, vehicleLength_=None, creatorKey_=None, landUse_=None, status_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'startTime': startTime_, 'endTime': endTime_, 'province': province_, 'city': city_, 'county': county_, 'searchKey': searchKey_, 'circulationStartTime': circulationStartTime_, 'circulationEndTime': circulationEndTime_, 'landAreaBegin': landAreaBegin_, 'landAreaEnd': landAreaEnd_, 'plantType': plantType_, 'vehicleLength': vehicleLength_, 'creatorKey': creatorKey_, 'landUse': landUse_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'startTime': startTime_, 'endTime': endTime_, 'province': province_, 'city': city_, 'county': county_, 'searchKey': searchKey_, 'circulationStartTime': circulationStartTime_, 'circulationEndTime': circulationEndTime_, 'landAreaBegin': landAreaBegin_, 'landAreaEnd': landAreaEnd_, 'plantType': plantType_, 'vehicleLength': vehicleLength_, 'creatorKey': creatorKey_, 'landUse': landUse_, 'status': status_}
        response = self.request.post(url=self.url+'/admin/land/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/land/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_landLocation_detail(self, landId_=None):
        if self.user is None:
            data = {'landId': landId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'landId': landId_}
        response = self.request.post(url=self.url+'/admin/landLocation/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/landLocation/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_service_point_add(self, pointName_=None, pointType_=None, managerName_=None, managerPhone_=None, farmScale_=None, status_=None, subjectId_=None, openBusiness_=None, landId_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, bizAttachAddInputs_=None):
        if self.user is None:
            data = {'pointName': pointName_, 'pointType': pointType_, 'managerName': managerName_, 'managerPhone': managerPhone_, 'farmScale': farmScale_, 'status': status_, 'subjectId': subjectId_, 'openBusiness': openBusiness_, 'landId': landId_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'bizAttachAddInputs': bizAttachAddInputs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pointName': pointName_, 'pointType': pointType_, 'managerName': managerName_, 'managerPhone': managerPhone_, 'farmScale': farmScale_, 'status': status_, 'subjectId': subjectId_, 'openBusiness': openBusiness_, 'landId': landId_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'bizAttachAddInputs': bizAttachAddInputs_}
        response = self.request.post(url=self.url+'/admin/service-point/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/service-point/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_service_point_detail(self, servicePointId_=None):
        if self.user is None:
            data = {'servicePointId': servicePointId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'servicePointId': servicePointId_}
        response = self.request.post(url=self.url+'/admin/service-point/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/service-point/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_service_point_edit(self, id_=None, pointName_=None, pointType_=None, managerName_=None, managerPhone_=None, farmScale_=None, status_=None, subjectId_=None, openBusiness_=None, landId_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, bizAttachAddInputs_=None):
        if self.user is None:
            data = {'id': id_, 'pointName': pointName_, 'pointType': pointType_, 'managerName': managerName_, 'managerPhone': managerPhone_, 'farmScale': farmScale_, 'status': status_, 'subjectId': subjectId_, 'openBusiness': openBusiness_, 'landId': landId_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'bizAttachAddInputs': bizAttachAddInputs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'pointName': pointName_, 'pointType': pointType_, 'managerName': managerName_, 'managerPhone': managerPhone_, 'farmScale': farmScale_, 'status': status_, 'subjectId': subjectId_, 'openBusiness': openBusiness_, 'landId': landId_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'bizAttachAddInputs': bizAttachAddInputs_}
        response = self.request.post(url=self.url+'/admin/service-point/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/service-point/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_service_point_list(self, pn_=None, ps_=None, province_=None, city_=None, county_=None, startTime_=None, endTime_=None, pointType_=None, lat_=None, lng_=None, pointName_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'pointType': pointType_, 'lat': lat_, 'lng': lng_, 'pointName': pointName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'pointType': pointType_, 'lat': lat_, 'lng': lng_, 'pointName': pointName_}
        response = self.request.post(url=self.url+'/admin/service-point/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/service-point/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_service_point_map_list(self, pn_=None, ps_=None, province_=None, city_=None, county_=None, startTime_=None, endTime_=None, pointType_=None, lat_=None, lng_=None, pointName_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'pointType': pointType_, 'lat': lat_, 'lng': lng_, 'pointName': pointName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'pointType': pointType_, 'lat': lat_, 'lng': lng_, 'pointName': pointName_}
        response = self.request.post(url=self.url+'/admin/service-point/map-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/service-point/map-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_slaughter_company_add(self, pics_=None, companyName_=None, slaughterScale_=None, actualSlaughterCount_=None, cattleSource_=None, quarantineCondition_=None, purchaseStandard_=None, settleMethod_=None, priceType_=None, contactName_=None, contactPhone_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, extendAddInput_=None):
        if self.user is None:
            data = {'pics': pics_, 'companyName': companyName_, 'slaughterScale': slaughterScale_, 'actualSlaughterCount': actualSlaughterCount_, 'cattleSource': cattleSource_, 'quarantineCondition': quarantineCondition_, 'purchaseStandard': purchaseStandard_, 'settleMethod': settleMethod_, 'priceType': priceType_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'extendAddInput': extendAddInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'companyName': companyName_, 'slaughterScale': slaughterScale_, 'actualSlaughterCount': actualSlaughterCount_, 'cattleSource': cattleSource_, 'quarantineCondition': quarantineCondition_, 'purchaseStandard': purchaseStandard_, 'settleMethod': settleMethod_, 'priceType': priceType_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'extendAddInput': extendAddInput_}
        response = self.request.post(url=self.url+'/admin/slaughter-company/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/slaughter-company/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_slaughter_company_detail(self, companyId_=None):
        if self.user is None:
            data = {'companyId': companyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'companyId': companyId_}
        response = self.request.post(url=self.url+'/admin/slaughter-company/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/slaughter-company/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_slaughter_company_edit(self, id_=None, companyName_=None, slaughterScale_=None, actualSlaughterCount_=None, cattleSource_=None, quarantineCondition_=None, purchaseStandard_=None, settleMethod_=None, priceType_=None, contactName_=None, contactPhone_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'id': id_, 'companyName': companyName_, 'slaughterScale': slaughterScale_, 'actualSlaughterCount': actualSlaughterCount_, 'cattleSource': cattleSource_, 'quarantineCondition': quarantineCondition_, 'purchaseStandard': purchaseStandard_, 'settleMethod': settleMethod_, 'priceType': priceType_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'companyName': companyName_, 'slaughterScale': slaughterScale_, 'actualSlaughterCount': actualSlaughterCount_, 'cattleSource': cattleSource_, 'quarantineCondition': quarantineCondition_, 'purchaseStandard': purchaseStandard_, 'settleMethod': settleMethod_, 'priceType': priceType_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/admin/slaughter-company/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/slaughter-company/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_slaughter_company_edit_extend(self, pics_=None, id_=None, companyId_=None, acidDischargeStatus_=None, halalAuthStatus_=None, countryStoreStatus_=None, insteadSlaughterProcessFeeStatus_=None, saleProducts_=None, saleChannel_=None, bodyDealCondition_=None, dealFaecesType_=None, productionFactory_=None):
        if self.user is None:
            data = {'pics': pics_, 'id': id_, 'companyId': companyId_, 'acidDischargeStatus': acidDischargeStatus_, 'halalAuthStatus': halalAuthStatus_, 'countryStoreStatus': countryStoreStatus_, 'insteadSlaughterProcessFeeStatus': insteadSlaughterProcessFeeStatus_, 'saleProducts': saleProducts_, 'saleChannel': saleChannel_, 'bodyDealCondition': bodyDealCondition_, 'dealFaecesType': dealFaecesType_, 'productionFactory': productionFactory_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'id': id_, 'companyId': companyId_, 'acidDischargeStatus': acidDischargeStatus_, 'halalAuthStatus': halalAuthStatus_, 'countryStoreStatus': countryStoreStatus_, 'insteadSlaughterProcessFeeStatus': insteadSlaughterProcessFeeStatus_, 'saleProducts': saleProducts_, 'saleChannel': saleChannel_, 'bodyDealCondition': bodyDealCondition_, 'dealFaecesType': dealFaecesType_, 'productionFactory': productionFactory_}
        response = self.request.post(url=self.url+'/admin/slaughter-company/edit-extend', data=data, hosts=self.url)
        apiTestResult(api='/admin/slaughter-company/edit-extend', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_slaughter_company_list(self, pn_=None, ps_=None, companyName_=None, province_=None, city_=None, county_=None, startTime_=None, endTime_=None, searchKey_=None, lat_=None, lng_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'companyName': companyName_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'searchKey': searchKey_, 'lat': lat_, 'lng': lng_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'companyName': companyName_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'searchKey': searchKey_, 'lat': lat_, 'lng': lng_}
        response = self.request.post(url=self.url+'/admin/slaughter-company/list', data=data, hosts=self.url)
        apiTestResult(api='/admin/slaughter-company/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_tradeCenter_add(self, name_=None, tradeTime_=None, historyTurnover_=None, brokerCount_=None, cattleSource_=None, cattleSourceType_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, contactPhone_=None, brokerName_=None, brokerContactPhone_=None, farmerName_=None, famerContactPhone_=None, tradeCenterFeeAddInput_=None, tradeCenterExtendAddInput_=None, tradeCategoryAddInputs_=None, bizAttachAddInputs_=None):
        if self.user is None:
            data = {'name': name_, 'tradeTime': tradeTime_, 'historyTurnover': historyTurnover_, 'brokerCount': brokerCount_, 'cattleSource': cattleSource_, 'cattleSourceType': cattleSourceType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'contactPhone': contactPhone_, 'brokerName': brokerName_, 'brokerContactPhone': brokerContactPhone_, 'farmerName': farmerName_, 'famerContactPhone': famerContactPhone_, 'tradeCenterFeeAddInput': tradeCenterFeeAddInput_, 'tradeCenterExtendAddInput': tradeCenterExtendAddInput_, 'tradeCategoryAddInputs': tradeCategoryAddInputs_, 'bizAttachAddInputs': bizAttachAddInputs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'tradeTime': tradeTime_, 'historyTurnover': historyTurnover_, 'brokerCount': brokerCount_, 'cattleSource': cattleSource_, 'cattleSourceType': cattleSourceType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'contactPhone': contactPhone_, 'brokerName': brokerName_, 'brokerContactPhone': brokerContactPhone_, 'farmerName': farmerName_, 'famerContactPhone': famerContactPhone_, 'tradeCenterFeeAddInput': tradeCenterFeeAddInput_, 'tradeCenterExtendAddInput': tradeCenterExtendAddInput_, 'tradeCategoryAddInputs': tradeCategoryAddInputs_, 'bizAttachAddInputs': bizAttachAddInputs_}
        response = self.request.post(url=self.url+'/admin/tradeCenter/add', data=data, hosts=self.url)
        apiTestResult(api='/admin/tradeCenter/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_tradeCenter_detail(self, tradeCenterId_=None):
        if self.user is None:
            data = {'tradeCenterId': tradeCenterId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'tradeCenterId': tradeCenterId_}
        response = self.request.post(url=self.url+'/admin/tradeCenter/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/tradeCenter/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_tradeCenter_edit(self, id_=None, name_=None, tradeTime_=None, historyTurnover_=None, brokerCount_=None, cattleSource_=None, cattleSourceType_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, contactPhone_=None, brokerName_=None, brokerContactPhone_=None, farmerName_=None, famerContactPhone_=None, tradeCategoryEditInputs_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, 'tradeTime': tradeTime_, 'historyTurnover': historyTurnover_, 'brokerCount': brokerCount_, 'cattleSource': cattleSource_, 'cattleSourceType': cattleSourceType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'contactPhone': contactPhone_, 'brokerName': brokerName_, 'brokerContactPhone': brokerContactPhone_, 'farmerName': farmerName_, 'famerContactPhone': famerContactPhone_, 'tradeCategoryEditInputs': tradeCategoryEditInputs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_, 'tradeTime': tradeTime_, 'historyTurnover': historyTurnover_, 'brokerCount': brokerCount_, 'cattleSource': cattleSource_, 'cattleSourceType': cattleSourceType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'contactPhone': contactPhone_, 'brokerName': brokerName_, 'brokerContactPhone': brokerContactPhone_, 'farmerName': farmerName_, 'famerContactPhone': famerContactPhone_, 'tradeCategoryEditInputs': tradeCategoryEditInputs_}
        response = self.request.post(url=self.url+'/admin/tradeCenter/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/tradeCenter/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_tradeCenter_page_list(self, pn_=None, ps_=None, startTime_=None, endTime_=None, province_=None, city_=None, county_=None, name_=None, contactPhone_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'startTime': startTime_, 'endTime': endTime_, 'province': province_, 'city': city_, 'county': county_, 'name': name_, 'contactPhone': contactPhone_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'startTime': startTime_, 'endTime': endTime_, 'province': province_, 'city': city_, 'county': county_, 'name': name_, 'contactPhone': contactPhone_}
        response = self.request.post(url=self.url+'/admin/tradeCenter/page-list', data=data, hosts=self.url)
        apiTestResult(api='/admin/tradeCenter/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_tradeCenterFee_detail(self, tradeCenterId_=None):
        if self.user is None:
            data = {'tradeCenterId': tradeCenterId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'tradeCenterId': tradeCenterId_}
        response = self.request.post(url=self.url+'/admin/tradeCenterFee/detail', data=data, hosts=self.url)
        apiTestResult(api='/admin/tradeCenterFee/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _admin_tradeCenterFee_edit(self, tradeCenterId_=None, setleType_=None, settleTime_=None, depositPayType_=None, entryFee_=None, exitFee_=None, quarantineFee_=None, fenceFee_=None, siteFee_=None, dealPrice_=None, tradeCenterExtendAddInput_=None, bizAttachAddInputs_=None):
        if self.user is None:
            data = {'tradeCenterId': tradeCenterId_, 'setleType': setleType_, 'settleTime': settleTime_, 'depositPayType': depositPayType_, 'entryFee': entryFee_, 'exitFee': exitFee_, 'quarantineFee': quarantineFee_, 'fenceFee': fenceFee_, 'siteFee': siteFee_, 'dealPrice': dealPrice_, 'tradeCenterExtendAddInput': tradeCenterExtendAddInput_, 'bizAttachAddInputs': bizAttachAddInputs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'tradeCenterId': tradeCenterId_, 'setleType': setleType_, 'settleTime': settleTime_, 'depositPayType': depositPayType_, 'entryFee': entryFee_, 'exitFee': exitFee_, 'quarantineFee': quarantineFee_, 'fenceFee': fenceFee_, 'siteFee': siteFee_, 'dealPrice': dealPrice_, 'tradeCenterExtendAddInput': tradeCenterExtendAddInput_, 'bizAttachAddInputs': bizAttachAddInputs_}
        response = self.request.post(url=self.url+'/admin/tradeCenterFee/edit', data=data, hosts=self.url)
        apiTestResult(api='/admin/tradeCenterFee/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_land_list(self, city_=None, county_=None, landUse_=None, province_=None):
        if self.user is None:
            data = {'city': city_, 'county': county_, 'landUse': landUse_, 'province': province_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'city': city_, 'county': county_, 'landUse': landUse_, 'province': province_}
        response = self.request.post(url=self.url+'/api/land/list', data=data, hosts=self.url)
        apiTestResult(api='/api/land/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_land_stopCirculation_task(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/api/land/stopCirculation-task', data=data, hosts=self.url)
        apiTestResult(api='/api/land/stopCirculation-task', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_service_point_detail(self, servicePointId_=None):
        if self.user is None:
            data = {'servicePointId': servicePointId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'servicePointId': servicePointId_}
        response = self.request.post(url=self.url+'/api/service-point/detail', data=data, hosts=self.url)
        apiTestResult(api='/api/service-point/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_service_point_list(self, ids_=None):
        if self.user is None:
            data = {'ids': ids_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'ids': ids_}
        response = self.request.post(url=self.url+'/api/service-point/list', data=data, hosts=self.url)
        apiTestResult(api='/api/service-point/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _api_service_point_subject_list(self, subjectId_=None):
        if self.user is None:
            data = {'subjectId': subjectId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'subjectId': subjectId_}
        response = self.request.post(url=self.url+'/api/service-point/subject-list', data=data, hosts=self.url)
        apiTestResult(api='/api/service-point/subject-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _config_common_get_all_enum_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/config/common/get-all-enum-list', data=data, hosts=self.url)
        apiTestResult(api='/config/common/get-all-enum-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _config_common_pic_upload(self, file_=None, type_=None):
        if self.user is None:
            data = {'file': file_, 'type': type_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'file': file_, 'type': type_}
        response = self.request.post(url=self.url+'/config/common/pic-upload', data=data, hosts=self.url)
        apiTestResult(api='/config/common/pic-upload', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _location_statistics_all_list(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/location/statistics/all-list', data=data, hosts=self.url)
        apiTestResult(api='/location/statistics/all-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _location_statistics_count(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/location/statistics/count', data=data, hosts=self.url)
        apiTestResult(api='/location/statistics/count', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattle_farm_add(self, pics_=None, farmName_=None, ownerName_=None, sellTo_=None, farmScale_=None, actualOwnCount_=None, cattleSource_=None, contactName_=None, contactPhone_=None, breedType_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, categoryAddInputs_=None, extendAddInput_=None):
        if self.user is None:
            data = {'pics': pics_, 'farmName': farmName_, 'ownerName': ownerName_, 'sellTo': sellTo_, 'farmScale': farmScale_, 'actualOwnCount': actualOwnCount_, 'cattleSource': cattleSource_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'breedType': breedType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'categoryAddInputs': categoryAddInputs_, 'extendAddInput': extendAddInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'farmName': farmName_, 'ownerName': ownerName_, 'sellTo': sellTo_, 'farmScale': farmScale_, 'actualOwnCount': actualOwnCount_, 'cattleSource': cattleSource_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'breedType': breedType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'categoryAddInputs': categoryAddInputs_, 'extendAddInput': extendAddInput_}
        response = self.request.post(url=self.url+'/mobile/cattle-farm/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattle-farm/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattle_farm_detail(self, cattleFarmId_=None):
        if self.user is None:
            data = {'cattleFarmId': cattleFarmId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'cattleFarmId': cattleFarmId_}
        response = self.request.post(url=self.url+'/mobile/cattle-farm/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattle-farm/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattle_farm_edit(self, id_=None, farmName_=None, ownerName_=None, sellTo_=None, farmScale_=None, actualOwnCount_=None, cattleSource_=None, contactName_=None, contactPhone_=None, breedType_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, categoryAddInputs_=None):
        if self.user is None:
            data = {'id': id_, 'farmName': farmName_, 'ownerName': ownerName_, 'sellTo': sellTo_, 'farmScale': farmScale_, 'actualOwnCount': actualOwnCount_, 'cattleSource': cattleSource_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'breedType': breedType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'categoryAddInputs': categoryAddInputs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'farmName': farmName_, 'ownerName': ownerName_, 'sellTo': sellTo_, 'farmScale': farmScale_, 'actualOwnCount': actualOwnCount_, 'cattleSource': cattleSource_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'breedType': breedType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'categoryAddInputs': categoryAddInputs_}
        response = self.request.post(url=self.url+'/mobile/cattle-farm/edit', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattle-farm/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattle_farm_edit_extend(self, pics_=None, id_=None, cattleFarmId_=None, slaughterSellStatus_=None, growRoughageStatus_=None, roughagePurchaseWay_=None, grazeStatus_=None, feedProcessStatus_=None, silageCellarStatus_=None, liveCattleIndexStatus_=None, addFencePlanStatus_=None, organicFertilizerStatus_=None, autoFeedStatus_=None, dealFaecesType_=None, nearbyBreedState_=None, cowshedType_=None):
        if self.user is None:
            data = {'pics': pics_, 'id': id_, 'cattleFarmId': cattleFarmId_, 'slaughterSellStatus': slaughterSellStatus_, 'growRoughageStatus': growRoughageStatus_, 'roughagePurchaseWay': roughagePurchaseWay_, 'grazeStatus': grazeStatus_, 'feedProcessStatus': feedProcessStatus_, 'silageCellarStatus': silageCellarStatus_, 'liveCattleIndexStatus': liveCattleIndexStatus_, 'addFencePlanStatus': addFencePlanStatus_, 'organicFertilizerStatus': organicFertilizerStatus_, 'autoFeedStatus': autoFeedStatus_, 'dealFaecesType': dealFaecesType_, 'nearbyBreedState': nearbyBreedState_, 'cowshedType': cowshedType_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'id': id_, 'cattleFarmId': cattleFarmId_, 'slaughterSellStatus': slaughterSellStatus_, 'growRoughageStatus': growRoughageStatus_, 'roughagePurchaseWay': roughagePurchaseWay_, 'grazeStatus': grazeStatus_, 'feedProcessStatus': feedProcessStatus_, 'silageCellarStatus': silageCellarStatus_, 'liveCattleIndexStatus': liveCattleIndexStatus_, 'addFencePlanStatus': addFencePlanStatus_, 'organicFertilizerStatus': organicFertilizerStatus_, 'autoFeedStatus': autoFeedStatus_, 'dealFaecesType': dealFaecesType_, 'nearbyBreedState': nearbyBreedState_, 'cowshedType': cowshedType_}
        response = self.request.post(url=self.url+'/mobile/cattle-farm/edit-extend', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattle-farm/edit-extend', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattle_farm_list(self, pn_=None, ps_=None, farmName_=None, province_=None, city_=None, county_=None, lng_=None, lat_=None, startTime_=None, endTime_=None, searchKey_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'farmName': farmName_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'startTime': startTime_, 'endTime': endTime_, 'searchKey': searchKey_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'farmName': farmName_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'startTime': startTime_, 'endTime': endTime_, 'searchKey': searchKey_}
        response = self.request.post(url=self.url+'/mobile/cattle-farm/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattle-farm/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_cattle_farm_map_list(self, farmName_=None, province_=None, city_=None, county_=None, lng_=None, lat_=None, startTime_=None, endTime_=None):
        if self.user is None:
            data = {'farmName': farmName_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'startTime': startTime_, 'endTime': endTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'farmName': farmName_, 'province': province_, 'city': city_, 'county': county_, 'lng': lng_, 'lat': lat_, 'startTime': startTime_, 'endTime': endTime_}
        response = self.request.post(url=self.url+'/mobile/cattle-farm/map-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/cattle-farm/map-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_farm_retail_add(self, contactName_=None, contactPhone_=None, farmScale_=None, inventory_=None, farmType_=None, breedWay_=None, categoryType_=None, openSaleTime_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, remark_=None, extendAddInput_=None, bizAttachAddInputs_=None):
        if self.user is None:
            data = {'contactName': contactName_, 'contactPhone': contactPhone_, 'farmScale': farmScale_, 'inventory': inventory_, 'farmType': farmType_, 'breedWay': breedWay_, 'categoryType': categoryType_, 'openSaleTime': openSaleTime_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'remark': remark_, 'extendAddInput': extendAddInput_, 'bizAttachAddInputs': bizAttachAddInputs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'contactName': contactName_, 'contactPhone': contactPhone_, 'farmScale': farmScale_, 'inventory': inventory_, 'farmType': farmType_, 'breedWay': breedWay_, 'categoryType': categoryType_, 'openSaleTime': openSaleTime_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'remark': remark_, 'extendAddInput': extendAddInput_, 'bizAttachAddInputs': bizAttachAddInputs_}
        response = self.request.post(url=self.url+'/mobile/farm-retail/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/farm-retail/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_farm_retail_detail(self, farmRetailId_=None):
        if self.user is None:
            data = {'farmRetailId': farmRetailId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'farmRetailId': farmRetailId_}
        response = self.request.post(url=self.url+'/mobile/farm-retail/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/farm-retail/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_farm_retail_detail_extend(self, farmRetailId_=None):
        if self.user is None:
            data = {'farmRetailId': farmRetailId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'farmRetailId': farmRetailId_}
        response = self.request.post(url=self.url+'/mobile/farm-retail/detail-extend', data=data, hosts=self.url)
        apiTestResult(api='/mobile/farm-retail/detail-extend', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_farm_retail_edit(self, id_=None, contactName_=None, contactPhone_=None, farmScale_=None, inventory_=None, farmType_=None, breedWay_=None, categoryType_=None, openSaleTime_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, remark_=None, extendEditInput_=None, bizAttachAddInputs_=None):
        if self.user is None:
            data = {'id': id_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'farmScale': farmScale_, 'inventory': inventory_, 'farmType': farmType_, 'breedWay': breedWay_, 'categoryType': categoryType_, 'openSaleTime': openSaleTime_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'remark': remark_, 'extendEditInput': extendEditInput_, 'bizAttachAddInputs': bizAttachAddInputs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'farmScale': farmScale_, 'inventory': inventory_, 'farmType': farmType_, 'breedWay': breedWay_, 'categoryType': categoryType_, 'openSaleTime': openSaleTime_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'remark': remark_, 'extendEditInput': extendEditInput_, 'bizAttachAddInputs': bizAttachAddInputs_}
        response = self.request.post(url=self.url+'/mobile/farm-retail/edit', data=data, hosts=self.url)
        apiTestResult(api='/mobile/farm-retail/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_farm_retail_list(self, pn_=None, ps_=None, province_=None, city_=None, county_=None, startTime_=None, endTime_=None, categoryType_=None, searchKey_=None, creatorKey_=None, lat_=None, lng_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'categoryType': categoryType_, 'searchKey': searchKey_, 'creatorKey': creatorKey_, 'lat': lat_, 'lng': lng_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'categoryType': categoryType_, 'searchKey': searchKey_, 'creatorKey': creatorKey_, 'lat': lat_, 'lng': lng_}
        response = self.request.post(url=self.url+'/mobile/farm-retail/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/farm-retail/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_farm_retail_map_list(self, pn_=None, ps_=None, province_=None, city_=None, county_=None, startTime_=None, endTime_=None, categoryType_=None, searchKey_=None, creatorKey_=None, lat_=None, lng_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'categoryType': categoryType_, 'searchKey': searchKey_, 'creatorKey': creatorKey_, 'lat': lat_, 'lng': lng_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'categoryType': categoryType_, 'searchKey': searchKey_, 'creatorKey': creatorKey_, 'lat': lat_, 'lng': lng_}
        response = self.request.post(url=self.url+'/mobile/farm-retail/map-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/farm-retail/map-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_farm_retail_queryList(self, pn_=None, ps_=None, province_=None, city_=None, county_=None, startTime_=None, endTime_=None, categoryType_=None, searchKey_=None, creatorKey_=None, lat_=None, lng_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'categoryType': categoryType_, 'searchKey': searchKey_, 'creatorKey': creatorKey_, 'lat': lat_, 'lng': lng_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'categoryType': categoryType_, 'searchKey': searchKey_, 'creatorKey': creatorKey_, 'lat': lat_, 'lng': lng_}
        response = self.request.post(url=self.url+'/mobile/farm-retail/queryList', data=data, hosts=self.url)
        apiTestResult(api='/mobile/farm-retail/queryList', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_add(self, landArea_=None, landType_=None, landUse_=None, plantType_=None, plantOtherName_=None, raiseCrops_=None, raiseCropsOther_=None, plantWay_=None, vehicleLength_=None, lng_=None, lat_=None, province_=None, city_=None, county_=None, address_=None, villageName_=None, contactName_=None, contactPhone_=None, remark_=None, landLocationAddInput_=None, landTradeAddInput_=None, bizAttachAddInputs_=None):
        if self.user is None:
            data = {'landArea': landArea_, 'landType': landType_, 'landUse': landUse_, 'plantType': plantType_, 'plantOtherName': plantOtherName_, 'raiseCrops': raiseCrops_, 'raiseCropsOther': raiseCropsOther_, 'plantWay': plantWay_, 'vehicleLength': vehicleLength_, 'lng': lng_, 'lat': lat_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'villageName': villageName_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'remark': remark_, 'landLocationAddInput': landLocationAddInput_, 'landTradeAddInput': landTradeAddInput_, 'bizAttachAddInputs': bizAttachAddInputs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'landArea': landArea_, 'landType': landType_, 'landUse': landUse_, 'plantType': plantType_, 'plantOtherName': plantOtherName_, 'raiseCrops': raiseCrops_, 'raiseCropsOther': raiseCropsOther_, 'plantWay': plantWay_, 'vehicleLength': vehicleLength_, 'lng': lng_, 'lat': lat_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'villageName': villageName_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'remark': remark_, 'landLocationAddInput': landLocationAddInput_, 'landTradeAddInput': landTradeAddInput_, 'bizAttachAddInputs': bizAttachAddInputs_}
        response = self.request.post(url=self.url+'/mobile/land/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_all_list(self, pn_=None, ps_=None, startTime_=None, endTime_=None, province_=None, city_=None, county_=None, searchKey_=None, circulationStartTime_=None, circulationEndTime_=None, landAreaBegin_=None, landAreaEnd_=None, plantType_=None, vehicleLength_=None, creatorKey_=None, landUse_=None, status_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'startTime': startTime_, 'endTime': endTime_, 'province': province_, 'city': city_, 'county': county_, 'searchKey': searchKey_, 'circulationStartTime': circulationStartTime_, 'circulationEndTime': circulationEndTime_, 'landAreaBegin': landAreaBegin_, 'landAreaEnd': landAreaEnd_, 'plantType': plantType_, 'vehicleLength': vehicleLength_, 'creatorKey': creatorKey_, 'landUse': landUse_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'startTime': startTime_, 'endTime': endTime_, 'province': province_, 'city': city_, 'county': county_, 'searchKey': searchKey_, 'circulationStartTime': circulationStartTime_, 'circulationEndTime': circulationEndTime_, 'landAreaBegin': landAreaBegin_, 'landAreaEnd': landAreaEnd_, 'plantType': plantType_, 'vehicleLength': vehicleLength_, 'creatorKey': creatorKey_, 'landUse': landUse_, 'status': status_}
        response = self.request.post(url=self.url+'/mobile/land/all-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/all-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_confirm(self, id_=None, landArea_=None, circulationStartTime_=None, circulationEndTime_=None, remark_=None, landLocationAddInput_=None, landTradeAddInput_=None):
        if self.user is None:
            data = {'id': id_, 'landArea': landArea_, 'circulationStartTime': circulationStartTime_, 'circulationEndTime': circulationEndTime_, 'remark': remark_, 'landLocationAddInput': landLocationAddInput_, 'landTradeAddInput': landTradeAddInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'landArea': landArea_, 'circulationStartTime': circulationStartTime_, 'circulationEndTime': circulationEndTime_, 'remark': remark_, 'landLocationAddInput': landLocationAddInput_, 'landTradeAddInput': landTradeAddInput_}
        response = self.request.post(url=self.url+'/mobile/land/confirm', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/confirm', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_detail(self, landId_=None):
        if self.user is None:
            data = {'landId': landId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'landId': landId_}
        response = self.request.post(url=self.url+'/mobile/land/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_edit(self, id_=None, landArea_=None, circulationStartTime_=None, circulationEndTime_=None, landLocationAddInput_=None, landTradeAddInput_=None):
        if self.user is None:
            data = {'id': id_, 'landArea': landArea_, 'circulationStartTime': circulationStartTime_, 'circulationEndTime': circulationEndTime_, 'landLocationAddInput': landLocationAddInput_, 'landTradeAddInput': landTradeAddInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'landArea': landArea_, 'circulationStartTime': circulationStartTime_, 'circulationEndTime': circulationEndTime_, 'landLocationAddInput': landLocationAddInput_, 'landTradeAddInput': landTradeAddInput_}
        response = self.request.post(url=self.url+'/mobile/land/edit', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_editNotCirculation(self, id_=None, landArea_=None, lng_=None, lat_=None, province_=None, city_=None, county_=None, address_=None, landType_=None, plantType_=None, plantOtherName_=None, vehicleLength_=None, villageName_=None, contactName_=None, contactPhone_=None, remark_=None, bizAttachAddInputs_=None, landUse_=None, raiseCrops_=None, raiseCropsOther_=None, plantWay_=None, landLocationAddInput_=None, landTradeAddInput_=None):
        if self.user is None:
            data = {'id': id_, 'landArea': landArea_, 'lng': lng_, 'lat': lat_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'landType': landType_, 'plantType': plantType_, 'plantOtherName': plantOtherName_, 'vehicleLength': vehicleLength_, 'villageName': villageName_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'remark': remark_, 'bizAttachAddInputs': bizAttachAddInputs_, 'landUse': landUse_, 'raiseCrops': raiseCrops_, 'raiseCropsOther': raiseCropsOther_, 'plantWay': plantWay_, 'landLocationAddInput': landLocationAddInput_, 'landTradeAddInput': landTradeAddInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'landArea': landArea_, 'lng': lng_, 'lat': lat_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'landType': landType_, 'plantType': plantType_, 'plantOtherName': plantOtherName_, 'vehicleLength': vehicleLength_, 'villageName': villageName_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'remark': remark_, 'bizAttachAddInputs': bizAttachAddInputs_, 'landUse': landUse_, 'raiseCrops': raiseCrops_, 'raiseCropsOther': raiseCropsOther_, 'plantWay': plantWay_, 'landLocationAddInput': landLocationAddInput_, 'landTradeAddInput': landTradeAddInput_}
        response = self.request.post(url=self.url+'/mobile/land/editNotCirculation', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/editNotCirculation', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_page_list(self, pn_=None, ps_=None, startTime_=None, endTime_=None, province_=None, city_=None, county_=None, searchKey_=None, circulationStartTime_=None, circulationEndTime_=None, landAreaBegin_=None, landAreaEnd_=None, plantType_=None, vehicleLength_=None, creatorKey_=None, landUse_=None, status_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'startTime': startTime_, 'endTime': endTime_, 'province': province_, 'city': city_, 'county': county_, 'searchKey': searchKey_, 'circulationStartTime': circulationStartTime_, 'circulationEndTime': circulationEndTime_, 'landAreaBegin': landAreaBegin_, 'landAreaEnd': landAreaEnd_, 'plantType': plantType_, 'vehicleLength': vehicleLength_, 'creatorKey': creatorKey_, 'landUse': landUse_, 'status': status_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'startTime': startTime_, 'endTime': endTime_, 'province': province_, 'city': city_, 'county': county_, 'searchKey': searchKey_, 'circulationStartTime': circulationStartTime_, 'circulationEndTime': circulationEndTime_, 'landAreaBegin': landAreaBegin_, 'landAreaEnd': landAreaEnd_, 'plantType': plantType_, 'vehicleLength': vehicleLength_, 'creatorKey': creatorKey_, 'landUse': landUse_, 'status': status_}
        response = self.request.post(url=self.url+'/mobile/land/page-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_land_stopCirculation(self, landId_=None):
        if self.user is None:
            data = {'landId': landId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'landId': landId_}
        response = self.request.post(url=self.url+'/mobile/land/stopCirculation', data=data, hosts=self.url)
        apiTestResult(api='/mobile/land/stopCirculation', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_landLocation_detail(self, landId_=None):
        if self.user is None:
            data = {'landId': landId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'landId': landId_}
        response = self.request.post(url=self.url+'/mobile/landLocation/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/landLocation/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_landLocation_edit(self, input_=None, landId_=None):
        if self.user is None:
            data = {'input': input_, 'landId': landId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_, 'landId': landId_}
        response = self.request.post(url=self.url+'/mobile/landLocation/edit', data=data, hosts=self.url)
        apiTestResult(api='/mobile/landLocation/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_landLocation_editNoCirculation(self, input_=None, landId_=None):
        if self.user is None:
            data = {'input': input_, 'landId': landId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'input': input_, 'landId': landId_}
        response = self.request.post(url=self.url+'/mobile/landLocation/editNoCirculation', data=data, hosts=self.url)
        apiTestResult(api='/mobile/landLocation/editNoCirculation', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_service_point_list(self, pn_=None, ps_=None, province_=None, city_=None, county_=None, startTime_=None, endTime_=None, pointType_=None, lat_=None, lng_=None, pointName_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'pointType': pointType_, 'lat': lat_, 'lng': lng_, 'pointName': pointName_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'pointType': pointType_, 'lat': lat_, 'lng': lng_, 'pointName': pointName_}
        response = self.request.post(url=self.url+'/mobile/service-point/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/service-point/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_slaughter_company_add(self, pics_=None, companyName_=None, slaughterScale_=None, actualSlaughterCount_=None, cattleSource_=None, quarantineCondition_=None, purchaseStandard_=None, settleMethod_=None, priceType_=None, contactName_=None, contactPhone_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, extendAddInput_=None):
        if self.user is None:
            data = {'pics': pics_, 'companyName': companyName_, 'slaughterScale': slaughterScale_, 'actualSlaughterCount': actualSlaughterCount_, 'cattleSource': cattleSource_, 'quarantineCondition': quarantineCondition_, 'purchaseStandard': purchaseStandard_, 'settleMethod': settleMethod_, 'priceType': priceType_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'extendAddInput': extendAddInput_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'companyName': companyName_, 'slaughterScale': slaughterScale_, 'actualSlaughterCount': actualSlaughterCount_, 'cattleSource': cattleSource_, 'quarantineCondition': quarantineCondition_, 'purchaseStandard': purchaseStandard_, 'settleMethod': settleMethod_, 'priceType': priceType_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'extendAddInput': extendAddInput_}
        response = self.request.post(url=self.url+'/mobile/slaughter-company/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/slaughter-company/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_slaughter_company_detail(self, companyId_=None):
        if self.user is None:
            data = {'companyId': companyId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'companyId': companyId_}
        response = self.request.post(url=self.url+'/mobile/slaughter-company/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/slaughter-company/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_slaughter_company_edit(self, id_=None, companyName_=None, slaughterScale_=None, actualSlaughterCount_=None, cattleSource_=None, quarantineCondition_=None, purchaseStandard_=None, settleMethod_=None, priceType_=None, contactName_=None, contactPhone_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None):
        if self.user is None:
            data = {'id': id_, 'companyName': companyName_, 'slaughterScale': slaughterScale_, 'actualSlaughterCount': actualSlaughterCount_, 'cattleSource': cattleSource_, 'quarantineCondition': quarantineCondition_, 'purchaseStandard': purchaseStandard_, 'settleMethod': settleMethod_, 'priceType': priceType_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'companyName': companyName_, 'slaughterScale': slaughterScale_, 'actualSlaughterCount': actualSlaughterCount_, 'cattleSource': cattleSource_, 'quarantineCondition': quarantineCondition_, 'purchaseStandard': purchaseStandard_, 'settleMethod': settleMethod_, 'priceType': priceType_, 'contactName': contactName_, 'contactPhone': contactPhone_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_}
        response = self.request.post(url=self.url+'/mobile/slaughter-company/edit', data=data, hosts=self.url)
        apiTestResult(api='/mobile/slaughter-company/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_slaughter_company_edit_extend(self, pics_=None, id_=None, companyId_=None, acidDischargeStatus_=None, halalAuthStatus_=None, countryStoreStatus_=None, insteadSlaughterProcessFeeStatus_=None, saleProducts_=None, saleChannel_=None, bodyDealCondition_=None, dealFaecesType_=None, productionFactory_=None):
        if self.user is None:
            data = {'pics': pics_, 'id': id_, 'companyId': companyId_, 'acidDischargeStatus': acidDischargeStatus_, 'halalAuthStatus': halalAuthStatus_, 'countryStoreStatus': countryStoreStatus_, 'insteadSlaughterProcessFeeStatus': insteadSlaughterProcessFeeStatus_, 'saleProducts': saleProducts_, 'saleChannel': saleChannel_, 'bodyDealCondition': bodyDealCondition_, 'dealFaecesType': dealFaecesType_, 'productionFactory': productionFactory_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pics': pics_, 'id': id_, 'companyId': companyId_, 'acidDischargeStatus': acidDischargeStatus_, 'halalAuthStatus': halalAuthStatus_, 'countryStoreStatus': countryStoreStatus_, 'insteadSlaughterProcessFeeStatus': insteadSlaughterProcessFeeStatus_, 'saleProducts': saleProducts_, 'saleChannel': saleChannel_, 'bodyDealCondition': bodyDealCondition_, 'dealFaecesType': dealFaecesType_, 'productionFactory': productionFactory_}
        response = self.request.post(url=self.url+'/mobile/slaughter-company/edit-extend', data=data, hosts=self.url)
        apiTestResult(api='/mobile/slaughter-company/edit-extend', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_slaughter_company_list(self, pn_=None, ps_=None, companyName_=None, province_=None, city_=None, county_=None, startTime_=None, endTime_=None, searchKey_=None, lat_=None, lng_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'companyName': companyName_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'searchKey': searchKey_, 'lat': lat_, 'lng': lng_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'companyName': companyName_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, 'searchKey': searchKey_, 'lat': lat_, 'lng': lng_}
        response = self.request.post(url=self.url+'/mobile/slaughter-company/list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/slaughter-company/list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_slaughter_company_map_list(self, companyName_=None, province_=None, city_=None, county_=None, startTime_=None, endTime_=None):
        if self.user is None:
            data = {'companyName': companyName_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'companyName': companyName_, 'province': province_, 'city': city_, 'county': county_, 'startTime': startTime_, 'endTime': endTime_}
        response = self.request.post(url=self.url+'/mobile/slaughter-company/map-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/slaughter-company/map-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_statistics_countByUser(self):
        if self.user is None:
            data = {}
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id}
        response = self.request.post(url=self.url+'/mobile/statistics/countByUser', data=data, hosts=self.url)
        apiTestResult(api='/mobile/statistics/countByUser', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_trade_contact_farm_retail(self, contactPhone_=None):
        if self.user is None:
            data = {'contactPhone': contactPhone_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'contactPhone': contactPhone_}
        response = self.request.post(url=self.url+'/mobile/trade/contact/farm-retail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/trade/contact/farm-retail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_trade_contact_farm_retail_or_slaughter_company(self, contactPhone_=None):
        if self.user is None:
            data = {'contactPhone': contactPhone_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'contactPhone': contactPhone_}
        response = self.request.post(url=self.url+'/mobile/trade/contact/farm-retail-or-slaughter-company', data=data, hosts=self.url)
        apiTestResult(api='/mobile/trade/contact/farm-retail-or-slaughter-company', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_tradeCenter_add(self, name_=None, tradeTime_=None, historyTurnover_=None, brokerCount_=None, cattleSource_=None, cattleSourceType_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, contactPhone_=None, brokerName_=None, brokerContactPhone_=None, farmerName_=None, famerContactPhone_=None, tradeCenterFeeAddInput_=None, tradeCenterExtendAddInput_=None, tradeCategoryAddInputs_=None, bizAttachAddInputs_=None):
        if self.user is None:
            data = {'name': name_, 'tradeTime': tradeTime_, 'historyTurnover': historyTurnover_, 'brokerCount': brokerCount_, 'cattleSource': cattleSource_, 'cattleSourceType': cattleSourceType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'contactPhone': contactPhone_, 'brokerName': brokerName_, 'brokerContactPhone': brokerContactPhone_, 'farmerName': farmerName_, 'famerContactPhone': famerContactPhone_, 'tradeCenterFeeAddInput': tradeCenterFeeAddInput_, 'tradeCenterExtendAddInput': tradeCenterExtendAddInput_, 'tradeCategoryAddInputs': tradeCategoryAddInputs_, 'bizAttachAddInputs': bizAttachAddInputs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'name': name_, 'tradeTime': tradeTime_, 'historyTurnover': historyTurnover_, 'brokerCount': brokerCount_, 'cattleSource': cattleSource_, 'cattleSourceType': cattleSourceType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'contactPhone': contactPhone_, 'brokerName': brokerName_, 'brokerContactPhone': brokerContactPhone_, 'farmerName': farmerName_, 'famerContactPhone': famerContactPhone_, 'tradeCenterFeeAddInput': tradeCenterFeeAddInput_, 'tradeCenterExtendAddInput': tradeCenterExtendAddInput_, 'tradeCategoryAddInputs': tradeCategoryAddInputs_, 'bizAttachAddInputs': bizAttachAddInputs_}
        response = self.request.post(url=self.url+'/mobile/tradeCenter/add', data=data, hosts=self.url)
        apiTestResult(api='/mobile/tradeCenter/add', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_tradeCenter_all_list(self, pn_=None, ps_=None, startTime_=None, endTime_=None, province_=None, city_=None, county_=None, name_=None, contactPhone_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'startTime': startTime_, 'endTime': endTime_, 'province': province_, 'city': city_, 'county': county_, 'name': name_, 'contactPhone': contactPhone_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'startTime': startTime_, 'endTime': endTime_, 'province': province_, 'city': city_, 'county': county_, 'name': name_, 'contactPhone': contactPhone_}
        response = self.request.post(url=self.url+'/mobile/tradeCenter/all-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/tradeCenter/all-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_tradeCenter_detail(self, tradeCenterId_=None):
        if self.user is None:
            data = {'tradeCenterId': tradeCenterId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'tradeCenterId': tradeCenterId_}
        response = self.request.post(url=self.url+'/mobile/tradeCenter/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/tradeCenter/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_tradeCenter_edit(self, id_=None, name_=None, tradeTime_=None, historyTurnover_=None, brokerCount_=None, cattleSource_=None, cattleSourceType_=None, province_=None, city_=None, county_=None, address_=None, lng_=None, lat_=None, contactPhone_=None, brokerName_=None, brokerContactPhone_=None, farmerName_=None, famerContactPhone_=None, tradeCategoryEditInputs_=None):
        if self.user is None:
            data = {'id': id_, 'name': name_, 'tradeTime': tradeTime_, 'historyTurnover': historyTurnover_, 'brokerCount': brokerCount_, 'cattleSource': cattleSource_, 'cattleSourceType': cattleSourceType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'contactPhone': contactPhone_, 'brokerName': brokerName_, 'brokerContactPhone': brokerContactPhone_, 'farmerName': farmerName_, 'famerContactPhone': famerContactPhone_, 'tradeCategoryEditInputs': tradeCategoryEditInputs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'id': id_, 'name': name_, 'tradeTime': tradeTime_, 'historyTurnover': historyTurnover_, 'brokerCount': brokerCount_, 'cattleSource': cattleSource_, 'cattleSourceType': cattleSourceType_, 'province': province_, 'city': city_, 'county': county_, 'address': address_, 'lng': lng_, 'lat': lat_, 'contactPhone': contactPhone_, 'brokerName': brokerName_, 'brokerContactPhone': brokerContactPhone_, 'farmerName': farmerName_, 'famerContactPhone': famerContactPhone_, 'tradeCategoryEditInputs': tradeCategoryEditInputs_}
        response = self.request.post(url=self.url+'/mobile/tradeCenter/edit', data=data, hosts=self.url)
        apiTestResult(api='/mobile/tradeCenter/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_tradeCenter_page_list(self, pn_=None, ps_=None, startTime_=None, endTime_=None, province_=None, city_=None, county_=None, name_=None, contactPhone_=None):
        if self.user is None:
            data = {'pn': pn_, 'ps': ps_, 'startTime': startTime_, 'endTime': endTime_, 'province': province_, 'city': city_, 'county': county_, 'name': name_, 'contactPhone': contactPhone_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'pn': pn_, 'ps': ps_, 'startTime': startTime_, 'endTime': endTime_, 'province': province_, 'city': city_, 'county': county_, 'name': name_, 'contactPhone': contactPhone_}
        response = self.request.post(url=self.url+'/mobile/tradeCenter/page-list', data=data, hosts=self.url)
        apiTestResult(api='/mobile/tradeCenter/page-list', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_tradeCenterFee_detail(self, tradeCenterId_=None):
        if self.user is None:
            data = {'tradeCenterId': tradeCenterId_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'tradeCenterId': tradeCenterId_}
        response = self.request.post(url=self.url+'/mobile/tradeCenterFee/detail', data=data, hosts=self.url)
        apiTestResult(api='/mobile/tradeCenterFee/detail', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))

    def _mobile_tradeCenterFee_edit(self, tradeCenterId_=None, setleType_=None, settleTime_=None, depositPayType_=None, entryFee_=None, exitFee_=None, quarantineFee_=None, fenceFee_=None, siteFee_=None, dealPrice_=None, tradeCenterExtendAddInput_=None, bizAttachAddInputs_=None):
        if self.user is None:
            data = {'tradeCenterId': tradeCenterId_, 'setleType': setleType_, 'settleTime': settleTime_, 'depositPayType': depositPayType_, 'entryFee': entryFee_, 'exitFee': exitFee_, 'quarantineFee': quarantineFee_, 'fenceFee': fenceFee_, 'siteFee': siteFee_, 'dealPrice': dealPrice_, 'tradeCenterExtendAddInput': tradeCenterExtendAddInput_, 'bizAttachAddInputs': bizAttachAddInputs_, }
        else:
            data = {'_tk_': self.user.token, '_deviceId_': self.user.device_id, 'tradeCenterId': tradeCenterId_, 'setleType': setleType_, 'settleTime': settleTime_, 'depositPayType': depositPayType_, 'entryFee': entryFee_, 'exitFee': exitFee_, 'quarantineFee': quarantineFee_, 'fenceFee': fenceFee_, 'siteFee': siteFee_, 'dealPrice': dealPrice_, 'tradeCenterExtendAddInput': tradeCenterExtendAddInput_, 'bizAttachAddInputs': bizAttachAddInputs_}
        response = self.request.post(url=self.url+'/mobile/tradeCenterFee/edit', data=data, hosts=self.url)
        apiTestResult(api='/mobile/tradeCenterFee/edit', host=self.url,datas=data, resp=response)
        return self.__judge_response_status(json.loads(response))
