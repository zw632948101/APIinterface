from interfaces.beefcattle.BreedAction import breedAction
from interfaces.beefcattle.PlantAction import plantAction
from interfaces.beefcattle.TradeAction import tradeAction
from interfaces.beefcattle.WagyAction import wagyAction
import json
import random

from interfaces.middleground.Wms_apiAction import wms_apiAction
from testcase.middleground.sql.mpWmsSql import OutStorehouseSql
from ddt import data, ddt
from utils import runlevel, conversion
from faker import Faker
import unittest



class OutStorehouse(unittest.TestCase):
    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        """
        测试前数据准备
        :return:
        """
        self.api = breedAction()
        self.api.set_user(mobile=15198034727)
        # self.db = mp_label()
        self.faker = Faker('zh_CN')

    def tearDown(self) -> None:
        pass

    # 新增牛栏
    # def test_admin_cattleFence_add(self):
    #     resp = self.api._admin_cattleFence_add(fenceNo_="01-01",
    #                                     fenceName_="测试牛栏1",
    #                                     cowshedId_=None,
    #                                     cattleFarmId_=1,
    #                                     type_=1002,
    #                                     area_=None,
    #                                     epcNo_=None,
    #                                     remark_=None)
    #     if resp.get('status') == 'OK':
    #         pass


    def test_admin_cattle_add(self):
        resp = self.api._admin_cattle_add(
                                            cattleEarTagNo_=39, #牛耳标号
                                            cattleFenceId_=1, #牛栏ID
                                            variety_="黄牛",
                                            gender_=1002, #性别
                                            birthday_=1579453179000, #出生日期
                                            entryDate_= 1611075579000,# 入场日期
                                            currentChildTime_=2, #当前胎次
                                            birthWeight_=100,
                                            feedType_="繁育",
                                            fatherNo_="F001",
                                            motherNo_="M001",
                                            rfidCode_="RF52515",
                                            nucleusGroupStatus_=1,
                                            insureNo_="青牛",
                                            purchaseOrderNo_=None,
                                            skuCode_="T160802", # sku码
                                            usedNo_="HD0100124", #曾用牛号
                                            pics_=None #牛只照片(json数组格式入参最多三张(1.牛头，2.牛左，3.牛右),[{"bizType":1,"url":"123"}])
                                   )
        print("新增牛只: %s"%resp.get('status'))

    # def test_admin_cattleFence_list(self):
    #     resp = self.api._admin_cattleFence_list(pn_=None, ps_=None, cattleFarmId_=1, fenceName_=None, fenceNo_=None, cowshedId_=None, cattleExistFilter_=None)
    #     print(resp.get('content'))

    # def test_admin_cattleFamilyTree_list(self):
    #     resp = self.api._admin_cattleFamilyTree_list(pn_=None, ps_=None, cattleEarTagNo_=None, gender_=None)
    #     print(resp.get('content'))


if __name__ == '__main__':
    unittest.main()