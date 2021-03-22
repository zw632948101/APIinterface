from interfaces.beefcattle.BreedAction import breedAction
from testcase.beefcattle.Bullpen.case_list.Bullpen_case import bullpen_case
from testcase.beefcattle.sql.Bullpen_sql import Bullpen
from ddt import data, ddt
from utils import runlevel, conversion
from faker import Faker
import unittest


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
            actual = int(Bullpen().get_cattle()[0]['cattle_ear_tag_no'])
            self.assertEqual(expect,actual)
        else:
            pass



    # def test_admin_cattleFence_list(self):
    #     resp = self.api._admin_cattleFence_list(pn_=None, ps_=None, cattleFarmId_=1, fenceName_=None, fenceNo_=None, cowshedId_=None, cattleExistFilter_=None)
    #     print(resp.get('content'))

    # def test_admin_cattleFamilyTree_list(self):
    #     resp = self.api._admin_cattleFamilyTree_list(pn_=None, ps_=None, cattleEarTagNo_=None, gender_=None)
    #     print(resp.get('content'))


if __name__ == '__main__':
    unittest.main()