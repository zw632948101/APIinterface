import unittest
from interfaces.middleground.Wms_apiAction import wms_apiAction
from testcase.middleground.sql.shopMP import mpShopSql
from testcase.middleground.WMS.datas.warehouse_data import warehouse_data
from ddt import data, ddt
from testcase.middleground.WMS.common.Mysql import mp_label
from utils import runlevel
from faker import Faker



@ddt
class warehouseAdd(unittest.TestCase):
    def setUp(self) -> None:
        """
               测试前数据准备
               :return:
               """
        self.api = wms_apiAction()
        self.api.set_user(mobile=15198034727, account_type='web-mp')
        self.db = mpShopSql()
        self.faker = Faker('zh_CN')

    def tearDown(self) -> None:
        pass
    @data(*warehouse_data().warehouse_add)
    def test_admin_warehouse_add(self,case):
        resp = self.api._admin_warehouse_add(name_=case['data']['name_'],
                                             outWarehouseCode_=case['data']['outWarehouseCode_'],
                                             companyCode_=case['data']['companyCode_'],
                                             shopCode_=case['data']['shopCode_'],
                                             warehouseTypeId_=case['data']['warehouseTypeId_'],
                                             contactId_=case['data']['contactId_'],
                                             province_=case['data']['province_'],
                                             city_=case['data']['city_'],
                                             county_=case['data']['county_'],
                                             lng_=case['data']['lng_'],
                                             lat_=case['data']['lat_'],
                                             address_=case['data']['address_'],
                                             status_=case['data']['status_'],
                                             isThird_=case['data']['isThird_'],
                                             isVirtual_=case['data']['isVirtual_'],
                                             isMonitor_ = case['data']['isMonitor_'],
                                             remark_=case['data']['remark_'])

        self.assertEqual(case['expect'],resp.get('status'))
        if resp.get('status') == "OK":
            self.assertEqual(case['data']['name_'],mp_label().git_warehouse_status()[0]['name'])
            self.assertEqual(case['data']['companyCode_'],int(mp_label().git_warehouse_status()[0]['company_code']))
            self.assertEqual(case['data']['contactId_'],mp_label().git_warehouse_status()[0]['contact_id'])
            self.assertEqual(case['data']['status_'],mp_label().git_warehouse_status()[0]['status'])

        elif resp.get('status') == "OK":
            # 新增仓库成功,推送至ERP
            id_ = mp_label().git_warehouse_status()[0]['id']
            resp = self.api._admin_warehouse_push_to_erp(id_=id_)
            self.assertEqual('OK',resp.get('status'))
        else:
            pass
    # 添加附加属性
    @data(*warehouse_data().admin_warehouse_additional_update)
    def test_admin_warehouse_additional_update(self,case):
        # id查库里最新的仓库
        id_ = mp_label().git_warehouse_status()[0]['id']
        resp = self.api._admin_warehouse_additional_update(images_=case['data']['images_'],
                                                           id_=id_,
                                                           area_=case['data']['area_'],
                                                           capacity_=case['data']['capacity_'],
                                                           cargoType_=case['data']['cargoType_'])

        self.assertEqual(case['expect'],resp.get('status'))
        # 添加属性成功，查看属性并断言
        detail = self.api._admin_warehouse_additional_detail(id_=id_)
        if resp.get('status') == 'OK':
            self.assertEqual(case['data']['area_'],detail['content']['area'])
            self.assertEqual(case['data']['capacity_'],detail['content']['capacity'])
            self.assertEqual(case['data']['cargoType_'],detail['content']['cargoType'])
        else:
            pass

    # 仓库ERP同步日志
    def test_admin_warehouse_erp_sync_log_list(self):
        id = mp_label().git_warehouse_status()[0]['id']
        resp = self.api._admin_warehouse_erp_sync_log_list(id_=id)
        self.assertEqual('OK',resp.get('status'))




if __name__ == '__main__':
    unittest.main()