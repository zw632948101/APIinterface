#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
import random
from unittest import TestCase
from utils.log.logger import logger
from interfaces.flowerChaser.BeeAction import BeeAction
from testcase.flowerChaser.sql.Bee import BeekeeperNearbySql


class BeekeeperNearby(TestCase):
    log = logger('BeekeeperNearby', level='DEBUG').logger
    log.debug('周边蜂友接口测试')

    @staticmethod
    def build_dict(**kwargs) -> dict:
        return kwargs

    def setUp(self) -> None:
        """
        测试前数据准备
        :return:
        """
        self.api = BeeAction()
        self.api.set_user(mobile=19988776655)
        self.db = BeekeeperNearbySql()

    def test_mobile_nearby_bee_friend_page_list(self):
        """
        蜂友分页列表(周边蜂友) mobile/nearby-bee-friend/page-list
        :return: None
        """

        def beekeeper_nearby_search_content() -> dict:
            """
            随机组装查询条件
            :return: dict
            """
            store_content = self.db.sql_beekeeper_nearby_search_content_random()
            search_content = dict()
            search_type = random.randint(0, 3)
            search_content.update(self.build_dict(pn=random.choice([i for i in range(1, 3)])))
            # 不通页面有不通搜索逻辑限制，此处简单限制
            if search_type == 0:
                if random.choice([False, True]):
                    search_key = random.choice([v.get("username") for v in store_content.get('user_name')])
                else:
                    search_key = random.choice([v.get("phone") for v in store_content.get('user_mobile')])
                start_ = random.randint(0, len(search_key))
                end_ = random.randint(start_, len(search_key))
                search_content.update(self.build_dict(searchKey=search_key[start_:end_]))
            elif search_type == 1:
                search_content.update(self.build_dict(mutualLabels=random.sample([v.get("value") for v in store_content.get('mutual_labels_all')],
                                                                                  random.randint(0, len(store_content.get('mutual_labels_all'))))))
                search_content.update(self.build_dict(intentions=random.sample([0, 1, 2], random.randint(0, 3))))
            else:
                from utils.fake.FakeLocation import FakeLocation
                location = FakeLocation().fake_location()
                search_content.update(self.build_dict(lng=location[4]))
                search_content.update(self.build_dict(lat=location[5]))
                if search_type == 2:
                    search_content.update(self.build_dict(searchType='2'))
                    search_content.update(self.build_dict(distanceType=random.choice([1, 2, 3])))
                else:
                    search_content.update(self.build_dict(province=location[0]))
                    search_content.update(self.build_dict(city=location[1]))
                    search_content.update(self.build_dict(county=location[2]))
                    search_content.update(self.build_dict(searchType='1'))

            return search_content

        search_contents = beekeeper_nearby_search_content()
        api_content = self.api._mobile_nearby_bee_friend_page_list(intentions_=search_contents.get("intentions", None),
                                                                   mutualLabels_=search_contents.get("mutualLabels", None),
                                                                   pn_=search_contents.get("pn", None),
                                                                   ps_=search_contents.get("ps", None),
                                                                   searchKey_=search_contents.get("searchKey", None),
                                                                   searchType_=search_contents.get("searchType", None),
                                                                   province_=search_contents.get("province", None),
                                                                   city_=search_contents.get("city", None),
                                                                   county_=search_contents.get("county", None),
                                                                   lng_=search_contents.get("lng", None),
                                                                   lat_=search_contents.get("lat", None),
                                                                   distanceType_=search_contents.get("distanceType", None))
        store_content = self.db.sql_mobile_nearby_bee_friend_page_list(search_contents)
        try:
            if len(store_content) == len(api_content.get('content').get('datas')):
                # 删除值为None的数据
                for item in store_content:
                    for k in list(item.keys()):
                        if item[k] is None:
                            del item[k]

                # 删除返回数据中不断言的 labelList 和 regularSourceStr
                for item in api_content.get('content').get('datas'):
                    for k in list(item.keys()):
                        try:
                            del item["regularSourceStr"]
                            del item["labelList"]
                        except KeyError:
                            pass

                if len(store_content) == 0 and len(api_content.get('content').get('datas')) == 0 :
                    pass
                else:
                    self.assertEqual(api_content.get('content').get('datas'), store_content,
                                     '返回的顺序或数据不一致，接口返回：%s\n数据库返回:%s' % (api_content.get('content').get('datas'), store_content))
            else:
                self.assertFalse(True, '接口返回与数据库返回数据不一致，接口返回%s,\n数据库返回%s' % (api_content, store_content))
        except TypeError:
            if len(api_content.get('content').get('datas')) != 0:
                self.assertFalse(True, '接口返回与数据库返回数据条数不一致，接口返回%s,\n数据库返回%s' % (api_content, store_content))

    def test_mobile_nearby_bee_friend_nearby_list(self):
        """
        附近蜂友列表(周边蜂友) mobile/nearby-bee-friend/nearby-list
        :return: None
        """
        from utils.fake.FakeLocation import FakeLocation
        store_content = self.db.sql_beekeeper_nearby_search_content_random()
        search_contents = dict()
        search_contents.update(self.build_dict(mutualLabels=random.sample([v.get("value") for v in store_content.get('mutual_labels_all')],
                                                           random.randint(0, len(store_content.get('mutual_labels_all')))
                                                                         )))
        location = FakeLocation().fake_location()
        search_contents.update(self.build_dict(lng=location[4]))
        search_contents.update(self.build_dict(lat=location[5]))
        search_contents.update(self.build_dict(distanceType='2'))
        search_contents.update(self.build_dict(searchType='2'))

        api_content = self.api._mobile_nearby_bee_friend_nearby_list(lat_=search_contents.get('lat'),
                                                                     lng_=search_contents.get('lng'),
                                                                     mutualLabels_=search_contents.get('mutualLabels'))
        store_content = self.db.sql_mobile_nearby_bee_friend_page_list(search_contents)
        try:
            if len(store_content) == len(api_content.get('content')):
                # 删除值为None的数据
                for item in store_content:
                    for k in list(item.keys()):
                        if item[k] is None:
                            del item[k]

                # 删除返回数据中不断言的 labelList 和 regularSourceStr
                for item in api_content.get('content'):
                    for k in list(item.keys()):
                        try:
                            del item["regularSourceStr"]
                            del item["labelList"]
                        except KeyError:
                            pass

                if len(store_content) == 0 and len(api_content.get('content')) == 0:
                    pass
                else:
                    self.assertEqual(api_content.get('content'), store_content,
                                     '返回的顺序或数据不一致，接口返回：%s\n数据库返回:%s' % (api_content.get('content'), store_content))
            else:
                self.assertFalse(True, '接口返回与数据库返回数据不一致，接口返回%s,\n数据库返回%s' % (api_content, store_content))
        except TypeError:
            if len(api_content.get('content')) != 0:
                self.assertFalse(True, '接口返回与数据库返回数据条数不一致，接口返回%s,\n数据库返回%s' % (api_content, store_content))

    def test_mobile_nearby_bee_friend_associate(self):
        """
        搜索蜂友，自动联想 mobile/nearby-bee-friend/associate
        :return: None
        """
        search_content = self.db.sql_beekeeper_nearby_search_content_random()
        if random.choice([False, True]):
            search_key = random.choice([v.get("username") for v in search_content.get('user_name')])
        else:
            search_key = random.choice([v.get("phone") for v in search_content.get('user_mobile')])
        start_ = random.randint(0, len(search_key))
        end_ = random.randint(start_, len(search_key))
        store_content = self.db.sql_mobile_nearby_bee_friend_associate(search_key[start_:end_])
        api_content = self.api._mobile_nearby_bee_friend_associate(searchKey_=search_key[start_:end_])
        try:
            if len(store_content) == len(api_content.get('content')):
                # 删除值为None的数据
                for item in store_content:
                    for k in list(item.keys()):
                        if item[k] is None:
                            del item[k]

                if len(store_content) == 0 and len(api_content.get('content')) == 0:
                    pass
                else:
                    self.assertEqual(api_content.get('content'), store_content,
                                     '返回的顺序或数据不一致，接口返回：%s\n数据库返回:%s' % (api_content.get('content'), store_content))
            else:
                self.assertFalse(True, '接口返回与数据库返回数据不一致，接口返回%s,\n数据库返回%s' % (api_content, store_content))
        except TypeError:
            if len(api_content.get('content')) != 0:
                self.assertFalse(True, '接口返回与数据库返回数据条数不一致，接口返回%s,\n数据库返回%s' % (api_content, store_content))

    def test_mobile_nearby_bee_friend_detail(self):
        """
        蜂友详情-用户部分 mobile/nearby-bee-friend/detail
        :return: None
        """
        from datetime import datetime
        search_content = self.db.sql_beekeeper_nearby_search_content_random().get('user_id')[0].get('id')
        # search_content = 505
        store_content = self.db.sql_mobile_nearby_bee_friend_detail(search_content)
        api_content = self.api._mobile_nearby_bee_friend_detail(userId_=search_content)
        if api_content.get('errorCode') == '10100363':
            self.assertEqual(len(store_content), 0)
        else:
            for item in store_content[0]:
                try:
                    if item == 'regularSourceCode':
                        api_content['content']['regularSourceCode'] = ','.join(api_content['content']['regularSourceCode'])
                    if item == 'labelList':
                        api_content['content']['labelList'] = ','.join(
                            [x.get('labelCode') for x in api_content['content']['labelList']]
                        )
                    if item == 'locationUpdateTime':
                        api_content['content']['locationUpdateTime'] = datetime.strftime(datetime.fromtimestamp(api_content['content']['locationUpdateTime']/1000),
                                                                                         '%Y-%m-%d %H:%M:%S')
                except KeyError:
                    continue
                self.assertEqual(store_content[0].get(item),
                                 api_content.get('content').get(item),
                                 '%s不正确' % item)

    def test_mobile_swarm_get_by_user(self):
        # search_content = self.db.sql_beekeeper_nearby_search_content_random().get('user_id')[0].get('id')
        search_content = 505
        store_content = self.db.sql_mobile_swarm_get_by_user(search_content)
        api_content = self.api._mobile_swarm_get_by_user(userId_=search_content)
        self.log.warning(api_content)

        if api_content.get('errorCode') == '10100363':
            self.assertEqual(len(store_content), 0)
        else:
            for item in store_content[0]:
                self.assertEqual(store_content[0].get(item),
                                 api_content.get('content').get(item),
                                 '%s不正确' % item)

