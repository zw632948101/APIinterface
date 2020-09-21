#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2020 2020/8/06 17:10
收购单流程
"""
import unittest
from interfaces.flowerChaser.TradeAction import TradeAction
from testcase.flowerChaser.sql.Bee import VisitRecordSql
from utils.fake.FakeLocation import FakeLocation
from testcase.flowerChaser.sql.Trade import ConfigProductSql
from faker import Faker
from utils.dataConversion.dataConversion import DataConversion
import random
import json


class WorkbenchMain(unittest.TestCase, ConfigProductSql, FakeLocation, DataConversion):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    trad = TradeAction()
    pr_db = ConfigProductSql()
    vr = VisitRecordSql()
    fl = FakeLocation()
    fake = Faker(locale="zh_CN")
    trad.set_user('15200000033')

    def test_mobile_purchase_order_add(self):
        """
        V2.4.0 POST /mobile/purchase-order/add  订单生成
        :param self:
        :return:
        """
        remark = '接口测试备注'
        province, city, county, address, lng, lat = self.fl.fake_location()
        seller_id = self.pr_db.query_product_seller_id().get('seller_id')
        product_info = self.pr_db.query_product_info_by_seller_id(seller_id)
        category = product_info['parent_key']
        userinfo_p = self.trad._mobile_manager_purchase_order_friend_list(searchKey_=category)
        userinfo = random.choice(userinfo_p.get('content'))
        userid = userinfo.get('userId')
        product_i = self.trad._mobile_manager_purchase_order_product_sale_list(sellerId_=userid)

        product_json = [{"grade": grade, "price": price, "productId": product_id}]
        product_json = json.dumps(product_json)
        response = self.trad._mobile_manager_purchase_order_add(userId_='', province_=province, city_=city,
                                                                county_=county, address_=address, lng_=lng, lat_=lat,
                                                                remark_=remark, productIds_=product_json)
        self.assertEqual("OK", response["status"])

    def test_mobile_purchase_order_base_info(self):
        """
        POST /mobile/purchase-order/base-info 订单详情-基本信息
        :return:
        """
        order_no = self.pr_db.query_purchase_order()['order_no']
        order_no = 2008061756196901600502
        response = self.trad._mobile_purchase_order_base_info(orderNo_=order_no)
        self.assertEqual("OK", response["status"])

    def test_mobile_purchase_order_product_list(self):
        """
        POST /mobile/purchase-order/product-list 订单详情-商品列表
        :return:
        """
        order_no = self.pr_db.query_purchase_order()['order_no']
        order_no = 2008071510343650100302
        response = self.trad._mobile_purchase_order_product_list(orderNo_=order_no)
        self.assertEqual("OK", response["status"])

    def test_admin_purchase_order_base_info(self):
        """
        POST /admin/purchase-order/base-info 订单详情-基本信息
        :return:
        """
        order_no = self.pr_db.query_purchase_order()['order_no']
        order_no = 2008061551453441600302
        response = self.trad._admin_purchase_order_base_info(orderNo_=order_no)
        self.assertEqual("OK", response["status"])

    def test_admin_purchase_order_pay_apply(self):
        """
        POST /admin/purchase-order/pay-apply 订单详情-打款记录
        new v2.4.0
        :return:
        """
        order_no = self.pr_db.query_purchase_order()['order_no']
        order_no = 2008061551453441600302
        response = self.trad._admin_purchase_order_pay_apply(orderNo_=order_no)
        self.assertEqual("OK", response["status"])

    def test_admin_purchase_order_opt_log(self):
        """
        POST /admin/purchase-order/opt-log 订单详情-操作日志
        new v2.4.0
        :return:
        """
        order_no = self.pr_db.query_purchase_order()['order_no']
        order_no = 2008061551453441600302
        response = self.trad._admin_purchase_order_opt_log(orderNo_=order_no)
        self.assertEqual("OK", response["status"])

    def test_admin_purchase_order_status_count(self):
        """
        POST /admin/purchase-order/status-count 订单-状态分类统计
        :return:
        """
        response = self.trad._admin_purchase_order_status_count()
        db_response = self.pr_db.query_purchase_order_status_count()[0]
        self.assertEqual(db_response['全部'], response['content']["totalNum"])
        self.assertEqual(db_response['待审核'], response['content']["reviewedNum"])
        self.assertEqual(db_response['待质检'], response['content']["qualityNum"])
        self.assertEqual(db_response['待确认'], response['content']["unConfirmNum"])
        self.assertEqual(db_response['待结算尾款'], response['content']["unSettledNum"])
        self.assertEqual(db_response['已完成'], response['content']["finishNum"])

    def test_admin_purchase_order_page_list(self):
        """
        POST /admin/purchase-order/page-list 订单-分页列表
        :return:
        """
        response = self.trad._admin_purchase_order_page_list()
        self.assertEqual("OK", response["status"])

    def test_admin_purchase_order_product_info(self):
        """
        POST /admin/purchase-order/product-info 订单详情-商品信息
        :return:
        """
        order_no = 2008071038390690100502
        response = self.trad._admin_purchase_order_product_info(orderNo_=order_no)
        self.assertEqual("OK", response["status"])

    def test_admin_purchase_order_edit_grade(self):
        """
        POST /admin/purchase-order/edit-grade 修改收购价
        :return:
        """
        product_p = self.pr_db.query_product_by_status()
        product_id = product_p['id']
        category = product_p['category']
        product_c = self.trad._admin_purchase_order_product_grade_list(category_=category)
        i = random.randrange(0, 3)
        grade = product_c["content"][i]["grade"]
        price = product_c["content"][i]["price"] * 100
        response = self.trad._admin_purchase_order_edit_grade(productId_=32, grade_=grade, price_=price)
        self.assertEqual("OK", response["status"])

    def test_admin_purchase_order_confirm_grade(self):
        """
        POST /admin/purchase-order/confirm-grade 确认收购价
        :return:
        """
        order_no = 2008071719290591600702
        response = self.trad._admin_purchase_order_confirm_grade(orderNo_=order_no)
        self.assertEqual("OK", response["status"])

    def test_admin_purchase_order_product_grade_list(self):
        """
        POST /mobile/purchase-order/product-grade-list 定价标准列表
        :return:
        """
        category = 1001403
        response = self.trad._admin_purchase_order_product_grade_list(category_=category)
        self.assertEqual("OK", response["status"])

    def test_admin_quality_add(self):
        """
        POST /admin/quality/add 新增质检信息
        :return:
        """
        images = 'https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-user/headImg/1596765774337.jpeg'
        order_no = 2008071719290591600702
        type = random.choice([1, 2])
        type = 1
        remark = None
        deduct_price = None
        if type == 2:
            remark = remark = self.fake.text(max_nb_chars=100)
            deduct_price = random.randint(100, 1000)
        response = self.trad._admin_quality_add(images_=images, orderNo_=order_no, type_=type, remark_=remark,
                                                deductPrice_=deduct_price)
        self.assertEqual("OK", response["status"])

    def test_admin_quality_edit(self):
        """
        POST /admin/quality/edit 编辑质检信息
        :return:
        """
        images = 'https://zyp-farm-2.oss-ap-southeast-1.aliyuncs.com/data/fc-user/headImg/1596765774337.jpeg'
        quality_id = 20
        type = random.choice([1, 2])
        type = 1
        remark = None
        deduct_price = None
        if type == 2:
            remark = self.fake.text(max_nb_chars=100)
            deduct_price = random.randint(100, 100000)
        response = self.trad._admin_quality_edit(images_=images, qualityId_=quality_id, type_=type, remark_=remark,
                                                 deductPrice_=deduct_price)
        self.assertEqual("OK", response["status"])

    def test_admin_quality_del(self):
        """
        POST /admin/quality/del 删除质检信息
        :return:
        """
        quality_id = 12
        response = self.trad._admin_quality_del(qualityId_=quality_id)
        self.assertEqual("OK", response["status"])

    def test_admin_purchase_order_quality_commit(self):
        """
        POST /admin/purchase-order/quality-commit 确认质检结果
        :return:
        """
        order_no = 2008071719290591600702
        response = self.trad._admin_purchase_order_quality_commit(orderNo_=order_no)
        self.assertEqual("OK", response["status"])

    def test_admin_quality_info(self):
        """
        POST /admin/quality/info 获取质检信息
        :return:
        """
        order_no = 2008071038390690100502
        response = self.trad._admin_quality_info(orderNo_=order_no)
        self.assertEqual("OK", response["status"])

    def test_mobile_purchase_order_deduction_confirm(self):
        """
        POST /mobile/purchase-order/deduction-confirm 确认扣款/确认收购价格
        :return:
        """
        order_id = 32
        response = self.trad._mobile_purchase_order_deduction_confirm(orderId_=order_id)
        self.assertEqual("OK", response["status"])

    def test_admin_pay_apply_add(self):
        """
        POST /admin/pay-apply/add 新建打款申请单
        :return:
        """
        order_no = 2008071510343650100302
        amount = 300
        type = 2
        payee_id = 1315
        remark = self.fake.text(max_nb_chars=100)
        response = self.trad._admin_pay_apply_add(orderNo_=order_no, amount_=amount, type_=type, payeeId_=payee_id,
                                                  remark_=remark)
        self.assertEqual("OK", response["status"])

    def test_admin_pay_apply_audit(self):
        """
        POST /admin/pay-apply/audit 审核打款申请单
        :return:
        """
        apply_id = 12
        type = 30
        reason = None
        if type == 20:
            reason = self.fake.text(max_nb_chars=100)
        response = self.trad._admin_pay_apply_audit(applyId_=apply_id, type_=type, reason_=reason)
        self.assertEqual("OK", response["status"])

    def test_admin_pay_apply_confirm(self):
        """
        POST /admin/pay-apply/confirm 确认打款
        :return:
        """
        apply_id = 12
        response = self.trad._admin_pay_apply_confirm(applyId_=apply_id)
        self.assertEqual("OK", response["status"])
