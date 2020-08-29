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
        result = self.action._mobile_nectar_source_point_list(purpose_=2)

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
        nectarSourcePointAttachInputs =''
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
                                                             nectarSourceFlowInputs_=nectarSourceFlowInputs)
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
        result = self.action._mobile_nectar_source_point_edit()

    def test_mobile_nectar_source_point_detail(self):
        """
        蜜源勘察--详情
        :return:
        """
        curs = self.connection.cursor()
        # 随机取数量小于5的蜜源点ID
        sql = """SELECT point_id FROM t_nectar_source_flow GROUP BY point_id HAVING count(point_id)<5 """
        curs.execute(sql)
        log.info("----执行查询语句----")
        result = curs.fetchall()
        id = result[random.randint(0, len(result))][0]
        log.info("查询蜜源点ID为： {}".format(id))
        sum_sql_id = """SELECT * FROM t_nectar_source_flow WHERE point_id=%s"""
        # 查询数据库中ID的数据条数
        log.info('执行sum_sql_ID查询语句')
        curs.execute(sum_sql_id, id)
        result = curs.fetchall()
        sum = len(result)
        result = self.action._mobile_nectar_source_point_detail(id_=id)
        self.assertEqual(result['status'], 'OK', msg='code码错误')
        self.assertEqual(len(result['content']['flowOutputs']), sum, msg='返回数据与数据库查询的数据条数不一致')

    def test_mobile_nectar_source_point_del(self):
        """
        蜜源勘察--删除蜜源点
        :return:
        """
        result = self.action._mobile_nectar_source_point_del(id_=500)
        self.assertEqual(result['status'], 'OK', msg='status错误')

    def test_mobile_nectar_source_plant_list(self):
        """
        获取蜜源品种信息
        :return:
        """
        self.action._mobile_nectar_source_plant_list()


if __name__ == '__main__':
    unittest.main()
