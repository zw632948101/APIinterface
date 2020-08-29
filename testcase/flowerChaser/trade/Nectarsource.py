from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log import log
from utils.fake.FakeLocation import FakeLocation
import faker
import pymysql
import random
import unittest

class Nectarsource_auth(unittest.TestCase):

    """
    FC2.5.0接口
    """
    action = BeeAction()
    log.info("执行用例")
    action.set_user(19988776655)
    fl = FakeLocation()
    f = faker.Faker(locale='zh-CN')


    def setUp(self):
        """
        连接数据库
        :return:
        """
        try:
            self.connection = pymysql.connect(
                '192.168.62.211',
                'farm',
                'WorldFarm',
                'fc-bee',
                charset='utf8'
            )
            print('数据库连接成功')

        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))


    def tearDown(self):
        self.connection.close()
        print('关闭数据库')

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
        curs = self.connection.cursor()
        sql_province = """SELECT id FROM t_region WHERE `level`=0"""
        sql_city = """SELECT id FROM t_region WHERE `level`=1"""
        sql_count = """SELECT id FROM t_region WHERE `level`=2"""
        sql_plantCode = """SELECT `code` FROM t_nectar_source_plant"""
        curs.execute(sql_province)
        a = curs.fetchall()
        curs.execute(sql_city)
        b = curs.fetchall()
        curs.execute(sql_count)
        c = curs.fetchall()
        curs.execute(sql_plantCode)
        d = curs.fetchall()
        province = a[random.randint(0,len(a))][0]
        city = b[random.randint(0,len(b))][0]
        county = c[random.randint(0,len(c))][0]
        plantCode = d[random.randint(0,len(d))][0]
        result = self.action._mobile_nectar_source_point_add(province_= province,city_= city,
                                                             county_= county,
                                                             plantCode_= plantCode,
                                                             lng_= random.uniform(85.205565, 117.593261),
                                                             lat_= random.uniform(28.549271, 41.581054),
                                                             floweringStartDate_= 1507,
                                                             floweringEndDate_= 1508,
                                                             purpose_= 1)
        log.info("插入数据为-->province:%s ; city:%s ; county:%s ; plantCode:%s" % (province, city, county, plantCode))
        curs = self.connection.cursor()
        sql = """SELECT * FROM t_nectar_source_point WHERE province=%s AND city=%s AND county=%s AND plant_code=%s"""
        curs.execute(sql % (province,city,county,plantCode))
        result_sql = curs.fetchall()
        self.connection.close()
        print(result_sql)
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
        #随机取数量小于5的蜜源点ID
        sql = """SELECT point_id FROM t_nectar_source_flow GROUP BY point_id HAVING count(point_id)<5 """
        curs.execute(sql)
        log.info("----执行查询语句----")
        result = curs.fetchall()
        id = result[random.randint(0,len(result))][0]
        log.info("查询蜜源点ID为： {}".format(id))
        sum_sql_id = """SELECT * FROM t_nectar_source_flow WHERE point_id=%s"""
        #查询数据库中ID的数据条数
        log.info('执行sum_sql_ID查询语句')
        curs.execute(sum_sql_id, id)
        result = curs.fetchall()
        sum = len(result)
        result = self.action._mobile_nectar_source_point_detail(id_= id)
        self.assertEqual(result['status'], 'OK',msg='code码错误')
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