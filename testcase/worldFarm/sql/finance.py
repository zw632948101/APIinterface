#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2019 2019/12/30 11:16
__author__: wei.zhang
__remark__: 财务
"""
from .. import FarmQuery


class Finance(FarmQuery):
    def __init__(self):
        super(Finance, self).__init__()
        self.level = 'CattleManage'

    def query_farm_book_buy_farm_id(self, farm_id, is_default=None):
        """
        查询默认农场下的账本信息
        :return:
        """
        if is_default is None:
            is_default = "AND (tfab.is_default = 1 OR tfab.is_default =0)"
        elif is_default == 1:
            is_default = "AND tfab.is_default = 1"
        else:
            is_default = "AND tfab.is_default = 0"

        sql = """SELECT
                    tfab.*
                FROM
                    `world-koala`.t_farm_account_book tfab
                WHERE
                    tfab.is_delete =0
                    AND tfab.farm_id = '%s'
                    %s
                    ORDER BY tfab.id DESC;""" % (farm_id, is_default)
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_bill_info(self, farm_id, book_id, budget_type):
        """
        查询账本信息
        :return:
        """
        sql = """SELECT
                    tfb.*
                FROM
                    `world-koala`.t_farm_bill tfb
                WHERE
                    tfb.farm_id = '%s'
                    AND tfb.book_id = '%s' 
                    AND budget_type = '%s' ORDER BY id DESC;""" % (farm_id, book_id, budget_type)
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_default_farm_not_default_book(self, email):
        """
        查询默认农场的非默认账本
        :return:
        """
        sql = """SELECT
                    tfab.id,
                    tfu.farm_id,
                    tfab.account_book_name,
                    tfab.is_default,
                    tfab.create_time
                FROM
                    `world-user`.t_user tu
                    LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                    LEFT JOIN `world-koala`.t_farm_account_book tfab ON tfu.farm_id = tfab.farm_id
                WHERE
                    tu.email = '%s' 
                    AND tu.is_delete = 0 
                    AND tfu.is_delete = 0 
                    AND tfu.is_default = 1
                    AND tfab.is_default = 0
                    AND tfab.is_delete = 0;""" % email
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_default_farm_all_book(self, email):
        """
        查询默认农场的所有账本
        :return:
        """
        sql = """SELECT
                    tfab.id,
                    tfu.farm_id,
                    tfab.account_book_name,
                    tfab.is_default,
                    tfab.create_time,
                    tfab.edit_time
                FROM
                    `world-user`.t_user tu
                    LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                    LEFT JOIN `world-koala`.t_farm_account_book tfab ON tfu.farm_id = tfab.farm_id
                WHERE
                    tu.email = '%s' 
                    AND tu.is_delete = 0 
                    AND tfu.is_delete = 0 
                    AND tfu.is_default = 1
                    AND tfab.is_delete = 0;""" % email
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_book_info_buy_id(self, book_id):
        """
        通过账本id查询账本信息
        :return:
        """
        sql = """SELECT
                    tfab.*
                FROM
                    `world-koala`.t_farm_account_book tfab
                WHERE
                    tfab.id = '%s';""" % book_id
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_bill_list_buy_email(self, email):
        """
        查询默认农场下默认账本的流水信息
        :return:
        """
        sql = """SELECT
                    tfb.*
                FROM
                    `world-user`.t_user tu
                    LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                    LEFT JOIN `world-koala`.t_farm_account_book tfab ON tfu.farm_id = tfab.farm_id
                    LEFT JOIN `world-koala`.t_farm_bill tfb ON tfab.id = tfb.book_id
                WHERE
                    tu.email = '%s' 
                    AND tu.is_delete = 0 
                    AND tfu.is_delete = 0 
                    AND tfu.is_default = 1
                    AND tfab.is_default = 1
                    AND tfab.is_delete = 0
                    AND tfb.is_delete = 0;""" % email
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_bill_info_buy_id(self, bill_id):
        """
        通过流水id查询流水信息
        :return:
        """
        sql = """SELECT
                    tfb.*,
                    tu.username
                FROM
                    `world-koala`.t_farm_bill tfb
                    LEFT JOIN `world-user`.t_user tu ON tu.id = tfb.creator_id
                WHERE
                    tfb.id = '%s';""" % bill_id
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info[0]
        return

    def query_income_sum_buy_email(self, book_id, bill_type_id=None):
        """
        通过邮箱号查询默认农场的默认账本当天的收入统计
        :return:
        """
        if bill_type_id is None:
            bill_type_id = ""
        else:
            bill_type_id = "AND tfb.bill_type_id = %s" % bill_type_id
        sql = """SELECT
                    SUM(tfb.price)
                FROM
                    `world-koala`.t_farm_bill tfb 
                WHERE
                    tfb.book_id = %s
                    AND tfb.budget_type = 10
                    AND tfb.is_delete = 0
                    %s
                    AND TO_DAYS(record_date) = TO_DAYS(NOW());""" % (book_id, bill_type_id)
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_expend_sum_buy_email(self, book_id, bill_type_id):
        """
        通过邮箱号查询默认农场的默认账本当天的支出统计
        :return:
        """
        if bill_type_id is None:
            bill_type_id = ""
        else:
            bill_type_id = "AND tfb.bill_type_id = %s" % bill_type_id
        sql = """SELECT
                    SUM(tfb.price)
                FROM
                    `world-koala`.t_farm_bill tfb 
                WHERE
                    tfb.book_id = %s
                    AND tfb.budget_type = 20
                    AND tfb.is_delete = 0
                    %s
                    AND TO_DAYS(record_date) = TO_DAYS(NOW());""" % (book_id, bill_type_id)
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_bill_type_buy_email(self, email):
        """
        通过邮箱号查询流水类别
        :return:
        """
        sql = """SELECT
                    tfbt.*
                FROM
                    `world-user`.t_user tu
                    LEFT JOIN `world-koala`.t_farm_user tfu ON tfu.user_id = tu.id
                    LEFT JOIN `world-koala`.t_farm_bill_type tfbt ON tfu.farm_id = tfbt.farm_id
                WHERE
                    tu.email = '%s' 
                    AND tu.is_delete = 0 
                    AND tfu.is_delete = 0 
                    AND tfu.is_default = 1
                    AND tfbt.is_delete = 0 ORDER BY id DESC;""" % email
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_bill_type_buy_farm_id(self, farm_id):
        """
        通过农场id查询流水类别
        :return:
        """
        sql = """SELECT
                     tfbt.*
                 FROM
                     `world-koala`.t_farm_bill_type tfbt
                 WHERE
                     tfbt.is_delete = 0
                     AND tfbt.budget_type =10
                     AND (tfbt.farm_id = 0 OR tfbt.farm_id = "%s");""" % farm_id
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_farm_finance_bill_type(self, farmid):
        """
        查询当前账本的全部流水类别
        :param farmid:
        :return:
        """
        sql = """
            SELECT
                tfbt.farm_id,
                tfbt.id,
                tfbt.budget_type,
                tfbt.bill_type_name 
            FROM
                `world-koala`.t_farm_bill_type tfbt
            WHERE
                tfbt.farm_id = '%s'
                AND tfbt.is_delete = 0
                OR tfbt.farm_id = 0;
               """ % farmid
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return

    def query_bill_type_buy_id(self, bill_type_id):
        """
        根据流水分类id查询流水分类信息
        :return:
        """
        sql = """
            SELECT
                * 
            FROM
                `world-koala`.t_farm_bill_type tb 
            WHERE
                tb.id = '%s'
              """ % bill_type_id
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info[0]
        return

    def query_farm_all_bill(self, farmid):
        """
        通过农场id查询全部流水
        :param farmid:
        :return:
        """
        sql = """
        SELECT * FROM `world-koala`.t_farm_bill tb WHERE tb.farm_id = %s AND tb.is_delete = 0
              """ % farmid
        info = self.operate(self.hostip, 'world-koala', sql)
        if info:
            return info
        return
