#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2019 2019/12/30 15:05
@Author: hengxin
"""

import random
import json
from testcase.flowerChaser.sql.Bee import ConfigInformationSql
from utils.dataRequest.dataRequester import Request


class FakeLocation(object):
    config_db = ConfigInformationSql()
    req = Request()

    def fake_location(self):
        city_id = ''
        while city_id == '':
            lat = random.uniform(28.549271, 41.581054)
            lng = random.uniform(85.205565, 117.593261)
            address_res = self.req.get('https://restapi.amap.com/v3/geocode/regeo?key=7c0cae0c8cbe417c489a613ec254b4cb'
                                       '&location=%s,%s' % (lng, lat))
            address_json = json.loads(address_res)
            address = address_json["regeocode"]["formatted_address"]

            if address:
                # province = address_json["regeocode"]["addressComponent"]["province"]
                district = address_json["regeocode"]["addressComponent"]["district"]
                city = address_json["regeocode"]["addressComponent"]["city"]
                district = district[:2]
                province = address_json["regeocode"]["addressComponent"]["province"]
                if city is not None:
                    try:
                        if len(city) > 2:
                            city_id = str(self.config_db.sql_id_by_full_name(city[:2])[0]["id"])
                        else:
                            city_id = str(self.config_db.sql_id_by_full_name(city)[0]["id"])
                        province_id = self.config_db.query_province_id_by_province_name(province[:2]).get('id')
                        district_id = self.config_db.query_reason_cityid_by_full_name(city_id, district).get('id')
                        return province_id, city_id, district_id, address, lng, lat
                    except IndexError:
                        city_id = ''
                else:
                    city_id = ''
            else:
                city_id = ''


if __name__ == '__main__':
    fake_location = FakeLocation()
    fake_location.fake_location()
