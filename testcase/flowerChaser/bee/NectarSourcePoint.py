import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log import log
from testcase.flowerChaser.sql.NectarSourcePointSql import NectarSourcePointSql
import random
from faker import Faker
from utils.fake.FakeLocation import FakeLocation
import json
from utils.dataConversion.dataConversion import DataConversion as dc
from utils.Timestamp.TimestampTransform import TimestampTransform as tt


class CraneManagement(unittest.TestCase):
    """
    接口文档: http://qa-gateway.worldfarm.com/swagger-ui.html#/
    FC2.5.0接口
    """
    action = BeeAction()
    db = NectarSourcePointSql()
    log.info("开始执行信息采集-蜜源勘察管理模块测试用例")
    action.set_user(19988776655)
    fake = Faker(locale="zh_CN")
    fl = FakeLocation()

    def test_mobile_nectar_source_point_list(self):
        """
        蜜源勘察--列表查询
        :return:
        """
        plantlist = self.db.query_plant_code_all()
        plantCodes = random.choice(plantlist).get('code')
        plantCodes = plantCodes if random.randint(1, 2) == 1 else None
        purpose = random.randint(1, 6) if random.randint(1, 2) == 1 else None
        pn = 1
        ps = 20
        searchType = random.randint(1, 2)
        province, city, county, address, lng, lat = self.fl.fake_location()
        distanceType = random.randint(1, 4)
        if searchType == 1:
            distanceType = None
        else:
            province = city = county = None
        result = self.action._mobile_nectar_source_point_list(plantCodes_=plantCodes, purpose_=purpose, pn_=pn, ps_=ps,
                                                              searchType_=searchType, province_=province, city_=city,
                                                              county_=county, lng_=lng, lat_=lat,
                                                              distanceType_=distanceType)
        self.assertEqual(result['status'], 'OK', msg="断言失败")

    def test_mobile_nectar_source_point_add(self):
        """
        蜜源勘察--新增
        :return:
        """
        province, city, county, address, lng, lat = self.fl.fake_location()
        plantlist = self.db.query_plant_code_all()
        plantCode = random.choice(plantlist).get('code')
        nectarSourceArea = random.randint(100, 99999)
        apiaryDensity = random.randint(10, 99999)
        purpose = random.randint(1, 6)
        pesticideCondition = '接口测试农药情况'

        def nectar_dict(infoType):
            addressinfo = self.fl.fake_location()
            plant = dc.data_assemble('code', plantlist, 3)
            plantstr = ','.join(list(map(str, plant)))
            plantdict = {"province": addressinfo[0], "city": addressinfo[1], "plantCode": plantstr,
                         "infoType": infoType}
            return plantdict

        Abee = [nectar_dict(infoType=1) for i in range(9)]
        Bbee = [nectar_dict(infoType=2) for i in range(9)]
        nectarSourceFlowInputs = json.dumps(Abee + Bbee)
        # nectarSourceFlowInputs =None
        nectarSourcePointAttachInputs = dc.assemble_picture_dictionary(20, remark="接口测试")
        # nectarSourcePointAttachInputs = None
        result = self.action._mobile_nectar_source_point_add(province_=province, city_=city, county_=county,
                                                             plantCode_=plantCode, lng_=lng, lat_=lat,
                                                             floweringStartDate_=tt.get_random_date(),
                                                             floweringEndDate_=tt.get_random_date(),
                                                             nectarFlow_=tt.get_random_date(),
                                                             entryDate_=tt.get_random_date(),
                                                             departureDate_=tt.get_random_date(),
                                                             nectarSourceArea_=nectarSourceArea,
                                                             apiaryDensity_=apiaryDensity, purpose_=purpose,
                                                             pesticideCondition_=pesticideCondition,
                                                             nectarSourceFlowInputs_=nectarSourceFlowInputs,
                                                             nectarSourcePointAttachInputs_=nectarSourcePointAttachInputs)
        log.info("插入数据为-->province:%s ; city:%s ; county:%s ; plantCode:%s" % (province, city, county, plantCode))
        result_sql = self.db.query_add_nectar_point(province, city, county, plantCode)
        log.info("数据库查询新增数据为： %s" % str(result_sql))
        self.assertEqual(result['status'], 'OK', msg="断言失败")
        self.assertEqual(len(result_sql), 1, msg="断言失败--数据库插入数据失败")

    def test_mobile_nectar_source_point_edit(self):
        """
        蜜源勘察--编辑
        :return:
        """
        province, city, county, address, lng, lat = self.fl.fake_location()
        pointall = random.choice(self.db.query_nectar_source_point_all())
        pointid = pointall.get('id')
        plantlist = self.db.query_plant_code_all()
        plantCode = random.choice(plantlist).get('code')
        nectarSourceArea = random.randint(100, 99999)
        apiaryDensity = random.randint(10, 99999)
        purpose = random.randint(1, 6)
        # purpose = 'd'
        pesticideCondition = '接口测试农药情况'

        def nectar_dict(infoType):
            addressinfo = self.fl.fake_location()
            plant = dc.data_assemble('code', plantlist, 3)
            plantstr = ','.join(list(map(str, plant)))
            plantdict = {"province": addressinfo[0], "city": addressinfo[1], "plantCode": plantstr,
                         "infoType": infoType}
            return plantdict

        Abee = [nectar_dict(infoType=1) for i in range(9)]
        Bbee = [nectar_dict(infoType=2) for i in range(9)]
        nectarSourceFlowInputs = json.dumps(Abee + Bbee)
        # nectarSourceFlowInputs =None
        nectarSourcePointAttachInputs = dc.assemble_picture_dictionary(20, remark="接口测试")
        # nectarSourcePointAttachInputs = None
        result = self.action._mobile_nectar_source_point_edit(province_=province, city_=city, county_=county,
                                                              plantCode_=plantCode, lng_=lng, lat_=lat,
                                                              floweringStartDate_=tt.get_random_date(),
                                                              floweringEndDate_=tt.get_random_date(),
                                                              nectarFlow_=tt.get_random_date(), id_=pointid,
                                                              entryDate_=tt.get_random_date(),
                                                              departureDate_=tt.get_random_date(),
                                                              nectarSourceArea_=nectarSourceArea,
                                                              apiaryDensity_=apiaryDensity, purpose_=purpose,
                                                              pesticideCondition_=pesticideCondition,
                                                              nectarSourceFlowInputs_=nectarSourceFlowInputs,
                                                              nectarSourcePointAttachInputs_=nectarSourcePointAttachInputs)
        self.assertEqual(result['status'], 'OK', msg="断言失败")

    def test_mobile_nectar_source_point_detail(self):
        """
        蜜源勘察--详情
        :return:
        """
        pointall = random.choice(self.db.query_nectar_source_point_all())
        pointid = pointall.get('id')
        result = self.action._mobile_nectar_source_point_detail(id_=pointid)
        self.assertEqual(result['status'], 'OK', msg='code码错误')

    def test_mobile_nectar_source_point_del(self):
        """
        蜜源勘察--删除蜜源点
        :return:
        """
        pointtype = random.randint(1, 2)
        pointall = random.choice(
            self.db.query_current_user_creation_point(userid=self.action.user.user_id, usertype=pointtype))
        pointid = pointall.get('id')
        result = self.action._mobile_nectar_source_point_del(id_=pointid)
        if pointtype == 1:
            self.assertEqual(result['status'], 'OK', msg='status错误')
        else:
            self.assertEqual(result['status'], 'ERROR')

    def test_mobile_nectar_source_plant_list(self):
        """
        获取蜜源品种信息
        :return:
        """
        result = self.action._mobile_nectar_source_plant_list()
        self.assertEqual(result['status'], 'ERROR')

    def test_mobile_nectar_source_plant_detail(self):
        plantlist = self.db.query_plant_code_all()
        plantCodes = random.choice(plantlist).get('code')
        result = self.action._mobile_nectar_source_plant_detail(plantCode_=plantCodes)
        self.assertEqual(result['status'], 'OK', msg='code码错误')


if __name__ == '__main__':
    unittest.main()
