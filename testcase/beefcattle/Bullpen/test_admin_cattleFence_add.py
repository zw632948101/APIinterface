from interfaces.beefcattle.BreedAction import breedAction
from testcase.beefcattle.Bullpen.case_list.Bullpen_case import bullpen_case,Random
from testcase.beefcattle.sql.Bullpen_sql import Bullpen
from ddt import data, ddt
from utils import runlevel, conversion
from faker import Faker
import unittest
import json


@ddt
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
        self.faker = Faker('zh_CN')

    def tearDown(self) -> None:
        pass

    @data(*bullpen_case().admin_cattle_add)
    def test_admin_cattle_add(self,case):
        resp = self.api._admin_cattle_add(
                                            cattleEarTagNo_=case['data']['cattleEarTagNo_'],
                                            cattleFenceId_=case['data']['cattleFenceId_'],
                                            variety_=case['data']['variety_'],
                                            gender_=case['data']['gender_'],
                                            birthday_=case['data']['birthday_'],
                                            entryDate_=case['data']['entryDate_'],
                                            currentChildTime_=case['data']['currentChildTime_'],
                                            birthWeight_=case['data']['birthWeight_'],
                                            feedType_=case['data']['feedType_'],
                                            fatherNo_=case['data']['fatherNo_'],
                                            motherNo_=case['data']['motherNo_'],
                                            rfidCode_=case['data']['rfidCode_'],
                                            nucleusGroupStatus_=case['data']['nucleusGroupStatus_'],
                                            insureNo_=case['data']['insureNo_'],
                                            purchaseOrderNo_=case['data']['purchaseOrderNo_'],
                                            skuCode_=case['data']['skuCode_'],
                                            usedNo_=case['data']['usedNo_'],
                                            pics_=case['data']['pics_']
                                   )
        try:
            self.assertEqual(case['expect'],resp.get('status'))
        except Exception as e:
            print("断言失败原因: {}".format(e))
            raise "请求参数:{}".format(case['data'])

        if resp.get('status') == "OK":
            # 确保值写入库中
            expect = case['data']['cattleEarTagNo_']
            actual = Bullpen().get_cattle()[0]['cattle_ear_tag_no']
            self.assertEqual(expect,actual)
        else:
            pass


    def test_admin_cattle_detail(self):
        resp = self.api._admin_cattle_detail(cattleId_=Bullpen().get_cattle()[0]['id'])
        self.assertEqual('OK',resp.get('status'))
        print(resp.get('content'))


    @data(*bullpen_case().admin_cattle_batch_add)
    def test_admin_cattle_batch_add(self,case):
        resp = self.api._admin_cattle_batch_add(
                                                purchaseOrderNo_=case['data']['purchaseOrderNo_'],
                                                jsonStr_=json.dumps(case['data']['jsonStr_'])
                                                )

        if resp.get("status") == 'OK':
            print(case['title'],"结果: %s"%resp.get('content'))
            self.assertEqual(case['expect'], resp.get("status"))
            # 确保值写入库中
            expect = len(Bullpen().get_cattle()[0]) + 1
            actual = len(Bullpen().get_cattle()[0])
            self.assertEqual(expect, actual)
        elif resp.get('stauts') == 'ERROR':
            print(case['title'], "结果: %s" % resp.get('content'))
            self.assertEqual(case['expect'],resp.get("status"))


    @data(*bullpen_case().admin_cattle_edit)
    def test_admin_cattle_edit(self,case):
        # id数据库中去查
        id_ = Bullpen().get_cattle()[0]['id']
        resp = self.api._admin_cattle_edit(id_=id_,
                                    cattleFenceId_=case['data']['cattleFenceId_'],
                                    variety_=case['data']['variety_'],
                                    gender_=case['data']['gender_'],
                                    birthday_=case['data']['birthday_'],
                                    entryDate_=case['data']['entryDate_'],
                                    currentChildTime_=case['data']['currentChildTime_'],
                                    birthWeight_=case['data']['birthWeight_'],
                                    feedType_=case['data']['feedType_'],
                                    fatherNo_=case['data']['fatherNo_'],
                                    motherNo_=case['data']['motherNo_'],
                                    nucleusGroupStatus_=case['data']['nucleusGroupStatus_'],
                                    insureNo_=case['data']['insureNo_'],
                                    skuCode_=case['data']['skuCode_'],
                                    usedNo_=case['data']['usedNo_'],
                                    pics_=case['data']['pics_'])

        print(resp.get("status"))
        self.assertEqual(case['expect'],resp.get("status"))
        if resp.get("status") == "ERROR":
            case['data']['id_']=Bullpen().get_cattle()[0]['id']
            print("错误case: %s,传入参数: %s"%(case['title'],case['data']))


    @data(*bullpen_case().admin_cattle_list)
    def test_admin_cattle_list(self,case):
        resp = self.api._admin_cattle_list(pn_=case['data']['pn_'],
                                    ps_=case['data']['ps_'],
                                    cattleEarTagNo_=case['data']['cattleEarTagNo_'],
                                    cowshedId_=case['data']['cowshedId_'],
                                    cattleFenceId_=case['data']['cattleFenceId_'],
                                    nucleusGroupStatus_=case['data']['nucleusGroupStatus_'],
                                    gender_=case['data']['gender_'],
                                    inGroupStatus_=case['data']['inGroupStatus_'],
                                    variety_=case['data']['variety_'],
                                    currentChildTime_=case['data']['currentChildTime_'],
                                    startEntryDate_=case['data']['startEntryDate_'],
                                    endEntryDate_=case['data']['endEntryDate_'],
                                    startDepartureDate_=case['data']['startDepartureDate_'],
                                    endDepartureDate_=case['data']['endDepartureDate_'])

        self.assertEqual(case['expect'],resp.get('status'))


    def test_admin_cattle_list_by_cattle_no(self):
        cattleEarTagNos_ = Bullpen().get_cattle_cattle_list_by_cattle_no()
        resp = self.api._admin_cattle_list_by_cattle_no(
                                                        cattleEarTagNos_=cattleEarTagNos_)
        self.assertEqual('OK',resp.get("status"))





if __name__ == '__main__':
    unittest.main()