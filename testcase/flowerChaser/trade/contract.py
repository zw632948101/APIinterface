#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2020 2020/10/06 14:22
合同管理
CREATE: heshihcao
"""
import unittest
from interfaces.flowerChaser.TradeAction import TradeAction
from utils.log import log


class Contract_auth(unittest.TestCase):
    """
    数据暂时写死
    """

    def __init__(self, methodName=None):
        super(Contract_auth, self).__init__(methodName)
        self.trad = TradeAction()
        self.trad.set_user('15882438888')


    def test_web_friend_contract_list(self):
        """
        蜂友端-合同列表
        :return:
        """
        statusList = 10
        pn = 1
        ps = 10
        sortType = 1
        result = self.trad._web_friend_contract_list(statusList_=statusList, pn_=pn, ps_=ps, sortType_=sortType)
        self.assertEqual(result['status'], 'OK', msg='接口错误')
        log.info('test_web_friend_contract_list接口测试完毕')

    def test_web_friend_contract_detail(self):
        """
        蜂友端-合同详情
        :return:
        """
        contractID = 1    #合同ID
        result = self.trad._web_friend_contract_detail(contractId_=contractID)
        self.assertEqual(result['status'], 'OK', msg='接口错误')
        log.info('test_web_friend_contract_detail接口测试完毕')

    def test_web_friend_contract_perfect(self):
        """
        蜂友端-合同信息完善
        :return:
        """
        id = 4
        realName = '萌萌站起来'
        idCardNo = 51078199604144256
        identityFront = '["http://dnkj-world-farm-prd.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1585547226152.jpg"]'
        identityBack = '["http://dnkj-world-farm-prd.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1585547226152.jpg"]'
        cardNo = 54645645464645446
        bankName = '成都市交通银行'
        branchName = '高新区支行'
        bankFront = '["http://dnkj-world-farm-prd.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1585547226152.jpg"]'
        bankBack = '["http://dnkj-world-farm-prd.oss-ap-southeast-1.aliyuncs.com/data/fc-bee/attach/1585547226152.jpg"]'
        result = self.trad._web_friend_contract_perfect(id_=id, realName_=realName, idCardNo_=idCardNo, identityFront_=identityFront,
                                                        identityBack_=identityBack, cardNo_=cardNo, bankBack_=bankBack,
                                                        bankFront_=bankFront, bankName_=bankName, branchName_=branchName)
        self.assertEqual(result['status'], 'OK', msg='接口错误')
        log.info('test_web_friend_contract_perfect接口测试完毕')

    def test_web_friend_contract_sign(self):
        """
        蜂友端-合同签字确认
        :return:
        """
        id =4
        signUrl = ''    #签名上传地址
        result = self.trad._web_friend_contract_sign(id_=id, signUrl_=signUrl)
        self.assertEqual(result['status'], 'OK', msg='接口错误')
        log.info('test_web_friend_contract_sign接口测试完毕')

    def test_web_manager_contract_check_phone(self):
        """
        管理版-合同手机号校验
        :return:
        """
        iphone = 15882438888
        result = self.trad._web_manager_contract_check_phone(phone_=iphone)
        self.assertEqual(result['status'], 'OK', msg='接口错误')
        log.info('test_web_manager_contract_check_phone接口测试完毕')

    def test_web_manager_contract_add(self):
        """
        管理版-新增合同
        :return:
        """
        userid = 18455
        realname = '萌萌站起来'
        swarmid = 18295
        signTime = '2020-09-17 17:58:33'
        expiretime = '2020-10-23 11:50:33'
        variety = 1001
        margin = 1000
        serviceFee = 20
        shippingType = 1
        result = self.trad._web_manager_contract_add(userId_=userid, realName_=realname, swarmId_=swarmid,
                                                     signTime_=signTime, expireTime_=expiretime, variety_=variety,
                                                     margin_=margin, serviceFee_=serviceFee, shippingType_=shippingType)
        self.assertEqual(result['status'], 'OK', msg='接口错误')
        log.info('test_web_manager_contract_add接口测试完毕')

    def test_web_manager_contract_varieties(self):
        """
        管理版-合同品种选择
        :return:
        """
        category = 1
        result = self.trad._web_manager_contract_varieties(category_=category)
        self.assertEqual(result['status'], 'OK', msg='接口错误')
        log.info('test_web_manager_contract_varieties接口测试完毕')

    def test_web_manager_contract_edit(self):
        """
        管理版-合同编辑
        :return:
        """
        userId = 18455
        realname = '萌萌站起来'
        swarmid = 18295
        signtime = '2020-09-17 17:58:33'
        expiretime = '2020-10-23 11:50:33'
        variety = 1001
        margin = 1000
        serviceFee = 20
        shippingType = 1
        remark = '接口测试'
        result = self.trad._web_manager_contract_edit(userId_=userId, realName_=realname, swarmId_=swarmid,
                                                      signTime_=signtime, expireTime_=expiretime, variety_=variety,
                                                      margin_=margin, serviceFee_=serviceFee, shippingType_=shippingType,
                                                      remark_=remark)
        self.assertEqual(result['status'], 'OK', msg='接口错误')
        log.info('test_web_manager_contract_edit接口测试完毕')

    def test_web_manager_contract_list(self):
        """
        管理版-合同列表
        :return:
        """
        statusList = 10
        pn = 1
        ps = 10
        sortType = 1
        result = self.trad._web_manager_contract_list(statusList_=statusList, pn_=pn, ps_=ps, sortType_=sortType)
        self.assertEqual(result['status'], 'OK', msg='接口错误')
        log.info('test_web_manager_contract_list接口测试完毕')

    def test_web_manager_contract_detail(self):
        """
        管理版-合同详情
        :return:
        """
        contractId = 100
        result = self.trad._web_manager_contract_detail(contractId_=contractId)
        self.assertEqual(result['status'], 'OK', msg='接口错误')
        log.info('test_web_manager_contract_detail接口测试完毕')

    def test_web_manager_contract_abort(self):
        """
        管理版-终止合同
        :return:
        """
        id = 100
        abortType = 1
        result = self.trad._web_manager_contract_abort(id_=id, abortType_=abortType)
        self.assertEqual(result['status'], 'OK', msg='接口错误')
        log.info('test_web_manager_contract_abort接口测试完毕')

