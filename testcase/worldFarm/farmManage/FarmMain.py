"""
__author__ = 'Heng Xin'
__date__ = '2018/8/20'

测试集中包括  农场管理  围栏林区管理  地标管理
"""

import time
import json
from random import choice, randint
from testcase.worldFarm import testCase,FarmManage


class FarmMain(testCase):

    fq = FarmManage()

    def test_add_farm(self):
        """
        移动端-农场管理-创建农场
        1.2.4修改
        :return:
        """
        name = "接口测试农场%s" % int(time.time() * 1000)
        address = "中国四川省绵阳市三台县%s" % int(time.time() * 1000)
        lng = 104.03994443737503
        lat = 30.77899307208601
        currencyType = choice(['AUD', 'USD', 'CNY'])
        geo_list = '[{"locations":[{"lng": 104.08544443737503, "lat": 30.82449307208601}, {"lng": 104.08544443737503, "lat": 30.73349307208601}, {"lng": 103.99444443737502, "lat": 30.73349307208601}, {"lng": 103.99444443737502, "lat": 30.82449307208601}, {"lng": 104.08544443737503, "lat": 30.82449307208601}]}]'
        geo_json = json.dumps(json.loads(geo_list))
        register = self.ka.mobile_farm_add(name=name, postcodeId=2, address=address, lng=lng,
                                           lat=lat, currencyType=currencyType, farmRightAddList=geo_json)
        self.assertEqual(register['status'], "OK")
        farmer = self.fq.query_farm_my_farmer(self.email)[0]
        self.assertEqual(name, farmer.get('name'))
        self.assertEqual(address, farmer.get('address'))
        self.assertEqual(lng, farmer.get('lng'))
        self.assertEqual(lat, farmer.get('lat'))
        self.assertEqual(currencyType, farmer.get('currency_type'))

    def test_mobile_farm_update(self):
        """
        移动端-农场管理-编辑农场
        :return:
        """
        geo_list = '[{"locations":[{"lng": 104.08544443737503, "lat": 30.82449307208601}, {"lng": 104.08544443737503, "lat": 30.73349307208601}, {"lng": 103.99444443737502, "lat": 30.73349307208601}, {"lng": 103.99444443737502, "lat": 30.82449307208601}, {"lng": 104.08544443737503, "lat": 30.82449307208601}]}]'
        farmer = self.fq.query_farm_my_farmer(self.email)[0].get('id')
        geo_json = json.dumps(json.loads(geo_list))
        pic_str = [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)]
        pic = ''.join(self.tool.data_assemble(parameters_ld=pic_str, num=8))
        name = "接口测试农场编辑农场信息%s" % int(time.time() * 1000)
        address = "成都市高新区天府大道%s" % int(time.time() * 1000)
        lng = 104.03994443737503
        lat = 30.77899307208601
        rightArea = 24895038.67
        type = choice([10, 20, 30, 40])
        rightNum = randint(1, 50)
        purchasePrice = randint(10000, 9999999)
        register = self.ka.mobile_farm_update(farmId=farmer, name=name, postcodeId=3, address=address,
                                              lng=lng, lat=lat, rightArea=rightArea,
                                              type=type, rightNum=rightNum, purchasePrice=purchasePrice,
                                              farmRightUpdateList=geo_json, pic=pic)
        self.assertEqual(register['status'], "OK")
        farmdate = self.fq.query_update_farm_data(farmer)
        self.assertEqual(name, farmdate.get('name'))
        self.assertEqual(pic, farmdate.get('pic'))
        self.assertEqual(address, farmdate.get('address'))
        self.assertEqual(lng, farmdate.get('lng'))
        self.assertEqual(lat, farmdate.get('lat'))
        self.assertEqual(rightArea, farmdate.get('right_area'))
        self.assertEqual(rightNum, farmdate.get('right_num'))

    def test_mobile_farm_add(self):
        """
        添加农场缺省校验
        :return:
        """
        geo_list = '[{"locations":[{"lat":31.034976885551373,"lng":105.10651153740901},{"lat":30.933928419629027,"lng":104.85937029385036},{"lat":30.719090791291833,"lng":104.93389288881303},{"lat":30.571234296640057,"lng":105.21905583536591},{"lat":30.573853180147438,"lng":105.51942748401791},{"lat":30.952842381895124,"lng":105.61904438345789},{"lat":31.202936087481078,"lng":105.50041659769431},{"lat":31.034976885551373,"lng":105.10651153740901}]}]'
        geo_json = json.dumps(json.loads(geo_list))
        register = self.ka.mobile_farm_add(name="皮卡丘", postcodeId=2, address="中国四川省绵阳市三台县", lng=0, lat=0,
                                           currencyType="AUD", farmRightAddList=geo_json)
        self.assertEqual(register['status'], "OK")

    def test_mobile_farm_del(self):
        """
        移动端-农场管理-删除农场
        :return:
        """
        farmId = self.fq.query_farm_my_farmer(self.email)[0].get('id')
        register = self.ka.mobile_farm_del(farmId=farmId)
        self.assertEqual(register['status'], "OK")

    def test_mobile_farm_list(self):
        """
        移动端-农场管理-查询农场列表
        V1.2.5 修改
        :return:
        """

        register = self.ka.mobile_farm_list()
        farminfo = self.fq.query_my_farm_list(self.email)
        self.assertEqual(register['status'], "OK")
        register = register.get('content')
        for i in range(len(register)):
            self.assertEqual(farminfo[i].get('name'), register[i].get('farmName'))
            self.assertEqual(farminfo[i].get('id'), register[i].get('farmId'))
            self.assertEqual(farminfo[i].get('currency_type'), register[i].get('currencyType'))
            self.assertEqual(farminfo[i].get('address'), register[i].get('address'))
            self.assertEqual(farminfo[i].get('right_area'), register[i].get('rightArea'))
            self.assertEqual(farminfo[i].get('number'), register[i].get('number'))
            self.assertEqual(farminfo[i].get('lat'), register[i].get('lat'))
            self.assertEqual(farminfo[i].get('lng'), register[i].get('lng'))

    def test_admin_farm_detail(self):
        """
        ADMIN-农场管理-农场详情
        1.2.5修改
        :return:
        """
        farmId = self.fq.query_default_farm(self.email)[0]
        register = self.ka.admin_farm_detail(farmId=farmId.get('farm_id'))
        self.assertEqual(register['status'], 'OK')
        farminfo = self.fq.query_one_farm_info(farmid=farmId.get('farm_id'))
        self.assertEqual(farminfo.get('name'), register['content'].get('farmName'))
        self.assertEqual(farminfo.get('currency_type'), register['content'].get('currencyType'))
        self.assertEqual(farminfo.get('address'), register['content'].get('address'))
        self.assertEqual(farminfo.get('right_area'), register['content'].get('rightArea'))
        self.assertEqual(farminfo.get('number'), register['content'].get('number'))
        self.assertEqual(farminfo.get('lat'), register['content'].get('lat'))
        self.assertEqual(farminfo.get('lng'), register['content'].get('lng'))
        self.assertEqual(farminfo.get('postcode_id'), register['content'].get('postcodeId'))

    def test_mobile_farm_set_default(self):
        """
        移动端-农场管理-设置默认农场
        :return:
        """
        farmId = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        # farmId = 547
        register = self.ka.mobile_farm_set_default(farmId=farmId)
        self.assertEqual(register['status'], "OK")

    def test_mobile_farm_detail(self):
        """
        移动端-农场管理-农场详情
        :return:
        """
        farmId = choice(self.fq.query_my_farm_list(self.email)).get('id')
        register = self.ka.mobile_farm_detail(farmId=farmId)
        self.assertEqual(register['status'], 'OK')
        farminfo = self.fq.query_one_farm_info(farmid=farmId)
        self.assertEqual(farminfo.get('name'), register['content'].get('farmName'))
        self.assertEqual(farminfo.get('currency_type'), register['content'].get('currencyType'))
        self.assertEqual(farminfo.get('address'), register['content'].get('address'))
        self.assertEqual(farminfo.get('right_area'), register['content'].get('rightArea'))
        self.assertEqual(farminfo.get('number'), register['content'].get('number'))
        self.assertEqual(farminfo.get('lat'), register['content'].get('lat'))
        self.assertEqual(farminfo.get('lng'), register['content'].get('lng'))
        self.assertEqual(farminfo.get('postcode_id'), register['content'].get('postcodeId'))

    def test_mobile_farm_get_default(self):
        """
        移动端-农场管理-获取默认农场
        1.2.4 修改
        1.2.5 修改
        :return:
        """
        farm_list = self.fq.query_farm_default(self.email)
        register = self.ka.mobile_farm_get_default()
        self.assertEqual(register['status'], 'OK')
        for farm in farm_list:

            if farm.get('id') == register['content']['farmId']:
                self.assertEqual(farm.get('id'), register['content']['farmId'])
                self.assertEqual(farm.get('name'), register['content']['farmName'])
                self.assertEqual(farm.get('address'), register['content']['address'])
                self.assertEqual(farm.get('currency_type'), register['content']['currencyType'])

    def test_mobile_farm_search_condition(self):
        """
        移动端-农场管理-农场围栏/区域/地标筛选条件/分享内容列表
        :return:
        """
        farm_id = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        register = self.ka.mobile_farm_search_condition(farmId=farm_id)
        self.assertEqual(register['status'], 'OK')

    def test_mobile_share_add(self):
        """
        移动端-分享-新增分享农场
        :return:
        """
        landmarkdata = self.fq.query_all_farm_landmark(self.email)
        landmarkType = ','.join(list(set(self.tool.data_assemble('type2', landmarkdata))))
        farmid = landmarkdata[0].get('farm_id')
        register = self.ka.mobile_share_add(farmId=farmid, content='{"landmarkType":"%s"}' % landmarkType)
        self.assertEqual(register['status'], "OK")

    def test_web_share_detail(self):
        """
        Web端-地图分享-查看分享内容
        :return:
        """
        register = self.ka.web_share_detail(shareId="6B8B7412C98FA0925C21AC74EB1B4E87")
        self.assertEqual(register['status'], "OK")

    def test_mobile_farm_right_list(self):
        """
        移动端-产权边界-查询农场的产权边界列表
        :return:
        """
        farm_id = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        register = self.ka.mobile_farm_right_list(farmId=farm_id)
        self.assertEqual(register['status'], "OK")

    def test_mobile_label_list(self):
        """
        移动端-公共自定义标签-照片标签列表
        :return:
        """
        farm_id = choice(self.fq.query_default_farm(self.email)).get('farm_id')
        register = self.ka.mobile_label_list(id=None, bizId=farm_id, nameLike=None)
        self.assertEqual(register['status'], "OK")


if __name__ == '__main__':
    m = FarmMain()
