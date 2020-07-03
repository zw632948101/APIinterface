#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
import unittest
from interfaces.flowerChaser.BeeAction import BeeAction
from utils.log import log
from testcase.flowerChaser.sql.Bee import ContainerInformationSql, PurchaseSql
import random
from faker import Faker
import time, datetime
import json


class ContainerMain(unittest.TestCase):
    """
    接口文档:http://192.168.62.242:36054/swagger-ui.html
    """
    container = BeeAction()
    container_db = ContainerInformationSql()
    purchase_db = PurchaseSql()

    log.info("开始执行合同管理接口测试用例")
    fake = Faker(locale="zh_CN")
    container.set_user('19982917912')

    def test_mobile_purchase_add(self):
        """
        POST _mobile_contract_add
        新增合同 new 1.2.1
        :return:
        """
        friend_id_list = self.purchase_db.query_customer_id()
        user_id = friend_id_list[0]['user_id']
        sign_time = (int(time.time())) * 1000
        num = random.randint(1, 99)
        remark = '接口测试新增采购单备注文案'
        img_list = ["http://a0.att.hudong.com/78/52/01200000123847134434529793168.jpg"]
        img_json = json.dumps(img_list, ensure_ascii=False)
        self.container._mobile_contract_add(userId_=user_id, amount_=num, handsel_=num, identityFront_=img_json,
                                            identityBack_=img_json, bankFront_=img_json, bankBack_=img_json,
                                            contractPics_=img_json,
                                            signTime_=sign_time, hiveNum_=num, standardNum_=num, smallNum_=num,
                                            tent_=num, honeyMachine_=num, scraper_=num, motorcycle_=num,
                                            honeypot_=num, alternator_=num, solarPanel_=num, remark_=remark)
        # contract_info = self.purchase_db.query_contract_info(friend_id=user_id)
        # self.assertEqual(num, contract_info[0]['amount'])
        # self.assertEqual(num, contract_info[0]['handsel'])
        # self.assertEqual(img_json, contract_info[0]['identity_front'])
        # self.assertEqual(img_json, contract_info[0]['identity_back'])
        # self.assertEqual(img_json, contract_info[0]['bank_front'])
        # self.assertEqual(img_json, contract_info[0]['bank_back'])
        # self.assertEqual(img_json, contract_info[0]['contract_pics'])
        # # assert_time = time.strftime(str(sign_time), "%Y-%m-%d %H:%M:%S")
        # # self.assertEqual(assert_time, contract_info[0]['sign_time'])
        # self.assertEqual(num, contract_info[0]['hive_num'])
        # self.assertEqual(num, contract_info[0]['standard_num'])
        # self.assertEqual(num, contract_info[0]['small_num'])
        # self.assertEqual(num, contract_info[0]['tent'])
        # self.assertEqual(num, contract_info[0]['honey_machine'])
        # self.assertEqual(num, contract_info[0]['scraper'])
        # self.assertEqual(num, contract_info[0]['motorcycle'])
        # self.assertEqual(num, contract_info[0]['honeypot'])
        # self.assertEqual(num, contract_info[0]['alternator'])
        # self.assertEqual(num, contract_info[0]['solar_panel'])
        # self.assertEqual(remark, contract_info[0]['remark'])

    def test_mobile_purchase_edit(self):
        """
        POST /mobile/purchase/edit  修改为 mobile/contract/edit
        编辑采购单和采购清单 new 1.2
        合同编辑(含清单) V1.2.1 修改
        :return:
        """
        purchase = self.purchase_db.query_contract_id()
        purchase_id = random.choice(purchase).get('id')
        contract_no = int(time.time())
        num = random.randint(1, 100)
        remark = '接口测试编辑采购单和采购清单采购单备注文案'
        img_list = ["http://a0.att.hudong.com/78/52/01200000123847134434529793168.jpg"]
        img_json = json.dumps(img_list, ensure_ascii=False)
        sign_time = (int(time.time())) * 1000
        # if purchase[0]['status'] == 1:
        #     status = random.choice([1, 2, 3, 4])
        #     if status == 2 or status == 3:
        self.container._mobile_contract_edit(id_=purchase_id, identityFront_=img_json,
                                             identityBack_=img_json, bankFront_=img_json, bankBack_=img_json,
                                             contractPics_=img_json,
                                             signTime_=sign_time, standardNum_=num, smallNum_=num,
                                             tent_=num, honeyMachine_=num, scraper_=num, motorcycle_=num,
                                             honeypot_=num, alternator_=num, solarPanel_=num, remark_=remark)
        purchase_detail = self.purchase_db.query_contract_info_by_contract_id(contract_id=purchase_id)
        # self.assertEqual(status, purchase_detail[0]['status'])
        # self.assertEqual(contract_no, int(purchase_detail[0]['contract_no']))
        # self.assertEqual(num, purchase_detail[0]['amount'])
        # self.assertEqual(num, purchase_detail[0]['hive_num'])
        self.assertEqual(img_json, purchase_detail[0]['identity_front'])
        self.assertEqual(img_json, purchase_detail[0]['identity_back'])
        self.assertEqual(img_json, purchase_detail[0]['bank_front'])
        self.assertEqual(img_json, purchase_detail[0]['bank_back'])
        self.assertEqual(img_json, purchase_detail[0]['contract_pics'])
        self.assertEqual(num, purchase_detail[0]['standard_num'])
        self.assertEqual(num, purchase_detail[0]['small_num'])
        self.assertEqual(num, purchase_detail[0]['tent'])
        self.assertEqual(num, purchase_detail[0]['honey_machine'])
        self.assertEqual(num, purchase_detail[0]['scraper'])
        self.assertEqual(num, purchase_detail[0]['motorcycle'])
        self.assertEqual(num, purchase_detail[0]['honeypot'])
        self.assertEqual(num, purchase_detail[0]['alternator'])
        self.assertEqual(num, purchase_detail[0]['solar_panel'])
        self.assertEqual(remark, purchase_detail[0]['remark'])
        #     else:
        #         self.container._mobile_purchase_edit(id_=purchase_id, status_=status)
        #         purchase_detail = self.purchase_db.query_purchase_detail(purchase_id)
        #         self.assertEqual(status, purchase_detail[0]['status'])
        # elif purchase[0]['status'] == 2:
        #     status = random.choice([2, 3, 4])
        #     if status == 2 or status == 3:
        #         self.container._mobile_purchase_edit(id_=purchase_id, status_=status, contractNo_=contract_no,
        #                                              amount_=num,
        #                                              hiveNum_=num, standardNum_=num, smallNum_=num, tent_=num,
        #                                              honeyMachine_=num, scraper_=num, motorcycle_=num,
        #                                              honeypot_=num, alternator_=num, solarPanel_=num, remark_=remark)
        #         purchase_detail = self.purchase_db.query_purchase_detail(purchase_id=purchase_id)
        #         self.assertEqual(status, purchase_detail[0]['status'])
        #         self.assertEqual(contract_no, int(purchase_detail[0]['contract_no']))
        #         self.assertEqual(num, purchase_detail[0]['amount'])
        #         self.assertEqual(num, purchase_detail[0]['hive_num'])
        #         self.assertEqual(num, purchase_detail[0]['standard_num'])
        #         self.assertEqual(num, purchase_detail[0]['small_num'])
        #         self.assertEqual(num, purchase_detail[0]['tent'])
        #         self.assertEqual(num, purchase_detail[0]['honey_machine'])
        #         self.assertEqual(num, purchase_detail[0]['scraper'])
        #         self.assertEqual(num, purchase_detail[0]['motorcycle'])
        #         self.assertEqual(num, purchase_detail[0]['honeypot'])
        #         self.assertEqual(num, purchase_detail[0]['alternator'])
        #         self.assertEqual(num, purchase_detail[0]['solar_panel'])
        #         self.assertEqual(remark, purchase_detail[0]['remark'])
        #     else:
        #         self.container._mobile_purchase_edit(id_=purchase_id, status_=status)
        #         purchase_detail = self.purchase_db.query_purchase_detail(purchase_id)
        #         self.assertEqual(status, purchase_detail[0]['status'])
        # elif purchase[0]['status'] == 3:
        #     status = random.choice([3, 4])
        #     if status == 3:
        #         self.container._mobile_purchase_edit(id_=purchase_id, status_=status, contractNo_=contract_no,
        #                                              amount_=num,
        #                                              hiveNum_=num, standardNum_=num, smallNum_=num, tent_=num,
        #                                              honeyMachine_=num, scraper_=num, motorcycle_=num,
        #                                              honeypot_=num, alternator_=num, solarPanel_=num, remark_=remark)
        #         purchase_detail = self.purchase_db.query_purchase_detail(purchase_id=purchase_id)
        #         self.assertEqual(status, purchase_detail[0]['status'])
        #         self.assertEqual(contract_no, int(purchase_detail[0]['contract_no']))
        #         self.assertEqual(num, purchase_detail[0]['amount'])
        #         self.assertEqual(num, purchase_detail[0]['hive_num'])
        #         self.assertEqual(num, purchase_detail[0]['standard_num'])
        #         self.assertEqual(num, purchase_detail[0]['small_num'])
        #         self.assertEqual(num, purchase_detail[0]['tent'])
        #         self.assertEqual(num, purchase_detail[0]['honey_machine'])
        #         self.assertEqual(num, purchase_detail[0]['scraper'])
        #         self.assertEqual(num, purchase_detail[0]['motorcycle'])
        #         self.assertEqual(num, purchase_detail[0]['honeypot'])
        #         self.assertEqual(num, purchase_detail[0]['alternator'])
        #         self.assertEqual(num, purchase_detail[0]['solar_panel'])
        #         self.assertEqual(remark, purchase_detail[0]['remark'])
        #     else:
        #         self.container._mobile_purchase_edit(id_=purchase_id, status_=status)
        #         purchase_detail = self.purchase_db.query_purchase_detail(purchase_id)
        #         self.assertEqual(status, purchase_detail[0]['status'])
        # else:
        #     self.container._mobile_purchase_edit(id_=purchase_id, status_=4)
        #     purchase_detail = self.purchase_db.query_purchase_detail(purchase_id)
        #     self.assertEqual(4, purchase_detail[0]['status'])

    def test_mobile_purchase_edit_purchase_detail(self):
        """
        POST /mobile/purchase/edit-purchase-detail
        编辑采购清单 new 1.2
        :return:
        """
        purchase = self.purchase_db.query_purchase_id()
        purchase_id = purchase[0]['id']
        num = random.randint(1, 100)
        remark = '接口测试新增采购单备注文案'
        self.container._mobile_purchase_edit_purchase_detail(id_=purchase_id, amount_=num, hiveNum_=num,
                                                             standardNum_=num, smallNum_=num, tent_=num,
                                                             honeyMachine_=num, scraper_=num, motorcycle_=num,
                                                             honeypot_=num, alternator_=num, solarPanel_=num,
                                                             remark_=remark)
        purchase_detail = self.purchase_db.query_purchase_detail(purchase_id=purchase_id)
        self.assertEqual(num, purchase_detail[0]['amount'])
        self.assertEqual(num, purchase_detail[0]['hive_num'])
        self.assertEqual(num, purchase_detail[0]['standard_num'])
        self.assertEqual(num, purchase_detail[0]['small_num'])
        self.assertEqual(num, purchase_detail[0]['tent'])
        self.assertEqual(num, purchase_detail[0]['honey_machine'])
        self.assertEqual(num, purchase_detail[0]['scraper'])
        self.assertEqual(num, purchase_detail[0]['motorcycle'])
        self.assertEqual(num, purchase_detail[0]['honeypot'])
        self.assertEqual(num, purchase_detail[0]['alternator'])
        self.assertEqual(num, purchase_detail[0]['solar_panel'])
        self.assertEqual(remark, purchase_detail[0]['remark'])

    def test_mobile_contract_page_list(self):
        """
        POST /mobile/contract/page-list 合同分页列表
        :return:
        """
        customer_id_list = self.purchase_db.query_customer_id()
        user_id = customer_id_list[0]['user_id']
        pn = 1
        ps = 20
        response_data = self.container._mobile_contract_page_list(pn_=pn, ps_=ps, userId_=user_id)
        list_db = self.purchase_db.query_purchase_list(customer_id=user_id, pn=pn, ps=ps)
        if response_data['status'] == "OK":
            for i in range(len(list_db)):
                self.assertEqual(response_data['content']['datas'][i]['id'], list_db[i]['id'])
                self.assertEqual(response_data['content']['datas'][i]['contractNo'], list_db[i]['contract_no'])
                self.assertEqual(response_data['content']['datas'][i]['hiveNum'], list_db[i]['hive_num'])
                # sign_time = time.localtime(response_data['content']['datas'][i]['signTime'] / 1000)
                # sign_time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", sign_time)
                # self.assertEqual(sign_time_stamp, list_db[i]['sign_time'])
                self.assertEqual(response_data['content']['datas'][i]['status'], list_db[i]['status'])
                self.assertEqual(response_data['content']['datas'][i]['amount'], list_db[i]['amount'])
                self.assertEqual(response_data['content']['datas'][i]['handsel'], list_db[i]['handsel'])

    def test_mobile_purchase_purchase_detail(self):
        """
         POST /mobile/purchase/purchase-detail
         获取采购单详情 new 1.2
        :return:
        """
        purchase_id_list = self.purchase_db.query_purchase_id()
        purchase_id = purchase_id_list[0]['id']
        response_data = self.container._mobile_contract_contract_detail(id_=purchase_id)
        if response_data['status'] == "OK":
            purchase_db_list = self.purchase_db.query_purchase_detail(purchase_id)
            self.assertEqual(response_data['content']['detailInfo']['alternator'], purchase_db_list[0]['alternator'])
            self.assertEqual(response_data['content']['detailInfo']['contractId'], purchase_db_list[0]['contract_id'])
            self.assertEqual(response_data['content']['detailInfo']['hiveNum'], purchase_db_list[0]['hive_num'])
            self.assertEqual(response_data['content']['detailInfo']['honeyMachine'], purchase_db_list[0]['honey_machine'])
            self.assertEqual(response_data['content']['detailInfo']['honeypot'], purchase_db_list[0]['honeypot'])
            self.assertEqual(response_data['content']['detailInfo']['motorcycle'], purchase_db_list[0]['motorcycle'])
            self.assertEqual(response_data['content']['detailInfo']['remark'], purchase_db_list[0]['remark'])
            self.assertEqual(response_data['content']['detailInfo']['scraper'], purchase_db_list[0]['scraper'])
            self.assertEqual(response_data['content']['detailInfo']['smallNum'], purchase_db_list[0]['small_num'])
            self.assertEqual(response_data['content']['detailInfo']['solarPanel'], purchase_db_list[0]['solar_panel'])
            self.assertEqual(response_data['content']['detailInfo']['standardNum'], purchase_db_list[0]['standard_num'])
            self.assertEqual(response_data['content']['detailInfo']['tent'], purchase_db_list[0]['tent'])
            self.assertEqual(response_data['content']['amount'], purchase_db_list[0]['amount'])
            self.assertEqual(response_data['content']['bankBack'], purchase_db_list[0]['bank_back'])
            self.assertEqual(response_data['content']['bankFront'], purchase_db_list[0]['bank_front'])
            self.assertEqual(response_data['content']['contractNo'], purchase_db_list[0]['contract_no'])
            self.assertEqual(response_data['content']['contractPics'], purchase_db_list[0]['contract_pics'])
            self.assertEqual(response_data['content']['friendId'], purchase_db_list[0]['friend_id'])
            self.assertEqual(response_data['content']['handsel'], purchase_db_list[0]['handsel'])
            self.assertEqual(response_data['content']['id'], purchase_db_list[0]['id'])
            self.assertEqual(response_data['content']['identityBack'], purchase_db_list[0]['identity_back'])
            self.assertEqual(response_data['content']['identityFront'], purchase_db_list[0]['identity_front'])
            self.assertEqual(response_data['content']['status'], purchase_db_list[0]['status'])

    def test_mobile_purchase_purchase_info(self):
        """
        POST /mobile/purchase/purchase-info
        获取采购清单详情 new 1.2
        :return:
        """
        purchase_id_list = self.purchase_db.query_purchase_id()
        purchase_id = purchase_id_list[0]['id']
        response_data = self.container._mobile_purchase_purchase_info(id_=purchase_id)
        purchase_db_list = self.purchase_db.query_purchase_detail(purchase_id=purchase_id)
        self.assertEqual(response_data['content']['alternator'], purchase_db_list[0]['alternator'])
        self.assertEqual(response_data['content']['amount'], purchase_db_list[0]['amount'])
        self.assertEqual(response_data['content']['hiveNum'], purchase_db_list[0]['hive_num'])
        self.assertEqual(response_data['content']['honeyMachine'], purchase_db_list[0]['honey_machine'])
        self.assertEqual(response_data['content']['honeypot'], purchase_db_list[0]['honeypot'])
        self.assertEqual(response_data['content']['id'], purchase_db_list[0]['customer_id'])
        self.assertEqual(response_data['content']['motorcycle'], purchase_db_list[0]['motorcycle'])
        self.assertEqual(response_data['content']['remark'], purchase_db_list[0]['remark'])
        self.assertEqual(response_data['content']['scraper'], purchase_db_list[0]['scraper'])
        self.assertEqual(response_data['content']['smallNum'], purchase_db_list[0]['small_num'])
        self.assertEqual(response_data['content']['solarPanel'], purchase_db_list[0]['solar_panel'])
        self.assertEqual(response_data['content']['standardNum'], purchase_db_list[0]['standard_num'])
        self.assertEqual(response_data['content']['tent'], purchase_db_list[0]['tent'])

    def test_mobile_contract_contract_view(self):
        """
        POST /mobile/contract/contract-view
        根据蜂友id获取展示的合同 new v1.2.1
        v2.0 传参变更
        :return:
        """
        id = 1
        response_data = self.container._mobile_contract_contract_view(userId_=477)
        self.assertEqual("OK", response_data["status"])
        # if response_data['status'] == "OK":
            # contract_db_list = self.purchase_db.sql_contract_view_by_friend_id(id)[0]
            # self.assertEqual(response_data['content']['id'], contract_db_list['id'])
            # self.assertEqual(response_data['content']['contractNo'], contract_db_list['contract_no'])
            # # sign_time = time.localtime(response_data['content']['datas'][ ]['signTime'] / 1000)
            # # sign_time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", sign_time)
            # # self.assertEqual(sign_time_stamp, list_db[ ]['sign_time'])
            # self.assertEqual(response_data['content']['status'], contract_db_list['status'])
            # self.assertEqual(response_data['content']['amount'], contract_db_list['amount'])
            # self.assertEqual(response_data['content']['handsel'], contract_db_list['handsel'])

    def test_mobile_contract_pay_off(self):
        """
        POST mobile/contract/pay-off
        移动端-合同-付清尾款  V1.2.1
        :return:
        """
        contract = random.choice(self.purchase_db.query_contract_id())
        contract_id = contract.get('id')
        contract_status = contract.get('status')
        response = self.container._mobile_contract_pay_off(id_=contract_id)
        if contract_status == 1:
            self.assertEqual(response.get('status'), 'OK')
            contract_info = self.purchase_db.query_contract_info_by_contract_id(contract_id=contract_id)
            self.assertEqual(contract_info[0]["status"], 2)
        else:
            self.assertEqual(response.get('status'), 'ERROR')
            self.assertEqual(response.get('errorMsg'), '合同已是完成状态')

    def test_mobile_contract_discard(self):
        """
        POST mobile/contract/discard
        移动端-合同-废弃合同  V1.2.1
        :return:
        """
        contract = random.choice(self.purchase_db.query_contract_id())
        contract_id = contract.get('id')
        contract_status = contract.get('status')
        response = self.container._mobile_contract_discard(id_=contract_id)
        if contract_status != 3:
            self.assertEqual(response.get('status'), 'OK')
            contract_info = self.purchase_db.query_contract_info_by_contract_id(contract_id=contract_id)
            self.assertEqual(contract_info[0]["status"], 3)
        else:
            self.assertEqual(response.get('status'), 'ERROR')
            self.assertEqual(response.get('errorMsg'), '合同已是废弃状态')
