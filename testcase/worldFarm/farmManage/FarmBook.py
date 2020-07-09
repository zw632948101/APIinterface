#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Xiujuan Chen'
__date__ = '2019/10/29'
农场账本
"""
import time
from random import choice
from testcase.worldFarm import testCase,Finance


class Main(testCase):

    fq = Finance()

    def test_mobile_farm_book_add(self):
        """
        新建农场账本 V 1.2.5
        :return:
        """
        farm_id_list = self.fq.query_default_farm(email=self.email)
        farm_id = farm_id_list[0]['farm_id']
        account_book_name = str(int(time.time()))
        self.ka.mobile_farm_book_add(farmId=farm_id, accountBookName=account_book_name)
        account_book_list = self.fq.query_farm_book_buy_farm_id(farm_id=farm_id)
        farm_id_sql = account_book_list[0]["farm_id"]
        account_book_name_sql = account_book_list[0]["account_book_name"]
        self.assertEqual(farm_id, farm_id_sql)
        self.assertEqual(account_book_name, account_book_name_sql)

    def test_mobile_farm_book_set_default(self):
        """
        设置农场默认账本 V 1.2.5
        :return:
        """
        not_account_book_list = self.fq.query_default_farm_not_default_book(self.email)
        if len(not_account_book_list) != 0:
            book_id = not_account_book_list[0]["id"]
            farm_id = not_account_book_list[0]["farm_id"]
            self.ka.mobile_farm_book_set_default(bookId=book_id)
            account_book_list = self.fq.query_farm_book_buy_farm_id(farm_id=farm_id, is_default=1)
            book_id_sql = account_book_list[0]["id"]
            self.assertEqual(book_id, book_id_sql)
        else:
            self.log.info("当前农场暂无其他账本！")

    def test_mobile_farm_book_list(self):
        """
        农场账本列表V 1.2.5
        :return:
        """
        farm_id_list = self.fq.query_default_farm(self.email)
        farm_id = farm_id_list[0]["farm_id"]
        register = self.ka.mobile_farm_book_list(farmId=farm_id)
        farm_book_list = self.fq.query_default_farm_all_book(self.email)
        if len(register["content"]) == len(farm_book_list):
            for i in range(len(register["content"])):
                self.assertEqual(register["content"][i]["accountBookName"], farm_book_list[i]["account_book_name"])
        else:
            self.log.info("输出信息与数据库信息不匹配！")

    def test_mobile_farm_book_get_default_book(self):
        """
        获取农场默认账本信息V 1.2.5
        :return:
        """
        default_farm = self.fq.query_default_farm(self.email)
        farm_id = default_farm[0]["farm_id"]
        account_book_list = self.fq.query_farm_book_buy_farm_id(farm_id=farm_id, is_default=1)
        farm_id = account_book_list[0]["farm_id"]
        self.ka.mobile_farm_book_get_default_book(farmId=farm_id, countType=1)

    def test_mobile_farm_book_detail(self):
        """
        账本详情V 1.2.5
        :return:
        """
        default_farm = self.fq.query_default_farm(self.email)
        farm_id = default_farm[0]["farm_id"]
        book_list = self.fq.query_farm_book_buy_farm_id(farm_id=farm_id, is_default=1)
        book_id = book_list[0]["id"]
        self.ka.mobile_farm_book_detail(bookId=book_id, countType=1, startDate=None, endDate=None)

    def test_mobile_farm_book_del(self):
        """
        删除账本 V 1.2.5
        :return:
        """
        book_list = self.fq.query_default_farm_all_book(self.email)
        book_id = book_list[-1]["id"]
        self.ka.mobile_farm_book_del(bookId=book_id)
        book_info_list = self.fq.query_book_info_buy_id(book_id=book_id)
        is_delete = book_info_list[0]["is_delete"]
        self.assertEqual(1, is_delete)

    def test_mobile_farm_book_update(self):
        """
        WEB端-农场账本-修改账本【v1.2.7 可对字段】   Not Found
        :return:
        """
        book_list = choice(self.fq.query_default_farm_all_book(self.email))
        bookname = '接口测试%s' % (int(time.time()) >> 4)
        self.ka.mobile_farm_book_update(farmId=book_list.get('farm_id'), accountBookId=book_list.get('id'),
                                        accountBookName=bookname)
        book_info_list = self.fq.query_book_info_buy_id(book_id=book_list.get('id'))
        self.assertEqual(bookname, book_info_list[0].get('account_book_name'))


if __name__ == '__main__':
    m = Main()
