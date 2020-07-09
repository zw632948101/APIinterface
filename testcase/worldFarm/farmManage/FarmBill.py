#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
__author__ = 'Xiujuan Chen'
__date__ = '2019/10/29'
农场流水
"""
import time
from random import choice
from testcase.worldFarm import testCase,Finance


class Main(testCase):

    fq = Finance()

    def test_mobile_farmBill_add(self):
        """
        新建农场流水 V 1.2.5
        :return:
        """
        farm_id_list = self.fq.query_default_farm(email=self.email)
        farm_id = farm_id_list[0]['farm_id']
        account_book_list = self.fq.query_farm_book_buy_farm_id(farm_id=farm_id, is_default=1)
        book_id = choice(account_book_list).get("id")
        billtype = choice(self.fq.query_farm_finance_bill_type(farm_id))
        price = 500
        record_date = self.tt.get_timestamp()
        remark = "接口测试新增收入流水备注"
        self.ka.mobile_farmBill_add(farmId=farm_id, bookId=book_id, budgetType=billtype.get("budget_type"),
                                    billTypeId=billtype.get('id'), price=price, recordDate=record_date,
                                    remark=remark)
        bill_info_list = self.fq.query_bill_info(farm_id=farm_id, book_id=book_id,
                                                 budget_type=billtype.get("budget_type"))
        record_date_sql = self.tt.str_time_timestamp(bill_info_list[0]["record_date"])
        self.assertEqual(billtype.get('id'), bill_info_list[0]["bill_type_id"])
        self.assertEqual(price, bill_info_list[0]["price"])
        self.assertEqual(record_date, record_date_sql)
        self.assertEqual(remark, bill_info_list[0]["remark"])

    def test_mobile_farmBill_bill_count_page_list(self):
        """
        农场流水分页列表V 1.2.5
        :return:
        """
        farm_id_list = self.fq.query_default_farm(email=self.email)
        farm_id = farm_id_list[0]['farm_id']
        account_book_list = self.fq.query_farm_book_buy_farm_id(farm_id=farm_id, is_default=1)
        book_id = choice(account_book_list).get("id")
        billtype = choice(self.fq.query_farm_finance_bill_type(farm_id))
        budget_type = billtype.get('budget_type')
        bill_type_id = billtype.get('id')
        record_date = int(round(time.time() * 1000))
        register = self.ka.mobile_farmBill_bill_count_page_list(bookId=book_id, budgetType=budget_type,
                                                                billTypeId=bill_type_id, queryDate=record_date)
        income_list = self.fq.query_income_sum_buy_email(book_id, bill_type_id)
        expend_list = self.fq.query_expend_sum_buy_email(book_id, bill_type_id)
        if "incomePrice" in register["content"]:
            income = int(income_list[0]["SUM(tfb.price)"])
            self.assertEqual(register["content"]["incomePrice"], income)
        if "expensePrice" in register["content"]:
            expend = int(expend_list[0]["SUM(tfb.price)"])
            self.assertEqual(register["content"]["expensePrice"], expend)

    def test_mobile_farmBill_del(self):
        """
        删除农场流水 V 1.2.5
        :return:
        """
        bill_list = self.fq.query_bill_list_buy_email(self.email)
        bill_id = bill_list[0]["id"]
        self.ka.mobile_farmBill_del(billId=bill_id)
        delete_bill_list = self.fq.query_bill_info_buy_id(bill_id=bill_id)
        bill_id_sql = delete_bill_list.get("is_delete")
        self.assertEqual(1, bill_id_sql)

    def test_mobile_farmBill_detail(self):
        """
        农场流水详情 V 1.2.5
        :return:
        """
        bill_list = self.fq.query_bill_list_buy_email(self.email)
        bill_id = choice(bill_list).get("id")
        register = self.ka.mobile_farmBill_detail(billId=bill_id)
        bill_info_list = self.fq.query_bill_info_buy_id(bill_id)
        self.assertEqual(register.get('status'), 'OK')
        content = register.get('content')
        create_time = self.tt.str_time_timestamp(bill_info_list.get("create_time"))

        self.assertEqual(content.get("billTypeIcon"), bill_info_list.get("bill_type_icon"))
        self.assertEqual(content.get("billTypeId"), bill_info_list.get("bill_type_id"))
        self.assertEqual(content.get("billTypeName"), bill_info_list.get("bill_type_name"))
        self.assertEqual(content.get("bookId"), bill_info_list.get("book_id"))
        self.assertEqual(content.get("budgetType"), bill_info_list.get("budget_type"))
        self.assertEqual(content.get("createTime"), create_time)
        self.assertEqual(content.get("creator"), bill_info_list.get("username"))
        self.assertEqual(content.get("creatorId"), bill_info_list.get("creator_id"))
        self.assertEqual(content.get("farmId"), bill_info_list.get("farm_id"))
        self.assertEqual(content.get("id"), bill_info_list.get("id"))
        self.assertEqual(content.get("price"), bill_info_list.get("price"))
        self.assertEqual(content.get("remark"), bill_info_list.get("remark"))

    def test_mobile_farmBillType_add(self):
        """
        新建农场流水类别V 1.2.5
        :return:
        """
        farm_id_list = self.fq.query_default_farm(email=self.email)
        farm_id = farm_id_list[0]['farm_id']
        budget_type = 20
        bill_type_name = int(time.time())
        icon_url = "http://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/farm/head/1530012097899.png"
        self.ka.mobile_farmBillType_add(farmId=farm_id, budgetType=budget_type, billTypeName=bill_type_name,
                                        iconUrl=icon_url)
        bill_type_list = self.fq.query_bill_type_buy_email(self.email)
        self.assertEqual(farm_id, bill_type_list[0]["farm_id"])
        self.assertEqual(budget_type, bill_type_list[0]["budget_type"])
        self.assertEqual(bill_type_name, int(bill_type_list[0]["bill_type_name"]))
        self.assertEqual(icon_url, bill_type_list[0]["icon_url"])

    def test_mobile_farmBillType_del(self):
        """
        删除农场流水类别V 1.2.5
        :return:
        """
        bill_type_list = self.fq.query_bill_type_buy_email(self.email)
        bill_type_id = bill_type_list[0]["id"]
        self.ka.mobile_farmBillType_del(billTypeId=bill_type_id)
        type_id_list = self.fq.query_bill_type_buy_id(bill_type_id)
        is_delete = type_id_list.get("is_delete")
        self.assertEqual(1, is_delete)

    def test_mobile_farmBillType_list(self):
        """
        农场流水类别列表V 1.2.5
        :return:
        """
        farm_id_list = self.fq.query_default_farm(email=self.email)
        farm_id = farm_id_list[0]['farm_id']
        budget_type = 10
        register = self.ka.mobile_farmBillType_list(farmId=farm_id, budgetType=budget_type)
        bill_type_list = self.fq.query_bill_type_buy_farm_id(farm_id=farm_id)
        if len(register["content"]) == len(bill_type_list):
            for i in range(len(register["content"])):
                if "isDefault" in register["content"][i]:
                    self.assertEqual(register["content"][i]["billTypeName"], bill_type_list[i]["bill_type_name"])
                    self.assertEqual(register["content"][i]["budgetType"], bill_type_list[i]["budget_type"])
                    self.assertEqual(register["content"][i]["creatorId"], bill_type_list[i]["creator_id"])
                    self.assertEqual(register["content"][i]["farmId"], bill_type_list[i]["farm_id"])
                    self.assertEqual(register["content"][i]["iconUrl"], bill_type_list[i]["icon_url"])
                    self.assertEqual(register["content"][i]["id"], bill_type_list[i]["id"])
                    self.assertEqual(register["content"][i]["isDefault"], bill_type_list[i]["is_default"])
                else:
                    self.assertEqual(register["content"][i]["billTypeName"], bill_type_list[i]["bill_type_name"])
                    self.assertEqual(register["content"][i]["budgetType"], bill_type_list[i]["budget_type"])
                    self.assertEqual(register["content"][i]["creatorId"], bill_type_list[i]["creator_id"])
                    self.assertEqual(register["content"][i]["farmId"], bill_type_list[i]["farm_id"])
                    self.assertEqual(register["content"][i]["iconUrl"], bill_type_list[i]["icon_url"])
                    self.assertEqual(register["content"][i]["id"], bill_type_list[i]["id"])
        else:
            self.log.info("输出信息与数据库信息不匹配！")

    def test_mobile_farmBill_update(self):
        """
        WEB端-农场流水-修改流水【v1.2.7 可对字段】
        :return:
        """
        farm_id = choice(self.fq.query_default_farm(email=self.email)).get('farm_id')
        bill_list = choice(self.fq.query_farm_all_bill(farmid=farm_id))
        bill_type_list = choice(self.fq.query_farm_finance_bill_type(farmid=farm_id))
        price = 700
        record_date = int(round(time.time()) * 1000)
        remark = "接口测试编辑流水备注"
        self.ka.mobile_farmBill_update(id=bill_list.get('id'), farmId=farm_id, bookId=bill_list.get('book_id'),
                                       budgetType=bill_type_list.get('budget_type'),
                                       billTypeId=bill_type_list.get('id'), price=price,
                                       recordDate=record_date, remark=remark)
        billinfo = self.fq.query_bill_info_buy_id(bill_id=bill_list.get('id'))
        self.assertEqual(farm_id, billinfo.get('farm_id'))
        self.assertEqual(bill_list.get('id'), billinfo.get('id'))
        self.assertEqual(bill_list.get('book_id'), billinfo.get('book_id'))
        self.assertEqual(bill_type_list.get('budget_type'), billinfo.get('budget_type'))
        self.assertEqual(bill_type_list.get('id'), billinfo.get('bill_type_id'))
        self.assertEqual(bill_type_list.get('bill_type_name'), billinfo.get('bill_type_name'))
        self.assertEqual(price, billinfo.get('price'))
        self.assertEqual(record_date, self.tt.str_time_timestamp(billinfo.get('record_date')))
        self.assertEqual(remark, billinfo.get('remark'))


if __name__ == '__main__':
    m = Main()
